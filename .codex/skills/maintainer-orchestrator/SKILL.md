---
name: maintainer-orchestrator
description: "Use when coordinating repository maintenance through workers, PR queues, CI, owner decision briefs, and releases."
---

# Maintainer Orchestrator — Codex Adaptation

This is the Codex-facing adaptation of Peter Steinberger's Maintainer Orchestrator skill. Treat the upstream copy in `.agents/skills/maintainer-orchestrator/SKILL.md` and `.ai/external/steipete-agent-scripts/maintainer-orchestrator/SKILL.md` as the reference.

## Role

Codex is usually a repository worker, not the root orchestrator.

When acting as a worker:

- Work only on the assigned repository, issue, PR, or spec.
- Do not create subworkers or delegate to other agents.
- Read `AGENTS.md`, `CONTEXT.md`, relevant `specs/`, the GitHub issue/PR discussion, and relevant code before changing files.
- Stay inside the granted authorization boundary: local edit, push, CI repair, merge, close, release are separate permissions.
- Prefer repairing an existing PR when possible; preserve contributor credit.
- Add regression coverage when appropriate.
- Run focused tests, broader checks, live proof where applicable, and report exact commands/results.
- Stop at the last authorized boundary and request the exact next permission.

When acting as root orchestrator, use the full upstream skill and keep the coordinator thread lightweight:

```text
inspect → classify → delegate → monitor → decision brief → report
```

## Decision-Ready Rule

Do not ask the owner from a rough issue or half-fixed PR. Prepare the work first:

- inspect/reproduce/root cause;
- implement bounded candidate when autonomous;
- add tests/docs/changelog where relevant;
- run live proof / CI / review gates;
- push branch or prepare PR if authorized;
- ask only for the exact remaining decision/access/waiver/land/delete action.

## Owner Decision Brief

Every owner question must include:

- full canonical URL and title;
- what changes and who benefits;
- why a decision is needed now;
- completed proof: reproduction, tests, live proof, autoreview, CI, mergeability as applicable;
- tradeoffs, residual risks, missing evidence;
- recommendation and rationale;
- exact choices and consequences.

## Mapping to This Repo's AI Method Wheel

Use with:

- `.agents/skills/ai-workflow-loop-orchestrator/SKILL.md` for loop control-plane design.
- `.agents/skills/ai-workflow-codex-issue/SKILL.md` for worker execution.
- `.agents/skills/ai-workflow-review-qa/SKILL.md` for proof gates.
- `.ai/templates/owner-decision-brief.md` for decision requests.
- `.ai/templates/loop-run.md` for durable loop state.
