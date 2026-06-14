---
name: ai-workflow-brainstorm-grill
description: "Use when a request is vague, risky, or product-facing. Brainstorm against the existing repo, then grill assumptions until the requirement is clear enough to become a spec or issue."
version: 1.0.0
author: Curated from superpowers, spec-kit, and mattpocock/skills
license: MIT
---

# AI Workflow: Brainstorm + Grill

## Purpose
Prevent the agent from implementing the wrong thing. This skill combines Superpowers `brainstorming`, Matt Pocock `grill-me` / `grill-with-docs`, and Spec Kit `clarify`.

## Process
1. Restate the user's idea in one paragraph.
2. Inspect relevant repo context before proposing implementation.
3. Ask questions about user, success, non-goals, existing behavior, edge cases, permissions, security, accessibility, data, migration, testing, and acceptance.
4. Challenge assumptions with "what if" questions until new questions stop changing the design.
5. Record new project language in `CONTEXT.md`.
6. Produce decisions, open questions, risks, and acceptance criteria draft.

## Output Template
```md
# Requirement Interrogation Summary
## Restated Goal
## Existing Repo Context
## Decisions Made
## Open Questions
## Risks
## Acceptance Criteria Draft
## Suggested Next Artifact
```

## Stop Condition
Do not proceed to implementation until acceptance criteria are testable and unresolved questions are either answered or explicitly deferred.
