---
name: ai-workflow-brainstorm-grill
description: Use when a requirement, feature, bug, or ops request is still ambiguous. Brainstorm against the repo, grill assumptions, clarify missing constraints, and update shared docs before implementation.
---

# AI Workflow: Brainstorm + Grill

Derived from Superpowers `brainstorming`, Matt Pocock `grill-me`/`grill-with-docs`, and Spec Kit `clarify`.

## Goal
Prevent agents from implementing vague or wrong requirements.

## Process
1. Restate the request in concrete language.
2. Inspect relevant repo context before proposing implementation.
3. Ask hard questions about user/use case, non-goals, edge cases, data/security/privacy, accessibility, failure modes, compatibility, observability, and operations.
4. Challenge assumptions until questions repeat or no longer change the plan.
5. Write outcomes to durable repo docs.

## Output
- Clarified requirement summary
- Open questions
- Accepted tradeoffs
- Non-goals
- Proposed acceptance criteria
- `CONTEXT.md` updates if shared language changed
- ADR candidate if a decision matters

## Stop condition
Do not proceed to coding until acceptance criteria and non-goals are explicit.
