"""Preservation and stale-build checks, independent of scientific answers."""
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'

def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixture(tmp_path, monkeypatch):
    module = load('build_report')
    monkeypatch.setattr(module, 'ROOT', tmp_path)
    (tmp_path / 'report').mkdir()
    (tmp_path / 'results').mkdir()
    (tmp_path / 'results/steady_state_locus.png').write_bytes(b'test figure')
    (tmp_path / 'report/audit_fallback.tex').write_text('test source')
    def successful_build(*args, **kwargs):
        (tmp_path / 'report/audit_fallback.pdf').write_bytes(b'test pdf')
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(module.subprocess, 'run', successful_build)
    assert module.main([]) == 0
    assert module.main(['--check']) == 0
    return module


def test_receipt_detects_source_edit(tmp_path, monkeypatch):
    module = fixture(tmp_path, monkeypatch)
    (tmp_path / 'report/audit_fallback.tex').write_text('changed source')
    assert module.main(['--check']) == 1


def test_receipt_detects_changed_evidence_and_pdf(tmp_path, monkeypatch):
    module = fixture(tmp_path, monkeypatch)
    (tmp_path / 'results/steady_state_locus.png').write_bytes(b'changed evidence')
    assert module.main(['--check']) == 1
    (tmp_path / 'results/steady_state_locus.png').write_bytes(b'test figure')
    (tmp_path / 'report/audit_fallback.pdf').write_bytes(b'changed pdf')
    assert module.main(['--check']) == 1


def test_failed_rebuild_invalidates_old_success(tmp_path, monkeypatch):
    module = fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(module.subprocess, 'run', lambda *a, **kw: SimpleNamespace(returncode=1))
    assert module.main([]) == 1
    assert (tmp_path / 'report/audit_fallback.pdf').exists()
    assert module.main(['--check']) == 1


def test_source_inspection_does_not_expose_execution_outputs(tmp_path, monkeypatch, capsys):
    module = load('inspect_notebook')
    monkeypatch.setattr(module, 'ROOT', tmp_path)
    (tmp_path / 'notebooks').mkdir()
    (tmp_path / 'notebooks/cstr_exploration.ipynb').write_text(json.dumps({'cells':[
        {'cell_type':'code', 'source':['x = 1'], 'outputs':['DO NOT PRINT OUTPUTS']}]}))
    assert module.main(['--cell','0']) == 0
    output = capsys.readouterr().out
    assert 'x = 1' in output and 'DO NOT PRINT OUTPUTS' not in output
