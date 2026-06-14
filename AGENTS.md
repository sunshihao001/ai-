# AGENTS.md — AI Method Wheel Project Instructions

This repository is configured for an AI-assisted software engineering workflow. Agents should treat GitHub files as the project source of truth and chats as temporary working context.

## Core Principle
Do not jump from vague request to code. Use this loop:

1. Interrogate the idea.
2. Convert decisions into production documents.
3. Split into user stories / issues.
4. Implement with Codex or a coding agent.
5. Verify with tests, Playwright, accessibility, security, and human review.
6. Record decisions in GitHub: specs, ADRs, issues, PRs.

## Required Reading Order for Agents
Before editing code, read:

1. `AGENTS.md`
2. `.ai/methods/ai-method-wheel.md`
3. Relevant `specs/<feature>/spec.md`, `plan.md`, `tasks.md`, `checklist.md`
4. Relevant GitHub issue
5. Existing tests and CI configuration

## Work Rules
- Ask clarifying questions when the goal, acceptance criteria, or risk is unclear.
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
