# Results

Generated artifacts go here. Nothing in this directory is edited by hand, and
nothing in it is the source of truth for anything — it can always be recreated
by running the documented command.

Workshop 1 asks you to put three things here before you refactor anything:

| File | What it is |
|---|---|
| `baseline.json` | The nominal solution plus everything needed to interpret it: parameters, software versions, solver tolerances, sweep definition, residual norm, and the exact command that produced it |
| `steady_states.csv` | One row per steady state found at each swept condition |
| `steady_state_locus.png` | The figure, regenerated from the CSV rather than redrawn by hand |

## Why this order matters

The baseline is evidence that the code did something specific before you changed
it. Captured after a refactor, it records only that the new code agrees with
itself.

## Git

Generated results are ignored by `.gitignore` by default, because regenerating
them is cheap and diffs of regenerated binaries are noise. Commit a result only
when you have a reason — a figure that goes into the report, or a baseline you
need to compare against months from now — and say in the commit message which
command produced it.
