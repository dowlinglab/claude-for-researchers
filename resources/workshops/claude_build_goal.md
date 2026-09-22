# Claude Code handoff: build the CSTR workshop materials

Run Claude Code from the root of the private instructor repository,
`claude-for-researchers-private`. Confirm that the public repository
`claude-for-researchers` is available as a sibling checkout. The private
repository is initially almost empty, so the goal also asks Claude to establish
its concise project instructions. Then paste the goal below into Claude Code.

The `/goal` condition is intentionally measurable. Claude's goal evaluator sees
what Claude reports in the transcript; it does not independently run commands or
read files. Claude therefore needs to surface the final test, build, repository
boundary, and Git-status evidence in its completion report.

```text
/goal Build and validate version 1 of the two nonisothermal CSTR workshop activities described in ../claude-for-researchers/resources/workshops/cstr_two_workshop_plan.md. Treat the current claude-for-researchers-private repository as PRIVATE-EDIT for instructor answers, reference implementations, reference results, rubrics, mutation tests, and teaching notes. Treat ../claude-for-researchers as PUBLIC-EDIT only for student-facing starter materials, the executable starter notebook, activity instructions, templates, and general resources. Read ../claude-for-researchers/CLAUDE.md and any existing private-repository instructions, then inspect both repositories before changing anything. If this private repository has no CLAUDE.md, create a concise one that records the repository roles, write boundaries, verification commands, and prohibition on copying instructor answers into public history.

Work through the implementation phases and gates in the plan. The public starter must include a scientifically sound executable nonisothermal CSTR notebook, a documented environment, starter project structure, exact instructions for both 1.75-hour activities, literature and LaTeX templates, a fallback report for the audit activity, and commands that work from a clean copy. The private repository must include the reference implementation and results, tolerances, activity_answers, rubrics, known fallback-report findings, common agent failures, and mutation checks. Do not commit copyrighted or access-restricted PDFs. Do not place answers in the public repository, another public branch, or public Git history. Preserve unrelated existing work.

Use small coherent commits in each repository after its relevant checks pass, but do not push. The goal is complete only when: (1) every documented public setup, notebook, reproduction, test, and LaTeX command has been run successfully from a clean copy; (2) the private scientific and mutation tests pass and demonstrate detection of the planned meaningful defects; (3) the fallback audit identifies exactly the intended evidence problems; (4) documentation links pass; (5) the public tree and reachable history contain no instructor answers; (6) the private STARTER_VERSION.md records the exact public commit; (7) both working trees are clean; and (8) the final transcript reports the commands run, their results, commit hashes in both repositories, and any limitations. If a required scientific or pedagogical choice cannot be resolved from the plan, record it in one decision queue with a recommendation and continue with all independent work. Stop and report rather than inventing evidence, silently reducing scope, publishing, or pushing. If completion remains impossible because of an external dependency or a decision only Alex can make, stop after documenting the blocker and verified repository state.
```

Useful status commands while it runs:

```text
/goal
/goal clear
```

If tool approvals would interrupt unattended work, configure Claude Code's
permission mode deliberately before starting. A goal continues across turns but
does not itself grant additional permissions.
