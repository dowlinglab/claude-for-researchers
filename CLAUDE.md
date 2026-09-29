# Project instructions: claude-for-research

Persistent context for any AI assistant (Claude, ChatGPT/Codex, Gemini, etc.) working in this repository. This file is itself a live example of the "context, not conversation" pattern the seminar teaches.

## What this repo is

Source material for a seminar, *Claude (or Codex) for Research: Beyond the Chatbot*, delivered to CBE graduate students and faculty at Notre Dame as a **two-part hands-on series**. Part 1 covers setting up a project; Part 2 covers advanced features. The two-week spacing is deliberate: participants experiment on their own work between the sessions. Each part is presentation plus a hands-on activity. See [README.md](README.md) for event details.

The thesis: the most powerful uses of GenAI in research go beyond chatbot Q&A and come from integrating AI into a deliberate, reproducible, auditable workflow. The reasoning behind the design is in [notes/seminar_design.md](notes/seminar_design.md).

**This repository is the source of truth for the project.** Content and durable rationale belong in files here, not only in chat history. History belongs in Git.

## Layout

| Path | Contents |
|---|---|
| `README.md` | Event details, downloads, and the abstract (already submitted, so final) |
| `outline.md` | Act-level outline and narrative through-line |
| `slides/` | Two Beamer decks built from shared sources (ND theme), facilitator run sheets, `storyboard.md` (frame map), `style_guide.md`, and `image_plan.md` |
| `handout/` | Two LaTeX handouts (summary front, activity back) |
| `resources/` | Reusable student takeaways: practice guides, prompts, templates, scripts, and the two activities under `resources/workshops/` (`cstr/` for Part 1 and an optional report audit, `stats_audit/` for Part 2) |
| `notes/` | Design rationale, open questions, sources with access dates, and machine setup |

## Working practices

1. **Keep the repository lean.** Durable rationale goes in [notes/seminar_design.md](notes/seminar_design.md), unresolved items in [notes/open_questions.md](notes/open_questions.md), and sources in [notes/references.md](notes/references.md). Do not keep diaries, dated logs, finished plans, or superseded drafts. Delete outdated files rather than archiving them: Git history is the archive.
2. **Preserve rationale**, not just outcomes, for non-obvious decisions. Write the *why*, not just the *what*.
3. **Prefer incremental changes.** Do not rewrite large portions of the repo unnecessarily. The abstract in `README.md` has already been submitted and is final. Do not edit it unless explicitly asked.
4. **Separate polished material from scratch notes.** Anything intended for students belongs in `slides/`, `handout/`, or `resources/`.
5. **Flag uncertainty.** Do not convert a guess into a seminar claim. This applies especially to claims about Anthropic/OpenAI/Google products and Notre Dame IT policy, which change quickly.
6. **Use authoritative sources** for claims about Claude, ChatGPT, Gemini, Notre Dame policy, or journal/technical standards. Track sources in [notes/references.md](notes/references.md), with an access date.
7. **Don't overfit to Claude.** Claude is the hook (academic Team plan access), but most recommendations should be model-independent. Distinguish general practice from tool-specific implementation where it matters.
8. **Optimize for teaching value, not technical elegance.** The test for any addition: "What should a graduate student remember and actually change about how they work on Monday morning?"
9. **Prefer a small number of polished resources over a large prompt library.** See [resources/README.md](resources/README.md). Don't add low-value prompt files without discussion.
10. **Git:** commit incrementally as coherent units of work land. Create new commits rather than amending. Review `git status` and the diff before staging.
11. **Keep slide sources readable.** Add comments only when they explain a durable implementation constraint.
12. **Two-repository boundary.** A private sibling repository, `claude-for-researchers-private`, holds the instructor-only half of the workshops: reference implementation, reference results, tolerances, rubrics, mutation tests, and expected outcomes. **Nothing from it may appear here**: not in a file, not in a commit message, not on a side branch. A public branch is public. Public writes are limited to student-facing material: the starter under `resources/workshops/cstr/`, activity instructions, templates, and general resources. Nothing that reveals an expected numerical answer, a rubric threshold, the seeded defects in the fallback report, or the planted problems in the statistics audit. The audit's notebook and write-up are public and contain those problems by design. What must never appear here, in files, comments, notes, or commit messages, is any statement of which problems exist, where they are, or why they are wrong.
13. **The starter must stay independently answerable.** A participant working only from this repository must be able to complete both activities. A clean-agent validation must use a copy of the public tree only, because telling an agent not to read an accessible answer folder is not an access control.
14. **Activities teach the mental model, not a command recipe.** A public step-by-step command sequence lets an agent reproduce the expected solution instead of reasoning, and leaves beginners copying syntax they do not understand. Activity handouts give the objective, the mental model, a few starter prompts, questions to ask, conceptual checkpoints, and troubleshooting prompts. Claude generates commands when they are needed. Do not add long runs of shell or Git commands to student-facing material.
15. **Keep top-level docs from going stale.** The README, this file, and the outline should not state slide or frame counts, page counts of built PDFs, or step-by-step activity detail. Point to the file that owns the detail: frame numbers live in `slides/storyboard.md`, activity steps in the activity guides, and the release contents in the release workflow.

## Content conventions

- Avoid generic AI-writing patterns in seminar content itself (inflated importance, formulaic transitions, excessive three-item lists, vague claims). The seminar teaches against this, so it should model good practice.
- No decorative AI/robot/brain imagery. Favor screenshots, repository trees, real workflow diagrams, checklists, and before/after examples.
- Slides: sparse text, strong hierarchy, built on the [ND Beamer template](https://github.com/dowlinglab/ND_Beamer_Template); see `slides/style_guide.md` for the rules. Handout: denser, and functions as a standalone reference after the talk.
