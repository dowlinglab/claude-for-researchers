# Working on a different machine

Written 2026-09-24, when the project moved off the laptop it was built on. Every
item here cost time to rediscover once; none of it is inferable from the
repository layout.

## The two checkouts

| Repository | Path on the 2026-09 laptop | Visibility |
|---|---|---|
| `claude-for-researchers` | `~/GitHub/Teaching/claude-for-researchers` | Public |
| `claude-for-researchers-private` | `~/GitHub/DowlingLab/Teaching/claude-for-researchers-private` | Private |

**They are not siblings**, and several tools originally assumed they were.
Since 2026-09-28 no private tool guesses. Tell the private checkout where the
public one is, once per machine:

```bash
cd /path/to/claude-for-researchers-private
echo /path/to/claude-for-researchers > .public_root     # git-ignored
```

Every private tool — the release checks, the pytest fixtures, the solution
runner, and both instructor-deck builds — reads it through
`scripts/public_root.py`. An explicit argument or `PUBLIC_ROOT` still takes
precedence. If none of them points at a public checkout, the tool stops and
prints the command above.

The public docs check takes its path directly:

```bash
python /path/to/claude-for-researchers/resources/scripts/check_docs.py /path/to/claude-for-researchers
```

## The conda environment is per-machine

`cstr-workshop` is defined in the public starter and exists only where it has
been built. Nothing in either repository will tell you it is missing until a
test run fails in a confusing way. Build it first:

```bash
conda env create -f resources/workshops/cstr/environment.yml
conda activate cstr-workshop
pip install -e reference_implementation          # from the private repo
```

Budget 3–8 minutes, longer on a cold package cache. This is also the single
largest setup cost for participants. The preparation list asks participants to
install Miniconda if needed; the activity creates its environment in the room.

## Building the PDFs

From the public repository:

```bash
make -C slides   # part1_slides.pdf and part2_slides.pdf
make -C handout  # part1_handout.pdf and part2_handout.pdf, two pages each
```

Two documents do **not** build with a bare `latexmk`, and both failures are
quiet:

1. **`resources/workshops/cstr/report/audit_fallback.tex`** needs an explicit
   BibTeX pass or `woolf2009cstr` stays undefined. There is no `Makefile` in
   that directory.

   ```bash
   cd resources/workshops/cstr/report
   pdflatex audit_fallback.tex && bibtex audit_fallback
   pdflatex audit_fallback.tex && pdflatex audit_fallback.tex
   ```

   Worth fixing with a small `Makefile` before building it in front of anyone.

2. **`activity_answers/02_evidence_linked_report/reference_report.tex`** (private)
   is not a self-contained LaTeX project. Copy the public `ref.bib` alongside it
   and build in a scratch directory, so nothing untracked is left in the private
   repository:

   ```bash
   cp resources/workshops/cstr/report/ref.bib /tmp/refrep/
   ```

The private instructor decks need the public slide sources and theme. Their
`Makefile` handles both, finding the public checkout from `.public_root`.

## Before calling a slide done

`slides/style_guide.md` rule 10: render it and look at it. A frame compiles
clean and still comes out visually wrong. `python3 slides/check_layout.py`
flags top-empty/bottom-crowded frames but does not replace looking.

## Before any release

Run all five private checks (see the private `README.md`). They detect different
things and the overlap is small. `scripts/check_public_boundary.sh` is the one
that must never be skipped — it greps the public tree *and all reachable public
history* for answer markers.

**Neither repository may be pushed without Alex's approval.**
