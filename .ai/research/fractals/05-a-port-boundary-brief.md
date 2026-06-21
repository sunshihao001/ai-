# A-Port Boundary Grilling Brief: Automated Loop Design Limits for Fractals

## Original Ask

User wants to decide the boundary of automated looping in the A-port first, then let Codex produce detailed theory for the remaining parts.

## Improved Question

Given the current Method Wheel and the `TinyAGI/fractals` evidence pack, what is the **maximum safe boundary** for A-port automatic looping and idea diversification, while preserving the separation between A-port reasoning and C/D/E execution/orchestration? Success means A can generate diverse candidate directions, classify ambiguity, and stop or transfer correctly without drifting into execution behavior. Verify by a concrete routing/stop rule and a clear forbidden-actions list. If the boundary cannot be stated precisely, stop and ask for one blocking owner decision.

## Intent and Alternatives

### True goal

The user is not asking to make A a mini orchestrator. The user wants A to:

- explore an idea broadly,
- auto-ask the few questions that matter,
- optionally use fractals-like branching heuristics,
- and then hand off cleanly to later stages.

### Alternatives

- **A-only divergence helper**: safest; only classify/decompose/branch.
- **A+C split**: A generates candidate directions, C does detailed theory.
- **A as loop orchestrator**: risky unless tightly bounded.

## Context and Constraints

- Current Method Wheel uses logical ports only.
- `fractals` is a recursive task orchestrator, not a simple skill.
- B-port evidence shows classify/decompose and tree branching are real; worktree execution is D/E.
- Codex should handle the long theory generation after the A boundary is fixed.

## Scope and Non-Goals

### In scope

- Define A-port boundary for automatic looping.
- Define what A may auto-generate (candidate branches, ambiguity questions, transfer triggers).
- Define what A must not do (execution, worktrees, batch scheduling, CLI spawning).

### Out of scope

- Implementing execution orchestration.
- Installing new live skills.
- Turning A into a task runner.

## Assumptions and Risks

- [confirmed] A-port can own divergence, classification, and transfer logic.
- [confirmed] D/E own execution and verification.
- [unconfirmed] The ideal branch count for A is 3-5.
- [risky] If A becomes too powerful, it will swallow C/D/E responsibilities.

## Acceptance Criteria

- A boundary is stated in one paragraph.
- A forbidden-actions list is explicit.
- A stop/transfer rule exists.
- The boundary is usable as a prompt/contract for later Codex theory generation.

## Verification Plan

- Check the boundary against the source facts for `fractals`.
- Ensure no execution-layer behavior is included in A.
- Ensure the boundary can be summarized in a Codex prompt without ambiguity.

## Agent Execution Classification

- **Classification:** Autonomous for drafting the boundary, Needs owner for any expansion beyond divergence/clarification.
- **Handoff target:** Codex for detailed theory after the boundary is fixed.
- **Authority boundary:** A may propose and stop; it may not execute or install.

## Loop Stop Conditions

- Stop after 1-2 rounds if the route is clear.
- Stop if additional questions only change wording, not boundary.
- Transfer to Codex once the forbidden-actions list and transfer rule are stable.

## Critique Prompts

- What assumption would make A drift into execution?
- What execution behavior is hardest to keep out of A?
- What proof would show A is overreaching?
- What part belongs in C instead of A?

## Missing High-Value Questions

1. How many candidate branches should A generate by default?
2. Should A ask at most one blocking question before transfer?
3. What exact stop condition should trigger handoff to C?

## Next Stage

Ready for: Codex

## Copy-Paste Handoff Template

```md
# A-Port Boundary Brief

## Boundary
A may classify, decompose, and generate candidate branches, but must not execute tasks, create worktrees, or schedule batches.

## Forbidden Actions
- leaf execution
- worktree creation
- swarm execution
- batch scheduling
- CLI spawning

## Stop Rule
Stop when goal, boundary, and verification are 3/4 actionable, or after 1-2 non-informative rounds.

## Transfer Rule
Transfer to C for long-form theory generation once the boundary is stable.
```
