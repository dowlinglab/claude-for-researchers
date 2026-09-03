# Storyboard

The talk's structure, locked 2026-09-02, following the Dowling Lab presentation-planning algorithm (group manual §Presentations): question → main points → outline → slide budget → slide titles → feedback → slides. This file is steps 3–6.

**Status:** structure locked; the entire deck is built and compiles clean, 43 slides end to end (`00_open.tex`, `00b_roadmap.tex`, `01_ecosystem.tex`, `02_act1_understand.tex`, `03_act2_build.tex`, `04_act3_challenge.tex`, `05_epilogue.tex`). A 2026-09-02 confidentiality re-check found no issues — every example matches its locked naming decision in `notes/demo_ideas.md`. That same pass, verifying real screenshots against primary sources, caught and fixed two fabricated-content bugs (a non-verbatim "verbatim" commit excerpt in Act I, a fabricated diff mislabeled as real in Act II) and surfaced one real addition: Jeff Kantor co-created the notebook behind `grad-visit-scheduler`, credited on the Prologue hook with a follow-up slide in Act II on the broader impact (Alex getting his whole group onto Codex as a direct result) — see the commit history for detail.

**2026-09-03 revision (beginning of the talk), per Alex's detailed feedback:** the title slide now reads "Prof. Alexander (Alex) Dowling" with his email under the department line. The old single-slide teaser is now two hook slides in `00_open.tex` — a synthetic (not real — see that file's own comment on why) "before Codex" schedule visual with the DGA/Jeff-Kantor history, then the full Codex-conversion story (real dates/versions, Carla's spreadsheet, the 1.5hr/8.5hr split, 100% test coverage) ending on the live-demo tease and the hanging question. "The claim" moved from right after the title to right after this hook, as the takeaway rather than the opener. The roadmap slide's act list is now single-line ("Prologue: Tinker", …) instead of a two-line-per-act table, closing the whitespace gap on the right. "Everything today is on GitHub" now lists actual filenames (was counts only) plus the repo link. A "Six kinds of task" preview of the six example types from `demo_ideas.md` was first its own slide, then **folded into "One year of practices, not a tool tutorial" the same day**, replacing that slide's `\actstrip{0}` diagram — Alex's call: the act-strip repeated the roadmap slide's outline and added nothing (now codified as `style_guide.md` rule 9), and the freed space was better spent foreshadowing the acts than on a redundant diagram. Two IT-policy slides (data classification, the two-checks list) moved from the Prologue to the Epilogue, on Alex's suggestion that they read as "Trust" material — "Don't become loyal to a model" stayed in the Prologue on his counter-argument that it cashes out the "not a product comparison" scoping slide right before it. Act I's opening "commit message" slide was cut (too in-the-weeds per Alex, more room for visual examples elsewhere); the next slide's dangling "same commit as the last slide" callback was fixed to stand alone. Because the hook now tells the grad-visit-scheduler story in full in the Prologue, Act II's old two-slide opener (the version-timeline "resolved" slide + the group-impact slide) collapsed into one slide — a one-line callback straight into the group-impact material, which the Prologue doesn't cover. Bold, sparse `\stagedivider` transition slides ("Act I: Understand", etc., using the act-strip macro that already existed but was never invoked) now open each act and the Epilogue.

Several slides still carry a `TODO` comment for a real screenshot not yet captured (grad-visit-scheduler's PyPI/tags/commit-graph, emcal/bits_for_gaps repo pages, a real `latexdiff` output, the capstone course's website) — needs a live session with Alex present, since the in-app browser used for autonomous passes can't save screenshots to disk (see `image_plan.md`). A typeset fallback ships in the meantime so no slide is empty. Next: the visual-asset capture pass (Alex's own next session), and rehearsal-driven trimming toward the ~35-40 slide target for a 60-minute slot.

---

## Why this structure, not the lifecycle taxonomy

The first pass organized the talk around the research lifecycle (Explore → Ground → Build → Record → Write → Verify). That's a sound teaching taxonomy but a weak *story* — it has completeness, not tension. Nothing in the middle makes you want the next slide.

Modeled instead on *This American Life*'s cold-open-then-three-acts structure: a short, low-stakes teaser states the theme as a question; three acts develop it with escalating stakes; an epilogue returns to the question without fully resolving it. The lifecycle stages still exist as *content* inside the acts — they just stopped being the organizing principle.

The organizing principle is **escalating trust**: how much you let an AI touch.

- **Act I — Understand:** it explains things to me.
- **Act II — Build:** it changes my artifacts.
- **Act III — Challenge:** it tells me I'm wrong.

## The anonymity constraint resolved itself

Every dramatic *failure* beat in the evidence base is Alex's own (a lost-context commit, a status report wrong on eleven items, a retracted finding that was a software bug, a `CLAUDE.md` warning about stale paths directly above stale paths). The *routine* material — refactoring, packaging, migration — is what came from inherited/former-student work, and it needs no drama, so it can stay generic ("a project I inherited") with no loss. The self-implicating half needs no anonymization; the anonymized half needs no anonymizing effort. Concretely: **grad-visit-scheduler carries the hook and Act II's depth because it is 100% Alex's own work** — the most memorable material in the talk needs no hedging at all.

---

## At a glance

Each act and the Epilogue now opens on a quick, bold `\stagedivider` transition slide (act-strip + act name + a one-line question) — counted in that beat's slide total below, not broken out separately.

| Beat | Name | Job | Slides | Rough time |
|---|---|---|---|---|
| — | Title | | 1 | 0.5 min |
| Prologue | **Tinker** | Hook in full (real dates, visuals), the claim, scope, orient, show the toolkit and the archetypes, prove the thesis is live | 8 | 7.5 min |
| Act I | **Understand** | A sell: git is the prerequisite, not the payoff | 8 (incl. divider) | 9.5 min |
| Act II | **Build** | It changes my artifacts (the hook's impact, resolved) | 10 (incl. divider) | 13 min |
| Act III | **Challenge** | It tells me I'm wrong, closing on a capstone | 8 (incl. divider) | 11 min |
| Epilogue | **Trust** | Return to the open question; the IT-policy "trust" beats; close on curiosity | 8 (incl. divider) | 6 min |
| | | **Total** | **43** | **~47.5 min**, trim ~7.5 in drafting/rehearsal |

See [`../notes/demo_ideas.md`](../notes/demo_ideas.md) for the confirmed six example types, which projects ground which slide, and the naming decision per type — this file only has slide titles; that one has the full mapping.

---

## Prologue — Tinker

**Job:** tell the grad-visit-scheduler story in full, with real visuals, as the hook — then state the seminar's central claim as the takeaway, scope what the talk is and isn't, orient the room, preview the six kinds of task the acts will draw on, and show what they walk away with today.

**Revised 2026-09-03** at Alex's request: the single-slide teaser undersold the hook, so it's now two slides with real detail and visuals, and "the claim" moved from opener to takeaway (was items 2/3 pre-2026-09-02; before that, items 2 and 5 were cut and restored on 2026-09-02 — see the open-questions entry below for that history). Two IT-policy slides (now in the Epilogue) moved out. The six-archetypes preview was briefly its own slide, then folded into item 6 the same day, replacing that slide's act-strip diagram. Net Prologue slide count: 9 → 8 (two new hook slides, offset by two moved-out policy slides and the archetypes slide folding into an existing one rather than adding a new one).

1. **Title slide** — *(revised 2026-09-03)* "Prof. Alexander (Alex) Dowling," with `adowling@nd.edu` under the department line.
2. **Before Codex: ten hours, a notebook, then patches** — *(new, 2026-09-03, `00_open.tex`)* a synthetic visit-day-schedule mockup (illustrative, not a real screenshot — real schedules carry visiting students' and faculty's actual names, which is exactly the kind of data the Epilogue's own classification slide says not to publish) plus the pre-AI history: ~10 hours by hand for the DGA, then a Python notebook Alex and **Jeff Kantor** built years later to formulate and solve the scheduling as an optimization problem, then ad-hoc features bolted on (e.g. auto-generating each visitor's Word-doc schedule).
3. **One weekend with Codex, and I kept going** — *(new, 2026-09-03, `00_open.tex`)* the full Codex-conversion story, real dates and version numbers (v0.1.2 → v0.3.1, Feb 11–17 — the version-timeline diagram moved here from Act II, which no longer repeats it): on sabbatical, nearly declining the ask, then ~1.5 hours to reformat **Carla**'s spreadsheet and regenerate the schedule with Codex, then ~8.5 more hours to a tested, documented, pip-installable package with 100% test coverage. Ends on the live 20-minute feature-add tease and the unresolved question: *"How do we train the next generation to get both?"* Do not answer it here.
4. **The claim** — *(built, `00_open.tex`; moved here 2026-09-03, was item 2)* the seminar's thesis, stated directly, now as the hook's takeaway rather than its opener: the most powerful uses of generative AI in research go beyond chatbot Q&A, and come from putting AI inside a workflow that is deliberate, reproducible, and auditable. Matches the abstract/`CLAUDE.md` wording.
5. **Borrowed structure** — *(revised 2026-09-03)* the *This American Life* citation + the Prologue/Act/Epilogue outline, now single-line entries ("Prologue: Tinker", …) instead of a two-line-per-act table — closes the whitespace gap on the right that the old layout left.
6. **One year of practices, not a tool tutorial** — *(revised 2026-09-03, `01_ecosystem.tex`)* scope the talk: not a Claude tutorial, not a product comparison, not a claim that AI does research; instead one year of practices and their failures, mostly model-independent, things to change on Monday. **The closing act-strip is cut** (it repeated the roadmap slide's outline with nothing new — `style_guide.md` rule 9) and replaced with a compact preview of the six example types from `notes/demo_ideas.md`'s confirmed roster (inherited material, manuscript audits, literature reviews, proposals, code → package, course retooling) — no new taxonomy, just a preview, now sharing this slide instead of getting its own.
7. **Don't become loyal to a model** — *(built)* pick tools by task, not brand. Kept in the Prologue (not moved to the Epilogue with item 9 below) on Alex's own argument: it directly cashes out item 6's "not a product comparison" claim.
8. **Everything today is on GitHub** — *(revised 2026-09-03)* actual filenames now, not counts — all nine practice files, all three prompts, all three scripts, all three templates, laid out as a repo tree — plus the repo link (`github.com/dowlinglab/claude-for-researchers`), per Alex's request to fill the slide's space better.
9. **This talk was built the same way** — *(built)* the deck itself is a live instance of the thesis — 10+ real projects identified, Claude Opus agents dispatched to examine their history, findings distilled into practice guides, a story arc crafted, slides built iteratively with Claude (including analyzing Alex's own past talks to match his real style). Placed here so it establishes authority and foreshadows the acts early, without revealing their specific content — the Epilogue's summary matrix gets a seventh row ("Creating this talk") to complete the loop instead of repeating the slide.

**Moved to the Epilogue, 2026-09-03** (see that section below): "At Notre Dame: know your data classification" and "Two things to check before you start" — Alex's call that they read as "Trust" material, not Prologue scoping.

*(All built. Items 6-8 have titles that state the frame's point directly, since the closing `\takeaway` bar they used to end on is retired deck-wide — see `style_guide.md` rule 5.)*

## Act I — Understand: conversation → living context, with git

**Job, sharpened 2026-09-02:** Act I is a **sell, not a payoff**. Its one argument is that version control is the prerequisite that unlocks what Codex/Claude Code can actually do — not a demonstrated outcome in itself. The mature, sophisticated result (a project that took this all the way) is deliberately *not* shown here; it's held for Act III's capstone, so Act I stays tight and single-minded instead of trying to also prove the payoff.

Organized around two parallel transitions, both "an ephemeral, unbacked-up thing becomes durable and versioned": a chat conversation → a repository of literature with validated claims; a local notebook with no backup → git. The graduating-student "inherited project" story lives here as the generic case behind the second parallel.

0. **Divider: "Act I: Understand"** — *(new, 2026-09-03)* bold, sparse `\stagedivider` transition slide: the act-strip with "Understand" lit, plus the one-line question "The prerequisite that unlocks everything else."
1. **State the shift** — a conversation vs. a repository; the filesystem is the source of truth.
2. **What git and GitHub actually give you** — a short, concrete explainer, anchored to a real commit (`dowlinglab/emcal` `31184f4`). Audience calibration: not everyone in the room is a software engineer.
3. **Three kinds of context** — persistent, authoritative, task, illustrated with the same membrane-transport project as slide 4 (its conventions; its actual data and model; the question this run is asking), not stated as abstract taxonomy. A chat history is a poor substitute for any of the three.
4. **One file, read at the start of every session** — that same project's actual `CLAUDE.md`, continuing slide 3's example. Name it neutrally, so `CLAUDE.md`/`AGENTS.md` become three-line pointers to it rather than the content itself.
5. **Parallel A, idea-first** — a chat conversation crossing two literatures on purpose to pressure-test an idea (a chromatography/digital-twin proposal, generic).
6. **Parallel A, corpus-first** — a folder of PDFs becomes an onboarding report, claims validated (a watershed project and a desalination project, generic). "Interpret, don't copy the abstract."
7. **Parallel B, closing the act** — a departed collaborator's local notebook, no backup, no version control → git. The inherited-project case, generic. Close on the forward pointer: *version control is the prerequisite — what it unlocks is the rest of this talk.*

*(Built in `02_act1_understand.tex`. **Cut 2026-09-03** at Alex's request: the old opening slide, "See conversation for the plan" — the real, verified `emcal` commit `31184f4`, word for word — judged too in-the-weeds for the time it cost, with more slides going to visual examples instead; its point still stands via the next slide. The old slide 3's "same commit as the last slide" callback was fixed to introduce the commit fresh, since there's no longer a preceding slide to call back to. Slides 3-4 (now) were restored 2026-09-02 from `02_context.tex`'s "three kinds of context" and project-file frames, Alex's call over cutting them as redundant with slide 2; slides 5-7 each have a constructed workflow diagram rather than bare text, per Alex's note that even an anonymized example should have something to look at. See `notes/demo_ideas.md` Act I table for exactly which project grounds each slide. The mature-example slide stays out of this act entirely, moved to Act III's capstone, so the act doesn't dilute its own sell with an early taste of the payoff.)*

## Act II — Build

**Job:** AI changes what you keep — code, and the documents that describe your work. The hook's impact resolves here in full (the story itself now lives in the Prologue), then widens twice: to research code that isn't just a personal tool, and to a proposal instead of a codebase.

0. **Divider: "Act II: Build"** — *(new, 2026-09-03)* `\stagedivider`: act-strip with "Build" lit, question "What's worth keeping?"
1. **As promised — and why it mattered** — *(revised 2026-09-03, was two slides)* now a one-line callback into new material only: the direct causal result Alex named — this success is why he got everyone in the group access to Codex. The version-timeline diagram and the full notebook/Jeff-Kantor/10-hour story that used to open this act moved to the Prologue hook (2026-09-03), which now tells it in full with real visuals — repeating it here would have been pure duplication.
2. **Prototype in notebooks; promote what matures.**
3. **Before you refactor: run it, pin it, baseline it.**
4. **Freeze the science, move the code — never both at once** — the controlled-comparison framing, queue-don't-fix for bugs found mid-refactor.
5. **A regression harness is what made a reversed conclusion believable** — the isotherm-correction story, generic.
6. **Not just a hobby-adjacent tool** — one line each on emcal / bits_for_gaps: the same discipline, in published research code.
7. **Review the diff, not the summary.**
8. **The same discipline, on a document instead of code** — draft tersely against the sponsor's own form, restore its exact wording before submission; AI as a compliance reviewer with findings written inline (`\foacomment{}`-style) rather than in a separate comments doc, flagged → fixed → removed.
9. **Verify every revision before you commit** — the `latexdiff`-against-last-commit habit, word-level, catching a softened claim or a changed number a normal re-read misses. Point to `resources/scripts/latexdiff_check.sh`.

## Act III — Challenge

**Job:** AI tells you that you're wrong, and you have to decide whether to believe it. Six slides on manuscript audits, then a two-part capstone (confirmed 2026-09-02) that closes the act as one integrated example instead of scattering it.

0. **Divider: "Act III: Challenge"** — *(new, 2026-09-03)* `\stagedivider`: act-strip with "Challenge" lit, question "Do you believe it?"
1. **Arithmetic, method, transcription: separate them** — merging them reads as an attack; separating them is what makes criticism land as methodology.
2. **Trace every number back to the file that produced it** — the claim-tracing table.
3. **"Cannot verify" is a result you want to get.**
4. **A clean build hid a silent failure** — three independent instances, three unrelated domains: a manuscript's empty nomenclature table (exit code 0), "Optimization for Decision Science"'s stale `.gitignore` rule that silently dropped a build artifact for 1.5 days while CI stayed green, and a project's own `CLAUDE.md` warning about stale absolute paths directly above four stale absolute paths (restored 2026-09-02 from `02_context.tex`'s "honest limit" frame, folded in here rather than kept as its own slide, since it's the same lesson as the other two). "A request to enumerate beats a request to confirm."
5. **My status report was wrong about eleven items; the fix was a script** — deriving status from evidence, not memory.
6. **Capstone, part 1 — the Act I argument, taken all the way** — "Optimization for Decision Science," named: the same `CLAUDE.md` pattern Act I explained generically, now a mature, specific instance — converted (handwritten notes → LaTeX, the coursepack) and challenged (an adversarial verification pass catches a real, decade-old sign error). One project, watched end to end.
7. **Capstone, part 2 — the verifier needed verifying too** — same course: one of the verification pass's own three checks needed correcting. The same self-correction principle as the manuscript audits, now from a second domain — closes the act.

## Epilogue — Trust

**Job:** return to the hook's question, land the responsible-use synthesis (now including the two IT-policy beats moved in from the Prologue), close on curiosity.

0. **Divider: "Epilogue: Trust"** — *(new, 2026-09-03)* `\stagedivider`: act-strip with "Trust" lit, question "What do you trust, and why?"
1. **Back to the question** — "how do we train the next generation" — not answered, sat with.
2. **At Notre Dame: know your data classification** — *(moved here 2026-09-03, was Prologue)* the 🟢🟡🟠🔴 table + Claude-is-Public-only finding. Alex's call: reads as "Trust" material, and lands better as the practical form of trust right after the question than as a pre-talk compliance interruption.
3. **Two things to check before you start** — *(moved here 2026-09-03, was Prologue)* DoD/DoW, and "ask your PI" generalized. Kept immediately after item 2 — same policy family.
4. **The summary matrix** — a simplified projects-×-acts grid built from `notes/demo_ideas.md`'s six-types table, plus a seventh row, "Creating this talk," checked under Prologue only — the payoff half of the meta-slide now living there instead of a second telling of the same slide.
5. **You own every claim, whatever helped you make it** — the compressed responsible-use list.
6. **The hobby stories, as the final example** — the boot-dryer octopus and the hobbies gallery (organizer, telescope shelf, radio book). No repeated argument. Ends on curiosity, not a caveat.
7. **One thing to change Monday morning** — pointer to the repo, close.

---

## Open questions

- ~~Where does the proposal-writing material live~~ — resolved: literature review in Act I, proposal writing in Act II (§8–9), as a document-shaped instance of "AI changes what you keep" alongside the code-shaped instance the hook already carries.
- ~~Act I's role~~ — resolved 2026-09-02: Act I is a sell (git is the prerequisite that unlocks Codex/Claude Code), not a payoff. The mature-example slide was cut entirely rather than kept as an early teaser, so the act doesn't dilute its own argument. 7 slides → 6.
- ~~The example roster and naming per type~~ — resolved 2026-09-02, recorded in `notes/demo_ideas.md`'s six-types table: types 3 and 6 named (`bits_for_gaps`/`emcal`/`grad-visit-scheduler`; "Optimization for Decision Science"), everything else generic, no exceptions — including `data3` (membrane-transport), deliberately not named alongside its two generic Type-1 siblings even though naming it in isolation would have been low-risk, because the asymmetry would draw more attention than the name would add.
- ~~Whether to restore the cut thesis and scoping slides~~ — resolved 2026-09-02: restored, Alex's call — he's willing to cut elsewhere rather than lose either concept. Prologue 7 → 9 slides, total 35 → 37.
- ~~Where does `02_context.tex`'s orphaned content go~~ — resolved and built 2026-09-02. Two of its five frames were already Act I in disguise (the `emcal` commit, "the filesystem is the source of truth") and needed no change beyond a title. The other three: the context taxonomy and a generic project-file example joined Act I as new slides 4-5, Alex's call over cutting them as redundant; the "honest limit" staleness story is earmarked for Act III slide 4 as a third silent-failure instance once that file is built, since it's the same lesson from the same domain (context files) as the other two. Act I 6 → 8 slides, total 37 → 39. `02_context.tex` itself has been removed — its content lives in `02_act1_understand.tex` (Act III's instance still pending that file).
- **Slide count vs. budget.** Alex confirmed 2026-09-02: a 60-minute slot, targeting 35-40 slides to leave real room for Q&A and discussion; confirmed again 2026-09-03 that he isn't worried about the count while there's still this much editing left to do, so this line is tracking information, not a constraint driving cuts right now. Current total is 43 — over the original 35-40 range, after the 2026-09-03 revision added four `\stagedivider` transition slides (quick and sparse, not full content beats) and a fuller Prologue hook, partly offset by cutting Act I's opening slide, merging Act II's old two-slide opener into one, and folding the archetypes preview into an existing slide instead of giving it its own. The at-a-glance table's rough-time estimates (~47.5 min) still run over a 40-minute talk portion. A rehearsal pass with real timing, not a slide-count target, should drive any further trim — the dividers in particular should read as very fast in person even though they count as slides.
- ~~The DGA/Carla details in the Prologue hook~~ — resolved 2026-09-03, confirmed directly with Alex: "DGA" is Director of Graduate Admissions (kept generic, not attributed to a specific person); Carla is named by first name plus role ("Carla, the graduate program coordinator" in prose — the slide itself just says "Carla's spreadsheet," role established by the surrounding sentence). The year the Jeff-Kantor notebook was built is deliberately not stated (Alex's own notes had it as a placeholder, "In XYZ") — said as "years later" instead; add the real year if he wants it on the slide.
- **Feedback pass.** Per the group manual: get outline feedback at least 8 days before the talk. Not yet done.
