# Spec Kit Extension and Ecosystem Model

## 1. Ecosystem layers

Spec Kit is designed as an extensible SDD platform:

```text
core templates and commands
→ integrations
→ extensions
→ presets
→ workflows
→ workflow steps
→ bundles
→ catalogs
```

This matters because it shows how a finished AI workflow project avoids becoming a monolith.

---

## 2. Integrations

Integrations adapt Spec Kit commands to many AI agents. They define agent name, command folder, command format, argument placeholder, context file, CLI requirement, and invoke separator.

Formats include:

```text
Markdown commands
TOML commands
YAML recipes
SKILL.md directories
Copilot prompt/agent files
```

Hermes is included as a built-in integration, but direct installation must be guarded because this user's active Hermes profile is `cangwei`, not necessarily generic `~/.hermes/skills`.

---

## 3. Extensions

Extensions add capabilities: commands, hooks, scripts, quality gates, tool integrations, config.

They install under:

```text
.specify/extensions/<extension-id>/
```

Important built-ins:

```text
agent-context → keeps agent context files in sync
git           → branch/remote/commit/validation hooks
bug           → bug assess/fix/test workflow
```

Method Wheel lesson:

```text
External GitHub skills should be treated like extensions: source-reviewed, versioned, enabled/disabled, and gated.
```

---

## 4. Presets

Presets customize method behavior by overriding/composing templates, commands, and scripts.

Resolution stack:

```text
project overrides
→ installed presets by priority
→ extensions
→ core templates
```

Composition strategies:

```text
replace
prepend
append
wrap
```

Method Wheel lesson:

```text
Do not fork core workflow for every domain. Add priority-ordered presets or bridge layers.
```

---

## 5. Workflows and Bundles

Workflows are YAML pipelines with persistent run state, gates, conditions, loops, and fan-out/fan-in.

A Method Wheel workflow should eventually be stronger than the built-in linear workflow:

```text
A specify/clarify
→ B/B2 source or project absorption if needed
→ C plan
→ E analyze
→ F owner gate for risky changes
→ D bounded implement
→ E verify/converge
```

Bundles aggregate extensions, presets, workflow steps, and workflows. Keep bundle adoption as `PATTERN_ONLY` until distribution needs are real.

---

## 6. Catalogs and trust

Catalog discovery is not adoption.

```text
Discovery → Source Pack → B2 absorption → A decision → E/F gate → install or bridge.
```
