# Working on a different machine

Written 2026-09-24, when the project moved off the laptop it was built on. Every
item here cost time to rediscover once; none of it is inferable from the
repository layout.

## The two checkouts

| Repository | Path on the 2026-09 laptop | Visibility |
|---|---|---|
| `claude-for-researchers` | `~/GitHub/Teaching/claude-for-researchers` | Public |
| `claude-for-researchers-private` | `~/GitHub/DowlingLab/Teaching/claude-for-researchers-private` | Private |

**They are not siblings**, and several tools originally assumed they were. The
private release checks and the regroup deck now take an explicit path to the
public checkout; pass it rather than moving either repository:

```bash
make PUBLIC_ROOT=/path/to/claude-for-researchers
python ../claude-for-researchers/resources/scripts/check_docs.py ../claude-for-researchers
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
largest setup cost for participants, which is why the announcement asks them to
do it in advance.

## Building the PDFs

From the public repository:

```bash
make -C slides            # part1.pdf (27 frames) and part2.pdf (31 frames)
make -C slides combined   # main.pdf, both parts in one 58-frame sequence
make -C handout           # main.pdf, the two-page reference
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

The private regroup deck needs the public theme on `TEXINPUTS`, which its
`Makefile` handles given `PUBLIC_ROOT`.

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
