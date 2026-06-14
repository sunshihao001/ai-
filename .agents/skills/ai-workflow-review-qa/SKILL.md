---
name: ai-workflow-review-qa
description: Use before PR/merge to verify spec alignment, tests, Playwright/E2E, accessibility, security, architecture, and human review readiness.
---

# AI Workflow: Review + QA

Derived from Superpowers `verification-before-completion`/`requesting-code-review`, Matt Pocock `review`/`improve-codebase-architecture`, and Spec Kit `analyze`/`checklist`.

## Review gates
- Spec alignment: implements the stated issue only.
- Tests: unit/integration/e2e relevant to the change.
- Playwright QA: critical user paths if UI is affected.
- Accessibility: keyboard, labels, contrast, semantics if UI is affected.
- Security: auth, injection, secrets, dependencies, permissions.
- Architecture: no unnecessary complexity or muddy boundaries.
- Operations: logging, rollback, monitoring when applicable.

## Output
- Pass/fail checklist
- Verification command outputs
- Risks and follow-ups
- PR-ready summary
