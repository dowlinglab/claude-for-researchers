# Scripts

| Script | What it does |
|---|---|
| `baseline.py capture` / `baseline.py compare` | The in-room route: preserve live notebook evidence, then execute a fresh kernel in a separate directory and compare it without replacing the original. See [session guide](../activities/session_guide.md). |
| `run_notebook.py` | Executes `notebooks/cstr_exploration.ipynb` from the project root. `--check` executes in a temporary workspace and discards all outputs, preserving project evidence. Use baseline capture/compare to save evidence. |
| `inspect_notebook.py` | Lists original source cells; `--cell INDEX` prints exact source without outputs. |
| `build_report.py --evidence results` | Copies the audited figure and builds the fallback report; `--check` validates the saved build receipt against current inputs/PDF. Use `results/recheck` for fresh comparison evidence. |

## `reproduce.py` is missing on purpose

Building it is an optional full-workflow extension: one documented command that
regenerates every result without opening the notebook.

What it has to do:

1. Read the parameters from `data/reactor_parameters.yml` — not from values
   retyped into the script.
2. Solve the nominal condition and the sweep using the functions you extracted
   into `src/cstr_workshop/`.
3. Write fresh CSV, figure and manifest into a separate directory such as
   `results/reproduced/`, preserving the baseline and its supporting artifacts.
4. Record, in that manifest, everything needed to interpret those numbers:
   parameters, software versions, solver tolerances, the sweep definition, the
   residual norms, and the command that produced them.

**Write the manifest to a new file — `results/reproduced.json` is a good name —
not to `results/baseline.json`.** The baseline is the evidence you captured
before refactoring. A reproduction script that overwrites it destroys the only
thing you can check against, and it does so at exactly the moment you most want
to check: when the numbers have moved. Have `reproduce.py` *compare* against
`baseline.json` and report the differences instead.

The gate is that its output matches the baseline you captured *before* you
started refactoring, within the tolerance you stated. If it does not, the
refactor changed the science, whatever the tests say.
