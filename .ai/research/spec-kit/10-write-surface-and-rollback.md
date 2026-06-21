# Spec Kit write-surface and rollback map

> Pack: `.ai/research/spec-kit/`
> Purpose: summarize where Spec Kit writes, what is derived, and how to roll back safely.

---

## 1. Write surface table

| Path / surface | Written by | Scope | Risk level | Source of truth | Rollback path | Method Wheel stance |
|---|---|---|---|---|---|---|
| `.specify/memory/constitution.md` | `speckit.constitution` | project-local | low | yes | overwrite from previous constitution or delete generated folder | ADOPT as governance pattern |
| `specs/<feature>/spec.md` | `speckit.specify` / `speckit.clarify` | project-local | low | yes | revert spec commit or restore from git | ADOPT as spec spine |
| `specs/<feature>/checklists/*.md` | `speckit.checklist` | project-local | low | derived | regenerate from spec | ADOPT as quality gate pattern |
| `specs/<feature>/plan.md` / `research.md` / `data-model.md` / `contracts/` / `quickstart.md` | `speckit.plan` | project-local | low-medium | mostly derived | revert plan commit or re-run plan generation | BRIDGE into C-port |
| `specs/<feature>/tasks.md` | `speckit.tasks` | project-local | low-medium | derived | regenerate from plan/spec | ADOPT as D queue pattern |
| `.specify/*` scaffold | `specify init` | project-local | medium | mixed | delete `.specify/` or reset repo commit | PATTERN_ONLY until sandbox verified |
| `.hermes/skills/speckit-*` or `~/.hermes/skills/speckit-*` | Hermes integration / runtime install | profile/global | high | no | remove generated skill dirs; avoid baseline install | REJECT as baseline without wrapper |
| `.specify/workflows/runs/<run_id>/state.json` | workflow engine | project-local | low-medium | derived | delete run state; rerun workflow | BRIDGE as harness run-state pattern |

---

## 2. Rollback rules

1. Prefer git revert or restoring committed artifacts for repo-local files.
2. Treat any profile/global skill write as a guarded runtime experiment only.
3. Never promote direct Hermes skill installation to baseline without wrapper/adapter and owner approval.
4. Separate generated state from source-of-truth artifacts before using the project as a workflow foundation.

---

## 3. Evidence notes

- The strongest rollback risk is not the spec artifacts; it is the runtime integration and profile/global skill write path.
- Spec Kit should remain a reference spec spine until sandboxed runtime behavior is fully controlled.
