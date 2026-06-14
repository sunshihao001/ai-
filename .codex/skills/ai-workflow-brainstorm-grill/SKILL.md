---
name: ai-workflow-brainstorm-grill
description: "Use when a request is vague, risky, product-facing, or needs routing into an agent loop. Combine brainstorming, requirement grilling, repo-doc grilling, spec clarification, owner authority, and verification lenses into one Demand Grilling Brief."
version: 1.1.0
when_to_use: "Before spec writing, GitHub issue creation, Codex handoff, or maintainer-orchestrator delegation when the ask is ambiguous, risky, product-facing, or needs maker/checker loop routing."
---

# AI Workflow: Demand Grilling Control Gate

## Purpose

Prevent the agent from implementing the wrong thing and prevent loop agents from running without a control plane. This skill combines:

- Superpowers `brainstorming`,
- Matt Pocock `grill-me` / `grill-with-docs`,
- Spec Kit `clarify`,
- `dbs-good-question`,
- maintainer-orchestrator classification,
- review/verification gate thinking.

The output is not a giant questionnaire. The output is one **Demand Grilling Brief** that makes the ask agent-usable, criticizable, verifiable, and routable.

## Process

1. **Restate the ask.** Capture the user's raw intent without inventing missing facts.
2. **Challenge the goal.** Ask whether the proposed solution is the real goal or only one possible approach.
3. **Inspect available context.** Use AGENTS.md, CONTEXT.md, specs, ADRs, issues, PRs, tests, and current repo behavior when present.
4. **Clarify boundaries.** Identify users, operators, scope, non-goals, edge cases, and must-not-change behavior.
5. **Classify assumptions and risks.** Mark assumptions as `confirmed`, `unconfirmed`, or `risky`; include security, privacy, accessibility, operations, cost, and performance where relevant.
6. **Define verification.** Convert done into objective evidence: commands, tests, CI links, Playwright/manual QA, screenshots/traces, security/a11y checks, live proof.
7. **Classify execution.** Decide whether the work is `Autonomous`, `Needs owner`, or `Ignored by owner`.
8. **Set the loop control plane.** Define maker, checker, durable state, authority boundary, stop conditions, and blocker/owner-decision brief rules.
9. **Ask only high-value questions.** Prefer 1-3 questions that change scope, safety, routing, authority, or verification.
10. **Route to next artifact.** Choose more questions, spec, GitHub issue, Codex task, maintainer-orchestrator item, or owner decision brief.

## Skill Lenses

Use the right lenses; do not average all lenses every time.

- **Product idea:** brainstorming + grill-me + clarify + dbs-good-question.
- **Existing repo feature:** grill-with-docs + project context + clarify + review-quality gate.
- **Codex candidate:** dbs-good-question + spec-driven docs + codex-execution-loop + TDD verification.
- **Repo queue / multi-PR work:** maintainer-orchestrator + loop-orchestrator + GitHub handoff + owner decision brief.
- **High-risk work:** review-quality gate + security/a11y/ops + authority boundary + live proof / waiver.

## Output Template

Use `.ai/templates/good-question-brief.md`.

The brief must include:

```md
# Demand Grilling Brief

## 1. Original Ask
## 2. Improved Agent-Usable Question
## 3. Intent and Alternatives
## 4. Context and Constraints
## 5. Scope and Non-Goals
## 6. Assumptions and Risks
## 7. Acceptance Criteria
## 8. Verification Plan
## 9. Agent Execution Classification
## 10. Loop Stop Conditions
## 11. Critique Prompts
## 12. Missing High-Value Questions
## 13. Next Stage
```

## Stop Condition

The gate is complete when:

- a Demand Grilling Brief exists,
- the next stage is selected,
- unresolved questions are limited to the smallest high-value set,
- no implementation starts from raw ambiguous chat.

Stop and ask the owner when a missing answer changes safety, authority, scope, or verification.

## Pitfalls

- Do not implement from raw chat.
- Do not ask a huge generic questionnaire.
- Do not show a pile of skill outputs to the user; synthesize one brief.
- Do not let Codex receive vague chat history; give it a bounded issue/spec/checklist.
- Do not let a maker grade itself; define checker evidence before execution.
- Do not treat merge, release, destructive changes, secret access, or spending as implied by implementation permission.
