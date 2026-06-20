# Spec Kit Hermes Adapter Generator Report

> Generated repo-local wrapper drafts only. No Hermes profile writes were performed.

## Source

- Source repo: https://github.com/github/spec-kit
- Source path: `C:\Users\Administrator\spec-kit-source`
- Source commit: `487af97864901462874f18f1c7f8d8adec0b7ddd`

## Safety Invariants

- Does not run `specify init --integration hermes`.
- Does not write `~/.hermes`.
- Does not write the active `cangwei` profile.
- Generates `speckit-implement` as `disabled-handoff-only`.

## Generated Commands

- `speckit-analyze`: `enabled-draft` → `E` — Read-only cross-artifact checker; no mutation.
- `speckit-checklist`: `enabled-draft` → `A/E` — Check requirement/spec quality; do not implement.
- `speckit-clarify`: `enabled-draft` → `A` — Ask only high-impact questions and write accepted answers back to durable spec.
- `speckit-constitution`: `gated-draft` → `F/A` — Governance/baseline command; owner/F approval required before use.
- `speckit-converge`: `enabled-draft` → `E→D` — Append-only repair task generation after checker finding.
- `speckit-implement`: `disabled-handoff-only` → `D` — Do not expose as raw skill. Represent only as D-port handoff after A/B/C/E/F gates.
- `speckit-plan`: `enabled-draft` → `C` — Requires stable WHAT and accepted evidence/caveat state before HOW.
- `speckit-specify`: `enabled-draft` → `A` — WHAT/spec candidate only; do not choose technology stack.
- `speckit-tasks`: `enabled-draft` → `D-prep` — Produce bounded maker queue only; does not grant execution authority.
- `speckit-taskstoissues`: `gated-draft` → `D/F` — GitHub side-effect handoff; requires repo/remote confirmation and owner approval.

## Next E-Port Review

Check wrapper guardrails, command policy, manifest, and generated diffs before any promotion.
Initial promotion subset, if approved later: `speckit-specify`, `speckit-clarify`, `speckit-checklist`, `speckit-analyze`.
