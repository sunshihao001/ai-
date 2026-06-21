# Absorption Decision — Agent Harness Anatomy and Skill Progression

- Date: 2026-06-17
- Decision owner: A-port demand/control
- Verification: E-port consistency review
- Overall decision: ACCEPT_WITH_GUARDRAILS / PARTIAL_ACCEPT

## Sources reviewed

- Viv, `The Anatomy of an Agent Harness`
- Riley West, `how to master AI in 30 days`

## Decision

- Viv: ACCEPT_WITH_GUARDRAILS as a strong harness-engineering source.
- Riley: WATCH / PARTIAL_ACCEPT as a broad skill progression source.

## Accepted updates

- Strengthen harness-control templates with environment/sandbox/tool policy, hooks/middleware, and context-rot mitigation.
- Add skill progression language: repeated prompts should become templates, scripts, tools/MCP workflows, then SKILL.md packages.

## Blocked updates

- No replacement of current A/B/C/D/E/F baseline.
- No unguarded bash/code execution.
- No silent conversion of personal prompt libraries into shared skills without review.
- No vendor-specific lock-in.

## E-port consistency result

PASS WITH GUARDRAILS.

The updates strengthen already-accepted harness-control architecture and do not weaken maker/checker separation, owner boundaries, rollbackability, or baseline protection.
