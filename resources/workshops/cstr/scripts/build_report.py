#!/usr/bin/env python3
"""Build the fallback report from a named evidence folder, or check its receipt."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inputs(report):
    return {str(p.relative_to(report)): digest(p) for p in sorted(report.rglob('*'))
            if p.is_file() and p.suffix in {'.tex', '.bib', '.sty', '.cls', '.png', '.jpg', '.pdf'}
            and (p.suffix != '.pdf' or 'figures' in p.relative_to(report).parts)}

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence', default='results', help='project-relative evidence directory, e.g. results/recheck')
    parser.add_argument('--check', action='store_true', help='check that successful build inputs and PDF are unchanged')
    args = parser.parse_args(argv)
    report = ROOT / 'report'
    receipt = report / 'build_receipt.json'
    pdf = report / 'audit_fallback.pdf'
    if args.check:
        try:
            record = json.loads(receipt.read_text())
            current = (record['status'] == 'built' and record['inputs'] == inputs(report)
                       and record['pdf_sha256'] == digest(pdf)
                       and record['evidence_sha256'] == digest(ROOT / record['evidence']))
        except (OSError, ValueError, KeyError):
            current = False
        print('CURRENT: receipt matches source, evidence and PDF; human review remains separate.' if current else
              'NOT CURRENT: no successful matching build receipt. Rebuild or record source-only status.')
        return 0 if current else 1
    evidence = (ROOT / args.evidence).resolve()
    if not evidence.is_relative_to(ROOT.resolve()):
        parser.error('--evidence must be inside this project')
    figure = evidence / 'steady_state_locus.png'
    command = ['latexmk', '-g', '-pdf', '-interaction=nonstopmode', '-halt-on-error', 'audit_fallback.tex']
    record = {'status': 'failed', 'source': 'report/audit_fallback.tex',
              'command': command, 'working_directory': 'report',
              'evidence': str(figure.relative_to(ROOT)), 'created_utc': datetime.now(timezone.utc).isoformat()}
    # Invalidate an older success even if the new attempt cannot start.
    receipt.write_text(json.dumps(record, indent=2) + '\n')
    try:
        (report / 'figures').mkdir(exist_ok=True)
        shutil.copy2(figure, report / 'figures/steady_state_locus.png')
        before = inputs(report)
        result = subprocess.run(command, cwd=report)
        if result.returncode or not pdf.exists() or before != inputs(report):
            raise RuntimeError('Build failed or inputs changed during build; previous PDF is not current evidence.')
        record.update(status='built', inputs=before, pdf_sha256=digest(pdf), evidence_sha256=digest(figure))
    except (OSError, RuntimeError) as exc:
        record['error'] = str(exc)
        print(f'Report not built: {exc}')
    receipt.write_text(json.dumps(record, indent=2) + '\n')
    print('Build receipt: report/build_receipt.json. This checks build provenance, not claim correctness.')
    return 0 if record['status'] == 'built' else 1

if __name__ == '__main__':
    raise SystemExit(main())
