# Claude for Research: Beyond the Chatbot

A seminar for graduate students and faculty in Chemical and Biomolecular Engineering at the University of Notre Dame, on integrating generative AI into a deliberate, reproducible, and auditable research workflow — not just asking a chatbot questions or polishing prose.

## Event details

This is a **two-part series**. Both parts are in the same room, two weeks apart, and are designed to be taken together — Part 2 builds directly on the workspace and project each participant sets up in Part 1.

| | Part 1 | Part 2 |
|---|---|---|
| **Date** | Monday, September 28, 2026 | Monday, October 12, 2026 |
| **Time** | 3:30 – 5:15 PM | 3:30 – 5:15 PM |
| **Location** | McCourtney Hall West, B01 Auditorium (Basement) | McCourtney Hall West, B01 Auditorium (Basement) |

| | |
|---|---|
| **Format** | 1 hour 45 minutes per part: 35-minute presentation, 10-minute Q&A, 45-minute activity, and 15-minute regroup |
| **Audience** | CBE graduate students and faculty, Notre Dame (faculty from other departments welcome) |
| **Speaker** | Alex Dowling |
| **RSVP** | [forms.gle/SnyVmEQkWwvq2bk3A](https://forms.gle/SnyVmEQkWwvq2bk3A) |

### Prepare to attend

Setup time in the room is time not spent on the activity. Before Part 1, please:

1. **Bring a laptop** with a charged battery — power at the seats is limited.
2. Ask your PI to [apply for Anthropic's team plan for scientists](https://claude.com/programs/team-plan-for-scientists) and add you if approved.
3. Install the [Claude](https://claude.com/download) or [ChatGPT](https://chatgpt.com/download/) desktop app.
4. Create a [GitHub account](https://github.com); you can also apply for the optional [GitHub Education upgrade](https://github.com/education).
5. Install [GitHub Desktop](https://desktop.github.com/download/).
6. Clone the [workshop repository](https://github.com/dowlinglab/claude-for-researchers) and [download the Workshop 1 notebook ZIP](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/cstr/workshop1_notebook.zip). Unzip and open its `cstr-project/` folder for the activity; the notebook in this seminar repository is only the source for the ZIP.
7. If you do not already have Conda, [install Miniconda](https://www.anaconda.com/download/success?reg=skipped-miniconda). An existing Anaconda installation works too.

You do not need to run the notebook or create its environment before the workshop.

## Workshop materials

For **Part 1**, [download the notebook ZIP](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/cstr/workshop1_notebook.zip). It contains an exploratory notebook and a YAML parameter file. Unzip it, open the folder in Claude, and follow the [Activity 1 guide](resources/workshops/cstr/activities/01_notebook_to_reproducible_project.md): ask Claude to walk you through turning the folder into a clean GitHub repository, explaining each step. The guide gives starter prompts, questions, and checkpoints rather than commands. The optional "keep going" paths lead to running and auditing the notebook, extracting tested functions, and one [analysis extension](resources/workshops/cstr/activities/workshop1_extensions.md). The [session guide](resources/workshops/cstr/activities/session_guide.md) explains the two sessions.

For **Part 2**, [download the audit project ZIP](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/stats_audit/workshop2_audit_project.zip) and follow the [Activity 2 guide](resources/workshops/stats_audit/activity.md). You audit a colleague's statistical analysis of the public Palmer Penguins data against open statistics references, verify a sample of what Claude reports, and judge the quality of the audit. The [exercise overview](resources/workshops/stats_audit/README.md) explains the files. The longer [reactor-report audit](resources/workshops/cstr/activities/02_evidence_linked_report.md) remains as an optional take-home.

## Abstract

Generative AI is becoming part of the research environment, but its most powerful uses go far beyond asking a chatbot questions or polishing prose. This seminar will share practical lessons from a year of using GenAI tools (Gemini, ChatGPT/Codex, Claude) for literature exploration, software development, reproducible data analysis, scientific writing, and the completion of long-running research projects. We will discuss how to build effective AI-assisted workflows, organize project context, improve research code, and use AI to check papers against underlying data, code, and guidelines. The emphasis will be on concrete practices that make research more efficient, reproducible, and auditable while keeping scientific judgment and responsibility with the researcher.

**Why Claude?** Anthropic just announced free or heavily discounted Team plans for academic researchers. PIs can apply [here](https://claude.com/programs/team-plan-for-scientists) for their research groups. While aspects of this seminar are Claude-centric, the overall themes and recommendations apply across current AI tools.

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

This builds the 34-slide Part 1 deck, the 41-slide Part 2 deck, and a two-page handout for each part. `make -C slides notes` builds instructor copies with speaker notes. The [slide build guide](slides/README.md) and [handout print guide](handout/README.md) have details. Instructor answers stay in a separate private repository.

To publish the four public PDFs, push a version tag such as `v1.0.0`. The
[release workflow](.github/workflows/release.yml) compiles the sources and
attaches the two slide decks and two handouts to a GitHub Release. It does not
publish instructor materials. A manual run from the Actions tab builds a
downloadable artifact without creating a release.

```bash
git tag -a v1.0.0 -m "Workshop materials v1.0.0"
git push origin v1.0.0
```

For development notes, see [open questions](notes/open_questions.md). On another machine, read the [machine setup notes](notes/machine_setup.md) first.

## License

BSD 3-Clause — see [LICENSE](LICENSE).
