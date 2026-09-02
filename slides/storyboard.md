# Storyboard

The talk's structure, locked 2026-09-02, following the Dowling Lab presentation-planning algorithm (group manual §Presentations): question → main points → outline → slide budget → slide titles → feedback → slides. This file is steps 3–6.

**Status:** structure locked; slide titles drafted below; `slides/sections/00_open.tex`, `01_ecosystem.tex`, `02_context.tex` predate this and still use the old ten-section framing (Explore/Ground/Build/Record/Write/Verify). They need rewriting to match the acts below — tracked as the immediate next step, not yet done. `00b_roadmap.tex` is the first slide built against this structure.

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

| Beat | Name | Job | Rough time |
|---|---|---|---|
| — | Title | | 0.5 min |
| Prologue | **Tinker** | Hook (teased), orient, show the toolkit | 6 min |
| Act I | **Understand** | It explains things to me | 9 min |
| Act II | **Build** | It changes my artifacts (hook resolved in full) | 13 min |
| Act III | **Challenge** | It tells me I'm wrong | 9 min |
| Epilogue | **Trust** | Return to the open question; close on curiosity | 4 min |
| | | **Total** | **~41.5 min**, trim ~1.5 in drafting |

---

## Prologue — Tinker

**Job:** open with the grad-visit-scheduler headline as a teaser (not the full story — that's Act II), leave its closing question hanging, orient the room, and show what they walk away with today.

1. **Title slide**
2. **The teaser** — "One weekend, an annual scheduling headache, and a package on PyPI." Dates, Codex (not Claude), the 5× line — and the unresolved question left hanging: *"I'd touched every stage of this before. How do we train the next generation to get both?"* Do not answer it here.
3. **Borrowed structure** — *(built)* the *This American Life* citation + the Prologue/Act/Epilogue outline.
4. **The landscape, briefly** — pick tools by task, not brand; don't become loyal to a model.
5. **At Notre Dame: know your data classification** — the 🟢🟡🟠🔴 table + Claude-is-Public-only finding.
6. **Two things to check before you start** — DoD/DoW, and "ask your PI" generalized.
7. **What you get today** — a quick look at the resources: nine practice files, three prompts, three working scripts, three templates. This is the "show the resources" beat — a screenshot or a live `ls resources/` moment, not a detailed walkthrough.

*(2, 4–6 are largely built already in `01_ecosystem.tex` under the old numbering; 3 is built; 2 and 7 are new.)*

## Act I — Understand

**Job:** AI as something that explains an existing situation back to you, before you trust it to change anything. Where the graduating-student "inherited project" story now lives — supporting material, not the frame.

**Threads:** project memory (the enabling condition — nothing later works without it); understanding inherited code; literature review, both idea-first (crossing two fields to pressure-test an idea) and corpus-first (turning a collected folder into an onboarding report).

1. **The shift that matters most** — a conversation vs. a repository; the filesystem is the source of truth.
2. **"See conversation for the plan"** — the real commit message; the conversation no longer exists.
3. **A context file orients; only a check enforces** — the honest limit (both of my own context files are stale).
4. **A student is graduating, the code runs on their laptop** — the inherited-project case, generic.
5. **Never cite a paper because an AI said it exists** — the verification chain.
6. **Cross two literatures on purpose** — idea-first pressure-testing an idea against an adjacent field.
7. **The corpus becomes someone else's starting point** — corpus-first: a getting-started report, the fixed annotation schema, "interpret, don't copy the abstract."
8. **Correct in place; never delete** — the struck-through, dated correction as a habit that shows up again in Act III.

*(Roughly maps to the old `02_context.tex` plus new material from `literature_review.md`.)*

## Act II — Build

**Job:** AI changes what you keep. The hook resolves here in full, then widens to show the same discipline in research code, not just a personal tool.

1. **The hook, in full** — the internal tool → Codex-assisted → tested, documented, CI-backed PyPI package. Real dates, real version numbers (v0.1.2 → v0.3.1, Feb 11–17), the 20-minute live feature-add demo.
2. **Prototype in notebooks; promote what matures.**
3. **Before you refactor: run it, pin it, baseline it.**
4. **Freeze the science, move the code — never both at once** — the controlled-comparison framing, queue-don't-fix for bugs found mid-refactor.
5. **A regression harness is what made a reversed conclusion believable** — the isotherm-correction story, generic.
6. **Not just a hobby-adjacent tool** — one line each on emcal / bits_for_gaps: the same discipline, in published research code.
7. **Review the diff, not the summary.**
8. **The same discipline, applied to a proposal** — draft against the sponsor's form, restore its wording, `latexdiff` before every commit. *(Bridges into Act III's audit theme; could move there instead — see open question below.)*

## Act III — Challenge

**Job:** AI tells you that you're wrong, and you have to decide whether to believe it. The climax.

1. **Arithmetic, method, transcription: separate them** — merging them reads as an attack; separating them is what makes criticism land as methodology.
2. **Trace every number back to the file that produced it** — the claim-tracing table.
3. **"Cannot verify" is a result you want to get.**
4. **A clean build printed an empty table for every reviewer** — the silent-failure-mode slide; "a request to enumerate beats a request to confirm."
5. **My status report was wrong about eleven items; the fix was a script** — deriving status from evidence, not memory.
6. **Retract in place** — the callback to Act I's correction habit, now in a manuscript instead of a literature review.
7. **The compliance review, inline** — `\foacomment{}`-style AI-as-reviewer on a proposal, structurally identical to the manuscript audit, applied before submission instead of after a result exists. *(If §8 of Act II moves here instead, this is where it lands.)*

## Epilogue — Trust

**Job:** return to the hook's question, land the responsible-use synthesis, close on curiosity.

1. **Back to the question** — "how do we train the next generation" — not answered, sat with.
2. **You own every claim, whatever helped you make it** — the compressed responsible-use list.
3. **The boot-dryer octopus** — the hook/tinkering story, closing on its own open question about CBE coursework.
4. **The hobbies gallery** — organizer, telescope shelf, radio book. No repeated argument. Ends on curiosity, not a caveat.
5. **One thing to change Monday morning** — pointer to the repo, close.

---

## Open questions

- **Where does the proposal-writing material live** — Act II (as a "build" of a document) or Act III (as an audit applied pre-submission)? Leaning Act III; not settled. See `resources/practices/grant_proposal_writing.md`.
- **Slide count vs. budget.** At-a-glance table above assumes roughly one slide per minute in the acts, less in the Prologue/Epilogue. Needs a real count once `00_open.tex`/`01_ecosystem.tex`/`02_context.tex` are rewritten against this structure — the group-manual algorithm's step 4 ("check you have ~1 slide per minute") hasn't been re-run since the restructure.
- **Feedback pass.** Per the group manual: get outline feedback at least 8 days before the talk. Not yet done.
