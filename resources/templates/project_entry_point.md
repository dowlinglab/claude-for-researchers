# Template: project entry point

The one file an AI assistant reads first — and the one a collaborator or a future you reads first too.

**Why a neutral name.** Tool-specific files (`CLAUDE.md`, `AGENTS.md`) are read automatically by one vendor's tool and ignored by the others. Keep the content in a tool-neutral file and make each tool's file a thin pointer to it. Then switching tools, or working with someone who uses a different one, costs nothing. See [`../practices/working_with_ai_agents.md`](../practices/working_with_ai_agents.md) §2 and §11.

**How to use this.** Copy the block below into `PROJECT.md` at your repository root, fill it in, and delete what doesn't apply. Then add the two pointer files at the end of this document.

**Keep it short.** Route to detail rather than inlining it; a long entry point stops being read. If it grows past about a screen and a half, move sections into their own files and link them.

---

```markdown
# <Project name>

<One to three sentences: what this project is and what question it answers.>

**Status:** <active | paused | wrapping up>   **Last updated:** <YYYY-MM-DD>

## Where things are

| Path / repo | Role |
|---|---|
| `src/<pkg>/` | <the method / the analysis code> |
| `scripts/` | <entry points; one per analysis> |
| `results/` | <computed outputs; not hand-edited> |
| `manuscript/` | <LaTeX source> |
| `<../other-repo>` | <its role — READ-ONLY, or the code this paper reports> |

Use repo-relative paths everywhere. This repository is checked out at different
absolute paths on different machines, and absolute paths go stale silently.

## How to run it

```bash
# environment
<conda env create -f environment.yml && conda activate <name>>

# the three commands that matter
<python scripts/run_analysis.py --config configs/base.yaml>
<python -m pytest -m "not slow">
<python scripts/make_figures.py>
```

<Any environment trap worth one sentence — a version that must be pinned and
why, a binary that must be on PATH, a step that fails silently if skipped.>

## Conventions

- <Convention that encodes a past failure, e.g. "results/ is written by scripts
  only; never hand-edit a file there.">
- <e.g. "Figures are saved with figure_style.save_fig so provenance is recorded.">
- <e.g. "Numerical results are deterministic; treat any change to them as a
  finding, not as noise.">

Standing rules for AI assistants: `practices/working_with_ai_agents.md` §5–§6.

## Current state

<Rewrite this section in place each time. It is the only section that must be
true right now — everything else changes slowly.>

- **Working on:** <the current thread, in one line>
- **Resume point:** <the exact next thing to do, specific enough to act on>
- **Uncommitted:** <what is in the working tree and why, or "nothing">
- **Blocked on:** <or "nothing">

## Open questions (for me, not the assistant)

<Decisions only a human can make. Keep them here so they don't scatter.>

- [ ] <question — with your current leaning, if you have one>
- [x] ~~<resolved question>~~ — decided <YYYY-MM-DD>: <the decision>

**Already decided — do not reopen:** <settled trade-offs that keep coming back up>

## Handoff

<Write this before stopping for the day, or before switching machines or tools.
Verified state, stated literally — "everything is pushed" is a belief, a commit
hash is a fact.>

```
## State snapshot — <YYYY-MM-DD>

Git:        <branch> at <hash>, identical to origin/<branch>. Working tree clean.
In flight:  <long-running job, where its output lands, when it started>
Resume:     <the first thing the next session should do>
For me:     <anything needing a human decision before work continues>
```
```

---

## Companion pointer files

Add these so any assistant lands on the same content. Both are three lines; the content lives in one place.

**`CLAUDE.md`**

```markdown
Read `PROJECT.md` first — it is the source of truth for this repository.

Follow `practices/working_with_ai_agents.md` §5 (standing rules) and §6
(guardrails). For code, `practices/scientific_computing_workflow.md`.
```

**`AGENTS.md`**

```markdown
Read `PROJECT.md` first — it is the source of truth for this repository.

Follow `practices/working_with_ai_agents.md` §5 (standing rules) and §6
(guardrails). For code, `practices/scientific_computing_workflow.md`.
```

## Two things that make this work

**Rewrite "Current state" in place; append everywhere else.** The common failure is an entry point that grows chronologically until the top of the file describes a project that no longer exists. If yours has already become chronological, put a pointer at the very top — *"For current state, start at the bottom; everything above is historical log, kept for narrative continuity, not as a to-do list"* — but a section rewritten in place is better.

**Three or four living documents, maximum.** This file, a decision queue, and a log. Everything else should be a dated record that is frozen by definition and therefore cannot go stale. See [`../practices/working_with_ai_agents.md`](../practices/working_with_ai_agents.md) §3.
