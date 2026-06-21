# Linux Migration Restore — One-Page Command Sheet

## 0. Variables to set once

```bash
export BACKUP_SOURCE='/mnt/backup/linux-migration-backup.tar.gz'
export WORKSPACE_ROOT='~/workspaces'
```

If your backup is a directory, point `BACKUP_SOURCE` to that directory instead.

---

## 1. Preflight: make sure repos are already synced

```bash
cd ~/ai-work/ai- && git status --short --branch
cd ~/Documents/MQL5_第一控盘区成本中枢回收模型_学习资料 && git status --short --branch
```

What you want to see:
- no uncommitted changes you care about
- no ahead/behind divergence
- the important local data already pushed to GitHub

---

## 2. Dry-run restore first

```bash
cd ~/ai-work/ai-
bash scripts/restore-linux-state.sh --dry-run "$BACKUP_SOURCE" "$WORKSPACE_ROOT"
```

Expected:
- script prints clone/update actions
- script prints backup source handling
- no files are written
- exit code is non-zero only if the backup source is missing or invalid

---

## 3. Real restore

```bash
cd ~/ai-work/ai-
bash scripts/restore-linux-state.sh "$BACKUP_SOURCE" "$WORKSPACE_ROOT"
```

What it does:
- clones or updates `ai-`
- clones or updates `meme`
- restores approved local project artifacts
- skips secrets, `.env`, caches, build outputs, `node_modules`, `.venv`, and `.git`

---

## 4. Verify after restore

```bash
cd "$WORKSPACE_ROOT/ai-" && git status --short --branch
cd "$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料" && git status --short --branch
```

Optional content checks:

```bash
find "$WORKSPACE_ROOT" -maxdepth 3 -type f | head
```

---

## 5. If you need to inspect the final docs

```bash
cd ~/ai-work/ai-
cat specs/linux-migration-resume/FINAL.md
cat specs/linux-migration-resume/CHECKLIST.md
cat specs/linux-migration-resume/spec.md
```

---

## 6. Minimal recovery sequence

```bash
export BACKUP_SOURCE='/mnt/backup/linux-migration-backup.tar.gz'
export WORKSPACE_ROOT='~/workspaces'
cd ~/ai-work/ai-
bash scripts/restore-linux-state.sh --dry-run "$BACKUP_SOURCE" "$WORKSPACE_ROOT"
bash scripts/restore-linux-state.sh "$BACKUP_SOURCE" "$WORKSPACE_ROOT"
cd "$WORKSPACE_ROOT/ai-" && git status --short --branch
cd "$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料" && git status --short --branch
```

---

## 7. Decision rule

If dry-run matches the expected scope, run the real restore. If the backup source is missing, stop and fix the backup first. If you later want environment bootstrap, treat that as a separate phase.
