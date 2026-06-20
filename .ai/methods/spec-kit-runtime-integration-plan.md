# Spec Kit Runtime Integration Plan

> Status: v0.1 C-port plan  
> Scope: design a safe runtime path for testing Spec Kit with Hermes, without installing into the active Method Wheel repo or active Hermes profile yet.  
> Related: `.ai/research/spec-kit/`, `.ai/methods/spec-kit-bridge-layer.md`, `.ai/methods/hermes-codex-role-split.md`

---

## 1. Stage goal

The current Method Wheel status is:

```text
B2 Spec Kit finished-project absorption: complete enough for runtime planning
C bridge/method synthesis: complete enough for a runtime integration plan
Runtime integration: not started
```

This plan defines the next safe stage:

```text
Spec Kit sandbox runtime experiment
```

The goal is **not** to install Spec Kit into the real AI Method Wheel repo. The goal is to verify, in isolation:

```text
1. How `specify-cli` installs and runs on this Windows/Hermes environment.
2. What `specify init --integration hermes` generates.
3. Where Hermes integration writes `speckit-*` skills or command files.
4. Whether it respects the active Hermes profile or writes to generic `~/.hermes/skills`.
5. Whether generated artifacts can be mapped safely to A/B/C/D/E/F.
6. What rollback/uninstall procedure is required before any real adoption.
```

---

## 2. Non-goals and forbidden actions

Do **not** do these in this stage:

```text
- Do not run `specify init --here --force` in the AI Method Wheel repo.
- Do not install global `speckit-*` Hermes skills into the active cangwei profile.
- Do not treat generated Spec Kit commands as baseline skills.
- Do not run `/speckit.implement` or any broad implementation command from owner chat.
- Do not let Codex run without a bounded handoff.
- Do not mutate `~/.hermes` or another Hermes profile without explicit F/owner confirmation.
```

Allowed in this stage:

```text
- Create an isolated sandbox directory outside the Method Wheel repo.
- Initialize a git repo inside the sandbox.
- Use a temporary `HERMES_HOME` if needed to protect the active cangwei profile.
- Install or run `specify-cli` only in a way that is reversible and logged.
- Record generated files, diffs, and path writes.
```

---

## 3. Hermes / Codex split for this stage

Hermes owns this plan and the experiment control.

```text
Hermes = control plane, experiment designer, runner, checker, report writer
Codex  = optional bounded worker only if scripts/prototype automation are needed
```

For now, **do not invoke Codex**. The first experiment can be run by Hermes with deterministic shell commands because the task is environment inspection and sandbox setup, not open-ended coding.

Codex may be used later only if Hermes creates a handoff like:

```text
Create a sandbox setup script under <path>.
Allowed paths: <sandbox only>.
Forbidden: active Hermes profile, Method Wheel repo except report output.
Verify by: command output + generated tree + git diff.
```

---

## 4. Proposed sandbox layout

Use a sandbox root outside the Method Wheel repo:

```text
C:/Users/Administrator/AppData/Local/Temp/spec-kit-hermes-runtime-sandbox/
```

Suggested layout:

```text
spec-kit-hermes-runtime-sandbox/
├── project/                 # target repo for `specify init`
├── hermes-home/             # optional temporary HERMES_HOME
├── logs/
│   ├── environment.txt
│   ├── specify-version.txt
│   ├── before-tree.txt
│   ├── after-tree.txt
│   ├── hermes-home-before.txt
│   ├── hermes-home-after.txt
│   └── command-output.txt
└── report.md                # experiment result
```

If testing `HERMES_HOME`, set it only for the command invocation:

```bash
HERMES_HOME="<sandbox>/hermes-home" specify init --here --integration hermes
```

Do not export it into the long-lived Hermes session environment unless needed.

---

## 5. Preflight checks

Before any runtime experiment, record:

```bash
pwd
python --version
uv --version
pip --version
which specify || true
which hermes || true
hermes profile show cangwei || true
hermes config path || true
git status --short --branch
```

Also record known sensitive paths to protect:

```text
C:/Users/Administrator/AppData/Local/hermes/profiles/cangwei
C:/Users/Administrator/.hermes
C:/Users/Administrator/ai-skill-install-work/ai-
```

If a command would write to these paths unexpectedly, stop.

---

## 6. Experiment sequence

### Step 1 — create sandbox

```bash
SANDBOX="/c/Users/Administrator/AppData/Local/Temp/spec-kit-hermes-runtime-sandbox"
rm -rf "$SANDBOX"
mkdir -p "$SANDBOX/project" "$SANDBOX/hermes-home" "$SANDBOX/logs"
cd "$SANDBOX/project"
git init
```

Use a temp directory only. Never run in the Method Wheel repo.

### Step 2 — locate or install Spec Kit CLI

Preferred order:

```text
1. Use local cloned source if available.
2. Use uvx / uv tool in an isolated way if needed.
3. Do not permanently install global tools unless owner approves.
```

Possible safe source-based command from cloned repo:

```bash
python -m specify_cli --version
```

If source invocation needs `PYTHONPATH`, use:

```bash
PYTHONPATH="C:/Users/Administrator/spec-kit-source/src" python -m specify_cli --version
```

If this fails, record the failure and stop before trying global installation.

### Step 3 — dry inspect Hermes integration target behavior if possible

Before running init, inspect source code or run a non-mutating command to determine:

```text
- integration key: hermes
- target command directory
- whether it uses `~/.hermes/skills` or `HERMES_HOME/skills`
- generated skill names
- manifest files
```

Expected source file:

```text
C:/Users/Administrator/spec-kit-source/src/specify_cli/integrations/hermes/__init__.py
```

### Step 4 — run isolated init only with temporary HERMES_HOME

If preflight is clean:

```bash
cd "$SANDBOX/project"
HERMES_HOME="$SANDBOX/hermes-home" \
PYTHONPATH="C:/Users/Administrator/spec-kit-source/src" \
python -m specify_cli init --here --integration hermes --ignore-agent-tools --force
```

If `python -m specify_cli` is not supported, use the equivalent safe CLI invocation and record it.

### Step 5 — collect generated files

Record:

```bash
find "$SANDBOX" -maxdepth 5 -type f | sort
find "$SANDBOX/project" -maxdepth 5 -type f | sort
find "$SANDBOX/hermes-home" -maxdepth 5 -type f | sort
```

Expected categories to check:

```text
.specify/templates/
.specify/scripts/
.specify/memory/constitution.md
.specify/integration.json
.specify/init-options.json
.specify/integrations/*.manifest.json
speckit-* SKILL.md or Hermes command files under temporary hermes-home
```

### Step 6 — classify generated artifacts into Method Wheel roles

Map generated files to:

```text
A: specify/clarify/checklist skills or commands
C: plan/research/contracts commands
D: tasks/implement commands
E: analyze/converge commands
F: constitution/governance commands
Harness: workflow run/resume, manifests, integration state
```

### Step 7 — cleanup / rollback check

Because this stage must be reversible:

```bash
rm -rf "$SANDBOX"
```

Only do cleanup after logs/report are copied into the Method Wheel repo if the experiment succeeded or failed with useful data.

---

## 7. E-port verification criteria

The runtime experiment passes only if all are true:

```text
1. All writes stayed inside the sandbox or explicitly recorded expected temp dirs.
2. Active cangwei profile was not modified.
3. Method Wheel repo was not modified except the final report commit.
4. Generated Spec Kit files were captured in a file tree/log.
5. Hermes integration target path was identified.
6. Rollback path is clear and tested or sandbox deletion is sufficient.
7. The result report says whether direct Hermes integration is safe, unsafe, or needs source patching/adapter.
```

Fail conditions:

```text
- Any unexpected write to active Hermes profile.
- Any unexpected write to the Method Wheel repo.
- CLI requires global installation before path behavior is understood.
- Generated skills cannot be distinguished from existing active skills.
- No rollback path.
```

---

## 8. F-port confirmation points

Before moving from sandbox to real adoption, owner must approve:

```text
1. Whether to install `specify-cli` globally or keep it source/uvx-based.
2. Whether to allow Spec Kit to write Hermes skills into the active cangwei profile.
3. Whether to keep generated `speckit-*` skills as-is, wrap them, or translate them into Method Wheel-native skills.
4. Whether `/speckit.implement` is disabled, hidden, or guarded by Method Wheel rules.
5. Whether Spec Kit becomes optional sandbox tool, default project scaffold, or only pattern reference.
```

Recommended default:

```text
Do not install into cangwei yet.
Use sandbox result to build a wrapper/bridge plan first.
```

---

## 9. Expected outcome of the next stage

The next stage should produce:

```text
.ai/research/spec-kit-runtime/experiment-YYYY-MM-DD.md
```

It should include:

```text
commands run
stdout/stderr excerpts
file tree before/after
Hermes profile write behavior
Spec Kit generated command/skill names
risk assessment
recommendation: SAFE / NEEDS WRAPPER / UNSAFE
```

---

## 10. Current stage completion definition

This plan is complete when:

```text
- The plan is written and committed.
- README and validation script reference it.
- `python scripts/validate-ai-method-wheel.py` passes.
- No runtime experiment has been run yet.
```

After that, the next phase is:

```text
D/E sandbox runtime experiment
```

with Hermes as runner/checker and Codex only optional for bounded automation.
