#!/usr/bin/env python3
"""Verify the DOIs in a BibTeX file against Crossref.

Two questions, kept separate because they have different failure modes:

  1. For entries that HAVE a DOI: does it resolve, and does it resolve to the work
     the entry describes? A DOI that resolves to a different paper is far worse
     than a missing one, and looks identical to a correct one on the page.
  2. For entries that have NO DOI: does Crossref know of one? Only proposed when
     the returned record matches unambiguously. Never guessed.

This script REPORTS. It never edits your bibliography. Apply proposed DOIs by
hand after checking the returned title, authors, year and venue -- an automated
"fix" here is precisely the failure mode the script exists to catch.

Usage
-----
    python check_dois.py refs.bib --mailto you@example.edu

    # only check keys actually cited in the manuscript
    python check_dois.py refs.bib --mailto you@example.edu \
        --tex main.tex sections/*.tex

    # machine-readable output, and a non-zero exit code for CI
    python check_dois.py refs.bib --mailto you@example.edu \
        --json doi_results.json

Exit status is 1 if any entry is UNRESOLVED or MISMATCH, so this can gate a
commit or a CI job. CHECK results do not fail the run -- they need a human.

Requires network access and the Python standard library. Nothing else.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CROSSREF_WORK = "https://api.crossref.org/works/{doi}"
CROSSREF_QUERY = (
    "https://api.crossref.org/works"
    "?rows=3&select=DOI,title,author,type,issued,container-title"
    "&query.bibliographic={q}"
)


# --------------------------------------------------------------------------- #
# Crossref access
# --------------------------------------------------------------------------- #

def fetch(url: str, user_agent: str, timeout: int = 25):
    """One Crossref request. Returns parsed JSON, or None on any failure.

    Failures are deliberately swallowed and reported as "unresolved" rather than
    raised: a flaky network should degrade the report, not abort a run that has
    already made fifty successful requests.
    """
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
            json.JSONDecodeError, UnicodeDecodeError, OSError):
        return None


# --------------------------------------------------------------------------- #
# BibTeX parsing
#
# Brace-counting rather than regex throughout. Titles routinely contain nested
# braces ({CO$_2$} {Capture}), and a regex that stops at the first closing brace
# truncates the entry to its title -- silently, and in a way that makes every
# comparison downstream look like a mismatch.
# --------------------------------------------------------------------------- #

def parse_bib(path: str) -> dict:
    """Split a .bib file into {key: {"kind": str, "raw": str}}."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        src = fh.read()

    entries = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", src):
        kind, key = m.group(1).lower(), m.group(2)
        if kind in {"comment", "preamble", "string"}:
            continue
        # Start the walk at the entry's own opening brace, which sits between
        # "@article" and the key -- not at the end of the match, which is past
        # it. Starting late closes the walk on the first FIELD's brace.
        i = src.index("{", m.start())
        depth = 0
        while i < len(src):
            if src[i] == "{":
                depth += 1
            elif src[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        entries[key] = {"kind": kind, "raw": src[m.start():i + 1]}
    return entries


def field(raw: str, name: str):
    """Value of one bib field. Handles {..}, "..", and bare values."""
    m = re.search(rf"[,{{]\s*{name}\s*=\s*", raw, re.I)
    if not m:
        return None
    i = m.end()
    if i >= len(raw):
        return None
    if raw[i] == "{":
        depth, j = 0, i
        while j < len(raw):
            if raw[j] == "{":
                depth += 1
            elif raw[j] == "}":
                depth -= 1
                if depth == 0:
                    return raw[i + 1:j].strip()
            j += 1
        return None
    if raw[i] == '"':
        j = raw.find('"', i + 1)
        return raw[i + 1:j].strip() if j > 0 else None
    return raw[i:].split(",")[0].strip()


def cited_keys(tex_paths) -> set:
    """Citation keys actually used in the given .tex files."""
    keys = set()
    pattern = re.compile(r"\\[a-zA-Z]*cite[a-zA-Z]*\*?\s*(?:\[[^\]]*\]){0,2}\s*\{([^}]*)\}")
    for path in tex_paths:
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)
            continue
        for m in pattern.finditer(text):
            keys.update(k.strip() for k in m.group(1).split(","))
    return {k for k in keys if k}


# --------------------------------------------------------------------------- #
# Comparison
# --------------------------------------------------------------------------- #

def norm(s) -> str:
    """Normalise a title for comparison: strip LaTeX, punctuation, case, spacing."""
    if not s:
        return ""
    s = re.sub(r"\\[a-zA-Z]+\s*", " ", s)
    s = re.sub(r"[{}$\\]", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return " ".join(s.split())


def cr_title(msg) -> str:
    t = msg.get("title") or []
    return t[0] if t else ""


def cr_first_author(msg) -> str:
    for a in msg.get("author") or []:
        if a.get("family"):
            return a["family"]
    return ""


def bib_first_author(raw: str) -> str:
    a = re.sub(r"[{}\\]", "", field(raw, "author") or "")
    first = a.split(" and ")[0].strip()
    if "," in first:
        return first.split(",")[0].strip()
    return first.split()[-1] if first.split() else ""


def normalise_doi(doi: str) -> str:
    return re.sub(r"^(https?://(dx\.)?doi\.org/)", "", doi.strip(), flags=re.I)


def verdict_for(ratio: float, author_ok: bool, match_at: float, check_at: float) -> str:
    if ratio >= match_at and author_ok:
        return "MATCH"
    if ratio >= check_at:
        return "CHECK"
    return "MISMATCH"


# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Verify BibTeX DOIs against Crossref. Reports only; never edits.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("bib", help="path to the .bib file")
    p.add_argument("--mailto", required=True,
                   help="your email, sent in the User-Agent per Crossref's "
                        "polite-pool etiquette. Required.")
    p.add_argument("--tex", nargs="*", default=[],
                   help="manuscript .tex files; if given, only keys cited in "
                        "them are checked")
    p.add_argument("--json", dest="json_out", default=None,
                   help="also write machine-readable results here")
    p.add_argument("--match-at", type=float, default=0.90,
                   help="title similarity at or above which a resolved DOI is a "
                        "MATCH (default 0.90)")
    p.add_argument("--check-at", type=float, default=0.55,
                   help="title similarity below which it is a MISMATCH rather "
                        "than a CHECK (default 0.55)")
    p.add_argument("--propose-at", type=float, default=0.92,
                   help="similarity required to propose a DOI for an entry that "
                        "lacks one. Deliberately stricter than --match-at "
                        "(default 0.92)")
    p.add_argument("--sleep", type=float, default=0.12,
                   help="seconds between requests (default 0.12)")
    args = p.parse_args(argv)

    user_agent = f"doi-checker/1.0 (mailto:{args.mailto})"

    try:
        bib = parse_bib(args.bib)
    except OSError as exc:
        print(f"error: cannot read {args.bib}: {exc}", file=sys.stderr)
        return 2
    if not bib:
        print(f"error: no entries parsed from {args.bib}", file=sys.stderr)
        return 2

    if args.tex:
        cited = cited_keys(args.tex)
        missing = sorted(cited - set(bib))
        keys = sorted(cited & set(bib))
        print(f"cited keys: {len(cited)}   present in bib: {len(keys)}   "
              f"bib entries total: {len(bib)}")
        if missing:
            print(f"!! cited but NOT in the bib: {missing}")
        print(f"uncited bib entries: {len(set(bib) - cited)}")
    else:
        keys = sorted(bib)
        print(f"checking all {len(keys)} bib entries "
              f"(pass --tex to restrict to cited keys)")
    print()

    have, lack = [], []
    for k in keys:
        raw = bib[k]["raw"]
        doi = field(raw, "doi")
        (have if doi else lack).append((k, raw, normalise_doi(doi) if doi else None))

    print(f"entries WITH a doi field: {len(have)}")
    print(f"entries WITHOUT one:      {len(lack)}")
    print()

    # ---- Part 1: do the DOIs we have resolve to the right work? ----------- #
    print("=" * 78)
    print("PART 1 -- entries that have a DOI: does it resolve, and to the right work?")
    print("=" * 78)
    rows = []
    for k, raw, doi in have:
        title = field(raw, "title")
        j = fetch(CROSSREF_WORK.format(doi=urllib.parse.quote(doi)), user_agent)
        time.sleep(args.sleep)
        if not j or j.get("status") != "ok":
            rows.append({"key": k, "doi": doi, "verdict": "UNRESOLVED",
                         "crossref_title": "", "ratio": 0.0})
            print(f"UNRESOLVED  {k:28s} {doi}")
            continue
        msg = j["message"]
        ratio = difflib.SequenceMatcher(None, norm(cr_title(msg)), norm(title)).ratio()
        fam_bib, fam_cr = norm(bib_first_author(raw)), norm(cr_first_author(msg))
        author_ok = (not fam_bib) or (not fam_cr) or fam_bib in fam_cr or fam_cr in fam_bib
        v = verdict_for(ratio, author_ok, args.match_at, args.check_at)
        rows.append({"key": k, "doi": doi, "verdict": v,
                     "crossref_title": cr_title(msg), "ratio": round(ratio, 4)})
        if v != "MATCH":
            print(f"{v:10s}  {k:28s} {doi}")
            print(f"{'':12s}bib : {title}")
            print(f"{'':12s}cr  : {cr_title(msg)}")
            print(f"{'':12s}ratio {ratio:.2f}   first author bib={fam_bib!r} cr={fam_cr!r}")
    n_match = sum(1 for r in rows if r["verdict"] == "MATCH")
    print(f"\n  {n_match} of {len(have)} verified as MATCH")

    # ---- Part 2: can Crossref supply the missing ones? -------------------- #
    print()
    print("=" * 78)
    print("PART 2 -- entries with no DOI: does Crossref have one?")
    print("=" * 78)
    found = []
    for k, raw, _ in lack:
        title = field(raw, "title")
        kind = bib[k]["kind"]
        if not title:
            print(f"NO TITLE    {k:28s} ({kind}) -- cannot search")
            continue
        q = re.sub(r"[{}\\$]", "", title)
        author = bib_first_author(raw)
        if author:
            q = f"{q} {author}"
        j = fetch(CROSSREF_QUERY.format(q=urllib.parse.quote_plus(q)), user_agent)
        time.sleep(args.sleep)
        items = ((j or {}).get("message") or {}).get("items") or []
        best, best_r = None, 0.0
        for it in items:
            r = difflib.SequenceMatcher(None, norm(cr_title(it)), norm(title)).ratio()
            if r > best_r:
                best, best_r = it, r
        if best and best_r >= args.propose_at:
            found.append({"key": k, "doi": best["DOI"],
                          "crossref_title": cr_title(best), "ratio": round(best_r, 4)})
            print(f"FOUND {best_r:.2f}  {k:28s} ({kind})  {best['DOI']}")
            print(f"{'':12s}bib : {title}")
            print(f"{'':12s}cr  : {cr_title(best)}")
        else:
            note = f"best {best_r:.2f}" if best else "no candidate"
            print(f"none        {k:28s} ({kind})  {note}")
    print(f"\n  {len(found)} DOIs proposed for the {len(lack)} entries without one")
    if found:
        print("  These are PROPOSALS. Check the title, authors, year and venue,")
        print("  then add them by hand. This script does not edit your .bib.")

    # ---- Summary and exit status ----------------------------------------- #
    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print()
    print("summary: " + ("  ".join(f"{v}={n}" for v, n in sorted(counts.items()))
                         or "nothing checked"))

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"verified": rows, "proposed": found}, fh, indent=1)
        print(f"wrote {args.json_out}")

    bad = counts.get("UNRESOLVED", 0) + counts.get("MISMATCH", 0)
    if bad:
        print(f"\nFAIL: {bad} entr{'y' if bad == 1 else 'ies'} unresolved or mismatched")
        return 1
    if counts.get("CHECK"):
        print(f"\nPASS with {counts['CHECK']} entr"
              f"{'y' if counts['CHECK'] == 1 else 'ies'} needing a human look")
    return 0


if __name__ == "__main__":
    sys.exit(main())
