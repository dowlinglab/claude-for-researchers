"""Checks for evidence preservation; no expected scientific answers supplied."""
import importlib.util
import json
from pathlib import Path

import nbformat

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/baseline.py'
spec = importlib.util.spec_from_file_location('baseline_helper', SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def test_code_hash_ignores_outputs_but_detects_code_edits():
    notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell('x = 1')])
    before = helper.code_hash(notebook)
    notebook.cells[0].outputs = [nbformat.v4.new_output('stream', text='1')]
    assert helper.code_hash(notebook) == before
    notebook.cells[0].source = 'x = 2'
    assert helper.code_hash(notebook) != before


def sample():
    return {'parameters': {'sample': 2}, 'units': {}, 'settings': {}, 'nominal_states': [],
            'sweep': [{'sample': 1}], 'software': {},
            'provenance': {'notebook_code_sha256': 'code', 'parameter_file_sha256': 'yaml'},
            'artifacts': {'steady_states.csv': {'sha256': 'csv'}}}


def test_compare_detects_numeric_change_even_if_csv_digest_is_unchanged():
    saved = sample()
    fresh = sample()
    assert helper.compare_documents(saved, fresh)['match']
    fresh['sweep'][0]['sample'] = 3
    result = helper.compare_documents(saved, fresh)
    assert not result['match']
    assert not result['checks']['sweep']


def test_capture_refuses_existing_evidence_without_execution(tmp_path, monkeypatch):
    monkeypatch.setattr(helper, 'ROOT', tmp_path)
    (tmp_path / 'results').mkdir()
    saved = tmp_path / 'results/baseline.json'
    saved.write_text('keep this evidence')
    monkeypatch.setattr(helper, 'execute_snapshot', lambda *args: (_ for _ in ()).throw(AssertionError('must not execute')))
    assert helper.main(['capture']) == 2
    assert saved.read_text() == 'keep this evidence'


def test_compare_refuses_modified_saved_artifact(tmp_path, monkeypatch):
    monkeypatch.setattr(helper, 'ROOT', tmp_path)
    (tmp_path / 'results').mkdir()
    saved = sample()
    (tmp_path / 'results/baseline.json').write_text(json.dumps(saved))
    (tmp_path / 'results/steady_states.csv').write_text('changed')
    monkeypatch.setattr(helper, 'execute_snapshot', lambda *args: (_ for _ in ()).throw(AssertionError('must not execute')))
    assert helper.main(['compare']) == 2
    assert not (tmp_path / 'results/recheck').exists()
