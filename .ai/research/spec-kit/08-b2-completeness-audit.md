# Spec Kit B2 Completeness Audit

> Date: 2026-06-20  
> Audited pack: `.ai/research/spec-kit/`  
> Audit template: `.ai/templates/finished-project-absorption/e-completeness-checklist.template.md`  
> Verdict: `PARTIAL PASS — sufficient for current bridge decision, but needs v0.2 hardening before treating Spec Kit as a fully reusable gold-standard B2 example.`

---

## 1. Audit purpose

This file checks whether the existing Spec Kit B2 pack satisfies the newly created Finished Project Absorption template standard.

The goal is not to redo the whole Spec Kit study. The goal is to answer:

```text
Does the current Spec Kit pack already meet the B2 standard?
If not, what exactly is missing before future projects can copy it as the model example?
```

---

## 2. Current pack inventory

Existing Spec Kit B2 pack files:

```text
.ai/research/spec-kit/00-index.md
.ai/research/spec-kit/01-theory-and-doctrine.md
.ai/research/spec-kit/02-code-architecture.md
.ai/research/spec-kit/03-project-structure-and-scaffold.md
.ai/research/spec-kit/04-command-and-artifact-model.md
.ai/research/spec-kit/05-extension-and-ecosystem-model.md
.ai/research/spec-kit/06-fit-to-ai-method-wheel.md
.ai/research/spec-kit/07-absorption-decision.md
```

Newly added audit file:

```text
.ai/research/spec-kit/08-b2-completeness-audit.md
```

---

## 3. E-port checklist result

| Required B2 coverage | Status | Evidence | Gap |
|---|---|---|---|
| Theory / doctrine documented with source evidence | PASS | `01-theory-and-doctrine.md` covers SDD, anti-pattern, artifact doctrine, persistence models, Method Wheel mapping. | Needs more explicit source path citations per claim. |
| Code architecture names concrete entrypoints, modules, state/config flow | PASS | `02-code-architecture.md` names `specify-cli`, `src/specify_cli/__init__.py`, `commands/init.py`, integration, extension, preset, workflow, bundle modules, and state files. | Could add a diagram-level flow and exact test command evidence. |
| Source repo layout separated from generated target-project scaffold | PASS | `03-project-structure-and-scaffold.md` separates source layout from generated `.specify/` and `specs/<feature>/` scaffold. | Could add generated scaffold provenance by command/template source. |
| Command / artifact model lists reads, writes, source-of-truth status, and gates | PARTIAL PASS | `04-command-and-artifact-model.md` maps commands, inputs, outputs, gates, Method Wheel roles. | Missing explicit source-of-truth vs derived column per artifact. |
| Extension / ecosystem model covers integrations, presets/plugins/workflows, trust boundaries | PASS | `05-extension-and-ecosystem-model.md` covers integrations, extensions, presets, workflows, bundles, catalogs, and trust. | Could add a risk table with global/profile writes and rollback quality. |
| Tests / release / packaging / operational safety evidence recorded | PARTIAL PASS | `02-code-architecture.md` section 10 lists broad test/safety/release areas. Runtime experiment docs record Hermes integration risk. | Needs direct commands, file paths, and results for tests/release/packaging checks. |
| Fit/non-fit table maps parts to A/B/B2/C/D/E/F/Harness/Skill insertion points | PASS | `06-fit-to-ai-method-wheel.md` maps Spec Kit layers to A/C/F/D/E/Harness/Skill and classifies ADOPT/BRIDGE/MERGE/PATTERN_ONLY/REJECT. | Could expand to an explicit full port matrix including B2 and Skill columns for every component. |
| Risks, rollback boundaries, and forbidden shortcuts explicit | PASS | `07-absorption-decision.md` sections 6–11 cover direct install, Hermes integration boundary, WATCH/REJECT, owner approval, runtime integration boundary. | Could move rollback into a concise table for faster reuse. |
| Final decision uses ADOPT / BRIDGE / MERGE / PATTERN_ONLY / WATCH / REJECT AS BASELINE | PASS | `07-absorption-decision.md` records `PARTIAL_ACCEPT_EXPAND` with ADOPT/BRIDGE/MERGE/PATTERN_ONLY/WATCH/REJECT boundaries. | Decision class is clear, but future packs should also include a one-line final label from the standard set. |

---

## 4. Anti-shallow-adoption questions

### 4.1 Did we inspect code, not only README and marketing docs?

Verdict: `PASS`

Evidence:

```text
02-code-architecture.md
03-project-structure-and-scaffold.md
05-extension-and-ecosystem-model.md
```

The pack names concrete code paths including:

```text
src/specify_cli/__init__.py
src/specify_cli/commands/init.py
src/specify_cli/integrations/*
src/specify_cli/extensions.py
src/specify_cli/presets/*
src/specify_cli/workflows/engine.py
src/specify_cli/commands/bundle/*
```

### 4.2 Did we distinguish project theory from implementation mechanics?

Verdict: `PASS`

Evidence:

```text
01-theory-and-doctrine.md      → theory / doctrine
02-code-architecture.md        → implementation mechanics
03-project-structure-and-scaffold.md → generated scaffold
```

### 4.3 Did we distinguish source repo structure from generated scaffold?

Verdict: `PASS`

Evidence:

```text
03-project-structure-and-scaffold.md
```

It explicitly separates:

```text
source repo areas: README/docs/templates/scripts/src/integrations/extensions/presets/workflows/tests
from generated target project: .specify/ and specs/<feature>/
```

### 4.4 Did we identify all profile/global writes before install or runtime use?

Verdict: `PARTIAL PASS`

Evidence:

```text
07-absorption-decision.md
.ai/methods/spec-kit-runtime-integration-plan.md
.ai/research/spec-kit-runtime/experiment-2026-06-20.md
.ai/methods/spec-kit-hermes-wrapper-adapter.md
```

The current pack identifies the Hermes profile/global-write risk, especially that direct Hermes integration may target generic `~/.hermes/skills` instead of the active profile.

Gap:

```text
The B2 pack itself should include a compact generated-files/write-surface table rather than relying on external runtime docs.
```

### 4.5 Did we avoid promoting external commands that bypass A/B/C/E/F gates?

Verdict: `PASS`

Evidence:

```text
07-absorption-decision.md
```

The decision rejects:

```text
raw owner idea → /speckit.implement
replacing A/B/C/D/E/F with a linear Spec Kit workflow
installing global Hermes skills without profile check and rollback
```

### 4.6 Did we define objective verification before baseline changes?

Verdict: `PARTIAL PASS`

Evidence:

```text
scripts/validate-ai-method-wheel.py
.ai/research/spec-kit-runtime/experiment-2026-06-20.md
```

Gap:

```text
The Spec Kit B2 pack should include its own E-port verification evidence section listing commands run, source commit, local path, and any failed/blocked checks.
```

### 4.7 Did we define rollback before adoption?

Verdict: `PARTIAL PASS`

Evidence:

```text
07-absorption-decision.md section 11
spec-kit-hermes-wrapper-adapter.md
```

Gap:

```text
Rollback is defined for runtime integration, but not summarized as a B2-level rollback table for every accepted/bridged component.
```

---

## 5. Overall verdict

```text
PARTIAL PASS
```

Meaning:

```text
The existing Spec Kit pack is good enough to justify the current bridge decision:
Spec Kit = Spec Spine, AI Method Wheel = control plane, B2 is required for mature repos.

But it is not yet complete enough to serve as the final gold-standard B2 example for all future mature external projects.
```

The pack is stronger than the earlier shallow review because it covers theory, code, scaffold, command/artifact model, ecosystem, fit, and decision boundaries. The remaining gaps are mostly **audit hardening and reusability** rather than conceptual understanding.

---

## 6. Required repairs before calling Spec Kit B2 v1.0 complete

### Repair 1 — Add explicit source evidence table

Create or extend `00-index.md` with a table:

```text
claim / evidence file / lines or section / status / notes
```

Purpose:

```text
Make source grounding auditable without rereading the whole repo.
```

### Repair 2 — Strengthen command/artifact source-of-truth model

Update `04-command-and-artifact-model.md` to add columns:

```text
source-of-truth / derived
artifact owner
mutation rule
validation rule
```

Purpose:

```text
Prevent future C/D agents from treating derived artifacts as editable source of truth.
```

### Repair 3 — Add write-surface and rollback table

Add a compact table either to `02-code-architecture.md` or a new runtime appendix:

```text
path written / command / scope / profile-global risk / rollback path / Method Wheel stance
```

Purpose:

```text
Make direct install/runtime use impossible to approve accidentally.
```

### Repair 4 — Add verification evidence section

Add command/file evidence for:

```text
repo commit reviewed
source tree inspected
validation command run
runtime sandbox result
known blocked checks
```

Purpose:

```text
Avoid reporting B2 as complete only from reading/synthesis.
```

### Repair 5 — Add final E-port checklist file for Spec Kit

Copy the template:

```text
.ai/templates/finished-project-absorption/e-completeness-checklist.template.md
```

into the pack as a project-specific checklist, for example:

```text
.ai/research/spec-kit/e-completeness-checklist.md
```

Purpose:

```text
Make E-port pass/fail evidence local to the pack.
```

---

## 7. Recommended next action

Do not redo the whole B2 pack from scratch. Instead run a v0.2 hardening pass:

```text
1. Patch 00-index.md with source evidence inventory.
2. Patch 04-command-and-artifact-model.md with source-of-truth columns.
3. Add e-completeness-checklist.md for Spec Kit.
4. Add write-surface / rollback table.
5. Run validate-ai-method-wheel.py.
```

After that, the verdict can likely move from:

```text
PARTIAL PASS
```

to:

```text
PASS — sufficient as reusable B2 example
```

---

## 8. Current workflow state

Current state after this audit:

```text
B2 template system exists.
Spec Kit has an existing B2 pack.
This audit confirms the pack is directionally correct but needs v0.2 hardening.
Next stage should be Spec Kit B2 Pack v0.2 repair, not another theory discussion.
```
