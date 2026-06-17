# Source Note: GitHub Spec Kit / Spec-Driven Development

- Source ID: 2026-06-17-github-spec-kit-sdd
- Title: GitHub Spec Kit / Spec-Driven Development
- URL: https://github.com/github/spec-kit
- Local mirror: `C:/Users/Administrator/ai-skill-install-work/external-repos/spec-kit`
- Captured: 2026-06-17
- Upstream commit: `3e69233adb6bce3ce351fb8bd1cc84c3f938546a`
- Source type: GitHub repo / official toolkit docs
- Quality level: S1 official source / reproducible repository

## Why this matters

Spec Kit is close to the user's AI Method Wheel because it treats structured specs, plans, tasks, checklists, and agent integrations as the control surface for AI-assisted development. It is not just a prompt pack; it is a repeatable spec-driven workflow with CLI bootstrap, templates, command prompts, hooks, extensions, presets, and multiple AI-agent integrations.

## Core claims extracted

1. Spec-driven development inverts source-of-truth: specifications become primary artifacts and code serves them.
2. Workflow sequence: constitution → specify → clarify/checklist → plan → tasks → analyze → implement.
3. Template constraints improve LLM output: user stories, independent tests, edge cases, measurable success criteria, `NEEDS CLARIFICATION` markers, and governance checks.
4. Constitution as project law: `constitution.md` captures non-negotiable principles and gates planning.
5. Analyze is a read-only consistency checker across `spec.md`, `plan.md`, and `tasks.md` before implementation.
6. Specs have persistence choices: spec-first, spec-anchored, spec-as-source; flow-back, flow-forward, living spec.
7. Extensibility matters: extensions/presets/hooks customize workflow without rewriting the baseline.
8. Multi-agent integration is an adapter layer: Spec Kit supports many agents through integration metadata and command/skill formats.

## Evidence / important upstream files

- `README.md`: CLI setup and command sequence.
- `spec-driven.md`: philosophy, power inversion, executable specs, command workflow.
- `templates/commands/specify.md`: natural language feature → spec directory and feature spec.
- `templates/commands/clarify.md`: up to 5 targeted clarification questions, writes answers into spec.
- `templates/commands/plan.md`: plan generation from spec + constitution with gates.
- `templates/commands/tasks.md`: dependency-ordered task list from design docs and user stories.
- `templates/commands/analyze.md`: read-only cross-artifact consistency analysis.
- `templates/commands/implement.md`: task execution with checklist gate.
- `templates/spec-template.md`: prioritized independently-testable user stories and edge cases.
- `templates/plan-template.md`: technical context, constitution check, project structure.
- `templates/tasks-template.md`: setup/foundation/user-story task phases and parallel markers.
- `docs/concepts/spec-persistence.md`: spec persistence models.
- `AGENTS.md`: integration architecture and agent adapter design.

## Fit to current AI Method Wheel

Strong fit, but partial acceptance only. Spec Kit confirms the current method-wheel direction:

- A端 should produce intent/spec quality, not vague implementation prompts.
- D端/Codex should receive spec/plan/tasks artifacts, not raw chat.
- E端 should run read-only cross-artifact analysis before implementation and separate verification after implementation.
- repo/GitHub artifacts are the durable source of truth.

Spec Kit alone is not enough for the user's full loop because it does not fully encode the user's multi-port A/B/C/D/E/F ownership model, protective knowledge-update loop, maker/checker separation as a bot topology, Codex command orchestration policy, or external-learning reserve.

## Risks / caveats

- Do not replace the current method wheel with Spec Kit wholesale.
- Do not treat `spec-as-source` as mandatory for every project.
- Spec Kit's `/speckit.implement` is too broad for the user's bounded Codex maker rule unless wrapped by A/D/E controls.
- Spec Kit checklists say tests can be optional in generic templates; the user's serious implementation loop should keep verification mandatory when code or business behavior changes.
- Community extensions/presets are not official; review before use.

## Recommended A-port decision

`PARTIAL_ACCEPT`

Absorb Spec Kit as the method-wheel's spec artifact spine, not as the whole operating system.
