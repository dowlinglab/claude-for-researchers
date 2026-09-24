# Claude for Research: Beyond the Chatbot

A seminar for graduate students and faculty in Chemical and Biomolecular Engineering at the University of Notre Dame, on integrating generative AI into a deliberate, reproducible, and auditable research workflow — not just asking a chatbot questions or polishing prose.

## Event details

This is a **two-part series**. Both parts are in the same room, two weeks apart, and are designed to be taken together — Part 2 builds directly on the workspace and project each participant sets up in Part 1.

| | Part 1 | Part 2 |
|---|---|---|
| **Date** | Monday, September 28, 2026 | Monday, October 12, 2026 |
| **Time** | 3:30 – 5:15 PM | 3:30 – 5:15 PM |
| **Location** | McCourtney Hall, B01 Auditorium (Basement) | McCourtney Hall, B01 Auditorium (Basement) |

| | |
|---|---|
| **Format** | 1 hour 45 minutes per part: 25–35 slides, a hands-on activity on your own laptop, and time for questions and a group regroup |
| **Audience** | CBE graduate students and faculty, Notre Dame (faculty from other departments welcome) |
| **Speaker** | Alex Dowling |
| **RSVP** | [forms.gle/SnyVmEQkWwvq2bk3A](https://forms.gle/SnyVmEQkWwvq2bk3A) |

### Before Part 1

Setup time in the room is time not spent on the activity. Please arrive having done all five:

1. **Bring a laptop** with a charged battery — power at the seats is limited.
2. **Install the ChatGPT or Claude desktop app**, including Codex or Claude Code.
3. **Create a GitHub account.**
4. **Install GitHub Desktop.**
5. **Clone this repository** to get the workshop materials.

*The original single 1-hour slot (October 15, 2026, Carey Auditorium) was replaced by this two-part series; the abstract below was submitted against the original format.*

## Abstract

Generative AI is becoming part of the research environment, but its most powerful uses go far beyond asking a chatbot questions or polishing prose. This seminar will share practical lessons from a year of using GenAI tools (Gemini, ChatGPT/Codex, Claude) for literature exploration, software development, reproducible data analysis, scientific writing, and the completion of long-running research projects. We will discuss how to build effective AI-assisted workflows, organize project context, improve research code, and use AI to check papers against underlying data, code, and guidelines. The emphasis will be on concrete practices that make research more efficient, reproducible, and auditable while keeping scientific judgment and responsibility with the researcher.

**Why Claude?** Anthropic just announced free or heavily discounted Team plans for academic researchers. PIs can apply [here](https://claude.com/programs/team-plan-for-scientists) for their research groups. While aspects of this seminar are Claude-centric, the overall themes and recommendations apply across current AI tools.

*This abstract has already been submitted and is considered final — edit only if the actual submitted text changes. It lives only here; there is no separate `abstract.md`.*

## What this seminar is — and isn't

Claude is the hook — Anthropic's new academic Team plan is the immediate reason this talk exists — but this is **not** a Claude product tutorial. The content is drawn from a year of using Claude, ChatGPT/Codex, and Gemini across real research projects, and most of the recommendations are model-independent.

> The goal is not to have AI "do your research." The goal is to build a research workflow in which AI makes it easier to think deeply, work reproducibly, preserve context, and catch mistakes.

## Repository structure

This repository is the source of truth for the seminar. Decisions, rationale, and content live here — not only in chat history with an AI assistant used to help develop it.

```
claude-for-research/
├── outline.md       current high-level talk outline and two-part session map
├── slides/          current 54-slide Beamer deck and source
├── handout/         LaTeX leave-behind handout (not yet built)
├── resources/       companion guides, prompts, scripts, templates, and checks
├── notes/           decisions, source references, and planning history
└── README.md        this file
```

- **[outline.md](outline.md)** — the current act-level structure and narrative through-line.
- **[`slides/`](slides/README.md)** — the live-talk Beamer deck. Sparse text, worked examples, file trees, workflow diagrams.
- **[`resources/workshops/`](resources/workshops/README.md)** — the student-facing plan and build handoff for two hands-on CSTR workshops. The starter is not yet built; solutions and instructor notes stay in the separate private `claude-for-researchers-private` repository.
- **`notes/`** — project memory and source tracking:
  - [notes/seminar_design.md](notes/seminar_design.md) — deeper rationale and the bank of candidate stories/examples
  - [notes/open_questions.md](notes/open_questions.md) — remaining follow-up items
  - [notes/references.md](notes/references.md) — authoritative sources for claims about Anthropic/OpenAI/Google products and Notre Dame policy
  - [notes/demo_ideas.md](notes/demo_ideas.md) — candidate live-demo material, including personal examples this talk draws on

## Status

**Both session decks, the activities, and the handout are built and verified.** The overnight build of September 21–22 split the deck, reworked the activities, and produced the handout; all five private release checks and the public documentation check passed against the merged starter.

Per-meeting budget, approved by Alex: **35 minutes presentation, 10 Q&A, 45 hands-on, 15 regroup.**

| Artifact | State |
|---|---|
| `slides/part1.pdf` | 27 frames — Part 1, "Setting up a project" |
| `slides/part2.pdf` | 31 frames — Part 2, "Advanced features" |
| `slides/main.pdf` | 58 frames — both parts in one sequence |
| `handout/main.pdf` | 2 pages, standalone reference |
| `resources/workshops/cstr/` | Starter, session guide, and both activities |

**Outstanding before Part 1 on September 28** — see [notes/open_questions.md](notes/open_questions.md) for the full list:

1. **Send the announcement.** It has not gone out. The draft content and the arrival prerequisites are above; the RSVP form is live.
2. **Review the built PDFs.** Generated and handed to Alex for review on September 24; no changes have been made from that review yet.
3. **Rehearse both decks** against the 35-minute slot.
4. **Recheck time-sensitive claims** — model availability, product limits, Notre Dame approvals. The overnight edit preserved the existing claims rather than re-auditing them.
5. **Capture the desktop-app screenshot** for Part 1 frame 12; the placeholder remains.
6. **Decide when to remove DRAFT**, still on both title slides.

Resuming on another machine: read [notes/machine_setup.md](notes/machine_setup.md) first. The conda environment is per-machine, the two checkouts are not siblings, and two LaTeX documents fail quietly without extra steps.

The deck's content was revised after the September 11, 2026 practice talk and again on September 14 from Alex's annotated read-through. It uses six research tasks, with expanded workspace setup, literature-guided writing, overnight work, and concrete review visuals. The companion resources are complete and cross-referenced from the talk.

## License

BSD 3-Clause — see [LICENSE](LICENSE).
