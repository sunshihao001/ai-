# Spec Kit Bridge Layer for AI Method Wheel

> Status: v0.1  
> Purpose: absorb GitHub Spec Kit as a spec-driven artifact spine and bridge layer inside the AI Method Wheel without replacing A/B/C/D/E/F control.

---

## 1. Core judgment

Spec Kit is not just another code repo. It is GitHub's concrete answer to a common AI-programming failure:

```text
natural-language idea
→ agent freely interprets it
→ implementation drifts
→ verification becomes vague
```

Spec Kit's fix is:

```text
intent
→ constitution
→ specification
→ clarification
→ plan
→ tasks
→ implementation
```

The AI Method Wheel should adopt this as a **Spec Spine**, while keeping the Method Wheel as the higher-level control plane.

```text
Spec Kit = spec-driven artifact spine
AI Method Wheel = A/B/C/D/E/F control plane
```

---

## 2. Why this matters for AI coding

Before Spec Kit-style structure, the workflow is:

```text
"Build a task app"
→ hope the agent understands the intent
→ hope it stays on track
→ hope the output is testable
```

After Spec Kit-style structure, the workflow becomes:

```text
rules / constitution
→ what to build
→ unresolved questions
→ how to build
→ dependency-ordered tasks
→ bounded implementation
→ read-only consistency checks
```

The important shift is:

```text
prompt-to-code
→ intent-to-spec-to-code
```

For this user's AI workflow, this directly strengthens A-port demand control and E-port verification.

---

## 3. Six-command bridge

### `/speckit.constitution` → Governance baseline

Spec Kit role:

```text
project rules: quality, testing, architecture, governance, amendment policy
```

AI Method Wheel mapping:

```text
F/A boundary: owner-approved governance and project principles
E boundary: constitution violations are critical
D boundary: makers cannot dilute the constitution
```

Use when:

```text
project baseline, quality rules, testing discipline, architecture principles, or governance changes are being defined or amended
```

Do not use when:

```text
the owner is only exploring a vague idea and no project baseline should change yet
```

---

### `/speckit.specify` → WHAT before HOW

Spec Kit role:

```text
turn natural-language feature description into spec.md
focus on what to build, not technology stack
```

AI Method Wheel mapping:

```text
A-port: Raw intent → professional problem statement → spec candidate
```

Absorb into A-port:

```text
user stories
acceptance scenarios
functional requirements
measurable success criteria
assumptions
[NEEDS CLARIFICATION] markers
```

Guardrail:

```text
A-port still owns route, boundary, non-goals, authority, verification plan, and stop condition.
```

---

### `/speckit.clarify` → Targeted ambiguity removal

Spec Kit role:

```text
ask targeted questions before planning; write answers back into spec
```

AI Method Wheel mapping:

```text
A-port deep-path questioning
```

Important absorption:

```text
ask only high-impact questions
prefer <= 5 targeted questions
do not expose the full future question queue
write accepted clarification back into durable artifact
```

Guardrail:

```text
Do not turn A-port into endless interrogation. Clarify only questions that materially affect scope, architecture, data, tests, UX, operations, compliance, or safety.
```

---

### `/speckit.plan` → HOW after WHAT is stable

Spec Kit role:

```text
choose technical approach, resolve research unknowns, produce implementation plan and design artifacts
```

AI Method Wheel mapping:

```text
C-port: theory / architecture / implementation package
```

Artifacts:

```text
plan.md
research.md
data-model.md
contracts/
quickstart.md
```

Guardrail:

```text
Do not enter C-port plan mode until A has a stable enough spec candidate and B has supplied evidence if external knowledge is needed.
```

---

### `/speckit.tasks` → Dependency-ordered maker queue

Spec Kit role:

```text
turn spec + plan + design artifacts into dependency-ordered tasks.md
```

AI Method Wheel mapping:

```text
D-port preparation: bounded maker queue / GitHub issue candidates / Codex slices
```

Absorb:

```text
T001 task IDs
[P] parallel markers
user-story phases
independent test criteria
MVP-first sequencing
file paths per task
```

Guardrail:

```text
Tasks are not permission to execute broad repo changes. D-port still needs bounded scope, branch/worktree policy, and E verification.
```

---

### `/speckit.implement` → Agent builds from tasks

Spec Kit role:

```text
execute tasks.md phase by phase
```

AI Method Wheel mapping:

```text
D-port maker execution only
```

Use only when:

```text
A route is stable
B evidence gaps are resolved or explicitly accepted
C plan is ready
D task queue is bounded
E pre-implementation analysis is acceptable
F/owner has approved risky scope if needed
```

Reject as baseline:

```text
natural-language idea → direct implement
```

This is the exact anti-pattern Spec Kit exists to prevent.

---

## 4. Missing command in the user's six-command summary: `/speckit.analyze`

The user's summary lists six commands, but the inspected Spec Kit source also makes `/speckit.analyze` central.

Spec Kit role:

```text
read-only cross-artifact consistency and quality analysis
```

AI Method Wheel mapping:

```text
E-port verification / checker
```

It checks:

```text
spec.md ↔ plan.md ↔ tasks.md ↔ constitution
requirements coverage
duplications
ambiguity
underspecification
unmapped tasks
constitution conflicts
```

AI Method Wheel rule:

```text
No D-port implementation should be considered ready until an E-style read-only analyze pass has either passed or produced accepted caveats.
```

---

## 5. Artifact mapping

```text
.specify/memory/constitution.md     → F/A governance baseline
specs/<feature>/spec.md             → A-port accepted WHAT
specs/<feature>/checklists/*.md     → A/E quality checklist
specs/<feature>/plan.md             → C-port HOW package
specs/<feature>/research.md         → B/C evidence and technical decisions
specs/<feature>/data-model.md       → C-port domain/data model
specs/<feature>/contracts/          → C-port interface contract
specs/<feature>/quickstart.md       → E-port validation scenario
specs/<feature>/tasks.md            → D-port bounded maker queue
analyze report                      → E-port read-only consistency report
```

---

## 6. Spec persistence rule for this user

Default recommendation:

```text
spec-anchored + controlled flow-back
```

Use when normal implementation discoveries should update spec/plan/tasks after review.

For method-wheel or baseline-changing work:

```text
spec-anchored + flow-forward
```

Use when auditability matters and a new method update should preserve prior history.

Avoid as default:

```text
spec-as-source
```

Reason:

```text
The user's current role is nonprofessional Owner/operator. Treating spec.md as the sole editable source and regenerating everything requires a mature engineering team and strict E/F gates.
```

---

## 7. Presets and extensions as skill-governance pattern

Spec Kit presets map well to internal skill/template layering:

```text
project override
→ high-priority preset
→ extension template
→ core template
```

AI Method Wheel mapping:

```text
internal skill layers
bridge rules
merge strategy
priority / conflict handling
```

Spec Kit extensions map to external GitHub skill governance:

```text
ADOPT / BRIDGE / MERGE / PATTERN_ONLY / REJECT / WATCH
```

Rule:

```text
No community extension, preset, or external skill is installed merely because it exists. It first needs Source Pack, A absorption decision, and E/F gates if it changes baseline behavior.
```

---

## 8. Hermes integration caution

Spec Kit source includes a Hermes integration:

```bash
specify init --integration hermes
```

It installs `speckit-*` command templates as Hermes skills under generic:

```text
~/.hermes/skills/speckit-<command>/SKILL.md
```

Caution for this environment:

```text
Current active Hermes profile is cangwei under AppData/Local/hermes/profiles/cangwei.
Do not assume Spec Kit's generic ~/.hermes/skills path matches the active profile.
```

Before running installation:

```text
1. use an isolated test repo
2. check clean git state
3. check active Hermes profile skill path
4. preview files created
5. define rollback / uninstall path
6. do not run --force in the method-wheel repo without owner approval
```

---

## 9. A/B/C/D/E/F operating rule

Use Spec Kit like this:

```text
A: convert raw intent into spec candidate and clarification questions
B: supply evidence/source packs when knowledge is missing
C: synthesize plan/research/contracts/quickstart
D: execute bounded tasks only
E: run read-only analyze and verification
F: approve governance, risky scope, and baseline changes
```

Do not use it like this:

```text
Owner idea → /speckit.implement → broad agent build
```

That collapses the control plane and reintroduces the original problem.

---

## 10. Adoption decision

Classification:

```text
PARTIAL_ACCEPT_EXPAND
```

Meaning:

```text
Adopt Spec Kit's artifact spine.
Bridge its commands into A/B/C/D/E/F.
Merge preset/extension/workflow ideas into skill governance.
Keep implementation and global installation guarded.
```

One-line rule:

```text
Spec Kit tells the AI exactly what to build, in what order, and why; the AI Method Wheel decides when that spine is mature enough to execute, who verifies it, and who may approve baseline changes.
```
