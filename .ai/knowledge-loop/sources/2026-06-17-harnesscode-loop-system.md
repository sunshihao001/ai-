# Source Note — yzddp/harnesscode Loop System

## Metadata

- Source ID: 2026-06-17-harnesscode-loop-system
- Title: HarnessCode
- Author: yzddp
- URL: https://github.com/yzddp/harnesscode
- Captured at: 2026-06-17
- Source type: GitHub repo / framework
- Quality level: S1 for repository implementation and docs
- Processing status: extracted

## Why this source matters

HarnessCode is a concrete long-running AI development harness with a tight loop architecture: orchestrator, coder, tester, fixer, reviewer, state files, tech-spec-driven inputs, and backend abstraction for OpenCode/Claude Code.

It is useful as a comparison point for the user's own AI Method Wheel because it shows a simpler, more implementation-oriented pattern than the user's multi-port knowledge/control system.

## Core claims

1. A full development loop can run unattended if PRD and tech specs are complete.
2. Human-in-the-loop is still present for critical nodes.
3. The harness is built around five agents: orchestrator, coder, tester, fixer, reviewer.
4. State files and progress logs drive the loop.
5. The system is tech-stack agnostic as long as `tech-stack.md` exists.
6. The backend abstraction supports both OpenCode and Claude Code.

## Evidence / examples

Repository docs show:

- `input/PRD/tech-stack.md` is required.
- `input/techspec/tech-spec-*.md` files define implementation rules.
- `.harnesscode/feature_list.json`, `test_report.json`, `review_report.json`, `missing_info.json`, and `claude-progress.txt` are runtime state.
- `orchestrator.md` decides the next agent by priority rules.
- `reviewer.md` loads all tech specs and checks all incremental files.
- `infinite_dev.py` loops until orchestrator says complete, with false-completion protection and timeout handling.

## Concepts extracted

| Concept | Explanation | Evidence strength | Candidate target |
| --- | --- | --- | --- |
| Orchestrator-driven loop | A central controller decides the next agent from state files. | S1 | loop orchestrator docs |
| PRD + tech spec inputs | The loop needs structured requirements and rules before execution. | S1 | spec/plan/checklist layer |
| Five-agent harness | Orchestrator, coder, tester, fixer, reviewer. | S1 | multi-port comparison |
| State-file-driven execution | Progress is recorded in runtime files, not only chat. | S1 | knowledge loop / loop-state |
| False-completion guard | The loop refuses to stop if tests/reviews still fail. | S1 | stop conditions |
| Backend abstraction | OpenCode and Claude Code are swappable executors. | S1 | Hermes/Codex orchestration comparison |

## Fit to current Knowledge Frame

| Current frame module | Fit | Notes |
| --- | --- | --- |
| AI Method Wheel | Strong | Confirms loop engineering as a real harness, not just prompt flow. |
| A-port demand/control | Strong | Requirements and tech spec gating match A-port intake. |
| B-port source pack | Medium | HarnessCode is less about external research, more about execution scaffolding. |
| C/D/E loop roles | Strong | Coder / Tester / Fixer / Reviewer map well to maker-checker structure. |
| Knowledge Loop | Strong | State files, reports, and progress logs reinforce durable memory. |

## Risks / caveats

- The repo is a practical harness, not a full knowledge-management or multi-domain reasoning system.
- It is more centralized than the user's multi-port A/B/C/D/E/F model.
- The "fully autonomous" claim should be treated carefully; human interruption is still part of the design.

## Recommended decision

PARTIAL_ACCEPT

Use HarnessCode as a reference for execution-loop structure, state files, false-completion guards, and role separation. Do not adopt its centralized five-agent model as the user's baseline without adapting it to the A/B/C/D/E/F contract.

## Raw summary

HarnessCode combines PRD + tech specs + runtime state files + orchestrator decision logic + four worker agents and a reviewer. It is a concrete example of a harness, while the user's method wheel is a broader control-plane and knowledge-frame system.
