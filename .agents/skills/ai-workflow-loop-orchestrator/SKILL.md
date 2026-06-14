---
name: ai-workflow-loop-orchestrator
description: Use when designing or operating an AI engineering loop that coordinates makers, checkers, Codex workers, GitHub issues/PRs, CI, QA, and durable state. Applies loop-engineering safeguards: separate checker, explicit stop conditions, disk/GitHub state, budget caps, and decision-ready owner asks.
---

# AI Workflow Loop Orchestrator

This is the control-plane skill for the AI method wheel. It does **not** perform substantial repository work itself. It inspects, classifies, delegates, monitors, asks for owner decisions only when decision-ready, and reports.

## Core principle

Do not manually prompt agents forever. Design a loop that prompts agents, checks their output, records state, and stops when a verifiable condition is met.

A safe loop has:

1. **Trigger** — manual, scheduled, GitHub event, issue, PR, failing CI, failing trace.
2. **Maker** — Codex/worker that produces the work.
3. **Checker** — separate model/tool/human that grades the output.
4. **Durable state** — files, GitHub issues, PRs, checklists, CI logs. Not just chat context.
5. **Stop condition** — explicit pass/fail rule, max iterations, and budget cap.
6. **Evidence** — tests, lint, typecheck, Playwright, a11y, security, logs, screenshots.
7. **Owner decision brief** — only when autonomous work is done or truly blocked.

## When to use

Use this skill when the user asks to:

- build an AI coding workflow,
- run multiple agents,
- improve the method wheel,
- coordinate Codex work from GitHub issues,
- triage a repo queue,
- design long-running loops,
- keep state across sessions,
- decide what should be automated vs human-reviewed.

## Do not use for

- one-off trivial prompts,
- fuzzy product strategy with no checkable outcome,
- destructive production actions,
- auth/payments/security-sensitive changes without human approval,
- tasks where nobody will read the diff.

## Loop shape

```text
Discover/trigger
→ classify work
→ prepare spec/issue/checklist
→ delegate maker worker
→ run tests/tools
→ separate checker reviews
→ maker fixes findings
→ repeat until stop condition
→ owner decision brief or merge
→ record regression/lesson
```

## Work classification

Classify every item before delegation:

### Autonomous

Clear, bounded, reproducible, has a verification path.

Examples:
- CI failure triage,
- dependency bump PRs,
- lint/typecheck fixes,
- missing tests,
- small bug with reproduction,
- docs sync from existing source.

### Needs owner

Requires judgment or access:
- product choice,
- security/privacy decision,
- irreversible/destructive action,
- unavailable credentials,
- live proof requiring a human account/device,
- ambiguous “done”.

### Ignored by owner

Only if explicitly stated by owner. Do not mark stale/difficult items as ignored by yourself.

## Delegation rules

The orchestrator may create or assign workers. Workers must not create subworkers.

Every worker prompt must include:

```text
You are a repository worker. Do not create subworkers or delegate.
Work only on the assigned issue/spec.
Read AGENTS.md, CONTEXT.md, relevant specs, and QA checklist.
Produce a PR-ready change with tests and verification evidence.
If blocked, finish all autonomous work first, then report the exact remaining blocker.
```

## Maker/checker separation

Never let the maker be the only judge of completion.

- Maker: implements or edits.
- Checker: reviews diff, tests, QA checklist, and spec alignment.
- Human: reads important diffs and makes judgment-heavy decisions.

Checker findings become the next maker instruction.

## Stop conditions

Set before the loop starts:

- max iterations, e.g. 2 or 3,
- token/time/budget cap,
- required deterministic checks,
- final separate checker pass,
- no-progress/diff-size guard.

Example:

```text
Stop after at most 2 maker/checker loops.
Success requires: tests pass, lint clean, typecheck clean, checklist complete, checker finds no major issue.
If still failing after 2 loops, stop and write a blocker brief.
```

## Durable state

State must live in the repository/GitHub, not only in chat.

Prefer:

- `specs/<feature>/spec.md`,
- `specs/<feature>/plan.md`,
- `specs/<feature>/tasks.md`,
- `specs/<feature>/checklist.md`,
- GitHub issues,
- PR descriptions,
- CI runs,
- `docs/adr/*.md`,
- `docs/qa/checklist.md`,
- regression tests.

## Decision-ready owner ask

Do not ask the owner from a raw issue or rough branch. Before asking:

1. Refresh current PR/issue/CI state.
2. Finish code, tests, docs, review, and CI if possible.
3. Prepare alternatives and tradeoffs.
4. Ask only the exact remaining decision.

A good owner brief contains:

```text
Decision needed:
Recommended default:
Alternatives:
Evidence:
Risk:
Rollback:
Exact action requested:
```

## Harness repair loop

When the AI workflow itself fails, repair the harness, not just the output.

```text
Bad run/trace/failure
→ diagnose root cause
→ patch prompt/skill/tool/checklist
→ replay the exact failing input if possible
→ lock regression as test/checklist item
→ document the lesson
```

## Good first loops

Start with boring, repetitive, reviewable work:

- CI failure diagnosis,
- stale dependency review,
- lint/typecheck fixes,
- missing tests for a touched module,
- Playwright smoke checks,
- docs drift checks,
- issue-to-PR drafts on well-tested code.

Avoid early automation for:

- architecture rewrites,
- vague product work,
- auth/payments/security-sensitive code,
- production deploys,
- anything where done is mostly judgment.
