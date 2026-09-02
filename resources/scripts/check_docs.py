#!/usr/bin/env python3
"""Catch documentation that has quietly gone wrong.

Three checks, all cheap, all things that go unnoticed until someone acts on a
stale instruction:

  1. **Broken internal links.** A markdown link to a file that does not exist.
     Documents routinely cite a plan or a notes file that was renamed, moved, or
     never committed -- and the citation looks authoritative either way.
  2. **Stale living documents.** A file that claims to describe the current state
     but has not been touched while the repository moved underneath it.
  3. **Dangling supersession banners.** "This file is superseded by X" where X
     does not exist.

The point is not that these are hard to notice. It is that written instructions
degrade, and a rule you actually need enforced has to have something that fails.
See practices/working_with_ai_agents.md §3 and §9.

Usage
-----
    python check_docs.py                         # check the repo you are in
    python check_docs.py docs/ notes/            # only these paths
    python check_docs.py --living PROJECT.md CLAUDE.md --stale-commits 20

Exit status is 1 if anything is flagged, so it can gate a commit or a CI job.
Standard library only; git is used when available and skipped when not.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# [text](target) -- ignore images, anchors, and anything with a scheme.
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(\s*([^)\s#]+)[^)]*\)")
# A banner declaring THIS document superseded -- not prose that merely uses the
# word. Matching bare "supersed" flags sentences like "superseding the earlier
# version of this section", and a check that cries wolf gets switched off.
SUPERSEDED = re.compile(
    r"superseded\s+by\b"           # "superseded by `x.md`"
    r"|\bis\s+superseded\b"        # "this file is superseded"
    r"|^\s*[>*_\s]*\**\s*superseded\b",  # "**Superseded.** Do not source ..."
    re.I,
)
BACKTICKED = re.compile(r"`([^`]+)`")

DEFAULT_LIVING = ["PROJECT.md", "CLAUDE.md", "AGENTS.md", "RESUME_HERE.md"]
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "build",
             "dist", ".mypy_cache", ".pytest_cache"}


def git(*args, cwd="."):
    """Run a git command; return stdout, or None if git is unavailable."""
    try:
        r = subprocess.run(["git", "-C", cwd, *args], capture_output=True,
                           text=True, timeout=15)
        return r.stdout.strip() if r.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def markdown_files(roots):
    for root in roots:
        if os.path.isfile(root):
            yield root
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in sorted(filenames):
                if name.lower().endswith((".md", ".markdown")):
                    yield os.path.join(dirpath, name)


def check_links(path, text, repo_root):
    """Markdown links pointing at files that do not exist."""
    problems = []
    base = os.path.dirname(path)
    for m in LINK.finditer(text):
        target = m.group(1).strip()
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
            continue  # http:, mailto:, etc.
        target = target.split("#", 1)[0]
        if not target:
            continue
        candidate = os.path.normpath(os.path.join(base, target))
        if os.path.exists(candidate):
            continue
        # Also allow repo-root-relative links written with a leading slash.
        if target.startswith("/") and os.path.exists(
                os.path.normpath(os.path.join(repo_root, target.lstrip("/")))):
            continue
        line = text[:m.start()].count("\n") + 1
        problems.append((line, f"broken link -> {target}"))
    return problems


def check_supersession(path, text):
    """A supersession banner naming a file that does not exist."""
    problems = []
    base = os.path.dirname(path)
    for i, line in enumerate(text.splitlines()[:40], start=1):
        if not SUPERSEDED.search(line):
            continue
        named = [t for t in BACKTICKED.findall(line)
                 if "/" in t or t.lower().endswith((".md", ".py", ".tex", ".csv"))]
        if not named:
            problems.append((i, "supersession banner names no successor file"))
            continue
        for target in named:
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                problems.append((i, f"supersession banner points at missing `{target}`"))
    return problems


def check_staleness(path, repo_root, stale_commits):
    """A living document the repository has moved past."""
    last_doc = git("rev-list", "-1", "HEAD", "--", path, cwd=repo_root)
    if not last_doc:
        return [(1, "living document is not committed, so staleness cannot be judged")]
    behind = git("rev-list", "--count", f"{last_doc}..HEAD", cwd=repo_root)
    if behind is None:
        return []
    behind = int(behind)
    if behind > stale_commits:
        when = git("show", "-s", "--format=%ad", "--date=short", last_doc, cwd=repo_root)
        return [(1, f"living document last updated {when} and is {behind} commits "
                    f"behind HEAD; confirm it still describes the current state")]
    return []


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("paths", nargs="*", default=["."],
                   help="files or directories to check (default: the whole repo)")
    p.add_argument("--living", nargs="*", default=None,
                   help=f"documents that must be current "
                        f"(default: {' '.join(DEFAULT_LIVING)} where present)")
    p.add_argument("--stale-commits", type=int, default=25,
                   help="flag a living document this many commits behind HEAD "
                        "(default 25)")
    p.add_argument("--no-staleness", action="store_true",
                   help="skip the staleness check")
    args = p.parse_args(argv)

    repo_root = git("rev-parse", "--show-toplevel") or "."
    paths = args.paths or ["."]

    findings = {}
    for path in markdown_files(paths):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError as exc:
            findings[path] = [(1, f"unreadable: {exc}")]
            continue
        issues = check_links(path, text, repo_root) + check_supersession(path, text)
        if issues:
            findings.setdefault(path, []).extend(issues)

    if not args.no_staleness:
        living = args.living if args.living is not None else [
            f for f in DEFAULT_LIVING if os.path.exists(f)
        ]
        for path in living:
            if not os.path.exists(path):
                findings.setdefault(path, []).append((1, "listed as living but missing"))
                continue
            issues = check_staleness(path, repo_root, args.stale_commits)
            if issues:
                findings.setdefault(path, []).extend(issues)

    if not findings:
        print("check_docs: no issues found")
        return 0

    total = 0
    for path in sorted(findings):
        print(f"\n{path}")
        for line, msg in sorted(findings[path]):
            print(f"  {line}: {msg}")
            total += 1
    print(f"\ncheck_docs: {total} issue(s) in {len(findings)} file(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
