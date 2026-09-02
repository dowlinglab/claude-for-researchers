# Open questions

Decisions not yet made. Once resolved, move the outcome into [seminar_notes.md](seminar_notes.md) (as a dated decision) and, if it changes the plan, update [outline.md](../outline.md) or [seminar_design.md](seminar_design.md), then delete the item from this list.

## Logistics
- **Start time and location** for the September 17, 2026 talk — format is decided (1-hour slot, 40-minute talk + 20 minutes of questions) but the clock time and room are still needed to finish the event-details block in [README.md](../README.md).
- **Room AV / internet access** — determines whether live demos in Sections 3, 6, and 7 can hit real APIs (e.g., a live Claude Code or DOI-lookup call) or need to be screenshots/pre-recorded. Live demos are riskier; default to screenshots unless the room is confirmed reliable.
- **Handout distribution** — printed copies, PDF-only, or also published from this repo as a web page.

## Content
- **Amateur Radio anecdote** — include as a single spoken aside (near Section 3 or 6) or cut entirely? See [demo_ideas.md](demo_ideas.md) story #4.
- **Frame story** — confirm "finishing a paper after the student graduated" (story #5) as the open/close bookend, and decide how much identifying detail is appropriate (which project, any implicit identification of the student).
- **Journal-selection workflow (charter §12)** — drop entirely, or keep as a one-paragraph handout mention? Currently recommended: drop. See [seminar_design.md](seminar_design.md).
- **Real vs. composite examples** — for the notebook→package story and the graduated-student story, decide whether to use an actual (anonymized, permission-checked) Dowling-lab project or a composite/fictionalized example. Real examples are more convincing; composite examples avoid any need for anonymization or student consent.
- **Writing-style guide source material** — blocked on Alex supplying the prior style-analysis output before `resources/style/alex_dowling_writing_style.md` can be drafted.

## Institutional facts to verify before the talk (do not state live without confirming)
- **ND Claude access path(s).** As of this drafting (2026-09-02), search results indicate: Gemini is available campus-wide via Google Workspace SSO; Magai gives some Arts & Letters faculty access to ~26 models including several Claude versions; and Notre Dame's AI Enablement team is piloting a direct Claude license (with Internet2) separate from Anthropic's academic Team-for-Scientists plan. Direct fetch of `ai.nd.edu` failed during drafting (TLS error) — this was pieced together from search snippets only, not confirmed against the primary page. **Re-verify directly on ai.nd.edu before the talk**, since the two Claude access paths (ND's own pilot vs. Anthropic's PI-application Team plan) should not be conflated on a slide.
- **DoD/DoW usage restriction on Anthropic products.** A search snippet attributed to `ai.nd.edu/ai-in-action/approved-ai-tools/claude/` states that researchers with DoD/DoW contracts/agreements are restricted from using Anthropic products, citing March/April 2026 DoD/DoW memos. This is potentially relevant to CBE researchers with defense-funded work and is worth a one-line caveat in Section 1 — but given it wasn't confirmed against the primary page, **verify wording and current status directly (or with OIT) before stating it live.**
- **CBE-specific data-sensitivity or export-control considerations** (e.g., ITAR/EAR-adjacent work) — not investigated yet; flag only if directly relevant to this audience.

## Design/production
- **Beamer theme** — resolved: [ND Beamer Template](https://github.com/dphow/ND_Beamer_Template) (public domain). Still open: whether to use the white color variant or the default, and whether ND logo/navigation bar options are wanted in a "clean, sparse" deck.
- **Manuscript-audit resource scope** — confirm bundling quantitative-claim, methods-vs-code, figure-vs-text, and journal-guideline compliance into one `resources/prompts/manuscript_audit.md` (current plan) rather than separate files, once a draft exists to review.
- **DOI checker scope** — BibTeX/manuscript validation only, or also live Crossref (or similar) API queries? Live queries add real value but also a network dependency and rate-limit/error-handling surface area worth scoping deliberately.
