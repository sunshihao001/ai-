# Synthesis — Stacked Loops and Self-Improving Skills

## Sources

- `sources/2026-06-17-sydney-runkle-art-of-loop-engineering.md`
- `sources/2026-06-17-zach-lloyd-self-improving-skills.md`
- `templates/runtime-loop-state.md`
- `templates/false-completion-guard.md`

## Synthesis claim

The current method wheel should treat "loop" as a family of nested control systems rather than one repeated agent call.

```text
Agent loop → Verification loop → Event-driven loop → Self-improvement / hill-climbing loop
```

This professionalizes the A-port question. A should ask: which loop layer are we designing or evaluating?

## Mapping to A/B/C/D/E/F

| Loop layer | Method-wheel interpretation | Main port |
| --- | --- | --- |
| Agent loop | A bounded maker uses tools to complete one task | D/C |
| Verification loop | A checker applies tests/rubrics/review and feeds back failures | E |
| Event-driven loop | Schedules, webhooks, issues, Slack, heartbeats trigger loop runs | A/D/E |
| Self-improvement loop | Traces/feedback/human corrections propose changes to skills/templates/harness | A/B/E/D/F |

## Update to current workflow

The user already has:

- runtime loop state template,
- false-completion guard,
- protective knowledge-update loop,
- skills as procedural memory,
- maker/checker separation.

The new useful addition is a **self-improving skill loop** template where:

1. inner loop runs a skill and records versioned outputs;
2. humans/checkers correct outputs or provide feedback;
3. outer loop periodically extracts generalizable lessons;
4. outer loop proposes a skill/template diff;
5. A/E gates decide whether to merge or keep as experiment.

## Guardrails

Do not allow hill-climbing/self-improvement to bypass baseline protection:

- no silent skill mutation;
- no baseline overwrite from weak feedback;
- no promotion without diff/PR/review;
- no automated update from one-off cases;
- human judgment required for broad principle changes.

## A-port decision

PARTIAL_ACCEPT / ACCEPT_WITH_GUARDRAILS

- Accept stacked-loop taxonomy as A-port professional language.
- Accept self-improving skill loop as a narrow template.
- Do not make LangChain/Warp/Oz the required implementation path.
- Do not change current V4 baseline from these sources alone.
