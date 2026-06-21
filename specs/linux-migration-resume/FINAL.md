# Linux Migration Restore — Final Runbook

## Goal

Restore the current working state of the two project repos after switching from Windows to Linux, with a safe preflight pressure test and a reproducible restore command.

## What this restores

- Git-tracked repo content
- Approved local-only project artifacts from a backup directory or archive
- Current repo branch/status visibility after restore

## What this does not restore

- Secrets
- `.env` files
- Tokens / private credentials
- Dependency caches
- Build outputs
- Virtualenvs / `node_modules`
- `.git` payload from backups

## One-line prompt for A-mode demand grilling

```md
请按 A 端需求澄清模式处理，不要直接给结论。

目标：
我要把当前 Windows 上的项目运行状态，在切换到 Linux 后尽可能完整恢复出来。
需要你围绕“恢复什么、从哪里恢复、怎么验证恢复成功”做需求拷问，并使用 Fractals 多分叉方式进行压力测试。

必须做到：
1. 先明确当前状态里哪些内容已经在 Git 仓库里，哪些是本地 only。
2. 再明确哪些需要用 Git 恢复，哪些需要单独备份。
3. 再明确哪些内容不应进入仓库（例如 secrets、.env、缓存、依赖目录）。
4. 对“恢复当前运行状态”做多分叉压力测试：
   - Git 只恢复是否足够？
   - 仅恢复 Markdown 知识文件是否足够？
   - 本地导出、下载、缓存、session、索引是否需要保留？
   - 环境依赖、shell 配置、路径、venv、Node/Python 是否也算恢复目标？
5. 产出一个可执行的恢复契约：
   - 一个提示词
   - 一条命令
   - 一个可验证的恢复流程
6. 必须先做 dry-run / 模拟恢复，确认恢复后状态是否符合预期，再给最终结论。
7. 如果信息不足，只问最关键的 1-3 个问题，不要发散成大清单。

输出格式：
- 当前理解
- 已确认边界
- 仍缺的信息
- Fractals 分叉结论
- 最终建议恢复契约
- 验证方式
- 下一步
```

## Restore command

```bash
bash scripts/restore-linux-state.sh <backup_source> <workspace_root> [state_pack_source]
```

Example:

```bash
bash scripts/restore-linux-state.sh /mnt/backup/linux-migration-backup.tar.gz ~/workspaces
```

Directory example:

```bash
bash scripts/restore-linux-state.sh /mnt/backup ~/workspaces
```

For the data-heavy `meme` project, provide a separate state pack source as the third argument:

```bash
bash scripts/restore-linux-state.sh /mnt/backup ~/workspaces /mnt/meme-state-pack
```

## Dry-run command

Use this first.

```bash
bash scripts/restore-linux-state.sh --dry-run <backup_source> <workspace_root>
```

Example:

```bash
bash scripts/restore-linux-state.sh --dry-run /mnt/backup ~/workspaces
```

## Recommended restore flow

1. Prepare backup source.
2. Run dry-run.
3. Check that the simulated restore matches expected scope.
4. Run the real restore command.
5. Verify repo status after restore.

## Pressure-test checklist

Use Fractals-style branches to test the boundary:

- Git branch: does clone/pull alone restore enough?
- Knowledge branch: are the markdown files already safe in Git?
- Local-only branch: are any untracked downloads/exports missing from Git?
- Environment branch: do shell, PATH, venv, Node/Python matter?
- State branch: do caches/session artifacts matter or not?
- Human branch: is a one-command flow actually useful for the user?

## Success criteria

- The restore command runs.
- Dry-run works without writing files.
- Missing backup source exits non-zero.
- Repo status is visible after restore.
- The boundary between Git-backed and local-only state is explicit.

## Current script

- `scripts/restore-linux-state.sh`

## Current spec

- `specs/linux-migration-resume/spec.md`

## Notes

If the backup source contains only repository files and approved Markdown artifacts, the restore flow should be enough to recreate the current working state on a fresh Linux machine.

If the user later wants environment bootstrap, that should be added as a separate phase, not silently folded into file restore.
