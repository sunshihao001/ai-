---
name: ai-workflow-codex-issue
description: "Use when handing a narrow GitHub issue or task to Codex for implementation. Forces Codex to read project docs, stay in scope, test, and report verification."
version: 1.0.0
author: Curated for Codex execution
license: MIT
---

# AI Workflow: Codex Issue Execution

## Purpose
Connect the planning/grilling side to the coding side. Codex should execute from GitHub artifacts, not from vague chat.

## Prompt Template for Codex
```text
Read first:
- AGENTS.md
- CONTEXT.md
- .ai/methods/ai-method-wheel.md
- specs/<feature>/spec.md
- specs/<feature>/plan.md
- specs/<feature>/tasks.md
- GitHub issue #<id>

Task:
Implement only issue #<id>.

Rules:
- Do not expand scope.
- Prefer TDD: add/update failing test first where practical.
- Keep the change as a vertical slice.
- Run relevant lint/typecheck/tests.
- If a command is missing or fails for environment reasons, report it honestly.
- Summarize changed files, verification commands, results, and remaining risks.
```

## Completion Report Template
```md
## Summary
## Files Changed
## Verification
## Risks / Follow-ups
```
