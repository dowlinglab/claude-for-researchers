#!/usr/bin/env python3
"""Capture the untouched notebook, or compare a fresh run without replacing it."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / 'notebooks/cstr_exploration.ipynb'
PARAMETERS = ROOT / 'data/reactor_parameters.yml'
CONTRACT = Path(__file__).with_name('baseline_contract.json')
ARTIFACTS = ('baseline.json', 'baseline.executed.ipynb', 'steady_states.csv', 'steady_state_locus.png')


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def code_hash(notebook):
    """Ignore execution outputs; preserve every original code cell byte."""
    source = [cell.source for cell in notebook.cells if cell.cell_type == 'code']
    return hashlib.sha256(json.dumps(source, ensure_ascii=False).encode()).hexdigest()


# This observer reads live variables. It does not evaluate a model or solver.
OBSERVER = '''import json as _capture_json
from pathlib import Path as _CapturePath
_CapturePath("results/live.json").write_text(_capture_json.dumps({
    "parameters": params,
    "nominal_states": nominal_states,
    "sweep": sweep_df.to_dict(orient="records"),
    "settings": {"guess_temperatures_K": guess_temperatures.tolist(),
                 "coolant_temperatures_K": Tc_values.tolist(),
                 "root_deduplication_K": TOL_T,
                 "residual_acceptance": TOL_RESIDUAL,
                 "solver": "scipy.optimize.fsolve",
                 "solver_options": "defaults; full_output=True",
                 "initial_concentration": "material balance at each guess temperature"}
}, indent=2, allow_nan=False) + "\\n")'''


def compare_documents(saved, fresh):
    """Exact comparison of a same-environment rerun; never relax a mismatch."""
    fields = ('parameters', 'units', 'settings', 'nominal_states', 'sweep', 'software')
    checks = {field: saved[field] == fresh[field] for field in fields}
    checks['notebook_code'] = saved['provenance']['notebook_code_sha256'] == fresh['provenance']['notebook_code_sha256']
    checks['parameter_file'] = saved['provenance']['parameter_file_sha256'] == fresh['provenance']['parameter_file_sha256']
    checks['csv_bytes'] = saved['artifacts']['steady_states.csv']['sha256'] == fresh['artifacts']['steady_states.csv']['sha256']
    return {'comparison': 'exact same-environment rerun; no tolerance or rounding applied',
            'checks': checks, 'match': all(checks.values()),
            'note': 'A mismatch needs investigation. Do not replace the baseline. Human scientific review is separate.'}


def execute_snapshot(destination, command):
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    contract = json.loads(CONTRACT.read_text())
    if code_hash(notebook) != contract['notebook_code_sha256'] or sha256(PARAMETERS) != contract['parameter_file_sha256']:
        raise ValueError('Notebook code or parameter file differs from the supplied starter. Stop: restore/review the original before first capture; do not bless edited science as its baseline.')
    (destination / 'results').mkdir()
    observer = nbformat.v4.new_code_cell(OBSERVER, metadata={'tags': ['baseline-observer']})
    notebook.cells.append(observer)
    NotebookClient(notebook, timeout=600, kernel_name='python3',
                   resources={'metadata': {'path': str(destination)}}).execute()
    out = destination / 'results'
    nbformat.write(notebook, out / 'baseline.executed.ipynb')
    payload = json.loads((out / 'live.json').read_text())
    (out / 'live.json').unlink()
    payload.update({
        'schema_version': 1,
        'units': {'q': 'L/min', 'V': 'L', 'CAf': 'mol/L', 'Tf': 'K', 'rho': 'g/L',
                  'Cp': 'J/(g K)', 'dHr': 'J/mol', 'EoverR': 'K', 'k0': '1/min',
                  'UA': 'J/(min K)', 'Tc': 'K', 'CA': 'mol/L', 'T': 'K',
                  'conversion': 'fraction', 'residual_norm': 'norm of mixed-unit balance residuals; see notebook'},
        'software': {'python': platform.python_version(), **{name: importlib.metadata.version(name)
                     for name in ('numpy', 'scipy', 'pandas', 'matplotlib', 'nbclient', 'nbformat')}},
        'provenance': {'created_utc': datetime.now(timezone.utc).isoformat(), 'command': command,
                       'source_notebook': 'notebooks/cstr_exploration.ipynb',
                       'notebook_code_sha256': contract['notebook_code_sha256'],
                       'parameter_file_sha256': sha256(PARAMETERS),
                       'capture': 'Original code cells executed unchanged in a fresh kernel; final observer serializes live variables.',
                       'locations': {'parameters': 'original cell 3', 'nominal_states': 'original cell 9',
                                     'settings': 'original cells 9 and 11', 'sweep': 'original cell 11; CSV keys Tc and branch_index'},
                       'cell_numbering': 'zero-based'},
        'review': {'human_review': 'pending', 'assumptions': 'Read original notebook introduction; helper does not verify scientific validity.'},
        'artifacts': {name: {'sha256': sha256(out / name)} for name in ARTIFACTS if name != 'baseline.json'},
    })
    (out / 'baseline.json').write_text(json.dumps(payload, indent=2, allow_nan=False) + '\n')
    return out, payload


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('capture', 'compare'))
    args = parser.parse_args(argv)
    results = ROOT / 'results'
    results.mkdir(exist_ok=True)
    saved = results / 'baseline.json'
    target = results if args.action == 'capture' else results / 'recheck'
    try:
        if args.action == 'capture' and any((target / name).exists() for name in ARTIFACTS):
            raise ValueError('Capture refuses to overwrite existing evidence. Inspect/archive any earlier run before first capture. For an accepted baseline use compare.')
        if args.action == 'compare':
            if not saved.exists():
                raise ValueError('No baseline exists. On an untouched starter, run capture first.')
            if target.exists():
                raise ValueError('results/recheck already exists. Preserve/rename that rerun before another comparison.')
            original = json.loads(saved.read_text())
            for name, info in original['artifacts'].items():
                if sha256(results / name) != info['sha256']:
                    raise ValueError(f'Saved evidence was changed: {name}. Investigate before comparing.')
        with tempfile.TemporaryDirectory(prefix='cstr-baseline-') as tmp:
            out, fresh = execute_snapshot(Path(tmp), f'python scripts/baseline.py {args.action}')
            comparison = compare_documents(original, fresh) if args.action == 'compare' else None
            if comparison is not None:
                (out / 'comparison.json').write_text(json.dumps(comparison, indent=2) + '\n')
                shutil.copytree(out, target)
            else:
                for name in ARTIFACTS:
                    shutil.copy2(out / name, target / name)
        print(f'Saved evidence in {target.relative_to(ROOT)}; original notebook unchanged.')
        if comparison is not None:
            print('MATCH' if comparison['match'] else 'MISMATCH: inspect results/recheck/comparison.json')
            return 0 if comparison['match'] else 1
        print('Human review pending. Inspect one nominal record, one CSV row, units, settings, and assumptions.')
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(f'Baseline stopped: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
