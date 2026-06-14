---
name: ai-workflow-tdd
description: Use when behavior can be verified by tests. Enforce red-green-refactor and prevent unverified coding completion.
---

# AI Workflow: TDD

Derived from Matt Pocock `tdd` and Superpowers `test-driven-development`.

## Process
1. Identify behavior and acceptance criteria.
2. Write or update a failing test first.
3. Run it and record the failure.
4. Implement the minimal fix.
5. Run test suite until green.
6. Refactor only after green.
7. Add regression tests for bugs.

## Rules
- Never fake tests to pass.
- Do not delete meaningful tests to get green.
- If a test cannot be written, explain why and propose another verification method.
