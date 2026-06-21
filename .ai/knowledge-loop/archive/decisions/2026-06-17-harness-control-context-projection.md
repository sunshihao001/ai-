# Absorption Decision — Harness Control Surface and Context Projection

- Date: 2026-06-17
- Decision owner: A-port demand/control
- Verification: E-port consistency review
- Overall decision: PARTIAL_ACCEPT

## Sources reviewed

- dongxi_nlp Harness series posts 1/4/5/6 and short control-state posts:
  - The Harness Is The Product
  - Model remembers transcript, harness must remember truth
  - Model can request, harness decides
  - The Agent's Toolkit: "/"
  - Markdown Is A Context Interface
  - Context Is A Projection

## Decision

Accept the harness-control framing as a narrow workflow update.

## Accepted updates

- Add `.ai/templates/harness-control-surface.md`.
- Update A-port to classify runtime/control inputs before treating them as prompts.
- Update AI Method Wheel language with truth/transcript/context split.
- Add context projection and markdown routing to the workflow.

## Blocked updates

- No replacement of current A/B/C/D/E/F baseline.
- No blind raw markdown dump into prompt.
- No reliance on transcript text as source of truth.
- No model-side execution of tool calls without harness policy checks.

## E-port consistency result

PASS WITH GUARDRAILS.

The update strengthens the current method wheel by making runtime state, context projection, and input routing explicit, while preserving maker/checker separation and owner boundaries.
