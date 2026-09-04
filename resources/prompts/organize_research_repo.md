# Prompt: get a research project under version control

Two different starting points, two different prompts below:

- **[Starting from scratch](#path-1-starting-from-scratch)** — a folder of files that grew locally with no version control at all, and you just want it under git, cleanly.
- **[Reorganizing an existing repository](#path-2-reorganizing-an-existing-repository)** — inherited code, a project that outgrew its structure, or something you need to hand to someone else, where a git history already exists.

Both share the same discipline: an AI agent inspects and proposes before it touches anything. **What neither prompt does is reorganize on the first pass.** You approve a plan before a single file moves. That ordering is the whole design: a large restructuring you did not review is worse than a messy repository you understand.

**Companion reading:** [`../practices/scientific_computing_workflow.md`](../practices/scientific_computing_workflow.md) (especially §3–§4 on baselining before refactoring) and [`../practices/private_code_to_public_package.md`](../practices/private_code_to_public_package.md) §1–§2 if this is heading toward a release.

---

## Path 1: starting from scratch

For a folder of scripts, notebooks, or data that has never been under version control — the very first `git init` on a project, not a restructuring.

```markdown
# Task: set up version control for this project

Folder: <absolute path>

## How we work

Look, propose, and stop before committing anything you have not shown me.

## Ground rules

- Read the files here before proposing anything — don't assume a generic
  layout without checking what's actually in the folder.
- Never delete or overwrite a file. If something looks disposable (cache
  output, a stray duplicate), flag it — don't remove it yourself.
- Show me the full `git status` and `git diff --stat` before running
  `git commit`, not after.

## What to do

1. **Look at what's here.** List every file, what each one is (script,
   notebook, data, config, generated output), and a one-line guess at
   what the project does.
2. **Propose a `.gitignore`.** Exclude anything regenerable (outputs,
   caches, environment directories) and anything that should never be
   committed (credentials, large raw data better tracked elsewhere). Do
   not exclude anything that is the only copy of real work.
3. **Propose a minimal structure**, only if the current flat folder would
   genuinely be clearer with a few subdirectories (e.g. separating a
   model from its outputs). Don't restructure for its own sake — a
   handful of files in one folder is often fine exactly as it is.
4. **Run `git init`, add the proposed `.gitignore`, and stage everything
   that should be tracked** — then stop and show me the full `git
   status` and `git diff --stat` before the first `git commit`.
5. After I approve, make the first commit with a message describing the
   project's actual starting state, not just "initial commit."

## Report back

- What's in the folder and what each piece does.
- The proposed `.gitignore`, with a reason for each exclusion.
- Whether a subdirectory structure is actually warranted, and why (or
  why not).
- The exact `git status` / `git diff --stat` you're about to commit,
  shown before you commit it.
```

**Companion reading:** the "Task 2" pattern right after this one — once the repository exists, [`../templates/project_entry_point.md`](../templates/project_entry_point.md) and a `CLAUDE.md`/`AGENTS.md` pointer file are usually the next thing worth adding, before the details of how to run the project live only in your memory.

---

## Path 2: reorganizing an existing repository

For a research repository that grew organically and already has some git history to inspect.

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

**Which path, if you're not sure:** if `git log` would show anything, you're reorganizing (Path 2), even if the history is short or messy. Path 1 is only for the moment before any commit exists.

**The inspection report is the deliverable, even if you stop there.** For an inherited project, a written account of how it actually runs is often worth more than any reorganization — and it is the thing that does not exist anywhere else. For a from-scratch setup, the file-by-file list plays the same role: it is the first time anyone has written down what is actually in the folder.

**"I cannot tell how this runs" is a finding, not a failure.** If the agent cannot determine the entry point, neither can the next student.

**Do not skip the baseline (Path 2).** The prompt asks for it in Phase 2 deliberately. Restructuring research code without a numerical baseline means you cannot prove afterward that the results are the same ones the paper reported — see [`../practices/scientific_computing_workflow.md`](../practices/scientific_computing_workflow.md) §3.

**Resist restructuring a folder that doesn't need it (Path 1).** The most common failure mode here isn't a messy repo — it's over-organizing three files into five folders before there's any reason to. Version control is the win; subdirectories can wait until there's something to separate.
