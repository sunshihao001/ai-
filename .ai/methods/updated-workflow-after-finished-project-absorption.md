# Updated AI Method Wheel After Finished Project Absorption

> Status: v0.1  
> Trigger source: owner correction during Spec Kit review  
> Core change: mature external projects must pass through `B2 Finished Project Absorption` before they are allowed to reshape the AI Method Wheel.

---

## 1. Why the workflow changed

The old shortcut was too shallow:

```text
external repo link
→ read README / command list
→ decide whether to bridge into A/B/C/D/E/F
```

That is not enough for a mature project like GitHub Spec Kit because a finished project contains multiple layers:

```text
theory / doctrine
→ user workflow
→ executable CLI/code architecture
→ generated scaffold
→ command and artifact model
→ integrations/extensions/presets/workflows
→ tests / release / operational model
→ ecosystem and trust boundaries
```

If the Method Wheel jumps directly from source discovery to bridge decision, A-port will make a conceptual decision before B/C actually understand the project.

Therefore the workflow now has a new mandatory component:

```text
B2 Finished Project Absorption
```

---

## 2. Updated top-level workflow

### Previous method wheel

```text
A demand/control
→ B source/evidence pack
→ C theory/spec synthesis
→ D repo landing / maker
→ E verification / checker
→ F owner decision
```

### Updated method wheel

```text
A demand/control
→ B source/evidence pack
→ B2 finished-project absorption pack
→ A absorption decision
→ C bridge/spec/method synthesis
→ D repo landing / maker
→ E verification / checker
→ F owner decision
```

The new workflow does **not** replace A/B/C/D/E/F. It inserts a project-understanding layer between raw evidence and synthesis.

---

## 3. What B2 does

B2 converts a complete external project into an internal understanding package.

Its output is not a recommendation yet. Its output is a normalized map:

```text
What theory does this project teach?
How does the code implement that theory?
What scaffold does it generate?
What artifacts become source of truth?
What commands/gates change the user workflow?
How does it extend itself?
What should be adopted, bridged, merged, watched, or rejected?
```

For foundational projects, B2 must produce separate documents:

```text
00-index.md
01-theory-and-doctrine.md
02-code-architecture.md
03-project-structure-and-scaffold.md
04-command-and-artifact-model.md
05-extension-and-ecosystem-model.md
06-fit-to-ai-method-wheel.md
07-absorption-decision.md or knowledge-loop decision update
```

Spec Kit is the first concrete example:

```text
.ai/research/spec-kit/
```

---

## 4. Updated port responsibilities

### A-port — demand/control + absorption framing

A no longer asks only:

```text
Can this repo improve our workflow?
```

A must first classify the request:

```text
Is this a small source, a tool, or a finished project?
```

If it is a mature project, A routes to B2 and defines the absorption question:

```text
What exactly are we trying to learn from this project?
Which parts may affect baseline workflow?
What is forbidden until B2 finishes?
```

A also makes the post-B2 decision:

```text
ADOPT / BRIDGE / MERGE / PATTERN_ONLY / WATCH / REJECT
```

### B-port — source collection

B still collects evidence, but it is not enough for mature projects.

B supplies:

```text
repo clone / docs / README / code entrypoints / tests / release notes / examples / external references
```

Then B passes evidence to B2 instead of jumping directly to C.

### B2 — finished-project absorption

B2 is the new understanding layer.

It reads across theory, code, scaffold, commands, artifacts, extensions, workflows, and ecosystem. It distinguishes:

```text
source repo layout
vs
what the tool generates inside a target project
vs
what behavior it expects from the human/agent workflow
```

### C-port — synthesis after understanding

C no longer synthesizes from raw repo impressions. C receives the B2 pack and produces bridge/method/spec updates.

For Spec Kit, C uses:

```text
Spec Kit = spec/artifact spine
AI Method Wheel = control plane
```

### D-port — bounded landing

D implements only bounded repo changes after A/C/E gates.

For Spec Kit-style projects, D should not globally install tools or copy integrations by default. D lands docs, templates, scripts, or isolated experiments first.

### E-port — checker and anti-shallow-adoption gate

E must verify:

```text
Did B2 cover all required axes?
Does the bridge decision follow evidence?
Did C over-absorb the external project?
Are rollback boundaries explicit?
Are validation scripts updated?
```

For Spec Kit specifically, E also inherits `/speckit.analyze` as a pattern: read-only cross-artifact consistency checking.

### F-port / owner — baseline approval

F approves baseline-level changes:

```text
new permanent workflow phase
new global port responsibility
new governance rule
new install/runtime dependency
new self-improving skill path
```

B2 can propose such changes, but cannot silently promote them.

---

## 5. Updated workflow for absorbing a mature repo

Use this when the owner says:

```text
先了解这个项目到底是什么
不要只是看 README
要理解理论、代码、项目结构、脚手架
之后再判断如何加入工作流
```

Mandatory flow:

```text
1. A frames the absorption question.
2. B gathers source material and clones/reads the repo.
3. B2 creates the finished-project absorption pack.
4. E checks whether the B2 pack is complete enough.
5. A makes an absorption decision: ADOPT / BRIDGE / MERGE / PATTERN_ONLY / WATCH / REJECT.
6. C creates bridge or method updates from the accepted parts.
7. D lands bounded repo changes.
8. E runs validation and consistency checks.
9. F/owner approves baseline or risky changes.
```

Stop rule:

```text
If theory, code architecture, scaffold, command/artifact model, extension model, or fit table is missing, do not produce a final bridge decision. Route back to B2.
```

---

## 6. What changed because of Spec Kit

Spec Kit changed the Method Wheel in two ways.

### Change 1 — it added the Spec Spine

Spec Kit contributes the artifact spine:

```text
constitution
→ specify
→ clarify
→ checklist
→ plan
→ tasks
→ analyze
→ implement
→ converge/repair
```

Mapped into the Method Wheel:

```text
constitution      → F/A governance
specify/clarify   → A WHAT stabilization
defensive checklist → A/E ambiguity and quality gate
plan/research/contracts → C HOW package
tasks             → D bounded maker queue
analyze           → E read-only consistency checker
implement         → D execution only after gates
converge          → E→D repair loop candidate
```

### Change 2 — it exposed the need for B2

The first bridge was not wrong, but it was incomplete. Treating Spec Kit only as slash commands misses:

```text
specify-cli architecture
integration registry
manifest/state tracking
agent command installation
extensions
presets
workflows
bundles
catalogs
scaffold generation
```

Therefore Spec Kit becomes both:

```text
1. a source of SDD patterns
2. the first test case proving that finished-project absorption is needed
```

---

## 7. New default mental model

The Method Wheel now has three different source intake levels:

| Level | Source type | Workflow |
| --- | --- | --- |
| B1 | article/thread/simple source | B source pack → A decision → C synthesis |
| B2 | mature repo / finished project | B source pack → B2 absorption pack → E check → A decision → C synthesis |
| B3 | ecosystem/platform family | multiple B2 packs → comparison frame → architecture decision |

Spec Kit is B2.

A future example of B3 would be comparing multiple agent workflow platforms or multiple skill ecosystems before changing the Method Wheel baseline.

---

## 8. Updated operating rules

1. Do not bridge a mature repo after reading only README and command names.
2. Do not install external workflow tools globally before B2/E/F review.
3. Separate project theory from implementation code.
4. Separate source repo structure from generated target-project scaffold.
5. Separate user-facing workflow from extension/plugin architecture.
6. Use classification labels: `ADOPT`, `BRIDGE`, `MERGE`, `PATTERN_ONLY`, `WATCH`, `REJECT`.
7. Keep baseline changes as reviewable diffs, not hidden prompt drift.
8. Add validation markers when a new method component becomes baseline.
9. Treat chat as working context; repo files remain the durable source of truth.

---

## 9. Practical result for future work

When the owner drops a serious GitHub project and asks whether it can improve the AI workflow, the correct response is no longer:

```text
I read the README; here is how to map it.
```

The correct response is:

```text
I will build a Finished Project Absorption Pack first:
- theory/doctrine
- code architecture
- scaffold/generated project structure
- command/artifact model
- extension/ecosystem model
- fit/non-fit table
Then we decide how it changes A/B/C/D/E/F.
```

That is the new workflow cognition.
