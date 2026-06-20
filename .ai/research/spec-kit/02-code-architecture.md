# Spec Kit Code Architecture

## 1. Package identity

Spec Kit's CLI package is `specify-cli`.

Key file:

```text
pyproject.toml
```

Important properties:

```text
Python >= 3.11
CLI entrypoint: specify = specify_cli:main
main library style: Typer + Rich + PyYAML + packaging + platformdirs
```

Bundled assets include templates, command templates, scripts, extensions, workflows, and presets.

---

## 2. CLI root

Main file:

```text
src/specify_cli/__init__.py
```

It defines the Typer app and registers command groups:

```text
specify init
specify check
specify version
specify self check/upgrade
specify integration ...
specify extension ...
specify preset ...
specify bundle ...
specify workflow ...
```

---

## 3. Init flow

Main implementation:

```text
src/specify_cli/commands/init.py
```

`specify init` performs:

```text
select integration
select script type sh/ps
validate target directory
install integration commands
copy shared infra into .specify/
initialize .specify/memory/constitution.md
install built-in speckit workflow
install agent-context extension
write .specify/init-options.json
write .specify/integration.json
write integration manifests
optionally install preset
```

This is the core scaffold engine.

---

## 4. Integration system

Main files:

```text
src/specify_cli/integrations/__init__.py
src/specify_cli/integrations/base.py
src/specify_cli/integrations/manifest.py
src/specify_cli/integration_state.py
src/specify_cli/integration_runtime.py
src/specify_cli/agents.py
```

The central registry is `INTEGRATION_REGISTRY`. Built-in integrations include Claude, Codex, Copilot, Cursor Agent, Gemini, Hermes, OpenCode, Qwen, Zed and many others.

Integration base classes:

```text
MarkdownIntegration
TomlIntegration
YamlIntegration
SkillsIntegration
```

They convert the same `templates/commands/*.md` source commands into each agent's native command format.

---

## 5. State and manifest model

Spec Kit writes project-local state:

```text
.specify/init-options.json
.specify/integration.json
.specify/integrations/<key>.manifest.json
.specify/extensions/.registry
.specify/presets/.registry
.specify/workflows/runs/<run_id>/state.json
```

Integration manifests record files and hashes. Uninstall/upgrade can preserve user-modified files instead of blindly deleting them.

---

## 6. Extension implementation

Main file:

```text
src/specify_cli/extensions.py
```

Extensions provide commands, hooks, scripts, and configuration. They install under `.specify/extensions/<extension-id>/` and register hooks through `.specify/extensions.yml`.

---

## 7. Preset implementation

Main files:

```text
src/specify_cli/presets/__init__.py
src/specify_cli/presets/_commands.py
```

Presets can override or compose templates, commands, and scripts using `replace`, `prepend`, `append`, and `wrap` strategies.

---

## 8. Workflow engine

Main files:

```text
src/specify_cli/workflows/engine.py
src/specify_cli/workflows/steps/*
```

Workflow definitions are YAML and support command, prompt, shell, init, gate, if, switch, while, do-while, fan-out, and fan-in steps.

Run state is persisted under:

```text
.specify/workflows/runs/<run_id>/
```

---

## 9. Bundle system

Main files:

```text
src/specify_cli/commands/bundle/__init__.py
src/specify_cli/bundler/*
```

Bundles aggregate extensions, presets, workflow steps, and workflows. This can inspire future Method Wheel distribution, but should remain `PATTERN_ONLY` for now.

---

## 10. Code-level implication for integration

Do not think of Spec Kit as only a prompt set. Its code implements:

```text
asset packaging
project initialization
agent command rendering
state/manifest tracking
plugin installation
workflow execution
catalog resolution
upgrade/uninstall safety
```

AI Method Wheel should absorb these as architecture patterns before attempting direct installation.
