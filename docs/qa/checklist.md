# QA Checklist

Use this as the final gate before merging AI-generated or AI-assisted work.

## Product / Spec

- [ ] Linked issue is clear.
- [ ] Linked spec exists for non-trivial work.
- [ ] Acceptance criteria are satisfied.
- [ ] Non-goals were not implemented accidentally.

## Code

- [ ] Diff is understandable.
- [ ] No unrelated formatting churn.
- [ ] No hidden broad rewrites.
- [ ] Complexity is justified.

## Tests

- [ ] Unit tests pass.
- [ ] Integration tests pass where applicable.
- [ ] Regression tests exist for bugs.
- [ ] Tests fail on the old behavior where practical.

## Playwright / E2E

- [ ] Critical path tested.
- [ ] Screenshots/traces reviewed when UI changed.
- [ ] Mobile/responsive state checked if relevant.

## Accessibility

- [ ] Keyboard-only path works.
- [ ] Interactive controls have accessible names.
- [ ] Focus states are visible.
- [ ] Color contrast is acceptable.
- [ ] No obvious ARIA misuse.

## Security

- [ ] No secrets in code, logs, screenshots, or fixtures.
- [ ] User input is validated/encoded.
- [ ] Auth and permission boundaries reviewed.
- [ ] Dependency changes reviewed/audited.
- [ ] Dangerous operations have guards and rollback.

## Operations

- [ ] Logs are useful but not sensitive.
- [ ] Migrations are reversible or documented.
- [ ] Rollback path is documented.
- [ ] Monitoring/alerts considered for production-impacting changes.

## Human Review

- [ ] I read the diff.
- [ ] I understand why the code has this shape.
- [ ] I can explain the tradeoffs.
