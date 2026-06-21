# AGENTS.md — AI Method Wheel Project Instructions

This repository is configured for an AI-assisted software engineering workflow. Agents should treat GitHub files as the project source of truth and chats as temporary working context.

## Core Principle
Do not jump from vague request to code. Use this loop:

1. Route through the existing front door first: use the current router / umbrella skill / repo pattern before inventing anything new.
2. Prefer bridge-over-build: reuse mature skills, workflows, and repo conventions whenever they already cover the need.
3. Design the loop if the task may run repeatedly or involve multiple agents.
4. Interrogate the idea.
5. Convert decisions into production documents.
6. Split into user stories / issues.
7. Implement with Codex or a coding agent as maker only after the reusable path is exhausted.
8. Verify with a separate checker, tests, Playwright, accessibility, security, and human review.
9. Record decisions in GitHub: specs, ADRs, issues, PRs.
10. If the workflow failed, repair the harness and capture a regression.
11. For repeated/generalizable failures, use a self-improving skill loop: collect feedback signals, propose a reviewable skill/template diff, and pass A/E protection gates before promotion.

## Required Reading Order for Agents
Before editing code, read:

1. `AGENTS.md`
2. `.ai/methods/ai-method-wheel.md`
3. Relevant `specs/<feature>/spec.md`, `plan.md`, `tasks.md`, `checklist.md`
4. Relevant GitHub issue
5. Existing tests and CI configuration

## Spec Spine
Use a Spec Kit-inspired artifact spine inside the broader AI Method Wheel. The spine is:

```text
constitution/governance → spec.md → clarification answers → plan.md → research/data/contracts/quickstart → tasks.md → checklists → E-port analyze → D/Codex bounded implementation → E-port verification → PR/ADR/handoff
```

- A-port owns intent, scope, non-goals, acceptance criteria, `[NEEDS CLARIFICATION]` markers, the spec persistence choice, and the autonomous A-mode route judgment.
- B-port supplies research/source evidence for `research.md` or source packs.
- C-port drafts theory, architecture, `plan.md`, data models, contracts, and quickstart artifacts.
- A/B/C are logical stages by default inside one control plane; do not split them into multiple physical bots unless the owner explicitly requests runtime separation.
- D-port lands bounded repo changes or Codex task slices; do not treat a broad implementation command as permission to expand scope.
- E-port runs read-only cross-artifact analysis before implementation and objective verification after implementation.
- F/owner approves broad persistence-model changes, baseline changes, risky governance changes, and broad execution scope.

Default spec persistence: use `spec-anchored + flow-forward` for method-wheel or baseline-changing work; use `spec-anchored + controlled flow-back` for normal repo implementation discoveries; use `spec-first` only for throwaway spikes.

## Work Rules
- Ask clarifying questions when the goal, acceptance criteria, or risk is unclear.
- When the owner uses a strong A-mode trigger, enter A-port logical-loop mode: infer the primary route, select the relevant skill family, avoid repeated multiple-choice loops, and ask only the next blocking question.
- For looped or multi-agent work, classify the loop layer (agent, verification, event-driven, or self-improvement), then define maker, checker, durable state, stop condition, and budget before running.
- Prefer vertical slices over technical-layer tasks.
- Do not expand scope beyond the issue/spec.
- For implementation tasks, use TDD when practical: failing test → minimal code → passing test → refactor.
- Run available checks before claiming completion.
- Do not mark work complete unless there is objective verification.
- Never commit secrets, tokens, `.env` files, credentials, or private keys.

## Harness Control Rules
- Treat the repo/GitHub/state files as truth; chat transcripts are evidence, not source of truth.
- Before sending input to a maker/model, classify whether it is an ordinary task, control command, state query, diagnostic, skill invocation, owner decision, or knowledge-frame update.
- Do not route tool side effects directly from model proposals to execution; apply path, permission, scope, and owner-policy checks first.
- Load markdown by context type: `AGENTS.md` as workspace instruction context, `SKILL.md` as task procedure context, specs as bounded task context, logs/transcripts as projected evidence.
- For long-running work, project context before each model call: preserve current state, selected evidence, and handles to full logs instead of blindly appending transcript.

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
- `.ai/knowledge-loop/dbs-content-system/` — single-directory content-structuring module for source packs, content units, topic maps, and assembly drafts
- GitHub Issues — user stories / vertical slices
- Pull Requests — implementation record and verification results

Chat logs are not the project memory.
