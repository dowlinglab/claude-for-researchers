# Slide style guide

Extracted 2026-09-02 from two real sources — `DowlingLab_template.pptx` (a 2018 conference template, 2 slides) and `Dowling Teaching Controls MPC Academy 2025.pptx` (a real, delivered 26-slide talk, MPC Academy, Wayne State, August 2025) — plus Alex's direct critique of this deck's stale draft sections. Both files live in the lab's Google Drive (Conferences and Presentations), not this repo; the analysis (word counts, font sizes, positions) was done directly against their XML. This file is the rule set the Beamer deck (`main.tex`, `sections/*.tex`) must follow; it is not itself a PowerPoint document.

## What the audit found

**Text density.** Word count per slide across the 26 real talk slides ranged from 6 to 229, but the distribution is bimodal, not a spread: most slides (18 of 26) run under 45 words of prose and many under 20 — these are the image-forward slides that carry the talk. A handful of outliers (the agenda slide, two "why this works" summary slides, and one 229-word reference/citation slide) are backup or reference material, not narrative slides, and read that way — dense text is acceptable there because the audience isn't meant to read it live, only to have it available. **Rule: narrative content slides stay under ~20–25 words of body prose** (titles and diagram labels don't count). If a slide needs more, split it or demote the extra material to a backup slide.

**Font sizes.** The real deck's own slide master defines exactly one title size (32pt, bold) and a two-level body hierarchy (28pt / 24pt) — that discipline is already there in the master, even though individual slides drift from it ad hoc. This repo's own draft sections had drifted further: `\Large`, `\large`, `\small`, and `\scriptsize` were all in use as body text with no rule distinguishing them (`sections/00_open.tex`, `01_ecosystem.tex`, `02_context.tex`). **Rule, effective now: exactly two body-text sizes.** `\large` for the one big idea a slide argues (the NDBlue bold callout pattern already used throughout — see `\slidepoint` below); `\small` for everything supporting it — captions, attributions, footers, secondary explanation. `\scriptsize`/`\tiny` are not body text; they're reserved for diagram micro-labels and code (`lstlisting` already sets `\scriptsize`), exactly the way the real deck reserves 10–12pt Courier New for citation lines and URLs, never for the point being made.

**Color.** The template's own theme XML carries no real brand palette — it's the default Office color scheme (`4472C4` blue, etc.); whatever ND identity the real deck has comes from images (the logo) and a few manually-applied text colors, not a defined scheme. That confirms the right move already made in `main.tex`: define the actual official ND colors once (`NDBlue` `#0C2340`, `Dome Gold` `#C99700`, `Irish Green` `#00843D`, documented with WCAG contrast in `theme/README.md`) and use only those plus the Okabe-Ito data palette — never the incidental blues that show up in pasted clip-art (`0022F5`, `1511EE` were leftover artifact colors in the real deck, not deliberate choices).

**Logo placement.** The real deck's slide master places the ND wordmark in the **bottom-left corner** — roughly 1% of slide width from the left edge, 1% from the bottom, sized to about 10% of slide width. This is Alex's own established convention, not a new stylistic add-on. `main.tex` now reproduces it: a small `figures/nd_logo.png` renders bottom-left on every content frame via a background template (title slide excepted — it already carries its own full-size logo in the closing columns, and a second small copy there would collide).

**Layout.** Every real content slide keeps title, body, and page number in the same three fixed positions (title top-left in a full-width bar, page number bottom-right, content filling the middle) — nothing floats between slides. The Beamer deck already has this from `\frametitle`/`footerSimple`; no change needed there.

## Rules for this deck going forward

1. **One title size.** The theme's `frametitle` template already enforces this everywhere except the cover (title) slide, which is its own one-off typographic treatment (a cover, not a body slide) and is exempt.
2. **Two body sizes, no more.** `\large` for the slide's one argument; `\small` for support. Never `\Large`, `\normalsize` mixed in ad hoc, or `\footnotesize` as body text.
3. **Logo bottom-left**, automatic via the background template — section files don't need to add it themselves.
4. **Colors**: `NDBlue`, `NDGold`, `IrishGreen`, `Muted`, and the Okabe-Ito data colors only. No other hex values in slide content.
5. **Text density**: ~20–25 words of prose per narrative slide. If a slide needs more, it's doing two jobs — split it.

## Still stale

`sections/00_open.tex`, `01_ecosystem.tex`, `02_context.tex` predate both the three-act restructure (`storyboard.md`) and this style guide — they mix `\Large`/`\large`/`\small`/`\scriptsize` freely and were written before the two-size rule existed. They're getting rewritten from scratch against `storyboard.md` regardless (tracked there), so they're listed here rather than hand-patched — the rewrite is where this guide actually takes effect.
