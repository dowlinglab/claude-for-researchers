# Demo ideas — the project inventory, mapped to acts

**Supersedes the pre-restructure version of this file**, which was written for the six-stage lifecycle framing (Explore/Ground/Build/Record/Write/Verify) before the talk became a three-act story (`storyboard.md`). That framing is gone; the underlying evidence isn't — this file re-maps it.

**What this file is for.** The Acts are meant to be a *collection of concrete tasks an academic actually performs*, each grounded in a real project, with a general principle extracted from it — not one flagship story per act. This is the map from raw evidence (17 projects/repos inventoried, most already generalized into `resources/practices/`) to which act each concrete task belongs in, and what principle it earns its place by demonstrating.

**Naming convention**, consistent with `resources/practices/`: **public repos are named** (Alex's own or fully public, no student exposure — `emcal`, `bits_for_gaps`, `grad-visit-scheduler`, `radio-extra-book`, `optimization`/`optimization-private`). **Private, unpublished, or student-adjacent work stays generic** — a domain descriptor ("a hybrid-modeling project," "a membrane-transport project," "a returning-sponsor proposal"), never a repo name or a student reference. No exceptions either direction.

**Status:** all 17 projects inventoried.

---

## Master inventory

| Project | Public? | Domain | Primary act |
|---|---|---|---|
| CDSE hybrid-modeling project | private | hybrid modeling (adsorption) | Act I (support), Act III |
| BITS for GAPS / `bits_for_gaps` | **public** | Bayesian experimental design | Act II |
| GPBO / `emcal` | **public** | Bayesian optimization for calibration | Act I, Act II |
| First manuscript audit (ESS-FO-Audit) | private | force-field / thermophysical properties | Act III |
| SAF Brazil manuscript audit | private | sustainable aviation fuel policy | Act III |
| Grey-box identifiability paper | private | hybrid model identifiability | Act I, Act III |
| Crystallization / Pyomo.DoE project | private | crystallization, design of experiments | Act II, Act III |
| Membrane transport project (data3) | private | membrane transport / diafiltration | Act II, Act III |
| `grad-visit-scheduler` | **public** | admissions-visit scheduling (MILP) | Prologue, Act II |
| Chromatography digital-twin proposal | private | chromatography + digital twins | Act I |
| Watershed decision-support project | private | watershed modeling, sensor design | Act I |
| Coastal desalination onboarding project | private | desalination process design | Act I |
| A returning-sponsor proposal (Genesis) | private | materials/energy (unspecified) | Act II |
| A multi-year proposal program (CPM) | private | AI-agent-based process tools | Act II |
| `radio-extra-book` | **public** | amateur radio exam study guide | Epilogue |
| 3D-printing hobby projects | personal | boot-dryer, kitchen organizer | Prologue, Epilogue |
| `optimization-private` / `optimization` | course dev. (private/public pair) | optimization course materials | Act I, Act II, Act III |

---

## Prologue — Tinker

| Concrete task | Example | Principle |
|---|---|---|
| Turn a personal annual chore into a published tool | `grad-visit-scheduler` (teased here, resolved in Act II) | The habits that work on a weekend project are the same ones that work on research — tinkering is where you build the muscle memory cheaply |
| Tinker with a hobby project using AI for the first time | boot-dryer-octopus, kitchen organizer | Curiosity and low stakes are a feature, not a consolation prize |

## Act I — Understand: it explains things to me

| Concrete task | Example | Principle | Practice file |
|---|---|---|---|
| Get inherited/old code running again before restructuring it | CDSE project; grey-box identifiability | Run it before you refactor it — you cannot restructure code you haven't watched execute | `scientific_computing_workflow.md` §3 |
| Reconstruct a project's history from files, not memory | CDSE's group report, built from README + running notes + git log, explicitly credited as "evidence, not memory" | The repository is the source of truth; a conversation about the project is not | `working_with_ai_agents.md` §1 |
| Explore a new research idea by crossing two literatures on purpose | Chromatography digital-twin proposal (chromatography literature + a second, deliberate pass on LLM-agents-in-chemistry) | Bring in a second literature specifically to pressure-test an idea, not incidentally | `literature_review.md` §2 |
| Turn a collected literature folder into an onboarding report for the next person | Watershed project; desalination project | Interpret how the evidence changes a project decision — don't copy the abstract | `literature_review.md` §4, §9 |
| Verify a stated claim against a primary source before teaching it | Optimization course: lecture-note claims checked against a textbook + its own errata sheet, with an independent adversarial second pass that isn't the same agent that wrote the lecture | The same discipline that audits a manuscript claim audits a lecture-note claim — the audience doesn't change the method | `manuscript_audit.md` §4, §5 |
| A context file that stays current, for once | Optimization course `CLAUDE.md`: every rule is attached to a dated, named incident, and corrections are kept in place rather than deleted | Rules with no incident record read as boilerplate and rot; a rule with "here is the day this cost real work" attached gets re-verified | `working_with_ai_agents.md` §2, §9 |
| Fact-check an institutional policy claim against its primary source | (Meta-example: this talk's own ND AI-policy slide, verified against `ai.nd.edu` directly rather than trusted from a search summary) | Authoritative claims get checked at the source, even when — especially when — the claim is about your own institution | `notes/references.md` |

## Act II — Build: it changes my artifacts

| Concrete task | Example | Principle | Practice file |
|---|---|---|---|
| Convert an internal tool into a tested, documented, released package | `grad-visit-scheduler` (the hook, resolved in full: Codex, real dates/versions, a 20-minute live feature add) | Ship the skeleton early; TODO notes committed into the docs are a durable review mechanism | `private_code_to_public_package.md` |
| The same conversion, on published research code, not a personal tool | `emcal`, `bits_for_gaps` | Split by audience (package vs. archive), not by code quality | `private_code_to_public_package.md` §1 |
| Capture a numerical baseline before refactoring, then prove the refactor didn't change the science | Membrane transport project; crystallization project; grey-box identifiability project — three independent instances of the same pattern | Freeze the science, move the code — never both at once | `scientific_computing_workflow.md` §3–§4 |
| Convert handwritten source material into a structured digital artifact | Optimization course: handwritten lecture notes → transcribed → typeset LaTeX, with duplicate scans verified byte-identical before deletion | The same "promote what matures" move, applied to a medium change instead of a language change | `scientific_computing_workflow.md` §2 |
| Migrate a whole toolchain, not just a codebase | Optimization course website: JupyterBook v1 → MyST v2, cutover compressed into one afternoon | Keep the old path alive for exactly one safety-net commit, then delete it deliberately once the new one is verified — not a long parallel-build period | `scientific_computing_workflow.md` §4 |
| Generate two versions of one document, safely, from one source | Optimization course: instructor/student coursepack from one `.tex` file, with a redaction macro that measures the answer text and replaces it with an identically-sized invisible rule — plus a mechanical leak-checker, because a prior year's white-on-white redaction left the answer text copyable | Never redact by color; measure and replace, then verify mechanically, not visually | `scientific_figures_tables.md` (redaction as a figure/document-integrity problem) |
| Share one figure/code source across two repositories without duplicating it | Optimization course: TikZ and matplotlib sources live once in the public repo, `\input`/extracted into the private repo's LaTeX handouts; a git submodule was considered and explicitly rejected (a pointer-bump commit per edit, an empty directory for students). A real bug this caught: a TikZ figure rendered fine standalone but broke the actual handout, because a required `\usetikzlibrary` was only loaded by the standalone wrapper, not the shared source | "Generation alone guarantees nothing... without a checker, 'single source of truth' is a claim; with one, it is an invariant" | `scientific_figures_tables.md` §5 |
| Keep one "golden" copy of code that appears in two places (a notebook and a document) | Optimization course: the Pyomo model lives once in the notebook; the LaTeX handout extracts it, gated by a content-hash staleness check | Regenerate, don't retype — extended from tables to embedded code | `scientific_figures_tables.md` §6 |
| Track, and disclose to the audience, which content is AI-drafted and not yet reviewed | Optimization course: a maintained per-item status (`unreviewed`/`reviewed`/`reviewed-stale`/`exempt`) drives a live banner shown to students on any AI-drafted page the instructor hasn't signed off on yet | Disclosure can be a running, visible state, not just a one-time statement — practiced on students the same way it's asked of researchers with reviewers | *(candidate for a new resource — see notes below)* |
| Guard against an AI's voice contaminating content that should stay human | Optimization course: a check specifically watches for the AI-heavy lecture-note prose "leaking backward" into the notebooks' pre-existing human-voice corpus | A style guide isn't just what to write toward — it's also a boundary to actively defend | `writing_style_guide.md` §3 |
| Publish a concrete, per-assignment AI-use policy to the people whose work you're grading | Optimization course syllabus: per-assignment labels (no AI / AI after an independent attempt / AI required), plus a required "AI and independent-work report" on every homework | State the policy at the level of the actual assignment, not once in a syllabus paragraph nobody rereads | group manual GenAI section; `working_with_ai_agents.md` §10 |
| Draft a proposal against a sponsor's own form, then restore its exact wording | The Genesis proposal; the multi-year CPM program | Draft tersely against the form first; restore the sponsor's own language before submission | `grant_proposal_writing.md` §2 |
| Verify a revision with a word-level diff before committing | The Genesis proposal (reconstructed practice, now a real script) | A normal re-read misses a softened claim; `latexdiff` doesn't | `grant_proposal_writing.md` §5, `resources/scripts/latexdiff_check.sh` |

## Act III — Challenge: it tells me I'm wrong

| Concrete task | Example | Principle | Practice file |
|---|---|---|---|
| Audit every quantitative claim in a manuscript against its results | First manuscript audit; SAF Brazil audit | Separate arithmetic, method, and transcription — merging them reads as an attack | `manuscript_audit.md` §1, §4 |
| Discover a "scientific finding" was actually a software bug, and retract it in writing | CDSE (a temperature-dependent isotherm correction); BITS for GAPS (a mutated-kernel-state bug); crystallization (a measurement-tool bug) — three independent instances | Verify the instrument before believing the finding; retract in place when you're wrong, don't quietly edit it away | `manuscript_audit.md` §10 |
| Catch a silent failure a clean build/exit-code hid | SAF Brazil (an empty nomenclature table rendered in every reviewer's copy; five other silent defects, all exit-code 0); the optimization course website (a stale `.gitignore` rule silently dropped a required build artifact from every commit for 1.5 days — CI stayed green the whole time) | The countermeasure that works is reading the rendered output, never the log or the exit status | `manuscript_audit.md` §8 |
| Discover a checker was measuring the wrong thing entirely | Optimization course: an execution-only audit reported the site "healthy" while two published notebooks were functionally empty; separately, a `grep`-based leak checker missed a real leak because it checked cell *source* while the leak was in cell *output* | Verifying that something ran is not the same as verifying it did the right thing — the metric has to match the actual risk | `manuscript_audit.md` §6, `scientific_computing_workflow.md` §6 |
| Discover your own status report was wrong, and fix the *process*, not just the mistake | SAF Brazil (a status claim wrong for 11 of 17 items, reported from memory) | Determine status from evidence, never recollection — the fix is a script, not "being more careful" | `manuscript_audit.md` §7 |
| Cross-check a literature or verification claim independently, and let it correct you | The optimization course's adversarial verification pass, which found a real sign/dimension error in a decade-old lecture and, separately, that one of the *verifier's* three checks needed correcting | The second, independent pass is not optional — the checker needs checking too | `manuscript_audit.md` §10 |

## Epilogue — Trust

| Concrete task | Example | Principle |
|---|---|---|
| Return to the hook's unresolved question | grad-visit-scheduler's own "how do we train the next generation" line | Sit with the tension; don't resolve it artificially |
| Apply the same habits somewhere low-stakes and fun | boot-dryer-octopus; kitchen organizer/telescope; `radio-extra-book` | The same discipline — ground it, iterate in small steps, verify — pays off outside the lab too |

---

## Notes for building slides from this

- **The optimization course now grounds all three acts**, not research examples — worth featuring prominently. It needs zero anonymization, and it's instantly relatable to a grad-student audience who have all sat through a lecture course (several as a TA, which makes "would you trust this pipeline on your own course" land even closer to home).
- **The "retraction" principle now has three independent research instances plus one teaching instance** (a decade-old lecture error caught by an adversarial pass). Four is enough to say "this keeps happening independently" without naming any of them.
- **The "silent failure" and "wrong verification metric" principles are now each grounded in two independent projects** across two completely different domains (a manuscript audit; a course website) — the strongest repeated-pattern evidence in the whole inventory, and worth stating explicitly as "this is not a one-off."
- ~~The multi-agent spend-limit-kills-agents-mid-task incident~~ — resolved 2026-09-02: added to `working_with_ai_agents.md` §6 as a guardrail (expect hard external kills, not just self-imposed stop conditions; checkpoint often enough that a kill loses minutes, not hours; treat resuming as reconciliation, not a clean restart).
- ~~The `\fillin` redaction mechanism~~ — resolved: out of scope. It's lecture-material-specific and doesn't generalize; stays a slide-only example, not a practice-file addition.
- ~~The AI-review-status disclosure tracker~~ — resolved: genuinely useful, and generalizes beyond course material. Added to `working_with_ai_agents.md` §10 as a per-unit review-status pattern (`unreviewed`/`reviewed`/`reviewed-stale`/`exempt`, never silently reverting to `reviewed`), explicitly extended to proposals and manuscripts, not just course pages.
