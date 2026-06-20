# Spec Kit Hermes Runtime Experiment — 2026-06-20

> Stage: D/E sandbox runtime experiment  
> Related plan: `.ai/methods/spec-kit-runtime-integration-plan.md`  
> Result: `NEEDS WRAPPER / UNSAFE FOR DIRECT ACTIVE-PROFILE INSTALL`

---

## 1. Purpose

Verify whether GitHub Spec Kit can be safely initialized with Hermes integration without touching the active Method Wheel repo or active Hermes profile.

Questions tested:

```text
1. Can `specify-cli` run from the cloned Spec Kit source?
2. Can `specify init --integration hermes` initialize a sandbox project?
3. Does temporary `HERMES_HOME` isolate generated Hermes skills?
4. What files are generated?
5. Is the active cangwei profile modified?
6. What rollback is required?
```

---

## 2. Sandbox

Sandbox root:

```text
C:/Users/Administrator/AppData/Local/Temp/spec-kit-hermes-runtime-sandbox/
```

Main subpaths:

```text
project/       # sandbox git repo for `specify init`
hermes-home/   # intended temporary HERMES_HOME
logs/          # captured command outputs and file trees
```

Active profile protected:

```text
C:/Users/Administrator/AppData/Local/hermes/profiles/cangwei
```

---

## 3. Commands and outcomes

### 3.1 Direct source invocation failed at first

Command shape:

```bash
PYTHONPATH='C:/Users/Administrator/spec-kit-source/src' python -m specify_cli --version
```

Outcome:

```text
ModuleNotFoundError: No module named 'typer'
```

Reason: system Python did not have Spec Kit CLI dependencies installed.

### 3.2 `uv run --project` succeeded

Command:

```bash
uv run --project 'C:/Users/Administrator/spec-kit-source' specify --version
```

Outcome:

```text
specify 0.11.4.dev0
```

Note: `uv` created a virtual environment under the Spec Kit source checkout:

```text
C:/Users/Administrator/spec-kit-source/.venv
```

This is not an active Hermes profile write, but it is a source-checkout cache side effect.

### 3.3 First `specify init` attempt timed out

Command shape omitted `--script`:

```bash
HERMES_HOME="$SANDBOX/hermes-home" \
uv run --project 'C:/Users/Administrator/spec-kit-source' \
specify init --here --integration hermes --ignore-agent-tools --force
```

Outcome:

```text
timeout after 300s
```

Likely cause: command still waited for interactive script selection. Residual process was killed.

### 3.4 Second `specify init` with `--script sh` succeeded

Command:

```bash
HERMES_HOME="$SANDBOX/hermes-home" \
uv run --project 'C:/Users/Administrator/spec-kit-source' \
specify init --here --integration hermes --script sh --ignore-agent-tools --force
```

Outcome:

```text
Selected coding agent integration: hermes
Selected script type: sh
Project ready.
EXIT_CODE=0
```

Generated next-step commands shown by Spec Kit:

```text
/speckit-constitution
/speckit-specify
/speckit-plan
/speckit-tasks
/speckit-implement
/speckit-converge
/speckit-clarify
/speckit-analyze
/speckit-checklist
```

---

## 4. Generated sandbox project files

Generated under sandbox `project/`:

```text
.specify/extensions.yml
.specify/extensions/.registry
.specify/extensions/agent-context/...
.specify/init-options.json
.specify/integration.json
.specify/integrations/hermes.manifest.json
.specify/integrations/speckit.manifest.json
.specify/memory/constitution.md
.specify/scripts/bash/check-prerequisites.sh
.specify/scripts/bash/common.sh
.specify/scripts/bash/create-new-feature.sh
.specify/scripts/bash/setup-plan.sh
.specify/scripts/bash/setup-tasks.sh
.specify/templates/checklist-template.md
.specify/templates/constitution-template.md
.specify/templates/plan-template.md
.specify/templates/spec-template.md
.specify/templates/tasks-template.md
.specify/workflows/speckit/workflow.yml
.specify/workflows/workflow-registry.json
AGENTS.md
.hermes/skills/   # empty marker directory
```

`AGENTS.md` contains managed Spec Kit context markers:

```text
<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
```

---

## 5. Critical finding: HERMES_HOME did not isolate global skill writes

The experiment intended to isolate Hermes writes via:

```bash
HERMES_HOME="$SANDBOX/hermes-home"
```

But source inspection shows `HermesIntegration` uses:

```python
Path.home() / ".hermes" / "skills"
```

not `HERMES_HOME` and not the active Hermes profile path.

Source file:

```text
C:/Users/Administrator/spec-kit-source/src/specify_cli/integrations/hermes/__init__.py
```

Relevant behavior:

```text
- writes each speckit command as ~/.hermes/skills/speckit-<name>/SKILL.md
- creates project-local .hermes/skills/ as an empty marker
- teardown removes all ~/.hermes/skills/speckit-* dirs
```

Therefore temporary `HERMES_HOME` is **not sufficient protection**.

---

## 6. Unexpected write and rollback

Unexpected generated dirs appeared under default Hermes home:

```text
C:/Users/Administrator/.hermes/skills/speckit-agent-context-update
C:/Users/Administrator/.hermes/skills/speckit-analyze
C:/Users/Administrator/.hermes/skills/speckit-checklist
C:/Users/Administrator/.hermes/skills/speckit-clarify
C:/Users/Administrator/.hermes/skills/speckit-constitution
C:/Users/Administrator/.hermes/skills/speckit-converge
C:/Users/Administrator/.hermes/skills/speckit-implement
C:/Users/Administrator/.hermes/skills/speckit-plan
C:/Users/Administrator/.hermes/skills/speckit-specify
C:/Users/Administrator/.hermes/skills/speckit-tasks
C:/Users/Administrator/.hermes/skills/speckit-taskstoissues
```

These were timestamped around:

```text
2026-06-20 00:37:09 -0700
```

Rollback performed:

```bash
rm -rf /c/Users/Administrator/.hermes/skills/speckit-*
```

Post-cleanup check:

```text
no /c/Users/Administrator/.hermes/skills/speckit-* dirs remained
```

Active cangwei profile check:

```text
C:/Users/Administrator/AppData/Local/hermes/profiles/cangwei/skills
```

Diff count before/after:

```text
0
```

So the active `cangwei` profile was not modified, but the default `~/.hermes` profile path was temporarily polluted and then cleaned.

---

## 7. Manifest findings

Sandbox project `.specify/integration.json`:

```json
{
  "integration": "hermes",
  "default_integration": "hermes",
  "integration_settings": {
    "hermes": {
      "script": "sh",
      "invoke_separator": "-"
    }
  }
}
```

Sandbox project `.specify/integrations/hermes.manifest.json`:

```json
{
  "integration": "hermes",
  "version": "0.11.4.dev0",
  "files": {}
}
```

Interpretation:

```text
The project-local Hermes manifest does not track the global speckit-* skills it created.
```

This increases uninstall/rollback risk for profile-managed Hermes setups.

---

## 8. Method Wheel mapping of generated commands

```text
/speckit-constitution → F/A governance baseline
/speckit-specify      → A WHAT/spec candidate
/speckit-clarify      → A targeted ambiguity removal
/speckit-checklist    → A/E English-unit-test gate for requirements
/speckit-plan         → C HOW package
/speckit-tasks        → D bounded maker queue
/speckit-analyze      → E read-only cross-artifact checker
/speckit-implement    → D maker execution only after gates
/speckit-converge     → E→D append-only repair loop
/speckit-taskstoissues → D/F GitHub issue handoff
```

---

## 9. E-port verdict

Verdict:

```text
NEEDS WRAPPER / UNSAFE FOR DIRECT ACTIVE-PROFILE INSTALL
```

Passes:

```text
- Spec Kit CLI can run from source via `uv run --project`.
- `specify init --integration hermes --script sh` succeeds in a sandbox.
- Sandbox project scaffold is generated correctly.
- Active cangwei profile was not modified.
- Unexpected default ~/.hermes writes were detected and removed.
```

Fails / blockers:

```text
- `HERMES_HOME` did not isolate Hermes integration skill writes.
- Hermes integration hardcodes `Path.home()/.hermes/skills`.
- Project-local `hermes.manifest.json` records no generated global skill files.
- Direct use could pollute the wrong Hermes profile.
- Direct use could expose `/speckit-implement` without Method Wheel gates.
```

---

## 10. Recommendation

Do **not** install Spec Kit Hermes integration into the active Method Wheel workflow yet.

Recommended next step:

```text
Create a wrapper/adapter plan before any real install.
```

The wrapper must provide at least one of:

```text
1. Patch/adapter so Spec Kit respects active Hermes profile or HERMES_HOME.
2. Project-local translation from generated speckit command templates into Method Wheel-native skills.
3. A guarded import process that copies only ADOPT/BRIDGE commands and disables or wraps `/speckit-implement`.
4. A cleanup verifier that detects and removes default ~/.hermes/skills/speckit-* pollution.
```

Recommended classification after runtime experiment:

```text
Spec Kit CLI scaffold: usable in sandbox
Spec Kit Hermes integration: pattern useful, direct install unsafe
Spec Kit commands: bridge manually or via wrapper
Spec Kit implement command: must be gated or excluded
```

---

## 11. Next phase

Next Method Wheel phase should be:

```text
C: Spec Kit Hermes wrapper/adapter design
```

not:

```text
D: install into active Hermes profile
```

Codex still not required unless we decide to implement a wrapper script or patch against Spec Kit integration behavior.
