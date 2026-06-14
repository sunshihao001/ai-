# Checklist: <Feature Name>

## Spec alignment

- [ ] Implementation matches `spec.md`.
- [ ] Non-goals were not implemented accidentally.
- [ ] Edge cases are handled or explicitly deferred.

## Tests

- [ ] Unit tests added/updated.
- [ ] Integration tests added/updated where needed.
- [ ] E2E/Playwright covers critical path where needed.
- [ ] Regression test added for bugs.
- [ ] Tests fail for the right reason before the fix when using TDD.

## Quality

- [ ] Lint passes.
- [ ] Typecheck passes.
- [ ] Build passes.
- [ ] No unrelated formatting churn.
- [ ] No over-broad rewrites.

## Security

- [ ] Permissions/auth checked.
- [ ] Inputs validated.
- [ ] No secrets printed or committed.
- [ ] Dependency/security audit considered.

## Accessibility

- [ ] Keyboard path works.
- [ ] Focus states are visible.
- [ ] Screen reader labels are present where relevant.
- [ ] Contrast and motion concerns considered.

## Operations

- [ ] Logs/metrics are adequate.
- [ ] Rollback path documented.
- [ ] Migration/deployment risk reviewed.

## Human review

- [ ] Diff read by a human.
- [ ] CI result inspected.
- [ ] PR description includes verification evidence.
