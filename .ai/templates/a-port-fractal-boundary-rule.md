# A-Port Fractal Boundary Rule

> Purpose: promote the accepted `TinyAGI/fractals` lesson into a reusable A-port control rule.

## Fixed decision

```text
PARTIAL_ACCEPT + BRIDGE
```

A-port may borrow recursive classify/decompose/branch-shaping ideas.
A-port must not absorb runtime execution, worktrees, batching, swarm behavior, or server/API execution ownership.

## Maximum safe A-port boundary

```text
A may classify, decompose, and compare candidate branches.
A must stop before execution planning becomes implementation orchestration.
A transfers to C when the branch shape, boundary, and verification question are stable enough for theory generation.
```

## Allowed A-port actions

A may:

- classify an input as `atomic`, `composite`, or `unclear`;
- generate 2-5 candidate conceptual branches;
- identify primary, secondary, risky, and out-of-scope branches;
- compare branches by scope, risk, dependency, usefulness, and verifiability;
- ask one next blocking clarification question if the boundary is unstable;
- route to B when evidence is missing;
- route to C when a theory/planning package is ready;
- route to F when owner decision is required;
- create an A→C transfer packet.

## Forbidden A-port actions

A must not:

- create worktrees;
- run leaf tasks;
- spawn Claude/Codex/OpenCode workers;
- choose or run batch execution strategy;
- own server/API execution endpoints;
- treat decomposition as permission to execute;
- convert candidate branches into a maker queue;
- claim status propagation is quality verification.

## Stop condition

A stops when:

```text
1. branch shape is stable enough to name primary/secondary/non-goal branches;
2. scope boundary is explicit enough to prevent accidental implementation expansion;
3. verification question is clear enough for C/E to design checks;
4. further A questions would mostly change wording, not route.
```

A-loop may do 1-2 refinement rounds. After that, transfer instead of deepening the A loop unless a true blocking owner question remains.

## A→C transfer packet

When transferring from A to C, include:

```text
- original user intent
- atomic/composite/unclear judgment
- selected branch shape
- rejected branches / non-goals
- unresolved assumptions
- acceptance criteria draft
- verification question
- risk notes
- recommended next port: B / C / F
```

## Relation to Fractals

This rule absorbs `fractals` as a reasoning pattern only:

```text
fractals execution tree  → rejected for A
Method Wheel decision tree → accepted for A
```

A uses tree thinking to clarify and transfer; D/E own execution and verification.
