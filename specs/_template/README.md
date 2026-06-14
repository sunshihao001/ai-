# First Feature Spec Template

Copy this directory to `specs/<feature-slug>/` for each production-bound feature or bug fix.

## Files

- `spec.md` — user-facing requirement and acceptance criteria.
- `plan.md` — implementation approach and tradeoffs.
- `tasks.md` — vertical slices/issues.
- `checklist.md` — verification, QA, security, accessibility.

## Workflow

1. Brainstorm/grill the idea before coding.
2. Convert clarified intent into `spec.md`.
3. Capture architectural choices in `plan.md` or an ADR.
4. Split into vertical slices in `tasks.md`.
5. Use `checklist.md` as the PR quality gate.
6. Create GitHub issues from tasks.
7. Hand one issue/spec slice to Codex at a time.
