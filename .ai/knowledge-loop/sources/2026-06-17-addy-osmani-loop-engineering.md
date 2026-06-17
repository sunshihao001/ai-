# Source Note — Addy Osmani: Loop Engineering

## Metadata

- Source ID: 2026-06-17-addy-osmani-loop-engineering
- Title: Loop Engineering
- Author: Addy Osmani
- URL: https://addyosmani.com/blog/loop-engineering/
- Published: 2026-06-07
- Captured at: 2026-06-17
- Source type: expert article / primary referenced source
- Quality level: S2
- Processing status: extracted

## Why this source matters

Yanhua's X article explicitly references Addy Osmani's Loop Engineering post. Addy's article provides a stronger framework for the repository's method wheel: loops are systems that find work, assign it to agents, check results, record progress, and decide the next step.

## Core claims

1. Loop engineering is replacing yourself as the person who prompts the agent: you design the system that prompts it instead.
2. A loop is a recursive AI workflow: define purpose/goal, iterate until completion.
3. A loop finds work, hands it to agents, checks results, records progress, decides the next step, and repeats.
4. Loop engineering sits above harness engineering, factory model, plugins/connectors, skills, worktrees, and sub-agents.
5. Operators should build loops while remaining engineers, not passive button-pressers.
6. Token/cost and review bandwidth are real constraints.

## Evidence / examples

Addy identifies five primitives plus memory/state:

- Automations: heartbeat, schedules, work discovery.
- Worktrees: isolate parallel agent work.
- Skills: reusable project knowledge and intent outside conversation.
- Plugins/connectors: tool access beyond filesystem.
- Sub-agents: specialized makers/checkers.
- Memory/state: records progress and enables continuation.

Key quoted ideas from extracted article summary:

- "Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."
- "Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go."
- Maker/checker separation matters because the model that wrote the code is too nice grading its own homework.

## Concepts extracted

| Concept | Explanation | Evidence strength | Candidate target |
| --- | --- | --- | --- |
| Recursive AI workflow | Goal-driven repeated execution until completion. | S2 | loop-orchestrator |
| Automations | Heartbeat/schedule/discovery layer. | S2 | A-port loop state |
| Worktrees | Isolation for parallel agent work. | S2 | D/Codex execution |
| Skills | Reusable project intent outside chat. | S2 | skills/templates |
| Plugins/connectors | Tools that let loops see issues, CI, APIs, messages. | S2 | Hermes gateway / OpenCLI |
| Sub-agents | Specialized maker/checker roles. | S2 | multi-port contracts |
| Memory/state | Durable record of progress and next steps. | S2 | `.ai/knowledge-loop/loop-state.yaml` |

## Fit to current Knowledge Frame

| Current frame module | Fit | Notes |
| --- | --- | --- |
| AI Method Wheel | Strong | Validates loop engineering as control layer above prompt engineering. |
| Multi-port contracts | Strong | Maps sub-agents to A/B/C/D/E/F ports. |
| A↔B double-gate loop | Strong | B source packs and A gates are loop primitives. |
| Knowledge Loop | Strong | Knowledge loop itself is a loop with memory/state and decisions. |
| Codex/Hermes orchestration | Strong | Worktrees, skills, connectors, sub-agents align with Hermes→Codex model. |

## Risks / caveats

- Loop engineering is early; token costs can explode.
- Review bandwidth remains a ceiling even when worktrees isolate agents.
- Loops should not replace engineering judgment.

## Recommended decision

ACCEPT

Use this source as a primary framework source for loop engineering in the method wheel, especially the primitives: automation, worktree, skills, connectors, sub-agents, and memory/state.

## Raw excerpt / summary

Extracted summary says Loop Engineering is about building a system that finds work, hands it to agents, checks results, writes down what is done, decides next steps, and repeats, rather than the user manually prompting agents turn by turn.
