# Fractals Practical Adoption Correction

> Purpose: correct the Method Wheel direction after owner feedback.  
> Owner correction: do not over-theorize or reinvent an existing tool. Treat `TinyAGI/fractals` as a practical external workflow component candidate that can be lightly optimized and connected to the whole workflow.

## 1. Correction

The previous line of work correctly protected A-port from becoming an execution engine, but it over-emphasized internal theory and under-emphasized the practical fact:

```text
fractals already exists as a working recursive task orchestration tool.
```

For a nonprofessional owner who advances work by natural language, the preferred path is not to recreate `fractals` inside the Method Wheel.

The preferred path is:

```text
Use the existing project
→ test it in a sandbox
→ lightly wrap the inputs/outputs
→ map it to A/B/C/D/E/F
→ keep only a few safety boundaries
```

## 2. Revised classification

Previous classification:

```text
PARTIAL_ACCEPT + BRIDGE as theory pattern
```

Corrected practical classification:

```text
PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE
```

Meaning:

- do not make it a Method Wheel baseline runtime yet;
- do not rebuild its task tree logic ourselves;
- do test the existing runtime/tool as a whole-workflow component;
- use Method Wheel only to define when/how it is invoked and how outputs are reviewed.

## 3. Whole-workflow usefulness

`fractals` may be useful across the whole workflow, not only A-port:

```text
A: natural-language idea → candidate branches
B: context/source hints before decomposition
C: recursive plan/tree review
D: leaf-task execution in worktrees, if sandbox-approved
E: status/result checking and false-completion guard
F: owner plan approval before execution
```

The key is not to split these into many custom internal tools. The key is to let the existing Fractals project do what it already does, while Method Wheel controls the boundary and review.

## 4. Nonprofessional-owner operating principle

The user is not trying to become a TypeScript maintainer of `fractals`.

The user needs a natural-language workflow like:

```text
1. I describe an idea.
2. A/Hermes decides whether a Fractals-style tree is useful.
3. Fractals generates a task tree.
4. I review the tree visually or as text.
5. If I approve, later ports decide what to execute.
6. Hermes records decisions and checks outputs.
```

Therefore, the implementation should optimize for:

- simple commands;
- clear prompts;
- visible task tree output;
- owner review before execution;
- minimal code modification;
- no requirement that the owner understand TypeScript internals.

## 5. What to optimize instead of rebuilding

Prefer light modifications/wrappers around existing Fractals behavior:

- add a Method Wheel prompt preset for classify/decompose;
- add export from Fractals tree to Method Wheel markdown;
- add a review checklist before execution;
- add a mode that stops after planning/tree generation;
- add a natural-language handoff from A/C to Fractals;
- add a simple `no-execute` sandbox workflow first.

Do not rewrite:

- recursive planner;
- task tree structure;
- server/UI;
- worktree execution engine;
- batching engine.

## 6. Correct next stage

The next stage should not be more C-port abstract theory.

The next stage should be:

```text
D/E sandbox practical trial
```

Suggested trial:

```text
1. Install/run `TinyAGI/fractals` in a sandbox folder.
2. Use a harmless natural-language task.
3. Generate the task tree only.
4. Do not execute leaf tasks yet.
5. Export or copy the tree into `.ai/research/fractals/sandbox/`.
6. Evaluate whether the output helps the owner think better.
7. Only then consider execution integration.
```

## 7. Updated decision

```text
PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE
```

This supersedes a purely theoretical reading of `PARTIAL_ACCEPT + BRIDGE`.

The core insight remains:

```text
A should not execute.
```

But the practical correction is:

```text
Do not rebuild Fractals. Try the existing tool, lightly adapt it, and connect it to the full workflow.
```
