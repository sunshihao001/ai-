# meme Project State Pack — Packaging Guide

## Why this exists

The `meme` knowledge-base project is too data-heavy to restore from Git alone. Git restores the committed docs and structure, but the current working state also depends on local generated data and artifacts.

This state pack is the second restore layer.

## What to include in the state pack

Include only approved, non-secret local artifacts that are required to recreate the current working state.

### Required / likely important
- `skills-lock.json`
- `mql5/indicators/*.ex5`
- Any other generated binaries needed to reproduce current behavior
- Any explicit local data directory you decide must survive migration

### Do not include
- `.env` files
- API keys
- tokens
- credentials
- `.git`
- dependency caches
- build outputs that can be regenerated quickly
- `node_modules`
- `.venv`
- `__pycache__`

## Recommended state-pack layout

A simple directory form is easiest:

```text
meme-state-pack/
├─ skills-lock.json
└─ mql5/
   └─ indicators/
      └─ FCZ_Cost_Reclaim_Observer.ex5
```

## Recommended archive form

You may also compress the directory into a tar archive:

```bash
tar -czf meme-state-pack.tar.gz meme-state-pack/
```

## Restore command

```bash
bash scripts/restore-linux-state.sh <backup_source> <workspace_root> <state_pack_source>
```

Example:

```bash
bash scripts/restore-linux-state.sh /mnt/git-backup ~/workspaces /mnt/meme-state-pack
```

## Verification

After restore, verify:

```bash
cd ~/workspaces/MQL5_第一控盘区成本中枢回收模型_学习资料
git status --short --branch
ls skills-lock.json
ls mql5/indicators/FCZ_Cost_Reclaim_Observer.ex5
```

## Notes

The state pack is intentionally narrow. If you later discover another data directory is essential, add it explicitly and keep it out of the generic restore path until you are sure it should be preserved.
