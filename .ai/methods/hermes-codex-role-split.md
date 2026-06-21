# Hermes and Codex Logical-Port Split in the AI Method Wheel

> Status: v0.1  
> Purpose: define when Hermes remains the control plane and when Codex is invoked as a maker/reviewer during C/D/E work, without implying separate physical bots.

---

## 1. Core principle

Entering C-port does **not** automatically mean Codex starts changing files.

This document describes **logical port routing only**:

```text
Hermes/Codex are stage roles in one control plane
not separate physical bots.
```
Hermes = control plane / orchestrator / owner-facing reasoning loop
Codex  = bounded coding or review worker, invoked only with a prepared contract

Both are logical roles inside one workflow; no bot split is implied.
```

The AI Method Wheel must preserve:

```text
A/B/C reasoning and routing
→ D bounded maker execution
→ E independent verification
→ F owner gate
```

Codex can participate in C/D/E, but it must not replace Hermes as the controller.

---

## 2. Hermes responsibilities

Hermes owns the continuous control plane:

```text
A-port: demand/control, ambiguity reduction, route decision
B-port: source pack and evidence compression
B2: finished-project absorption pack
C-port: method synthesis, plan shape, handoff contract
D-port: decide whether to invoke a maker and with what scope
E-port: verify outputs, inspect diffs, run checks, compare against specs
F-port: prepare owner decision brief
```

Hermes should do these directly:

```text
read docs and source packs
write method docs and templates
maintain knowledge-loop decisions
update validation scripts
run deterministic checks
inspect git diff/status/log
prepare Codex handoff prompts
review Codex output before accepting it
```

Hermes is also responsible for stopping unsafe routes:

```text
no direct broad implementation from vague intent
no global installs without sandbox/rollback
no Codex run without clean task contract
no self-claimed completion without verification
```

---

## 3. Codex responsibilities

Codex is a worker, not the owner of the workflow.

Use Codex when there is a bounded artifact-producing or review task, such as:

```text
implement one issue or task slice
refactor a specific module
generate or update tests for a defined behavior
review a diff against a spec
convert a prepared plan into code changes
perform a read-only coding-agent review in a git repo
```

Codex should receive:

```text
repo path
branch/worktree policy
exact target files or allowed scope
source spec / plan / tasks / acceptance criteria
what not to change
verification commands
completion evidence required
pause/block conditions
```

Codex should not receive:

```text
raw chat history as the main instruction
vague owner intent
unbounded permission to redesign the repo
permission to install global tools without approval
method-wheel baseline changes without A/E/F gates
```

---

## 4. C-port does not equal Codex

C-port means:

```text
theory/spec/plan synthesis
```

Hermes can usually do C-port itself when the output is:

```text
method doc
architecture decision
runtime integration plan
bridge mapping
handoff template
risk model
verification checklist
```

Codex enters C-port only when the synthesis is code-heavy or benefits from a separate coding-agent review, for example:

```text
generate a detailed implementation plan from a spec
review a proposed scaffold integration for missing tests
prototype a sandbox repo setup script
prepare a PR-sized patch from an already accepted method plan
```

Even then, Hermes must first create the C-port contract and later verify Codex's work.

---

## 5. Spec Kit runtime integration split

For the next Spec Kit phase, the correct split is:

### Hermes should do first

```text
1. Write `spec-kit-runtime-integration-plan.md`.
2. Define sandbox scope and rollback boundaries.
3. Decide what will be tested: specify-cli install, `specify init --integration hermes`, generated files, Hermes profile path, uninstall/rollback.
4. Prepare Codex handoff only if implementation/sandbox scripting is needed.
5. Run or supervise deterministic shell checks.
6. Record E-port verification report.
```

### Codex may do later

```text
1. Create or modify sandbox setup scripts.
2. Execute a bounded prototype in a git worktree or sandbox repo.
3. Review generated files against expected Spec Kit/Hermes mapping.
4. Produce a patch if the integration plan is accepted.
```

### Codex must not do yet

```text
install speckit globally into the active Hermes profile
run `specify init --here --force` in the Method Wheel repo
modify baseline Method Wheel docs without a prepared plan and E/F gates
commit broad changes without Hermes diff review
```

---

## 6. Invocation rule

Use this rule before invoking Codex:

```text
If the task is still about understanding, routing, deciding, or designing the workflow, Hermes handles it.
If the task is a bounded code/scaffold/test/review job with clear inputs and verification, Hermes may delegate to Codex.
```

In Method Wheel terms:

```text
A/B/B2/C-design: Hermes primary
C-code-heavy/D-maker: Codex optional
E-review: Hermes primary, Codex optional as second reviewer
F-decision: Hermes prepares, owner decides
```

---

## 7. Required Codex handoff shape

Before Codex is invoked, Hermes must create a bounded handoff:

```text
# Codex Handoff

## Goal

## Repo / Workdir

## Allowed Scope

## Forbidden Actions

## Inputs
- Spec / plan / tasks / Source Pack paths

## Required Output

## Verification Commands

## Stop / Pause Conditions

## Commit Policy
```

This prevents Codex from acting like an uncontrolled C/D hybrid.

---

## 8. Current recommendation for Spec Kit

For the immediate next step, do **not** invoke Codex yet.

First Hermes should create:

```text
.ai/methods/spec-kit-runtime-integration-plan.md
```

Then E checks the plan. If the plan requires sandbox scripts or a prototype repo setup, Hermes can prepare a Codex handoff for that bounded D/C task.

One-line rule:

```text
Hermes designs and controls the route; Codex executes or reviews bounded code work after the route is stable.
```
