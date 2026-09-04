# Demo ideas — the project inventory, mapped to acts

**Supersedes the pre-restructure version of this file**, which was written for the six-stage lifecycle framing (Explore/Ground/Build/Record/Write/Verify) before the talk became a three-act story (`storyboard.md`). That framing is gone; the underlying evidence isn't — this file re-maps it.

**What this file is for.** The Acts are meant to be a *collection of concrete tasks an academic actually performs*, each grounded in a real project, with a general principle extracted from it — not one flagship story per act. This is the map from raw evidence (17 projects/repos inventoried, most already generalized into `resources/practices/`) to which act each concrete task belongs in, and what principle it earns its place by demonstrating.

**Naming convention — confirmed 2026-09-02, per example type (see below).** Public repos stay named regardless of type. Everything else follows the decision recorded for its type; nothing is named by default.

**Status:** all 17 projects inventoried; example roster and naming confirmed; both this file and `storyboard.md` updated to match.

---

## The six example types

The confirmed roster. Every concrete task below belongs to one of these.

| # | Type | Examples | Named? |
|---|---|---|---|
| 1 | Inherited material maturing toward a manuscript | a hybrid-modeling adsorption project; a crystallization/design-of-experiments project; a membrane-transport project — inherited MATLAB code, spreadsheets, PowerPoint decks, and draft documents, reconstructed | **No** — the membrane-transport project also grounds Act I's Task 2; the hybrid-modeling adsorption project also grounds Act III's Task 6 (rebuilt 2026-09-04, revision #8 — has a real drafted manuscript, unlike the other two which are still "figuring out the science") |
| 2 | Auditing a manuscript's final version | a first attempt at a manuscript audit (force-field properties); a sustainability-policy manuscript audit | **No** |
| 3 | Turning code into a released software product | `bits_for_gaps`, `emcal`, `grad-visit-scheduler` | **Yes** — public packages, no exposure |
| 4 | Literature review → project getting-started guide | a watershed decision-support project; a coastal desalination onboarding project | No *(assumed, not explicitly asked — flag if wrong; same conservative default as 1–2, both are sponsored/private)* |
| 5 | Crafting a proposal | a returning-sponsor proposal; a recurring sponsor program; a chromatography/digital-twin proposal | **No** — confirmed 2026-09-02: kept generic, same treatment as 1–2, since these may be live or competitively sensitive |
| 6 | Retooling and refreshing a course | **"Optimization for Decision Science"** (`ndcbe.github.io/optimization`) | **Yes** — confirmed 2026-09-02: Alex's own class, already-public course website |

Outside this taxonomy by design: the Prologue's `grad-visit-scheduler` teaser (told in full there, not a numbered task). The Epilogue's hobby material (the boot-dryer-octopus and kitchen-organizer stories, `radio-extra-book`) carries its own real number, **Task 8 (hobbies)** — Alex's own call, 2026-09-04 — but deliberately outside the professional Task 1-7 taxonomy: it doesn't appear in the Prologue's task preview or the Epilogue's summary matrix.

---

## Prologue — Tinker

**Revised 2026-09-03:** the hook (row 1) is now told in full here, across two slides with real visuals — not teased and held for Act II. Act II's own opener is now a one-line callback into the material it still owns exclusively: the group-wide impact. The archetypes preview (row 2) was briefly its own slide, then folded into the "not a tool tutorial" scoping slide the same day, replacing that slide's act-strip diagram — Alex's call, now `style_guide.md` rule 9: the act-strip repeated the roadmap slide's outline and added nothing, and the freed space was better spent foreshadowing the acts.

| Concrete task | Example | Principle |
|---|---|---|
| Turn a personal annual chore into a published tool | `grad-visit-scheduler` — told in full here (type 3); Act II covers its group-wide impact | The habits that work on a side project are the same ones that work on research |
| Preview the six kinds of task before the acts use them | The six-types table above, previewed directly, no new examples — shares a slide with the "not a tool tutorial" scoping content | Every example today is one of six familiar kinds |
| Desktop app, terminal, or editor extension | Generic — no project example, just the three surfaces themselves | Same engine, three doors; pick based on workflow, not mystique |
| Which model, and how much of it do you get | Generic — current frontier models and how each vendor meters usage, verified via web search 2026-09-04 (re-check before the talk) | Neither publishes a token budget; the mid-tier model is usually the right default |

## Act I — Understand: conversation → living context, with git

**The organizing device**, confirmed 2026-09-02: two parallel transitions, both "an ephemeral, unbacked-up thing becomes a durable, versioned one." A chat conversation → a repository of literature with validated claims. A local notebook with no backup → git.

**Act I's role, sharpened 2026-09-02: a sell, not a payoff.** Its one argument is that version control is the prerequisite that unlocks what Codex/Claude Code can do — not a demonstrated outcome. The mature-example slide (originally planned here, showing "Optimization for Decision Science"'s well-kept `CLAUDE.md`) was **cut from Act I entirely** rather than kept as an early teaser, so the act doesn't dilute its own sell with a taste of the payoff. That example now appears fresh in Act III's capstone instead of being planted here first.

Slides 4-5 restored 2026-09-02 from `02_context.tex`'s original "three kinds of context" and project-file frames, which predated the three-act restructure and had been dropped when it happened — Alex's call to bring them back rather than treat them as redundant with slide 3. Built in `slides/sections/02_act1_understand.tex`, which replaces `02_context.tex` (removed); that file's fifth frame, the "honest limit" story, still needs to land in Act III once that file exists.

**Cut 2026-09-03** at Alex's request (too in-the-weeds, more room for visual examples elsewhere): the old opening row, "a plan that lived only in a conversation" — the real, verified `emcal` commit `31184f4`. Its point ("the repository is the source of truth; a conversation about the project is not") still stands via row 1 below. Row 2 (git/GitHub explainer) no longer calls back to the cut commit slide; it introduces the same `emcal` commit fresh instead.

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | State the shift | Conversation vs. repository, generally | The filesystem is the source of truth | `working_with_ai_agents.md` §1 |
| 2 | Explain what git/GitHub actually give you | Anchored to a real commit, introduced fresh: `dowlinglab/emcal` `31184f4` — what a commit is, what a repository is, what GitHub adds (hosted, shared, backed up) | A specific, nameable fix, not a vague "be better organized" | — |
| 3 | Three kinds of context: persistent, authoritative, task | Type 1 — the same membrane-transport/diafiltration project as row 4, named concretely for each kind (conventions, the actual data/model, this run's question) rather than stated as abstract taxonomy | A chat history is a poor substitute for any of the three | `working_with_ai_agents.md` §2 |
| 4 | One file, read at the start of every session | Type 1 — the membrane-transport/diafiltration project's actual `CLAUDE.md`, continuing row 3's example rather than switching to a new one | Name it neutrally; `CLAUDE.md`/`AGENTS.md` become three-line pointers to it | `working_with_ai_agents.md` §2 |
| 5 | Parallel A, idea-first: a chat conversation crossing two literatures on purpose | Type 5 — the chromatography/digital-twin proposal (generic) | Bring in a second literature specifically to pressure-test an idea, not incidentally | `literature_review.md` §2 |
| 6 | Parallel A, corpus-first: a folder of PDFs → an onboarding report, claims validated | Type 4 — the watershed and desalination projects (generic) | Interpret how the evidence changes a project decision — don't copy the abstract | `literature_review.md` §4, §9 |
| 7 | Parallel B, closing the act: a local notebook with no backup → git | Generic "inherited project" case — a departed collaborator's unversioned work | Version control is the prerequisite — what it unlocks is the rest of this talk | `scientific_computing_workflow.md` §2 |

## Act II — Build: it changes what you keep

Row 1 expanded 2026-09-02, then **merged into a single callback row 2026-09-03**: the notebook behind `grad-visit-scheduler` predates the AI story by years, co-created with **Jeff Kantor** for their own use (credited the same way the package's own PyPI page credits him — no added biographical detail). The AI conversion started as a narrow test (could Codex format the input data?) before becoming a full package in ~10 hours, and that success is what got Alex's whole group access to Codex — a direct causal result, not incidental color. That whole story now lives in the Prologue hook instead (told in full there, with real visuals); this act's old two-row opener collapsed into one row that just calls back and moves straight to the group-impact material, which is still exclusively Act II's.

**REFRESHED 2026-09-04** — rows 1–6 below replace an earlier, generic version of this table (Prototype → promote / Run it, pin it, baseline it / Freeze the science, move the code / A regression harness…) written before Task 4 was rebuilt around `bits_for_gaps`' real, git-verified phase history. That generic framing is gone from the slides (storyboard.md's own comment: "Phase 4's decomposition **is** 'promote what matures,' Phase 9c's behavior-preserving hardening **is** 'freeze the science, move the code'"); this table was never updated to match until now.

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | Task 4 opens on the paper | Type 3 — `bits_for_gaps`, **Dr. Kyla Jones**, named | Celebration first, packaging second | `private_code_to_public_package.md` |
| 2 | The recipe, in the order it actually happened | Type 3, same — reconstructed from the real repo's own git history and its since-deleted, git-recoverable `HANDOFF.md`/`REFACTOR_PLAN.md`: 13 phases executed against 10 planned, four (9b–9e) proposed live, one at a time | The plan held for eight phases, then grew four more | `scientific_computing_workflow.md` §1–§4 |
| 3 | Baseline before touching anything | Type 3, same — Phase 2 (regression harness), Phase 4 STEP 0 (pinned exact-value baseline) | Run it before you refactor it — prove you can reproduce it first | `scientific_computing_workflow.md` §3 |
| 4 | Decompose, generalize, port | Type 3, same — Phase 4 (decompose `sampler.py`), Phase 5 (1D/3D → N-D), Phase 6 (the paper's own VLE/distillation example) | Promote what matures | `scientific_computing_workflow.md` §2, §4 |
| 5 | The bug the reproduction found | Type 3, same — Phase 9b: a from-scratch figure reproduction flagged a discrepancy, confirmed as a shared-mutable-state bug (a GP kernel mutated in place, then reused) | A regression harness is what makes a reversal attributable rather than suspicious | `scientific_computing_workflow.md` §3–§4 |
| 6 | Ship the skeleton, scrub the scaffolding | Type 3, same — trusted publishing via OIDC; `HANDOFF.md`/`REFACTOR_PLAN.md` removed before release, recoverable from git history | Move to the archive, not out of history | `private_code_to_public_package.md` §10 |
| 7 | Not just a hobby-adjacent tool | Type 3 — `emcal`, `bits_for_gaps`, named | Split by audience (package vs. archive), not by code quality | `private_code_to_public_package.md` §1 |
| 8 | One manuscript, three places, one history | Generic — distilled (not quoted) from the Dowling Lab group manual's own Overleaf/LaTeX policy: one Overleaf project per manuscript synced to one GitHub repo, local editing via GitHub sync (never a direct Overleaf download), `todonotes` for open items in the PDF itself | GitHub is the archive; Overleaf is where you draft | — (manual stays lab-internal) |
| 9 | The same discipline, on a document instead of code | Type 5 — a returning-sponsor proposal and a recurring sponsor program (generic): draft against the form, restore its wording, `\foacomment{}`-style inline review | AI as a compliance reviewer, findings inline, flagged → fixed → removed | `grant_proposal_writing.md` §2, §4 |
| 10 | Best practices: review the diff, verify every revision | Generic — an AI-written summary vs. the actual diff, plus `latexdiff`-against-last-commit, word-level | The diff says what actually changed; a normal re-read misses what `latexdiff` catches | `working_with_ai_agents.md` §6, `grant_proposal_writing.md` §5, `resources/scripts/latexdiff_check.sh` |

## Act III — Challenge: it tells me I'm wrong

**RESTRUCTURED 2026-09-04** — Task 5 gained a walkthrough slide (rows 1–2 below now cover what used to be a single "separate the three questions" row, and the old 3-column framing is gone). A new Task 6 (generic, rows 7–9) was inserted — home for three practice files (`technical_writing.md`, `writing_style_guide.md`, `scientific_figures_tables.md`) that had no live task anywhere in the talk until now. The old two-slide Type-6 capstone (rows 6–7 in the prior version of this table) is cut entirely and replaced by Task 7, rows 10–15 — six slides built from a freshly authorized audit of the real `optimization`/`optimization-private` repo pair, not the generic "adversarial verification pass" version this table used to describe.

**Task 6 REBUILT AGAIN, same day (revision #8)** — rows 7–9 originally continued the membrane-transport project (Type 1, row 1), but that project is still "figuring out the science" (Task 2 territory). The hybrid-modeling adsorption project (also row 1) has a real drafted manuscript instead, so it anchors Task 6 now, with the Task 2 and Task 3 callbacks made explicit in the frame titles rather than left implicit. `scientific_figures_tables.md` moved off Task 6 entirely — it's anchored by Task 7 (row 11) instead, unaffected by this change.

**Row 4 added same night**, from a parallel audit wave over other roster projects: two independent real manuscript audits (a technical paper, a policy paper) each turned up a citation-tracing failure of the same shape as the existing claim-tracing table, generalized here with no repo/student names.

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | Task 5 — audit a manuscript before it's submitted | Type 2 — both manuscript audits (generic); five real audit questions | Ask them separately — together they read as an attack | `manuscript_audit.md` §1 |
| 2 | Task 5 — walk it through, one question at a time | Type 2, same — mechanics, not a transcript: point Claude at the manuscript and repo, one question at a time | The audit is only as good as the files you hand it | `resources/prompts/manuscript_audit.md` |
| 3 | Task 5 — trace every number back to the file that produced it | Type 2, same examples | The claim-tracing table; "cannot verify" is a result you want | `manuscript_audit.md` §4, §5 |
| 4 | Task 5 — the same table works on a citation | Type 2 **and** type 5 (two independent real audits, a technical paper and a policy paper, each caught a citation-tracing failure of this shape) | A citation is a claim too — verified or wrong, not close enough | `resources/scripts/doi_checker/`, `manuscript_audit.md` §12 |
| 5 | Task 5 — a clean build hid a silent failure | Type 2 (an empty nomenclature table, exit code 0), type 6 (a stale `.gitignore` rule dropped a build artifact for 1.5 days, CI stayed green), **and** a project's own `CLAUDE.md` warning about stale absolute paths directly above four stale absolute paths | Read the rendered output, never the log or the exit status | `manuscript_audit.md` §8 |
| 6 | Task 5 — my own status report was wrong; the fix was a script | Type 2, same audit | Determine status from evidence, never recollection | `manuscript_audit.md` §7 |
| 7 | Task 6 — inherited a notebook, understood before it changed (Task 2) | Type 1, generic — the hybrid-modeling adsorption project (rebuilt 2026-09-04, revision #8; not the membrane-transport project) | A one-day handoff; three weeks reproducing fifteen numbered experiments before anything was corrected | `technical_writing.md` |
| 8 | Task 6 — verify the literature the same way you verify the code (Task 3) | Type 1, same | 76 cited papers checked against their own PDFs; six wrong, one with the finding stated backwards | `literature_review.md`, `writing_style_guide.md` |
| 9 | Task 6 — the manuscript audits itself, before anyone else does | Type 1, same | 25 discrepancies found against its own code and data, 22 fixed, 3 left explicitly flagged | `manuscript_audit.md`, `resources/templates/results_manifest.md` |
| 10 | Task 7 — a week before the semester, at scale | Type 6, named — `optimization`/`optimization-private`: ~1,450 commits in 2.5 weeks, 98% of the private repo's entire history | The same shape as the Prologue's hook — years of patches, then a burst | — |
| 11 | Task 7 — retire the scan, own the figure | Type 6, same — JupyterBook 1→2; eight orphaned textbook scans deleted, three redrawn in TikZ, five book tables replaced with native Markdown | A figure the repo can regenerate beats one it can only redisplay | `scientific_figures_tables.md`, `resources/scripts/figure_style/` |
| 12 | Task 7 — ink to LaTeX, verified page by page | Type 6, same — a 45-page annotated instructor PDF, rendered and read one page at a time | The ink, not just the typing that describes it | — |
| 13 | Task 7 — an overnight report, self-auditing as it went | Type 6, same — a false journal citation caught against `MyPublications.bib`; a refused Simon-1960 page number; a self-corrected citation count (79 → 75) | Written as the work happened — and it audited itself | `manuscript_audit.md` §3, §4, §7 |
| 14 | Task 7 — close the flag where the flag lives | Type 6, same — the course's own `CLAUDE.md`, "four instances in one day" | A commit message is a record, not a notification | `working_with_ai_agents.md` §9 |
| 15 | Task 7 — pick the tool for the task, grounded in evidence | Type 6, same — a prose-trim job handed to Codex/GPT-5.6, briefed with real diffs of Alex's own hand-edits | The brief came from evidence — the tool came second | `writing_style_guide.md` (callback) |

## Epilogue — Trust

Rows 2-3 moved in from the Prologue 2026-09-03, Alex's suggestion — they read as "Trust" material (what's safe to run through which tool) rather than Prologue scoping.

| # | Concrete task | Example | Principle |
|---|---|---|---|
| 1 | Return to the hook's unresolved question | `grad-visit-scheduler`'s own "how do we train the next generation" line | Sit with the tension; don't resolve it artificially |
| 2 | Know your data classification | Notre Dame's tier table + which tools are approved through which tier | Trust the tool the institution has actually vetted, not the one that's fastest |
| 3 | Two checks before you start | DoD/DoW funding status; "ask your PI" | Institutional trust has real, project-specific limits |
| 4 | **The summary matrix** — projects × acts, visualized | A simplified grid built from the six-types table above | A handful of real projects recur across every act; this isn't asserted, it's shown |
| 5 | You own every claim, whatever helped you make it | Generic, group-manual GenAI section; the disclosure bullet folds in a real editorial decision (2026-09-04 audit wave: a project's own revision notes record deciding to name AI use as a research method, at the PI's own call) | Journals increasingly expect it, not just tolerate it |
| 6 | Task 8 (hobbies), the final example | boot-dryer-octopus; kitchen organizer/telescope; `radio-extra-book` | The same discipline pays off outside the lab too |
| 7 | One thing to change tomorrow morning | Pointer to the repo | — |
| 8 | So, what now? (final slide) | Generic — the concrete five-step call to action; cites the new `resources/prompts/getting_started.md` | The resources are what your chatbot builds on, not a tutorial to finish |

---

## Resolved this round (2026-09-02)

- ~~The multi-agent spend-limit-kills-agents-mid-task incident~~ — added to `working_with_ai_agents.md` §6.
- ~~The `\fillin` redaction mechanism~~ — out of scope, lecture-specific, stays slide-only.
- ~~The AI-review-status disclosure tracker~~ — generalized into `working_with_ai_agents.md` §10.
- ~~Act II's "what else" candidates from the teaching sweep~~ — resolved: none added. Act II's existing 9 slides already cover the Build principle set; the teaching-sweep material is better spent as the Act III capstone.
- ~~Where does the course material go~~ — resolved, then revised 2026-09-02: Act III alone carries it, as the two-part capstone. The originally planned Act I plant (the `CLAUDE.md`) was cut once Act I was reframed as a sell, not a payoff — the course now appears fresh in Act III instead of being teased earlier.
- ~~Naming for types 5 and 6~~ — resolved: type 5 generic, type 6 named ("Optimization for Decision Science").
- ~~Act I's role~~ — resolved 2026-09-02: a sell (git as the prerequisite that unlocks Codex/Claude Code), not a payoff. 7 slides → 6.
- ~~Type 1's roster~~ — resolved 2026-09-02: added a third example, the membrane-transport project (`data3`), kept generic like its two siblings — naming it alone would have created an unhelpful asymmetry with no real narrative gain.

## Still open

- **Type 4's naming** was not explicitly asked about; assumed generic by the same conservative default as types 1–2. Confirm or correct.
- ~~Slide count vs. budget~~ — this file no longer tracks the running count; `slides/storyboard.md`'s "At a glance" table is authoritative (currently 43 slides, ~47.5 min, against a 35-40 slide / ~40-minute-talk target — over budget, but Alex confirmed 2026-09-03 he isn't worried about the count while there's still this much editing left; rehearsal-driven trimming still pending).
