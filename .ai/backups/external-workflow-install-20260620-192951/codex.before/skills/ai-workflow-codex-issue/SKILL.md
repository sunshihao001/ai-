---
name: ai-workflow-codex-issue
description: Use when Codex should implement one GitHub issue from AGENTS.md, CONTEXT.md, specs, and acceptance criteria. Keep scope narrow, run tests, and report verification.
---

# AI Workflow: Codex Issue Execution

This project-level Codex skill is a portable copy of the core issue-execution workflow.

## Required Inputs

Read, in order:

1. `AGENTS.md`
2. `CONTEXT.md`
3. The linked GitHub issue
4. The linked `specs/<feature>/spec.md`
5. The linked `specs/<feature>/plan.md`
6. The linked `specs/<feature>/tasks.md`
7. Any linked ADRs or runbooks

## Rules

- Implement exactly one issue or one vertical slice.
- Do not silently expand scope.
- Prefer TDD when behavior changes.
- Add or update tests before or alongside implementation.
- Run the repository verification commands from `AGENTS.md`.
- Do not read or print secrets.
- Summarize changed files and verification results.

## Output Format

```md
## Summary

## Files Changed

## Verification
- command:
- result:

## Risks / Follow-ups
```
