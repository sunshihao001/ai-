# Spec Kit B2 Source Evidence Appendix

> Purpose: make the existing Spec Kit B2 pack auditable at a glance.
> Pack scope: `.ai/research/spec-kit/`
> Date: 2026-06-20

---

## Evidence table

| Claim | Source path(s) | Evidence type | Notes |
|---|---|---|---|
| Spec Kit is a spec-driven development system, not only a command list | `01-theory-and-doctrine.md`, `07-absorption-decision.md` | doctrine / synthesis | WHAT-before-HOW, constitution, clarify, checklist, analyze, converge |
| `specify-cli` is the implementation package | `02-code-architecture.md` | code architecture | entrypoint and modules named explicitly |
| `specify init` generates project-local scaffold under `.specify/` | `03-project-structure-and-scaffold.md`, `02-code-architecture.md` | scaffold / code | source layout vs generated layout separated |
| Commands map to artifacts and gates | `04-command-and-artifact-model.md` | command/artifact model | now includes source-of-truth, derived, mutation, validation columns |
| Integrations / extensions / presets / workflows / bundles form an ecosystem | `05-extension-and-ecosystem-model.md` | ecosystem model | includes trust boundary and adoption caution |
| Spec Kit should bridge into Method Wheel, not replace it | `06-fit-to-ai-method-wheel.md` | fit analysis | classifies ADOPT / BRIDGE / MERGE / PATTERN_ONLY / WATCH / REJECT |
| Direct install/runtime use is a guarded experiment, not baseline | `07-absorption-decision.md` | decision / risk | runtime integration boundary and owner approval gates |
| B2 completeness is partial and needs hardening | `08-b2-completeness-audit.md` | E audit | residual hardening repairs recorded |

---

## Local verification pointers

- Review source pack anchor:
  - `00-index.md`
- Review command/mutation semantics:
  - `04-command-and-artifact-model.md`
- Review unsafe runtime boundary:
  - `07-absorption-decision.md`
- Review open hardening work:
  - `08-b2-completeness-audit.md`

---

## Remaining v0.2 hardening tasks

1. Add explicit source / lines / section citations where practical.
2. Add a compact write-surface / rollback table for generated files and profile-level risk.
3. Add a project-specific `e-completeness-checklist.md` copy for Spec Kit.
4. Keep the B2 pack reusable for future mature projects by preserving this evidence format.
