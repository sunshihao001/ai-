---
name: ai-workflow-review-qa
description: "Use before merge or completion. Checks spec alignment, tests, Playwright QA, accessibility, security, architecture, and human-review readiness."
version: 1.0.0
author: Curated from superpowers verification/code-review, spec-kit analyze/checklist, and mattpocock review
license: MIT
---

# AI Workflow: Review / QA Gate

## Purpose
Prevent "agent says done" from becoming real completion.

## Review Areas
1. Spec alignment: does the code satisfy the documented goal and non-goals?
2. Scope control: are unrelated changes included?
3. Tests: do tests cover the behavior and fail without the fix?
4. Playwright / E2E: are user-facing paths verified?
5. Accessibility: keyboard, labels, contrast, focus states, semantic HTML where applicable.
6. Security: auth, authorization, input validation, secrets, dependency risk, logging.
7. Architecture: is the solution simple, local, and consistent with existing patterns?
8. Maintainability: can a human explain the diff?

## Required PR Evidence
- Summary
- Linked issue/spec
- Verification commands and results
- Screenshots / Playwright evidence if UI
- Accessibility notes
- Security notes
- Risks
- Rollback

## Stop Conditions
Block completion when acceptance criteria are not objectively checked, tests are missing without explanation, security-sensitive code was changed without review, the diff includes unrelated rewrites, or the agent cannot explain why the code has its shape.
