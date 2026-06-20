# Spec Kit Command and Artifact Model

## Command map

| Command | Primary role | Main inputs | Main outputs | Method Wheel mapping |
| --- | --- | --- | --- | --- |
| `/speckit.constitution` | Define/update project principles | user principles, existing constitution, templates | `.specify/memory/constitution.md`, sync impact report | F/A governance baseline |
| `/speckit.specify` | Create WHAT spec | feature description, spec template, constitution | `specs/<feature>/spec.md`, requirements checklist | A demand/spec candidate |
| `/speckit.clarify` | Resolve ambiguity | current `spec.md`, constitution | updated `spec.md` clarifications | A deep-path clarification |
| `/speckit.checklist` | Test requirement quality | `spec.md`, user checklist theme | `checklists/*.md` | A/E requirement quality gate |
| `/speckit.plan` | Design HOW | `spec.md`, constitution, plan template | `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` | C synthesis |
| `/speckit.tasks` | Generate maker queue | `plan.md`, `spec.md`, design docs | `tasks.md` | D task queue preparation |
| `/speckit.analyze` | Read-only consistency check | `spec.md`, `plan.md`, `tasks.md`, constitution | analysis report | E checker |
| `/speckit.implement` | Execute tasks | `tasks.md`, plan/spec/design docs | code changes, completed task checkboxes | D maker execution |
| `/speckit.converge` | Compare implementation with intent | code + spec/plan/tasks | appended convergence tasks | E→D repair loop |
| `/speckit.taskstoissues` | Convert tasks to issues | `tasks.md` | GitHub issue candidates | D/F issue handoff |

---

## Artifact spine

```text
constitution.md
→ spec.md
→ checklists/*.md
→ plan.md
→ research.md / data-model.md / contracts / quickstart
→ tasks.md
→ code
→ analyze/converge reports
```

This is the spine to bridge into the AI Method Wheel.

---

## Gate semantics

```text
WHAT/HOW boundary: specify does not choose technology; plan begins HOW.
Clarification boundary: clarify asks only high-impact questions.
Analyze boundary: analyze is read-only.
Implement boundary: implement executes tasks.md, not owner chat.
Converge boundary: converge appends repair tasks instead of rewriting history.
```

Method Wheel translation:

```text
A cannot leak into C too early.
E can block/report caveats but must not silently rewrite A/C/D artifacts.
D receives bounded tasks only after A/B/C/E/F gates.
E findings become D repair tasks or A/C update proposals, not silent drift.
```
