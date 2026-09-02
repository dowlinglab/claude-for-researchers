# Demo ideas — candidate stories and examples

Working notes on the personal examples this seminar draws from, kept separate from polished content. See [seminar_design.md](seminar_design.md) for how each maps into [outline.md](../outline.md), and [open_questions.md](open_questions.md) for what's still undecided about each.

## 1. Turning graduate-student research code into a real Python package

**Supports:** Outline Section 4 (Build).
**Shape:** Organically-grown research code → reorganized files, deduplicated logic, notebook logic separated into reusable modules, `pip install`-able package, docs, tests, reproducible install/run, better Git hygiene.
**Core line:** "The student's code works" → "the research software is an auditable artifact someone else can install, understand, test, and extend."
**Status:** Resolved (2026-09-02) — two real, public examples, verified directly against their repos:
  - **[emcal](https://github.com/dowlinglab/emcal)** — Gaussian-process Bayesian optimization for calibrating nonlinear computational models. BSD-3, unit tests, GitHub Actions CI. Accompanies a peer-reviewed paper ("Bayesian Optimization Methods for Nonlinear Model Calibration," *Ind. Eng. Chem. Res.*, 2025). Notably, the reproducible-research workflow for the paper stays in a separate *archived research repository* — a real instance of the split-repo pattern from Outline Section 4/[seminar_design.md](seminar_design.md).
  - **[bits_for_gaps](https://github.com/dowlinglab/bits_for_gaps)** — information-theoretic sequential experimental design with Bayesian hierarchical GP surrogates. BSD-3, `pip install bits_for_gaps`, unit/integration/regression tests with coverage, Sphinx docs on ReadTheDocs. Published in *Computers & Chemical Engineering* (2026). Its README states, almost verbatim what this talk argues: *"The research code behind the paper was originally developed in a private repository... then migrated here and reorganized into an installable, tested package."* Strong candidate for a direct quote on the slide.
  - Both repos are public, so cite them by name and link freely — but don't name or otherwise identify the student who wrote the original code in the spoken narrative, even though it's discoverable from commit history.

## 2. Moving beyond Jupyter notebooks — and end-to-end with Codex

**Supports:** Outline Section 4 (Build) — now the primary demo for the whole section, not just a conceptual setup.
**Shape:** An internal, Jupyter-centric scheduling tool (built with a colleague, refined over years) → converted end-to-end into a tested, documented, CI/CD-backed PyPI package, then generalized, using ChatGPT/Codex.
**Real example:** **[grad-visit-scheduler](https://github.com/dowlinglab/grad-visit-scheduler)** — optimizes meeting schedules between prospective grad students and faculty at a departmental open house, formulated as a MILP in Pyomo. "Created by Alex Dowling and Jeff Kantor... the meeting scheduler used by Notre Dame Chemical and Biomolecular Engineering, released as a general-purpose, open-source tool." BSD-3; pip-installable as **`grad-visitor-scheduler`** on PyPI (note the repo/package name mismatch — worth double-checking on the slide rather than trusting memory); GitHub Actions test suite + Codecov + tag-driven automated PyPI releases; docs on ReadTheDocs; multi-building support (`travel_time`, `nonoverlap_time`) and top-N ranked schedules (`schedule_visitors_top_n()`).
**Narrative arc, from Alex's own LinkedIn posts (his to quote/paraphrase freely):**
  1. Originally 10 hours of manual scheduling → a Jupyter tool built with Jeff Kantor, refined over years.
  2. On sabbatical, used Codex to go from internal tool to a first PyPI release in about 2 days total (vs. an estimated 2+ weeks solo) — isolating ND-specific data, adding examples/tests/docs, identifying edge cases, improving error handling, and writing out the MILP formulation from the code itself.
  3. Live demo with his grad student and postdoc: added a top-N no-good-cut feature in ~20 minutes, including real back-and-forth on software design, not just code generation.
  4. From v0.1.2 (Feb 11, 2026) to v0.3.1 (Feb 17, 2026): generalized from a 2-building, ND-specific tool to arbitrary buildings with configurable travel times, plus automated release workflows and stronger CI/coverage.
  5. Self-assessed productivity: "easily a 5x productivity multiplier" — **with an explicit caveat, in his own words**, worth using directly: *"I've touched every stage of the software pipeline before. This is the first project where I did it end-to-end solo, and my prior context made the tool dramatically more effective."*
**Core line:** "Prototype in notebooks; promote mature logic into an auditable codebase" — and this is what it looks like end-to-end, with dates, versions, and a public, checkable result, not an anonymized composite.
**Model-independence bonus:** This flagship example used ChatGPT/Codex, not Claude — a natural, honest callback to Section 1's "don't become loyal to one model."
**Status:** Ready — richest, most concrete, fully public material in the whole talk. See also the "training-model tension" entry below for the self-critical reflection this story sets up for Section 8.

## 3. Maintaining a running research/results log

**Supports:** Outline Section 5 (Record) directly — and this project's own [seminar_notes.md](seminar_notes.md) is now a live instance of the pattern, worth mentioning as a meta-example.
**Shape:** Persistent Markdown log — date, question, experiment, commit, config, datasets, outputs, interpretation, failed approaches, next questions.
**Core line:** Lets AI answer "what did we learn from experiments 14–27?" without relying on memory or a huge chat history.
**Status:** Ready. Need one realistic sample entry for the slide (can be synthetic/representative rather than from a real project).

## 4. Creating a custom Amateur Radio exam study guide

**Supports:** Not core research lifecycle — moved (2026-09-02) to the new closing Section 9, "Unleash Your Curiosity: AI and your hobbies," rather than a Section 3 aside.
**Shape:** Curated source material (exam question pool, regulations) → structured, purpose-built study resource via iterative generation, verified against authoritative sources.
**Core line:** "AI can transform a curated body of source material into a new structured artifact tailored to a specific purpose" — the same pattern as Section 3 (grounding) and Section 6 (structured writing), applied outside of research.
**Status:** Resolved — one-line story with a link, in Section 9. Repo is public: [github.com/adowling2/radio-extra-book](https://github.com/adowling2/radio-extra-book). Paired with the 3D-printing story below.

## 4b. 3D printing with ChatGPT + OpenSCAD (new, 2026-09-02; expanded same day with an earlier post)

**Supports:** Outline Section 9, paired with the Amateur Radio story — and its "iterate, don't regenerate" and "speed vs. understanding" lessons double back to reinforce Sections 4 and 8. Alex supplied two LinkedIn posts, chronologically in this order:

**Post A (earlier, first-ever attempt) — the "boot dryer octopus."** Aldi had a glove dryer on sale; Alex wondered whether he could build one at home for wet snow gear. Late at night, he brainstormed with ChatGPT, which surfaced DIY PVC+hairdryer designs, then *flagged the hairdryer as a fire hazard* and recommended a $10 inline 4" ventilation fan instead — a nice, concrete example of AI catching a real safety issue, not just generating code. The hard part: adapting a 4" fan to 2" PVC (boots) and 1.25" PVC (gloves) — no off-the-shelf part fit. With ~30 minutes of CAD experience ever and no prior 3D-printing experience, he asked ChatGPT, which introduced OpenSCAD (install: under 5 minutes) and generated the script. The loop that worked: render in OpenSCAD (seconds to a minute) → screenshot → hand ChatGPT the screenshot plus a bulleted list of refinements → repeat. He then used Notre Dame's own **Hesburgh Libraries 3D printing service** and the **College of Engineering Innovation Hub** to get the part checked and printed — a same-day email exchange with library staff (credited: Adam Heet). Ends with a genuine, forward-looking question for CBE specifically: where could 3D printing become an experiential-learning vehicle in the department's courses (e.g., a turbulent-mixing baffle; a vehicle for teaching thermodynamics, polymers, transport, reactions, controls)?
**Post B (later, ~7 months before this seminar) — kitchen organizer and telescope shelf.** Two more projects, over two months: a kitchen drawer organizer (~15-minute dimensioned sketch, photographed, ~45 minutes to a submitted print — the easy case) and a Dobsonian telescope shelf with a custom compass holder (30+ iterations, ChatGPT struggling with geometric reasoning on underside supports and cutouts — the hard case). Alex flagged this post's own prose as "a little too AI sounding" (emoji-numbered listicle) — this write-up deliberately doesn't reuse that structure, extracting the substance in plain prose instead, consistent with Section 6's own teaching.
**Images:** two collages are already in hand (OpenSCAD editor + render + printed green "octopus" fitting + the fan, for Post A; sketch + printed organizer + telescope shelf, for Post B) — both need adding to `slides/figures/` when slides are built; not extractable from the conversation automatically.
**Core lines (in Alex's own words, lightly compressed):**
  - *Workflow, demonstrated vividly in Post A and stated explicitly in Post B:* generate code → render → screenshot → give targeted feedback beat regenerating the whole script from scratch, which tended to introduce new errors; small patches worked better than full rewrites, and re-sharing the full script in each prompt cut down on hallucination. This is the *exact same lesson* as Section 4's "review the diff, prefer small changes over large AI refactors" — independently rediscovered in a completely different domain.
  - *The tradeoff, stated plainly (Post B):* "there's always a tradeoff between speed and understanding." Alex lost count of how many versions ChatGPT named `final`, `final_final`, `final_final_final` — and reflected that this gave him new empathy for how students might use these tools to finish faster at the expense of deeper learning.
  - *Without irony (Post A):* ChatGPT "empowered me to tinker for an afternoon" on something he'd never have attempted otherwise.
**Design note for Section 9 (1 minute is tight for three hobby examples — radio book + two 3D-printing posts):** recommended shape is one anchor story (Post A — best narrative arc, funniest, and it names real ND resources), one brief "and I kept going" line covering Post B and the radio book with links on the slide rather than spoken detail, and closing on Post A's own CBE-course question rather than a generic "try this yourself" line — it's a genuine open question Alex is already wrestling with, and it doubles as a natural bridge into the 20-minute Q&A, especially for faculty in the room. Flagged as ambitious for 60 seconds; worth timing out loud during rehearsal and trimming further (e.g., dropping Post B to a link-only mention with zero narration) if it runs long.
**Status:** Ready, pending Alex's sign-off on the anchor-story choice above. Deliberately chosen to *echo* the Section 8 training-model tension from a totally different, low-stakes domain rather than introduce a new idea. Also another real, non-Claude example (ChatGPT + OpenSCAD) reinforcing Section 1.

## 5. Finishing papers after students graduate

**Supports:** Confirmed frame story for Outline Section 0 (open) and Section 8 (close) — bookending the talk.
**Shape:** Inheriting a project after the person who wrote the analysis has moved on — using AI to understand unfamiliar code, reconstruct how analyses work, trace outputs back to scripts, understand undocumented design decisions, refactor enough to finish the manuscript, and check the paper against the actual implementation.
**Core line:** Preserving context in files/repos/logs/docs matters far more than preserving it inside an AI chat — because the person who *had* that context is gone, and so is any chat history they had with an AI about it.
**Status:** Resolved (2026-09-02). Confirmed as the bookend, reframed around *expediting* completion rather than only "recovery after abandonment" — e.g., "helping a graduating student (or their advisor) get a project across the finish line," which reads as proactive and applies more broadly to the audience than pure salvage work. Uses a real, anonymized project; no student named or identifiable. Open at Section 0 with the premise, resolve it at Section 8 once every practice (context files, the log, reproducible code, the audit) has been introduced.

## The training-model tension (new, 2026-09-02)

**Supports:** Outline Section 8 (Responsible use & closing), as an honest, unresolved question rather than a wrap-up bullet.
**Shape:** Straight from the grad-visit-scheduler LinkedIn posts (Story #2): Alex got a 5x productivity multiplier with Codex, but attributes much of that to already having "touched every stage of the software pipeline before." His own question, asked twice across the three posts: *"how do we train future scientists and engineers to use GenAI tools for major productivity gains while still developing deep technical expertise?"*
**Core line:** This is the single best piece of material in the whole charter for the "not a celebration of AI for its own sake" guardrail (see [seminar_design.md](seminar_design.md)) — it's Alex's own genuine reflection, not a manufactured caveat, and it directly reinforces the closing teaching point that scientific/technical judgment stays with the researcher.
**Status:** Ready. Candidate use: close Section 8 with this question rather than an answer — consistent with "the goal is not to have AI do your research," and a good bridge into the 20-minute Q&A. Echoed a second time, in miniature, by the 3D-printing story (#4b) in Section 9 — don't over-explain the callback when it happens; let the audience make the connection.

## ND data-classification chart (new, 2026-09-02)

**Supports:** Outline Section 1 (Ecosystem), possibly echoed in Section 8 (Responsible use).
**Shape:** Notre Dame's own 🟢 Public / 🟡 Internal / 🟠 Sensitive / 🔴 Restricted data tiers, confirmed directly from `ai.nd.edu`, paired with which tools are currently cleared at which tier — Gemini/ChatGPT EDU/NotebookLM through Sensitive, Claude currently Public-only. See [references.md](references.md) for full quotes.
**Core line:** Institution-specific, concrete, and slightly uncomfortable for a Claude-titled talk to say out loud — which is exactly why it's worth saying: the talk should model the honesty it's asking students to bring to their own work.
**Status:** Ready to build as a slide once verified once more close to the talk date (see [open_questions.md](open_questions.md)).

## Other demo material referenced in the outline (not full "stories," just artifacts to build)

- **Section 2:** a short `CLAUDE.md`-style file vs. a chat that has lost track of project conventions. This repository's own [CLAUDE.md](../CLAUDE.md) can serve as the real example.
- **Section 3:** one evidence-seeking literature prompt with realistic output, citations traceable to specific (real or representative) papers.
- **Section 6:** one guideline file (`FIGURE_GUIDELINES.md` or similar) plus one flagged violation.
- **Section 7:** the claim-tracing table (see outline.md) — needs one "verified" row and one "cannot verify" row to make the point that both outcomes are useful.
