#!/usr/bin/env bash
set -euo pipefail

# restore-linux-state.sh
# One-command restore flow for Linux migration.
#
# Supported backup sources:
#   1) directory
#   2) tar/tar.gz/tgz/tar.bz2/tar.xz archive
#
# The script deliberately excludes:
#   - secrets and credentials
#   - dependency caches / build outputs
#   - .git directories from the backup payload
#
# It restores only approved local state on top of fresh repo clones.

show_usage() {
  cat <<'EOF'
Usage:
  restore-linux-state.sh [--dry-run] <backup_source> <workspace_root>

Examples:
  restore-linux-state.sh /mnt/backup/linux-migration-backup.tar.gz ~/workspaces
  restore-linux-state.sh /mnt/backup ~/workspaces
  restore-linux-state.sh --dry-run /mnt/backup ~/workspaces

Environment overrides:
  AI_REPO_URL, AI_BRANCH, MEME_REPO_URL, MEME_BRANCH
EOF
}

DRY_RUN=0
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
  shift
fi

if [[ $# -lt 2 ]]; then
  show_usage
  exit 2
fi

BACKUP_SOURCE="$1"
WORKSPACE_ROOT="$2"

AI_REPO_URL="${AI_REPO_URL:-https://github.com/sunshihao001/ai-.git}"
AI_BRANCH="${AI_BRANCH:-chore/a-port-intent-governance}"
MEME_REPO_URL="${MEME_REPO_URL:-https://github.com/sunshihao001/meme-.git}"
MEME_BRANCH="${MEME_BRANCH:-docs/project-governance-v1}"

AI_DIR="$WORKSPACE_ROOT/ai-"
MEME_DIR="$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料"
RESTORE_STAGING="$WORKSPACE_ROOT/.restore-staging"

mkdir -p "$WORKSPACE_ROOT"

log() {
  printf '%s\n' "$*"
}

run() {
  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "DRY-RUN: $*"
  else
    "$@"
  fi
}

clone_or_update() {
  local url="$1"
  local branch="$2"
  local dir="$3"

  if [[ -d "$dir/.git" ]]; then
    log "==> Updating $dir"
    run git -C "$dir" fetch --all --prune
    run git -C "$dir" checkout "$branch"
    run git -C "$dir" pull --rebase
  else
    log "==> Cloning $url"
    run git clone --branch "$branch" "$url" "$dir"
  fi
}

archive_to_staging() {
  local archive="$1"
  rm -rf "$RESTORE_STAGING"
  mkdir -p "$RESTORE_STAGING"
  case "$archive" in
    *.tar.gz|*.tgz) run tar -xzf "$archive" -C "$RESTORE_STAGING" ;;
    *.tar.bz2|*.tbz2) run tar -xjf "$archive" -C "$RESTORE_STAGING" ;;
    *.tar.xz|*.txz) run tar -xJf "$archive" -C "$RESTORE_STAGING" ;;
    *.tar) run tar -xf "$archive" -C "$RESTORE_STAGING" ;;
    *)
      log "==> Unsupported archive format: $archive"
      return 1
      ;;
  esac
}

sync_tree() {
  local source_root="$1"
  local target_root="$2"

  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "DRY-RUN: would sync $source_root -> $target_root"
    return 0
  fi

  python - "$source_root" "$target_root" <<'PY'
import fnmatch
import os
import shutil
import sys
from pathlib import Path

source = Path(sys.argv[1])
target = Path(sys.argv[2])

excludes = [
    '.git', '.git/**',
    '.env', '.env.*',
    '*.pem', '*.key', '*.p12', '*.pfx',
    'id_rsa', 'id_rsa.*',
    'credentials*', 'token*',
    '__pycache__', '__pycache__/**',
    '*.pyc', '*.pyo',
    'node_modules', 'node_modules/**',
    '.venv', '.venv/**', 'venv', 'venv/**',
    'dist', 'dist/**', 'build', 'build/**',
]


def excluded(rel: str) -> bool:
    rel = rel.replace('\\', '/')
    return any(fnmatch.fnmatch(rel, pat) for pat in excludes)


def main() -> int:
    if not source.exists():
        print(f'backup source not found: {source}', file=sys.stderr)
        return 1
    target.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(source):
        root_path = Path(root)
        rel_root = root_path.relative_to(source)
        if rel_root != Path('.') and excluded(str(rel_root)):
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if not excluded(str((rel_root / d).as_posix()))]
        dest_dir = target / rel_root
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name in files:
            rel_file = (rel_root / name).as_posix()
            if excluded(rel_file):
                continue
            src = root_path / name
            dst = dest_dir / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    return 0

raise SystemExit(main())
PY
}

restore_backup_if_present() {
  if [[ -z "$BACKUP_SOURCE" ]]; then
    return 0
  fi

  if [[ -f "$BACKUP_SOURCE" ]]; then
    log "==> Backup archive detected: $BACKUP_SOURCE"
    archive_to_staging "$BACKUP_SOURCE"
    sync_tree "$RESTORE_STAGING" "$WORKSPACE_ROOT"
  elif [[ -d "$BACKUP_SOURCE" ]]; then
    log "==> Backup directory detected: $BACKUP_SOURCE"
    sync_tree "$BACKUP_SOURCE" "$WORKSPACE_ROOT"
  else
    log "==> Backup source not found: $BACKUP_SOURCE"
    return 1
  fi
}

verify_repo() {
  local dir="$1"
  log "==> Verifying $dir"
  run git -C "$dir" status --short --branch
}

clone_or_update "$AI_REPO_URL" "$AI_BRANCH" "$AI_DIR"
clone_or_update "$MEME_REPO_URL" "$MEME_BRANCH" "$MEME_DIR"
restore_backup_if_present
verify_repo "$AI_DIR"
verify_repo "$MEME_DIR"

log "==> Restore complete"
