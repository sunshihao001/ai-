# Issue → Codex Handoff Template

Use this when handing one bounded GitHub issue/spec slice to Codex.

## Required inputs

- GitHub issue: `#<number>`
- Spec: `specs/<feature>/spec.md`
- Plan/tasks: `specs/<feature>/plan.md`, `specs/<feature>/tasks.md`
- Project instructions: `AGENTS.md`
- Shared language: `CONTEXT.md`
- QA checklist: `docs/qa/*`

## Prompt template

```text
Read these first:
- AGENTS.md
- CONTEXT.md
- specs/<feature>/spec.md
- specs/<feature>/plan.md
- specs/<feature>/tasks.md
- GitHub issue #<number>
- docs/qa/playwright-qa-template.md
- docs/qa/accessibility-checklist.md
- docs/qa/security-checklist.md

Task:
Implement only GitHub issue #<number> as a vertical slice.

Rules:
1. Do not expand scope beyond the issue/spec.
2. If behavior can be tested, write or update tests first.
3. Prefer the smallest correct implementation.
4. Run the repo test commands from AGENTS.md.
5. If tests fail, diagnose root cause before changing code.
6. Do not claim completion without verification output.
7. Summarize changed files, commands run, results, risks, and any follow-up issues.
```

## Codex completion report format

```md
## Summary

## Files changed

## Verification
- command:
- result:

## QA notes
- Playwright/E2E:
- Accessibility:
- Security:

## Risks / follow-ups
```

## Stop conditions

Stop and ask a human if:

- The issue conflicts with the spec.
- The fix requires architecture or product judgment outside the issue.
- Credentials, production data, auth, billing, or destructive operations are involved.
- Tests cannot be run locally and no equivalent verification exists.
