# Absorption Decision — TAN Agent Basic Primer

- Date: 2026-06-17
- Decision owner: A-port demand/control
- Verification: E-port consistency review
- Overall decision: WATCH / PARTIAL_ACCEPT

## Source reviewed

- TAN, `AI智能体（Agent）到底是个啥？`

## Decision

Keep this as a beginner-facing explanation of LLM vs Agent. Do not update the current V4 workflow baseline.

## Accepted

- Agent can be explained as: LLM brain + prompt/job description + tools + knowledge base + workflow.
- Multi-agent collaboration should be framed as specialized roles instead of one万能 agent.
- MCP/A2A should remain on the protocol-awareness watch list.

## Not accepted as baseline change

- The source does not add sufficient detail on state truth, sandbox policy, context projection, verification, false-completion guard, or owner boundaries.
- It should not replace the stronger harness-control framing already accepted from dongxi_nlp/Viv sources.

## E-port consistency result

PASS WITH CAVEAT.

Useful as an onboarding/glossary source, but too simplified to drive architecture changes.
