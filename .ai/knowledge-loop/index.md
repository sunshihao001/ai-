# Knowledge Reserve Index

This index tracks reusable learning sources and concepts absorbed into the AI Method Wheel.

## Active knowledge frames

| Frame | Status | Latest update | Notes |
| --- | --- | --- | --- |
| Multi-port loop agents | active | see `.ai/methods/multi-port-contracts/` | A/B/C/D/E/F port contracts |
| A↔B double-gate knowledge loop | active | see `.ai/methods/multi-port-contracts/a-b-double-gate-loop.md` | A controls frame, B supplies strategy/evidence |
| Loop Engineering / Ralph Loop | protected-learning | `frame-updates/2026-06-17-protective-loop-engineering-update.md` | Goal files, feedback, stop hooks, overbaking prevention with baseline protection |

## Source index

| ID | Source | Type | Quality | Status | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-06-17-yupi996-loop-engineering-ralph-overbaking | yupi996 X thread on Loop Engineering / Ralph / Overbaking | social thread | S3 | extracted | `sources/2026-06-17-yupi996-loop-engineering-ralph-overbaking.md` |
| 2026-06-17-pandatalk8-goal-loop-workflows | PandaTalk8 X article on Goal + Loop + Workflows | social article | S3 | extracted | `sources/2026-06-17-pandatalk8-goal-loop-workflows.md` |
| 2026-06-17-yanhua-design-loops-not-prompts | Yanhua X article on designing loops instead of prompts | social article | S3 | extracted | `sources/2026-06-17-yanhua-design-loops-not-prompts.md` |
| 2026-06-17-addy-osmani-loop-engineering | Addy Osmani Loop Engineering | expert article | S2 | extracted | `sources/2026-06-17-addy-osmani-loop-engineering.md` |
| 2026-06-17-freeman1266-loop-engineering-pr-watch | freeman1266 / MacTalk on Loop Engineering practice and PR watch loop | social/practitioner article | S2.5/S3 | extracted with caveat | `sources/2026-06-17-freeman1266-loop-engineering-pr-watch.md` |

## Concept index

| Concept | Sources | Absorption status | Target docs/templates |
| --- | --- | --- | --- |
| Goal Engineering | `2026-06-17-yupi996-loop-engineering-ralph-overbaking`, `2026-06-17-pandatalk8-goal-loop-workflows` | candidate | A-port / loop-control docs |
| Goal / Loop / Workflows distinction | `2026-06-17-pandatalk8-goal-loop-workflows` | candidate | multi-port contracts / README |
| Design loops, not prompts | `2026-06-17-yanhua-design-loops-not-prompts`, `2026-06-17-addy-osmani-loop-engineering` | candidate | ai-method-wheel |
| Loop primitives: automations, worktrees, skills, connectors, sub-agents, memory | `2026-06-17-addy-osmani-loop-engineering` | candidate | loop-orchestrator / Codex orchestration |
| Stop Condition / Stop Hook | `2026-06-17-yupi996-loop-engineering-ralph-overbaking` | candidate | A-port contract / loop-state |
| Overbaking | `2026-06-17-yupi996-loop-engineering-ralph-overbaking` | candidate | A-port stop conditions / E verification |
| Environment Feedback | `2026-06-17-yupi996-loop-engineering-ralph-overbaking`, `2026-06-17-addy-osmani-loop-engineering` | candidate | loop-orchestrator docs |
| Persistent State / Prompt file | `2026-06-17-yupi996-loop-engineering-ralph-overbaking`, `2026-06-17-addy-osmani-loop-engineering` | candidate | `.ai/knowledge-loop/loop-state.yaml` / templates |

| PR Watch Loop | `2026-06-17-freeman1266-loop-engineering-pr-watch` | watch/experiment | E-port / maintainer-orchestrator / future loop-run template |
| Same-failure escalation rule | `2026-06-17-freeman1266-loop-engineering-pr-watch` | partial_accept | `.ai/templates/loop-run.md` stop/uncertainty rule |
| Goal vs Loop distinction | `2026-06-17-pandatalk8-goal-loop-workflows`, `2026-06-17-freeman1266-loop-engineering-pr-watch` | candidate | A-port / loop-run template |

## Frame updates

| ID | Decision | Scope | Note |
| --- | --- | --- | --- |
| `2026-06-17-protective-loop-engineering-update` | PARTIAL_ACCEPT | protective knowledge-update gate + loop template update | Preserves current baseline while allowing new AI workflow knowledge to enter candidate/proposal layers. |
