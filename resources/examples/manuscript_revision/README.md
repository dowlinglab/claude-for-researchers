# A small manuscript revision you can inspect

These two short LaTeX documents are illustrative, not research results. They demonstrate a qualification added to a claim and a corrected percentage. The presentation displays actual `latexdiff` output generated from them.

From the repository root, with TeX and `latexdiff` installed:

```bash
mkdir -p /tmp/manuscript-revision-demo
latexdiff resources/examples/manuscript_revision/before.tex \
  resources/examples/manuscript_revision/after.tex \
  > /tmp/manuscript-revision-demo/diff.tex
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/manuscript-revision-demo \
  /tmp/manuscript-revision-demo/diff.tex
```

Open `/tmp/manuscript-revision-demo/diff.pdf`. Removed words are struck through; additions are marked. Ask an agent to explain what evidence would justify each revision. The markup reveals the change; it does not establish whether the new statement is true.

The deck asset is `slides/figures/manuscript_diff.pdf`, copied from this build. For a real manuscript comparison against Git history, use [the tracked-changes script](../../scripts/latexdiff_check.sh).
