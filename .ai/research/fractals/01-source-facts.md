# Fractals Source Facts

## Repository purpose

`TinyAGI/fractals` is a **recursive agentic task orchestrator**.
Its README describes it as a system that takes a high-level task, grows a self-similar tree of executable subtasks, and runs leaf tasks in isolated git worktrees with an agent swarm.

## PLAN vs EXECUTE flow

From the README and source:

- **PLAN phase**:
  - user enters a task and max depth
  - task is recursively classified as `atomic` or `composite`
  - composite tasks are decomposed into children
  - the tree is shown for review before execution
- **EXECUTE phase**:
  - user provides a workspace path
  - workspace is git-initialized
  - leaf tasks are executed in batches
  - each leaf runs in its own git worktree
  - status is polled through the server/UI

## Source-code-confirmed behavior

### `src/llm.ts`

- `classify(task, lineage)` calls OpenAI with structured output.
- It returns either `atomic` or `composite`.
- `decompose(task, lineage)` returns an array of subtask descriptions.
- The prompt instructs the model to split only when there are 2+ independent concerns.

### `src/orchestrator.ts`

- `plan(task, maxDepth)` recursively builds a tree.
- Atomic tasks are marked `ready`.
- Composite tasks are decomposed into children.
- Planning is recursive and tree-shaped, not linear.

### `src/executor.ts`

- Leaf tasks are executed through Claude or Codex CLI.
- Execution happens inside a git worktree created for the task.
- The prompt includes lineage context and sibling-awareness.

### `src/workspace.ts`

- Workspaces are created with `git init`.
- Worktrees are created under `.worktrees/<taskId>`.
- Worktrees are removed after completion when requested.

### `src/batch.ts`

- Depth-first batching is implemented.
- Breadth-first and layer-sequential are present as roadmap/fallback concepts.

### `src/server.ts`

- The server exposes APIs for session, decompose, workspace, execute, tree, and leaves.
- A single in-memory session is currently used.
- Execution progress is tracked and propagated up the tree.

## README claims

The README additionally claims:

- a Next.js frontend exists in `web/`
- the frontend provides task input, tree visualization, workspace setup, and execution polling
- OpenAI is used for planning/classification
- Claude / Codex CLI are used for execution
- the system is experimental

## Roadmap items explicitly named

- OpenCode CLI as a third executor option
- per-task executor override
- merge agent / backpropagation up the tree
- dependency-aware scheduling
- priority weights
- LLM-inferred dependencies
- breadth-first and layer-sequential batch strategies
- user-defined heuristics
- project-aware context
- calibration mode
- SSE/WebSocket updates
- task editing
- persistent sessions
- multi-session support

## Evidence boundary note

This note only records observable facts from the inspected files. Anything not seen directly in those files remains unknown and should not be promoted into interpretation.
