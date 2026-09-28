#!/usr/bin/env python3
"""List source-cell locations, or print one exact cell; never print outputs."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cell', type=int, help='zero-based source cell index')
    args = parser.parse_args(argv)
    cells = json.loads((ROOT / 'notebooks/cstr_exploration.ipynb').read_text())['cells']
    if args.cell is not None and not 0 <= args.cell < len(cells):
        parser.error(f'source cell index must be between 0 and {len(cells)-1}')
    for index, cell in enumerate(cells):
        if args.cell is not None and index != args.cell:
            continue
        source = ''.join(cell['source'])
        print(f'notebooks/cstr_exploration.ipynb: cell {index} ({cell["cell_type"]}; zero-based)')
        print(source if args.cell is not None else source.splitlines()[0] if source else '(empty)')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
