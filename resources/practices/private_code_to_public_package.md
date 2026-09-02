# From Private Research Code to a Public Package

**What this is.** How to turn working research code into something other people can install, understand, and trust — without breaking the results it already produced, and without leaking data that can't be public.

**When to reach for it.** When a paper is going out and the code should go with it; when a tool you built for yourself turns out to be useful to someone else; when you inherit code that works and needs to outlive the person who wrote it.

**Prerequisite.** `scientific_computing_workflow.md` §3–§4. Do not start extracting until the code runs, the environment is pinned, and a numerical baseline exists. Everything here assumes you can prove the package still computes what the original did.

**How to read it.** Sections are numbered and stable for citing in a prompt. §1 is the decision that shapes all the others.

---

## 1. Decide what the package is: split by audience

The first question is not "what do I clean up" but **"who is this for, and what do they need?"** Answer it explicitly, because it determines what ships and what stays behind.

A useful split for paper-associated code:

- **The package** — the method, plus what a general user needs to apply it to their own problem.
- **The research archive** — the reproduction workflow for *your* paper: parameter sweeps, cluster submission scripts, cross-method benchmarking, the exact figure scripts.

These have different audiences and different lifetimes. Someone who wants to use your method does not need your HPC submission scripts; someone reproducing your paper needs exactly those.

**Split by audience, not by code quality.** The temptation is to ship the parts you're proud of and hide the rest. That produces a package missing things users need and an archive missing things reproducers need. Ask "who calls this?" for each module, not "is this good?"

Write the split down in the README, so users know what they're getting:

> This package is the algorithm plus what a general user needs. The paper's full reproduction workflow — parameter sweeps, cluster submission, cross-method benchmarking, and all figures — is not part of the installed package; it lives in the archived research repository at [URL, commit or DOI].

When you cut something, record what you cut and what depended on it. A commit body listing every removed function, every place kept code had to be severed from removed code, and the dependencies that dropped out as a result is worth writing — it is the only reviewable record of a large deletion.

## 2. Isolate what cannot be public

Most research code has something that can't ship: institutional data, sponsor-restricted parameters, human-subjects data, an unpublished collaborator's dataset, or just names and email addresses.

**The move is to turn that content into inputs, not to scrub it out of code.** Hardcoded constants become configuration files; embedded data becomes a data file the code reads. Then publishing means shipping *synthetic instances of the same input files* — no scrubbing pass, no risk that a stray identifier survives in a default somewhere.

Concretely:

- Extract to input files: a configuration file for parameters, a data file for the dataset, a catalog file for anything institution-specific.
- Commit **synthetic examples** with obviously placeholder content — `Prof. A`, `Site 1`, `Building ABC` — that are complete enough to run end to end.
- Verify with a search, not by memory: grep the whole repository for institution names, personal names, internal hostnames, and email addresses. A clean result should be a handful of hits, all in prose attribution.
- Describe the real configuration in prose as *motivation* and encode it as a *parameter*. "Our two buildings are about a seven-minute walk apart" belongs in the README; `travel_time: 7` belongs in a config file.

**Then keep using the real data privately, as a dogfooding harness.** Migrating your actual dataset onto the public API surfaces awkwardness that synthetic examples hide — functions that return nothing useful, signatures nobody can remember, error messages that don't say what to do. Those fixes are the highest-value changes in the whole process.

## 3. Extract: structure, naming, and API

- **Use a `src/` layout and a `pyproject.toml`** from the start. It forces you to actually install the package to test it, which catches the class of bug where everything works only from the repository root.
- **Separate the heavy dependency.** If your method needs a large or licensed library, inject it rather than importing it at module load. A package whose top-level import pulls in a deep learning stack, a commercial solver, or another language runtime is a package most people will not try. Verify in a clean environment that a plain `import yourpackage` works with only the core dependencies.
- **Declare optional extras** — `[gpu]`, `[analysis]`, `[dev]` — and put a comment on every non-obvious pin explaining *why* it is pinned. A pinned version with no reason rots the moment someone needs to upgrade something.
- **Fix the names while you have permission to.** Research code accumulates `my_kernel_fxn.py`, `DataFrame2`, `retrain_GP`, misspellings that got frozen by use. Renaming is cheap during extraction and expensive after release. Do renames as their own commits, one category at a time, each gated by the baseline.
- **Generalize by adapter, not by rewrite.** When you extend a verified pipeline to a second case, add a thin adapter that maps the new case onto the existing verified path. Rewriting the core to be general breaks the thing you proved correct.

## 4. Don't break existing users: shims and deprecation

Your first users are you and your group, with notebooks and scripts that import the old names.

- **Leave a compatibility shim.** A short module that re-exports from the new location keeps existing code working during migration and removes the excuse to postpone the move. Then add a test asserting the shim re-exports the *same objects* — identity, not equality — so the two paths cannot silently diverge.
- **Deprecate loudly and specifically.** A warning that names the exact replacement call is actionable; "this is deprecated" is not. Update the warning text if the recommended replacement changes.
- **Keep a changelog** with a stable format, and record what a release *fixed*, not just what it added.

## 5. Tests that make a package trustworthy

The goal shifts here. During refactoring, tests protect *you* from changing behavior (`scientific_computing_workflow.md` §4). In a released package, they tell *other people* the thing works.

- **Rewrite smoke checks into behavior assertions.** "It ran without raising" tells a user nothing. Assert the returned value, the shape, the invariant, the error raised on bad input.
- **Separate fast from slow** with test markers, so the fast suite gates every change and the expensive one runs on a schedule. A suite nobody runs protects nothing.
- **Make the fast suite runnable without the heavy dependency**, using a test double — while keeping the real integration path covered by the slow suite. Never fake the component actually under test.
- **Cover paths that need something you don't have** (a commercial solver, a cluster) with doubles rather than skipping them silently.
- **Turn uncovered branches into named work items** rather than a percentage to raise, and **set the coverage gate at the level you achieved.** A gate below your current level protects nothing and permits a silent slide.
- **Validate inputs before the expensive step**, with errors that name the fix. "Constraints are mutually infeasible; see `set_bounds()`" saves a user from a solver traceback they cannot interpret.

## 6. Documentation that can't go stale

- **A quickstart that a stranger can complete**, including installation, in under ten minutes, using only committed example files.
- **Embed example files by reference**, not by pasting their contents — a documentation directive that includes the actual file keeps the docs correct automatically. Copy-pasted examples drift within one release.
- **Tie documented results to a test.** If your docs contain a table of computed outputs, have a test parse it and assert against a live run. This is the single most effective defense against generated documentation quietly becoming wrong.
- **Map the paper to the code.** A page connecting each equation in the paper to the module implementing it is worth more to a serious user than any amount of API reference.
- **Record where the code differs from the paper.** Bug fixes, improved numerics, and corrections made after publication belong in a short "differences from the published version" page. If a published claim turned out to rest on a bug, say so there, plainly.

## 7. Release engineering

- **Ship the skeleton early.** Getting a minimal version installable — even a placeholder that reserves the name — forces packaging metadata to be right on day one and makes every later change an increment rather than a big-bang packaging effort at the worst possible time.
- **Tag-driven releases.** Pushing a version tag triggers the pipeline; the version in the package metadata matches the tag exactly, with no manual step to forget.
- **Two-stage publish with a real install gate:** build → publish to a test index → **install that exact version from the test index in a clean environment and import it** → publish the *same artifact* to the real index. The install gate catches metadata and dependency errors that no local check will.
- **Use short-lived credentials.** Trusted publishing via OIDC means no long-lived API token in your repository secrets for a student to leak or an ex-member to still hold.
- **Write down the failure modes.** A release document with a checklist, the one-time setup steps, and a "common failures" table mapping each error message to its fix is the highest-value page in the repository the second time you release. Add a "notes for future you" section for the traps specific to your project — for example, a package name on the index that differs from the import name.
- **Post-mortem the process, not just the bug.** When a release ships a defect, record *why the release checks missed it* and amend the checklist so they cannot miss it again.

## 8. What stays human

An agent can prepare an entire release and should not execute it. Keep these on your side of the line:

- publishing to a package index; registering a trusted publisher
- creating and pushing version tags
- anything requiring credentials or an account
- the decision that a version is ready

State this in the task, and have the agent write the steps you will run rather than running them (`working_with_ai_agents.md` §6). A good release session ends with everything staged, documented, and untriggered.

## 9. Link the package and the paper, in both directions

This is the most commonly missed step, and the cheapest to fix.

**Package → paper.** Put the DOI in the project metadata, and include a reproduction guide: a table mapping each figure to the script, the input data, and the expected reference values.

**Paper → package.** The manuscript must name the repository and a *specific version* — a commit hash, a tag, or ideally an archival DOI. This is the direction that gets skipped, and skipping it means a reader holding your paper has no path to your code even when the code is public and excellent.

A data-availability statement reading "available upon request" while a public, installable, figure-reproducing package exists is a failure of provenance, not of generosity. Write the real link.

**One-line test:** hand someone only the PDF. Can they find the code? Hand someone only the repository. Can they find the paper? Both answers should be yes.

## 10. Archive the research side properly

The split in §1 only works if the archive is real.

- **A private repository is not an archive.** Neither is a shared-drive folder or an unpushed branch. If the reproduction workflow lives somewhere that can be reorganized, lost, or lose an access grant, the provenance chain rests on its weakest link.
- **Tag the state that produced the paper**, and deposit it somewhere with a DOI and a persistence guarantee.
- **Name the archive in the package**, and the package in the archive. "It lives in the archived research repository" without a URL is not a pointer.
- **Keep the process record.** When you strip development scaffolding before release — phase labels, planning notes, internal handoff files — it is right to remove them from user-facing docs and wrong to delete them outright. That material is the most reusable thing you produced for the *next* project. Move it into the archive rather than out of history.

---

## Checklist

**Before extracting**

- [ ] The code runs, the environment is pinned, and a numerical baseline exists
- [ ] The package/archive split is decided and written in the README
- [ ] Non-public content is isolated into input files, with synthetic examples committed
- [ ] A repository-wide search for names, hosts, and addresses comes back clean

**Before the first release**

- [ ] `src/` layout, `pyproject.toml`, extras declared, non-obvious pins explained
- [ ] Plain import works in a clean environment without the heavy dependencies
- [ ] Fast suite runs without optional dependencies; slow paths covered separately
- [ ] Smoke checks rewritten as behavior assertions
- [ ] Quickstart completable by a stranger in ten minutes from committed files
- [ ] Compatibility shims in place for the old import paths, with a test pinning them

**Before announcing it**

- [ ] Release pipeline includes a real install-and-import gate from a test index
- [ ] No long-lived credentials in repository secrets
- [ ] Failure modes and one-time setup written down
- [ ] Package names the paper; **paper names the package, with a version**
- [ ] The research archive exists, is tagged, and has a persistent identifier
- [ ] Development scaffolding was moved to the archive, not deleted

## Anti-patterns

- **Extracting before baselining.** You can no longer prove the package computes what the paper reported.
- **Splitting by code quality.** Ships an incomplete package and an incomplete archive.
- **Scrubbing instead of parameterizing.** One missed default and private content is public.
- **A top-level import that pulls in everything.** The most common reason a good package goes untried.
- **The modular-looking monolith.** Two-line re-export modules around one enormous file — the layout says modular, the code isn't.
- **A coverage gate below what you achieved.** Permits a silent slide with CI green.
- **Publishing straight to the real index.** No install gate, so metadata errors ship.
- **"Available upon request."** With a public repository sitting right there.
- **"The archived research repository."** Unnamed, unlinked, and in one case not actually archived.
- **Deleting the process record at release.** Removing it from user-facing docs is right; erasing it is a loss.

## Using this file with an AI assistant

**As a planning task (do this first):**

> Read `practices/private_code_to_public_package.md`. Inspect this repository and propose a package/archive split per §1: for each module, say who calls it and whether it belongs in the package, the archive, or both, with your reasoning. Identify everything that cannot be public per §2 and propose how to parameterize it. Do not move or change anything — produce a plan for me to approve, and flag anything you are unsure about rather than deciding it.

**As an extraction task (after the plan is approved):**

> Following the approved plan and `practices/private_code_to_public_package.md` §3–§4: create the `src/` layout, move the agreed modules, and leave compatibility shims for every old import path with a test asserting object identity. Make no behavioral changes — the numerical baseline must be byte-identical after this step, and report the baseline result in the commit message. Do not rename anything yet; renames are a separate gated step.

**As a pre-release audit:**

> Audit this repository against `practices/private_code_to_public_package.md` §7, §9, and §10. Report: whether a clean-environment import works with core dependencies only; whether the release pipeline includes an install gate from a test index; whether any long-lived credential is referenced; whether the package names the paper and the paper names the package with a specific version; and whether the research archive is named, tagged, and persistently identified. One row per check, with `pass` / `fail` / `cannot determine` and the evidence. Change nothing.
