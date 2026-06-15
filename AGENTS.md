# AGENTS.md — AI Method Wheel Project Instructions

This repository is configured for an AI-assisted software engineering workflow. Agents should treat GitHub files as the project source of truth and chats as temporary working context.

## Core Principle
Do not jump from vague request to code. Use this loop:

1. Design the loop if the task may run repeatedly or involve multiple agents.
2. Run the demand-grilling control gate: combine brainstorming, grill-me, grill-with-docs, clarify, dbs-good-question, maintainer-orchestrator, and verification lenses into one Demand Grilling Brief.
3. Convert decisions into production documents.
4. Split into user stories / issues.
5. Implement with Codex or a coding agent as maker.
6. Verify with a separate checker, tests, Playwright, accessibility, security, and human review.
7. Record decisions in GitHub: specs, ADRs, issues, PRs.
8. If the workflow failed, repair the harness and capture a regression.

## Required Reading Order for Agents
Before editing code, read:

1. `AGENTS.md`
2. `.ai/methods/ai-method-wheel.md`
3. `.ai/methods/demand-grilling-control-gate.md` when the ask is vague, risky, product-facing, or needs agent-loop routing
4. Relevant `specs/<feature>/spec.md`, `plan.md`, `tasks.md`, `checklist.md`
5. Relevant GitHub issue
6. Existing tests and CI configuration

## Work Rules
- Ask clarifying questions when the goal, acceptance criteria, or risk is unclear.
- For vague/risky/product-facing asks, produce a Demand Grilling Brief before spec, issue, Codex, or maintainer-orchestrator handoff.
- The Demand Grilling Brief must cover intent, context, scope, assumptions, risks, acceptance criteria, verification, execution classification, maker/checker split, authority boundary, stop conditions, critique prompts, missing high-value questions, and next stage.
- For looped or multi-agent work, define maker, checker, durable state, stop condition, and budget before running.
- Prefer vertical slices over technical-layer tasks.
- Do not expand scope beyond the issue/spec.
- For implementation tasks, use TDD when practical: failing test → minimal code → passing test → refactor.
- Run available checks before claiming completion.
- Do not mark work complete unless there is objective verification.
- Never commit secrets, tokens, `.env` files, credentials, or private keys.

## Recommended Verification
Use what exists in the project. Typical commands may include:

```bash
npm test
npm run lint
npm run typecheck
npx playwright test
```

If a command does not exist, report that honestly and propose the closest available check.

## GitHub as Source of Truth
Long-lived project state belongs in:

- `CONTEXT.md` — shared project language and domain concepts
- `specs/` — feature specs, plans, tasks, checklists
- `docs/adr/` — architecture decisions
- GitHub Issues — user stories / vertical slices
- Pull Requests — implementation record and verification results

Chat logs are not the project memory.
