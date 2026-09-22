# Standalone reference handout

A two-page, US-letter reference for *Claude for Research: Beyond the Chatbot*.
Print one sheet, double-sided, flipped on the long edge. It retains the compact
front-and-back format chosen in September and gives enough context to use after
the seminar without reading the slide transcript.

## Build

From the repository root:

```bash
make -C handout
pdftoppm -png -r 150 handout/main.pdf /tmp/seminar-handout
```

`main.tex` is the editable source; `main.pdf` is a generated, Git-ignored output.
The source uses the installed LaTeX toolchain, Latin Modern fonts, and Notre Dame
navy/gold. No additional images or downloaded assets are needed.

## Contents

- Page 1: the inspect/save/change/check/handoff cycle, project artifacts, and
  the two-session route with the approved 35/10/45/15-minute budget.
- Page 2: how to audit a claim, a generic worked example unrelated to the CSTR
  exercise, a reusable prompt, a stopping checklist, and repository resources.

The September plan included a compact tool-approval table. This edition instead
points readers to `notes/references.md` for current institutional and sponsor
sources, avoiding an undated policy snapshot on a printed reference. Full
literature, package-release, and manuscript workflows remain in
[the companion resources](../resources/README.md).

Both pages were rendered and visually reviewed. The final build has no
LaTeX overfull/underfull-box warnings. Re-render both pages after changing text.
