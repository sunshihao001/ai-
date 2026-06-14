---
name: ai-workflow-tdd
description: "Use when implementing or fixing code where behavior can be tested. Requires red-green-refactor and prevents unverified completion."
version: 1.0.0
author: Curated from mattpocock/skills tdd and superpowers test-driven-development
license: MIT
---

# AI Workflow: TDD

## Process
1. Identify the behavior from the spec or issue.
2. Write or update the smallest meaningful test first.
3. Run the test and confirm it fails for the expected reason.
4. Implement the minimal code to pass.
5. Run the test again.
6. Refactor only after green.
7. Run broader relevant checks.

## If TDD Is Not Practical
Explain why, then create the closest verification: snapshot before/after, integration test, Playwright path, script-based smoke test, or manual reproduction steps.

## Never Do
- Do not write implementation first and invent tests afterward without saying so.
- Do not mark completion based only on code inspection.
- Do not weaken tests to make them pass.
