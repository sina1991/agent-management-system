#!/usr/bin/env python3
"""Validate YAML files when PyYAML is installed; no files are modified."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".venv", "venv", "__pycache__"}

def main() -> int:
    try:
        import yaml
    except ImportError:
        print("PyYAML is not installed. Install it with: python -m pip install PyYAML")
        return 2

    yaml_files = []
    for path in ROOT.rglob("*.yaml"):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        yaml_files.append(path)

    errors = []
    for path in sorted(yaml_files):
        try:
            with path.open("r", encoding="utf-8") as handle:
                list(yaml.safe_load_all(handle))
        except Exception as exc:
            errors.append((path.relative_to(ROOT), str(exc)))

    if errors:
        for path, error in errors:
            print(f"FAIL {path}: {error}")
        return 1

    print(f"Validated {len(yaml_files)} YAML files.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
