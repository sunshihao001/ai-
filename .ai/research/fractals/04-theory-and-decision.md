# Fractals Theory and Decision

## What `fractals` is

`TinyAGI/fractals` is a recursive task orchestrator for agent swarms.
It takes a high-level task, recursively decomposes it into a tree of subtasks, and runs leaf tasks in isolated git worktrees.

## Why it is not a simple skill

It is not a simple skill because it contains:

- a planning phase and an execution phase
- LLM-based classify/decompose logic
- tree recursion and status propagation
- git worktree management
- batch execution strategies
- a server/UI control surface

That means it is closer to a workflow engine than to a single reusable prompt skill.

## Where it strengthens the Method Wheel

### Strengthens A

- helps A split vague ideas into candidate branches
- helps A distinguish atomic vs composite requests
- helps A compare multiple possible decompositions

### Strengthens C

- recursive planning theory
- decomposition strategy
- branch strategy and depth control
- dependency-aware thinking

### Strengthens D/E

- execution orchestration
- worktree isolation
- batch execution and progress tracking
- validation through tree/state review

## Where it conflicts with A-port expectations

A-port should not become an execution engine.
So the following must stay out of A:

- worktree creation
- leaf execution
- swarm spawning
- batch scheduling
- API/server execution endpoints

## Decision options

- `BRIDGE` — use as a bridge into A/C/D/E with clear boundaries.
- `PATTERN_ONLY` — keep only the design pattern, not the runtime.
- `PARTIAL_ACCEPT` — adopt the decomposition idea, not the execution stack.
- `REJECT AS BASELINE` — do not make it a default Method Wheel primitive.

## Recommended decision

```text
PARTIAL_ACCEPT + BRIDGE
```

Meaning:

- adopt the classify/decompose/divergence ideas for A/C
- keep execution orchestration in D/E
- do not treat the repo as a downloadable skill
- do not make its runtime a baseline control-plane primitive

## Remaining evidence gaps

- `web/` source was not inspected
- `src/index.ts` and `src/print.ts` were not inspected
- tests / CI / release behavior were not inspected
- runtime behavior beyond the static source files remains unverified
