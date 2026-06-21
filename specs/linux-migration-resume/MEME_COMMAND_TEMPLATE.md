# meme 项目恢复命令模板

## 1) 变量

```bash
export BACKUP_SOURCE='/mnt/backup/linux-migration-backup.tar.gz'
export WORKSPACE_ROOT='~/workspaces'
export STATE_PACK_SOURCE='/mnt/meme-state-pack'
```

说明：
- `BACKUP_SOURCE`：Git/仓库包（或目录）
- `STATE_PACK_SOURCE`：`meme` 的本地状态包

## 2) 先做模拟恢复

```bash
cd ~/ai-work/ai-
bash scripts/restore-linux-state.sh --dry-run "$BACKUP_SOURCE" "$WORKSPACE_ROOT" "$STATE_PACK_SOURCE"
```

## 3) 再做正式恢复

```bash
cd ~/ai-work/ai-
bash scripts/restore-linux-state.sh "$BACKUP_SOURCE" "$WORKSPACE_ROOT" "$STATE_PACK_SOURCE"
```

## 4) 恢复后检查

```bash
cd "$WORKSPACE_ROOT/ai-" && git status --short --branch
cd "$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料" && git status --short --branch
ls "$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料/skills-lock.json"
ls "$WORKSPACE_ROOT/MQL5_第一控盘区成本中枢回收模型_学习资料/mql5/indicators/FCZ_Cost_Reclaim_Observer.ex5"
```

## 5) 如果要做一个最小一行版

```bash
export BACKUP_SOURCE='/mnt/backup/linux-migration-backup.tar.gz' && export WORKSPACE_ROOT='~/workspaces' && export STATE_PACK_SOURCE='/mnt/meme-state-pack' && cd ~/ai-work/ai- && bash scripts/restore-linux-state.sh --dry-run "$BACKUP_SOURCE" "$WORKSPACE_ROOT" "$STATE_PACK_SOURCE" && bash scripts/restore-linux-state.sh "$BACKUP_SOURCE" "$WORKSPACE_ROOT" "$STATE_PACK_SOURCE"
```
