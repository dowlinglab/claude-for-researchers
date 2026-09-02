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

**Commit:** `d1f511b` — "Scaffold seminar repo: README, outline, CLAUDE.md, notes, resources plan".

**Open questions raised:** none new beyond what's already in [open_questions.md](open_questions.md); start time and room are still needed.

**Next:** draft the top-priority `resources/` files, starting with `prompts/organize_research_repo.md` and `prompts/manuscript_audit.md`.

---

## 2026-09-02 (verified ND policy directly)

**Decisions:**
- Verified Notre Dame's AI policy/tool-approval pages directly (Alex asked whether I could review `ai.nd.edu/ai-in-action/policies-and-guidelines/` and `.../approved-ai-tools/`). `WebFetch` fails on this domain (TLS error), but the in-app Browser tool loads it fine — noted in [references.md](references.md) for future sessions.
- Confirmed, with exact quotes: Claude is currently approved at ND for **Public data only**; Gemini, ChatGPT EDU, and NotebookLM are cleared through Sensitive; an Enterprise Claude license is "coming soon" (needs a departmental FOAPAL); DoD/DoW-funded researchers are prohibited from using any Anthropic product, contact `researchsecurity@nd.edu`.
- This resolves the two "verify before the talk" items in [open_questions.md](open_questions.md) and upgrades outline.md Section 1 from a hedged caveat to a stated fact — decided to say it plainly on the ecosystem slide rather than soften it, since the seminar should model the same honesty about limitations it asks of students.
- Added the ND data-classification chart as a new candidate demo in [demo_ideas.md](demo_ideas.md).

**Files touched:** `notes/references.md`, `outline.md`, `notes/open_questions.md`, `notes/demo_ideas.md`.

**Next:** one more quick re-check of the `ai.nd.edu` Claude/tools pages close to September 17 in case anything changed, then proceed to drafting `resources/` files.

---

## 2026-09-02 (event logistics confirmed)

**Decisions:** Alex confirmed the seminar is 11:00 AM–12:00 PM in Carey Auditorium, 107 Hesburgh Library. Event-details block in [README.md](../README.md) is now complete; the "start time and location" item in [open_questions.md](open_questions.md) is resolved. Remaining logistics open item: room AV/internet reliability, which determines whether live demos are feasible.

**Files touched:** `README.md`, `notes/open_questions.md`.

---

## 2026-09-02 (processed Alex's open-questions answers)

Alex answered most of [open_questions.md](open_questions.md) directly in the file (committed verbatim in `0c6f477` before processing, per his instruction to commit first). Decisions below; full detail in the individual files linked.

**Decisions:**
- **Room AV:** Alex presents from his own laptop; room A/V is reasonable but won't support audience-interactive activities. Live, presenter-driven demos are workable; no interactive exercises planned.
- **Handout:** rescoped hard, from a multi-section leave-behind to a **printed one-sheet, front and back (~1.5 pages)** so Alex can get copies made. See the rewritten [handout/README.md](../handout/README.md) — most planned content (full prompts, full checklists, repo-pattern write-ups) moves online-only into `resources/`; the handout becomes a reference card plus a pointer back to the repo.
- **Amateur Radio anecdote:** confirmed as a short spoken aside with a link, added to Outline Section 3. The book repo is already public: [github.com/adowling2/radio-extra-book](https://github.com/adowling2/radio-extra-book) (Alex shared the URL directly).
- **Frame story:** confirmed "finishing a paper after a student graduates" as the open/close bookend, reframed around *expediting* a finish (e.g., helping a graduating student wrap up) rather than only "recovery after someone left" — updated in [demo_ideas.md](demo_ideas.md) story #5 and Outline Sections 0 and 8.
- **Journal selection:** un-cut — kept as one bullet in Outline Section 6 (was previously slated to drop). Updated the charter-mapping table and "cut" list in [seminar_design.md](seminar_design.md).
- **Real vs. composite examples:** confirmed real, anonymized Dowling-lab projects for the code-maturity story and the frame story (two candidates already in hand) — no student named or identifiable, ever.
- **DoD/DoW and export-control guidance:** added as a generalized bullet in Outline Section 1 (extends the ND-specific DoD/DoW caveat into "check with your PI about project-specific restrictions," applicable beyond ND).
- **Manuscript-audit scope:** bundling plan stands; next step is a joint working session with Alex over 1–2 real recent projects to scope/test the prompt — not yet scheduled.
- **DOI checker:** Alex already built one in a recent project — plan changed from "build new" to "locate and adapt his existing script." Needs Alex to identify which project.
- **Still open:** the writing-style-guide source file (Alex will send it — his answer was cut off mid-sentence, "We have developed it" — worth a quick check on what he meant to say); the Beamer white-vs-default/logo question (no answer given yet).

**Files touched:** `notes/open_questions.md`, `notes/demo_ideas.md`, `notes/seminar_design.md`, `outline.md`, `handout/README.md`, `resources/README.md`, this file.

**Next:** confirm the writing-style-guide note wasn't cut off accidentally; schedule the manuscript-audit and DOI-checker working sessions; then start drafting the top-priority `resources/` files.

**Next:** unchanged — begin drafting `resources/` files.
