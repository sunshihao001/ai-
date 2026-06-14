# Codex Issue Handoff Template

Use this when handing one GitHub issue to Codex.

```md
Read first:
- AGENTS.md
- CONTEXT.md
- .codex/skills/ai-workflow-codex-issue/SKILL.md
- .codex/skills/ai-workflow-review-qa/SKILL.md
- specs/<feature>/spec.md
- specs/<feature>/plan.md
- specs/<feature>/tasks.md
- GitHub issue #<number>

Task:
Implement GitHub issue #<number> only.

Rules:
1. Keep scope to this issue.
2. Use TDD when behavior changes.
3. Add or update tests.
4. Run lint/typecheck/tests from AGENTS.md.
5. If UI changes, run Playwright or provide why it is not applicable.
6. Do not commit secrets.
7. Return changed files, verification commands, results, and risks.

Stop conditions:
- All required verification passes, or
- You are blocked by missing information, failing external dependency, or unsafe ambiguity.
```
