"""Build the small Part 1 handoff ZIP from its source files.

Usage: python build_workshop1_handoff.py [OUTPUT.zip]

The default output is workshop1_activity.zip beside this script. It is not tracked
in Git: the release workflow builds it from these sources.
"""
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "workshop1_activity.zip"
files = {
    "README.md": root / "workshop1_handoff/README.md",
    "notebooks/cstr_exploration.ipynb": root / "notebooks/cstr_exploration.ipynb",
    "data/reactor_parameters.yml": root / "data/reactor_parameters.yml",
    "results/.gitkeep": root / "workshop1_handoff/results/.gitkeep",
}
with ZipFile(out, "w", ZIP_DEFLATED) as archive:
    for name, source in files.items():
        archive.write(source, "cstr-project/" + name)
print(out)
