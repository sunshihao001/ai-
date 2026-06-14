#!/usr/bin/env python
"""Install this repository's curated AI workflow skills into local agent skill directories.

Default targets:
- ~/.codex/skills
- ~/.claude/skills

The repository remains the source of truth. This script copies `.agents/skills/*` into
local agent directories. Project-level `.codex/skills/*` stays committed for Codex to
read directly from the repository.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".agents" / "skills"
PROJECT_CODEX_SRC = ROOT / ".codex" / "skills"
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


def iter_skill_dirs(include_project_codex: bool) -> list[Path]:
    if not SRC.exists():
        raise SystemExit(f"Missing source directory: {SRC}")
    skills = [p for p in SRC.iterdir() if (p / "SKILL.md").exists()]
    if include_project_codex and PROJECT_CODEX_SRC.exists():
        for p in PROJECT_CODEX_SRC.iterdir():
            if (p / "SKILL.md").exists() and p.name not in {s.name for s in skills}:
                skills.append(p)
    return sorted(skills, key=lambda p: p.name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", action="append", help="Skill target directory. Can be repeated.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing installed skills.")
    parser.add_argument(
        "--include-project-codex",
        action="store_true",
        help="Also copy project-level .codex/skills entries that are not already in .agents/skills.",
    )
    args = parser.parse_args()
    targets = [Path(t).expanduser() for t in args.target] if args.target else DEFAULT_TARGETS
    skills = iter_skill_dirs(args.include_project_codex)
    print(f"source: {SRC}")
    if args.include_project_codex:
        print(f"project codex source: {PROJECT_CODEX_SRC}")
    print("skills:", ", ".join(p.name for p in skills))
    for target in targets:
        for skill in skills:
            copy_skill(skill, target, args.overwrite)
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
