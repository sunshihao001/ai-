# Spec Kit Hermes Wrapper / Adapter Design

> Status: v0.1 C-port design  
> Trigger: `.ai/research/spec-kit-runtime/experiment-2026-06-20.md` found that Spec Kit's Hermes integration writes to `Path.home() / ".hermes" / "skills"`, not `HERMES_HOME` or the active `cangwei` profile.  
> Goal: define a profile-safe way to use Spec Kit patterns and selected commands without direct unsafe installation.

---

## 1. Decision summary

Do **not** directly install Spec Kit's upstream Hermes integration into the active Method Wheel environment.

Use a wrapper/adapter approach instead:

```text
Spec Kit upstream templates / scaffold
→ Method Wheel adapter
→ selected, gated, profile-safe skills/templates
→ E verification
→ F owner approval before active use
```

Runtime experiment verdict:

```text
NEEDS WRAPPER / UNSAFE FOR DIRECT ACTIVE-PROFILE INSTALL
```

---

## 2. Why direct install is unsafe

The upstream Hermes integration says it installs skills globally:

```text
~/.hermes/skills/speckit-<name>/SKILL.md
```

The source implementation uses:

```python
Path.home() / ".hermes" / "skills"
```

This means:

```text
- temporary HERMES_HOME does not isolate writes
- active profile path is not respected
- cangwei profile is not targeted
- project manifest does not track generated global skills
- uninstall/rollback is not profile-aware
```

Experiment confirmed that `specify init --integration hermes` created:

```text
C:/Users/Administrator/.hermes/skills/speckit-*
```

These were removed, and active cangwei profile stayed unchanged.

---

## 3. Adapter goals

The adapter must provide:

```text
1. profile-safe target path
2. explicit command selection
3. Method Wheel gate wrapping
4. manifest/rollback tracking
5. E-port verification before enablement
6. F/owner confirmation before baseline install
```

It must prevent:

```text
raw owner intent → /speckit-implement
```

and must preserve:

```text
A/B/B2/C/D/E/F control plane
```

---

## 4. Recommended approach: Method Wheel-native skill translation

The safest path is not to run upstream Hermes integration in the active environment.

Instead:

```text
1. Read Spec Kit command templates from the cloned source repo.
2. Translate selected templates into Method Wheel-native skills or templates.
3. Write them under the active cangwei profile only through Hermes-approved skill tools or a reviewed adapter script.
4. Add wrapper frontmatter and guardrails.
5. Exclude or wrap high-risk commands.
6. Track every installed file in a Method Wheel manifest.
```

This treats upstream Spec Kit as source material, not as an installer.

---

## 5. Command import policy

### Import as enabled wrappers

These can become Method Wheel-native skills after wrapper review:

```text
speckit-specify      → A-port WHAT/spec candidate
speckit-clarify      → A-port targeted ambiguity removal
speckit-checklist    → A/E requirements quality checklist
speckit-plan         → C-port HOW package
speckit-tasks        → D-port task queue preparation only
speckit-analyze      → E-port read-only consistency checker
speckit-converge     → E→D repair task appender, guarded
```

### Import as gated / disabled by default

```text
speckit-constitution → F/A governance; owner approval required
speckit-taskstoissues → D/F GitHub side effect; only with repo/remote confirmation
```

### Do not enable as raw command

```text
speckit-implement
```

`implement` may exist only as a wrapper that checks:

```text
- A route is stable
- spec/plan/tasks exist
- E analyze pass is done or caveats accepted
- allowed paths are bounded
- branch/worktree policy is defined
- owner approved risky or broad scope
```

Default recommendation:

```text
Do not import `speckit-implement` as an active skill initially.
Represent it as a D-port handoff template instead.
```

---

## 6. Target path policy

Active profile path in this environment:

```text
C:/Users/Administrator/AppData/Local/hermes/profiles/cangwei/skills
```

The adapter must never infer this from `Path.home() / ".hermes"`.

Allowed write methods:

```text
- Hermes `skill_manage` for one-by-one reviewed skill creation
- reviewed adapter script that receives an explicit `--target-profile-skills-dir`
- repo-local generated templates under `.ai/generated/spec-kit-adapter/` before manual promotion
```

Forbidden write methods:

```text
- upstream `specify init --integration hermes` against active profile
- any command that writes `~/.hermes/skills/speckit-*` without profile awareness
- blind copy into another Hermes profile
```

---

## 7. Manifest and rollback design

If the adapter installs anything, it must create a manifest:

```text
.ai/manifests/spec-kit-hermes-adapter-manifest.json
```

Manifest fields:

```json
{
  "schema_version": 1,
  "source_repo": "github/spec-kit",
  "source_commit": "487af97864901462874f18f1c7f8d8adec0b7ddd or later verified commit",
  "target_profile": "cangwei",
  "target_skills_dir": "C:/Users/Administrator/AppData/Local/hermes/profiles/cangwei/skills",
  "installed_at": "ISO-8601",
  "commands": [
    {
      "name": "speckit-specify",
      "source_template": "templates/commands/specify.md",
      "target_path": ".../skills/.../SKILL.md",
      "status": "enabled|gated|disabled",
      "sha256": "..."
    }
  ]
}
```

Rollback must:

```text
1. read manifest
2. delete only paths listed in manifest
3. refuse to delete paths outside the target cangwei profile
4. report any missing or modified files
5. never wildcard-delete unrelated skills
```

---

## 8. Wrapper guardrail content

Each imported wrapper skill must add a Method Wheel header before the upstream command body:

```text
This skill is a Method Wheel wrapper around a GitHub Spec Kit command.
Do not execute it as a standalone linear workflow.
Respect A/B/C/D/E/F routing.
If prerequisites are missing, stop and produce a blocker brief.
```

Minimum per-command guardrails:

```text
specify: do not choose technology stack; produce WHAT/spec candidate only
clarify: ask only high-impact questions; write accepted answers to durable spec
checklist: test requirements quality, not implementation
plan: requires stable WHAT and evidence/caveat state
tasks: produces bounded maker queue; does not grant execution authority
analyze: read-only only
converge: append-only repair task generation
constitution: owner/F gate required
implement: disabled or D-port handoff only
```

---

## 9. Adapter implementation options

### Option A — Manual skill creation via Hermes tools

Use `skill_manage` to create selected wrapper skills one by one.

Pros:

```text
- safest
- profile-aware
- reviewed per skill
- no custom installer needed
```

Cons:

```text
- slower
- harder to update from upstream
```

Recommended for first adoption.

### Option B — Repo-local generator script

Create a script that reads upstream templates and writes generated wrapper files under:

```text
.ai/generated/spec-kit-hermes-adapter/
```

Then human/Hermes reviews generated files before promotion to active profile.

Pros:

```text
- repeatable
- does not touch Hermes profile during generation
- easy diff review
```

Cons:

```text
- still needs a promotion step
```

Recommended as the first automated prototype.

### Option C — Patch upstream Spec Kit integration

Patch `HermesIntegration._hermes_home_skills_dir()` to respect profile/HERMES_HOME or an explicit env var.

Possible env var:

```text
SPECKIT_HERMES_SKILLS_DIR
```

Pros:

```text
- could improve upstream integration
```

Cons:

```text
- requires maintaining fork or upstream PR
- still does not solve Method Wheel gating of implement
```

Keep as future contribution, not first internal adoption.

---

## 10. Recommended staged path

### Stage 1 — Generate repo-local wrappers only

```text
source templates → .ai/generated/spec-kit-hermes-adapter/*.md
```

No active profile writes.

### Stage 2 — E review generated wrappers

Check:

```text
- command selection policy followed
- implement disabled/gated
- profile path not touched
- wrapper guardrails present
- upstream source/commit recorded
```

### Stage 3 — Promote a minimal subset to cangwei

Initial subset:

```text
speckit-specify
speckit-clarify
speckit-checklist
speckit-analyze
```

Do not initially promote:

```text
speckit-implement
speckit-taskstoissues
```

### Stage 4 — Sandbox workflow test

Use a sandbox project and loaded wrapper skills to run:

```text
A specify/clarify/checklist
→ C plan maybe later
→ E analyze
```

No implementation.

### Stage 5 — F owner decision

Decide whether to expand to:

```text
plan/tasks/converge
```

and later whether `implement` remains excluded or becomes a gated D handoff.

---

## 11. Codex entry point

Codex is not needed for this design stage.

Codex can enter only after Hermes writes a bounded handoff to implement Option B:

```text
Goal: create repo-local generator script only.
Allowed paths: `.ai/generated/spec-kit-hermes-adapter/`, maybe `scripts/` if approved.
Forbidden: active Hermes profile, default ~/.hermes, upstream Spec Kit source, Method Wheel baseline docs except manifest/report.
Verification: generated wrappers exist, validation passes, git diff review.
```

Until then:

```text
Hermes remains controller and author of the adapter design.
```

---

## 12. E-port acceptance criteria for adapter

Adapter design is acceptable when:

```text
1. It names the unsafe upstream behavior.
2. It avoids direct active-profile install.
3. It defines explicit command import policy.
4. It excludes or gates `speckit-implement`.
5. It defines profile-safe target path.
6. It defines manifest and rollback.
7. It proposes a staged adoption path.
8. It states when Codex may enter.
9. Method Wheel validation passes.
```

---

## 13. Current recommendation

Proceed with:

```text
Option B first: repo-local generator prototype
```

but only after E/F accept this adapter design.

Do not proceed with:

```text
upstream `specify init --integration hermes` on any active workflow repo
```

One-line rule:

```text
Use Spec Kit's templates and theory; do not use its current Hermes installer as the active-profile installer.
```
