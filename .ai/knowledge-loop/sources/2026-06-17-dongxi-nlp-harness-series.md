# Source Note — dongxi_nlp Harness Series: Harness, Control Surface, Markdown Context, Context Projection

## Metadata

- Source ID: 2026-06-17-dongxi-nlp-harness-series
- Author: 马东锡 NLP (@dongxi_nlp)
- Series URLs:
  - https://x.com/dongxi_nlp/status/2064098727867163124
  - https://x.com/dongxi_nlp/status/2064921985734397963?s=20
  - https://x.com/dongxi_nlp/status/2065299516677402976?s=20
  - https://x.com/dongxi_nlp/status/2065713612384010332?s=20
  - https://x.com/dongxi_nlp/status/2066290950352081336?s=20
  - https://x.com/dongxi_nlp/status/2066991890348572950?s=20
- Captured at: 2026-06-17
- Source type: X article series / practitioner framework
- Quality level: S2
- Processing status: extracted from X/article summaries plus fxtwitter API

## Why this source matters

This series is one of the clearest practitioner descriptions of the coding-agent harness as the real product. It explains that coding agents need a runtime that owns truth, input routing, markdown context loading, and context projection.

The series is highly relevant to the user's AI Method Wheel because it sharpens the A-port into a real control plane: not just demand clarification, but runtime input routing, context selection, and state truth management.

## Core claims

1. **The harness is the product** for reliable coding agents.
2. A coding agent is model-in-a-runtime, not a bare prompt box.
3. The harness must own truth; the transcript only records what happened.
4. Some user inputs are control-plane intent, not ordinary chat prompts.
5. Slash commands and runtime tools should be routed before model prompting.
6. Markdown files work only when the harness knows what kind of context they are.
7. AGENTS.md and SKILL.md should enter different context layers differently.
8. Context is a projection: the harness decides what matters now from the full history.
9. Durable log, model-visible context, and app state are different things.
10. Session state must not depend on whether old transcript text remains in the prompt.

## Per-article extraction summary

### 2064098727867163124 — The Harness Is The Product

Key points extracted:

- Ask first what the harness is responsible for, not which model to use.
- The model sits inside a runtime that checks repo state, requests tools, edits files, runs checks, remembers what happened, and continues across rounds.
- The harness decides paths, approvals, baselines, validation, and state updates.
- Reliable behavior comes from the harness around the model.

### 2064921985734397963 — Model remembers transcript, harness must remember truth

Key point extracted:

- Transcript is not truth.
- File state is a basic harness requirement.

### 2065299516677402976 — Model can request, harness decides

Key point extracted:

- Tool calls should only execute after harness approval.
- That is the contract boundary.

### 2065713612384010332 — The Agent's Toolkit: "/"

Key points extracted:

- Not every input should be treated as a prompt.
- Slash commands are user control inputs for the runtime.
- `/goal` is explicit session state and lifecycle control.
- Diagnostics like `/audit` and `/doctor` should inspect local harness state, not ask the model to guess.
- Prompt box is not the only interface; the harness owns its own control surface.

### 2066290950352081336 — Markdown Is A Context Interface

Key points extracted:

- Markdown affects behavior when routed correctly by the harness.
- AGENTS.md is workspace instruction context.
- SKILL.md is task-procedure context.
- Raw markdown dumps are risky because old notes can compete with current instructions.
- The harness should load markdown by context type, not dump it blindly into the prompt.

### 2066991890348572950 — Context Is A Projection

Key points extracted:

- Transcript records what happened; context decides what matters now.
- Long sessions need projection.
- Durable log, model-visible context, and app state should be separated.
- The harness should project the full history into a smaller next-step view before model call.
- Auto-compact, result previews, summaries, and state injection are all projection moves.

## Concepts extracted

| Concept | Explanation | Evidence strength | Candidate target |
| --- | --- | --- | --- |
| Harness is the product | Runtime boundary, state, tools, and routing matter as much as the model. | S2 | AI Method Wheel / A-port |
| Truth vs transcript | The durable truth lives in state/files, not in conversation text. | S2 | runtime-loop-state / false-completion guard |
| Control-plane input routing | Slash commands and runtime commands should be handled before model prompting. | S2 | A-port / command layer |
| Markdown as context interface | AGENTS.md and SKILL.md enter distinct context layers through the harness. | S2 | project onboarding / port skills |
| Context as projection | The harness selects the relevant next-step view from full history. | S2 | context projection / loop-run |
| Durable log vs model-visible context vs app state | These are different and must not be conflated. | S2 | loop state templates |
| File state baseline | File state is required to avoid stale transcript truth. | S2 | false-completion guard |

## Fit to current Knowledge Frame

| Current frame module | Fit | Notes |
| --- | --- | --- |
| A-port Demand-Control Plane | Strong | A must now act as a control-plane router, not only a question refiner. |
| Runtime loop state | Strong | Supports explicit truth/state separation. |
| False-completion guard | Strong | Reinforces file state as source of truth. |
| Multi-port contracts | Strong | Markdown/interface/context routing maps to port-specific skill stacks. |
| Knowledge loop | Strong | Long sessions need projection, not naive append. |

## Risks / caveats

- These are practitioner/narrative sources, not formal specifications.
- Do not copy the LangChain/Warp terminology blindly; preserve the underlying control-plane idea.
- Do not let markdown files mutate the prompt without harness routing.
- Do not treat compacted context as equivalent to truth or full history.

## Recommended decision

PARTIAL_ACCEPT

Accept the harness-as-product framing, context projection, truth-vs-transcript split, control-plane routing, and markdown-as-context-interface ideas. Use them to sharpen A-port, runtime state, and context management. Do not rewrite the core V4 baseline or bind the workflow to a specific vendor stack.
