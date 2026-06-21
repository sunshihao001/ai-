# Spec Kit B2 Absorption Decision

> Status: v0.1  
> Decision class: `PARTIAL_ACCEPT_EXPAND`  
> Source project: `github/spec-kit`  
> Local source reviewed: `C:/Users/Administrator/spec-kit-source`  
> Upstream commit referenced by pack: `487af97864901462874f18f1c7f8d8adec0b7ddd`  
> Applies to: AI Method Wheel / B2 Finished Project Absorption / Spec Spine bridge

---

## 1. Decision summary

Spec Kit should be absorbed as a **finished-project reference system**, not as a simple slash-command list and not as a wholesale replacement for the AI Method Wheel.

Decision:

```text
PARTIAL_ACCEPT_EXPAND
```

Meaning:

```text
Adopt the spec-driven artifact spine.
Bridge the user-facing commands into A/B/C/D/E/F.
Merge extension/preset/workflow concepts into internal skill governance.
Use direct CLI/Hermes integration only as a guarded runtime experiment.
Reject broad direct implementation from raw owner intent.
```

The one-line rule is:

```text
Spec Kit tells the AI what to build, in what order, and why;
the AI Method Wheel decides when the spec spine is mature enough to execute,
who verifies it, and who may approve baseline changes.
```

---

## 2. Why this decision changed the Method Wheel

The owner correction was that Spec Kit had not been understood deeply enough if it was treated only as:

```text
README + six commands + quick bridge mapping
```

Spec Kit is a finished project with multiple layers:

```text
spec-driven development theory
→ specify-cli implementation
→ generated .specify/ scaffold
→ command templates
→ artifact lifecycle
→ agent integration registry
→ extension / preset / workflow / bundle ecosystem
→ tests / packaging / release / operational cautions
```

Therefore the Method Wheel now needs the inserted component:

```text
B2 Finished Project Absorption
```

Correct route for mature external projects:

```text
A absorption question
→ B repo/source evidence
→ B2 finished-project absorption pack
→ E completeness check
→ A absorption decision
→ C bridge/method synthesis
→ D bounded landing
→ E validation
→ F owner approval for baseline or risky changes
```

---

## 3. ADOPT

These parts are safe to internalize as Method Wheel baseline vocabulary or artifact expectations.

### 3.1 Spec-driven artifact spine

Adopt:

```text
constitution / governance
→ spec.md
→ clarification answers
→ checklists
→ plan.md
→ research.md / data-model.md / contracts / quickstart.md
→ tasks.md
→ analyze report
→ bounded implementation
→ converge / repair when implementation and intent drift
```

Why:

```text
This gives AI work durable structure before code and prevents prompt-to-code drift.
```

### 3.2 WHAT before HOW

Adopt the rule:

```text
A stable WHAT must exist before C/D choose HOW or implement.
```

This strengthens A-port demand control.

### 3.3 Requirements checklist as English unit tests

Adopt the pattern that a requirement document should be testable in natural language before implementation:

```text
user stories
acceptance scenarios
functional requirements
measurable success criteria
edge cases
assumptions
[NEEDS CLARIFICATION] markers
```

### 3.4 Analyze as E-port read-only gate

Adopt `/speckit.analyze` as a Method Wheel checker pattern:

```text
read-only consistency check across constitution / spec / plan / tasks
```

A D-port implementation should not be treated as ready unless E has either passed this style of check or recorded accepted caveats.

### 3.5 Dependency-ordered task queue principles

Adopt:

```text
T001-style task IDs
[P] parallel markers
user-story phases
MVP-first sequencing
file paths per task
independent test criteria
```

---

## 4. BRIDGE

These parts should be mapped into existing Method Wheel ports, not copied as a separate linear workflow.

| Spec Kit layer | Method Wheel bridge | Rule |
| --- | --- | --- |
| constitution | F/A governance baseline | Owner approves baseline/risky changes. |
| specify | A-port WHAT stabilization | Convert raw intent into spec candidate. |
| clarify | A-port targeted ambiguity removal | Ask only high-impact questions; write answers back to artifact. |
| checklist | A/E quality gate | Test whether requirements/spec are complete enough. |
| plan | C-port HOW package | Choose technical approach only after WHAT is stable. |
| research | B/C evidence and decision record | Unknowns become research items, not guesses. |
| data-model | C-port domain/data model | Use only when the feature has real entities/data. |
| contracts | C/E interface contract | API/CLI/UI boundaries become checkable. |
| quickstart | E validation scenario | Defines how a human/checker proves the feature works. |
| tasks | D bounded maker queue | Tasks are execution units, not broad permission. |
| analyze | E read-only checker | No mutation during consistency analysis. |
| implement | D maker execution | Only after A/B/C/E/F gates. |
| converge | E→D repair loop | Use when implementation and intent diverge. |
| taskstoissues | D/F issue handoff | Convert tasks to GitHub issues only when slices are owner-approved. |

---

## 5. MERGE

These parts should be merged with existing internal governance rather than adopted as-is.

### 5.1 Presets → internal skill/template layering

Spec Kit presets show a useful precedence model:

```text
project override
→ high-priority preset
→ extension template
→ core template
```

Merge into Method Wheel skill governance as:

```text
project instructions
→ port-specific skill
→ auxiliary skill/template
→ baseline method docs
```

### 5.2 Extensions → external skill governance

Spec Kit extensions map directly to the user's external GitHub skill governance problem.

Merge with labels:

```text
ADOPT / BRIDGE / MERGE / PATTERN_ONLY / WATCH / REJECT
```

No external skill/extension should be installed merely because it exists.

### 5.3 Workflows → harness run/resume/gate model

Spec Kit workflows provide a pattern for:

```text
workflow run
workflow resume
workflow status
review gates
```

Merge into Method Wheel harness records, but preserve A/B/C/D/E/F authority boundaries.

### 5.4 Bundles → future role/team package pattern

Bundles are promising as a distribution idea for packaging multiple workflow pieces together, but they should remain a future pattern until local runtime experiments prove safety.

---

## 6. PATTERN_ONLY

These parts are useful design references but should not become baseline behavior yet.

### 6.1 Direct CLI installation

`specify-cli` is real and useful, but direct installation into the Method Wheel repo or Hermes profile should be treated as an experiment first.

Reason:

```text
The current active Hermes profile is cangwei under AppData/Local/hermes/profiles/cangwei.
Spec Kit's generic Hermes integration may target ~/.hermes/skills.
That can create cross-profile or rollback ambiguity.
```

### 6.2 Hermes integration code path

Spec Kit includes a Hermes integration, but use it as a pattern until proven under an isolated `HERMES_HOME` / sandbox.

### 6.3 Catalog architecture

Spec Kit's registry/catalog approach is useful for future skill ecosystem design, but it should not force immediate restructuring of the current skill system.

### 6.4 Bundle distribution model

Use as inspiration for future packaging of port identities, skills, templates, and verification checklists.

---

## 7. WATCH

These parts are promising but need more live evidence before baseline promotion.

```text
- converge as a formal E→D repair loop
- taskstoissues as default GitHub issue generation
- workflow resume/status as local Method Wheel run-state mechanism
- direct Spec Kit commands as installed Hermes skills
- spec-as-source for nonprofessional Owner operations
```

Watch criteria:

```text
1. Run in an isolated test repo.
2. Capture generated files and rollback path.
3. Verify active Hermes profile behavior.
4. Compare with existing A/B/C/D/E/F artifacts.
5. Promote only through reviewable docs/scripts diffs.
```

---

## 8. REJECT AS BASELINE

Reject these as default Method Wheel behavior:

```text
raw owner idea → /speckit.implement
```

Reason:

```text
That reintroduces the exact prompt-to-code failure Spec Kit is designed to prevent.
```

Also reject:

```text
- replacing A/B/C/D/E/F with a linear Spec Kit workflow
- treating tasks.md as broad permission to change the repo
- installing global Hermes skills without profile check and rollback
- treating community extensions as trusted by default
- using spec-as-source as the default for the current nonprofessional Owner workflow
- letting D-port makers amend constitution or baseline rules without F approval
```

---

## 9. Updated Method Wheel insertion points

Spec Kit affects the workflow in these exact places:

```text
A-port:
- use specify/clarify/checklist patterns for demand control
- preserve route, authority, non-goals, acceptance criteria, and stop condition

B-port:
- gather repo/source evidence before method updates
- feed mature projects into B2 instead of jumping to C

B2:
- absorb finished projects across theory/code/scaffold/artifacts/ecosystem/risks
- produce normalized packs before decisions

C-port:
- synthesize bridge/method updates only after B2 and A decision
- use plan/research/contracts/quickstart semantics

D-port:
- implement bounded tasks only
- avoid broad install/runtime changes unless approved

E-port:
- run read-only analyze-style consistency checks
- verify B2 coverage and anti-over-absorption

F-port:
- approve constitution, baseline workflow, risky scope, installs, and governance changes
```

---

## 10. Owner approval boundaries

F/Owner approval is required for:

```text
- changing the Method Wheel baseline
- adding B2 as a permanent required phase for mature repos
- installing Spec Kit globally or into the active Hermes profile
- enabling external/community extensions
- changing constitution/governance rules
- adopting spec-as-source as a default mode
- allowing automated issue/PR generation from tasks.md without review
```

Owner approval is not required for:

```text
- writing Source Packs
- creating B2 absorption documents
- proposing bridge docs
- running read-only validation
- isolated sandbox experiments with explicit rollback
```

---

## 11. Runtime integration boundary

Before running `specify init --integration hermes` or installing `speckit-*` skills, require:

```text
1. clean git state or isolated test repo
2. temporary HERMES_HOME / profile sandbox
3. dry-run or file preview where possible
4. list of generated/modified files
5. rollback command or deletion plan
6. E verification after install
7. F approval before baseline promotion
```

The current decision is:

```text
Do not install Spec Kit globally as baseline yet.
Use direct integration as a guarded runtime experiment only.
```

---

## 12. Final decision

Final classification:

```text
PARTIAL_ACCEPT_EXPAND
```

Final routing:

```text
Spec Kit becomes:
1. the Method Wheel's reference Spec Spine,
2. the first concrete B2 Finished Project Absorption example,
3. a pattern source for skill/template layering and workflow gates,
4. a guarded runtime-integration candidate, not an automatic install.
```

This decision closes the B2 Spec Kit absorption pack and gives future mature GitHub projects a repeatable standard.
