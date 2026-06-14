---
name: ai-workflow-loop-orchestrator
description: Use when coordinating Codex workers through a GitHub-backed maker/checker loop with durable state, explicit stop conditions, QA gates, and decision-ready owner asks.
---

# Codex Loop Orchestrator

Codex is usually the **maker**. It should not be the only checker of its own work.

## Required inputs

Read before starting:

- `AGENTS.md`
- `CONTEXT.md`
- `.ai/methods/ai-method-wheel.md`
- `docs/qa/checklist.md`
- relevant `specs/<feature>/` files
- GitHub issue/PR context

## Worker rule

You are a repository worker. Do not create subworkers or delegate. Work only on the assigned issue/spec. If blocked, complete all autonomous work first and report the exact blocker.

## Execution loop

1. Confirm the assigned issue/spec and stop condition.
2. Create or use an isolated branch/worktree.
3. Implement only the assigned slice.
4. Add/update tests first when possible.
5. Run required checks.
6. Write verification evidence into PR/body/report.
7. Stop after max iterations or successful checks.

## Stop condition template

```text
Max maker/checker loops: 2
Success: tests pass + lint/typecheck clean + QA checklist complete + separate review has no major findings
Failure: stop and report blocker with logs, changed files, and next recommended action
```

## Do not

- expand scope,
- invent commands,
- skip tests silently,
- read or print secrets,
- ask owner before autonomous proof is complete,
- treat green tests as proof that humans understand the change.
