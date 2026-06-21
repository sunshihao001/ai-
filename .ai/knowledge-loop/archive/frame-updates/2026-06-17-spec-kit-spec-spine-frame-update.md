# Frame Update Proposal: Add Spec Kit-Inspired Spec Spine

- Status: proposal / partial accept
- Baseline affected: additive only; do not replace current A/B/C/D/E/F model

## Proposed new concept

Add a named **Spec Spine** layer to the AI Method Wheel.

```text
A端 Demand-Control Brief
→ constitution / governance constraints
→ specs/<feature>/spec.md
→ clarification answers and [NEEDS CLARIFICATION] resolution
→ specs/<feature>/plan.md
→ research.md / data-model.md / contracts / quickstart.md when relevant
→ specs/<feature>/tasks.md
→ checklists/*.md
→ E-port analyze report
→ D/Codex bounded implementation
→ E-port verification report
→ PR / ADR / handoff
```

## Port mapping

### A端

Owns intent, scope, non-goals, acceptance criteria, unknown markers, and spec persistence choice.

A端 must decide:

```text
spec-first / spec-anchored / spec-as-source
flow-back / flow-forward / living spec
```

Recommended default:

```text
method-wheel or baseline-changing work: spec-anchored + flow-forward
normal repo implementation: spec-anchored + controlled flow-back
throwaway spike: spec-first
```

### B端

Provides research/context that fills `research.md` or source packs. B should not rewrite baseline specs without A decision.

### C端

Turns accepted A/B context into theory, architecture, or plan artifacts. C may draft `plan.md`, `data-model.md`, `contracts/`, or `quickstart.md`.

### D端

Lands bounded changes or asks Codex to implement one `tasks.md` slice. D must not execute the entire broad task list if A/E require narrower slicing.

### E端

Runs read-only consistency analysis before implementation:

```text
spec.md ↔ plan.md ↔ tasks.md ↔ checklist.md ↔ AGENTS/constitution ↔ tool policy
```

E also verifies after implementation with real tool output.

### F端

Approves major persistence-model changes, baseline updates, broad implementation scope, and risky governance changes.

## Template implications

Future templates should include fields for:

- spec persistence model;
- artifact mutation model;
- `[NEEDS CLARIFICATION]` list;
- independently testable user stories;
- E-port read-only analyze result;
- Codex/D implementation slice boundary.

## Non-goals

- Do not install or run Spec Kit automatically in every repo.
- Do not let Spec Kit replace protective knowledge-update gates.
- Do not make `/speckit.implement` the default execution path for complex work.
- Do not collapse multi-port control into a single agent command chain.
