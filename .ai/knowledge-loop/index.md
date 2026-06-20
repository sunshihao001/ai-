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
| 2026-06-17-harnesscode-loop-system | yzddp/harnesscode GitHub repo loop system | GitHub repo | S1 | extracted | `sources/2026-06-17-harnesscode-loop-system.md` |
| 2026-06-17-sydney-runkle-art-of-loop-engineering | Sydney Runkle on stacked loop engineering / loopcraft | X article | S2 | extracted with caveat | `sources/2026-06-17-sydney-runkle-art-of-loop-engineering.md` |
| 2026-06-17-zach-lloyd-self-improving-skills | Zach Lloyd on self-improving Skills inner/outer loops | X article + GitHub demo | S1/S2 | extracted with caveat | `sources/2026-06-17-zach-lloyd-self-improving-skills.md` |
| 2026-06-17-dongxi-nlp-harness-series | dongxi_nlp Harness series on runtime control/context | X article series | S2 | extracted with caveat | `sources/2026-06-17-dongxi-nlp-harness-series.md` |
| 2026-06-17-viv-agent-harness-anatomy | Viv on Agent = Model + Harness and harness primitives | X article | S2 | extracted with caveat | `sources/2026-06-17-viv-agent-harness-anatomy.md` |
| 2026-06-17-riley-west-ai-30-day-roadmap | Riley West AI 30-day roadmap / skill progression | X article | S3 | extracted with caveat | `sources/2026-06-17-riley-west-ai-30-day-roadmap.md` |
| 2026-06-17-tan-agent-basic-primer | TAN beginner primer on LLM vs Agent | X article | S3 | extracted with caveat | `sources/2026-06-17-tan-agent-basic-primer.md` |
| 2026-06-19-github-spec-kit-code-review | GitHub Spec Kit source-code/docs/templates review | GitHub repo source | S1 | extracted; decision updated | `sources/2026-06-19-github-spec-kit-code-review.md` |

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
| Runtime loop state files | `2026-06-17-harnesscode-loop-system` | partial_accept | `.ai/templates/runtime-loop-state.md` |
| False-completion guard | `2026-06-17-harnesscode-loop-system` | partial_accept | `.ai/templates/false-completion-guard.md` |
| Stacked loop taxonomy | `2026-06-17-sydney-runkle-art-of-loop-engineering` | partial_accept | A-port loop classification / synthesis |
| Self-improving Skill Loop | `2026-06-17-zach-lloyd-self-improving-skills` | accept_with_guardrails | `.ai/templates/self-improving-skill-loop.md` |
| Harness control surface | `2026-06-17-dongxi-nlp-harness-series` | partial_accept | `.ai/templates/harness-control-surface.md` |
| Context projection | `2026-06-17-dongxi-nlp-harness-series` | partial_accept | AI Method Wheel control layer / harness template |
| Harness anatomy | `2026-06-17-viv-agent-harness-anatomy` | accept_with_guardrails | AI Method Wheel Phase 0 / harness template |
| Skill progression path | `2026-06-17-riley-west-ai-30-day-roadmap` | watch/partial_accept | AI Method Wheel Skill Layer |
| LLM vs Agent distinction | `2026-06-17-tan-agent-basic-primer` | watch/partial_accept | onboarding/glossary support |
| Spec Kit bridge layer | `2026-06-19-github-spec-kit-code-review` | partial_accept_expand | `.ai/methods/spec-kit-bridge-layer.md` after B2 full absorption |
| Finished Project Absorption | `2026-06-19-github-spec-kit-code-review`, `.ai/research/spec-kit/` | accepted_method_component | `.ai/methods/finished-project-absorption.md` |

## Frame updates

| ID | Decision | Scope | Note |
| --- | --- | --- | --- |
| `2026-06-17-protective-loop-engineering-update` | PARTIAL_ACCEPT | protective knowledge-update gate + loop template update | Preserves current baseline while allowing new AI workflow knowledge to enter candidate/proposal layers. |

## Comparison frames

| Frame | Status | Latest update | Notes |
| --- | --- | --- | --- |
| HarnessCode loop system | comparison | `sources/2026-06-17-harnesscode-loop-system.md` | Centralized five-agent harness with PRD/spec/state-file execution loop. |

## Decision updates

| ID | Decision | Scope | Note |
| --- | --- | --- | --- |
| `2026-06-17-stacked-loops-self-improving-skills` | PARTIAL_ACCEPT / ACCEPT_WITH_GUARDRAILS | stacked-loop taxonomy + self-improving skill template | Adds outer improvement loop while preserving baseline protection. |
| `2026-06-17-harness-control-context-projection` | PARTIAL_ACCEPT | harness control surface + context projection | Clarifies truth/transcript/context split and A-port input routing. |
| `2026-06-17-agent-harness-anatomy-skill-progression` | ACCEPT_WITH_GUARDRAILS / PARTIAL_ACCEPT | harness anatomy + skill progression | Strengthens harness primitive checklist and prompt-to-skill progression. |
| `2026-06-17-tan-agent-basic-primer` | WATCH / PARTIAL_ACCEPT | beginner LLM-vs-Agent explanation | Keep as onboarding/glossary support; no baseline architecture change. |
| `2026-06-19-spec-kit-code-level-expansion-decision` | PARTIAL_ACCEPT_EXPAND | Spec Kit bridge layer + B2 full absorption correction | Expand previous Spec Spine absorption with Hermes integration caution, presets/extensions/workflows governance, A/B/C/D/E/F mapping, and the new Finished Project Absorption norm. |
