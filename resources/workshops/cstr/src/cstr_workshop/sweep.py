"""Sweep one reactor parameter and collect every steady state found.

**Migrate from** `notebooks/cstr_exploration.ipynb`, cell 11.
"""

from __future__ import annotations

from typing import Iterable, Mapping


def sweep_parameter(params: Mapping[str, float], name: str,
                    values: Iterable[float], **solver_options):
    """Return one row per steady state for each value of ``params[name]``.

    The notebook produces these columns, and the rest of the project reads
    them, so keep the names: the swept parameter, ``branch_index`` (0 is the
    coldest steady state at that condition), ``n_steady_states`` at that
    condition, ``CA``, ``conversion``, ``T``, and ``residual_norm``.

    **The result is not one row per condition.** A condition with three steady
    states contributes three rows. Code that assumes one row per condition --
    including anything that quietly calls ``drop_duplicates`` on the swept
    column, or indexes the frame by it -- silently discards the ignited branch,
    which is the behavior the whole study is about.

    Raise ``ValueError`` for a ``name`` that is not a reactor parameter, rather
    than sweeping a key nothing reads.
    """
    raise NotImplementedError("Phase 3: migrate from notebook cell 11")
