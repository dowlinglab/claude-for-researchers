# Seminar notes — running decision log

A chronological record of decisions, actions, and open threads for this project, in the spirit of the research-log practice this seminar itself recommends (see [outline.md](../outline.md) Section 5). This is the process log; durable rationale belongs in [seminar_design.md](seminar_design.md), unresolved items in [open_questions.md](open_questions.md).

Entry format: date, decisions made, actions taken, files touched, commit (if any), open questions raised, next steps.

---

## 2026-09-14 (later) — slide 2 schedule rebuilt at four slots

**Decisions:**

- The slide 2 schedule now uses **four thirty-minute slots** (9:00–11:00) rather than eight
  fifteen-minute ones. Ten visitors across eight narrow slots produced blocks too small to read
  from the back of Carey Auditorium; the point of the figure is that it looks like a real
  recruitment day, which fails if nobody can read it.
- The schedule now enforces the **free-slot building-change constraint**
  (`movement.policy: travel_time`, NSH↔MCH lag of one slot). Under the previous `policy: none`
  the optimizer scheduled back-to-back NSH and MCH meetings, which is not a schedule a visitor
  could physically walk. Every building switch in the new figure shows a visible gap, which also
  makes the constraint something Alex can point at while narrating.
- **How to remake the figure is now recorded next to the inputs**, in
  [`slides/figures/grad_visit_schedule_10_source/README.md`](../slides/figures/grad_visit_schedule_10_source/README.md),
  rather than only in this log. It gives the run command, every solver setting with its reason,
  and the coupling between slot count, `min_faculty`, and the slide's column widths. The figure
  stays real package output; it should be regenerated, never edited as an image.

**Actions taken:**

- Set `min_faculty` to 2. Four slots and six faculty give 24 one-on-one meetings for ten visitors,
  so requiring three meetings each is infeasible once the travel lag applies.
- Rebalanced slide 2: the four-slot figure is roughly square rather than wide and short, so the
  figure column went from 0.60 to 0.50 and the timeline column from 0.37 to 0.46.
- Slide 3 now reads "I used this project to test Codex."
- Slide 6 regained a third "This is not" bullet --- *a Claude vs. Codex throw down* --- so the two
  columns balance again after "a product comparison" was cut, and so the disclaimer names the
  comparison people actually expect from a talk with Claude in the title.
- Rebuilt: 53 slides, no overfull or underfull boxes.

---

## 2026-09-14 — annotated read-through revisions

Alex marked up the 52-slide September 11 PDF and walked through the comments in conversation.
Every item below traces to one of those annotations; slide numbers in the *"was"* column are from
the annotated deck, and the current numbering is in [../slides/storyboard.md](../slides/storyboard.md).

**Decisions:**

- **`DRAFT` is Notre Dame green, not red.** Red is not in the deck palette, and the mark reads as
  a status label rather than an error.
- **Act I is reordered to agent → repository → problem.** The agent/file-system slide (was 14) now
  comes first and its title names the file system explicitly; the comparison slide (was 13) follows
  as a three-column argument — *a conversation*, *a file system*, *a repository* — so the payoff of
  version control lands on a slide built to sell it. Its title states the point: "A repository
  beats a folder, and a folder beats a chat." A short definition of version control was added,
  because the practice audience will include people who have never used Git.
- **Task 1 gets a problem statement.** A new slide (14) opens with a hypothetical: you join the
  group as a student or postdoc, inherit a zip file and the group's latest paper, and are asked to
  reproduce the paper's results before extending them. The rest of Task 1 then reads as the answer
  rather than as generic setup advice.
- **The overnight-work slide splits in two.** Slide 19 is now a concrete example prompt — asking the
  agent for help *writing the goal*, and listing what the goal document must state. Slide 20 gives
  the preferred sequence: the agent drafts the planning document, Alex reviews and edits it while
  awake, and only then does the run start as a Codex Goal, `/goal`, or `/loop`.
- **The hooks slide (was 20) is cut for time.** It explained a Claude-specific mechanism at a level
  of detail the rest of the deck does not need, and Act I had grown by two slides.
- **The LaTeX slide argues for LaTeX.** Retitled "Task 3: Why LaTeX makes the agent useful," it is
  two bulleted columns and closes on plain text being what lets an agent — and Git — work on a
  manuscript. The Overleaf/GitHub slide (was 31) moved up to follow it immediately, since it is the
  mechanics that argument implies.
- **Task 6 opens with motivation, then evidence, then machinery.** The coursepack slide (was 44)
  moved to directly after the four goals and the new calendar, so the audience sees the artifact the
  sprint produced before the repository and testing slides explain how it was produced.
- **The talk's own provenance moves to the epilogue.** "This talk was built with the practices it
  recommends" (was 11) now sits immediately after the six-tasks summary table, and the table's
  "Creating this talk" row was dropped because the following slide covers it in full. It fits better
  as a closing disclosure than as a prologue claim.

**Actions taken:**

- Regenerated the slide 2 schedule figure with **ten** fictional visitors instead of six, using the
  public `grad-visitor-scheduler` package rather than redrawing it. Inputs are preserved in
  `slides/figures/grad_visit_schedule_10_source/` so the figure stays reproducible; the figure column
  widened to 0.60 so the extra rows stay legible.
- Built a new TikZ calendar for slide 40 (`slides/figures/august_2026_calendar.tex`, generated by
  `make_calendar.py`) showing August 2026 with per-day commit shading, the sprint start on
  August 17, and the first lecture on August 24. The totals — **1,452 commits over August 17–31,
  1,084 private and 368 public** — are counted from `git log` in `optimization-private` and
  `ndcbe/optimization`. The lecture date comes from `org/calendar.md` in the public course repo.
- Trimmed text on the slides marked for it (7, 8, 9, and the old 3, 19, 29), converted the marked
  slides to bullets (8, 26, 27, 29, 43), matched steps 2 and 3 of Task 3 to the enumerate-plus-
  sub-bullet style of step 1, and reordered slide 8 to desktop app → editor extension → terminal so
  it can be narrated from easiest to most sophisticated.
- Slide 6: cut "a product comparison," changed "My experience" to "My past year," and switched the
  six-task listing to natural-width columns so no entry wraps.
- Slide 38 became two columns: the drafting sequence runs vertically on the left, the "The agent can
  help…" list on the right, with the trailing whitespace reduced.
- Slide 41 (was) dropped the Gate/Test column and became two bulleted columns, authoritative sources
  and derived artifacts. Slide 42 (was) split its three compound rows into six specific problems,
  and "Check added" became "Test added" throughout, including the frame title.
- Slide 25: "the result that made it credible" became "the published case studies that made it
  credible."
- Rebuilt the deck (53 slides) and visually reviewed every changed slide at 75 dpi; tightened
  spacing on slides 13, 38, 40, and 43 where content collided with the corner logo.

**Checked, no change needed:** the annotation on slide 5 asked to check the spelling of *Ira Glass*
— the host of *This American Life* — and it was already correct. The annotation on slide 9 asked to
check the current Haiku release; **Haiku 4.5 is still the current version**, so the model table is
unchanged. Both are worth rechecking before October 15 along with the other vendor claims.

**Open questions raised:** the deck is now 53 slides rather than 52, and Act I carries two more
slides than it did at the practice talk. Whether that fits the 40-minute budget needs a rehearsal,
not an estimate.

---

## 2026-09-11 — final slide audit and source cleanup

**Decisions:**

- The live deck is final at 52 slides, with `DRAFT` retained on the title slide for the practice talk.
- The narrative now moves from the research context and tool ecosystem through seven research tasks, then uses the optimization-course example to show how artifacts and gate/tests make an AI-assisted workflow progressively more robust. The hobby examples are explicitly framed as an eighth, optional extension.
- Companion resources should be discoverable twice: as a complete inventory and as links on the slides where each guide is useful.
- Detailed LaTeX editorial comments were removed after the final audit. They were valuable during iterative refinement, but the final source is easier to scan without them. The comments remain recoverable in Git history through commit `2c55c74`; durable implementation constraints belong in [style_guide.md](../slides/style_guide.md) or this decision log.

**Actions taken:**

- Audited formatting, narrative continuity, claims, terminology, and all companion-resource references.
- Rebuilt the deck and ran the documentation checks.
- Updated the storyboard, visual inventory, outline, repository READMEs, current follow-up list, style guide, and project instructions to match the final deck.

**Remaining follow-up:** recheck time-sensitive vendor and Notre Dame policy claims immediately before October 15; decide when to remove `DRAFT`; build the separate handout if desired. See [open_questions.md](open_questions.md).

---

## 2026-09-02

**Decisions:**
- Seminar date confirmed: September 17, 2026. Time and location still TBD (owner: Alex).
- Talk structure follows the research lifecycle (Explore → Ground → Build → Record → Write → Verify) rather than a product-by-product tour; full rationale in [seminar_design.md](seminar_design.md).
- Consolidated the three manuscript-audit prompts (quantitative-claim, methods-vs-code, figure-vs-text) plus the journal-guideline compliance prompt into a single `resources/prompts/manuscript_audit.md` with multiple modes, rather than four separate files — per the "small number of polished resources" preference.
- Expanded `resources/` beyond the charter's original tree to add `templates/` (research log, results manifest, `CLAUDE.md` example) and `checklists/` (reproducibility + graduation handoff, combined).
- Slides will be built on the [ND Beamer template](https://github.com/dowlinglab/ND_Beamer_Template) (ND colors/logo, `\usetheme{NotreDame}`).
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
- Confirmed the Beamer base template: [ND Beamer Template](https://github.com/dowlinglab/ND_Beamer_Template) (`\usetheme{NotreDame}`).

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

---

## 2026-09-02 (audit file drafted; scripts promoted to real deliverables)

**Decisions:**
- Drafted `resources/practices/manuscript_audit.md` — the deepest file, 12 sections. Its organizing idea is §1: separate *is the arithmetic right* from *is the method right* from *is the transcription right*, and report them in that order, because merging them guarantees a defensive reading from co-authors. Other load-bearing sections: §3 (state the standard of evidence, **including when not to change something** — that is what makes the changes credible), §5 ("cannot verify" as a first-class status), §7 (determine status from evidence, never recollection), §8 (read the rendered artifact, not the build log; "a request to enumerate is worth more than a request to confirm"), and §10 (audit the audit; retract in place).
- **`scripts/` are now working defaults, not illustrations**, at Alex's request: a nominal default **DOI checker** and a nominal default **Python figure style module**, both intended for the group and anyone else to adopt on new projects. Each ships with a README, real arguments instead of hardcoded paths, and minimal dependencies.
- The figure-style module exists because the same lesson was learned twice independently in different projects: plot styling scattered across dozens of scripts makes any later standard unenforceable, so conventions must be fixed centrally once and inherited. It pairs with the compliance checklist in `practices/scientific_figures_tables.md`.

**Files touched:** `resources/practices/manuscript_audit.md` (new), `resources/README.md`, this file.

**Next:** the writing trio (`technical_writing.md`, `writing_style_guide.md`, `scientific_figures_tables.md`), then `private_code_to_public_package.md`, then the scripts.

---

## 2026-09-02 (writing trio drafted — six of seven practice files done)

**Decisions:**
- `technical_writing.md` — structure before sentences; manuscript as files not a blob; the notation/equation/prose conventions worth enforcing because they are checkable; "never cite what you haven't read" with literature notes kept as a *claim audit* (what a source can and cannot support) rather than summaries; editing against a written standard instead of against taste; §6 on recognizing AI drift, whose two structural safeguards are protecting inconvenient results and carrying integrity constraints in the style file; review comments captured verbatim as a numbered work list before any editing; three graded submission-readiness gates.
- `writing_style_guide.md` — the three-part structure Alex asked for. **Part I** is the transferable method: derive from three to six named exemplars weighted by authorship role, commit the exemplars so they travel, extract what is observably true rather than inventing principles, and **mark confidence** (argument structure emerges reliably from a few documents; word-level preferences need a much larger sample). **Part II** is the group register, binding for group papers. **Part III** is how to rebuild it elsewhere. §3 carries the genuinely novel idea from the source material — a style guide that freezes *integrity constraints* alongside voice, so a later prose pass cannot quietly re-inflate a claim an audit had narrowed. §4 makes it checkable with a one-paragraph litmus test.
- `scientific_figures_tables.md` — lopsided by design, as expected: the figure-quality checklist consolidates guidance the group already has (with a placeholder for the canonical published link, which I did not want to guess at), while §3–§5 add the reproducibility layer that was missing — central styling so a later standard is enforceable, compute/plot separation, and a figure manifest, motivated by the specific failure where provenance exists in a staging directory and the copy into the manuscript destroys it. Tables are written fresh around one rule: **regenerate, never retype**, with the generating script formatting only and holding no state.
- Fixed a stale status row: `manuscript_audit.md` was marked "Next" in `resources/README.md` after it had been drafted and committed — exactly the class of drift `check_docs.py` is meant to catch.

**Files touched:** `resources/practices/technical_writing.md`, `writing_style_guide.md`, `scientific_figures_tables.md` (all new), `resources/README.md`, this file.

**Next:** `private_code_to_public_package.md` (last of the seven), then the tools — starting with the two Alex asked for as adoptable defaults, `scripts/doi_checker/` and `scripts/figure_style/`.

---

## 2026-09-02 (all seven practice files drafted)

**Decisions:**
- Drafted `private_code_to_public_package.md`, the last of the seven. Its §1 leads with the idea that organized every successful instance in the evidence: **split by audience, not by code quality** — the package is the method plus what a general user needs; the research archive is the paper's reproduction workflow. Splitting by quality (ship what you're proud of) produces both an incomplete package and an incomplete archive.
- §2 carries the other genuinely transferable move: **isolate non-public content by parameterizing it, not by scrubbing it.** Institution or sponsor specifics become input files; publishing then means shipping synthetic instances of those same files, so there is no scrubbing pass and no stray identifier surviving in a default. And the real data keeps earning its keep privately as a dogfooding harness — migrating it onto the public API is what surfaces the API defects synthetic examples hide.
- §9 and §10 encode the most consistent gap found across every project inventoried: provenance stops at the repository boundary. The rule is stated as a two-way test — hand someone only the PDF, can they find the code; hand them only the repository, can they find the paper — plus the point that a private repository, a shared drive, or an unpushed branch is not an archive.
- §10 also records the one place a "clean up before release" pass went too far: stripping development scaffolding from user-facing docs is right, deleting it outright is a loss, because that material is the most reusable thing produced for the next project. Move it to the archive rather than out of history.
- Added `resources/practices/README.md` — a "which file do I want?" table, a diagram of how the seven relate across a project arc, the shared conventions, and copy-paste text for pointing an assistant at them from another repository.

**Files touched:** `resources/practices/private_code_to_public_package.md` (new), `resources/practices/README.md` (new), `resources/README.md`, this file.

**Next:** the tools layer. Priority order: `scripts/doi_checker/` and `scripts/figure_style/` (the two adoptable defaults Alex asked for), then `templates/project_entry_point.md`, `templates/research_log.md`, `templates/results_manifest.md`, then `scripts/check_docs.py` and the prompts.

---

## 2026-09-02 (both default scripts built and tested)

**Decisions:**
- **`scripts/doi_checker/`** — adapted from an existing working script rather than rewritten, preserving the two hard-won parts: the brace-counting BibTeX parser (a regex truncates entries to their title whenever a title contains nested braces, silently, making everything downstream look like a mismatch) and the two-pass structure kept separate *because the passes fail differently*. Added for distribution: `argparse` (`--bib`, `--tex`, `--mailto`, `--json`, tunable thresholds), `urllib` instead of shelling out to `curl` so it is pure standard library, graceful degradation on network failure, and **exit codes so it can gate CI** — 1 on any `UNRESOLVED`/`MISMATCH`, 0 when only `CHECK` items remain, since those need a human rather than a build failure. It still never edits a bibliography.
- **`scripts/figure_style/`** — built on the existing `pubfig.py` specification (Okabe-Ito palette, the four standard sizes, 300/1200 dpi, bold 16 pt labels, ticks in with top/right on). Two additions beyond a restyle: it **fixes a real shipped bug** by checking *both* figure dimensions rather than width only (a right-width/wrong-height figure otherwise passes silently and prints at the wrong scale), and `save_fig` writes a **provenance sidecar by default** — script, git commit, dirty flag, input files, library versions — which operationalizes `practices/scientific_figures_tables.md` §5. Provenance defaults to on deliberately: it is skipped by default everywhere else, and that is precisely why figures become untraceable. Also added a one-line greyscale preview, since the accessibility checklist item is universally listed and almost never actually tested.
- Both were **tested, not just written**: the DOI checker against a synthetic bibliography exercising MATCH, MISMATCH, UNRESOLVED, a nested-brace title, a cited-but-missing key, and a below-threshold proposal (correctly declined at 0.63); the figure module end to end, including git provenance capture inside a repository, graceful degradation outside one, and warnings on both a wrong-height and a wrong-width figure. A runnable `example.py` ships with the module.
- Filled in the canonical figure-guidelines URL in `practices/scientific_figures_tables.md`, which had been left as a placeholder rather than guessed at. It was recovered from the existing implementation's own docstring.

**Files touched:** `resources/scripts/doi_checker/{check_dois.py,README.md}`, `resources/scripts/figure_style/{figure_style.py,example.py,README.md,example.*}` (all new), `resources/practices/scientific_figures_tables.md`, `resources/README.md`, this file.

**Next:** the three templates (`project_entry_point.md`, `research_log.md`, `results_manifest.md`), then `scripts/check_docs.py`, then the prompts.

---

## 2026-09-02 (templates built; legend-overlap check added after a real catch)

**Decisions:**
- Built the three templates. Design constraint throughout: **a template too elaborate to fill in doesn't get used**, so each has a minimal required core, optional fields marked as optional, and a worked example — the example is what makes a template usable.
  - `project_entry_point.md` — the tool-neutral `PROJECT.md` plus three-line `CLAUDE.md`/`AGENTS.md` pointer files, so switching tools or collaborating with someone on a different one costs nothing. Emphasizes rewriting "Current state" in place rather than appending, with the staleness-pointer trick offered only as a repair for files that already went chronological.
  - `research_log.md` — append-only, corrections as later entries, with the "Didn't work" field explicitly prompted because it is the one people skip and the one that saves the most time. Includes guidance that the *Interpretation* field stays human: an assistant can summarize what happened and verify that citations resolve, but what a result means is the part that has to come from whoever will defend it.
  - `results_manifest.md` — figures, tables, and every quantitative claim in the text, plus a run record and a draft data-availability statement kept in the same file so it stays in sync. `cannot_verify` is a legitimate recorded status. Integrates with the figure-style provenance sidecars so the manifest summarizes files that already exist rather than being reconstructed from memory.
- **Alex spotted that the shipped `example.png` had its legend overlapping the curves** — a genuine figure-quality violation in the very artifact demonstrating the figure standard. Rather than just fixing the example, added a real check: `save_fig` now warns when a legend covers plotted data, computed by transforming line and collection vertices into display coordinates and testing containment in the legend's bounding box. It catches `loc="best"` too, which people assume is safe (131 covered points on the five-series demo). The example now anchors the legend above the axes and passes under `python -W error::UserWarning`.
- **Deliberately did not add a "legend extends past the axes" check.** It fired on the *recommended fix* (anchoring outside with `bbox_to_anchor`, which `bbox_inches="tight"` then includes). A gate that cries wolf on correct usage trains people to disable it — taking the valuable overlap check with it. Recorded in the code and the README so it doesn't get "fixed" later.
- Added the legend rule to the figures practice file in three places: the readability checklist (with the fix hierarchy), the per-figure checklist, and the anti-patterns list, noting it is usually invisible to whoever made the figure because they already know what the data looks like.

**Files touched:** `resources/templates/{project_entry_point,research_log,results_manifest}.md` (new), `resources/scripts/figure_style/{figure_style.py,example.py,README.md,example.*}`, `resources/practices/scientific_figures_tables.md`, this file.

**Next:** `scripts/check_docs.py`, then the prompts (`organize_research_repo.md`, `manuscript_audit.md`, `literature_workflow.md`). After that: slides and handout.

---

## 2026-09-02 (six example types confirmed; Act I reframed as a sell; demo_ideas.md reconciled)

Context: since the previous entry, the talk was restructured from the six-stage lifecycle framing into the three-act story (Prologue "Tinker" / Act I "Understand" / Act II "Build" / Act III "Challenge" / Epilogue "Trust"), locked in `slides/storyboard.md` (commit `c049173`), and the resources layer, DOI checker, figure-style module, `check_docs.py`, and Beamer deck scaffold were all built and committed (see commit log; this log fell behind that work and picks back up here).

**Decisions:**
- **Confirmed the roster of six example types** (full table in [demo_ideas.md](demo_ideas.md)): (1) inherited material maturing toward a manuscript, generic; (2) auditing a manuscript's final version, generic; (3) code → released software product, named (`bits_for_gaps`, `emcal`, `grad-visit-scheduler` — public, no exposure); (4) literature review → getting-started guide, generic; (5) proposal writing, generic (kept consistent with 1–2 rather than named, since these may be live/competitively sensitive); (6) course retooling, named ("Optimization for Decision Science" — Alex's own, already-public course).
- **Added a third Type-1 example**, the membrane-transport project (`data3`) — inherited MATLAB code, spreadsheets, PowerPoint decks, and draft documents, reconstructed. Alex offered to name it despite the pattern, since naming it alone wouldn't expose anything sensitive; decided against it, because the value of an internal codename is low and naming one of three otherwise-generic Type-1 siblings would create a visible, unexplained asymmetry for the audience with no real narrative payoff.
- **Reframed Act I's job**: it is a sell, not a payoff. Its only argument is that version control is the prerequisite that unlocks what Codex/Claude Code can do — Alex's explicit framing ("version control is essential for unlocking the power of Codex or Claude Code"). The previously planned mature-example slide (the well-kept `CLAUDE.md` from "Optimization for Decision Science," originally planted in Act I to pay off later) was cut from Act I entirely rather than kept as an early teaser, so the act doesn't dilute its own sell with a taste of the payoff. Act I drops from 7 slides to 6; the course material now appears for the first time in Act III's two-part capstone rather than being planted earlier.
- Reconciled `notes/demo_ideas.md` against `slides/storyboard.md` to remove the now-stale references to the cut Act I plant (the old row 7 and its "deliberately a plant" note, and the capstone's "the plant from Act I pays off" language, now "the Act I argument, taken all the way").

**Files touched:** `notes/demo_ideas.md`, `slides/storyboard.md`, this file.

**Open questions raised:** Type 4's naming (watershed/desalination) was assumed generic by the same conservative default as types 1–2, not explicitly confirmed — flagged in `demo_ideas.md` "Still open." Slide count (35, ~41.5 min) still needs a real per-minute check once `slides/sections/*.tex` are rewritten against the current structure — tracked in `storyboard.md`.

**Next:** rewrite `slides/sections/00_open.tex`, `01_ecosystem.tex`, `02_context.tex` against the locked Prologue/Act structure (currently stale, predate the restructure); then draft new section files for Act II, Act III, and the Epilogue; get outline feedback at least 8 days before the talk per the group manual (not yet done).

---

## 2026-09-11 (seminar rescheduled)

**Decision:** The seminar date moved from September 17 to October 15, 2026. The time and location are unchanged. Until the next polishing pass is complete, the title slide carries a red `DRAFT` label in its upper-right whitespace.

**Actions taken:** Updated the date in the deck and current project metadata, adjusted the policy re-check deadline, rebuilt the 52-page PDF, and visually verified the revised title slide.

---

## 2026-09-11 (Task 7 reframed around the course's evolution)

**Decision:** Replace the six disconnected course-audit incidents with one six-slide narrative: course history, Fall 2026 goals, authoritative-source architecture, verification gates, bounded autonomy plus instructor review, and a minimal four-artifact version the audience can adopt using this repository's resources.

**Evidence:** The retired Spring 2021 `nbpages` site already orders Getting Started with Pyomo and Modeling/Applications before theory and algorithms. Git history shows Spring 2023 as the sprint-like JupyterBook conversion; later offerings are iterative refinement. The current public/private course handoff and verification entry points supply the source-map, gate, and review-loop details.

**Resource integration:** Task 7 now directly names or links the scientific-computing and figure practices, manuscript audit, agent and writing-style practices, project-entry and research-log templates, documentation/figure checks, and reproducibility/handoff checklist.

**Verification:** Rebuilt the full 52-page deck, ran `resources/scripts/check_docs.py` with no issues, and rendered/inspected all six revised Task 7 slides (pages 39–44). The revised frames add no overfull boxes.

---

## 2026-09-11 (Slide 9 model and usage re-check)

**Corrections:** Added GPT-6 Astra, announced September 3, to the OpenAI model sequence. Corrected the Codex usage description from only a five-hour window to five-hour and weekly windows, with a plan-dependent qualifier.

**Evidence:** OpenAI's current developer model catalog lists Astra as the flagship for the hardest end-to-end work. The signed-in EDU account's usage meter reports 300-minute and 10,080-minute windows, confirming a seven-day window alongside the five-hour window.

---

## 2026-09-11 (practice-talk feedback implemented)

**Decision:** Consolidate the talk into six research tasks. Act I now covers workspace setup and inheritance; Act II covers packaging then literature-grounded writing; Act III covers audit, manuscript drafting, and course modernization. The first slide of each task states its goal. The existing uncommitted partial revision was carried forward rather than replaced.

**Changes:** Added instruction-file helpers and a concise example, independent-work guidance, and Claude hooks. Completed the three-repository and Overleaf/branch workflow, with official documentation links in the slide footer and distributed Markdown. Replaced the simulated diff with actual compiled `latexdiff`; added attributed GitHub Desktop and Overleaf screenshots. Retained tangible audit checks and rebuilt the manuscript sequence around accumulated evidence. Enlarged the relevant coursepack excerpts and the hobby visual, and closed with a runnable first task in this public repository. Removed the requested bug/cleanup/audit detours. Companion guides, task indexes, storyboard, and handout plan now agree.

**Access correction:** Alex confirmed Antigravity is not included in Notre Dame's Google plan and supplied a screenshot of his ND account's ineligibility message. The slide and reference log now state that conclusion rather than treating access as unknown.

**Rationale and coverage:** [Practice-feedback implementation record](practice_feedback_2026-09-11.md). [Source verification](references.md). [Visual provenance](../slides/image_plan.md). Private examples were inspected read-only; no private scientific topic or student identity was added to the manuscript case.

**Verification:** Rebuilt the 52-page PDF, rendered and inspected the complete deck, then re-rendered the final coursepack and radio-book changes. The final LaTeX log has no overfull/underfull boxes or warning messages. Confirmed the compiled slide 31 contains the direct Overleaf documentation hyperlink, slide 7 contains the ND Antigravity correction, and the submitted abstract is unchanged. The documentation checker and Git whitespace check pass. Reproduced the illustrative `latexdiff` from the distributed source pair.

**Remaining:** A timed rehearsal of the revised sequence, a pre-event product/policy recheck, optional handout production, and removing DRAFT when requested. No timed rehearsal or handout build was performed. Changes are committed locally; nothing was pushed.

### 2026-09-11: Audit slide layout refinements

- Slide 34: split prerequisites into small-font bullets and number the five audit questions.
- Slide 36: give Existing DOI and Missing DOI a shared fixed text width and minimum height, wrap supporting text, and use aligned right-angle branching/merging connectors.
- Rebuilt the 52-slide deck and visually checked both affected slides; no LaTeX layout warnings.

### 2026-09-11: Manuscript integration diagram

- Slide 37 now reads from Task 1 at the top to Task 5 at the bottom, with centered boxes sized to their text.
- Plus signs between Tasks 1–4 emphasize that their outputs combine; the downward arrow leads to the manuscript.
- Rebuilt and visually checked slide 37; no LaTeX layout warnings.

### 2026-09-11: Slide 40 title

- Adopted “Four Goals... Starting One Week Before the First Lecture.” The requested title fits on one line at the existing title size; rebuilt and visually checked slide 40.

### 2026-09-11: Audit goals heading

- Added “Audit Goals” above slide 34’s numbered questions, matching the prerequisites heading. Rebuilt and visually checked the layout.

### 2026-09-11: Larger audit slide text

- Increased slide 34 prerequisites from small to normal size and audit goals from normal to large. Tightened wording and spacing to preserve every check while keeping the larger text on single lines.
- Rebuilt and visually checked slide 34; content clears the footer and the build has no layout warnings.

### 2026-09-11: Larger manuscript integration text

- Increased slide 37 diagram text from scriptsize to small, preserving the centered, content-sized boxes, plus signs, and top-down order. Rebuilt and visually checked the slide; no layout warnings.

### 2026-09-11: Slide 38 agent contributions

- Replaced the project paragraph with “The agent can help...” and six bullets, preserving all contributions. Ended with the requested researcher decision statement. Rebuilt and visually checked slide 38.

### 2026-09-11: Shared box styling

- Renamed slide 39 to “Modernize my graduate elective” and removed bold emphasis from “applications.”
- Adopted its white interiors, 0.8pt ND gold outlines, rounded corners, and ND blue text across editable diagram and section-divider boxes. Highlighted boxes now use ND green outlines.
- Centralized the treatment in `nd box` / `nd highlight` TikZ styles and updated the style guide. Rebuilt the deck and visually reviewed all 12 affected slides; no LaTeX layout warnings.

### 2026-09-11: Getting started slide

- Renamed slide 52 to “Getting started later today.” Added creating Claude and GitHub accounts and installing GitHub Desktop plus Claude or ChatGPT as step 1; retained the previous steps as steps 2–4.
- Rebuilt and visually checked slide 52; no layout warnings.

### 2026-09-11: Project-specific first activity

- Slide 52 now explicitly offers Claude/ChatGPT for both accounts and installation. The activity explores this repository, then uses the getting-started interview to recommend resources for the participant's own research.
- Updated the companion prompt's introductory activity to match. Rebuilt and visually checked slide 52; no layout warnings.

### 2026-09-11: Editor build dependency fix

- The editor reported missing `fontawesome5.sty`, followed by an emergency stop. The command-line TeX installation could locate the package, suggesting a different editor TeX environment.
- Removed the dependency and replaced its check/cross/question symbols with standard LaTeX equivalents. The unused image placeholder now uses a text label.
- Rebuilt successfully without Font Awesome in the dependency recorder and visually checked slides 35 and 46–48. No LaTeX layout warnings. The editor itself still needs a new typeset run to verify its environment.

### 2026-09-11: TexpadTeX compatibility follow-up

- The supplied TexpadTeX log confirms the Font Awesome error is resolved. Its older LaTeX format rejects `\textquotesingle`; replaced that command on slide 7 with an ordinary apostrophe.
- Reduced trailing spacing on slides 37, 38, 39, 42, 44, and 46 by more than the small vertical excess reported by TexpadTeX. Preserved font sizes and content.
- The command-line build passes without warnings, and all seven changed slides were visually checked. TexpadTeX needs another run to confirm its engine-specific warnings are resolved.
