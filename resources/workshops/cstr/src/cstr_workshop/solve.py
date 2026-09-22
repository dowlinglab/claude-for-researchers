"""Nonlinear solution of the steady-state balances, and distinct-root detection.

**Migrate from** `notebooks/cstr_exploration.ipynb`, cells 7 and 9.

A CSTR with an exothermic reaction can have one, two, or three steady states at
the same operating condition. One initial guess returns one root and tells you
nothing about how many exist, so the search over many guesses is not redundant
work to be tidied away -- it is the finding.

Keep the notebook's values when you move this code:

* ``1e-2`` K -- two roots closer than this are the same steady state
* ``1e-6``   -- the largest residual 2-norm that still counts as converged
* the initial-guess grid, 300 K to 440 K in 5 K steps

A coarser guess grid misses middle-branch roots near the turning points, and a
looser residual tolerance lets non-converged points into the results as if they
were steady states. Both changes leave output that looks entirely normal.
"""

from __future__ import annotations

from typing import Iterable, Mapping, Sequence

#: Two roots are the same steady state when their temperatures differ by less
#: than this, in K. Branches here are tens of kelvin apart while repeated
#: convergence to one root agrees to ~1e-9 K, so the exact value is not delicate.
TEMPERATURE_TOLERANCE_K = 1.0e-2

#: A solve counts as converged only below this residual 2-norm.
RESIDUAL_TOLERANCE = 1.0e-6


def initial_guesses(params: Mapping[str, float],
                    temperatures: Iterable[float] | None = None) -> list:
    """Return ``(C_A, T)`` starting points spanning the plausible outlet range.

    For each trial temperature, take the concentration that satisfies the
    material balance exactly at that temperature, so every guess is already
    consistent with one of the two equations. It costs nothing and substantially
    improves which roots the solver reaches.
    """
    raise NotImplementedError("Phase 3: migrate from notebook cell 9")


def solve_steady_state(params: Mapping[str, float],
                       guess: Sequence[float]) -> dict:
    """Solve the balances from one initial guess.

    Return the solution together with its residual norm and whether it
    converged -- a dict with ``CA``, ``T``, ``conversion``, ``residual_norm``,
    and ``converged`` is one reasonable shape.

    Report a failed or unphysical solve rather than raising: a sweep needs to
    discard it and carry on, not stop. Accept a result only when the solver
    reports success, the residual norm is below ``RESIDUAL_TOLERANCE``, and the
    state is physical (``0 <= C_A <= C_Af``, ``T > 0``).
    """
    raise NotImplementedError("Phase 3: migrate from notebook cells 7 and 9")


def find_distinct_steady_states(
    params: Mapping[str, float],
    guesses: Iterable[Sequence[float]] | None = None,
    temperature_tolerance: float = TEMPERATURE_TOLERANCE_K,
) -> list:
    """Return the distinct steady states found from many initial guesses.

    Sort by temperature, and report two solutions within
    ``temperature_tolerance`` of each other once.

    At the nominal condition this must find three. If it finds one, look at the
    initial guesses before anything else.
    """
    raise NotImplementedError("Phase 3: migrate from notebook cell 9")
