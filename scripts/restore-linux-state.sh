#!/usr/bin/env bash
set -euo pipefail

# restore-linux-state.sh
# Final restore flow for Linux migration.
#
# Inputs:
#   1) backup_source: optional directory or archive with repo-local payload
#   2) workspace_root: where repos should live
#   3) state_pack_source: optional directory or archive with local-only state
#
# Supported state pack contents (white-listed):
#   - skills-lock.json
#   - mql5/indicators/*.ex5
#   - additional explicitly approved files placed under known paths
#
# Always excluded:
#   - secrets and credentials
#   - .git directories
#   - dependency caches / build outputs
#   - .env*, token*, credentials*, id_rsa*, *.pem, *.key, *.p12, *.pfx

show_usage() {
  cat <<'EOF'
Usage:
  restore-linux-state.sh [--dry-run] <backup_source> <workspace_root> [state_pack_source]

Examples:
  restore-linux-state.sh /mnt/backup/linux-migration-backup.tar.gz ~/workspaces
  restore-linux-state.sh /mnt/backup ~/workspaces
  restore-linux-state.sh /mnt/backup ~/workspaces /mnt/state-pack
  restore-linux-state.sh --dry-run /mnt/backup ~/workspaces /mnt/state-pack

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
STATE_PACK_SOURCE="${3:-}"

AI_REPO_URL="${AI_REPO_URL:-https://github.com/sunshihao001/ai-.git}"
AI_BRANCH="${AI_BRANCH:-chore/a-port-intent-governance}"
MEME_REPO_URL="${MEME_REPO_URL:-https://github.com/sunshihao001/meme-.git}"
MEME_BRANCH="${MEME_BRANCH:-docs/project-governance-v1}"

AI_DIR="$WORKSPACE_ROOT/ai-"
MEME_DIR="$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料"
RESTORE_STAGING="$WORKSPACE_ROOT/.restore-staging"
STATE_STAGING="$WORKSPACE_ROOT/.state-staging"

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

archive_to_staging() {
  local archive="$1"
  local staging="$2"
  rm -rf "$staging"
  mkdir -p "$staging"
  case "$archive" in
    *.tar.gz|*.tgz) run tar -xzf "$archive" -C "$staging" ;;
    *.tar.bz2|*.tbz2) run tar -xjf "$archive" -C "$staging" ;;
    *.tar.xz|*.txz) run tar -xJf "$archive" -C "$staging" ;;
    *.tar) run tar -xf "$archive" -C "$staging" ;;
    *)
      log "==> Unsupported archive format: $archive"
      return 1
      ;;
  esac
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

excluded_path() {
  local rel="$1"
  rel="${rel//\\//}"
  local part
  IFS='/' read -r -a parts <<< "$rel"
  for part in "${parts[@]}"; do
    [[ -z "$part" || "$part" == "." ]] && continue
    case "$part" in
      .git|node_modules|.venv|venv|dist|build|__pycache__)
        return 0
        ;;
      .env*|token*|credentials*|id_rsa*|*.pem|*.key|*.p12|*.pfx|*.pyc|*.pyo)
        return 0
        ;;
    esac
  done
  return 1
}

sync_tree() {
  local source_root="$1"
  local target_root="$2"
  local mode="${3:-all}"

  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "DRY-RUN: would sync $source_root -> $target_root ($mode)"
    return 0
  fi

  python - "$source_root" "$target_root" "$mode" <<'PY'
from pathlib import Path
import os
import shutil
import sys

source = Path(sys.argv[1])
target = Path(sys.argv[2])
mode = sys.argv[3]

allowed_state_pack_paths = {
    'skills-lock.json',
}
allowed_state_pack_prefixes = (
    'mql5/indicators/',
)

sensitive_names = {
    '.git', 'node_modules', '.venv', 'venv', 'dist', 'build', '__pycache__',
}
sensitive_prefixes = ('.env', 'token', 'credentials', 'id_rsa')
sensitive_suffixes = ('.pem', '.key', '.p12', '.pfx', '.pyc', '.pyo')


def is_sensitive(rel: str) -> bool:
    rel = rel.replace('\\', '/')
    parts = [p for p in rel.split('/') if p and p != '.']
    if not parts:
        return False
    for part in parts:
        if part in sensitive_names:
            return True
        if part.startswith(sensitive_prefixes):
            return True
        if part.endswith(sensitive_suffixes):
            return True
    return False


def allowed_state_pack(rel: str) -> bool:
    rel = rel.replace('\\', '/')
    if rel in allowed_state_pack_paths:
        return True
    return rel.startswith(allowed_state_pack_prefixes)


def should_copy(rel: str) -> bool:
    if is_sensitive(rel):
        return False
    if mode == 'state':
        return allowed_state_pack(rel)
    return True


def main() -> int:
    if not source.exists():
        print(f'backup source not found: {source}', file=sys.stderr)
        return 1
    target.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(source):
        root_path = Path(root)
        rel_root = root_path.relative_to(source)
        rel_root_str = rel_root.as_posix()
        if rel_root_str != '.' and is_sensitive(rel_root_str):
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if not is_sensitive((rel_root / d).as_posix())]
        dest_dir = target / rel_root
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name in files:
            rel_file = (rel_root / name).as_posix()
            if not should_copy(rel_file):
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
    archive_to_staging "$BACKUP_SOURCE" "$RESTORE_STAGING"
    sync_tree "$RESTORE_STAGING" "$WORKSPACE_ROOT" all
  elif [[ -d "$BACKUP_SOURCE" ]]; then
    log "==> Backup directory detected: $BACKUP_SOURCE"
    sync_tree "$BACKUP_SOURCE" "$WORKSPACE_ROOT" all
  else
    log "==> Backup source not found: $BACKUP_SOURCE"
    return 1
  fi
}

restore_state_pack_if_present() {
  if [[ -z "$STATE_PACK_SOURCE" ]]; then
    return 0
  fi

  if [[ -f "$STATE_PACK_SOURCE" ]]; then
    log "==> State pack archive detected: $STATE_PACK_SOURCE"
    archive_to_staging "$STATE_PACK_SOURCE" "$STATE_STAGING"
    sync_tree "$STATE_STAGING" "$MEME_DIR" state
  elif [[ -d "$STATE_PACK_SOURCE" ]]; then
    log "==> State pack directory detected: $STATE_PACK_SOURCE"
    sync_tree "$STATE_PACK_SOURCE" "$MEME_DIR" state
  else
    log "==> State pack source not found: $STATE_PACK_SOURCE"
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
restore_state_pack_if_present
verify_repo "$AI_DIR"
verify_repo "$MEME_DIR"

log "==> Restore complete"
