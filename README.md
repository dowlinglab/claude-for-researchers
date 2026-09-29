# Claude (or Codex) for Research: Beyond the Chatbot

A seminar for graduate students and faculty in Chemical and Biomolecular Engineering at the University of Notre Dame, on integrating generative AI into a deliberate, reproducible, and auditable research workflow — not just asking a chatbot questions or polishing prose.

## Event details

This is a **two-part series**. Both parts are in the same room, two weeks apart. Part 2 opens with a recap of Part 1, and each part has its own activity download, so someone who misses one session can still follow the other.

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
6. Clone the [workshop repository](https://github.com/dowlinglab/claude-for-researchers) and download the Part 1 activity ZIP (see [Workshop materials](#workshop-materials)).
7. If you do not already have Conda, [install Miniconda](https://www.anaconda.com/download/success?reg=skipped-miniconda). An existing Anaconda installation works too.

You do not need to run the activity notebook or create its environment before the workshop.

For Part 2, bring the same laptop and accounts and download the Part 2 activity ZIP.

## Workshop materials

Each part has one downloadable activity, taken from the latest release, and one guide. Open the unzipped folder in Claude and follow the guide.

| | Download | Guide |
|---|---|---|
| **Part 1** | [`workshop1_activity.zip`](https://github.com/dowlinglab/claude-for-researchers/releases/latest/download/workshop1_activity.zip) | [Activity 1 guide](resources/workshops/cstr/activities/01_notebook_to_reproducible_project.md) |
| **Part 2** | [`workshop2_activity.zip`](https://github.com/dowlinglab/claude-for-researchers/releases/latest/download/workshop2_activity.zip) | [Activity 2 guide](resources/workshops/stats_audit/activity.md) |

The [session guide](resources/workshops/cstr/activities/session_guide.md) explains how the two sessions fit together. The slides and handouts are attached to each [release](https://github.com/dowlinglab/claude-for-researchers/releases), with the two ZIPs, so the activities match the slides they accompany.

## Abstract

Generative AI is becoming part of the research environment, but its most powerful uses go far beyond asking a chatbot questions or polishing prose. This seminar will share practical lessons from a year of using GenAI tools (Gemini, ChatGPT/Codex, Claude) for literature exploration, software development, reproducible data analysis, scientific writing, and the completion of long-running research projects. We will discuss how to build effective AI-assisted workflows, organize project context, improve research code, and use AI to check papers against underlying data, code, and guidelines. The emphasis will be on concrete practices that make research more efficient, reproducible, and auditable while keeping scientific judgment and responsibility with the researcher.

**Why Claude?** Anthropic offers free or heavily discounted Team plans for academic researchers. PIs can apply [here](https://claude.com/programs/team-plan-for-scientists) for their research groups. While aspects of this seminar are Claude-centric, the overall themes and recommendations apply across current AI tools.

## What this seminar is — and isn't

Claude is the hook (Anthropic's academic Team plan is the immediate reason this talk exists), but this is **not** a Claude product tutorial. The content is drawn from a year of using Claude, ChatGPT/Codex, and Gemini across real research projects, and most of the recommendations are model-independent.

> The goal is not to have AI "do your research." The goal is to build a research workflow in which AI makes it easier to think deeply, work reproducibly, preserve context, and catch mistakes.

## Repository structure

This repository is the source of truth for the seminar. Decisions, rationale, and content live here — not only in chat history with an AI assistant used to help develop it.

```
claude-for-researchers/
├── outline.md       act-level outline of the talk
├── slides/          sources for the two decks and facilitator run sheets
├── handout/         sources for the two printed handouts
├── resources/       practice guides, prompts, scripts, templates, and the two activities
├── notes/           design rationale, open questions, sources, and machine setup
├── .github/         the release workflow
├── CLAUDE.md        working instructions for AI assistants in this repository
├── LICENSE          BSD 3-Clause
└── NOTICE.md        material the license does not cover
```

- **[outline.md](outline.md)** — the current act-level structure and narrative through-line.
- **[`slides/`](slides/README.md)** — Beamer sources for the two decks, and the facilitator run sheets.
- **[`handout/`](handout/README.md)** — LaTeX sources for the two printed handouts.
- **[`resources/workshops/`](resources/workshops/README.md)** — the activity materials for the two parts and the downloads they use. Solutions and instructor notes stay in the separate private `claude-for-researchers-private` repository.
- **`notes/`** — project memory and source tracking:
  - [notes/seminar_design.md](notes/seminar_design.md) — why the seminar is built the way it is
  - [notes/open_questions.md](notes/open_questions.md) — remaining follow-up items
  - [notes/references.md](notes/references.md) — authoritative sources for claims about Anthropic/OpenAI/Google products and Notre Dame policy

## Build the slides and handouts

The PDFs are generated and are not tracked in Git. With a LaTeX toolchain installed, run:

```bash
make -C slides
make -C handout
```

This builds one deck and one handout for each part. The [slide build guide](slides/README.md) and [handout print guide](handout/README.md) have details, including the facilitator run sheets. Instructor answers stay in a separate private repository.

To publish a release, push a version tag such as `v1.1.0`. The [release workflow](.github/workflows/release.yml) builds the slides, the handouts, and the two activity ZIPs, and attaches them to a GitHub Release. It does not publish instructor materials. A manual run from the Actions tab builds the same files as a downloadable artifact without creating a release.

```bash
git tag -a v1.1.0 -m "Workshop materials v1.1.0"
git push origin v1.1.0
```

For development notes, see [open questions](notes/open_questions.md). On another machine, read the [machine setup notes](notes/machine_setup.md) first.

## License

The code, slide and handout sources, guides, prompts, and templates are released under the BSD 3-Clause license (see [LICENSE](LICENSE)). The University of Notre Dame logos and marks, and the screenshots and images from other sources, are not covered by that license and stay subject to their owners' terms. See [NOTICE.md](NOTICE.md).
