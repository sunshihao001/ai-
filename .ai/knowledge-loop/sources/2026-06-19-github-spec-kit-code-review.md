# Source Pack: GitHub Spec Kit code-level review

- Date: 2026-06-19
- Source repo: https://github.com/github/spec-kit
- Local source path inspected: `C:/Users/Administrator/spec-kit-source`
- Upstream commit inspected: `487af97864901462874f18f1c7f8d8adec0b7ddd`
- Source quality: S1 — official source code, docs, templates, and CLI implementation
- A-port decision status: candidate for expanded `PARTIAL_ACCEPT`, not baseline replacement

---

## 1. What Spec Kit is

Spec Kit is a toolkit and CLI for Spec-Driven Development (SDD). Its core claim is that specifications should become durable, executable assets rather than disposable notes.

Core philosophy from `docs/concepts/sdd.md`:

```text
intent-driven development: define what before how
rich specification creation using guardrails and organizational principles
multi-step refinement instead of one-shot code generation
AI model interprets and operationalizes specs
```

Development phases:

```text
0-to-1 / greenfield: high-level requirements → spec → plan → production-ready build
creative exploration: parallel implementations and diverse tech stacks
brownfield enhancement: iterative feature addition and modernization
```

---

## 2. What the code actually provides

### CLI package

`pyproject.toml` defines the `specify` CLI:

```text
project: specify-cli
python: >=3.11
entrypoint: specify = specify_cli:main
primary stack: Typer, Rich, PyYAML, platformdirs, json5
```

The CLI bootstraps and manages SDD project infrastructure:

```text
specify init
specify integration ...
specify extension ...
specify preset ...
specify workflow ...
specify self check/upgrade
```

### Core assets bundled into the package

`pyproject.toml` force-includes:

```text
templates/spec-template.md
templates/plan-template.md
templates/tasks-template.md
templates/checklist-template.md
templates/constitution-template.md
templates/commands/*
scripts/bash/*
scripts/powershell/*
extensions/*
workflows/speckit
presets/lean
```

So Spec Kit is not only a README methodology. It is a CLI that installs command templates, scripts, integration files, extensions, workflows, and presets.

---

## 3. The core command spine

The important command templates are:

```text
speckit.specify  → create/update feature spec from natural language
speckit.clarify  → clarify unresolved requirements
speckit.plan     → generate implementation plan and design artifacts
speckit.tasks    → generate dependency-ordered tasks.md
speckit.analyze  → read-only consistency and quality analysis
speckit.implement → execute tasks.md phase-by-phase
```

### `specify`

Creates feature directory and `spec.md`; uses a spec quality checklist; limits `[NEEDS CLARIFICATION]` markers to the highest-impact unknowns; requires user scenarios, functional requirements, success criteria, assumptions, and measurable outcomes.

Important fit for A-port:

```text
natural language → structured spec
what before how
max 3 critical clarifications
requirements must be testable
success criteria technology-agnostic
```

### `plan`

Loads spec and constitution, produces implementation plan, research.md, data-model.md, contracts, quickstart, and agent context updates.

Important fit for C-port:

```text
spec + governance → technical plan + design artifacts
unknowns become research tasks
constitution gates can block bad plans
```

### `tasks`

Loads plan/spec/design artifacts and creates dependency-ordered `tasks.md` organized by independently testable user stories.

Important fit for D-port handoff:

```text
user-story phases
task IDs
[P] parallel markers
file paths
MVP-first implementation strategy
```

### `analyze`

Read-only cross-artifact checker. It loads only needed parts of spec/plan/tasks/constitution and reports duplication, ambiguity, underspecification, constitution conflicts, coverage gaps, and inconsistencies.

Important fit for E-port:

```text
read-only checker
no file modification
severity classification
coverage mapping between requirements and tasks
constitution conflicts are critical
```

### `implement`

Executes tasks.md with checklist gates, loads plan/spec/design context, verifies project setup, follows phase order and TDD if tests exist, marks completed tasks, and validates completion.

Important caution:

```text
This maps to D-port maker execution only.
It must not bypass A/E/F gates in the AI Method Wheel.
```

---

## 4. Template structure

`templates/spec-template.md` enforces:

```text
prioritized independently testable user stories
acceptance scenarios
edge cases
functional requirements with FR IDs
key entities when data exists
measurable success criteria with SC IDs
assumptions
```

This is directly useful for turning vague Owner intent into a professional agent-usable problem statement.

---

## 5. Persistence and evolution model

Spec Kit explicitly names persistence models in `docs/concepts/spec-persistence.md`:

```text
spec-first      write spec before coding, may discard later
spec-anchored   keep spec after implementation for future changes
spec-as-source  spec is the human-edited source, implementation derived/regenerated
```

It also names artifact mutation strategies:

```text
flow-back    spec/plan/tasks/code can inform each other, then reconcile
flow-forward completed feature dirs remain history; new changes create new dirs
living spec  spec.md is contract; plan/tasks derived from it
```

Existing project guide `docs/guides/evolving-specs.md` says brownfield projects need separate loops:

```text
Spec Kit project-file updates
Feature artifact evolution
```

This maps strongly to the user's current need: workflow should continuously evolve, but baseline changes need evidence and gates.

---

## 6. Integrations, including Hermes

Source has built-in integrations for many agents. Inspected integration list includes:

```text
claude, codex, copilot, cursor_agent, devin, gemini, hermes, opencode, qwen, zed, ...
```

`src/specify_cli/integrations/hermes/__init__.py` shows an explicit Hermes Agent integration.

Important behavior:

```text
specify init --integration hermes
```

Installs Spec Kit commands as global Hermes skills under:

```text
~/.hermes/skills/speckit-<command>/SKILL.md
```

and creates a project-local marker:

```text
.hermes/skills/
```

Caution for this user's environment:

```text
Hermes profile path may differ from generic ~/.hermes/skills.
Current active profile is cangwei under AppData/Local/hermes/profiles/cangwei.
Do not blindly run installation without checking profile behavior and cross-profile effects.
```

---

## 7. Workflows, extensions, and presets

### Workflows

`docs/reference/workflows.md` and `workflows/speckit/workflow.yml` show Spec Kit can run repeatable YAML workflows:

```text
specify workflow run speckit
specify workflow resume <run_id>
specify workflow status [run_id]
```

The built-in workflow:

```text
specify → review-spec gate → plan → review-plan gate → tasks → implement
```

This is useful as a pattern, but the AI Method Wheel should insert B/C/E/F gates more explicitly.

### Extensions

Extensions add domain-specific commands, quality gates, and integrations. They have install/update/enable/disable/priority/catalog mechanisms.

Important safety note from docs:

```text
Community extensions are not reviewed/audited/endorsed by Spec Kit maintainers. Review source before installing.
```

This matches the user's external skill governance requirement.

### Presets

Presets are stackable, priority-ordered template/command overrides. They resolve templates through:

```text
project overrides
→ installed presets by priority
→ extensions
→ core templates
```

This is highly relevant to the user's internal skill layering/update/bridge/merge/reject problem.

---

## 8. Fit to AI Method Wheel

Decision: `PARTIAL_ACCEPT_EXPAND`.

Spec Kit should improve the AI workflow in these areas:

```text
A-port: stronger intent-to-spec artifact creation
B-port: source/evidence packaging before spec updates
C-port: plan/research/data/contracts/quickstart synthesis
D-port: tasks.md as bounded maker queue
E-port: analyze command as read-only consistency gate
F-port: review-spec/review-plan/constitution changes as owner gates
Self-improvement: presets/extensions/workflows as controlled evolution mechanisms
```

But Spec Kit should not replace the AI Method Wheel because:

```text
Spec Kit is primarily an SDD toolkit and CLI.
AI Method Wheel is a broader control plane: A/B/C/D/E/F routing, maker/checker separation, owner authority, knowledge-loop absorption, repo placement, and workflow evolution governance.
```

---

## 9. Recommended adoption mode

Use these adoption categories:

```text
ADOPT:
- spec artifact spine
- spec/plan/tasks/checklist/analyze artifact semantics
- spec persistence model vocabulary
- read-only analyze gate concept

BRIDGE:
- specify/clarify into A-port Demand Grilling Brief
- plan into C-port theory/implementation package
- tasks into D-port bounded issue/Codex queue
- analyze into E-port verification/checker
- workflow gates into F/owner decision briefs

MERGE:
- presets/extensions concept with internal skill layering and external skill governance
- workflow resume/status concept with A-mode replay/evolution logs

PATTERN_ONLY:
- CLI integration registry and catalog architecture as inspiration for skill registry/governance
- Hermes integration approach, because local Hermes profile behavior must be checked before using directly

REJECT AS BASELINE:
- broad direct `speckit.implement` from vague owner intent
- spec-as-source as default for this user's current nonprofessional Owner workflow
- installing all Spec Kit skills globally without A/E/F review
```

---

## 10. Main gap in current AI Method Wheel

The existing AI Method Wheel already absorbed Spec Kit as a Spec Spine. The new code-level review suggests one expansion:

```text
Add a Spec Kit bridge layer that maps Spec Kit CLI artifacts and commands to A/B/C/D/E/F responsibilities, including Hermes integration cautions, presets/extensions governance, and workflow-run state as an optional pattern.
```

This should be a bridge, not a wholesale install.
