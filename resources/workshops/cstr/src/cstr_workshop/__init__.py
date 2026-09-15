"""CSTR workshop package.

This package is deliberately empty at the start of Workshop 1. The reactor model
currently lives inside ``notebooks/cstr_exploration.ipynb``; extracting it into
modules here is the work of that activity.

There is no required module layout. A reasonable one is::

    cstr_workshop/
        model.py      parameters, kinetics, steady-state residuals
        solve.py      nonlinear solution and distinct-root detection
        sweep.py      parameter sweeps
        plotting.py   figures

Whatever you choose, the test is the same: ``scripts/reproduce.py`` must
regenerate the baseline you captured before you started refactoring.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
