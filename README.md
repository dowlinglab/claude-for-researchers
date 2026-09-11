# Claude for Research: Beyond the Chatbot

A seminar for graduate students and faculty in Chemical and Biomolecular Engineering at the University of Notre Dame, on integrating generative AI into a deliberate, reproducible, and auditable research workflow — not just asking a chatbot questions or polishing prose.

## Event details

| | |
|---|---|
| **Date** | October 15, 2026 |
| **Time** | 11:00 AM – 12:00 PM (40-minute talk + 20 minutes of questions) |
| **Location** | Carey Auditorium, 107 Hesburgh Library, University of Notre Dame |
| **Audience** | CBE graduate students and faculty, Notre Dame (faculty from other departments welcome) |
| **Speaker** | Alex Dowling |

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
├── outline.md       current high-level talk outline
├── slides/          final 52-slide Beamer deck and source
├── handout/         LaTeX leave-behind handout (not yet built)
├── resources/       companion guides, prompts, scripts, templates, and checks
├── notes/           decisions, source references, and planning history
└── README.md        this file
```

- **[outline.md](outline.md)** — the current act-level structure and narrative through-line.
- **[`slides/`](slides/README.md)** — the live-talk Beamer deck. Sparse text, worked examples, file trees, workflow diagrams.
- **[`handout/`](handout/README.md)** — a denser LaTeX leave-behind: checklists, prompts, and reference material that doesn't fit in the 40-minute talk.
- **[`resources/`](resources/README.md)** — reusable practice guides, prompts, scripts, templates, a checklist, and a repository example.
- **`notes/`** — project memory and source tracking:
  - [notes/seminar_design.md](notes/seminar_design.md) — deeper rationale and the bank of candidate stories/examples
  - [notes/open_questions.md](notes/open_questions.md) — remaining follow-up items
  - [notes/references.md](notes/references.md) — authoritative sources for claims about Anthropic/OpenAI/Google products and Notre Dame policy
  - [notes/demo_ideas.md](notes/demo_ideas.md) — candidate live-demo material, including personal examples this talk draws on

## Status

The 52-slide practice-talk deck was audited, rebuilt, and finalized on September 11, 2026. The title slide still says **DRAFT** by request. The companion resources are complete and cross-referenced from the talk; the separate handout remains unbuilt. See [notes/open_questions.md](notes/open_questions.md) for the small number of remaining follow-up items.

## License

BSD 3-Clause — see [LICENSE](LICENSE).
