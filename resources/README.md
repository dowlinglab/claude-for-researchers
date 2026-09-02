# Resources

The actual takeaways: polished, reusable artifacts students can apply to their own research on Monday morning. Per [CLAUDE.md](../CLAUDE.md), this is a deliberately small set of well-built resources rather than a large prompt library.

Resources come in two layers:

- **`practices/`** — the doctrine. Seven best-practice files, each mapped to a seminar section, written to be used *with* an AI assistant (as repo context, as a task prompt, or as an audit checklist) rather than just read.
- **`prompts/`, `templates/`, `scripts/`** — the tools. Runnable or copy-pasteable things that operationalize the practices and cite them by section rather than restating them.

Design principle for everything here: inspect before editing, distinguish fact from inference, report uncertainty, preserve provenance, never invent missing information, make small auditable changes, verify after changing anything, and summarize what changed and what's unresolved.

## Layer 1: `practices/` — the seven best-practice files

Each file uses the same shape: what it is and when to use it → numbered practice sections (stable, so a prompt can cite `§5`) → checklist → anti-patterns → how to use it with an AI assistant. Target length is 150–300 lines; anything longer stops being loaded and starts being skimmed.

All seven are tool-agnostic, with tool-specific mechanics confined to one clearly marked section carrying a staleness warning.

| File | Seminar section | Scope | Status |
|---|---|---|---|
| `working_with_ai_agents.md` | 2, 5 | Session conduct, roles, guardrails, project memory, document lifecycle, portability across tools and machines | **Drafted** |
| `scientific_computing_workflow.md` | 4 | Notebooks → modules, baseline-then-refactor, phase-matched verification, run provenance | **Drafted** |
| `manuscript_audit.md` | 7 | Claim tracing, status vocabularies, standards of evidence, retraction | Next |
| `technical_writing.md` | 6 | Structure, notation, submission readiness, AI-prose drift signals | Planned |
| `writing_style_guide.md` | 6 | How to derive and refine a style guide; the Dowling Lab register as the worked instance and group standard | Planned |
| `scientific_figures_tables.md` | 6 | Figure standards, reproducible figures, tables generated not retyped | Planned |
| `private_code_to_public_package.md` | 4 | Packaging, isolating private data, release engineering, human-only steps | Planned |

Three naming and scope decisions worth recording:

- **`writing_style_guide.md` does three jobs** (revised 2026-09-02, at Alex's request): (1) the transferable *method* for deriving and refining a style guide from your own prior writing, (2) the Dowling Lab register spelled out as the worked instance, and (3) a standard students can actually write group papers against going forward. One file rather than three, because the method and the instance teach each other — and because the group register and the PI's register are legitimately the same thing in an academic group, which the source material already says explicitly ("the prose pass should read as the first author writing in the group's established register").
- **Not named for one person.** A filename carrying an author's name teaches students to imitate a voice rather than to derive one. The file is explicit about which parts are the group standard and which are one author's habits, and closes with how to adapt it when writing outside the group.
- **`manuscript_audit.md` is a practice file, not only a prompt.** The audit is the seminar's climax and has the deepest evidence base; the prompt version (below) operationalizes it.

## Layer 2: tools

**Prompts** (`prompts/`)

1. **`organize_research_repo.md`** — Examine an existing research repository and propose a target architecture (single repo vs. split code/manuscript, staged migration plan) without touching anything until a human approves the plan.
2. **`manuscript_audit.md`** — The audit toolkit as one prompt with modes: quantitative-claim tracing, methods-vs-code, figure-vs-text, journal-guideline compliance. Cites `practices/manuscript_audit.md` rather than repeating it.
3. **`literature_workflow.md`** — Process a folder of PDFs: inspect metadata, determine the real citation and DOI, rename consistently, flag duplicates and uncertain metadata (never guess), generate/update `literature.md` and BibTeX.

**Templates** (`templates/`)

4. **`research_log.md`** — The persistent-log template from Outline Section 5.
5. **`results_manifest.md`** — Connecting a manuscript to the exact commit, script, config, and output behind each figure and table.
6. **`project_entry_point.md`** — A tool-neutral project context file, per `practices/working_with_ai_agents.md` §2, with thin `CLAUDE.md`/`AGENTS.md` pointer files.

**Scripts** (`scripts/`)

7. **`doi_checker/`** — Verifies DOIs against Crossref in two passes kept deliberately apart: does an existing DOI resolve to the work the entry describes, and does Crossref know one for entries lacking it. Proposes, never writes. Adapted from an existing working script; the main work is parameterizing hardcoded paths into `--bib` / `--tex` / `--mailto` arguments.
8. **`check_margins.py`** — Geometric overfull-box detection from a rendered PDF, because a clean LaTeX build does not reliably surface them. Already general-purpose; needs packaging and a README.
9. **`check_docs.py`** — New, ~40 lines. Flags internal links that don't resolve, living documents older than the commits that changed what they describe, and supersession banners naming files that don't exist. Turns `practices/working_with_ai_agents.md` §9 from advice into a gate.

## Also planned (lower priority)

- **`checklists/reproducibility_and_handoff_checklist.md`** — Reproducibility and "handing a project to the next person" combined, since both are the same test: can someone else install, understand, and extend this?
- **`examples/repository_patterns/single_repo.md`** and **`split_code_paper_repos.md`** — Worked examples of both patterns, with the provenance-manifest connection explained for the split case.

## Deliberately not building

- A project-README template and a computational-research `.gitignore` — useful but not distinctive; point to well-maintained existing templates in the handout instead.
- A journal-selection decision-matrix generator — see [notes/seminar_design.md](../notes/seminar_design.md); journal selection is one bullet in the live talk.

## Layout

```
resources/
├── README.md                          this file
├── practices/                          the seven best-practice files
│   ├── working_with_ai_agents.md
│   ├── scientific_computing_workflow.md
│   ├── manuscript_audit.md
│   ├── technical_writing.md
│   ├── writing_style_guide.md
│   ├── scientific_figures_tables.md
│   └── private_code_to_public_package.md
├── prompts/
│   ├── organize_research_repo.md
│   ├── manuscript_audit.md
│   └── literature_workflow.md
├── templates/
│   ├── research_log.md
│   ├── results_manifest.md
│   └── project_entry_point.md
├── scripts/
│   ├── doi_checker/
│   ├── check_margins.py
│   └── check_docs.py
├── checklists/
│   └── reproducibility_and_handoff_checklist.md
└── examples/
    └── repository_patterns/
        ├── single_repo.md
        └── split_code_paper_repos.md
```
