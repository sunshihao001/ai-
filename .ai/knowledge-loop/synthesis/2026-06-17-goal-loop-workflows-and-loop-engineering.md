# Synthesis — Goal, Loop, Workflows, Harness, and Loop Engineering

## Sources

- `sources/2026-06-17-pandatalk8-goal-loop-workflows.md`
- `sources/2026-06-17-yanhua-design-loops-not-prompts.md`
- `sources/2026-06-17-addy-osmani-loop-engineering.md`
- `sources/2026-06-17-yupi996-loop-engineering-ralph-overbaking.md`

## Synthesis claim

The useful distinction for this repository is not which buzzword is newest, but which operational layer is being designed:

```text
Prompt = one instruction to one agent.
Goal = a completion target for an agent/loop.
Harness = the environment, tools, state, and constraints around an agent.
Loop = repeated execution + feedback + state + stop condition.
Workflow = multi-step/multi-agent process with handoffs.
Loop Engineering = designing the system that prompts, checks, records, and routes agents instead of manually prompting them.
```

## Mapping to this repository

| External concept | Method-wheel meaning | Repo location |
| --- | --- | --- |
| Goal | A-port creates completion target and stop condition | A-port contract / loop-state |
| Loop | A controlled repeat cycle with feedback and stop gates | `.ai/templates/loop-run.md`, `.ai/knowledge-loop/` |
| Workflow | Multi-port A/B/C/D/E/F handoff system | `.ai/methods/multi-port-contracts/` |
| Harness | Durable state, tools, setup, feature list, progress files | Codex/Hermes orchestration docs |
| Skills | Reusable intent and project knowledge outside chat | `.agents/skills/`, `.codex/skills/` |
| Connectors | Tool/message/API access for loops | Hermes gateway / OpenCLI / GitHub |
| Sub-agents | Specialized maker/checker ports | B/C/D/E ports |
| Overbaking | Loop runs too long and expands/damages scope | A stop conditions + E verification |

## Implications for A-port

A-port is best described as:

```text
Goal Engineering + Loop Control + Knowledge Frame Gate
```

A-port should produce:

- Initial Knowledge Frame;
- goal and non-goals;
- evidence-fit criteria;
- maker/checker split;
- stop conditions;
- loop state;
- absorption decisions;
- next-route decisions.

## Implications for B-port

B-port is not a link collector. It is:

```text
Search Strategy + Source Pack + Knowledge Fit Feedback
```

B should first propose how to search, then execute after A Gate 1 approval, then return Source Pack + Knowledge Fit Report for A Gate 2.

## Knowledge-loop update

These sources justify keeping `.ai/knowledge-loop/` as a durable learning loop. Articles and social threads should move through:

```text
source note → synthesis → decision → method update
```

rather than remaining one-off chat material.

## Open gaps

- Need official docs for exact `/goal`, `/loop`, `/workflows` command semantics in specific tools.
- Need primary source for Peter Steinberger / Boris Cherny quotes if they will be used verbatim in framework docs.
- Need a concrete loop-run example that updates `.ai/knowledge-loop/loop-state.yaml` after each learning cycle.
