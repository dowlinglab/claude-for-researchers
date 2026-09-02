# Seminar notes — running decision log

A chronological record of decisions, actions, and open threads for this project, in the spirit of the research-log practice this seminar itself recommends (see [outline.md](../outline.md) Section 5). This is the process log; durable rationale belongs in [seminar_design.md](seminar_design.md), unresolved items in [open_questions.md](open_questions.md).

Entry format: date, decisions made, actions taken, files touched, commit (if any), open questions raised, next steps.

---

## 2026-09-02

**Decisions:**
- Seminar date confirmed: September 17, 2026. Time and location still TBD (owner: Alex).
- Talk structure follows the research lifecycle (Explore → Ground → Build → Record → Write → Verify) rather than a product-by-product tour; full rationale in [seminar_design.md](seminar_design.md).
- Consolidated the three manuscript-audit prompts (quantitative-claim, methods-vs-code, figure-vs-text) plus the journal-guideline compliance prompt into a single `resources/prompts/manuscript_audit.md` with multiple modes, rather than four separate files — per the "small number of polished resources" preference.
- Expanded `resources/` beyond the charter's original tree to add `templates/` (research log, results manifest, `CLAUDE.md` example) and `checklists/` (reproducibility + graduation handoff, combined).
- Slides will be built on the [ND Beamer template](https://github.com/dphow/ND_Beamer_Template) (public domain, ND colors/logo, `\usetheme{NotreDame}`).
- Created a project-level `CLAUDE.md` as persistent context for AI assistants working in this repo — and as a live demo candidate for the "context, not conversation" section of the talk.
- Started this file, `notes/seminar_notes.md`, as the running decision log for the project itself.

**Actions taken:**
- Reviewed the full project charter; identified overlaps (audit-prompt family, Sections 6/7 on repo structure) and scope-too-large items for a 45-minute talk.
- Researched Anthropic's Claude Team Plan for Scientists page for accurate program details (pricing, eligibility, application process).
- Researched Notre Dame's current AI access/policy landscape (AI@ND hub, Magai, Google Workspace Gemini access, an in-progress Claude pilot, and a DoD/DoW usage restriction) — flagged for verification before the talk since direct fetch of `ai.nd.edu` failed (TLS error); details sourced via search snippets only. See [references.md](references.md).
- Created `README.md`, `abstract.md`, `outline.md`.

**Files touched:** `README.md`, `abstract.md`, `outline.md`, `CLAUDE.md`, `notes/seminar_notes.md`, `.gitignore` (pending Python/OS additions).

**Commit:** none yet — repo has uncommitted new files as of this entry. Not committed automatically; ask before committing per [CLAUDE.md](../CLAUDE.md).

**Open questions raised:** see [open_questions.md](open_questions.md) — notably seminar time/location, whether to verify the ND Claude pilot and DoD/DoW restriction claims with a primary source before the talk, and whether the Amateur Radio anecdote appears live at all.

**Next:** finish `notes/seminar_design.md`, `notes/open_questions.md`, `notes/references.md`, `notes/demo_ideas.md`, and `resources/README.md`; then begin drafting the top-priority `resources/` files.

---

## 2026-09-02 (later same day)

**Decisions:**
- Seminar slot confirmed as 1 hour: 40-minute talk + 20 minutes of questions (not the 45-minute working estimate from the morning). [outline.md](../outline.md) retimed accordingly — cuts of 1 minute each came out of Sections 1, 2, 3, and 5; Write, Verify, and the closing kept full time.
- Deleted `abstract.md` — the abstract has already been submitted and won't change, so it now lives only in [README.md](../README.md) rather than being duplicated across two files.
- Alex authorized committing to git as work proceeds in this project going forward, rather than only on request.
- Added a Python/OS/editor section to `.gitignore` ahead of the planned `resources/scripts/doi_checker/`.
- Finalized the resources priority list (7 "build first" resources; see [resources/README.md](../resources/README.md)) and the improved `resources/` subtree (`templates/`, `checklists/` added beyond the original charter tree).
- Confirmed the Beamer base template: [ND Beamer Template](https://github.com/dphow/ND_Beamer_Template) (public domain, `\usetheme{NotreDame}`).

**Files touched:** `outline.md`, `README.md`, `CLAUDE.md`, `handout/README.md`, `.gitignore`, `notes/open_questions.md`, `notes/seminar_design.md`, `resources/README.md`; deleted `abstract.md`.

**Commit:** first commit for this project made today — see git log.

**Open questions raised:** none new beyond what's already in [open_questions.md](open_questions.md); start time and room are still needed.

**Next:** draft the top-priority `resources/` files, starting with `prompts/organize_research_repo.md` and `prompts/manuscript_audit.md`.
