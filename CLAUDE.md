# Project instructions: claude-for-research

Persistent context for any AI assistant (Claude, ChatGPT/Codex, Gemini, etc.) working in this repository. This file is itself a live example of the "context, not conversation" pattern the seminar teaches — treat it as a demo candidate, not just internal config.

## What this repo is

Source material for a seminar, *Claude for Research: Beyond the Chatbot*, delivered to CBE graduate students and faculty at Notre Dame on October 15, 2026 in a 1-hour slot (40-minute talk + 20 minutes of questions) — see [README.md](README.md) for event details. The seminar's thesis: the most powerful uses of GenAI in research go beyond chatbot Q&A, and come from integrating AI into a deliberate, reproducible, auditable workflow. Full charter/rationale: [notes/seminar_design.md](notes/seminar_design.md).

**This repository is the source of truth for the project.** Decisions, rationale, and content belong in files here, not only in chat history.

## Layout

| Path | Contents |
|---|---|
| `README.md` | Event details and the abstract (already submitted — final, no separate `abstract.md`) |
| `outline.md` | Current act-level outline and narrative through-line |
| `slides/` | Current 55-slide Beamer deck (ND theme). `storyboard.md` records the slide sequence, `style_guide.md` the design rules, and `image_plan.md` the final visual inventory |
| `handout/` | Planned LaTeX leave-behind handout; not yet built |
| `resources/` | Polished, reusable student takeaways (prompts, scripts, templates) |
| `notes/` | Project memory: design rationale, remaining follow-ups, references, demo ideas, and the running decision log |

## Working practices

1. **Repository is the memory.** Important decisions get written into the relevant Markdown file, not left only in conversation. Ongoing decisions/actions go in [notes/seminar_notes.md](notes/seminar_notes.md); durable rationale goes in [notes/seminar_design.md](notes/seminar_design.md); unresolved items go in [notes/open_questions.md](notes/open_questions.md).
2. **Preserve rationale**, not just outcomes, for non-obvious decisions — write the *why*, not just the *what*.
3. **Prefer incremental changes.** Do not rewrite large portions of the repo unnecessarily. The abstract in `README.md` has already been submitted and is final — do not edit it unless explicitly asked.
4. **Separate polished material from scratch notes.** Anything intended for students belongs in `slides/`, `handout/`, or `resources/`. Brainstorming and unresolved ideas belong in `notes/`.
5. **Flag uncertainty.** Do not convert a guess into a seminar claim. This applies especially to claims about Anthropic/OpenAI/Google products and Notre Dame IT policy — both change quickly.
6. **Use authoritative sources** for claims about Claude, ChatGPT, Gemini, Notre Dame policy, or journal/technical standards. Track sources in [notes/references.md](notes/references.md), with an access date.
7. **Don't overfit to Claude.** Claude is the title and hook (academic Team plan access), but most recommendations should be model-independent. Distinguish general practice from Claude-specific, ChatGPT/Codex-specific, and Gemini-specific implementation where it matters.
8. **Optimize for teaching value, not technical elegance.** The test for any addition: "What should a graduate student remember and actually change about how they work on Monday morning?"
9. **Prefer a small number of polished resources over a large prompt library.** See [resources/README.md](resources/README.md) for the prioritized list — don't add low-value prompt files beyond it without discussion.
10. **Git:** commit incrementally as coherent units of work land, rather than batching a long session into one commit (Alex's standing preference, 2026-09-02). Create new commits rather than amending. Review `git status`/diff before staging.
11. **Keep final slide sources readable.** Detailed editorial notes were useful during refinement but were removed after the final audit on 2026-09-11. Recover them from Git history through commit `2c55c74` if needed; add new comments only when they explain durable implementation constraints.

## Content conventions

- Avoid generic AI-writing patterns in seminar content itself (inflated importance, formulaic transitions, excessive three-item lists, vague claims) — the seminar teaches against this, so it should model good practice.
- No decorative AI/robot/brain imagery. Favor screenshots, repository trees, real workflow diagrams, checklists, before/after examples.
- Slides: sparse text, strong hierarchy, built on the [ND Beamer template](https://github.com/dowlinglab/ND_Beamer_Template); see `slides/style_guide.md` for the specific rules (word-count targets, two body-text sizes, official colors only, no closing takeaway bar — the frame title states the point). Handout: denser, functions as a standalone reference after the talk.
