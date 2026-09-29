"""Package audit-project/ as the Part 2 download.

Usage: python build_audit_zip.py [OUTPUT.zip]

The default output is workshop2_activity.zip beside this script. It is not tracked
in Git: the release workflow builds it from this folder.
"""
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent
project = root / "audit-project"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "workshop2_activity.zip"
skip = {".DS_Store"}
with ZipFile(out, "w", ZIP_DEFLATED) as archive:
    for path in sorted(project.rglob("*")):
        if path.is_file() and path.name not in skip and ".ipynb_checkpoints" not in path.parts:
            archive.write(path, "audit-project/" + path.relative_to(project).as_posix())
print(out)
