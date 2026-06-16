# Hermes-Orchestrated Codex Command Workflow

> Status: v0.1  
> Purpose: capture the corrected AI workflow cognition from live use: the operator should not treat Codex as a vague separate chat. Hermes is the demand/control/checker layer that chooses and invokes specific Codex CLI commands as bounded maker workers.

---

## 1. Core correction

Do not say only:

```text
Use Codex.
```

Say instead:

```text
Hermes decides whether Codex is appropriate, chooses the Codex command shape, writes the prompt file, launches Codex with the right sandbox/output mode, monitors completion, checks diff and validation, and only then commits/pushes or asks the owner.
```

The roles are:

```text
Hermes = demand clarification, control plane, command orchestrator, checker, PR/CI coordinator
Codex = maker worker invoked by Hermes CLI/terminal
GitHub/CI = durable state and objective verification
Owner = product/security/access/merge/release decision maker
```

This preserves maker/checker separation. Codex should not receive raw ambiguous chat, should not choose its own authority boundary, and should not be the final judge of completion.

---

## 2. Command family map

Use Codex CLI commands by task type:

```text
codex doctor            # diagnose install/auth/runtime before work
codex exec              # non-interactive maker task; default workhorse
codex exec resume       # continue an exec session when continuity is valuable
codex resume            # resume interactive session
codex review            # second-opinion diff/PR review, not final checker
codex exec review       # non-interactive review
codex apply             # apply a previously generated Codex diff after review
codex features          # inspect feature flags
codex update            # update Codex itself, owner-approved
```

Important flags:

```text
-C, --cd <DIR>                    set working root
--add-dir <DIR>                   add additional readable/writable directory
-s, --sandbox read-only           read-only analysis/theory generation
-s, --sandbox workspace-write     bounded repo edits
-s, --sandbox danger-full-access  fallback when sandbox breaks under gateway/service context
--output-last-message <FILE>      write final response to a file
--json                            JSONL event stream for automation
--output-schema <FILE>            enforce structured final response
--skip-git-repo-check             analyze non-git knowledge folders
--search                          enable web search only when explicitly needed
-m, --model <MODEL>               select model when configured
-p, --profile <PROFILE>           select Codex config profile when configured
```

Avoid by default:

```text
--dangerously-bypass-approvals-and-sandbox
```

Use only in an externally sandboxed environment with explicit owner authorization.

---

## 3. Demand-side routing rules

### Long theory generation

Use when the output is long and conceptual:

```text
architecture theory
method-wheel update
system layer map
large documentation draft
research synthesis
```

Recommended command pattern:

```bash
codex exec \
  -C "<target-repo>" \
  --sandbox read-only \
  --output-last-message "<output-file.md>" \
  - < "<prompt-file.md>"
```

If the task needs extra local references, prefer a compact Hermes-built source pack. Only use `--add-dir` for small, bounded reference dirs.

Hermes terminal mode:

```text
background=True
pty=True
notify_on_complete=True
```

Hermes post-checks:

```bash
git diff --exit-code
test -s "<output-file.md>"
```

If `git diff --exit-code` fails, Codex exceeded read-only expectations or modified the repo; stop and inspect.

---

### Short analysis / small summary

Use foreground when the task is small:

```bash
codex exec -C "<target-repo>" --sandbox read-only - < "<prompt-file.md>"
```

Use Hermes foreground terminal only when it should complete quickly. For anything long, use background.

---

### Repo landing / file updates

Use after theory/spec has been reviewed and the allowed paths are explicit.

Recommended command pattern:

```bash
codex exec \
  -C "<target-repo>" \
  --sandbox workspace-write \
  --output-last-message "<landing-report.md>" \
  - < "<landing-prompt.md>"
```

Fallback when `workspace-write` fails in gateway/service context:

```bash
codex exec \
  -C "<target-repo>" \
  --sandbox danger-full-access \
  --output-last-message "<landing-report.md>" \
  - < "<landing-prompt.md>"
```

Fallback requires:

```text
clean git status before launch
narrow prompt
explicit allowed_paths
explicit forbidden_paths
Hermes diff review after completion
Hermes validation after completion
```

Hermes post-checks:

```bash
git diff --stat
git diff --check
<project validation command>
git status --short --branch
```

Prefer Hermes, not Codex, for commit/push/PR/CI after review.

---

### PR or diff review

Codex review can be a second opinion:

```bash
codex review
codex exec review
```

But final completion decision remains:

```text
Hermes checker + project validation + CI + owner decision
```

Do not let the maker be its own only checker.

---

### Patch application

For higher-risk code changes:

```text
Codex generates diff → Hermes reviews diff → codex apply → validation → commit
```

Use:

```bash
codex apply
```

Avoid direct broad repo mutation when a patch-review-apply loop is safer.

---

### Non-git knowledge base analysis

For folders that are not git repositories:

```bash
codex exec \
  --skip-git-repo-check \
  -C "<knowledge-folder>" \
  --sandbox read-only \
  - < "<prompt-file.md>"
```

---

### External web research

Use `--search` only when local project sources are insufficient. For method-wheel/project consolidation tasks, default to local source packs first; web search easily causes scope expansion.

---

## 4. Source Pack rule for long theory work

A live failure mode was observed: giving Codex a broad prompt plus large `--add-dir` references caused it to spend time expanding source documents instead of producing the requested final theory file.

Rule:

```text
For long theory generation, Hermes should first create a compact source pack, then ask Codex to generate from that source pack. Do not let Codex freely crawl large knowledge bases unless exploration is the explicit task.
```

Bad pattern:

```bash
codex exec -C <repo> --add-dir <huge-knowledge-base> --add-dir <large-source-repo> --sandbox read-only ...
```

Better pattern:

```text
Hermes reads/selects key files
→ Hermes writes source-pack.md
→ Codex reads only source-pack.md plus target repo context
→ Codex writes output-last-message draft
→ Hermes checks repo diff and output file
```

A good source pack includes:

```text
project identity and current stage
root-demand corrections
current architecture/phase model
allowed and forbidden actions
selected facts from external knowledge sources
existing repo files to align with
target output structure
acceptance criteria
```

---

## 5. Prompt-file and output-file pattern

Do not stuff long prompts into a single shell argument. Prefer stdin:

```bash
codex exec ... - < "<prompt-file.md>"
```

For long output, prefer:

```bash
--output-last-message "<output-file.md>"
```

This makes Hermes review easier and avoids losing important content in terminal logs.

Suggested local layout under the Hermes profile:

```text
codex-prompts/<task-name>.md
codex-outputs/<task-name>-draft.md
codex-outputs/<task-name>-landing-report.md
source-packs/<task-name>-source-pack.md
```

These are working artifacts, not durable project truth. Durable truth belongs in the target repo after review.

---

## 6. Default orchestration loop

```text
1. Hermes runs demand clarification and classifies task.
2. Hermes decides if Codex is needed.
3. Hermes creates prompt/source-pack files.
4. Hermes launches Codex with the right command pattern.
5. Hermes monitors process completion.
6. Hermes checks output file and git diff.
7. Hermes reviews content against acceptance criteria and forbidden actions.
8. If landing is needed, Hermes launches a separate landing worker with allowed_paths.
9. Hermes runs validation and CI.
10. Hermes prepares owner decision brief.
```

---

## 7. Current recommended defaults

```text
Long theory:        codex exec + read-only + output-last-message + stdin prompt + background
Long theory w/refs: Hermes source pack first; avoid broad add-dir
Short analysis:     codex exec + read-only + foreground
Repo landing:       codex exec + workspace-write + output-last-message + background
Sandbox fallback:   danger-full-access only with clean git + narrow allowed_paths
Review:             codex review as second opinion; Hermes/CI final
Patch:              generate diff → Hermes review → codex apply
Non-git folder:     --skip-git-repo-check
External research:  --search only when explicitly needed
Structured output:  --output-schema / --json for routing/check reports, not long Markdown
```

---

## 8. Why this belongs in the method wheel

The method wheel's core claim is not merely “use AI agents.” It is:

```text
design the loop that keeps AI execution aligned, verified, reviewable, and recorded.
```

Codex command orchestration is one concrete implementation of that loop. It makes the execution boundary explicit instead of letting “Codex” mean a vague all-powerful agent.
