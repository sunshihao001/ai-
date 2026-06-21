# Fractals A-Port Diversity Subroutine

## Purpose

Extract only the narrow part of `fractals` that can help A-port generate more diverse and criticizable ideas.

## Safe A-port-adjacent subset

The following behaviors are useful as A-port support:

- classify a vague request as atomic or composite
- split one vague request into multiple candidate branches
- compare branch shapes before entering C
- adjust branching heuristics from feedback

## Example A-port use

Given a vague idea, A can do this:

1. decide whether it is one coherent unit or several concerns
2. generate 3-5 plausible sub-branches
3. label which branch looks primary
4. label which branches are secondary or risky
5. decide whether to continue questioning or hand off to C

## Why this is safe

This only improves the front-end of reasoning.
It does not create execution authority.
It does not create worktrees.
It does not spawn an agent swarm.

## Forbidden subset

Do not move these into A:

- any leaf execution
- worktree creation
- swarm execution
- batch scheduling

Those belong to D/E.

## Practical interpretation

For the Method Wheel, `fractals` can inspire an A-port routine like this:

```text
input idea
→ classify
→ branch into candidate directions
→ rank by usefulness / risk / verifiability
→ choose whether to continue A or hand off to C
```

That is the useful A-port slice.
Everything beyond that is orchestration/execution and should stay out of A.
