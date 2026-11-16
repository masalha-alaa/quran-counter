"""Compile all checked-in Qt translation catalogs before running or packaging."""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def compile_translations(output_dir):
    executable = "pyside6-lrelease.exe" if sys.platform == "win32" else "pyside6-lrelease"
    local_tool = Path(sys.executable).with_name(executable)
    tool = str(local_tool) if local_tool.is_file() else shutil.which(executable)
    if not tool:
        raise RuntimeError("pyside6-lrelease was not found. Install the project's PySide6 dependency first.")
    sources = sorted((ROOT / "translations").glob("*.ts"))
    if not sources:
        raise RuntimeError("No translation source files were found.")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for source in sources:
        subprocess.run([tool, str(source), "-qm", str(output_dir / f"{source.stem}.qm")], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "translations")
    args = parser.parse_args()
    try:
        compile_translations(args.output_dir)
    except (RuntimeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Translation compilation failed: {error}\n")
