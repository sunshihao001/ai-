# Spec Kit Project Structure and Scaffold

## 1. Source repo structure

Important top-level areas:

```text
README.md
spec-driven.md
docs/
templates/
scripts/
src/specify_cli/
integrations/
extensions/
presets/
workflows/
tests/
```

Each has a different role:

```text
spec-driven.md      → core theory
README/docs         → user workflow and reference
src/specify_cli     → CLI implementation
templates           → artifact templates and AI command templates
scripts             → feature/project helper scripts
integrations        → agent catalog/docs
extensions          → plugin system examples and docs
presets             → template/command override system
workflows           → YAML orchestration system
```

---

## 2. Generated target-project structure

After `specify init`, a target project is expected to contain:

```text
.specify/
├── init-options.json
├── integration.json
├── integrations/<integration>.manifest.json
├── scripts/{bash,powershell}/
├── templates/{spec,plan,tasks,checklist,constitution}-template.md
├── memory/constitution.md
├── workflows/speckit/workflow.yml
├── extensions/agent-context/
└── extensions.yml

specs/<feature-number>-<feature-name>/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
├── tasks.md
└── checklists/
```

Agent-specific command directories are also created depending on integration.

---

## 3. Command template scaffold

Source command templates:

```text
templates/commands/specify.md
templates/commands/clarify.md
templates/commands/checklist.md
templates/commands/plan.md
templates/commands/tasks.md
templates/commands/analyze.md
templates/commands/implement.md
templates/commands/converge.md
templates/commands/constitution.md
templates/commands/taskstoissues.md
```

These are transformed into agent-specific slash commands, skills, recipes, or prompt files.

Examples:

```text
Claude/Codex/Hermes skills: speckit-plan/SKILL.md
Gemini TOML command: speckit.plan.toml
Goose YAML recipe: speckit.plan.yaml
Markdown command: speckit.plan.md
```

---

## 4. Artifact templates

Core generated artifacts come from:

```text
templates/spec-template.md
templates/plan-template.md
templates/tasks-template.md
templates/checklist-template.md
templates/constitution-template.md
```

These templates are not cosmetic. They constrain LLM output shape and project governance.

---

## 5. Scripts

Scripts exist in Bash and PowerShell:

```text
create-new-feature
setup-plan
setup-tasks
check-prerequisites
common
```

They handle feature directory creation, template copying, prerequisite checks, path discovery, and JSON output for agent commands.

This is a practical pattern: AI commands should rely on deterministic scripts for file/path setup instead of letting the model guess.

---

## 6. Extensions / Presets / Workflows scaffold

```text
extensions → .specify/extensions/<id>/ + hooks/config/commands
presets    → .specify/presets/<id>/ + priority strategy
workflows  → .specify/workflows/<id>/workflow.yml + run state
```

The main scaffold lesson is:

```text
A mature AI workflow needs more than prompts.
It needs templates, scripts, manifests, state files, hooks, command registration, workflow run records, and rollback rules.
```
