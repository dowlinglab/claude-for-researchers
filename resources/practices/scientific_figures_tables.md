# Scientific Figures and Tables

**What this is.** Standards for figures and tables, and — the part that is usually missing — how to make them **reproducible and traceable**, so that six months later you can say which script, which data, and which commit produced each panel.

**When to reach for it.** When you start making figures for a paper, when you inherit a figure set you didn't produce, and before submission.

**How to read it.** §2 is the quality standard; §3–§5 are about reproducibility; §6–§7 cover tables, which are usually treated as an afterthought and shouldn't be. Sections are numbered and stable for citing in a prompt.

> **Note.** If your group already publishes figure guidelines, those are canonical for content and aesthetics — this file consolidates them and adds the reproducibility layer. Fill in the pointer to your group's version here.

---

## 1. Sketch before you plot

Draw the figure on paper or a whiteboard before opening a plotting library. Decide what the reader should conclude from it, then choose the chart that makes that conclusion visible.

This sounds precious and saves hours. The alternative — plotting what is convenient and then discovering what it shows — produces figure sets where every panel is defensible and the set as a whole makes no argument.

**Every figure answers one question.** If you cannot write the caption's first sentence before plotting, you do not yet know what the figure is for.

## 2. The quality checklist

Work through these before a figure is final.

**Story and structure**
- Does every panel earn its place? A panel that supports no claim in the text is clutter.
- Is the ordering of panels the order the reader needs them in?
- Does the figure make its point without the caption, and does the caption stand alone without the text?

**Scientific correctness**
- Are units stated on every axis and in every legend entry?
- Do error bars have a stated meaning — standard deviation, standard error, confidence interval, and over what?
- Are axis ranges honest? A truncated axis that exaggerates a difference is a claim, and it needs to be a deliberate one.
- Do the plotted values match the underlying results file (§5)?

**Chart choice and data presentation**
- Is the chart type appropriate to the data — and not just the default?
- Are you showing the data, or a summary that hides its structure? Overlay the points when there are few enough.
- Are comparisons on shared axes when the reader is meant to compare them?

**Readability**
- Legible at final printed size — check it at that size, not zoomed in on a monitor.
- Font sizes consistent across panels and comparable to the body text.
- No unexplained abbreviations in labels.

**Accessibility**
- Understandable in grayscale.
- Distinguishable by a colorblind reader — do not rely on red/green alone; combine color with marker or line style.
- Sufficient contrast between series and background.

**Consistency**
- The same quantity uses the same color, marker, and label everywhere it appears.
- Notation in the figure matches notation in the text exactly.
- One style across the whole paper, not per-panel improvisation (§3).

**Captions**
- States what is plotted, under what conditions, with what uncertainty.
- Defines any symbol or abbreviation appearing only in the figure.
- Does not simply restate the axis labels.

## 3. Fix conventions centrally, once

Put figure styling in **one module** that every plotting script imports — fonts, sizes, colors, marker cycles, grid behavior, and a `save_fig` helper that enforces dimensions, resolution, and format.

The reason is not tidiness. Two independent projects learned the same lesson: once plot styling is scattered across dozens of scripts, **any later standard becomes unenforceable**, and a compliance fix has to be made in dozens of places or not at all. Centralizing turns "update every figure to the new guideline" into a one-line change that everything inherits.

A useful shape:

- one `save_fig(fig, name, ...)` that enforces size and DPI and writes to a known location — and validates *both* dimensions, not just width
- a small set of helpers for the plot types you actually repeat
- no aesthetic decisions in analysis scripts

A working default lives in `resources/scripts/figure_style/`.

## 4. Separate compute from plotting

Restyling a figure should never trigger a recomputation, and regenerating results should never require opening a plotting script.

Split into two stages: a compute step that writes results to disk (CSV, JSON, whatever), and a plotting step that reads only from those files. In practice this means:

- figure iteration becomes seconds instead of hours
- the plotted data is inspectable independently of the plot
- someone can rebuild a figure without rerunning your model
- a change in a figure can be attributed to the styling or to the data, never ambiguously to both

This is the same discipline as `scientific_computing_workflow.md` §8, and it is what makes §5 possible.

## 5. Figure provenance: which script, which data, which commit

**The failure mode is specific and common:** figures are generated in a results directory that records the configuration, then *copied* into the manuscript as bare image files. The provenance existed and the copy step destroyed it. Nothing in the manuscript repository then says which run produced `figure_3.pdf`.

Fix it by recording provenance where the figure lands:

- **Keep a figure manifest** — one row per final figure: figure number, generating script, input data file(s), configuration, code commit, output filename. This is the artifact a reviewer, a coauthor, or you-in-six-months actually needs. Template: `resources/templates/results_manifest.md`.
- **Encode the configuration in the staged path** (`results/config_name/figure_3.pdf`) so a figure's provenance is visible before you open anything.
- **Never hand-edit a final figure.** A cropped or annotated PDF that cannot be regenerated is a dead end. If annotation is needed, do it in the plotting script.
- **Make figures independent of the bibliography.** Reference numbers baked into a figure image become wrong the moment citations are renumbered. Label series A–E and map them in the caption — the option that cannot rot again.
- **Pre-empt the false reproduction failure.** Rebuilt PDFs embed a creation timestamp, so `git status` shows them as modified even when the content is identical. Say so in the README; otherwise someone will report a reproducibility bug that isn't one.

A useful standard to hold a project to, from a group checklist: *the figure package is organized so that a future group member can determine which script, data, or notebook generated each final panel.*

## 6. Tables: regenerate, never retype

**Any table that appears both in a results file and in the manuscript must be generated from that results file by a script.** Not copied. Not retyped. Not "carefully checked."

The generating script should **only format** — no computation, no filtering, no hidden state. If the script computes anything, then there are two implementations of your result and they will eventually disagree.

Why this is non-negotiable: hand transcription of tables produces exactly the errors that are hardest to catch, because the number is plausible, appears once, and matches nothing that would flag it. A single digit transposed between a results file and a manuscript table can survive every read-through and reach print.

Two reinforcing practices:

- **Tie documented tables to a test.** If your documentation or supplement contains a table of computed values, have a test parse that table and assert every cell against a live computation. Documentation that can silently go stale is the default failure mode of generated content.
- **Don't duplicate table values in prose.** If a number must appear in both, generate both from the same source, or reference the table rather than restating the value.

## 7. Table conventions

- **Units in the column header**, not repeated in every cell.
- **Significant figures reflect precision, not float output.** Three digits because you can defend three, not because that is what printed.
- **Consistent alignment** — decimal-aligned numbers, left-aligned text.
- **Caption above the table** (convention in most venues), and it states what varies across rows and columns.
- **Notation matches the text exactly**, including subscripts and case.
- **No empty cells without a meaning.** Use an explicit marker and define it — a blank cell is ambiguous between "zero," "not measured," and "not applicable."
- **Every value traceable** to a results file, like any other quantitative claim (`manuscript_audit.md` §4).

## 8. Verify that figures changed for the right reason

When you restyle or regenerate a figure set, you need to know whether the *data* moved or only the presentation. Two instruments, each blind where the other sees:

- **A data-level comparison** — extract what a figure plots (vertex arrays, bar geometry, axis limits, label text) and compare across versions. This is blind to color, font, and marker size, which is exactly what you want when checking a restyle.
- **A pixel-level comparison** — render both and diff the images. This catches styling changes and layout breaks, and it is blind to whether the underlying numbers moved.

State what each cannot see, and never report a clean result from one as "verified" (`scientific_computing_workflow.md` §6). Two known traps: a comparison that reports "identical" by default when the two figures have different shapes, and contour or region plots that a data-level instrument records as a single degenerate entry — those need a human eye.

## 9. Working with an assistant on figures

- **Give it the style module, not aesthetic instructions.** "Use `figure_style.save_fig` and the standard palette" beats a paragraph describing what you want, and it stays consistent across sessions.
- **Ask for compliance audits against the checklist**, one figure at a time, with the rule cited for each violation. This is the cheapest high-value use of an assistant on a figure set.
- **Fix violations centrally.** When an audit finds a systematic problem — font too small, colors not colorblind-safe — the fix goes in the style module so future figures inherit it, not into each script.
- **Know the limitation.** Assistants are strong on numerical results and weak at looking at a plot. Anything that requires seeing whether a fit is bad, whether residuals are structured, or whether a panel is visually confusing still needs your eyes. Explore graphically yourself; use the assistant for consistency, compliance, and provenance.

---

## Checklist

**Per figure**

- [ ] Answers one question, stated in the caption's first sentence
- [ ] Units on every axis and legend entry; error bars have a stated meaning
- [ ] Legible at final printed size; readable in grayscale and colorblind-safe
- [ ] Notation and colors consistent with every other figure in the paper
- [ ] Generated by a script from a results file — never hand-edited
- [ ] No baked-in citation numbers

**Per table**

- [ ] Generated from a results file by a formatting-only script
- [ ] Units in headers; significant figures defensible
- [ ] Every value traceable to a results file
- [ ] Empty cells have an explicit, defined meaning

**Per figure set**

- [ ] Styling comes from one central module
- [ ] Compute and plotting are separate stages
- [ ] A manifest records script, data, config, and commit for every final figure
- [ ] The README notes that rebuilt PDFs differ by timestamp, not content

## Anti-patterns

- **Plot first, decide later.** A figure set where every panel is defensible and the set argues nothing.
- **Styling scattered across scripts.** Makes any later standard unenforceable.
- **Copying figures into the manuscript** and leaving their provenance behind.
- **The hand-edited PDF.** Unregenerable, and nobody remembers what was changed.
- **Retyping a table.** The error class you will not catch by reading.
- **A computing "formatting" script.** Two implementations of one result, guaranteed to diverge.
- **Citation numbers inside figure images.** Correct exactly until the next reference is added.
- **Reporting "figures verified"** from an instrument blind to the thing that changed.

## Using this file with an AI assistant

**As standing project context:**

> Follow `practices/scientific_figures_tables.md` for all figures and tables. Use the central style module for plotting; never hand-edit a final figure; generate every manuscript table from its results file with a formatting-only script.

**As a compliance audit:**

> Read `practices/scientific_figures_tables.md` §2. Audit every figure in `manuscript/figures/` against that checklist. Report one row per figure: figure | rule violated | evidence | suggested fix. Where a violation is systematic across figures, say so and propose a single central fix in the style module rather than per-script edits. Change nothing.

**As a provenance audit:**

> Read `practices/scientific_figures_tables.md` §5. For every figure referenced in the manuscript, determine which script and which data file produced it, and which commit that was. Report as a table with a `traced / partial / cannot determine` column. Do not guess a source — "cannot determine" is the correct answer where the link genuinely isn't recorded.
