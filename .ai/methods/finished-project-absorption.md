# Finished Project Absorption Method

> Status: v0.1  
> Purpose: define how the AI Method Wheel absorbs a mature external GitHub project as a reusable workflow component, instead of doing shallow repo review or prompt-level borrowing.

---

## 1. Why this component exists

A mature external project is not just a link or a set of tips. It usually contains several layers:

```text
theory / doctrine
→ user-facing workflow
→ source code implementation
→ project structure and scaffold
→ templates and generated artifacts
→ extension points
→ tests / release / packaging
→ operational cautions
```

If A-port only asks “can this improve our workflow?” too early, it will produce a shallow `ADOPT/BRIDGE/REJECT` decision before understanding the project.

Therefore the AI Method Wheel needs a dedicated component:

```text
Finished Project Absorption
```

Its job is to convert a complete external project into a structured internal understanding before any baseline integration.

---

## 2. Where it sits in the AI Method Wheel

Finished Project Absorption sits between B-port source collection and C-port synthesis:

```text
A: owner intent / absorption question
→ B: Source Pack from external repo
→ B2: Finished Project Absorption Pack
→ A: absorption decision
→ C: bridge/spec/method synthesis
→ D: repo landing
→ E: verification
→ F: owner approval for baseline changes
```

This is intentionally a new B2 component, not a replacement for A/B/C.

### Why B2, not A?

A decides whether a source matters and what decision is being made. But A should not pretend to understand a mature repo without a structured read.

### Why B2, not C?

C synthesizes into the user's framework. But C must receive already-normalized knowledge: theory, code, scaffold, artifacts, extension points, risks.

---

## 3. Trigger conditions

Use this component when the owner says or implies:

- “先了解这个仓库到底是什么”
- “不要只是看 README”
- “要理解理论、代码、项目结构、脚手架”
- “看它是否能完善到 AI 工作流”
- “这是一个成熟项目/成品项目/完整框架”
- “需要建立规范再吸收”

Do not use this component for small snippets, single blog posts, or simple tools unless they are proposed as workflow foundations.

---

## 4. Required output package

A Finished Project Absorption Pack must contain at least:

```text
00-index.md
01-theory-and-doctrine.md
02-code-architecture.md
03-project-structure-and-scaffold.md
04-command-and-artifact-model.md
05-extension-and-ecosystem-model.md
06-fit-to-ai-method-wheel.md
07-absorption-decision.md
```

For smaller repos, files may be merged. For foundational repos like Spec Kit, keep them separate.

---

## 5. Required reading axes

### Axis 1 — Theory / Doctrine

Ask:

```text
What problem does the project claim to solve?
What worldview does it encode?
What terms does it introduce?
What process does it teach?
What is its anti-pattern?
```

Evidence files usually include:

```text
README.md
docs/concepts/*
docs/guides/*
architecture docs
RFCs
command docs
templates
```

### Axis 2 — Code / Implementation

Ask:

```text
What is the executable entrypoint?
What modules implement the core behavior?
What data/config files are written?
What state does it manage?
How does it install, update, remove, or dispatch work?
```

Output must include concrete file paths and the main data flow.

### Axis 3 — Project Structure / Scaffold

Ask:

```text
What does the project generate?
What folders/files become the user's project scaffold?
What templates are copied?
What scripts run?
What manifests/state files exist?
```

Output must distinguish source repo layout from generated target-project layout.

### Axis 4 — Command / Artifact Model

Ask:

```text
What commands are user-facing?
What artifacts does each command read and write?
Which artifacts are source-of-truth vs derived?
What quality gates exist between commands?
```

### Axis 5 — Extension / Ecosystem Model

Ask:

```text
How does the project extend itself?
How are plugins/presets/integrations/workflows installed?
What is the conflict-resolution model?
What security or trust assumptions exist?
```

### Axis 6 — Fit / Non-fit

Classify each borrowed part as:

```text
ADOPT        — safe to internalize directly
BRIDGE       — map into an existing A/B/C/D/E/F component
MERGE        — combine with an existing internal component
PATTERN_ONLY — borrow design pattern, not code/process
WATCH        — promising but insufficiently proven
REJECT       — not suitable
```

---

## 6. Absorption gates

A project is not ready for C-port synthesis until these are true:

```text
1. Theory summary exists.
2. Code architecture summary exists.
3. Scaffold/generated layout summary exists.
4. Command/artifact map exists.
5. Extension/ecosystem model exists if the repo has plugins/integrations.
6. Fit/non-fit table exists.
7. Risks and rollback boundaries are explicit.
8. The target insertion point in AI Method Wheel is named.
```

If any are missing, route back to B2 instead of producing a final bridge.

---

## 7. Target insertion patterns

A mature external project can enter the Method Wheel through one or more of these insertion points:

```text
A-port: demand/control vocabulary or clarification method
B-port: source/evidence gathering and compression method
B2: finished project absorption method
C-port: theory/spec/plan synthesis framework
D-port: scaffold, scripts, task queues, CLI execution model
E-port: analyzer/checker/verification gates
F-port: governance/constitution/owner approval model
Skill layer: reusable skills/templates/prompts
Harness layer: workflow engine, state, resume, gates
```

A foundational project should almost never be inserted as a single blob. It should be decomposed across the relevant ports.

---

## 8. Default stance

The default decision is not `ADOPT`. The default is:

```text
UNDERSTAND → CLASSIFY → BRIDGE/MERGE/PATTERN_ONLY → VERIFY → PROMOTE
```

Do not promote external project assumptions into baseline until the Method Wheel has an explicit rollback path and E/F review.
