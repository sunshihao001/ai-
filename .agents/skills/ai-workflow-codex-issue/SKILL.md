---
name: ai-workflow-codex-issue
description: Use when handing one bounded GitHub issue/spec to Codex for implementation with verification evidence.
---

# AI Workflow: Codex Issue Execution

Derived from Superpowers `executing-plans`, `using-git-worktrees`, `subagent-driven-development`, Spec Kit `implement`, and Codex `AGENTS.md` usage.

## Goal
Make Codex a disciplined executor, not a vague chat participant.

## Prompt template
Ask Codex to read:
- `AGENTS.md`
- `CONTEXT.md`
- `.ai/methods/ai-method-wheel.md`
- relevant `.agents/skills/*/SKILL.md`
- relevant `specs/<feature>/*.md`
- GitHub issue body

Then instruct:
1. Implement only this issue.
2. Do not expand scope.
3. Add/update tests where appropriate.
4. Run required verification commands.
5. Summarize changed files and real command output.
6. If blocked, report blocker and smallest next question.

## Worktree recommendation
For parallel work, use one branch/worktree per issue.
