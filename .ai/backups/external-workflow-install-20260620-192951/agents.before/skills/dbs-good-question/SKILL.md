---
name: dbs-good-question
description: Use when the user has a vague, half-clarified, or cross-bot software/ops/product request and wants to turn it into an agent-reasonable, criticizable, verifiable problem statement before coding. Also trigger on '/dbs-good-question', '/好问题', '好问题生成器', '把问题变好', or '需求澄清端'.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [requirements, demand-grilling, spec-driven-development, ai-method-wheel, good-question]
    related_skills: [ai-method-wheel, maintainer-orchestrator, plan]
---

# DBS Good Question / 好问题生成器

## Purpose

Convert a vague request into a problem statement that an AI agent can reason about, criticize, implement, and verify.

This is the front-end of the user's AI method wheel. It should run before spec writing, Codex execution, or maintainer-orchestrator delegation when the request is still ambiguous.

## Core Output

Produce a **Question Brief** with these sections:

1. **Original Ask** — quote or summarize the user's raw request.
2. **Improved Question** — one precise question/task statement.
3. **Context Needed by an Agent** — repo, product, users, constraints, current state.
4. **Assumptions** — explicit assumptions, each marked `confirmed`, `unconfirmed`, or `risky`.
5. **Non-Goals** — what the agent must not do.
6. **Acceptance Criteria** — observable conditions for done.
7. **Verification Plan** — tests, CLI commands, Playwright/manual QA, security/a11y checks, CI evidence.
8. **Critique Prompts** — questions another agent/reviewer should ask to attack the plan.
9. **Missing Information** — ask the smallest number of high-value questions; prefer 1-3.
10. **Handoff Target** — whether this should become `spec`, `GitHub issue`, `Codex task`, `maintainer queue item`, or `owner decision brief`.

## Process

### 1. Classify the ambiguity

Identify which kind of ambiguity exists:

- **Goal ambiguity** — unclear desired outcome.
- **User ambiguity** — unclear user/operator/persona.
- **Scope ambiguity** — unclear boundaries and non-goals.
- **State ambiguity** — unclear current repo/system state.
- **Constraint ambiguity** — performance, security, compatibility, compliance, deployment, cost.
- **Verification ambiguity** — unclear how to prove done.
- **Authority ambiguity** — unclear whether the agent may edit, push, merge, deploy, delete, spend money, or access secrets.

### 2. Rewrite as an agent-usable task

The improved question should have this shape:

```text
Given <current state/context>, for <user/operator>, change/decide <specific target>, while preserving <constraints/non-goals>. Success means <objective acceptance criteria>. Verify by <specific checks>. If <blocked condition>, stop and ask <specific owner question>.
```

### 3. Make it criticizable

Add critique prompts such as:

- What assumption would make this fail?
- What simpler interpretation exists?
- What is the highest-risk file/module/system touched?
- What would be unsafe to automate?
- How could an agent falsely claim success?
- What proof would convince a skeptical maintainer?

### 4. Make it verifiable

Never accept “looks good” as done. Convert vague completion into evidence:

- command + exit code
- CI run link
- test name
- Playwright trace/screenshot
- diff summary
- log excerpt
- manual QA checklist
- a11y/security checklist
- owner decision brief if human judgment is required

### 5. Route to the next method-wheel stage

Choose one:

- `Need more questions` — ask only the most important missing question(s).
- `Ready for spec` — create/append `specs/<feature>/spec.md`.
- `Ready for GitHub issue` — turn into a vertical-slice issue.
- `Ready for Codex` — bounded implementation task with exact files/spec/checklist.
- `Ready for maintainer-orchestrator` — classify as autonomous/needs-owner/ignored.
- `Ready for owner decision` — prepare owner decision brief.

## Response Style

Be concise but structured. Prefer bullets and labeled fields. Do not over-ask. If the user is trying to transfer context to another bot, include a copy-paste block.

## Copy-Paste Handoff Template

```md
# Good Question Brief

## Original Ask

## Improved Question
Given ..., for ..., change/decide ..., while preserving .... Success means .... Verify by .... If blocked, ask ....

## Context Needed
- Repo/system:
- Current state:
- Existing discussion summary:
- Constraints:

## Assumptions
- [unconfirmed] ...

## Non-Goals
- ...

## Acceptance Criteria
- ...

## Verification Plan
- ...

## Critique Prompts
- What assumption is weakest?
- What proof would catch a false success claim?
- What security/a11y/ops risk exists?

## Missing Questions
1. ...

## Next Stage
Ready for: spec / issue / Codex / maintainer-orchestrator / owner decision
```

## Pitfalls

- Do not write code from a vague ask.
- Do not create a giant questionnaire; ask the few questions that change execution.
- Do not keep important decisions only in chat; route durable state to GitHub/repo docs.
- Do not let Codex receive raw, ambiguous chat history; give it a bounded question/spec/issue.
