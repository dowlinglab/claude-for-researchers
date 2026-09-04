# Scientific Computing Workflow

**What this is.** How to take research code from exploratory scripts and notebooks to something you, a collaborator, or a reviewer can rerun and trust — and how to verify it at each stage without drowning in tests you don't need yet.

**When to reach for it.** When a result is about to matter: it's going in a paper, someone else needs to run it, or you're about to restructure code that currently works.

**How to read it.** Sections are numbered and stable, so you can point an agent at one (`follow §4`). Start with §1 — it tells you which of the rest applies to you right now.

---

## 1. Match the verification to the phase

The most common bad advice in AI-assisted development is "write more tests." For research code that is wrong, because the right instrument depends on where you are.

| Phase | What actually verifies | What gets in the way |
|---|---|---|
| **Discovery** — the question is still moving | Fixed seeds; the result written down with its configuration; a physical-plausibility check; predicting the answer before you look | Pinned-value tests. Every legitimate change breaks them, so you learn to ignore failures — which is worse than having none |
| **Consolidation** — a result is going to be reused or believed | Characterize current behavior: capture a numerical baseline. This is a description, not yet a correctness claim | Asserting the baseline is *right*. It isn't — it's what the code does today |
| **Refactor / extension** — changing code that works | That baseline as a gate; cross-method agreement; invariants | Adding new science mid-refactor (§4) |
| **Publication / handoff** — someone else must rerun it | Invariants, reproduction scripts, environment pinning, run manifests | Brittle full-assignment assertions that break on any harmless change |

Two rules follow, and both are load-bearing:

- **A green test suite is evidence only about the code it executes.** A real case: a suite covering 24 of 29 analysis directories reported all-green while the four changes that mattered landed in the five directories it never ran. "All tests pass" was true and carried no information.
- **Tests are for code you intend not to change.** During discovery you are *trying* to change behavior. Instrument instead: record inputs and outputs, fix seeds, and check that results are physically sensible.

## 2. Prototype in notebooks; promote what matures

Notebooks are excellent for exploration and poor as the long-term home of scientific logic — hidden state, execution order that only you know, cells duplicated and then edited differently, hard-coded paths. The point is not that notebooks are bad. It is **prototype in a notebook, promote mature logic into modules.**

Promote when any of these becomes true:

- you have copied a cell for the third time
- someone else needs to run it
- a number from it is going into a paper
- it needs to run overnight, or on a cluster, or in a loop over configurations

Promotion, concretely: extract functions; separate calculation from plotting (§8); replace hard-coded constants with a configuration file; give it an entry point that runs top to bottom without a human. Keep a thin compatibility shim if that lets existing notebooks keep working while you migrate — a two-line module that re-exports the new location costs nothing and removes the excuse to delay.

The notebook can come back at the end as a *deliverable* — a tutorial that installs the package and demonstrates it — which is a very different artifact from the notebook that was the source of truth.

## 3. Before you refactor: run it, pin it, baseline it

Three steps, in this order, before you change any structure. Skipping them is why refactors of scientific code go wrong invisibly.

**Run it first.** Do not restructure code you have not watched execute. Getting inherited code to run unchanged routinely surfaces real defects, and it tells you which parts are actually exercised.

**Pin the environment, and record why.** Write down the working versions and the reason each one is pinned. Scientific stacks break in ways that are not obvious: a library pinned to a version that predates a breaking change in *its* dependency will fail to import if you install it naively, because the dependency resolves forward. A pinned list with no reasons rots as soon as someone needs to upgrade one thing. This step often deserves its own commit, containing only the environment file and its notes.

**Capture a numerical baseline on the unrefactored code.** This is the highest-value single step in this document. Design it deliberately:

- **Store pure numbers.** A baseline of raw values survives class, function, and column renames; a baseline of formatted output does not.
- **Committed program output works** when you have no unit tests. Running each driver and storing its stdout is a legitimate regression net for a research pipeline, and exact line-matching is usually achievable.
- **Capture enough detail to localize a change** — per-iteration trajectories, not just the final scalar. A baseline that only stores the final answer tells you *that* something moved, never *where*.
- **Establish determinism by measurement, not assumption.** Capture twice, diff the two captures. Where output is genuinely nondeterministic, that is a finding about the code — record it, and exclude that driver deliberately rather than loosening the tolerance until it passes.

## 4. Freeze the science, move the code, measure the delta

When refactoring, change exactly one thing at a time — and "the science" and "the code" are two things.

> Holding the science fixed while the code moves turns "did we break anything?" from an inspection into a **controlled comparison.**

That has a sharp consequence people resist: **bugs you find mid-refactor get queued, not fixed.** Fixing a real bug during a refactor introduces a second variable and makes every delta ambiguous. Write it down, finish the refactor, then fix it as its own change with its own justified baseline update.

The sequence:

1. **Prove the refactor is neutral.** Re-run the old analysis on the old inputs under the new code and show the baseline is unchanged. Do this *before* touching any science.
2. **Then change the science.** Now the baseline is *expected* to move — and it must move for a stated reason, with the new values checked for the right reason (closer agreement with an independent reference, not merely different).
3. **Account for every delta.** At the end, observed changes should equal the sum of documented, intended changes. Anything left over is a refactoring error, not a rounding artifact.

Supporting habits:

- **One semantic change per commit**, with the gate result in the message: *"tests 184/184, baseline 9/9 byte-identical."*
- **Regenerating a baseline requires a documented reason in the same commit.** Regenerating one to make a failing test pass defeats the entire mechanism.
- **Add coverage before deleting.** If you are about to remove code, first make sure something would notice if the removal broke a path you meant to keep.
- **Archive rather than delete.** Move superseded code to `legacy/` with a note. Deleting the script that produced a number leaves the claim without its working.
- **A phase plan discovers scope as it runs — budget for that, don't fight it.** A ten-phase plan can reasonably become thirteen: a from-scratch reproduction turns up a real bug, the bug motivates a hardening pass, the hardening pass turns up enough drift to justify a full polish pass. That is different from scope creep as long as each addition is proposed only *after* the previous one finished — a response to what execution actually revealed, not work queued speculatively up front. Track the plan as a dated, append-only log (new phases get new entries, not edits to old ones) so the gap between "planned" and "executed" stays visible instead of getting silently absorbed into a renumbered plan that reads as if it were right the first time.

## 5. Tests for research code: invariants, not magic numbers

Pinned values are fine as a refactor gate and poor as a permanent test, because they break whenever the science legitimately changes. Prefer assertions that stay true across a change of parameters, data, or ground truth:

- **Round-trips and conservation** — transform and invert; check mass, energy, or probability sums.
- **Limiting cases with a derived tolerance.** Reduce a general implementation to a case with a known closed-form answer. Derive the tolerance from the perturbation you introduced rather than guessing it, and assert with margin.
- **Cross-method agreement.** Two independent implementations of the same quantity should agree; where one is a reference you cannot run, port it faithfully and check the two ports against each other.
- **Textbook values.** Reproducing a classic result exactly is a physics check no unit test gives you.
- **Inequalities and orderings** that encode the paper's actual claim (`assert conditioning_a > 20 * conditioning_b`) rather than the specific magnitudes.
- **Documentation as a test.** If your docs contain a table of computed results, have a test parse that table and assert it against a live computation. Documentation that can silently go stale is the default failure mode of generated docs.

Practical notes:

- **Use test doubles for expensive or licensed dependencies** so the fast suite runs anywhere — but never fake the component actually under test.
- **Avoid over-specified assertions.** Check the objective value, not the entire solution vector; solvers legitimately return different optima.
- **On coverage:** treat uncovered branches as named work items rather than a percentage to raise. And set the gate at what you achieved — a target below your current level protects nothing.

## 6. Every instrument has blind spots

Verification tools give false confidence when their limits are unstated.

- **Make each instrument declare what it cannot see**, in the instrument. A comparison that checks plotted data but not rendered pixels is blind to styling; one that checks pixels is blind to whether the underlying numbers moved. Report results as "verified for everything this instrument can see, which excludes X," never as "verified."
- **Two instruments disagreeing about one fact is the signal that matters.** It is worth more attention than either instrument agreeing with itself.
- **Predict the answer before you read the instrument.** Writing down what you expect, first, is what catches a confidently wrong reading. This is cheap and it works.
- **Beware numbers that read as success because the measured thing did not happen.** A suite that finishes suspiciously fast may have been refused a lock and run nothing; a comparison may default to "identical" on a shape mismatch. Check that the work occurred before believing the result.
- **Do not trust reported values from failed runs.** A converged-looking objective on a run that terminated badly is not evidence; check the constraint violation at exit.

## 7. Run identity and provenance

Every result that reaches a manuscript should be traceable to the exact thing that produced it.

**Record what identifies a run:** the code commit, the configuration (hashed or copied verbatim), hashes of the input files, random seeds, versions of the solver and key libraries, and the exact command. A run record is a dated document — write it once and never edit it.

**Validate provenance at runtime and fail fast.** If a run depends on a specific build of a dependency, check at startup that the imported build has what you need and raise before doing any work. Silent version drift mid-run produces results that look fine and are not; a check that fails in the first second is much cheaper than discovering it two days later.

**Quarantine invalid runs; don't delete them.** Rename the directory with the reason encoded — `..._invalid_seed_collision`, `..._invalid_truncated` — so the record shows what was excluded and why.

**Keep one results manifest as the single source of truth** for every number that reaches prose. When someone asks where a number came from, exactly one file should be the answer, and figure directories should record the configuration that produced them (§8, and the `results_manifest.md` template).

## 8. Structure that survives

- **Separate compute from plotting.** Restyling a figure should never trigger a recomputation, and regenerating data should never require opening a plotting script. This one split does more for iteration speed than any other.
- **Configuration as data, from one place.** Parameters live in a config file or a single registry module, not scattered as constants. When a round of tuning settles a question, freeze the outcome into a *named* configuration with a short decision record of what was ruled out and why — otherwise it's just settings someone found once.
- **Name directories by topic, not by step number.** Step numbering ages badly as the structure evolves. (Numbering is fine for append-only records like dated prompts or logs, where the order is the point.)
- **Keep one definition of each thing.** Two modules defining the same function under different names — both individually justified when written — is how a codebase becomes quietly inconsistent. When you find a fork, resolve it and record the resolution.

## 9. Working with an agent on numerical code

Everything in `working_with_ai_agents.md` applies. These are the additions specific to computational work:

- **State the budget and the stop conditions** for long-running work — hours, concurrent processes, what to do when the budget expires — and add the anti-shortcut clause: *do not silently reduce the number of runs or iterations to fit the window; report the last completed stage.*
- **Do not edit the repository while a measurement is running.** The suite is an instrument; changing the tree mid-run invalidates the measurement, and the failure is confusing rather than obvious.
- **Record negative results and forbid repeats.** Write down which parameter sweeps, solver options, and formulations were tried and rejected, and instruct the agent not to re-run them. Otherwise settled questions get re-litigated every session.
- **Reduce an upstream bug to a minimal example with a known answer** before reporting it. A self-contained reproduction with an analytic result is checkable without solver tolerances and can be handed to anyone.
- **An agent's numerical claim needs the same verification as your own** — more, if it is surprising. A result that contradicts your physical intuition deserves a second, independent derivation before it changes what you believe.

## 10. Tool-specific notes

> ⚠️ **This section dates fastest** and describes tools as of September 2026. The practices above are meant to outlive it.

Useful mechanisms today: test markers to separate fast from slow suites so the fast one can gate every change; continuous integration with a dependency-light job plus one fully-pinned job; coverage reporting wired to the pinned job only. If your work depends on a licensed solver, structure tests so the suite is meaningful without it and the licensed paths are covered by doubles or a separate job.

---

## Checklist

**Before restructuring working code**

- [ ] The code runs, unchanged, and you have watched it
- [ ] The environment is pinned, with a reason recorded for each non-obvious pin
- [ ] A numerical baseline is captured from the *unrefactored* code and committed
- [ ] Determinism was measured (captured twice and diffed), not assumed

**During the refactor**

- [ ] The science is frozen; bugs found along the way are queued, not fixed
- [ ] The refactor was proven neutral before any science changed
- [ ] Each commit makes one semantic change and carries its gate result
- [ ] Every baseline change has a documented reason in the same commit

**Before a result leaves your machine**

- [ ] A run record captures commit, config, input hashes, seeds, versions, and the command
- [ ] One manifest is the single source of truth for numbers in the prose
- [ ] Figures record the configuration that produced them
- [ ] Invalid or superseded runs are quarantined with the reason in the name

## Anti-patterns

- **Coverage theater.** A high percentage over code that isn't where the risk lives.
- **Refactoring and fixing at once.** Now no delta can be attributed to anything.
- **Loosening a tolerance until it passes.** Nondeterminism is a finding, not a fixture problem.
- **Regenerating the baseline to make the suite green.** This deletes the only thing protecting you.
- **The final-scalar baseline.** It tells you something moved, never where.
- **Pinned-value tests during discovery.** They break constantly, so you stop reading failures.
- **Believing a fast, clean run.** Check that the work actually happened.
- **Deleting the script that produced a number.** The claim survives; its working doesn't.

## Using this file with an AI assistant

**As standing project context:**

> Follow `practices/scientific_computing_workflow.md` for all code work in this repository, especially §4 (freeze the science, move the code) and §7 (run identity).

**Before a refactor:**

> Read `practices/scientific_computing_workflow.md` §3. Do not change any code yet. Get the existing analysis running unchanged, record the working environment with a reason for each non-obvious pin, and propose a numerical baseline: which drivers to capture, which values, and how you would detect a behavior change after a rename. Report the plan for approval before capturing anything.

**As an audit:**

> Audit this repository against `practices/scientific_computing_workflow.md` §5–§7. For each verification mechanism you find, state what it cannot see. Identify every number in the manuscript prose that cannot be traced to a committed results file, and list runs whose provenance (commit, config, seeds, versions) is not recorded. Report as a table with a `verified / partial / cannot trace` column; change nothing.
