---
name: ai-workflow-review-qa
description: Use before PR completion to verify spec alignment, tests, Playwright flows, accessibility, security, architecture, and human-review readiness.
---

# AI Workflow: Review and QA Gate

## Inputs

- PR diff
- Linked issue
- Linked spec/plan/tasks/checklist
- CI results
- Playwright or E2E logs/screenshots when applicable

## Checklist

### Spec Alignment
- [ ] Implements the stated issue only.
- [ ] Meets acceptance criteria.
- [ ] Does not introduce unrelated changes.

### Test Quality
- [ ] Unit/integration tests cover changed behavior.
- [ ] Regression tests cover discovered bugs.
- [ ] Tests would fail without the implementation.

### UI / E2E
- [ ] Critical user paths verified with Playwright when UI changes.
- [ ] Screenshots or traces attached when useful.

### Accessibility
- [ ] Keyboard navigation still works.
- [ ] Labels, names, contrast, and focus states are checked.
- [ ] No obvious screen-reader regressions.

### Security
- [ ] No secrets committed or logged.
- [ ] Inputs validated.
- [ ] Authz/authn boundaries unchanged or explicitly reviewed.
- [ ] Dependencies audited when changed.

### Architecture
- [ ] No unnecessary abstraction.
- [ ] Module boundaries respected.
- [ ] Complexity did not increase without documented reason.

## Output

Return `PASS`, `PASS WITH FOLLOW-UPS`, or `BLOCKED`, with evidence.
