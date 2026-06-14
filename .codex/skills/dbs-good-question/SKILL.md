---
name: dbs-good-question
description: Use when the user has a vague, half-clarified, or cross-bot software/ops/product request and wants to turn it into an agent-reasonable, criticizable, verifiable Demand Grilling Brief before coding. Also trigger on '/dbs-good-question', '/好问题', '好问题生成器', '把问题变好', or '需求澄清端'.
version: 1.1.0
when_to_use: "Before spec writing, GitHub issue creation, Codex handoff, or maintainer-orchestrator delegation when the ask is ambiguous, risky, product-facing, or needs maker/checker loop routing."
---

# DBS Good Question / 好问题生成器

## Purpose

Convert a vague request into a problem statement that an AI agent can reason about, criticize, implement, verify, and route into the correct loop.

This is the front-end control gate of the AI Method Wheel. It should run before spec writing, Codex execution, or maintainer-orchestrator delegation when the request is still ambiguous.

## Core Output

Produce a **Demand Grilling Brief** with these sections:

1. **Original Ask** — quote or summarize the user's raw request.
2. **Improved Agent-Usable Question** — one precise task/decision statement.
3. **Intent and Alternatives** — true goal, whether the proposed solution is only an implementation idea, simpler/safer options.
4. **Context and Constraints** — repo, product, users, current state, docs, risky modules, constraints.
5. **Scope and Non-Goals** — what to do, what not to do, what must not change.
6. **Assumptions and Risks** — explicit assumptions marked `confirmed`, `unconfirmed`, or `risky`.
7. **Acceptance Criteria** — observable conditions for done.
8. **Verification Plan** — tests, CLI commands, Playwright/manual QA, security/a11y checks, CI evidence, live proof if needed.
9. **Agent Execution Classification** — `Autonomous`, `Needs owner`, or `Ignored by owner`; handoff target and authority boundary.
10. **Loop Stop Conditions** — maker/checker limits, budget, success condition, no-progress guard, blocker brief rule.
11. **Critique Prompts** — questions another agent/reviewer should ask to attack the plan.
12. **Missing High-Value Questions** — ask the smallest number of questions that change scope, safety, routing, authority, or verification; prefer 1-3.
13. **Next Stage** — `more questions`, `spec`, `GitHub issue`, `Codex`, `maintainer-orchestrator`, or `owner decision`.

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
- **Loop ambiguity** — unclear maker, checker, durable state, stop condition, or blocker format.

### 2. Rewrite as an agent-usable task

```text
Given <current state/context>, for <user/operator>, change/decide <specific target>, while preserving <constraints/non-goals>. Success means <objective acceptance criteria>. Verify by <specific checks/evidence>. If blocked, ask <specific owner question>.
```

### 3. Use multiple lenses, not multiple giant outputs

Synthesize the useful parts of:

- brainstorming — challenge the goal and alternatives,
- grill-me — remove ambiguity,
- grill-with-docs — check against repo/docs/current behavior,
- clarify — convert open questions into spec decisions,
- maintainer-orchestrator — classify autonomous vs owner-needed and set authority,
- review/verification gate — define proof and false-success traps.

### 4. Make it criticizable and verifiable

Include critique prompts and evidence requirements:

- command + exit code,
- CI run link,
- test name,
- Playwright trace/screenshot,
- diff summary,
- log excerpt,
- manual QA checklist,
- a11y/security checklist,
- live proof or explicit waiver,
- owner decision brief if human judgment is required.

### 5. Route to the next method-wheel stage

Choose one:

- `Need more questions` — ask only the most important missing question(s).
- `Ready for spec` — create/append `specs/<feature>/spec.md`.
- `Ready for GitHub issue` — turn into a vertical-slice issue.
- `Ready for Codex` — bounded implementation task with exact files/spec/checklist.
- `Ready for maintainer-orchestrator` — classify as autonomous/needs-owner/ignored and prepare queue item.
- `Ready for owner decision` — prepare owner decision brief.

## Response Style

Be concise but structured. Prefer bullets and labeled fields. Do not over-ask. If the user is trying to transfer context to another bot, include a copy-paste block.

## Copy-Paste Handoff Template

Use `.ai/templates/good-question-brief.md`.

## Pitfalls

- Do not write code from a vague ask.
- Do not create a giant questionnaire; ask the few questions that change execution.
- Do not keep important decisions only in chat; route durable state to GitHub/repo docs.
- Do not let Codex receive raw, ambiguous chat history; give it a bounded question/spec/issue.
- Do not skip maker/checker, authority, stop condition, or verification evidence just because the product goal sounds clear.
