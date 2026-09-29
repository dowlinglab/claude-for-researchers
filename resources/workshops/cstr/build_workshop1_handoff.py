"""Build workshop1_activity.zip, the small Part 1 handoff, from its source files."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent
out = root / "workshop1_activity.zip"
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
