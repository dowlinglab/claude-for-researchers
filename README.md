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
| **Format** | 1 hour 45 minutes per part: 35-minute presentation, 10-minute Q&A, 45-minute activity, and 15-minute regroup |
| **Audience** | CBE graduate students and faculty, Notre Dame (faculty from other departments welcome) |
| **Speaker** | Alex Dowling |
| **RSVP** | [forms.gle/SnyVmEQkWwvq2bk3A](https://forms.gle/SnyVmEQkWwvq2bk3A) |

### Before Part 1

Setup time in the room is time not spent on the activity. Please arrive having done all five:

1. **Bring a laptop** with a charged battery — power at the seats is limited.
2. **Install the ChatGPT or Claude desktop app**, including Codex or Claude Code.
3. **Create a GitHub account.**
4. **Install GitHub Desktop.**
5. **Download the Workshop 1 notebook ZIP** below. Cloning this whole repository is optional for the first activity.

*The original single 1-hour slot (October 15, 2026, Carey Auditorium) was replaced by this two-part series; the abstract below was submitted against the original format.*

## Workshop materials

For **Workshop 1**, [download the notebook ZIP](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/cstr/workshop1_notebook.zip). It contains an exploratory notebook and a YAML parameter file; the CSV and figure are generated when you run the notebook. Unzip it and follow the [four-step activity](resources/workshops/cstr/activities/01_notebook_to_reproducible_project.md) to create your own private Git repository, reproduce and audit the result, extract tested Python functions, and choose [one analysis extension](resources/workshops/cstr/activities/workshop1_extensions.md). The [session guide](resources/workshops/cstr/activities/session_guide.md) explains the in-room route and how to save a partial checkpoint.

For **Workshop 2**, use the [session guide](resources/workshops/cstr/activities/session_guide.md) and the [evidence-linked report activity](resources/workshops/cstr/activities/02_evidence_linked_report.md). The [CSTR workshop overview](resources/workshops/cstr/README.md) explains how the two activities connect.

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
claude-for-researchers/
├── outline.md       current high-level talk outline and two-part session map
├── slides/          sources for two session decks and their activities
├── handout/         sources for two two-page summary/activity sheets
├── resources/       companion guides, prompts, scripts, templates, and checks
├── notes/           decisions, source references, and planning history
└── README.md        this file
```

- **[outline.md](outline.md)** — the current act-level structure and narrative through-line.
- **[`slides/`](slides/README.md)** — Beamer sources for the two decks. Sparse text, worked examples, file trees, workflow diagrams.
- **[`handout/`](handout/README.md)** — LaTeX sources for the two-page session handouts.
- **[`resources/workshops/`](resources/workshops/README.md)** — the student-facing plan and build handoff for two hands-on CSTR workshops. The starter is built; solutions and instructor notes stay in the separate private `claude-for-researchers-private` repository.
- **`notes/`** — project memory and source tracking:
  - [notes/seminar_design.md](notes/seminar_design.md) — deeper rationale and the bank of candidate stories/examples
  - [notes/open_questions.md](notes/open_questions.md) — remaining follow-up items
  - [notes/references.md](notes/references.md) — authoritative sources for claims about Anthropic/OpenAI/Google products and Notre Dame policy
  - [notes/demo_ideas.md](notes/demo_ideas.md) — candidate live-demo material, including personal examples this talk draws on

## Build the slides and handouts

The PDF decks and handouts are generated locally and are not tracked in Git. With a LaTeX toolchain installed, run:

```bash
make -C slides
make -C handout
```

This builds the 32-slide Part 1 deck, the 36-slide Part 2 deck, and a two-page handout for each part. The [slide build guide](slides/README.md) and [handout print guide](handout/README.md) have details. Instructor answers stay in a separate private repository.

For development notes, see [open questions](notes/open_questions.md). On another machine, read the [machine setup notes](notes/machine_setup.md) first.

## License

BSD 3-Clause — see [LICENSE](LICENSE).
