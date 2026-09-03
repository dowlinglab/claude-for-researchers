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

| Concrete task | Example | Principle |
|---|---|---|
| Turn a personal annual chore into a published tool | `grad-visit-scheduler` — teased here (type 3), resolved in full in Act II | The habits that work on a weekend project are the same ones that work on research |
| Tinker with a hobby project using AI for the first time | boot-dryer-octopus, kitchen organizer | Curiosity and low stakes are a feature, not a consolation prize |

## Act I — Understand: conversation → living context, with git

**The organizing device**, confirmed 2026-09-02: two parallel transitions, both "an ephemeral, unbacked-up thing becomes a durable, versioned one." A chat conversation → a repository of literature with validated claims. A local notebook with no backup → git.

**Act I's role, sharpened 2026-09-02: a sell, not a payoff.** Its one argument is that version control is the prerequisite that unlocks what Codex/Claude Code can do — not a demonstrated outcome. The mature-example slide (originally planned here, showing "Optimization for Decision Science"'s well-kept `CLAUDE.md`) was **cut from Act I entirely** rather than kept as an early teaser, so the act doesn't dilute its own sell with a taste of the payoff. That example now appears fresh in Act III's capstone instead of being planted here first.

Slides 4-5 restored 2026-09-02 from `02_context.tex`'s original "three kinds of context" and project-file frames, which predated the three-act restructure and had been dropped when it happened — Alex's call to bring them back rather than treat them as redundant with slide 3. The `02_context.tex` file itself still needs to be split apart and rewritten into this table's slides plus Act III's, not done yet.

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | Open on the failure: a plan that lived only in a conversation | The real, verified commit: `dowlinglab/emcal` `31184f4` — "See conversation for the full KEEP/REMOVE inventory" | The repository is the source of truth; a conversation about the project is not | `working_with_ai_agents.md` §1 |
| 2 | State the shift | Conversation vs. repository, generally | The filesystem is the source of truth | `working_with_ai_agents.md` §1 |
| 3 | Explain what git/GitHub actually give you | Anchored to the same `emcal` commit — what a commit is, what a repository is, what GitHub adds (hosted, shared, backed up) | The fix to slide 1's failure is a specific, nameable thing, not a vague "be better organized" | — |
| 4 | Three kinds of context: persistent, authoritative, task | Type 1 — the same membrane-transport/diafiltration project as slide 5, named concretely for each kind (conventions, the actual data/model, this run's question) rather than stated as abstract taxonomy | A chat history is a poor substitute for any of the three | `working_with_ai_agents.md` §2 |
| 5 | One file, read at the start of every session | Type 1 — the membrane-transport/diafiltration project's actual `CLAUDE.md`, continuing slide 4's example rather than switching to a new one | Name it neutrally; `CLAUDE.md`/`AGENTS.md` become three-line pointers to it | `working_with_ai_agents.md` §2 |
| 6 | Parallel A, idea-first: a chat conversation crossing two literatures on purpose | Type 5 — the chromatography/digital-twin proposal (generic) | Bring in a second literature specifically to pressure-test an idea, not incidentally | `literature_review.md` §2 |
| 7 | Parallel A, corpus-first: a folder of PDFs → an onboarding report, claims validated | Type 4 — the watershed and desalination projects (generic) | Interpret how the evidence changes a project decision — don't copy the abstract | `literature_review.md` §4, §9 |
| 8 | Parallel B, closing the act: a local notebook with no backup → git | Generic "inherited project" case — a departed collaborator's unversioned work | Version control is the prerequisite — what it unlocks is the rest of this talk | `scientific_computing_workflow.md` §2 |

## Act II — Build: it changes what you keep

No structural change from the prior pass. Confirms which types ground which slides.

| # | Concrete task | Example | Principle | Practice file |
|---|---|---|---|---|
| 1 | The hook, in full | Type 3 — `grad-visit-scheduler`: Codex, real dates/versions, a 20-minute live feature add | Ship the skeleton early; TODO notes committed into the docs are a durable review mechanism | `private_code_to_public_package.md` |
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

| # | Concrete task | Example | Principle |
|---|---|---|---|
| 1 | Return to the hook's unresolved question | `grad-visit-scheduler`'s own "how do we train the next generation" line | Sit with the tension; don't resolve it artificially |
| 2 | **The summary matrix** — projects × acts, visualized | A simplified grid built from the six-types table above | A handful of real projects recur across every act; this isn't asserted, it's shown |
| 3 | You own every claim, whatever helped you make it | Generic, group-manual GenAI section | — |
| 4 | The hobby stories, as the final example | boot-dryer-octopus; kitchen organizer/telescope; `radio-extra-book` | The same discipline pays off outside the lab too |
| 5 | One thing to change Monday morning | Pointer to the repo | — |

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
- **Slide count vs. budget**, per `storyboard.md`: current total is 35 (Prologue 7, Act I 6, Act II 9, Act III 7, Epilogue 5), ~41.5 min. Needs a real per-minute check once `sections/*.tex` are rewritten against this structure.
