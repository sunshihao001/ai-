---
name: ai-workflow-specify
description: "Use when a clarified idea must become production documentation: spec, plan, tasks, checklist, ADR, and GitHub issues."
version: 1.0.0
author: Curated from spec-kit, superpowers, and mattpocock/skills
license: MIT
---

# AI Workflow: Specify / Plan / Tasks

## Purpose
Convert a clarified idea into durable GitHub/repo artifacts that a coding agent can execute.

## Required Outputs
Create:
```text
specs/<feature-slug>/
  spec.md
  plan.md
  tasks.md
  checklist.md
```
Add an ADR in `docs/adr/` if a significant architecture decision is made.

## Spec Structure
- Problem
- Users / actors
- Goals
- Non-goals
- User stories
- Functional requirements
- Edge cases
- Accessibility requirements
- Security requirements
- Acceptance criteria
- Test strategy
- Open questions

## Planning Rule
Use vertical slices. Avoid splitting only by technical layers.

## Checklist Must Include
- unit tests
- integration tests
- Playwright / E2E if UI-facing
- accessibility if UI-facing
- security review if auth/data/input/dependencies are touched
- manual review
