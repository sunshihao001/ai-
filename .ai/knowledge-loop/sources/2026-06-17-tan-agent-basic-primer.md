# Source Note — TAN: AI智能体（Agent）到底是个啥？

## Metadata

- Source ID: 2026-06-17-tan-agent-basic-primer
- Title: AI智能体（Agent）到底是个啥？
- Author: TAN (@tanzhengmc97)
- URL: https://x.com/tanzhengmc97/status/2066908870828564886
- Captured at: 2026-06-17
- Source type: X article / beginner conceptual explainer
- Quality level: S3
- Processing status: direct X extraction failed; article body extracted via `https://api.fxtwitter.com/status/2066908870828564886`

## Why this source matters

This is not a deep harness-engineering source, but it is a clear beginner-level articulation of the LLM vs Agent distinction. It gives a simple product-manager vocabulary:

```text
Agent = LLM brain + prompt role/rules + tools + knowledge base + workflow
```

It also introduces MCP, A2A, and multi-agent collaboration as expected product-manager basics.

## Core claims

1. A chatbot/LLM can answer, but an agent can take action through tools.
2. An agent is assembled from five pieces:
   - LLM / brain
   - Prompt / job description and behavior constraints
   - Tools / action permissions and integrations
   - Knowledge base / reference material
   - Workflow / sequence of steps
3. MCP is a universal connector for tools.
4. A2A is a protocol/metaphor for agent-to-agent communication.
5. Multi-agent collaboration replaces one all-purpose agent with specialized roles: task decomposition, execution, checking.
6. For agent product managers: tool quality, prompt quality, data quality, protocols, and team-style specialization matter.

## Concepts extracted

| Concept | Explanation | Evidence strength | Candidate target |
| --- | --- | --- | --- |
| LLM vs Agent distinction | LLM talks; agent acts with tools and workflow. | S3 | onboarding / glossary |
| Five-part agent explainer | Brain + prompt + tools + KB + workflow. | S3 | beginner-facing explanation |
| Multi-agent specialization | Specialized agents should cooperate instead of one万能 agent. | S3 | multi-port contracts intro |
| MCP/A2A awareness | Tool and agent communication protocols are basics for PMs. | S3 | watch list / future protocol study |

## Fit to current Knowledge Frame

| Current frame module | Fit | Notes |
| --- | --- | --- |
| AI Method Wheel | Low/Medium | Simplifies ideas already present in harness-control docs. |
| Multi-port contracts | Medium | Supports specialized-agent framing. |
| Harness control surface | Medium | Maps tools/knowledge/workflow to harness components. |
| Skill progression | Low | Does not directly add a new workflow template. |

## A-port demand-grilling result

Question: Does this source challenge or update the current method wheel?

Answer: No broad update. It validates existing direction but is lower-resolution than the current harness framework.

Useful low-risk absorption:

- Keep as a beginner-facing source note.
- Optionally reuse the five-part explanation when explaining agents to non-technical users or product managers.
- Do not promote it to baseline workflow architecture.

## Risks / caveats

- The explanation is simplified and omits harness policy, sandboxing, state, context projection, verification, and owner gates.
- Treating MCP/A2A as “must know basics” is directionally useful but not sufficient for implementation.
- The article uses product-manager vocabulary, not operational engineering detail.

## Recommended decision

WATCH / PARTIAL_ACCEPT

Accept only as onboarding/glossary support. No core method-wheel baseline change.
