"""The steady-state locus figure.

**Migrate from** `notebooks/cstr_exploration.ipynb`, cell 13.

Draw the figure from a dataframe rather than from whatever happens to be in
memory, so that it can be regenerated from ``results/steady_states.csv`` alone.
"""

from __future__ import annotations


def plot_steady_state_locus(frame, parameter: str,
                            ylabel: str = "Reactor temperature (K)",
                            column: str = "T", ax=None):
    """Plot every steady state against the swept parameter.

    Two things here are easy to get wrong, and both draw a curve the model does
    not have.

    ``branch_index`` is a *rank by temperature at one condition*, not an
    identity that persists across the sweep. Outside the multiplicity window
    there is a single steady state, which takes index 0 -- and above the upper
    fold that single state is the ignited one, near 395 K. Plotting index 0 as
    one connected series joins it to the cold states below the window and draws
    a near-vertical jump of about 67 K through a region where nothing exists.

    So break the line wherever ``n_steady_states`` changes, and label segments
    for what they are: lower, middle and upper only where all three are present,
    and a single neutral label elsewhere.

    The figure shows where multiple steady states exist. It does not show which
    of them a reactor would settle at -- that is a question about the dynamic
    model, which this project does not implement.

    Return the axes so the caller decides where to save and at what resolution.
    """
    raise NotImplementedError("Phase 3: migrate from notebook cell 13")
