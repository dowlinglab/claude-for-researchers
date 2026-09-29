# Working on a different machine

What to set up to build and check this repository. None of it is inferable from the layout.

## Building the PDFs

You need a TeX Live installation with `latexmk`, plus `make`. From the repository root:

```bash
make -C slides    # part1_slides.pdf and part2_slides.pdf
make -C handout   # part1_handout.pdf and part2_handout.pdf
```

The [release workflow](../.github/workflows/release.yml) runs the same two commands in a TeX Live container, so a build that works there works from a clean checkout.

## The optional report

The reactor report in `resources/workshops/cstr/report/` builds with `latexmk -pdf report.tex` (and `audit_fallback.tex`) from that directory.

## The conda environment is per-machine

`cstr-workshop` is defined in the Part 1 starter and exists only where it has been built. Nothing tells you it is missing until a test run fails in a confusing way:

```bash
conda env create -f resources/workshops/cstr/environment.yml
conda activate cstr-workshop
```

Budget 3 to 8 minutes, longer on a cold package cache.

## Before calling a slide done

Render it and look at it, as [`slides/style_guide.md`](../slides/style_guide.md) requires. A frame can compile cleanly and still come out visually wrong. `python3 slides/check_layout.py` flags top-empty and bottom-crowded frames but does not replace looking. `python3 resources/scripts/check_docs.py` checks documentation links.
