# Synthesis — Agent Harness Anatomy and Skill Progression

## Sources

- `sources/2026-06-17-viv-agent-harness-anatomy.md`
- `sources/2026-06-17-riley-west-ai-30-day-roadmap.md`
- `sources/2026-06-17-dongxi-nlp-harness-series.md`
- `templates/harness-control-surface.md`
- `templates/runtime-loop-state.md`

## Synthesis claim

Viv's harness anatomy provides a stronger conceptual foundation for the current method wheel:

```text
Agent = Model + Harness
```

The model contains intelligence; the harness turns it into reliable work through state, tools, infrastructure, orchestration, hooks, middleware, context management, verification, and constraints.

Riley West's roadmap is weaker as architecture evidence, but useful as a skill-progression ladder:

```text
one-off prompt → reusable prompt skeleton → prompt library → API/batch loop → tools/MCP → SKILL.md
```

## Update to current workflow

The current AI Method Wheel should treat harness design as a first-class A/E/D/F concern:

| Harness area | Method-wheel interpretation | Artifact |
| --- | --- | --- |
| System prompts / instructions | Stable workspace and port contracts | AGENTS.md, A/B/C/D/E/F prompts |
| Tools / Skills / MCPs | Task-specific procedure and external context access | SKILL.md, MCP config, tool policy |
| Bundled infrastructure | Filesystem, sandbox, browser, git, package managers | runtime-loop-state, tool-policy |
| Orchestration logic | Routing, subagents, handoffs, model/Codex command selection | A-port, Hermes-Codex orchestration |
| Hooks/middleware | Compaction, continuation, lint/test hooks, false-completion checks | loop-run, false-completion guard |
| Context management | Projection, output offloading, progressive disclosure | context-projection.md |
| Long horizon | Durable state, planning, verification, continuation | .ai/loop-runs/<run-id>/ |

## A-port decision

ACCEPT_WITH_GUARDRAILS for Viv harness anatomy.

WATCH / PARTIAL_ACCEPT for Riley roadmap.

## Narrow update route

Do not rewrite the V4 baseline. Strengthen runtime templates by adding:

- sandbox/environment policy;
- hooks/middleware list;
- context-rot mitigation;
- skill-progression path from prompt to SKILL.md.

## Guardrails

- Bash/code execution must remain behind sandbox/path/network/tool policy.
- Context compaction and output offloading must preserve audit handles.
- Prompt-library/skill progression should not bypass A/E review for shared workflow changes.
