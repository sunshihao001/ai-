#!/usr/bin/env python
"""Install project AI workflow skills into local agent skill directories.

The repo remains the source of truth. Installed copies are runtime convenience.
Default targets:
- ~/.codex/skills
- ~/.claude/skills
"""
from pathlib import Path
import shutil
import argparse

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".agents" / "skills"
DEFAULT_TARGETS = [Path.home()/".codex"/"skills", Path.home()/".claude"/"skills"]

def copy_tree(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

parser = argparse.ArgumentParser()
parser.add_argument("--target", action="append", help="Additional/override target skill dir. Can be repeated.")
args = parser.parse_args()

targets = [Path(t).expanduser() for t in args.target] if args.target else DEFAULT_TARGETS
if not SRC.exists():
    raise SystemExit(f"missing source skills: {SRC}")

for target in targets:
    target.mkdir(parents=True, exist_ok=True)
    for skill in SRC.iterdir():
        if skill.is_dir() and (skill/"SKILL.md").exists():
            copy_tree(skill, target/skill.name)
            print(f"installed {skill.name} -> {target/skill.name}")
