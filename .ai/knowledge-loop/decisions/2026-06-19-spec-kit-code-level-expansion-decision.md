# A-Port Absorption Decision: Spec Kit code-level expansion

- Date: 2026-06-19
- Source Pack: `.ai/knowledge-loop/sources/2026-06-19-github-spec-kit-code-review.md`
- Source repo: https://github.com/github/spec-kit
- Upstream commit inspected: `487af97864901462874f18f1c7f8d8adec0b7ddd`
- Previous decision: `.ai/knowledge-loop/decisions/2026-06-17-spec-kit-absorption-decision.md`
- Decision: `PARTIAL_ACCEPT_EXPAND`

---

## 1. Decision

Spec Kit can and should improve the AI Method Wheel, but as a **Spec Kit bridge layer**, not as a replacement control plane.

The accepted framing:

```text
AI Method Wheel = higher-level A/B/C/D/E/F control plane
Spec Kit = spec-driven artifact spine + CLI/tooling pattern
```

Therefore:

```text
Absorb Spec Kit's artifact semantics, persistence vocabulary, read-only analyze gate, presets/extensions/workflows ideas, and Hermes integration awareness.
Do not adopt broad direct `speckit.implement` as the default execution path.
```

---

## 2. What changed after code-level review

The previous decision already accepted Spec Kit as a Spec Spine:

```text
constitution → specify → clarify/checklist → plan → tasks → analyze → bounded implement
```

This review adds four new findings:

1. Spec Kit has explicit built-in **Hermes integration** that installs `speckit-*` commands as Hermes skills.
2. Spec Kit's **presets** are a strong pattern for priority-ordered skill/template layering.
3. Spec Kit's **extensions** are a strong pattern for external skill governance, but require source review before installation.
4. Spec Kit's **workflows** support run/resume/status, which is useful as a pattern for A-mode replay/evolution, but still needs AI Method Wheel gates.

---

## 3. A/B/C/D/E/F mapping

```text
A-port:
  Raw intent → spec candidate
  Use Spec Kit's specify/clarify/checklist ideas
  Still owns route, authority, non-goals, and acceptance criteria

B-port:
  Source Pack before adopting external extensions/presets/skills
  Evidence quality and fit decision

C-port:
  plan/research/data-model/contracts/quickstart as theory/implementation package

D-port:
  tasks.md and bounded implementation as maker queue
  Codex/agent gets one bounded task slice, not vague owner intent

E-port:
  analyze-style read-only consistency check
  spec ↔ plan ↔ tasks ↔ checklist ↔ constitution/AGENTS

F-port:
  review-spec/review-plan/constitution or baseline changes require owner gate
```

---

## 4. Adoption classification

### ADOPT

- Durable spec artifact spine.
- `[NEEDS CLARIFICATION]` markers for unresolved high-impact unknowns.
- Prioritized independently testable user stories.
- Functional Requirement IDs and measurable Success Criteria IDs.
- Read-only `analyze` gate before implementation.
- Spec persistence model vocabulary.

### BRIDGE

- `speckit.specify` → A-port Demand Grilling Brief / spec candidate.
- `speckit.plan` → C-port theory/technical plan package.
- `speckit.tasks` → D-port bounded maker queue / GitHub issue candidate.
- `speckit.analyze` → E-port read-only checker.
- `speckit.workflow` → A/E controlled run-state pattern.

### MERGE

- Presets/extensions with internal skill layering and external GitHub skill governance.
- Workflow run/resume/status with A-mode replay and evolution logs.

### PATTERN_ONLY

- CLI integration registry and catalog architecture.
- Hermes integration implementation, until local profile behavior is verified.

### REJECT AS BASELINE

- Spec-as-source as default for this user's current workflow.
- Direct `speckit.implement` from vague natural language.
- Installing global `speckit-*` Hermes skills without A/E review and profile-path check.
- Replacing A/B/C/D/E/F with a single linear Spec Kit flow.

---

## 5. Recommended next method-wheel update

Create a dedicated bridge method file:

```text
.ai/methods/spec-kit-bridge-layer.md
```

It should document:

```text
Spec Kit command/artifact → A/B/C/D/E/F mapping
Hermes integration caution and profile-path check
Preset/extension governance rules
Spec persistence selection rule
When to use Spec Kit manually vs when to only borrow the pattern
```

This is a C-port synthesis/update task after B Source Pack is complete.

---

## 6. Protection rules

- Do not run `specify init --here --force` in the AI Method Wheel repo without an explicit owner decision and clean git branch.
- Do not install global Hermes skills until the active Hermes profile path and uninstall behavior are confirmed.
- Do not let Spec Kit community extensions/presets bypass external skill ADOPT/BRIDGE/MERGE/REJECT/PATTERN_ONLY review.
- Keep AI Method Wheel as control plane; Spec Kit remains artifact spine/tooling bridge.
