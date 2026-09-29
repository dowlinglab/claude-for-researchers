"""Package audit-project/ as the workshop download."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent
project = root / "audit-project"
out = root / "workshop2_audit_project.zip"
skip = {".DS_Store"}
with ZipFile(out, "w", ZIP_DEFLATED) as archive:
    for path in sorted(project.rglob("*")):
        if path.is_file() and path.name not in skip and ".ipynb_checkpoints" not in path.parts:
            archive.write(path, "audit-project/" + path.relative_to(project).as_posix())
print(out)
