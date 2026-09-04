# Resources

The actual takeaways: polished, reusable artifacts students can apply to their own research on Monday morning. Per [CLAUDE.md](../CLAUDE.md), this is a deliberately small set of well-built resources rather than a large prompt library.

Resources come in two layers:

- **`practices/`** — the doctrine. Nine best-practice files, each mapped to one of the talk's numbered tasks, written to be used *with* an AI assistant (as repo context, as a task prompt, or as an audit checklist) rather than just read.
- **`prompts/`, `templates/`, `scripts/`** — the tools. Runnable or copy-pasteable things that operationalize the practices and cite them by section rather than restating them.

Design principle for everything here: inspect before editing, distinguish fact from inference, report uncertainty, preserve provenance, never invent missing information, make small auditable changes, verify after changing anything, and summarize what changed and what's unresolved.

## Layer 1: `practices/` — the ten best-practice files

Each file uses the same shape: what it is and when to use it → numbered practice sections (stable, so a prompt can cite `§5`) → checklist → anti-patterns → how to use it with an AI assistant. Target length is 150–300 lines; anything longer stops being loaded and starts being skimmed.

All ten are tool-agnostic, with tool-specific mechanics confined to one clearly marked section carrying a staleness warning.

**Task column relabeled 2026-09-04** from the old six-stage-lifecycle section numbers (`outline.md`'s framing, which [CLAUDE.md](../CLAUDE.md) itself calls out as no longer the live-talk plan) to the numbered tasks the live talk actually uses ([storyboard.md](../slides/storyboard.md)'s Task 1–7, threaded Prologue → Act I → Act II → Act III → Epilogue). Where a file backs more than one task, the primary one is listed first.

| File | Task | Scope | Status |
|---|---|---|---|
| `working_with_ai_agents.md` | 2 (also 7) | Session conduct, roles, guardrails, project memory, document lifecycle, portability across tools and machines | **Drafted** |
| `scientific_computing_workflow.md` | 4 (also 6) | Notebooks → modules, baseline-then-refactor, phase-matched verification, run provenance | **Drafted** |
| `manuscript_audit.md` | 5 (also 6, 7) | Claim tracing, status vocabularies, standards of evidence, retraction | **Drafted** |
| `technical_writing.md` | 6 | Structure, notation, submission readiness, AI-prose drift signals | **Drafted** |
| `writing_style_guide.md` | 6 (also 7) | How to derive and refine a style guide; the Dowling Lab register as the worked instance and group standard | **Drafted** |
| `scientific_figures_tables.md` | 6 (also 7) | Figure standards, reproducible figures, tables generated not retyped | **Drafted** |
| `private_code_to_public_package.md` | 4 | Packaging, isolating private data, release engineering, human-only steps | **Drafted** |
| `literature_review.md` | 3 | Idea-first vs. corpus-first, batch ingestion, two-pass verification, correction logs, getting-started reports | **Drafted** |
| `grant_proposal_writing.md` | 3, continued (Act II) | Drafting against sponsor forms, inline compliance review, latexdiff verification, template reuse across cycles | **Drafted** |
| `latex_overleaf_workflow.md` | 3, continued (Act II) | *(added 2026-09-04)* Overleaf ↔ GitHub ↔ local editor as one synced history, `todonotes` for open items, what to send when sharing a draft | **Drafted** |

Ten practice files total, added to as the underlying project inventory grew. See [practices/README.md](practices/README.md) for the "which file do I want?" index.

**Task 6 (added 2026-09-04) is what closed the gap for three of these files.** `technical_writing.md`, `writing_style_guide.md`, and `scientific_figures_tables.md` were fully drafted well before this date but backed by no live task anywhere in the talk — the old six-stage lifecycle's "Write" stage never got a home in the three-act storyboard. Task 6 ("inherit a project → an auditable draft manuscript," Act III) is that home; see `slides/sections/04_act3_challenge.tex`'s own header comment for the full rationale.

Three naming and scope decisions worth recording:

- **`writing_style_guide.md` does three jobs** (revised 2026-09-02, at Alex's request): (1) the transferable *method* for deriving and refining a style guide from your own prior writing, (2) the Dowling Lab register spelled out as the worked instance, and (3) a standard students can actually write group papers against going forward. One file rather than three, because the method and the instance teach each other — and because the group register and the PI's register are legitimately the same thing in an academic group, which the source material already says explicitly ("the prose pass should read as the first author writing in the group's established register").
- **Not named for one person.** A filename carrying an author's name teaches students to imitate a voice rather than to derive one. The file is explicit about which parts are the group standard and which are one author's habits, and closes with how to adapt it when writing outside the group.
- **`manuscript_audit.md` is a practice file, not only a prompt.** The audit is the seminar's climax and has the deepest evidence base; the prompt version (below) operationalizes it.

## Layer 2: tools

**Prompts** (`prompts/`)

1. **`organize_research_repo.md`** — ✅ Two prompts: get a from-scratch, never-versioned folder under git cleanly, or examine an existing research repository and propose a target architecture (single repo vs. split code/manuscript, staged migration plan). Neither touches anything until a human approves the plan.
2. **`manuscript_audit.md`** — ✅ The audit toolkit as one prompt with modes: quantitative-claim tracing, methods-vs-code, figure-vs-text, journal-guideline compliance. Cites `practices/manuscript_audit.md` rather than repeating it.
3. **`literature_workflow.md`** — ✅ Process a folder of PDFs: inspect metadata, determine the real citation and DOI, rename consistently, flag duplicates and uncertain metadata (never guess), generate/update `literature.md` and BibTeX.
4. **`proposal_review.md`** — ✅ *(added 2026-09-04)* Three modes for `grant_proposal_writing.md` (Task 3, continued): compliance review against a funding call (`\foacomment{}`, inline, flag-don't-fix), restoring the sponsor's exact wording, and expand-then-compress as two separate calls. Closes a parallel-structure gap: every other starring practice file already had a prompt counterpart.
5. **`getting_started.md`** — ✅ *(added 2026-09-04)* The Epilogue's closing prompt: point any chatbot at this repo after cloning it, answer ten short questions about your actual project, and get 2-4 specific file recommendations back instead of a generic tour. Works even without file access — degrades to "paste in `README.md`."

**Templates** (`templates/`)

5. **`research_log.md`** — ✅ The persistent-log template for the project-memory habit `practices/working_with_ai_agents.md` describes.
6. **`results_manifest.md`** — ✅ Connecting a manuscript to the exact commit, script, config, and output behind each figure and table.
7. **`project_entry_point.md`** — ✅ A tool-neutral project context file, per `practices/working_with_ai_agents.md` §2, with thin `CLAUDE.md`/`AGENTS.md` pointer files.

**Scripts** (`scripts/`)

These are meant to be **working defaults** that the group and others can drop into a project, not illustrations. Each ships with a README, arguments instead of hardcoded paths, and no dependencies beyond what the task genuinely needs.

8. **`doi_checker/`** — ✅ **Built and tested.** The nominal default DOI checker. Verifies references against Crossref in two passes kept deliberately apart *because they fail differently*: (1) for entries that have a DOI, does it resolve to the work the entry actually describes — fuzzy title match plus author-surname check, graded `MATCH` / `CHECK` / `MISMATCH`; (2) for entries lacking one, does Crossref know a DOI, proposed only above a stricter threshold. **It proposes and never writes**, because a DOI that resolves to the wrong paper is worse than a missing one and looks identical on the page. Adapted from a working script; the work is parameterizing paths into `--bib` / `--tex` / `--mailto` and restricting checks to keys actually cited.
9. **`figure_style/`** — ✅ **Built and tested.** The nominal default Python figure style. A small module implementing the group's publication-quality figure guidelines as matplotlib settings, plus a `save_fig` helper that enforces size, resolution, and format, and a short set of standard plot helpers. The point is that a project fixes figure conventions **centrally, once**, so later work inherits them — two separate projects independently discovered that scattering plot styling across dozens of scripts makes any later standard unenforceable. Ships with the compliance checklist from `practices/scientific_figures_tables.md` so a figure set can be audited against it.
10. **`check_margins.py`** — **Not started.** Geometric overfull-box detection from a rendered PDF, because a clean LaTeX build does not reliably surface them. Design sketch only; not in `resources/scripts/` yet.
11. **`latexdiff_check.sh`** — ✅ **Built and tested.** Diffs the working copy of a `.tex` file against its last committed version (or any ref — a submitted tag, say), compiles a word-level tracked-changes PDF, and cleans up its own build byproducts. Formalizes a habit found only as a reconstructed shell command in one of the projects surveyed — it existed nowhere as an actual tool before this.
12. **`check_docs.py`** — ✅ **Built and tested.** Flags markdown links that don't resolve, living documents the repository has moved past (measured in commits behind `HEAD`), and supersession banners naming a successor file that doesn't exist. Exits non-zero, so it can gate a commit or CI. This is `practices/working_with_ai_agents.md` §9 applied to the repository's own documentation — the rule that written instructions degrade unless something fails when they do.

**`checklists/reproducibility_and_handoff_checklist.md`** — ✅ *(built 2026-09-04)* Reproducibility and "handing a project to the next person" combined into one checklist with two halves (Receiving / Leaving), since both are the same test: can someone else install, understand, and extend this? Cites the practice files rather than repeating them.

**`examples/repository_patterns/single_repo.md`** — ✅ *(built 2026-09-04)* The one-repo pattern, worked from the real, git-verified `bits_for_gaps` decision (a REFACTOR_PLAN.md's locked day-one call: one repo, no separate paper repo, a curated data subset instead of the full 564 MB archive).

## Also planned (lower priority)

- **`examples/repository_patterns/split_code_paper_repos.md`** — The split pattern's worked example, with the provenance-manifest connection explained for that case. Not yet built — no real, git-verified instance of this pattern has turned up in the project inventory the way `single_repo.md`'s did.

## Deliberately not building

- A project-README template and a computational-research `.gitignore` — useful but not distinctive; point to well-maintained existing templates in the handout instead.
- A journal-selection decision-matrix generator — see [notes/seminar_design.md](../notes/seminar_design.md); journal selection is one bullet in the live talk.

## Layout

```
resources/
├── README.md                          this file
├── practices/                          the ten best-practice files
│   ├── README.md
│   ├── working_with_ai_agents.md
│   ├── scientific_computing_workflow.md
│   ├── manuscript_audit.md
│   ├── technical_writing.md
│   ├── writing_style_guide.md
│   ├── scientific_figures_tables.md
│   ├── private_code_to_public_package.md
│   ├── literature_review.md
│   └── grant_proposal_writing.md
├── prompts/
│   ├── organize_research_repo.md
│   ├── manuscript_audit.md
│   ├── literature_workflow.md
│   └── proposal_review.md
├── templates/
│   ├── research_log.md
│   ├── results_manifest.md
│   └── project_entry_point.md
├── scripts/
│   ├── doi_checker/
│   ├── figure_style/
│   └── check_docs.py                  check_margins.py (item 9 above): not started
├── checklists/
│   └── reproducibility_and_handoff_checklist.md
└── examples/
    └── repository_patterns/
        ├── single_repo.md
        └── split_code_paper_repos.md
```
