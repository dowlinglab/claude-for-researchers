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
| 1 | Inherited material maturing toward a manuscript | a hybrid-modeling adsorption project; a crystallization/design-of-experiments project; a membrane-transport project — inherited MATLAB code, spreadsheets, PowerPoint decks, and draft documents, reconstructed | **No** |
| 2 | Auditing a manuscript's final version | a first attempt at a manuscript audit (force-field properties); a sustainability-policy manuscript audit | **No** |
| 3 | Turning code into a released software product | `bits_for_gaps`, `emcal`, `grad-visit-scheduler` | **Yes** — public packages, no exposure |
| 4 | Literature review → project getting-started guide | a watershed decision-support project; a coastal desalination onboarding project | No *(assumed, not explicitly asked — flag if wrong; same conservative default as 1–2, both are sponsored/private)* |
| 5 | Crafting a proposal | a returning-sponsor proposal; a recurring sponsor program; a chromatography/digital-twin proposal | **No** — confirmed 2026-09-02: kept generic, same treatment as 1–2, since these may be live or competitively sensitive |
| 6 | Retooling and refreshing a course | **"Optimization for Decision Science"** (`ndcbe.github.io/optimization`) | **Yes** — confirmed 2026-09-02: Alex's own class, already-public course website |

Outside this taxonomy by design: the Prologue/Epilogue hobby material (`grad-visit-scheduler`'s teaser, the boot-dryer-octopus and kitchen-organizer stories, `radio-extra-book`) — deliberately a different, lower-stakes register, not another professional task type.

---

## Prologue — Tinker

**Revised 2026-09-03:** the hook (row 1) is now told in full here, across two slides with real visuals — not teased and held for Act II. Act II's own opener is now a one-line callback into the material it still owns exclusively: the group-wide impact. Row 2 below was stale — the hobby stories (boot-dryer-octopus, kitchen organizer) are Epilogue material, not Prologue; see that section.

| Concrete task | Example | Principle |
|---|---|---|
| Turn a personal annual chore into a published tool | `grad-visit-scheduler` — told in full here (type 3); Act II covers its group-wide impact | The habits that work on a weekend project are the same ones that work on research |
| Preview the six kinds of task before the acts use them | The six-types table above, previewed directly, no new examples | Every example today is one of six familiar kinds |

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

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | As promised — and why it mattered | Type 3 — `grad-visit-scheduler`, same example as the Prologue hook | A working proof, not a mandate, is what spreads a practice | `private_code_to_public_package.md` |
| 2 | Prototype → promote | Generic | Prototype in notebooks; promote what matures | `scientific_computing_workflow.md` §2 |
| 3 | Run it, pin it, baseline it | Type 1 — the hybrid-modeling, crystallization, and membrane-transport projects (generic); the last of these reconstructed from inherited MATLAB code, spreadsheets, PowerPoint decks, and draft documents, not just notebooks | Run it before you refactor it — and "it" may not be code at all | `scientific_computing_workflow.md` §3 |
| 4 | Freeze the science, move the code | Type 1, same three examples | Never change both at once | `scientific_computing_workflow.md` §4 |
| 5 | A regression harness is what made a reversed conclusion believable | Type 1 — the hybrid-modeling project's isotherm correction (generic); reinforced by the membrane-transport project's independent dual-implementation cross-check (faithful port vs. corrected port, validated against each other) | The harness is what makes a reversal attributable rather than suspicious | `scientific_computing_workflow.md` §3–§4 |
| 6 | Not just a hobby-adjacent tool | Type 3 — `emcal`, `bits_for_gaps`, named | Split by audience (package vs. archive), not by code quality | `private_code_to_public_package.md` §1 |
| 7 | Review the diff, not the summary | Generic | — | `working_with_ai_agents.md` §6 |
| 8 | The same discipline, on a document instead of code | Type 5 — a returning-sponsor proposal and a recurring sponsor program (generic): draft against the form, restore its wording, `\foacomment{}`-style inline review | AI as a compliance reviewer, findings inline, flagged → fixed → removed | `grant_proposal_writing.md` §2, §4 |
| 9 | Verify every revision before you commit | Type 5, same examples: `latexdiff`-against-last-commit, word-level | A normal re-read misses a softened claim; `latexdiff` doesn't | `grant_proposal_writing.md` §5, `resources/scripts/latexdiff_check.sh` |

## Act III — Challenge: it tells me I'm wrong

Six slides plus a two-part capstone, confirmed 2026-09-02 as the strongest structural addition this round: rather than scattering the course's Act II/III material as separate small beats, it closes the act as one integrated example.

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | Separate arithmetic, method, transcription | Type 2 — both manuscript audits (generic) | Merging them reads as an attack | `manuscript_audit.md` §1 |
| 2 | Trace every number back to the file that produced it | Type 2, same examples | The claim-tracing table | `manuscript_audit.md` §4 |
| 3 | "Cannot verify" is a result you want to get | Type 2, same examples | — | `manuscript_audit.md` §5 |
| 4 | A clean build hid a silent failure | Type 2 (an empty nomenclature table, exit code 0), type 6 (a stale `.gitignore` rule dropped a build artifact for 1.5 days, CI stayed green), **and** a project's own `CLAUDE.md` warning about stale absolute paths directly above four stale absolute paths (restored 2026-09-02 from `02_context.tex`'s "honest limit" frame, folded in here rather than kept separate) — three domains, one lesson | Read the rendered output, never the log or the exit status | `manuscript_audit.md` §8 |
| 5 | My own status report was wrong; the fix was a script | Type 2, same audit | Determine status from evidence, never recollection | `manuscript_audit.md` §7 |
| 6 | **Capstone, part 1** — the Act I argument, taken all the way | Type 6, named: the same course, now converted (handwritten notes → LaTeX, the coursepack) and challenged (an adversarial verification pass catches a real, decade-old sign error) | One project, watched end to end, across Understand → Build → Challenge | `manuscript_audit.md` §10 |
| 7 | **Capstone, part 2** — the verifier needed verifying too | Type 6, same course: one of the verification pass's own three checks needed correcting | The checker needs checking — same principle as the audit's own self-correction appendix, now a second domain | `manuscript_audit.md` §10 |

## Epilogue — Trust

Rows 2-3 moved in from the Prologue 2026-09-03, Alex's suggestion — they read as "Trust" material (what's safe to run through which tool) rather than Prologue scoping.

| # | Concrete task | Example | Principle |
|---|---|---|---|
| 1 | Return to the hook's unresolved question | `grad-visit-scheduler`'s own "how do we train the next generation" line | Sit with the tension; don't resolve it artificially |
| 2 | Know your data classification | Notre Dame's tier table + which tools are approved through which tier | Trust the tool the institution has actually vetted, not the one that's fastest |
| 3 | Two checks before you start | DoD/DoW funding status; "ask your PI" | Institutional trust has real, project-specific limits |
| 4 | **The summary matrix** — projects × acts, visualized | A simplified grid built from the six-types table above | A handful of real projects recur across every act; this isn't asserted, it's shown |
| 5 | You own every claim, whatever helped you make it | Generic, group-manual GenAI section | — |
| 6 | The hobby stories, as the final example | boot-dryer-octopus; kitchen organizer/telescope; `radio-extra-book` | The same discipline pays off outside the lab too |
| 7 | One thing to change Monday morning | Pointer to the repo | — |

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
- ~~Slide count vs. budget~~ — this file no longer tracks the running count; `slides/storyboard.md`'s "At a glance" table is authoritative (currently 44 slides, ~48 min, against a 35-40 slide / ~40-minute-talk target — over budget, rehearsal-driven trimming still pending).
