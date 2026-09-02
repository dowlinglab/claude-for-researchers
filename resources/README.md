# Resources

The actual takeaways: polished, reusable artifacts students can apply to their own research on Monday morning. Per [CLAUDE.md](../CLAUDE.md), this is a deliberately small set of well-built resources rather than a large prompt library — each entry below earns its place by being something a working researcher would plausibly reuse without heavy editing.

Design principle for every prompt in here (from the project charter, see [notes/seminar_design.md](../notes/seminar_design.md)): inspect before editing, distinguish fact from inference, report uncertainty, preserve provenance, never invent missing information, make small auditable changes, verify after changing anything, and summarize what changed and what's unresolved.

## Build first (priority order)

1. **`prompts/organize_research_repo.md`** — Examine an existing research repository and propose a target architecture (single repo vs. split code/manuscript, staged migration plan) without touching anything until a human approves the plan. Flagship resource — most broadly applicable, and it's the one referenced in Outline Section 4.
2. **`prompts/manuscript_audit.md`** — The audit toolkit: quantitative-claim tracing, methods-vs-code comparison, figure-vs-text comparison, and journal/guideline compliance, as modes of one prompt rather than four separate files (see [seminar_design.md](../notes/seminar_design.md) on why these were consolidated). This is the resource tied to the talk's climax (Outline Section 7).
3. **`prompts/literature_workflow.md`** — Process a folder of PDFs: inspect metadata, determine the real citation and DOI, rename consistently, flag duplicates and uncertain metadata (never guess), generate/update `literature.md` and BibTeX. Addresses a near-universal, tedious pain point.
4. **`scripts/doi_checker/`** — A small deterministic script (not just a prompt) that extracts DOIs from BibTeX/manuscripts, normalizes them, queries authoritative metadata, and flags mismatches — the seminar's concrete example of combining a script, authoritative external data, and AI judgment instead of asking a model to "just check my references."
5. **`templates/research_log.md`** — The persistent-log template from Outline Section 5: date, question, experiment, commit, config, datasets, outputs, interpretation, failed approaches, next questions. Low effort to adopt, high payoff.
6. **`templates/results_manifest.md`** — The results/provenance manifest pattern for connecting a manuscript to the exact code commit, script, config, and output behind each figure/table — pairs with the split-repo pattern in `examples/repository_patterns/`.
7. **`templates/CLAUDE.md.example`** — A stripped-down, annotated version of this repo's own [`CLAUDE.md`](../CLAUDE.md), showing the persistent-project-context pattern from Outline Section 2 in a form a student can drop into their own repo and adapt.

## Also planned (lower priority / blocked)

- **`checklists/reproducibility_and_handoff_checklist.md`** — One combined checklist covering general reproducibility and the "handing off a project after a student graduates" scenario, since both are really the same test (can someone else install, understand, and extend this?).
- **`examples/repository_patterns/single_repo.md`** and **`split_code_paper_repos.md`** — Worked, opinionated examples of both patterns from the charter, with the provenance-manifest connection explained for the split case.
- **`style/alex_dowling_writing_style.md`** — Blocked on Alex supplying the underlying style-analysis material (see [notes/open_questions.md](../notes/open_questions.md)). Doubles as a worked example of how a student could derive a style guide from their own prior writing.

## Deliberately not building separately

- A project-README template and a computational-research `.gitignore` — genuinely useful, but not distinctive enough to warrant their own polished resource; point to existing well-maintained templates (e.g., GitHub's own `.gitignore` collection) in the handout instead.
- A journal-selection decision-matrix generator — see [notes/seminar_design.md](../notes/seminar_design.md) for why this was cut from the live talk; not currently planned as a resource either, pending the open question there.

## Layout

```
resources/
├── README.md              this file
├── prompts/
│   ├── organize_research_repo.md
│   ├── literature_workflow.md
│   └── manuscript_audit.md
├── scripts/
│   └── doi_checker/
├── templates/
│   ├── research_log.md
│   ├── results_manifest.md
│   └── CLAUDE.md.example
├── checklists/
│   └── reproducibility_and_handoff_checklist.md
├── style/
│   └── alex_dowling_writing_style.md
└── examples/
    └── repository_patterns/
        ├── single_repo.md
        └── split_code_paper_repos.md
```
