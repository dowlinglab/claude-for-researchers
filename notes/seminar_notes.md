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

---

## 2026-09-02 (real code-maturity examples + new closing section)

**Decisions:**
- Replaced the planned anonymized-composite examples in Outline Section 4 with three real, public, verified repos: [emcal](https://github.com/dowlinglab/emcal) and [bits_for_gaps](https://github.com/dowlinglab/bits_for_gaps) (graduate-student research code → package, each tied to a peer-reviewed paper) and [grad-visit-scheduler](https://github.com/dowlinglab/grad-visit-scheduler) (Alex's own notebook-to-package story, now the section's primary demo, sourced from three of his LinkedIn posts). Verified all three directly against their READMEs before writing them into the outline, rather than trusting the LinkedIn summaries alone. Convention: cite the repos by name freely (public), but don't name/identify the student who wrote the original `emcal`/`bits_for_gaps` code in the spoken narrative.
- `grad-visit-scheduler`'s real, dated narrative (Codex, not Claude; v0.1.2→v0.3.1 Feb 11–17, 2026; "5x productivity" with Alex's own caveat about prior expertise) is strong enough that it replaces the generic before/after file-tree demo entirely.
- Added Alex's own "how do we train future scientists and engineers..." reflection (from the same LinkedIn posts) as a new, deliberately unresolved question closing Outline Section 8 — see [demo_ideas.md](demo_ideas.md) "training-model tension."
- New: a one-minute closing **Section 9, "Unleash Your Curiosity: AI and your hobbies,"** added after Section 8 and before Q&A, at Alex's request. Moved the Amateur Radio anecdote out of Section 3 into this new section, paired with a second hobby example (AI + 3D printing, a LinkedIn post from ~7 months ago) that Alex is still providing. This section doubles as the talk's time buffer — first thing to compress if running long.

**Files touched:** `outline.md`, `notes/demo_ideas.md`, `notes/seminar_design.md`, `notes/open_questions.md`, this file.

**Next:** get the 3D-printing LinkedIn post from Alex to finish Section 9; still waiting on the writing-style file and a Beamer white/default + logo decision; then begin drafting the top-priority `resources/` files.

---

## 2026-09-02 (3D-printing story received; Section 9 finished)

**Decisions:**
- Alex provided the 3D-printing LinkedIn post (ChatGPT + OpenSCAD, ~7 months prior) plus a photo collage (sketch → 3D-printed kitchen organizer, and a Dobsonian telescope shelf with a compass holder). He flagged the post's own prose as "a little too AI sounding" — deliberately did not reuse its emoji-listicle structure when writing it into [demo_ideas.md](demo_ideas.md) #4b; extracted the substance in plain prose instead, consistent with the seminar's own Section 6 teaching on avoiding generic AI-writing patterns.
- This story's two best lines turned out to reinforce material already planned elsewhere, so Section 9 was written to echo rather than repeat: the "generate → render → screenshot → targeted feedback, small patches over regeneration" workflow lesson matches Section 4's "review the diff, prefer small changes" almost exactly; the "speed vs. understanding" tradeoff echoes the Section 8 training-model tension from a low-stakes domain. Both call-backs are meant to be brief, not re-explained.
- Section 9 in [outline.md](../outline.md) is now fully specified — Amateur Radio link plus the 3D-printing collage, one slide.
- Flagged one production to-do: the collage image exists (Alex has it) but isn't yet a file in this repo — needs to be added to `slides/figures/` when slides are built; not something extractable from the conversation automatically.

**Files touched:** `notes/demo_ideas.md`, `outline.md`, `notes/open_questions.md`, this file.

**Next:** Section 9 is done. Still waiting on the writing-style file and the Beamer white/default + logo decision. Then begin drafting the top-priority `resources/` files.

---

## 2026-09-02 (earlier 3D-printing post added; Section 9 recurated)

**Decisions:**
- Alex sent a second, chronologically *earlier* 3D-printing post: the "boot dryer octopus" — a glove/boot dryer built from a $10 inline fan and a 3D-printed PVC adapter, ChatGPT's first-ever OpenSCAD project for him, including it catching a hairdryer fire-hazard risk and recommending the fan instead. Ends with a genuine open question about 3D printing as experiential learning in CBE courses (turbulent-mixing baffles; vehicles for teaching thermo/polymers/transport/reactions/controls).
- With three hobby examples now competing for Section 9's 1 minute (radio book, boot-dryer-octopus, kitchen-organizer/telescope), recurated rather than piling all three in equally: boot-dryer-octopus becomes the spoken anchor (best narrative arc, names real ND resources — Hesburgh Libraries 3D printing, the Innovation Hub, credited Adam Heet), the other two become link-only slide mentions with no spoken narration, and the section now closes on the boot-dryer post's own CBE-course question rather than a generic "try this yourself" line — a genuine unresolved question, and a natural bridge into Q&A that specifically engages faculty in the room.
- Flagged explicitly (not silently decided) that fitting three examples into 60 seconds is ambitious — recommended Alex time it out loud in rehearsal and be ready to cut Post B (kitchen organizer/telescope) to a bare link if it runs long.
- Second collage image (OpenSCAD editor + render + printed part + fan) also needs manual addition to `slides/figures/` later — same limitation as the first image.

**Files touched:** `notes/demo_ideas.md`, `outline.md`, this file.

**Next:** Alex to confirm (or adjust) the anchor-story choice for Section 9 above; still waiting on the writing-style file and the Beamer white/default + logo decision. Then begin drafting the top-priority `resources/` files.

---

## 2026-09-02 (Section 9 confirmed as two slides)

**Decisions:**
- Alex confirmed the boot-dryer anchor and expanded Section 9 to **two slides**: 9a, the boot-dryer story as a hook/encouragement to "tinker, think about possibilities," closing on its own CBE-course question; 9b, a pure hobbies gallery (kitchen organizer, telescope shelf, ham radio book) with no repeated argument — deliberately not restating Section 8's training-model tension a second time, so the talk ends on curiosity rather than another caveat.
- Section 9's time doubled from 1→2 minutes. To hold the 40-minute total, trimmed Section 4 (Build) from 7→6 min — it already gives `grad-visit-scheduler` the full story and treats `bits_for_gaps`/`emcal` as brief mentions, so this was a light cut, not a real loss of content.
- Updated the at-a-glance table's running totals and the "why these cuts" note in [outline.md](../outline.md) accordingly.

**Files touched:** `outline.md`, `notes/demo_ideas.md`, this file.

**Next:** still waiting on the writing-style file and the Beamer white/default + logo decision. Outline is otherwise feature-complete — next major step is drafting the top-priority `resources/` files.

---

## 2026-09-02 (hobby-project images added and renamed)

**Decisions:** Alex added the two photo collages to `slides/figures/` (arriving with generic upload-timestamp filenames). Renamed for clarity/consistency: `1765462525518.jpeg` → `boot_dryer_octopus.jpeg`, `1769434741290.jpeg` → `kitchen_organizer_telescope_shelf.jpeg`. Updated [outline.md](../outline.md) Section 9 and [demo_ideas.md](demo_ideas.md) #4b to link the real files instead of noting them as pending; resolved the corresponding [open_questions.md](open_questions.md) item fully.

**Files touched:** `slides/figures/boot_dryer_octopus.jpeg` (renamed), `slides/figures/kitchen_organizer_telescope_shelf.jpeg` (renamed), `outline.md`, `notes/demo_ideas.md`, `notes/open_questions.md`.

**Next:** unchanged — writing-style file and Beamer theme details still open; otherwise ready to start drafting `resources/` files.

---

## 2026-09-02 (practice-file structure decided; drafting begun)

Context: Alex had ten parallel workers inventory a year of his own AI-assisted research projects (code refactors, package migrations, manuscript audits, method development). Findings stay out of this repo by his explicit instruction — nothing project-identifying, no references to former group members, no "this project was in bad shape" framing. What lands here is generalized doctrine only.

**Decisions:**
- **`resources/` now has two layers:** `practices/` (seven best-practice files = the doctrine) and `prompts/`/`templates/`/`scripts/` (the tools, which cite the practice files by section rather than restating them). [resources/README.md](../resources/README.md) rewritten accordingly.
- **Seven practice files**, each mapped to a seminar section, each following the same shape: what it is → numbered stable sections → checklist → anti-patterns → how to use it with an AI assistant. Target 150–300 lines.
- Two of Alex's five proposed filenames changed: added `manuscript_audit.md` (the seminar's climax had no takeaway resource, and it has the deepest evidence base), and renamed the personal style guide to `personal_style_guide.md` — a file named for one author teaches students to adopt that author's voice, which inverts the goal. It becomes a worked example plus "derive your own."
- **Tool-agnostic by default**, with tool-specific mechanics quarantined in one clearly marked section per file carrying an explicit staleness warning. Rationale: vendor conventions (`CLAUDE.md`, `AGENTS.md`, settings files) will drift, and neither major tool reads the other's config, so the durable layer has to be tool-neutral markdown.

**Four pain points Alex raised, and how each is being handled:**
1. *Switching between tools and between computers.* Treated as a portability problem, not a tool problem — tool-neutral entry point, repo-relative paths, push-before-switch, and a "handoff block" convention recording verified git state literally. Cross-tool review is presented as a deliberate technique (adversarial second audit), not a friction.
2. *Agents create many markdown files that go stale.* Addressed with a living/dated/superseded taxonomy, a cap of three or four living documents per project, supersession banners naming a successor, append-only logs, and one rule aimed squarely at the cause: an agent may append to the log and create dated records, but may not create a new living document unless asked.
3. *Would a context file enforce rules like keeping docs current?* Answered honestly in the file: less than hoped. Written instructions are advisory and degrade. Anything that must hold needs a mechanical failure mode — hence the new `scripts/check_docs.py` and the §9 principle "determine status from evidence, not recollection."
4. *Tests help when refactoring but obstruct discovery; "more tests is better" is not a universal rule.* This reshapes `scientific_computing_workflow.md` around a **phase-matched verification** table (discovery / consolidation / refactor / publication), with the explicit warning that a green suite is evidence only about the code it executes, and that pinned-value tests are counterproductive during discovery because every legitimate change breaks them.

**New resource added to the plan:** `scripts/check_docs.py` (~40 lines) — internal-link resolution, stale living documents, supersession banners pointing at files that don't exist.

**Also resolved:** the writing-style-guide blocker in [open_questions.md](open_questions.md) — source material exists and is no longer needed from Alex separately.

**Files touched:** `resources/practices/working_with_ai_agents.md` (new), `resources/README.md`, this file.

**Next:** draft the remaining six practice files in the agreed order — `scientific_computing_workflow.md`, `manuscript_audit.md`, then the writing trio, then packaging.

---

## 2026-09-02 (workflow file drafted; style guide rescoped)

**Decisions:**
- Drafted `resources/practices/scientific_computing_workflow.md`. Its §1 is the phase-matched verification table (discovery / consolidation / refactor / publication), which is the direct answer to Alex's concern that "more pytests is better" is not a universal rule. Two rules carry that section: a green suite is evidence only about the code it executes, and tests are for code you intend *not* to change — during discovery, pinned-value tests are counterproductive because every legitimate change breaks them and you stop reading failures.
- **`personal_style_guide.md` renamed to `writing_style_guide.md` and rescoped** at Alex's request. It now does three jobs rather than one: the transferable method for deriving and refining a style guide from prior writing; the Dowling Lab register spelled out as the worked instance; and a standard students can write group papers against going forward. Kept as one file because the method and the instance teach each other, and because in an academic group the "group register" and the PI's register are legitimately the same thing — the source material says so directly. The file will mark which parts are group standard versus one author's habits, and close with how to adapt when writing outside the group.

**Files touched:** `resources/practices/scientific_computing_workflow.md` (new), `resources/README.md`, this file.

**Next:** `manuscript_audit.md`, then `technical_writing.md`, `writing_style_guide.md`, `scientific_figures_tables.md`, `private_code_to_public_package.md`.
