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
| **Format** | 1 hour 45 minutes per part: about 28 minutes of presentation, a 30-minute hands-on activity on your own laptop, and a group recap |
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
- **[`handout/`](handout/README.md)** — a denser LaTeX leave-behind: checklists, prompts, and reference material that doesn't fit in the presentation portions.
- **[`resources/`](resources/README.md)** — reusable practice guides, prompts, scripts, templates, a checklist, and a repository example. The student-facing workshop starter (`resources/workshops/`) has not been built yet — see Status.
- **`notes/`** — project memory and source tracking:
  - [notes/seminar_design.md](notes/seminar_design.md) — deeper rationale and the bank of candidate stories/examples
  - [notes/open_questions.md](notes/open_questions.md) — remaining follow-up items
  - [notes/references.md](notes/references.md) — authoritative sources for claims about Anthropic/OpenAI/Google products and Notre Dame policy
  - [notes/demo_ideas.md](notes/demo_ideas.md) — candidate live-demo material, including personal examples this talk draws on

## Status

**The event moved from a single 1-hour talk to a two-part, hands-on series (September 21, 2026).** The repository is mid-transition:

- **Done.** Event details and the RSVP link, the arrival prerequisites, the session shape (55 presentation minutes across both parts, a 30-minute activity and a group recap in each), the two-part session map in [outline.md](outline.md), and the repository-boundary rules in [CLAUDE.md](CLAUDE.md).
- **Not done — blocking.** The student-facing workshop starter under `resources/workshops/` is missing. It existed and was validated on September 15, 2026, but the commit it was validated at is not reachable in this repository or on `origin`; see item 8 of [notes/open_questions.md](notes/open_questions.md). Until it is recovered or rebuilt there is nothing for participants to clone and nothing for them to do in either session.
- **Not done.** The 54-slide deck is still one continuous sequence timed for a 40-minute talk. Splitting it is now a split rather than a cut, since the two parts together allow 55 minutes.

The deck itself was revised after the September 11, 2026 practice talk and again on September 14 from Alex's annotated read-through. It uses six research tasks, with expanded workspace setup, literature-guided writing, overnight work, and concrete review visuals. The title slide still says **DRAFT** by request. The companion resources are complete and cross-referenced from the talk; the separate handout remains unbuilt.

## License

BSD 3-Clause — see [LICENSE](LICENSE).
