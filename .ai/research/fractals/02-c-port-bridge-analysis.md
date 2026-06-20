# Fractals C-Port Bridge Analysis

## Bridge thesis

`TinyAGI/fractals` is a **task orchestration system**, not a drop-in skill.
Its strongest fit is **C/D/E**, with a narrow A-port contribution.

## Capability-to-port map

### A — divergence support only

Use only the classification/decomposition idea:

- atomic vs composite detection
- splitting one vague input into candidate branches
- comparing branch shapes before deeper work
- adjusting branching heuristics from feedback

Why: this helps A generate multiple candidate directions, but it does not belong to execution or orchestration.

### B — evidence/context compression

Use the notion of lineage-aware context packing:

- task hierarchy passed into classification and decomposition
- ancestor context used to avoid repeating scope
- source-aware decomposition hints

Why: this is evidence shaping, not execution.

### C — recursive planning and branch strategy

This is the strongest bridge point:

- recursive `plan()`
- composite vs atomic separation
- dependency shaping by hierarchy
- batch strategy selection as a planning concern

Why: the repo’s core value is tree construction before execution.

### D — execution orchestration

These capabilities belong to D:

- leaf task execution
- git worktree isolation
- Claude / Codex CLI invocation
- batch-running leaves

Why: they are maker-layer behaviors.

### E — validation and state tracking

These capabilities belong to E:

- tree review before execution
- leaf status polling
- completion propagation
- checking batch progress and final state

Why: they validate whether the plan/execution loop is behaving as intended.

### F — owner confirmation / gating

Use F for:

- accepting the plan tree before execution
- approving execution scope or workspace path
- deciding whether batch strategy changes are acceptable
- deciding whether deeper orchestration features should be adopted

## Explicit exclusions from A-port

Do **not** absorb these into A:

- worktree execution
- agent swarm spawning
- batch orchestration
- server/API execution endpoints

These are execution-system features, not idea-diversity features.

## Method Wheel conclusion

The right relationship is:

```text
fractals → bridge into C/D/E, with a small A-port divergence subroutine
```

It is not a direct A-port skill and not a baseline primitive for the Method Wheel.
