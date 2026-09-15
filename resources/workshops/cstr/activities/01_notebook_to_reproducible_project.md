# Activity 1 — From a notebook to a reproducible project

**Time:** 1 hour 45 minutes
**You need:** a GitHub account, Git, conda (or mamba), and an AI coding agent
(Claude Code, Codex, Cursor, or similar) you can run against a local directory.

## Objectives

By the end you will have a private, versioned repository containing:

- a documented environment that someone else can build;
- a **baseline** — evidence of what the code computed before you changed it;
- reusable model functions extracted out of the notebook;
- one command that regenerates every result without opening the notebook;
- tests that fail when the science changes, not only when the code moves;
- a handoff document recording the verified state.

The lesson underneath all of it: **capture evidence before restructuring code.**
A refactor is only safe if you can prove afterwards that the answers did not
move. Most people acquire that habit by losing a result once.

## The science, in one paragraph

A jacketed CSTR runs the irreversible exothermic reaction `A -> B` with
first-order Arrhenius kinetics. At steady state, a material balance and an
energy balance must hold simultaneously. Because the heat generated rises
exponentially with temperature while the heat removed rises linearly, the two
balances can be satisfied at more than one temperature for the same operating
condition. The notebook finds those steady states and sweeps the coolant
temperature. Full statement of the equations, assumptions, units, and sign
conventions is in the first cell of the notebook.

---

## Phase 0 — Setup (20 min)

### Create your private repository

Copy the starter into a **new private GitHub repository** of your own. Do not
fork the public one and do not work directly in it.

```bash
# from wherever you keep projects
cp -R /path/to/claude-for-researchers/resources/workshops/cstr ~/cstr-project
cd ~/cstr-project
git init
git add .
git commit -m "Start from the CSTR workshop starter"
```

Then create an empty **private** repository on GitHub and push to it:

```bash
git remote add origin git@github.com:YOUR-USERNAME/cstr-project.git
git branch -M main
git push -u origin main
```

If `git push` fails on authentication, that is the first thing to fix — see
[Common problems](#common-problems).

### Work on a branch

```bash
git switch -c workshop1
```

Everything below happens on this branch. You will review the whole thing as one
diff at the end, which is much easier when `main` is untouched.

### Build the environment

```bash
conda env create -f environment.yml
conda activate cstr-workshop
```

This installs the project itself in editable mode, so `import cstr_workshop`
works from anywhere once the environment is active.

> **Gate 0.** All three commands succeed:
> ```bash
> python -c "import numpy, scipy, pandas, matplotlib, yaml, cstr_workshop; print('ok')"
> pytest tests
> python scripts/run_notebook.py --check
> ```
> The third takes a few seconds and prints the working directory it used.
> **Do not continue until all three pass.** Everything after this point assumes
> a working environment, and debugging science on top of a broken environment
> wastes the rest of the session.

---

## Phase 1 — Agent instructions (10 min)

Point your agent at the repository and ask it to write project instructions.

> **Prompt.** Inspect this repository before changing anything. Read
> `notebooks/cstr_exploration.ipynb`, `data/reactor_parameters.yml`,
> `pyproject.toml`, `environment.yml`, and `tests/`. Then tell me, in your own
> words: what scientific problem this project solves, what the units and sign
> conventions are, and what is most likely to be gotten wrong by someone
> editing it. Do not edit any file yet.

Read its answer critically. If it describes the sign convention on the heat of
reaction wrongly, or claims the notebook establishes stability, you have learned
something useful about what it will do unsupervised.

Then:

> **Prompt.** Based on what you found, draft `CLAUDE.md` (or `AGENTS.md`) for
> this repository. Include only things a competent new collaborator would
> plausibly get wrong without being told. No generic software-engineering
> advice. Aim for under one page.

`AGENTS.md.example` and `CLAUDE.md.example` in this directory are worked
examples — compare yours against one *after* you have drafted your own.

**Now cut it.** Delete every line that is true of any Python project. What is
left is the file that actually changes the agent's behavior.

> **Gate 1.** `CLAUDE.md` or `AGENTS.md` is committed, is under roughly one
> page, and every line in it is specific to this project.

```bash
git add CLAUDE.md
git commit -m "Add project instructions for AI agents"
```

---

## Phase 2 — Run the notebook and capture the baseline (15 min)

### Run it untouched

```bash
jupyter lab      # start from the PROJECT ROOT, not from notebooks/
```

Open `notebooks/cstr_exploration.ipynb`, restart the kernel, and run all cells.
It takes a few seconds.

Read the output rather than skimming it. Three things are worth noticing:

1. The first `fsolve` call converges to a perfectly good steady state — and
   there are two more that it never finds.
2. The number of steady states changes across the sweep.
3. The final markdown cell is careful about what the result does *not* show.
   Check whether you agree with it.

### Capture the baseline

This is the part people skip.

Create `results/baseline.json` recording what the notebook just computed. It
must contain enough that someone could tell, a year from now, whether a new
result is the same result:

- every reactor parameter, with units;
- the nominal steady states: `CA`, conversion, `T`, and residual norm for each;
- the sweep definition — parameter, start, stop, step;
- the number of conditions, the number of rows, and the range over which three
  steady states exist;
- solver settings: residual tolerance, the distinct-root temperature tolerance,
  the initial-guess strategy;
- software versions — Python, numpy, scipy, pandas, matplotlib;
- the exact command that produced it.

The notebook already wrote `results/steady_states.csv` and
`results/steady_state_locus.png`. Keep them.

A reasonable prompt:

> **Prompt.** Read `notebooks/cstr_exploration.ipynb` and the files in
> `results/`. Write `results/baseline.json` capturing the nominal steady states,
> the sweep definition and summary, solver tolerances, all reactor parameters
> with units, the installed versions of Python and the scientific stack, and the
> command that produced these results. Take every number from the notebook's
> actual output or from `results/steady_states.csv` — do not recompute anything
> and do not round.

Then check it yourself against the notebook output. An agent that recomputes
instead of reading has produced a baseline of its own code, which is worthless
for this purpose.

> **Gate 2.** `results/baseline.json` exists, its numbers match the notebook's
> printed output, and it is committed. **The baseline must be committed before
> you change a single line of model code.**

```bash
git add -f results/baseline.json results/steady_states.csv
git commit -m "Capture baseline results from the untouched notebook"
```

(`-f` because `results/` is git-ignored by default. Committing the baseline is
a deliberate exception: it is evidence, not output.)

---

## Phase 3 — Extract the model (30 min)

Move the science out of the notebook into `src/cstr_workshop/`.

There is **no required module layout.** A reasonable one:

| Module | Contents |
|---|---|
| `model.py` | parameter loading and validation, rate constant, steady-state residuals |
| `solve.py` | solving from one guess; finding distinct steady states from many |
| `sweep.py` | sweeping a parameter and collecting every steady state found |
| `plotting.py` | the figure, drawn from a dataframe |

What matters is that the functions are importable, take parameters as arguments
rather than reading globals, and behave identically to the notebook.

> **Prompt.** Extract the model, solver, sweep, and plotting code from
> `notebooks/cstr_exploration.ipynb` into modules under `src/cstr_workshop/`.
> Requirements: no global state — every function takes the parameters it needs;
> parameters load from `data/reactor_parameters.yml`; the distinct-root
> tolerance and residual tolerance are named arguments with documented defaults,
> not literals buried in a loop; docstrings state units and sign conventions.
> Do not change any numerical value, tolerance, or initial-guess strategy. Show
> me the proposed module layout and function signatures before writing files.

Three things to insist on, because an agent will otherwise quietly drop them:

- **The multi-guess strategy survives.** It is tempting to "simplify" the root
  search to a single `fsolve` call. That deletes the entire finding.
- **The tolerances keep their values.** `1e-2` K for distinct roots, `1e-6` for
  the residual norm.
- **Parameters come from the YAML file.** Retyped constants in two places drift.

Add input validation while you are here — negative flow rate, zero volume, a
positive enthalpy of reaction, a temperature that is obviously Celsius. These
are cheap and they catch real mistakes.

> **Gate 3.** `python -c "from cstr_workshop import ...; print('ok')"` imports
> your functions, and the notebook still runs:
> `python scripts/run_notebook.py --check`.

---

## Phase 4 — One command, and tests (15 min)

### `scripts/reproduce.py`

Write the single documented command that regenerates everything without the
notebook. Requirements are in [`../scripts/README.md`](../scripts/README.md).

```bash
python scripts/reproduce.py
```

> **Gate 4a — the one that matters.** The regenerated results match the baseline
> you committed in Phase 2, within a tolerance you state explicitly.
>
> Compare them. Actually compare them — open both files, or write the four-line
> script that does it. "It looks right" is not the gate.
>
> If they differ: the refactor changed the science. Find out why before going
> further. Do **not** regenerate the baseline to make the comparison pass. That
> converts your evidence into a record of your bug.

### Tests

Add to `tests/`:

| Test | Why |
|---|---|
| Residuals are ~zero at each reported steady state | The solutions actually solve the equations |
| Physical bounds: `0 <= CA <= CAf`, `0 <= X <= 1`, `T` within the no-reaction and full-conversion limits | Catches sign and unit errors that still converge |
| Nominal values match the baseline within tolerance | The regression test proper |
| Three distinct steady states at `Tc = 300 K` | The finding itself |
| A single initial guess returns fewer than three | Documents the failure mode the project exists to avoid |
| Invalid inputs raise | Negative `q`, zero `V`, positive `dHr`, Celsius-looking temperatures |

Use *absolute* tolerances you can defend. `pytest.approx(x)` defaults to a
relative tolerance of 1e-6, which is far tighter than anything you should be
asserting about a cross-platform floating-point result — and tight enough to
fail on a different BLAS build for no scientific reason.

> **Gate 4b.** `pytest tests` passes.
>
> Then check the tests are worth anything: **temporarily** flip the sign of the
> heat-release term in your model, rerun, and confirm something fails. Undo it.
> A test suite that passes with a reversed heat of reaction is testing the
> plumbing, not the science.
>
> ```bash
> git diff              # confirm you actually undid it
> ```

---

## Phase 5 — Review and hand off (15 min)

### Read the diff

```bash
git diff main...workshop1
```

Read it. All of it. This is the step that catches the parameter an agent
"tidied", the tolerance that became `1e-8`, and the docstring that now claims
something the code does not do.

> **Prompt.** Summarize what changed in this branch relative to `main`, grouped
> by intent. Flag anything that changes a numerical value, a tolerance, an
> initial-guess strategy, or a physical assumption. List those separately and
> exactly.

Verify its summary against the diff yourself. That is the whole point.

### Rerun every gate

```bash
pytest tests
python scripts/reproduce.py
python scripts/run_notebook.py --check
```

### Commit and hand off

```bash
git add -A
git commit -m "Extract reactor model into modules with reproduction script and tests"
```

Fill in [`../docs/handoff.md`](../docs/handoff.md) with the branch, the commit
hash, which gates you actually ran and when, the decisions you made and why, and
what is still open.

> **Gate 5.** The working tree is clean, `docs/handoff.md` records the real
> commit hash, and the gate table lists only checks you ran.

---

## Minimum completion

If you run short of time, this is enough to have done the activity:

1. The environment builds and the untouched notebook runs.
2. `results/baseline.json` is committed, captured before any refactoring.
3. **One** model function is extracted and importable.
4. **One** numerical regression test passes and fails when the model changes.
5. `docs/handoff.md` records the state.

Full modularization is the nice-to-have. The baseline-before-refactor sequence
is the thing worth taking home.

## Extensions

- A command-line interface for `reproduce.py` (`--parameter`, `--start`,
  `--stop`, `--step`).
- **Stability analysis.** Write the *dynamic* balances, form the Jacobian, and
  compute eigenvalues along each branch. This is the calculation that would let
  you say something about stability — which the current project cannot.
- Continuation: track the turning points directly instead of resolving them to
  the sweep step.
- A second sweep parameter (feed temperature or flow rate) and a two-parameter
  multiplicity map.
- Reimplement the steady-state solve in Pyomo and compare.

## Common problems

**`git push` asks for a password and rejects it.** GitHub removed password
authentication for Git. Use SSH keys or a personal access token.

**`conda env create` hangs on solving.** Try `mamba env create -f
environment.yml`, or `conda config --set solver libmamba`.

**`ModuleNotFoundError: cstr_workshop`.** The environment is not active, or the
editable install did not run. `conda activate cstr-workshop`, then
`pip install -e .` from the project root.

**The notebook writes files somewhere unexpected, or fails on `results/`.** Its
paths are relative to the working directory. Start Jupyter from the project
root, or use `python scripts/run_notebook.py`.

**Your refactored code finds fewer steady states than the notebook.** Look at
the initial guesses before you look at anything else.

**Tests pass but `reproduce.py` disagrees with the baseline.** The tests are
checking something other than the numbers you care about. That is a finding
about your tests.

**Your agent rewrote the notebook.** It was asked to extract, not to edit.
`git checkout notebooks/` and tighten the boundary in `CLAUDE.md`.

**Your agent changed a parameter so the sweep "looked better".** Revert it, and
add an explicit line to `CLAUDE.md` forbidding it. This happens.

## Final verification

```bash
conda activate cstr-workshop
pytest tests
python scripts/reproduce.py
python scripts/run_notebook.py --check
git status                       # expect a clean tree
git log --oneline main..HEAD     # expect a small number of coherent commits
```

Bring your repository to Workshop 2. You will write about these results.
