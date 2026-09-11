# Practices

Ten best-practice files distilled from a year of AI-assisted research work — refactors, package releases, manuscript audits, method development — including the parts that did not work.

They are written to be **used with an AI assistant**, not just read. Each has stable numbered sections so a prompt can cite one (`follow §4 of manuscript_audit.md`), a checklist, a list of anti-patterns, and paste-ready invocations at the end.

## Which file do I want?

"Used live as" points at the seminar task where the talk actually demonstrates this file (`../../slides/storyboard.md`'s Task 1–6); a file with no live task is still real, checklist-usable doctrine — see `../README.md` for the full status note.

| I need to… | Read | Used live as |
|---|---|---|
| Set up a project so an AI agent can work in it — and keep the record straight across sessions, tools, and machines | [working_with_ai_agents.md](working_with_ai_agents.md) | Tasks 1 and 6 |
| Move from exploratory scripts and notebooks to code someone else can rerun — and know what to verify at each stage | [scientific_computing_workflow.md](scientific_computing_workflow.md) | Tasks 2 and 6 |
| Release research code as an installable package without leaking private data or breaking my own results | [private_code_to_public_package.md](private_code_to_public_package.md) | Task 2 |
| Draft or revise a manuscript | [technical_writing.md](technical_writing.md) | Task 5 |
| Write in the group's voice, or derive a style guide of my own | [writing_style_guide.md](writing_style_guide.md) | Task 5 |
| Make figures and tables that are correct, readable, and traceable to what produced them | [scientific_figures_tables.md](scientific_figures_tables.md) | Tasks 5 and 6 |
| Check a paper against its code, data, and results before reviewers do | [manuscript_audit.md](manuscript_audit.md) | Task 4 |
| Explore a new research idea, or process a corpus of papers into an onboarding document | [literature_review.md](literature_review.md) | Task 3 |
| Draft or revise a grant proposal against a sponsor's form | [grant_proposal_writing.md](grant_proposal_writing.md) | Task 3 |
| Keep one real history for a LaTeX manuscript edited in Overleaf and locally | [latex_overleaf_workflow.md](latex_overleaf_workflow.md) | Task 3 |

## How they fit together

Roughly the arc of a project:

```
working_with_ai_agents ──── applies throughout ─────────────────────┐
                                                                    │
scientific_computing_workflow ──► private_code_to_public_package    │
        (build it, verify it)          (release it)                 │
                                                                    │
technical_writing ──► writing_style_guide                           │
   (structure)            (voice)                                   │
        └──► scientific_figures_tables                              │
                  (evidence)                                        │
                        └──► manuscript_audit ◄────────────────────┘
                              (check all of it)
```

`working_with_ai_agents.md` is the one to read first — the others assume its guardrails and its rules about project memory.

## Conventions

- **Tool-agnostic**, with tool-specific mechanics marked and dated. Vendor conventions drift; share instruction content explicitly rather than assuming every tool discovers the same files.
- **Every rule carries its reason.** Rules without reasons get discarded the first time they are inconvenient.
- **Rules that must hold have a way to fail.** Written instructions are advisory; see `working_with_ai_agents.md` §9. The tools in [`../scripts/`](../scripts/) exist to turn some of these into gates.
- **Practices, not projects.** These are generalized. Nothing here identifies a specific paper, repository, or person.

## Using them in your own repository

Copy the files you want into your project (or reference this repository), and point your assistant at them from your project's entry-point file:

```markdown
Follow `practices/working_with_ai_agents.md` §5 (standing rules) and §6
(guardrails) for all work here. For code, follow
`practices/scientific_computing_workflow.md`. For prose, follow
`practices/technical_writing.md` and `practices/writing_style_guide.md`.
```

Each file's closing section has more specific invocations for one-off tasks and audits.
