# Linux Migration Resume / 恢复与迁移需求澄清

## Original Ask

> 现在我切换到Linux会清空数据，所以我需要把重要的两个项目，ai工作流和meme项目在本地储存的数据都上传到代码仓库以保证我切换到liunx能自动保持现在的运行状态，先检查下本地和仓库的同步情况再告诉我
>
> 继续
>
> 可以
>
> 都需要，我需要根据这个想法来进行a端的自动拷问需求澄清来深入解析需要，然后根据初步想法，多方面拷问使用Fractals来进行多想法思考，压力测试看真正恢复需要的部件，以及一键命令恢复脚本

## Improved Agent-Usable Question

Given the current Windows host, two Git repos already pushed to GitHub, and the user's goal of switching to Linux without losing important local project state, determine *exactly* what must be preserved, what can be restored from Git alone, what must be backed up separately, and what the one-command restore flow should do. Success means the restore path is explicit, pressure-tested, and reproducible from a fresh Linux machine.

## Current Understanding

### Repo A: ai-work / ai-
- Remote exists and is synced.
- Untracked local content was found and committed:
  - `codex知识学习/2026-06-06-AYi-Codex-Skill-全网整理.md`
- This appears to be durable knowledge content, not cache.

### Repo B: meme knowledge base
- Remote exists and is synced.
- Local changes were committed and pushed.
- The repo contains many markdown knowledge artifacts that are part of the durable state.

### User intent
- Preserve important local project state across Linux migration.
- Use A-port automatic demand grilling to clarify what counts as “important.”
- Use Fractals-style multi-branch thinking to pressure-test restoration needs.
- Produce a one-command restore script.

## Context and Constraints

- Source of truth for repo content is GitHub.
- Chat is not durable; the repo should contain the durable plan.
- The restore workflow should not expose secrets or credentials.
- The user wants reuse-first behavior and prefers durable file-based state.
- The Linux migration may wipe the current local machine state.

## Scope

### In scope
- Determine which parts of both projects are recoverable from Git alone.
- Identify non-Git local data that must be backed up separately.
- Define a restore script that can reconstruct the working state on Linux.
- Define verification steps for the restored environment.

### Out of scope
- Automatic upload of secrets, tokens, `.env`, or private credentials.
- Modifying production deployment config.
- Rewriting the projects themselves unless needed for recovery.

## Fractals / Pressure-Test Angles

Use multiple branches to test what “restore” actually means:

- **Git branch**: clone/pull only — is that enough?
- **Knowledge branch**: repo markdown files — already preserved?
- **Local-only branch**: untracked files, generated outputs, downloads, exports — must be archived separately?
- **Environment branch**: dependencies, shells, tools, PATH, venvs, Node/Python versions — must be recreated?
- **State branch**: run state, config, caches, session artifacts, agent memory — what matters and what does not?
- **Human convenience branch**: one command vs. multi-step recovery — how much automation is actually useful?

## Assumptions

- [confirmed] GitHub contains the current committed version of the two repos.
- [confirmed] The user wants to avoid losing local project data during migration.
- [unconfirmed] The restore target is a new Linux machine with no local state.
- [unconfirmed] Non-Git local files should be backed up as an archive, but the exact archive location is unknown.
- [unconfirmed] The restore flow should cover only project files, or also environment bootstrap.

## Acceptance Criteria

- A clear definition of what must be preserved is written down.
- The repo state that can be restored from Git is separated from local-only state.
- A one-command restore script is designed around the chosen restore boundary.
- The script has a defined input/output contract.
- Verification steps exist to prove the restore worked.

## Verification Plan

- Compare local repo state vs GitHub state before migration.
- Enumerate non-Git files that would be lost if the disk were wiped.
- Test the restore flow conceptually against at least these failure cases:
  - fresh Linux machine
  - Git present but no backup archive
  - backup archive present but wrong branch
  - backup archive present but missing environment dependencies
- After implementation, verify with a clean clone and a repeatable restore run.

## Critique Prompts

- What state is falsely assumed to be “in Git” but is actually local-only?
- What would break if the restore script runs on a machine with a different OS/toolchain version?
- What is the smallest restore unit that still makes the user productive?
- Which files are knowledge, which are configuration, and which are disposable output?
- How could the script falsely report success even if key content is missing?

## Missing High-Value Questions

1. Should the restore script restore **only Git-tracked repo content**, or also **local-only data/backups**?
2. Should it restore **environment/bootstrap state** too (Node/Python deps, shell config, tool setup), or only files?
3. Where is the canonical backup source for any non-Git files: a tar/zip archive, another folder, or a cloud drive?

## Next Stage

Need more questions before implementation.

## Candidate Restore Contract

The current restore boundary is:

- **Git-tracked repo content**: restored by clone/fetch/pull
- **Approved local-only project artifacts**: restored from a backup directory or archive
- **Sensitive data**: never restored by this script
- **Build caches / dependency caches**: intentionally excluded

The one-command flow is:

```text
restore-linux-state.sh [--dry-run] <backup-source> <workspace-root> [state-pack-source]
```

Behavior:
- clone or update the two repos
- restore approved local-only artifacts from a directory or tar archive
- exclude `.git`, `.env*`, credentials, caches, virtualenvs, build outputs, and package directories
- support a non-destructive dry-run mode
- run validation checks and exit non-zero on mismatch

Expected input shapes:
- `backup-source` may be a directory
- `backup-source` may be a tar/tar.gz/tgz/tar.bz2/tar.xz archive
- `workspace-root` is the parent directory where repos should exist after restore

Verification evidence:
- script usage path exits `2`
- dry-run path prints actions without writing files
- successful restore prints repo branch/status summaries
- missing backup source exits non-zero
```
