#!/usr/bin/env python3
"""Print a concise repository audit without reading file contents or secrets."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}

def main() -> int:
    print("=== Repository ===")
    print(ROOT)
    print("\n=== Git status ===")
    result = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--short", "--branch"],
        text=True, capture_output=True
    )
    print(result.stdout.strip() or "(not a Git repository or clean)")
    if result.returncode not in (0, 128):
        print(result.stderr.strip())
    print("\n=== Files (paths only) ===")
    paths = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP for part in path.parts):
            continue
        paths.append(path.relative_to(ROOT).as_posix())
    for item in sorted(paths):
        print(item)
    print(f"\nTotal files: {len(paths)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
