# Prompt: organize a research repository

For pointing an AI agent at a research repository that grew organically — inherited code, a project that outgrew its structure, or something you need to hand to someone else.

**What it does not do:** reorganize anything on the first pass. The agent inspects, reports what it found, and proposes a plan. You approve the plan before a single file moves. That ordering is the whole design: a large restructuring you did not review is worse than a messy repository you understand.

**Companion reading:** [`../practices/scientific_computing_workflow.md`](../practices/scientific_computing_workflow.md) (especially §3–§4 on baselining before refactoring) and [`../practices/private_code_to_public_package.md`](../practices/private_code_to_public_package.md) §1–§2 if this is heading toward a release.

---

## The prompt

```markdown
# Task: inspect this research repository and propose a reorganization

Repository: <absolute path>

## How we work

Three phases. **Stop after Phase 1 and wait for my approval.** Do not move,
rename, delete, or create any file before I approve a plan.

## Ground rules

- Phase 1 and 2 are strictly READ-ONLY. No edits, no commits, no `git` commands
  that change state (no checkout, switch, stash, reset, clean, rebase, amend).
- To inspect other branches use `git show <branch>:<path>` and `git log <branch>`.
- Never delete a file. When we get to Phase 3, move with `git mv` and record it.
- Use repo-relative paths in everything you write.
- If something is ambiguous, say so and ask. Do not resolve it plausibly.
- Report what you actually verified, separately from what you inferred.

## Phase 1 — Understand what is here (read-only)

Work out how this project actually runs, not how it looks like it should.

1. **Entry points.** Which files are meant to be executed, and in what order?
   How would a new person produce the main result? If you cannot tell, say so —
   that is itself the most important finding.
2. **Inputs and outputs.** Where does data come from, where do results go, and
   which files are generated rather than authored? Flag anything generated that
   is committed, and anything authored that looks like it is not backed up.
3. **The scientific logic.** Which code implements the method, as distinct from
   plumbing, plotting, and glue? This split matters more than any directory
   layout.
4. **Duplication.** Near-identical functions, copied cells, or two files that
   compute the same thing differently. Note which version appears to be current
   and how you can tell.
5. **State of the repository.** Branches with dates and whether each is merged;
   whether the default branch is current; uncommitted work; large or binary
   files; anything committed that looks accidental.
6. **Environment and reproducibility.** Is there a dependency specification?
   Could someone rebuild the environment? Are seeds fixed? Are there tests, and
   do they actually execute the code that matters?
7. **Risks.** What would silently break, be lost, or be irreproducible if this
   repository were handed to someone else tomorrow?

Report your findings, then **stop**.

## Phase 2 — Propose a target architecture and a migration plan

Only after I have read Phase 1.

1. **Propose a target layout**, with a one-line justification per directory.
   Do not apply a generic template — justify it from what this project does.
2. **Answer the repository-structure question explicitly:** should this stay one
   repository, or split into code and manuscript?
   - One repository is simpler: a single commit identifies the whole state,
     and code and paper evolve together.
   - Splitting makes sense when the manuscript syncs with a collaborative LaTeX
     editor, when results or data would bloat that sync, or when the code has a
     wider audience than the paper.
   - If you propose a split, you must also propose how provenance is preserved
     across it: how a figure in the paper is traced to the commit, script, and
     config that produced it. A split without that link is worse than no split.
3. **Propose a staged migration**, ordered so each stage is independently
   reviewable and revertible. Say what could break at each stage and how it
   would be detected.
4. **Say what must happen before any restructuring:** what needs to run, what
   needs pinning, and what numerical baseline should be captured so we can prove
   the reorganization did not change any result.
5. **List what you would NOT touch**, and why.

Then **stop** for approval.

## Phase 3 — Execute, one approved stage at a time

- One stage per commit, with the verification result in the commit message.
- No behavioral changes during a structural move. If a move requires a code
  change to work, stop and tell me.
- After each stage, confirm the baseline is unchanged and report it.

## Report back

- **Phase 1:** how the project runs; entry points; the scientific-logic /
  infrastructure split; duplication; repository state; reproducibility; risks —
  each marked `verified` or `inferred`.
- **Phase 2:** proposed layout; the one-repo-vs-split recommendation with
  reasoning; the staged plan; prerequisites; what you would leave alone.
- Anything you could not determine, listed plainly rather than guessed.
```

---

## Notes on using it

**The Phase 1 report is the deliverable, even if you stop there.** For an inherited project, a written account of how it actually runs is often worth more than any reorganization — and it is the thing that does not exist anywhere else.

**"I cannot tell how this runs" is a finding, not a failure.** If the agent cannot determine the entry point, neither can the next student.

**Do not skip the baseline.** The prompt asks for it in Phase 2 deliberately. Restructuring research code without a numerical baseline means you cannot prove afterward that the results are the same ones the paper reported — see [`../practices/scientific_computing_workflow.md`](../practices/scientific_computing_workflow.md) §3.
