# Companion resources

These files turn the talk's recommendations into reusable guides, prompts, templates, checks, and examples. They are designed to be read by researchers and supplied directly to an AI agent as project context.

## Practice guides

| File | Primary use in the talk |
|---|---|
| [`grant_proposal_writing.md`](practices/grant_proposal_writing.md) | Task 3: proposal development and compliance |
| [`latex_overleaf_workflow.md`](practices/latex_overleaf_workflow.md) | Task 3: one manuscript across Overleaf, GitHub, and local tools |
| [`literature_review.md`](practices/literature_review.md) | Tasks 3 and 6: idea-first search and source verification |
| [`manuscript_audit.md`](practices/manuscript_audit.md) | Tasks 5–7: evidence-based audits |
| [`private_code_to_public_package.md`](practices/private_code_to_public_package.md) | Task 4: packaging and release hygiene |
| [`scientific_computing_workflow.md`](practices/scientific_computing_workflow.md) | Tasks 4 and 7: reproducibility and automated checks |
| [`scientific_figures_tables.md`](practices/scientific_figures_tables.md) | Task 7: reproducible figures and tables |
| [`technical_writing.md`](practices/technical_writing.md) | Task 6: auditable technical writing |
| [`working_with_ai_agents.md`](practices/working_with_ai_agents.md) | Tasks 2 and 7: bounded work, Git, and handoffs |
| [`writing_style_guide.md`](practices/writing_style_guide.md) | Task 6: preserve a group's established voice |

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

### Checklist and example

- [`reproducibility_and_handoff_checklist.md`](checklists/reproducibility_and_handoff_checklist.md): receive or hand off a computational project.
- [`single_repo.md`](examples/repository_patterns/single_repo.md): a worked single-repository pattern.

## Design principles

Inspect before editing. Distinguish facts from inferences. Preserve provenance. Make small auditable changes. Verify after changing anything. Record unresolved decisions rather than guessing.

The final slide audit confirmed that all ten practice guides are named on the repository inventory slide and linked from relevant examples in the deck.
