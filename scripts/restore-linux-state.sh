#!/usr/bin/env bash
set -euo pipefail

# restore-linux-state.sh
# One-command restore skeleton for Linux migration.
# Usage:
#   ./restore-linux-state.sh <backup_source> <workspace_root>
#
# Behavior:
# - clones or updates the two tracked repos
# - optionally restores a backup archive if present
# - prints a verification summary
#
# This script is intentionally conservative: it does not restore secrets,
# .env files, or credentials.

if [[ $# -lt 2 ]]; then
  cat <<'EOF'
Usage: restore-linux-state.sh <backup_source> <workspace_root>

Examples:
  restore-linux-state.sh /mnt/backup/linux-migration-backup.tar.gz ~/workspaces
  restore-linux-state.sh /mnt/backup ~/workspaces
EOF
  exit 2
fi

BACKUP_SOURCE="$1"
WORKSPACE_ROOT="$2"

AI_REPO_URL="https://github.com/sunshihao001/ai-.git"
AIBRANCH="chore/a-port-intent-governance"
MEME_REPO_URL="https://github.com/sunshihao001/meme-.git"
MEMEBRANCH="docs/project-governance-v1"

AI_DIR="$WORKSPACE_ROOT/ai-"
MEME_DIR="$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料"

mkdir -p "$WORKSPACE_ROOT"

clone_or_update() {
  local url="$1"
  local branch="$2"
  local dir="$3"

  if [[ -d "$dir/.git" ]]; then
    echo "==> Updating $dir"
    git -C "$dir" fetch --all --prune
    git -C "$dir" checkout "$branch"
    git -C "$dir" pull --rebase
  else
    echo "==> Cloning $url"
    git clone --branch "$branch" "$url" "$dir"
  fi
}

restore_backup_if_present() {
  if [[ -z "$BACKUP_SOURCE" ]]; then
    return 0
  fi

  if [[ -f "$BACKUP_SOURCE" ]]; then
    echo "==> Backup archive detected: $BACKUP_SOURCE"
    echo "    (archive extraction not implemented yet; add policy-specific restore steps here)"
  elif [[ -d "$BACKUP_SOURCE" ]]; then
    echo "==> Backup directory detected: $BACKUP_SOURCE"
    echo "    (copy policy-specific files here)"
  else
    echo "==> Backup source not found: $BACKUP_SOURCE"
    return 1
  fi
}

verify_repo() {
  local dir="$1"
  echo "==> Verifying $dir"
  git -C "$dir" status --short --branch
}

clone_or_update "$AI_REPO_URL" "$AIBRANCH" "$AI_DIR"
clone_or_update "$MEME_REPO_URL" "$MEMEBRANCH" "$MEME_DIR"
restore_backup_if_present
verify_repo "$AI_DIR"
verify_repo "$MEME_DIR"

echo "==> Restore skeleton complete"
