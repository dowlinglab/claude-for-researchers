"""Reactor model: parameters, kinetics, and the steady-state balances.

**Migrate from** `notebooks/cstr_exploration.ipynb`, cells 3 and 5.

Reaction
--------
``A -> B``, irreversible, exothermic, first order in A.

Steady-state balances
---------------------
Material balance on A over the well-mixed liquid volume ``V``::

    0 = q * (C_Af - C_A) - V * k(T) * C_A                       [mol/min]

Energy balance, contents at the outlet temperature ``T``::

    0 = q * rho * Cp * (T_f - T)                                [J/min]
        + (-dH_rxn) * V * k(T) * C_A
        - UA * (T - T_c)

Sign conventions
----------------
``dHr`` is the enthalpy of reaction and is **negative** for an exothermic
reaction, so ``(-dHr)`` is a positive heat release. The exchange term is written
as heat *removed* to the coolant and is therefore subtracted; it becomes a heat
input when ``T < T_c``.

Units
-----
``q`` L/min, ``V`` L, ``C_A`` mol/L, ``T`` K, ``rho`` g/L, ``Cp`` J/(g K),
``dHr`` J/mol, ``EoverR`` K, ``k0`` 1/min, ``UA`` J/(min K).

All temperatures are absolute. There are no Celsius values in this project.

The one change from the notebook
--------------------------------
In the notebook these functions read the parameters from the surrounding cell
scope. Here every function takes ``params`` explicitly. That is the migration:
not retyping the formulas, but removing the hidden dependency on module-level
state so a function can be called, tested, and reasoned about on its own.
"""

from __future__ import annotations

from typing import Mapping, Sequence

#: Every key a parameter mapping must provide.
REQUIRED_KEYS = ("q", "V", "CAf", "Tf", "rho", "Cp", "dHr", "EoverR", "k0",
                 "UA", "Tc")


def load_parameters(path=None, **overrides: float) -> dict:
    """Return a validated parameter dictionary.

    Read ``data/reactor_parameters.yml`` rather than retyping the constants from
    the notebook: two copies of a number drift the first time one is edited.
    Apply any keyword ``overrides`` last, and validate before returning.

    Raise ``ValueError`` if a required key is missing.
    """
    raise NotImplementedError("Phase 3: load the parameters from YAML")


def validate_parameters(params: Mapping[str, float]) -> None:
    """Raise ``ValueError`` for parameters that are not physically admissible.

    Worth checking, because each of these produces plausible output rather than
    an error: a non-positive ``q``, ``V``, ``CAf``, ``k0`` or ``EoverR``; a
    negative ``UA``; a **positive** ``dHr`` (that is an endothermic reaction, not
    this problem); and a temperature below ~100, which is almost always a
    Celsius value that was never converted.
    """
    raise NotImplementedError("Phase 3: validate the inputs")


def arrhenius_rate_constant(T, params: Mapping[str, float]):
    """First-order rate constant ``k(T) = k0 * exp(-EoverR / T)``, in 1/min."""
    raise NotImplementedError("Phase 3: migrate from notebook cell 5")


def reaction_rate(CA, T, params: Mapping[str, float]):
    """Rate of consumption of A, ``k(T) * C_A``, in mol/(L min)."""
    raise NotImplementedError("Phase 3: migrate from notebook cell 5")


def steady_state_residuals(state: Sequence[float],
                           params: Mapping[str, float]) -> list:
    """Return ``[material_balance, energy_balance]`` at ``state``.

    ``state`` is ``(C_A, T)`` in mol/L and K. Both residuals are zero at a
    steady state; their units are mol/min and J/min.

    Keep the argument order ``(state, params)``: ``scipy.optimize.fsolve`` calls
    ``f(x, *args)``, so this signature works directly with ``args=(params,)``.
    """
    raise NotImplementedError("Phase 3: migrate from notebook cell 5")


def conversion(CA, params: Mapping[str, float]):
    """Fractional conversion of A, ``(C_Af - C_A) / C_Af``."""
    raise NotImplementedError("Phase 3: migrate from notebook cell 5")
