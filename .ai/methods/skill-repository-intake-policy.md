# Skill Repository Intake Policy

> Status: v0.1  
> Purpose: decide whether an external skill-shaped repository should be installed as a skill, merged as a pattern, or escalated to B2 finished-project absorption.

---

## 1. Why this policy exists

Many external repositories are **skills**, not workflow-control projects. If they are treated like B2 finished projects, the Method Wheel gets noisy and overfit.

Use this policy to prevent:

```text
skill repo → accidental baseline absorption → workflow clutter
```

---

## 2. Default rule

```text
Most skill repositories are SKILL_LAYER or PATTERN_ONLY.
Only a small minority become B2.
```

A repository should only enter B2 if it changes the control plane, not just the capability catalog.

---

## 3. Classification ladder

### A. REFERENCE_ONLY

Use when the repo is useful to read, but should not affect the workflow.

Signals:

- style reference
- one-off idea
- no reusable workflow boundary
- no new artifact spine

### B. SKILL_LAYER

Use when the repo should become an installable or referenceable skill, but not a baseline method component.

Signals:

- single-purpose skill
- command/prompt/recipe package
- local task automation
- does not redefine A/B/C/D/E/F

### C. PATTERN_ONLY

Use when the repo teaches a pattern, but the implementation should not be copied.

Signals:

- useful layering / naming / command shape
- unsafe or noisy runtime model
- install path is too coupled to a specific environment

### D. B2_FINISHED_PROJECT

Use only when the repo is a mature workflow or control-plane project.

Signals:

- defines new workflow stages
- changes artifact lifecycle
- changes ownership / verification / rollback
- affects governance or runtime integration

---

## 4. Decision questions

Ask these in order:

1. Does this repo change the control plane or only add one capability?
2. Does it create new durable artifacts or only runtime prompts?
3. Does it require a new B2 absorption pack, or only a skill install?
4. Would installing it increase workflow noise more than value?
5. Can it be safely represented as a skill template instead of a baseline component?

If the answer is mostly “single capability, installable prompt, no control-plane change,” then do **not** do B2.

---

## 5. Recommended routes

| Repo type | Route | Output |
|---|---|---|
| simple skill repo | SKILL_LAYER | installable skill or skill catalog entry |
| reusable prompt/recipe repo | PATTERN_ONLY | pattern note, not baseline change |
| skill framework with registry / bundles / governance | B2 maybe | B2 absorption pack first |
| workflow engine / control-plane repo | B2 | full absorption, then A/C/D/E/F decision |

---

## 6. Handoff rules

### If SKILL_LAYER

- install or register as a skill
- keep it out of baseline methods
- reference from A/B/C only when relevant

### If PATTERN_ONLY

- record the pattern in a method note
- do not install by default
- keep runtime behavior unchanged

### If B2

- create the full finished-project absorption pack
- require E completeness audit
- only then decide ADOPT / BRIDGE / MERGE / WATCH / REJECT AS BASELINE

---

## 7. Anti-mistakes

- Do not B2-absorb every skill repo.
- Do not install skill repos into baseline method docs.
- Do not confuse a capability repository with a workflow-control repository.
- Do not let a skill repo silently redefine port boundaries.

---

## 8. Practical summary

```text
skill repo → usually SKILL_LAYER
framework repo → maybe B2
control-plane repo → B2
```

This policy is the missing filter that prevents the workflow from becoming overstuffed.