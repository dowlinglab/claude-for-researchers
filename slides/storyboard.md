# Storyboard

The talk's structure, locked 2026-09-02, following the Dowling Lab presentation-planning algorithm (group manual §Presentations): question → main points → outline → slide budget → slide titles → feedback → slides. This file is steps 3–6.

**Status:** structure locked; slide titles drafted below; `slides/sections/02_context.tex` predates this and still uses the old ten-section framing (Explore/Ground/Build/Record/Write/Verify) — its five frames don't map onto Act I's locked slide list below, so it needs real content work, not a mechanical pass (see `style_guide.md` "Still stale"). Its `Muted`-color and `\takeaway`-bar usage were already brought into line with the current rules on 2026-09-02, independent of that larger question. `00b_roadmap.tex`, `00_open.tex`, and `01_ecosystem.tex` (rewritten 2026-09-02, against this file and `style_guide.md`) are built against this structure. See [`image_plan.md`](image_plan.md) for how every slide's visuals get sourced, before drafting goes further.

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

| Beat | Name | Job | Slides | Rough time |
|---|---|---|---|---|
| — | Title | | 1 | 0.5 min |
| Prologue | **Tinker** | Claim, hook (teased), scope, orient, show the toolkit | 9 | 7.5 min |
| Act I | **Understand** | A sell: git is the prerequisite, not the payoff | 6 | 8 min |
| Act II | **Build** | It changes my artifacts (hook resolved in full) | 9 | 13 min |
| Act III | **Challenge** | It tells me I'm wrong, closing on a capstone | 7 | 10 min |
| Epilogue | **Trust** | Return to the open question; close on curiosity | 5 | 4 min |
| | | **Total** | **37** | **~43 min**, trim ~3 in drafting |

See [`../notes/demo_ideas.md`](../notes/demo_ideas.md) for the confirmed six example types, which projects ground which slide, and the naming decision per type — this file only has slide titles; that one has the full mapping.

---

## Prologue — Tinker

**Job:** state the seminar's central claim, open with the grad-visit-scheduler headline as a teaser (not the full story — that's Act II), leave its closing question hanging, scope what the talk is and isn't, orient the room, and show what they walk away with today.

Items 2 and 5 (the claim, the scoping slide) were in the original pre-restructure open and were dropped when the talk moved to the three-act structure, on the reasoning that storyboard.md's own Prologue list didn't carry them forward. Restored 2026-09-02 at Alex's request — he liked both concepts and would rather cut elsewhere than lose them. Slide count: Prologue 7 → 9, total 35 → 37.

1. **Title slide**
2. **The claim** — *(built, `00_open.tex`)* the seminar's thesis, stated directly: the most powerful uses of generative AI in research go beyond chatbot Q&A, and come from putting AI inside a workflow that is deliberate, reproducible, and auditable. Matches the abstract/`CLAUDE.md` wording — this is the one slide that says it as a claim, not just implies it.
3. **The teaser** — *(built, `00_open.tex`)* "One weekend, an annual scheduling headache, and a package on PyPI." Dates, Codex (not Claude), the 5× line — and the unresolved question left hanging: *"I'd touched every stage of this before. How do we train the next generation to get both?"* Do not answer it here.
4. **Borrowed structure** — *(built)* the *This American Life* citation + the Prologue/Act/Epilogue outline.
5. **Today** — *(built, `01_ecosystem.tex`)* scope the talk: not a Claude tutorial, not a product comparison, not a claim that AI does research; instead one year of practices and their failures, mostly model-independent, things to change on Monday. Closes with the act-strip (still at 0 — nothing lit yet). The GitHub pointer originally closing this slide moved to item 9, its natural home.
6. **The landscape, briefly** — *(built)* pick tools by task, not brand; don't become loyal to a model.
7. **At Notre Dame: know your data classification** — *(built)* the 🟢🟡🟠🔴 table + Claude-is-Public-only finding.
8. **Two things to check before you start** — *(built)* DoD/DoW, and "ask your PI" generalized.
9. **What you get today** — a quick look at the resources: nine practice files, three prompts, three working scripts, three templates. This is the "show the resources" beat — a screenshot or a live `ls resources/` moment, not a detailed walkthrough. Now also carries the "everything is on GitHub" pointer moved from item 5.

*(2–8 are built; 9 is new. Items 5-8 also each got new titles that state the frame's point directly, since the closing `\takeaway` bar they used to end on is retired deck-wide — see `style_guide.md` rule 5.)*

## Act I — Understand: conversation → living context, with git

**Job, sharpened 2026-09-02:** Act I is a **sell, not a payoff**. Its one argument is that version control is the prerequisite that unlocks what Codex/Claude Code can actually do — not a demonstrated outcome in itself. The mature, sophisticated result (a project that took this all the way) is deliberately *not* shown here; it's held for Act III's capstone, so Act I stays tight and single-minded instead of trying to also prove the payoff.

Organized around two parallel transitions, both "an ephemeral, unbacked-up thing becomes durable and versioned": a chat conversation → a repository of literature with validated claims; a local notebook with no backup → git. The graduating-student "inherited project" story lives here as the generic case behind the second parallel.

1. **Open on the failure** — "See conversation for the plan," the real, verified commit (`dowlinglab/emcal` `31184f4`, word for word).
2. **State the shift** — a conversation vs. a repository; the filesystem is the source of truth.
3. **What git and GitHub actually give you** — a short, concrete explainer, anchored to the same `emcal` commit, motivated by slide 1's failure rather than delivered cold. Audience calibration: not everyone in the room is a software engineer.
4. **Parallel A, idea-first** — a chat conversation crossing two literatures on purpose to pressure-test an idea (a chromatography/digital-twin proposal, generic).
5. **Parallel A, corpus-first** — a folder of PDFs becomes an onboarding report, claims validated (a watershed project and a desalination project, generic). "Interpret, don't copy the abstract."
6. **Parallel B, closing the act** — a departed collaborator's local notebook, no backup, no version control → git. The inherited-project case, generic. Close on the forward pointer: *version control is the prerequisite — what it unlocks is the rest of this talk.*

*(Maps to the old `02_context.tex` plus new material from `literature_review.md`; see `notes/demo_ideas.md` Act I table for exactly which project grounds each slide. Down from 7 slides to 6 — the mature-example slide moved out entirely rather than staying as a planted teaser, so the act doesn't dilute its own sell with an early taste of the payoff.)*

## Act II — Build

**Job:** AI changes what you keep — code, and the documents that describe your work. The hook resolves here in full, then widens twice: to research code that isn't just a personal tool, and to a proposal instead of a codebase.

1. **The hook, in full** — the internal tool → Codex-assisted → tested, documented, CI-backed PyPI package. Real dates, real version numbers (v0.1.2 → v0.3.1, Feb 11–17), the 20-minute live feature-add demo.
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

1. **Arithmetic, method, transcription: separate them** — merging them reads as an attack; separating them is what makes criticism land as methodology.
2. **Trace every number back to the file that produced it** — the claim-tracing table.
3. **"Cannot verify" is a result you want to get.**
4. **A clean build hid a silent failure** — two independent instances, two unrelated domains: a manuscript's empty nomenclature table (exit code 0) and "Optimization for Decision Science"'s stale `.gitignore` rule that silently dropped a build artifact for 1.5 days while CI stayed green. "A request to enumerate beats a request to confirm."
5. **My status report was wrong about eleven items; the fix was a script** — deriving status from evidence, not memory.
6. **Capstone, part 1 — the Act I plant pays off** — "Optimization for Decision Science," named: the `CLAUDE.md` from Act I, now converted (handwritten notes → LaTeX, the coursepack) and challenged (an adversarial verification pass catches a real, decade-old sign error). One project, watched end to end.
7. **Capstone, part 2 — the verifier needed verifying too** — same course: one of the verification pass's own three checks needed correcting. The same self-correction principle as the manuscript audits, now from a second domain — closes the act.

## Epilogue — Trust

**Job:** return to the hook's question, land the responsible-use synthesis, close on curiosity.

1. **Back to the question** — "how do we train the next generation" — not answered, sat with.
2. **The summary matrix** — a simplified projects-×-acts grid built from `notes/demo_ideas.md`'s six-types table: a handful of real projects recur across every act, shown rather than asserted.
3. **You own every claim, whatever helped you make it** — the compressed responsible-use list.
4. **The hobby stories, as the final example** — the boot-dryer octopus and the hobbies gallery (organizer, telescope shelf, radio book). No repeated argument. Ends on curiosity, not a caveat.
5. **One thing to change Monday morning** — pointer to the repo, close.

---

## Open questions

- ~~Where does the proposal-writing material live~~ — resolved: literature review in Act I, proposal writing in Act II (§8–9), as a document-shaped instance of "AI changes what you keep" alongside the code-shaped instance the hook already carries.
- ~~Act I's role~~ — resolved 2026-09-02: Act I is a sell (git is the prerequisite that unlocks Codex/Claude Code), not a payoff. The mature-example slide was cut entirely rather than kept as an early teaser, so the act doesn't dilute its own argument. 7 slides → 6.
- ~~The example roster and naming per type~~ — resolved 2026-09-02, recorded in `notes/demo_ideas.md`'s six-types table: types 3 and 6 named (`bits_for_gaps`/`emcal`/`grad-visit-scheduler`; "Optimization for Decision Science"), everything else generic, no exceptions — including `data3` (membrane-transport), deliberately not named alongside its two generic Type-1 siblings even though naming it in isolation would have been low-risk, because the asymmetry would draw more attention than the name would add.
- ~~Whether to restore the cut thesis and scoping slides~~ — resolved 2026-09-02: restored, Alex's call — he's willing to cut elsewhere rather than lose either concept. Prologue 7 → 9 slides, total 35 → 37.
- **Slide count vs. budget.** Current total: 37 (35, then 37 after restoring the thesis and scoping slides). At-a-glance table assumes roughly one slide per minute in the acts, less in the Prologue/Epilogue — now running about 3 min over that budget, expected to trim in drafting. Still needs a real count once `02_context.tex` is rewritten against this structure — the group-manual algorithm's step 4 ("check you have ~1 slide per minute") hasn't been re-run since the restructure.
- **Feedback pass.** Per the group manual: get outline feedback at least 8 days before the talk. Not yet done.
