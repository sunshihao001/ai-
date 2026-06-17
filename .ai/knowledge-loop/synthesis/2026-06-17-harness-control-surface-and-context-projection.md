# Synthesis — Harness Control Surface and Context Projection

## Sources

- `sources/2026-06-17-dongxi-nlp-harness-series.md`
- `templates/runtime-loop-state.md`
- `templates/false-completion-guard.md`
- `templates/harness-control-surface.md`

## Synthesis claim

The latest harness-series sources sharpen the method wheel from "agent loop orchestration" into a broader runtime-control system:

```text
Model proposes. Harness decides. Runtime state is truth. Context is projection.
```

This should update the A-port professional framing:

```text
A-port is not only a demand-grilling gate; it is the Demand-Control Plane that routes intent, state, context, tools, and owner decisions before maker agents run.
```

## Core upgrade

Previous framing:

```text
A turns vague user requests into agent-usable questions.
```

Updated framing:

```text
A classifies whether input is a user task, control command, state query, diagnostic, skill invocation, or knowledge-frame update; then routes it through the correct harness surface.
```

## Mapping to current workflow

| Harness concept | Method-wheel meaning | Target update |
| --- | --- | --- |
| Harness is the product | Reliable behavior belongs in runtime/state/tools/context, not model vibes. | AI Method Wheel control layer |
| Model proposes, harness decides | Tool calls and side effects require A/E/F policy gates. | A-port / E-port / F-port |
| Truth vs transcript | State files and repo are truth; transcript is evidence. | runtime-loop-state / false-completion |
| Slash/control commands | Runtime control should not be treated as normal chat. | A-port routing matrix |
| Markdown context interface | AGENTS.md, SKILL.md, specs, logs enter different context layers. | skill-stack / onboarding |
| Context projection | Model sees selected next-step view, not raw full history. | harness-control-surface template |

## A-port decision

PARTIAL_ACCEPT

Accept as an additive control-plane clarification. Do not replace existing V4 workflow; update language and templates so future work distinguishes prompt, control command, runtime state, and projected context.

## Guardrails

- Do not let markdown files bypass system/developer policy.
- Do not treat compacted summary as full truth.
- Do not route tool side effects directly from model proposal to execution.
- Do not let diagnostics be model guesses when deterministic state exists.
