#!/usr/bin/env python3
"""Execute the exploration notebook from the project root.

    python scripts/run_notebook.py                 # execute in place
    python scripts/run_notebook.py --check         # execute a copy, change nothing

The notebook writes to `results/` using paths relative to the working directory,
which is fine when you launch JupyterLab from the project root and wrong the
moment anything else executes it. Rather than paper over that, this script sets
the working directory explicitly and says so. Noticing the difference is part of
Workshop 1.

`--check` is the gate command: it proves the notebook still runs top to bottom
without leaving modified outputs in your diff.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = PROJECT_ROOT / "notebooks" / "cstr_exploration.ipynb"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--notebook", type=Path, default=NOTEBOOK)
    parser.add_argument("--check", action="store_true",
                        help="execute a temporary copy and discard it")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args(argv)

    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError as exc:  # pragma: no cover - environment problem
        print(f"missing dependency: {exc}. Activate the cstr-workshop environment.",
              file=sys.stderr)
        return 2

    if not args.notebook.exists():
        print(f"no such notebook: {args.notebook}", file=sys.stderr)
        return 2

    (PROJECT_ROOT / "results").mkdir(exist_ok=True)

    source = args.notebook
    with tempfile.TemporaryDirectory() as tmp:
        if args.check:
            source = Path(tmp) / args.notebook.name
            shutil.copy2(args.notebook, source)

        notebook = nbformat.read(source, as_version=4)
        client = NotebookClient(
            notebook, timeout=args.timeout, kernel_name="python3",
            # Everything in the notebook writes paths relative to here.
            resources={"metadata": {"path": str(PROJECT_ROOT)}},
        )
        client.execute()

        if not args.check:
            nbformat.write(notebook, args.notebook)

    where = "a temporary copy" if args.check else args.notebook
    print(f"executed {where} with working directory {PROJECT_ROOT}")
    print("results/steady_states.csv and results/steady_state_locus.png are current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
