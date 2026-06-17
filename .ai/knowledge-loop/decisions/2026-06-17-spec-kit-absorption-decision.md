# A-Port Absorption Decision: GitHub Spec Kit

- Date: 2026-06-17
- Source: https://github.com/github/spec-kit
- Upstream commit: `3e69233adb6bce3ce351fb8bd1cc84c3f938546a`
- Decision owner: A-port demand/control
- Decision: `PARTIAL_ACCEPT`
- Promotion scope: additive method-wheel knowledge + template guidance, not baseline replacement

## Decision

Absorb GitHub Spec Kit as the user's **Spec Spine reference**:

```text
constitution → specify → clarify/checklist → plan → tasks → analyze → bounded implement
```

Do not replace the AI Method Wheel with Spec Kit. The Method Wheel remains the higher-level control plane:

```text
A demand/control → B evidence → C theory/spec → D repo landing/maker → E verification/checker → F owner gate
```

## What is accepted

- Specs as durable, reviewable artifacts.
- Constitution/governance principles as non-negotiable planning constraints.
- `[NEEDS CLARIFICATION]` markers instead of guessed requirements.
- Prioritized independently-testable user stories.
- Read-only cross-artifact analyze gate before implementation.
- Explicit spec persistence model selection.
- Extensions/presets/hooks as a model for customizable method variants.

## What is not accepted as baseline

- Direct broad `/speckit.implement` without A/D/E scope control.
- Treating code as disposable generated output in every project.
- Blind installation of all Spec Kit commands/extensions into all repos.
- Replacing A/B/C/D/E/F port contracts with a single linear command set.

## Rollback / protection

Current V4 method-wheel baseline remains protected. If later Spec Kit adoption creates confusion or over-centralization, revert the Spec Spine update and keep only source/synthesis notes.
