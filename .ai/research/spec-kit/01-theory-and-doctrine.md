# Spec Kit Theory and Doctrine

## 1. Core theory

Spec Kit teaches **Spec-Driven Development (SDD)**:

```text
specification becomes the primary artifact;
code becomes a downstream expression of the spec.
```

The key inversion is:

```text
old: code is truth, docs explain code
new: spec is truth, code realizes spec
```

For AI programming, this matters because a raw natural-language request lets the agent freely interpret the user's intent. Spec Kit inserts a structured artifact chain before implementation.

---

## 2. The anti-pattern

The anti-pattern is:

```text
"build me X"
→ agent guesses product intent
→ agent chooses architecture too early
→ tasks are implicit
→ verification is vague
→ implementation drifts
```

Spec Kit's answer is:

```text
constitution
→ specify WHAT
→ clarify unknowns
→ checklist requirements quality
→ plan HOW
→ tasks in dependency order
→ analyze consistency
→ implement bounded tasks
→ converge implementation gaps
```

---

## 3. Doctrine by artifact

### Constitution

`constitution.md` is the project's governance DNA: quality, testing discipline, architecture principles, simplicity, observability, versioning, and governance.

### Specify

`spec.md` captures WHAT and WHY, not HOW: user stories, acceptance scenarios, functional requirements, edge cases, entities, assumptions, measurable success criteria.

### Clarify

Clarification asks high-impact questions that materially affect implementation or validation, then writes accepted answers back into `spec.md`.

### Checklist

Spec Kit's checklist model is best understood as:

```text
unit tests for English requirements
```

It checks whether requirements are complete, clear, measurable, consistent, and testable before planning.

### Plan

`plan.md` is where HOW starts. It connects the spec to technical decisions, research, data model, contracts, and quickstart validation.

### Tasks

`tasks.md` converts the plan into a dependency-ordered maker queue. Good tasks are specific enough that an AI agent can execute without hidden context.

### Analyze

`/speckit.analyze` is a read-only cross-artifact consistency gate.

### Implement

`/speckit.implement` executes `tasks.md`, not raw owner intent.

### Converge

`/speckit.converge` compares implementation against intent and appends a convergence task phase. This is a missing but important bridge to repair loops.

---

## 4. Persistence models

Spec Kit separates spec lifecycle choices:

```text
spec-first      → useful before implementation, may not stay central
spec-anchored   → durable reference after implementation
spec-as-source  → spec is the primary editable source
```

It also describes evolution styles:

```text
flow-back    implementation discoveries can update artifacts
flow-forward new changes create new feature dirs/history
living spec  spec is contract; plan/tasks regenerate
```

Recommended for the current AI Method Wheel:

```text
normal repo work: spec-anchored + controlled flow-back
method/baseline changes: spec-anchored + flow-forward
avoid default spec-as-source until E/F governance is mature
```

---

## 5. Theory translated into AI Method Wheel terms

```text
Spec Kit constitution → F/A governance baseline
Spec Kit specify/clarify/checklist → A demand-control and requirements quality
Spec Kit plan/research/contracts → C synthesis and theory-to-plan bridge
Spec Kit tasks → D bounded maker queue
Spec Kit analyze → E read-only checker
Spec Kit converge → E→D repair loop candidate
Spec Kit presets/extensions/workflows/bundles → harness/skill ecosystem patterns
```

Spec Kit is not a replacement for A/B/C/D/E/F. It is a finished SDD system whose parts must be routed into the Method Wheel.
