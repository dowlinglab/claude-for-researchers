# Companion resources

These files turn the talk's recommendations into reusable guides, prompts, templates, checks, and examples. They are designed to be read by researchers and supplied directly to an AI agent as project context.

## Practice guides

| File | Primary use in the talk |
|---|---|
| [`grant_proposal_writing.md`](practices/grant_proposal_writing.md) | Task 3: proposal development and compliance |
| [`latex_overleaf_workflow.md`](practices/latex_overleaf_workflow.md) | Task 3: one manuscript across Overleaf, GitHub, and local tools |
| [`literature_review.md`](practices/literature_review.md) | Task 3: idea-first search and source verification |
| [`manuscript_audit.md`](practices/manuscript_audit.md) | Tasks 4–6: evidence-based audits |
| [`private_code_to_public_package.md`](practices/private_code_to_public_package.md) | Task 2: packaging and release hygiene |
| [`scientific_computing_workflow.md`](practices/scientific_computing_workflow.md) | Tasks 2 and 6: reproducibility and automated checks |
| [`scientific_figures_tables.md`](practices/scientific_figures_tables.md) | Tasks 5 and 6: reproducible figures and tables |
| [`technical_writing.md`](practices/technical_writing.md) | Task 5: auditable technical writing |
| [`working_with_ai_agents.md`](practices/working_with_ai_agents.md) | Tasks 1 and 6: bounded work, Git, and handoffs |
| [`writing_style_guide.md`](practices/writing_style_guide.md) | Task 5: preserve a group's established voice |

See [`practices/README.md`](practices/README.md) for a shorter “which guide should I use?” index.

## Ready-to-use artifacts

### Prompts

- [`getting_started.md`](prompts/getting_started.md): select useful resources for a real project.
- [`literature_workflow.md`](prompts/literature_workflow.md): process and verify a literature corpus.
- [`manuscript_audit.md`](prompts/manuscript_audit.md): audit claims, methods, figures, and guidelines.
- [`organize_research_repo.md`](prompts/organize_research_repo.md): place a project under version control and organize it.
- [`proposal_review.md`](prompts/proposal_review.md): check a proposal against sponsor requirements.

### Templates

- [`project_entry_point.md`](templates/project_entry_point.md): tool-neutral project instructions.
- [`research_log.md`](templates/research_log.md): decisions, evidence, failures, and next steps.
- [`results_manifest.md`](templates/results_manifest.md): connect claims and figures to exact computational artifacts.

### Scripts

- [`check_docs.py`](scripts/check_docs.py): detect broken links and stale documentation.
- [`doi_checker/`](scripts/doi_checker/): verify DOI metadata and propose missing DOIs without modifying the bibliography.
- [`figure_style/`](scripts/figure_style/): reusable matplotlib defaults and output checks.
- [`latexdiff_check.sh`](scripts/latexdiff_check.sh): build a tracked-changes PDF against a Git revision.

### Checklist and examples

- [`reproducibility_and_handoff_checklist.md`](checklists/reproducibility_and_handoff_checklist.md): receive or hand off a computational project.
- [`single_repo.md`](examples/repository_patterns/single_repo.md): a worked single-repository pattern.

- [`manuscript_revision/`](examples/manuscript_revision/README.md): two short LaTeX files for a real tracked-changes demonstration.

## Official tool documentation

- [Overleaf: GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization): linking projects, explicitly pushing/pulling, conflict handling, and size recommendations. Start here when configuring the writing repository; our [companion workflow](practices/latex_overleaf_workflow.md) explains the three-repository arrangement.

## Design principles

Inspect before editing. Distinguish facts from inferences. Preserve provenance. Make small auditable changes. Verify after changing anything. Record unresolved decisions rather than guessing.

All ten practice guides are named on the repository inventory slide. The six-task mapping above follows the September 11 practice-feedback revision.
