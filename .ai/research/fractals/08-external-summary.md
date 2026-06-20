# Fractals External Summary

> One-page readable summary for future review of `TinyAGI/fractals` in the AI Method Wheel.

## One-line conclusion

`TinyAGI/fractals` should be treated as a **recursive task-orchestration reference**, not a downloadable A-port skill.

Recommended classification:

```text
PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE
```

This refines the earlier theory decision `PARTIAL_ACCEPT + BRIDGE`.

Meaning:

- accept its recursive classify/decompose/branch-shaping ideas,
- bridge those ideas into logical A/C/D/E port design,
- keep execution, worktrees, batching, and swarm behavior out of A-port,
- do not promote the runtime as a Method Wheel baseline.

## What the repo is

Based on inspected source files, `fractals` has two major phases:

```text
PLAN: classify/decompose a high-level task into a recursive task tree
EXECUTE: run leaf tasks in isolated git worktrees through Claude/Codex CLI
```

Important source files inspected:

- `src/llm.ts` — OpenAI structured-output classify/decompose.
- `src/orchestrator.ts` — recursive `plan()` tree builder.
- `src/executor.ts` — Claude/Codex CLI execution for leaf tasks.
- `src/workspace.ts` — git init and worktree management.
- `src/batch.ts` — depth-first batch execution strategy.
- `src/server.ts` — API surface for decompose/workspace/execute/tree/leaves.

## What to absorb

### Absorb into A as a narrow support pattern

A-port may use the **branching idea**, not the execution engine:

```text
raw idea
→ classify atomic/composite
→ generate candidate branches
→ compare branch shapes
→ ask the next blocking question or transfer to C
```

This helps A-port produce more diverse and criticizable directions.

### Absorb into C as planning theory

C-port can use:

- recursive decomposition,
- branch depth limits,
- lineage-aware planning,
- atomic/composite classification,
- future dependency-aware scheduling ideas.

### Keep in D/E if ever implemented

D/E are the only places where these ideas belong:

- git worktree isolation,
- leaf task execution,
- batch scheduling,
- CLI worker spawning,
- progress/status checking.

## What not to absorb

A-port must not do these:

- create worktrees,
- run leaf tasks,
- schedule execution batches,
- spawn Claude/Codex workers,
- own server/API execution endpoints,
- treat a decomposition as permission to execute.

## Current safe boundary

A-port boundary:

```text
A may classify, decompose, and generate candidate branches.
A must stop before execution planning becomes implementation orchestration.
A transfers to C when the branch shape and boundary are stable enough for theory generation.
```

## Current state of the theory pack

Completed:

- B-port evidence collection
- C-port bridge analysis
- A-port diversity subroutine extraction
- A-port automatic-loop boundary brief
- resume guide for blocked Codex long-theory generation

Blocked / deferred:

- Codex long-theory generation was attempted but blocked by Windows sandbox helper failure and account concurrency limits.
- Web UI source, tests, CI, and runtime behavior remain unverified.

## Next recommended move

When continuing this line, do **not** restart from A.

Resume from:

```text
.ai/research/fractals/05-a-port-boundary-brief.md
```

Then either:

1. run Codex long-theory generation when the environment is usable, or
2. manually promote the current pack into a Method Wheel rule if the owner accepts the current boundary.

## Decision status

Current decision is no longer only theory-pattern acceptance:

```text
PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE
```

This refines the earlier `PARTIAL_ACCEPT + BRIDGE` decision. The practical correction is: do not rebuild Fractals; try the existing tool in a sandbox, lightly adapt it, and connect it to the full workflow.
