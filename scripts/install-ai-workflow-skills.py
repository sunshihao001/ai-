#!/usr/bin/env python
"""Install this repository's curated AI workflow skills into local agent skill directories.

Default targets:
- ~/.codex/skills
- ~/.claude/skills

The repository remains the source of truth. This script only copies `.agents/skills/*`.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".agents" / "skills"
DEFAULT_TARGETS = [Path.home() / ".codex" / "skills", Path.home() / ".claude" / "skills"]

def copy_skill(src: Path, target_root: Path, overwrite: bool) -> None:
    dst = target_root / src.name
    if dst.exists():
        if not overwrite:
            print(f"skip existing: {dst}")
            return
        shutil.rmtree(dst)
    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)
    print(f"installed: {dst}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", action="append", help="Skill target directory. Can be repeated.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing installed skills.")
    args = parser.parse_args()
    if not SRC.exists():
        raise SystemExit(f"Missing source directory: {SRC}")
    targets = [Path(t).expanduser() for t in args.target] if args.target else DEFAULT_TARGETS
    skills = [p for p in SRC.iterdir() if (p / "SKILL.md").exists()]
    print(f"source: {SRC}")
    print("skills:", ", ".join(p.name for p in skills))
    for target in targets:
        for skill in skills:
            copy_skill(skill, target, args.overwrite)
    print("done")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
