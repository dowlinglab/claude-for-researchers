"""Environment smoke test.

This is the only test that ships with the starter. It does not test the reactor
model -- there is no reactor model outside the notebook yet. It exists so that
``pytest`` is a working command from the first minute of Workshop 1, and so that
a broken environment is diagnosed before it is blamed on the science.

The regression tests you add in Workshop 1 belong beside this file.
"""

from __future__ import annotations

import sys

import pytest


def test_python_version_is_supported():
    assert sys.version_info >= (3, 10), (
        f"this project requires Python 3.10 or newer, found {sys.version.split()[0]}; "
        "activate the cstr-workshop environment"
    )


@pytest.mark.parametrize("module", ["numpy", "scipy", "pandas", "matplotlib", "yaml"])
def test_scientific_stack_is_importable(module):
    pytest.importorskip(module, reason=f"{module} missing from the environment")


def test_workshop_package_is_installed():
    import cstr_workshop

    assert cstr_workshop.__version__, "cstr_workshop is installed but has no version"


def test_reactor_parameters_file_is_complete():
    """The parameter file is data the whole project depends on; check it loads."""
    from pathlib import Path

    yaml = pytest.importorskip("yaml")
    path = Path(__file__).resolve().parents[1] / "data" / "reactor_parameters.yml"
    assert path.exists(), f"missing parameter file: {path}"
    params = yaml.safe_load(path.read_text())

    expected = {"q", "V", "CAf", "Tf", "rho", "Cp", "dHr", "EoverR", "k0", "UA", "Tc"}
    assert expected.issubset(params), (
        f"missing parameters: {sorted(expected - set(params))}"
    )
    assert params["dHr"] < 0, "dHr is the enthalpy of reaction: negative for exothermic"
    assert params["Tf"] > 100 and params["Tc"] > 100, "temperatures must be in kelvin"
