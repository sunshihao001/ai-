# Latest AI Methodology Sources

This file records external methodology inputs that informed the AI method wheel. It is a working research ledger, not a verbatim archive.

## 2026-06 Loop Engineering Inputs

### Avi Chawla / Karpathy leverage thread

Source: `https://x.com/_avichawla/status/2065727218991735000`

Key ideas:

- Remove the human as the bottleneck for every next prompt.
- Loop engineering moves two manual steps into the system:
  - deciding what the agent runs next,
  - checking the output before the next step.
- Core loop structure:
  - schedule/trigger,
  - maker loop,
  - separate checker agent,
  - durable state on disk,
  - done/max-iterations/budget exit.
- The maker should not grade itself.
- State must live on disk/GitHub, not only in context.
- Lower verification bar means safer loop.
- Green tests do not mean humans understand what shipped; someone must still read important diffs.
- Harnesses drift as models/tools/prompts change; harness repair needs its own loop.

Method-wheel impact:

- Added `ai-workflow-loop-orchestrator`.
- Added maker/checker separation.
- Added explicit stop conditions and durable state requirements.

### Akshay Pachaar / Self-repairing harness

Source: `https://x.com/akshay_pachaar/status/2064051835636498924`

Key ideas from accessible summaries:

- Observability traces show what the agent did, but not automatically why it failed or how to prevent recurrence.
- Production agent workflow should close the right-half loop:
  - bad trace,
  - root cause diagnosis,
  - proposed fix,
  - approval,
  - replay original failing input,
  - lock as regression test.
- Harness engineering is ongoing; failures should improve the harness, not just the current artifact.

Method-wheel impact:

- Added Phase 5: Harness Repair / Method Improvement.
- Added harness repair notes to loop template.

### Hamza Khalid / Stop prompting, build loops

Source: `https://x.com/humzaakhalid/status/2064996712910041409`

Key ideas from accessible metadata and related loop-engineering summaries:

- The shift is from prompt-by-prompt operation to no-code or low-code loop systems.
- The practical implementation should start small and use repeatable, reviewable tasks.

Method-wheel impact:

- Good first loops list: CI triage, docs drift, lint/typecheck, dependency review.

### Omar Sar / Autonomous long-running coding agents

Source: `https://x.com/omarsar0/status/2065880971031834786`

Key ideas from accessible metadata:

- Autonomous coding is moving from better prompting to better control systems.
- Engineers wrap agents in goals, evaluators, loops, and artifacts.

Method-wheel impact:

- Reinforced goal/evaluator/artifact structure.

### Jason Liu / Getting the most out of Codex

Source: `https://x.com/jxnlco/status/2057153744630890620`

Key ideas from accessible metadata:

- Codex is not only for raw code generation; much of the value comes from repository inspection, diffs, tests, and PR workflow.
- Codex should receive repository artifacts and bounded tasks, not vague chat context.

Method-wheel impact:

- Codex remains maker/executor.
- GitHub issues/specs/AGENTS.md remain the handoff interface.

### Cursor / Scaling long-running autonomous coding

Source: `https://cursor.com/blog/scaling-agents`

Key ideas:

- Single agents work well for focused tasks but struggle with large ambiguous projects.
- Flat self-coordination through shared files/locks creates bottlenecks and fragility.
- With no hierarchy, agents become risk-averse and churn on small safe changes.
- Planner/worker separation works better:
  - planners explore and create tasks,
  - workers focus on completing tasks,
  - hierarchy beats flat peer coordination.
- Too little structure causes conflict/drift; too much structure causes fragility.

Method-wheel impact:

- Added loop-orchestrator as control plane.
- Workers are not allowed to create subworkers.
- Planner/orchestrator prepares tasks; Codex workers execute bounded issues.

### Firecrawl / Loop engineering

Source: `https://www.firecrawl.dev/blog/loop-engineering`

Key ideas:

- Prompt engineering optimizes one turn; loop engineering optimizes a system.
- A loop needs trigger, state, verification, and halt logic.
- Tasks should be repetitive, reviewable, and valuable before becoming loops.
- Safeguards:
  - hard iteration ceiling,
  - no-progress/diff check,
  - token/dollar cap.
- Open loops are powerful but expensive/risky; closed loops are safer for production.

Method-wheel impact:

- Added loop candidate criteria.
- Added stop condition and budget cap template.

### steipete / Maintainer Orchestrator

Source: `https://github.com/steipete/agent-scripts/blob/main/skills/maintainer-orchestrator/SKILL.md`

Key ideas:

- A maintainer orchestrator is a control-plane skill: inspect, delegate, monitor, ask decisions, report.
- Substantial repository work belongs in repository worker threads, not the orchestrator.
- Classify items:
  - Autonomous,
  - Needs owner,
  - Ignored by owner.
- Only root orchestrator manages delegation; workers do not subdelegate.
- Do not ask owner from rough issues/branches; prepare decision-ready PRs first.
- Ask only for exact remaining blockers: credential, access, product choice, waiver, land/delete.

Method-wheel impact:

- Added work classification.
- Added owner decision brief template.
- Added no-subdelegation worker rule.

## Current Synthesis

The method wheel now treats AI software engineering as a layered system:

```text
Human engineering judgment
→ loop/control-plane design
→ requirement grilling
→ spec/issue artifacts
→ Codex maker workers
→ separate checker review
→ CI/QA/security/a11y evidence
→ GitHub PR memory
→ harness repair and regression capture
```

The core workflow remains human-in-the-loop, but the human should operate at the level of loop design, decision-making, and diff judgment instead of hand-prompting every agent step.
