# Open questions

Decisions not yet made. Once resolved, move the outcome into [seminar_notes.md](seminar_notes.md) (as a dated decision) and, if it changes the plan, update [outline.md](../outline.md) or [seminar_design.md](seminar_design.md), then delete the item from this list.

## Logistics
- ~~Start time and location~~ — resolved: 11:00 AM–12:00 PM, Carey Auditorium, 107 Hesburgh Library.
- **Room AV / internet access in Carey Auditorium** — determines whether live demos in Sections 3, 6, and 7 can hit real APIs (e.g., a live Claude Code or DOI-lookup call) or need to be screenshots/pre-recorded. Live demos are riskier; default to screenshots unless the room is confirmed reliable.
- **Handout distribution** — printed copies, PDF-only, or also published from this repo as a web page.

## Content
- **Amateur Radio anecdote** — include as a single spoken aside (near Section 3 or 6) or cut entirely? See [demo_ideas.md](demo_ideas.md) story #4.
- **Frame story** — confirm "finishing a paper after the student graduated" (story #5) as the open/close bookend, and decide how much identifying detail is appropriate (which project, any implicit identification of the student).
- **Journal-selection workflow (charter §12)** — drop entirely, or keep as a one-paragraph handout mention? Currently recommended: drop. See [seminar_design.md](seminar_design.md).
- **Real vs. composite examples** — for the notebook→package story and the graduated-student story, decide whether to use an actual (anonymized, permission-checked) Dowling-lab project or a composite/fictionalized example. Real examples are more convincing; composite examples avoid any need for anonymization or student consent.
- **Writing-style guide source material** — blocked on Alex supplying the prior style-analysis output before `resources/style/alex_dowling_writing_style.md` can be drafted.

## Institutional facts to verify before the talk (do not state live without confirming)
- ~~ND Claude access path(s) and DoD/DoW restriction~~ — resolved via direct browser read of `ai.nd.edu` on 2026-09-02 (the `WebFetch` tool can't reach this domain — TLS error — but the in-app Browser tool can). Confirmed: Claude is currently approved at ND for Public data only (Gemini/ChatGPT EDU/NotebookLM are cleared through Sensitive); an Enterprise Claude license is "coming soon" pending a FOAPAL, separate from Anthropic's own Team-for-Scientists plan; DoD/DoW-funded researchers are prohibited from using any Anthropic products (contact `researchsecurity@nd.edu`). Full quotes in [references.md](references.md). Residual risk: this is a fast-moving page — do one more quick check close to September 17 in case it changed again.
- **CBE-specific data-sensitivity or export-control considerations** (e.g., ITAR/EAR-adjacent work) — not investigated yet; flag only if directly relevant to this audience.

## Design/production
- **Beamer theme** — resolved: [ND Beamer Template](https://github.com/dphow/ND_Beamer_Template) (public domain). Still open: whether to use the white color variant or the default, and whether ND logo/navigation bar options are wanted in a "clean, sparse" deck.
- **Manuscript-audit resource scope** — confirm bundling quantitative-claim, methods-vs-code, figure-vs-text, and journal-guideline compliance into one `resources/prompts/manuscript_audit.md` (current plan) rather than separate files, once a draft exists to review.
- **DOI checker scope** — BibTeX/manuscript validation only, or also live Crossref (or similar) API queries? Live queries add real value but also a network dependency and rate-limit/error-handling surface area worth scoping deliberately.
