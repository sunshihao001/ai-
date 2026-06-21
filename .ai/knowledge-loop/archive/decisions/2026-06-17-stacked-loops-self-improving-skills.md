# Absorption Decision — Stacked Loops and Self-Improving Skills

- Date: 2026-06-17
- Decision owner: A-port demand/control
- Verification: E-port consistency review
- Overall decision: PARTIAL_ACCEPT / ACCEPT_WITH_GUARDRAILS

## Sources reviewed

- Sydney Runkle, `The Art of Loop Engineering`
- Zach Lloyd, `How to build a self-improvement loop for your Skills`
- LangChain rubric/HITL docs as supporting evidence
- Warp issue-triage-loop demo files as implementation evidence

## Decision

Accept the professional loop taxonomy and self-improvement pattern as additive templates.

Do not replace the current V4 method wheel or A/B/C/D/E/F port contracts.

## Accepted updates

- Add stacked-loop language to the knowledge reserve.
- Add `.ai/templates/self-improving-skill-loop.md`.
- Treat human corrections, test/review failures, and trace analysis as feedback signals for future skill improvement.
- Require all skill improvements to be reviewable diffs with A/E protection gates.

## Blocked updates

- No silent mutation of core skills/prompts.
- No automatic baseline rewrite from one-off or weak feedback.
- No mandatory dependency on LangChain, LangSmith, Warp, or Oz.
- No removal of human oversight for sensitive actions or broad method changes.

## E-port consistency result

PASS WITH GUARDRAILS.

The update strengthens the current method wheel by adding an outer improvement loop, while preserving maker/checker separation, owner boundaries, rollbackability, and baseline protection.
