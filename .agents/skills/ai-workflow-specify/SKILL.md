---
name: ai-workflow-specify
description: Use after requirements are clarified to produce production-grade spec, plan, tasks, checklist, ADRs, and GitHub issue slices.
---

# AI Workflow: Specify

Derived from GitHub Spec Kit `specify`/`plan`/`tasks`/`checklist`, Matt Pocock `to-prd`/`to-issues`, and Superpowers `writing-plans`.

## Goal
Turn discussion into executable, reviewable project artifacts.

## Required files per feature
Create `specs/<feature>/` containing:
- `spec.md` — problem, scope, non-scope, user stories, acceptance criteria
- `plan.md` — technical approach, files/modules, risks, rollback
- `tasks.md` — vertical slices, dependencies, owner/agent hints
- `checklist.md` — verification checklist

## Guidelines
- Prefer vertical slices over horizontal layers.
- Each task should map to one GitHub issue when practical.
- Include test expectations and QA/a11y/security checks.
- Capture major decisions in `docs/adr/`.

## Output quality bar
A coding agent should be able to implement one issue without relying on chat history.
