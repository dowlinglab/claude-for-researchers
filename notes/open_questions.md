# Open questions

Decisions not yet made. Once resolved, move the outcome into [seminar_notes.md](seminar_notes.md) (as a dated decision) and, if it changes the plan, update [outline.md](../outline.md) or [seminar_design.md](seminar_design.md), then delete the item from this list.

## Logistics
- ~~Start time and location~~ — resolved: 11:00 AM–12:00 PM, Carey Auditorium, 107 Hesburgh Library.
- ~~Room AV / internet access~~ — resolved: Alex presents from his own laptop; room A/V is reasonable, but the room does not support audience-interactive activities (e.g., live polling). Live, presenter-driven demos are workable; no interactive exercises planned.
- ~~Handout distribution~~ — resolved: printed, target length **1.5 pages (one sheet, front and back)** — see the [handout/](../handout/README.md) rescope. Also publish the same PDF in this repo once built, at no extra cost.

## Content
- ~~Amateur Radio anecdote~~ — resolved, then revised: moved from a Section 3 aside into its own new closing Section 9, "Unleash Your Curiosity: AI and your hobbies," alongside a second hobby example. Book repo: [github.com/adowling2/radio-extra-book](https://github.com/adowling2/radio-extra-book).
- ~~3D-printing examples for Section 9~~ — fully resolved: both stories received and both image collages are in the repo at `slides/figures/boot_dryer_octopus.jpeg` and `slides/figures/kitchen_organizer_telescope_shelf.jpeg`. See [demo_ideas.md](demo_ideas.md) #4b.
- ~~Frame story~~ — resolved: keep "finishing a paper after the student graduated" (story #5) as the open/close bookend, reframed around *expediting* completion (e.g., helping a graduating student wrap up) rather than only "recovery after someone left." See updated [demo_ideas.md](demo_ideas.md).
- ~~Journal-selection workflow~~ — resolved: one bullet point in the live talk (Outline Section 6), not dropped, not handout-only.
- ~~Real vs. composite examples~~ — resolved: use real (anonymized) Dowling-lab projects — Alex has two in mind already — with no student identified by name or implication.
- ~~Writing-style guide source material~~ — unblocked: two existing style guides were located during the project inventory (one derived empirically from a large corpus of the group's own papers, one anchored to named exemplar documents and carrying scientific-integrity constraints alongside voice rules). `resources/practices/personal_style_guide.md` will merge them into a worked example plus a "derive your own" section. Nothing further needed from Alex.

## Institutional facts to verify before the talk (do not state live without confirming)
- ~~ND Claude access path(s) and DoD/DoW restriction~~ — resolved via direct browser read of `ai.nd.edu` on 2026-09-02. Confirmed: Claude is currently approved at ND for Public data only (Gemini/ChatGPT EDU/NotebookLM are cleared through Sensitive); an Enterprise Claude license is "coming soon" pending a FOAPAL; DoD/DoW-funded researchers are prohibited from using any Anthropic products (contact `researchsecurity@nd.edu`). Full quotes in [references.md](references.md). Residual risk: re-check once more close to September 17 in case the page changed again.
- ~~CBE-specific data-sensitivity / export-control considerations~~ — resolved as a general-guidance bullet rather than a specific investigation: the talk will tell grad students/postdocs to check with their PI or project lead about special considerations (DoD/DoW, export control, etc.) before using any AI tool on their project. Added to Outline Section 1/8.

## Design/production
- **Beamer theme details** — [ND Beamer Template](https://github.com/dphow/ND_Beamer_Template) is confirmed as the base. Still open: white color variant vs. default, and whether the ND logo/navigation bar are wanted in an otherwise clean, sparse deck.
- **Two slide-content TODOs deferred pending the theme refactor** (a separate session is reworking the theme, 2026-09-03): (1) `slides/sections/03_act2_build.tex:68` — move the BITS-for-GAPS repo URL out of the body slidepoint and into a new corner box, to the right of the ND logo, that Alex wants added to the template itself; (2) `slides/sections/01_ecosystem.tex:174` — reposition the "watch the thesis" tikz overlay text into that same right-of-logo whitespace instead of centering it on the slide. Both depend on the new theme's logo geometry, so revisit together once that session's changes land. The ham radio slide's new GitHub link (`05_epilogue.tex`) is using the old inline-\slidepoint pattern as a stopgap for the same reason — move it into the corner box too once it exists.
- ~~Manuscript-audit resource scope~~ — bundling plan (quantitative-claim, methods-vs-code, figure-vs-text, journal-guideline compliance as one `resources/prompts/manuscript_audit.md`) stands. Next step, per Alex: co-review 1–2 real recent Dowling-lab projects/papers together to scope and test it — not yet scheduled.
- ~~DOI checker scope~~ — Alex has already built a DOI checker in a recent project; plan is to locate and adapt that rather than build one from scratch. Next step: Alex to point to / share that project so it can be located — not yet done.
