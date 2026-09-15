# Scripts

| Script | What it does |
|---|---|
| `run_notebook.py` | Executes `notebooks/cstr_exploration.ipynb` from the project root. `--check` runs a throwaway copy, so it can gate a commit without dirtying your diff. |

## `reproduce.py` is missing on purpose

Building it is the central task of Workshop 1: one documented command that
regenerates every result without opening the notebook.

What it has to do:

1. Read the parameters from `data/reactor_parameters.yml` — not from values
   retyped into the script.
2. Solve the nominal condition and the sweep using the functions you extracted
   into `src/cstr_workshop/`.
3. Write `results/baseline.json`, `results/steady_states.csv`, and
   `results/steady_state_locus.png`.
4. Record, in `baseline.json`, everything needed to interpret those numbers:
   parameters, software versions, solver tolerances, the sweep definition, the
   residual norms, and the command that produced them.

The gate is that its output matches the baseline you captured *before* you
started refactoring, within the tolerance you stated. If it does not, the
refactor changed the science, whatever the tests say.
