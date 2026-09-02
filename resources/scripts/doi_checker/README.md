# DOI checker

Verifies the DOIs in a BibTeX file against [Crossref](https://www.crossref.org/), and offers DOIs for entries that lack them.

**It reports. It never edits your bibliography.** That restraint is the whole point: a DOI that resolves to the *wrong* paper is worse than a missing one and looks identical on the page, so an automated "fix" would introduce exactly the error the tool exists to catch.

## Install

Nothing to install. Python 3.8+, standard library only, network access required.

```bash
python check_dois.py refs.bib --mailto you@example.edu
```

## Usage

```bash
# check every entry in the file
python check_dois.py refs.bib --mailto you@example.edu

# check only the keys actually cited in the manuscript
python check_dois.py refs.bib --mailto you@example.edu \
    --tex main.tex sections/*.tex

# save a report and machine-readable results
python check_dois.py refs.bib --mailto you@example.edu \
    --tex main.tex --json doi_results.json > doi_report.txt
```

`--mailto` is required. Crossref asks API users to identify themselves, and doing so puts you in their faster "polite pool" — it is courtesy that also happens to be in your interest.

## What it checks

Two passes, kept separate **because they fail differently**:

**Part 1 — entries that have a DOI.** Does it resolve, and does it resolve to the work the entry describes? The title from Crossref is compared to the title in your `.bib` (LaTeX stripped, punctuation and case normalised), and the first author's surname must be consistent.

| Verdict | Meaning |
|---|---|
| `MATCH` | Resolves, title similarity ≥ 0.90, author consistent |
| `CHECK` | Resolves, similarity 0.55–0.90 — a human needs to look |
| `MISMATCH` | Resolves to something else entirely |
| `UNRESOLVED` | Crossref does not know this DOI |

**Part 2 — entries with no DOI.** Searches Crossref by title and first author, and proposes a DOI only when the best match is ≥ 0.92 — deliberately stricter than the verification threshold, because proposing a wrong DOI is worse than proposing none.

## Exit status

- `0` — no unresolved or mismatched entries (`CHECK` results do not fail the run)
- `1` — at least one `UNRESOLVED` or `MISMATCH`
- `2` — could not read or parse the `.bib`

So it can gate a commit hook or a CI job:

```yaml
- run: python check_dois.py refs.bib --mailto ${{ secrets.CONTACT_EMAIL }} --tex main.tex
```

## Options

| Flag | Default | What it does |
|---|---|---|
| `--tex FILE...` | — | Restrict to keys cited in these files |
| `--json PATH` | — | Write structured results |
| `--match-at` | 0.90 | Similarity for `MATCH` |
| `--check-at` | 0.55 | Below this, `MISMATCH` rather than `CHECK` |
| `--propose-at` | 0.92 | Similarity required to propose a missing DOI |
| `--sleep` | 0.12 | Seconds between requests |

## Notes on the implementation

- **The BibTeX parser counts braces rather than matching a regex.** Titles routinely contain nested braces (`{CO$_2$} {Capture}`), and a regex that stops at the first `}` truncates the entry to its title — silently, and in a way that makes everything downstream look like a mismatch. This was a real bug in an earlier version.
- **Network failures degrade the report; they do not abort the run.** A request that fails is reported as `UNRESOLVED`, so a flaky connection does not throw away fifty successful lookups.
- **Crossref responses are treated as data**, never as instructions and never as ground truth. The tool tells you what Crossref said; you decide.

## What it does not do

- It does not check whether a reference is cited *for the right claim*. That needs a human or an audit pass — see [`../../practices/manuscript_audit.md`](../../practices/manuscript_audit.md) §12.
- It does not validate non-Crossref identifiers (arXiv IDs, ISBNs, dataset DOIs from some registries).
- It does not check that you have read the paper. Nothing can.
