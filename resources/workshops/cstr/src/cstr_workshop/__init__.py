"""CSTR workshop package.

The reactor model starts inside ``notebooks/cstr_exploration.ipynb``. Moving it
here is the work of Workshop 1.

Four modules are stubbed, each with the docstring, signature, and units it needs
and no body:

    model.py      parameters, kinetics, steady-state residuals   (cells 3, 5)
    solve.py      solving, and finding distinct steady states    (cells 7, 9)
    sweep.py      sweeping a parameter                           (cell 11)
    plotting.py   the locus figure                               (cell 13)

They are scaffolding, not a specification. Merge them, split them, rename them,
or replace them with something you prefer -- the gate is unchanged: whatever you
build must regenerate the baseline you captured before you started.

The one real change from the notebook is in the signatures. There, the functions
read parameters from the surrounding cell scope; here, every function takes
``params`` explicitly. Removing that hidden dependency is most of the migration,
and it is what makes the functions testable in isolation.

Nothing is imported here on purpose, so that renaming or deleting a module
cannot break ``import cstr_workshop``. Add re-exports if you want them.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
