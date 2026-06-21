# Linux Migration Restore — Preflight / Post-restore Checklist

## Purpose

Use this checklist before switching to Linux, during the restore dry-run, and after the real restore.

## 1. Preflight checklist

### Repo state

- [ ] `ai-` repo is committed and pushed
- [ ] `meme` repo is committed and pushed
- [ ] `git status --short --branch` shows no ahead/behind divergence
- [ ] No untracked local files remain that matter for recovery

### Backup source

- [ ] A backup source exists
- [ ] Backup source is either:
  - [ ] a directory
  - [ ] a tar/tar.gz/tgz/tar.bz2/tar.xz archive
- [ ] Backup source does not contain secrets or credentials
- [ ] Backup source contains only approved local artifacts

### Scope decision

- [ ] Restore scope is file-based only
- [ ] Environment bootstrap is explicitly out of scope or separately planned
- [ ] `.env`, keys, tokens, and credentials are excluded
- [ ] Dependency caches and build outputs are excluded

## 2. Dry-run checklist

Run:

```bash
bash scripts/restore-linux-state.sh --dry-run <backup_source> <workspace_root>
```

Expected:

- [ ] Command exits with the expected status
- [ ] The script identifies both repos
- [ ] The script reports clone/update actions
- [ ] The script reports the backup source type
- [ ] The script reports what would be synced
- [ ] No files are written during dry-run
- [ ] Missing backup source fails non-zero

## 3. Real restore checklist

Run:

```bash
bash scripts/restore-linux-state.sh <backup_source> <workspace_root>
```

Expected:

- [ ] Both repos exist under `workspace_root`
- [ ] Each repo is on the expected branch
- [ ] `git status --short --branch` shows the expected status
- [ ] Approved local artifacts are present
- [ ] Excluded files are still absent
- [ ] No secrets were restored

## 4. Post-restore verification checklist

### Git verification

- [ ] `git -C <repo> status --short --branch` is clean or only contains expected local edits
- [ ] Branch names match the intended restore branches
- [ ] Remotes point to the expected GitHub repos

### Content verification

- [ ] Expected markdown knowledge files are present
- [ ] Expected indexes / notes / runbooks are present
- [ ] Any required local-only artifacts were restored

### Safety verification

- [ ] No `.env` files were copied in
- [ ] No key/token/credential files were copied in
- [ ] No build/cache directories were restored

## 5. Failure modes to test

- [ ] Backup source path does not exist
- [ ] Backup archive format is unsupported
- [ ] Workspace root is empty and repos must be cloned fresh
- [ ] Backup contains excluded content and script skips it
- [ ] Git remote is unreachable

## 6. Final acceptance

- [ ] Dry-run is successful
- [ ] Real restore is successful
- [ ] Post-restore verification passes
- [ ] Recovery boundary is documented
- [ ] User can rerun the restore command from the runbook without extra context
