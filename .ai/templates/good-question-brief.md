# A-Port Demand-Control Brief

Use this when a request, article, repo, or workflow idea needs to be turned into a professional, executable agent task instead of a vague chat instruction.

## Original Ask

## Professional Framing

This is not merely “asking more questions.” This is an Intent-to-Spec Control Gate:

```text
Raw intent → Operational question → Routed execution contract
```

## Improved Agent-Usable Question

```text
Given <current baseline/context>, evaluate/change <specific target>, while preserving <constraints/protected invariants>. Success means <objective evidence>. Verify by <checks>. If <blocked/risky condition>, stop and ask <owner/A-port question>.
```

## Intent and Alternatives

- True goal:
- Is the proposed solution only one implementation path?
- Simpler/safer alternative:
- What should not be optimized yet?

## Context and Constraints

- Repo/system:
- Current baseline:
- Existing source/decision files:
- Protected invariants:
- Constraints:

## Scope and Non-Goals

Do:

- ...

Do not:

- ...

## Assumptions and Risks

- [confirmed]
- [unconfirmed]
- [risky]

## Acceptance Criteria

- [ ] A fit/routing decision exists.
- [ ] Target artifact is named.
- [ ] Verification evidence is defined.
- [ ] Stop/rollback condition is defined.
- [ ] Current baseline is not weakened.

## Verification Plan

- Static/document checks:
- Runtime/test checks:
- Review/checker evidence:
- False-completion traps:


## Harness Control Surface

Before routing to a maker/model, classify the input:

- Input type: ordinary task / control command / state query / diagnostic / skill invocation / owner decision / knowledge-frame update
- Source of truth:
- Runtime state to inspect/update:
- Model-visible context projection:
- Markdown context to load: AGENTS / SKILL / spec / source note / logs
- Tool side-effect policy:
- Human approval boundary:

## Agent Execution Classification

- Classification: Autonomous / Needs owner / Ignored by owner
- Maker:
- Checker:
- Authority boundary:
- Durable state file:

## Loop Stop Conditions

- Max loops:
- Time/cost cap:
- Success condition:
- Failure condition:
- Same-failure / repeated-uncertainty rule:
- Blocker brief format:

## Critique Prompts

- What assumption would make this fail?
- What simpler interpretation exists?
- How could an agent falsely claim success?
- What current baseline invariant could this weaken?
- What evidence would convince a skeptical checker?
- What decision truly requires the owner?

## Missing High-Value Questions

1. ...

## Next Stage

Ready for: source note / synthesis / frame-update / spec / issue / Codex / maintainer-orchestrator / owner decision
