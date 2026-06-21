# Synthesis: Spec Kit vs Current AI Method Wheel

## Summary

GitHub Spec Kit supplies a mature **spec artifact spine**: constitution → spec → clarify/checklist → plan → tasks → analyze → implement. The user's AI Method Wheel is broader: it is a control-plane and multi-port orchestration system that uses specs as one durable layer but also governs evidence search, theory generation, repo landing, verification, owner approvals, Codex command policy, and continuous learning protection.

## Alignment map

- Spec Kit `constitution.md` → Method Wheel `AGENTS.md` / `.ai/method-wheel` / governance principles.
- `/speckit.specify` → A端 demand-control brief → `spec.md`.
- `/speckit.clarify` → A端 demand grilling; targeted questions and write answers back into spec.
- `/speckit.checklist` → A/E quality checklist generation.
- `/speckit.plan` → C端 theory/technical plan draft, with A-approved constraints.
- `/speckit.tasks` → D端 bounded maker task queue / GitHub issues.
- `/speckit.analyze` → E端 read-only cross-artifact consistency gate.
- `/speckit.implement` → D/Codex maker execution, but only after A/E gates and with bounded scope.
- Spec persistence models → Protective baseline policy and feature artifact lifecycle.
- Extensions/presets/hooks → Method Wheel skill/template customization, but behind review gates.

## What should update in the Method Wheel

### 1. Add a Spec Spine layer

```text
constitution/governance
→ spec.md
→ clarification answers
→ plan.md
→ research.md / data-model.md / contracts / quickstart
→ tasks.md
→ checklist(s)
→ analyze report
→ implementation / PR
```

### 2. Add explicit spec persistence choice

Before a feature starts, A端 should choose one of:

- spec-first: useful for throwaway exploration.
- spec-anchored: default for the user's real repos; spec remains a durable reference.
- spec-as-source: only for highly disciplined/re-generatable systems.

And mutation model:

- flow-back: implementation discoveries can update spec/plan/tasks.
- flow-forward: new requirement creates a new feature directory.
- living spec: `spec.md` is contract, derived docs regenerate.

Default recommendation: **spec-anchored + flow-forward for baseline-changing method work; spec-anchored + controlled flow-back for normal repo implementation discoveries.**

### 3. Strengthen A端 clarification output

Borrow from Spec Kit:

- max targeted questions rather than huge questionnaires;
- mark unknowns as `[NEEDS CLARIFICATION: ...]`;
- encode accepted answers back into the spec artifact;
- use acceptance scenarios and independently testable user stories.

### 4. Turn E端 into read-only analyze gate before D implementation

Before Codex/D implements, E should run a read-only consistency check:

```text
spec.md ↔ plan.md ↔ tasks.md ↔ checklist.md ↔ AGENTS/constitution
```

E must output blockers and never silently rewrite artifacts.

### 5. Avoid importing Spec Kit wholesale

Spec Kit is an SDD toolkit. The user's framework is a loop-control and multi-agent orchestration framework. Absorb the spine, not the whole organism.

## A-port protective decision

Decision: `PARTIAL_ACCEPT`

## E-port consistency check

Pass with caveat.

- Maker/checker separation remains intact if `/speckit.analyze` maps to E and `/speckit.implement` maps only to D.
- A/B/C/D/E/F roles remain stronger than Spec Kit's single command flow.
- Baseline protection remains intact because updates are additive and proposal-first.
- Caveat: `spec-as-source` and broad implementation commands can over-centralize power and should not be the default.
