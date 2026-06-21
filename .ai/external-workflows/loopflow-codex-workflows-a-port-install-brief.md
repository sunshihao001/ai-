# A-port Install Brief: LoopFlow + codex-workflows

## 0. Owner correction captured

The owner corrected the workflow direction:

> When I ask to install an external workflow repository, do not default to absorbing its abstract bottom-layer logic into my workflow. First inspect the repository's own installation surface: what commands install it, what files it creates, what commands it exposes, what those commands are for, and where it should run. Then decide how it can operate harmoniously with the existing A/B/C/Bridge Method Wheel.

This brief follows that correction.

## 1. External repositories inspected

### LoopFlow

Repository: `https://github.com/faisalishfaq2005/loopflow`

Installation surface from README/package metadata:

- package: `@loopflow/cli`
- binary: `loopflow`
- requirement: Node 18+
- runtime dependency: Claude Code installed and authenticated
- install/run forms:
  - `npm install -g @loopflow/cli`
  - `npx @loopflow/cli`
- project initialization:
  - `loopflow init`
- validation:
  - `loopflow validate [name]`
- execution:
  - `loopflow run <name>`
  - `loopflow run <name> --dry-run`
- generated project surface:
  - `.loopflow/loops/*.yaml`
  - optional `.loopflow/worktrees/`
  - loop memory / run records during execution

Core runtime theory:

- A loop is a reusable goal pipeline.
- A maker step performs the work.
- A separate checker/gate step must end with `VERDICT: PASS` or `VERDICT: FAIL`.
- Budgets and iteration caps stop runaway agent loops.
- Memory files preserve learnings between runs.
- Optional git worktrees isolate concurrent or risky runs.

### codex-workflows

Repository: `https://github.com/shinpr/codex-workflows`

Installation surface from README/package metadata:

- package: `codex-workflows`
- binary: `codex-workflows`
- requirement: Node >= 22 and Codex CLI
- install:
  - `cd your-project`
  - `npx codex-workflows install`
- update:
  - `npx codex-workflows update --dry-run`
  - `npx codex-workflows update`
- status:
  - `npx codex-workflows status`
- generated project surface:
  - `.agents/skills/` — Codex skills / recipes
  - `.codex/agents/` — Codex subagent TOML definitions
  - manifest file for managed-file tracking
- Codex usage:
  - invoke recipes inside Codex CLI with `$recipe-*`, e.g. `$recipe-implement ...`

Core runtime theory:

- Codex should not receive one vague “just implement it” prompt for multi-file work.
- Larger changes should be split into requirements, design, task decomposition, TDD implementation, and quality checks.
- Agent/subagent context separation reduces context drift and author bias.
- Artifacts should be traceable: PRD → design doc → task → implementation/commit.

## 2. Local environment check

Observed on this machine:

- Node: `v22.22.3`
- npm: `10.9.8`
- Codex CLI: available at `/c/Users/Administrator/AppData/Local/Programs/OpenAI/Codex/bin/codex`
- Claude Code CLI: not found in PATH during this run
- Git: available

Therefore:

- `codex-workflows` can be installed and used now.
- LoopFlow can be initialized and validated now, but real non-dry-run execution requires installing/authenticating Claude Code first.

## 3. Installed into current Method Wheel repo

Target repo:

`C:\Users\Administrator\AppData\Local\hermes\profiles\cangwei\home\repos\ai-`

Backup created before install:

`.ai/backups/external-workflow-install-20260620-192951/`

Commands executed:

```bash
npx codex-workflows install
npx @loopflow/cli init
npx codex-workflows status
npx @loopflow/cli validate
npx @loopflow/cli run test-and-fix --dry-run
```

Observed results:

- `codex-workflows` installed v0.7.0.
- Install reported `.agents/ — 72 files`, `.codex/ — 25 files`, total 97 files installed.
- Status reported 116 managed files.
- LoopFlow initialized:
  - `.loopflow/loops/debt-audit.yaml`
  - `.loopflow/loops/docs-sync.yaml`
  - `.loopflow/loops/release-check.yaml`
  - `.loopflow/loops/test-and-fix.yaml`
- LoopFlow validation passed for all four loops.
- LoopFlow `test-and-fix --dry-run` successfully displayed the maker/checker prompts and `VERDICT` gate format.
- `.gitignore` was created/updated to ignore LoopFlow transient worktree/memory/run folders.

## 4. Placement in the Method Wheel

### Do not install as global Hermes skills by default

These projects are not merely prompt ideas. They are executable project-level workflow systems.

Installing them as Hermes skills would risk copying their entire workflow into the Hermes skill layer and confusing three different planes:

1. Hermes / Method Wheel: intent governance, A/B/C/Bridge routing, owner-facing control.
2. codex-workflows: Codex project-level skills, recipes, and subagents.
3. LoopFlow: Claude-Code-based loop runner with gates, budgets, and memory.

### Correct placement

```text
A-port / Method Wheel
  = decides whether the task is ready, what boundary applies, and which execution surface to use.

codex-workflows
  = Codex-side execution orchestration for repo work after A/B/C have produced enough boundary/spec.

LoopFlow
  = optional loop runner around repeated maker/checker work, enabled when Claude Code is available and the task benefits from budgeted retries.
```

## 5. Runtime routing rules

### Use codex-workflows when

- the task is repo-local,
- Codex CLI is the chosen maker,
- the work spans multiple files or requires design/task/quality gates,
- you want Codex recipes/subagents instead of a raw one-line Codex prompt.

Default route:

```text
A boundary brief → B source/context if needed → C design/spec → codex-workflows recipe in Codex → E verification → F owner decision
```

### Use LoopFlow when

- the task needs repeated fix/review cycles,
- a separate gate should judge maker output,
- budget/iteration cap matters,
- memory between iterations is useful,
- Claude Code is installed/authenticated.

Default route:

```text
A decides loop need → C defines loop goal/gate/budget → LoopFlow dry-run → owner/agent confirms → LoopFlow run → E records evidence
```

### Do not use either when

- the task is a simple one-off answer,
- no repo exists,
- there is no test/lint/build/reviewable artifact,
- the user only needs conceptual exploration,
- the relevant CLI/runtime is unavailable.

## 6. Correction to bottom workflow logic

Bad default to remove:

```text
external workflow repo appears → absorb its bottom-layer idea into Method Wheel → summarize theory
```

Correct default:

```text
external workflow repo appears
→ inspect install surface and runtime commands
→ identify generated files and target directories
→ sandbox/dry-run if possible
→ install into the correct execution surface
→ only then write a Method Wheel placement rule
→ keep A-port as the decision gate, not the installer itself
```

## 7. Current limitation

LoopFlow real execution is not fully enabled because `claude` was not found in PATH. The templates and dry-run path are installed/validated, but actual `loopflow run <name>` should wait until Claude Code is installed and authenticated.
