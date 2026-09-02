# Demo ideas — candidate stories and examples

Working notes on the personal examples this seminar draws from, kept separate from polished content. See [seminar_design.md](seminar_design.md) for how each maps into [outline.md](../outline.md), and [open_questions.md](open_questions.md) for what's still undecided about each.

## 1. Turning graduate-student research code into a real Python package

**Supports:** Outline Section 4 (Build).
**Shape:** Organically-grown research code → reorganized files, deduplicated logic, notebook logic separated into reusable modules, `pip install`-able package, docs, tests, reproducible install/run, better Git hygiene.
**Core line:** "The student's code works" → "the research software is an auditable artifact someone else can install, understand, test, and extend."
**Status:** Resolved (2026-09-02) — will use a real, anonymized Dowling-lab project (Alex has two candidates). No student named or otherwise identifiable; keep file trees/descriptions generic enough to avoid implication.

## 2. Moving beyond Jupyter notebooks

**Supports:** Outline Section 4 (Build), as the conceptual setup before the package story.
**Shape:** Exploratory notebooks (hidden state, duplicated cells, manual execution order, hard-coded paths) → functions, modules, scripts, config files, tests, explicit inputs/outputs.
**Core line:** "Prototype in notebooks; promote mature logic into an auditable codebase." Not "notebooks are bad."
**Status:** Likely folded into Story #1's before/after rather than shown separately — avoids two file-tree slides back to back.

## 3. Maintaining a running research/results log

**Supports:** Outline Section 5 (Record) directly — and this project's own [seminar_notes.md](seminar_notes.md) is now a live instance of the pattern, worth mentioning as a meta-example.
**Shape:** Persistent Markdown log — date, question, experiment, commit, config, datasets, outputs, interpretation, failed approaches, next questions.
**Core line:** Lets AI answer "what did we learn from experiments 14–27?" without relying on memory or a huge chat history.
**Status:** Ready. Need one realistic sample entry for the slide (can be synthetic/representative rather than from a real project).

## 4. Creating a custom Amateur Radio exam study guide

**Supports:** Not core research lifecycle — a short spoken aside in Section 3 (grounding a generative task in curated source material), with a link on the slide.
**Shape:** Curated source material (exam question pool, regulations) → structured, purpose-built study resource via iterative generation, verified against authoritative sources.
**Core line:** "AI can transform a curated body of source material into a new structured artifact tailored to a specific purpose" — a preview, in miniature, of what Section 3 (grounding) and Section 6 (structured writing) do for research.
**Status:** Resolved (2026-09-02) — one-line aside, not a case study. Repo is public: [github.com/adowling2/radio-extra-book](https://github.com/adowling2/radio-extra-book). Link it directly on the Section 3 slide.

## 5. Finishing papers after students graduate

**Supports:** Confirmed frame story for Outline Section 0 (open) and Section 8 (close) — bookending the talk.
**Shape:** Inheriting a project after the person who wrote the analysis has moved on — using AI to understand unfamiliar code, reconstruct how analyses work, trace outputs back to scripts, understand undocumented design decisions, refactor enough to finish the manuscript, and check the paper against the actual implementation.
**Core line:** Preserving context in files/repos/logs/docs matters far more than preserving it inside an AI chat — because the person who *had* that context is gone, and so is any chat history they had with an AI about it.
**Status:** Resolved (2026-09-02). Confirmed as the bookend, reframed around *expediting* completion rather than only "recovery after abandonment" — e.g., "helping a graduating student (or their advisor) get a project across the finish line," which reads as proactive and applies more broadly to the audience than pure salvage work. Uses a real, anonymized project; no student named or identifiable. Open at Section 0 with the premise, resolve it at Section 8 once every practice (context files, the log, reproducible code, the audit) has been introduced.

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
