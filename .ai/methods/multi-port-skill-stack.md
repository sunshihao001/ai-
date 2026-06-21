# Multi-Port Skill Stack

> Status: v0.1  
> Purpose: define the contract for composing several skills/roles into a port-oriented workflow using logical ports, not physical bot splits.

---

## 1. Core correction

Do not model a multi-agent workflow as:

```text
one bot = one vague role
```

Do not model a port as:

```text
one prompt only
```

Use this model instead:

```text
port = port identity prompt + port primary skill + auxiliary skill stack + handoff protocol + verification checklist
```

The port prompt initializes a new chat. The primary skill stabilizes the port role. Auxiliary skills provide reusable task capabilities. Repo files and PRs preserve durable state.

---

## 2. Why this matters

In gateway-style or multi-session workflows, each runtime instance may have a separate context. If a port only receives a long prompt once, behavior drifts:

```text
demand ports start executing
maker ports invent requirements
source-pack ports become theory writers
repo-landing ports self-review
review ports summarize without verification
```

Skill stacks reduce drift by making each port's role and tools explicit.

---

## 3. Generic port model

A mature loop-agent system can be split into these ports:

```text
A. Demand / control port
B. Source-pack / context compression port
C. Theory / draft maker port
D. Repo landing / implementation port
E. Verification / PR-CI checker port
F. Owner decision port
```

Loop shape:

```text
Owner trigger
→ A demand gate
→ B source pack
→ C theory maker
→ E draft checker
→ D repo landing maker
→ E repo/CI checker
→ F owner decision
→ GitHub/repo state
→ next loop
```

This is not merely "many runtimes." It is a loop with explicit maker/checker separation, state handoff, stop conditions, and owner gates.


---

## 3.1 Port core-focus rule

A port is mature only when its unique core product is obvious. The current corrected model is:

```text
A = decide what to do and why
B = decide what evidence/source context it is based on
C = form the theory/plan/package
D = land the reviewed package into repo state
E = prove whether it is correct with evidence
F = decide whether the next risk/permission/merge phase is allowed
```

Each port must have a Port Contract with:

```text
identity
unique core task
inputs
outputs
forbidden actions
return-to-upstream rules
downstream handoff rules
completion standard
```

Canonical port contracts live in:

```text
.ai/methods/multi-port-contracts/
```

Do not let ports compete for the same work:

```text
A does not do B's source compression.
B does not do C's theory generation.
C does not do D's repo landing.
D does not do E's independent review.
E does not do F's final decision.
F does not debug routine port work.
```

---

## 4. Port skill stack pattern

Each port should declare:

```text
primary skill: defines role, scope, non-goals, handoff shape
internal skill modules: input router, reasoning procedure, artifact writer, handoff builder, boundary self-check
auxiliary skills: provide specific capabilities
inputs: files, briefs, source packs, issues, PRs
outputs: files, reports, diffs, commits, owner briefs
forbidden actions: safety and authority boundaries
verification: commands, CI, diff checks, review checklists
return path: when to send work back upstream
```

Detailed per-port internals live in:

```text
.ai/methods/multi-port-internal-skill-blueprint.md
```

Do not update Telegram bot prompts directly from a high-level role name. First define the port's internal modules, then create/update the port skill, then update the runtime prompt only after A/E review and owner approval.

---

## 5. A port: demand / control

Primary skill examples:

```text
project-demand-control-port
ai-workflow-demand-port
```

Auxiliary skills:

```text
dbs-good-question
ai-method-wheel
maintainer-orchestrator
github-pr-workflow
github-repo-management
```

Responsibilities:

```text
clarify vague asks
rewrite into agent-usable questions
classify ambiguity
route to next port
set authority boundary
define forbidden actions
define acceptance criteria
prepare owner decision briefs
```

Do not:

```text
do long maker work
run broad Codex tasks from vague input
self-declare implementation complete
merge PRs without owner approval
```

---

## 6. B port: source-pack / context compression

Primary skill examples:

```text
project-source-pack-port
ai-workflow-source-pack-port
```

Auxiliary skills:

```text
codebase-inspection
ai-method-wheel
github-repo-management
ocr-and-documents  # optional when handling PDFs/scans
```

Responsibilities:

```text
read key repo/source files
compress context for maker ports
build source-pack.md
record files read and not read
mark unknowns instead of guessing
prevent broad uncontrolled context crawling
```

Do not:

```text
write final theory
do repo landing
call Codex maker unless explicitly routed
copy huge source documents verbatim
```

Return upstream when:

```text
required files are missing
goal or scope is unclear
source evidence is insufficient
owner decision is needed
```

---

## 7. C port: theory / draft maker

Primary skill examples:

```text
project-theory-codex-port
ai-workflow-theory-codex-port
```

Auxiliary skills:

```text
codex
ai-method-wheel
maintainer-orchestrator
github-repo-management
```

Responsibilities:

```text
consume source pack
create bounded Codex prompt
choose correct Codex command pattern
run read-only theory generation or repo-external output worker
produce draft/theory package files
check target repo has no diff
handoff to checker port
```

For long theory work, prefer:

```text
source pack → Codex prompt → repo-external output directory → multi-file theory package
```

Do not:

```text
modify target repo
commit/push
call live execution tools
access secrets
turn a shallow single-file draft into “deep completion” by label only
```

Return upstream when:

```text
source pack lacks evidence
acceptance criteria are too shallow
business direction needs owner decision
forbidden actions would be required
```

---

## 8. D port: repo landing / implementation

Primary skill examples:

```text
project-repo-landing-port
ai-workflow-repo-landing-port
```

Auxiliary skills:

```text
github-pr-workflow
github-repo-management
codex
requesting-code-review
```

Responsibilities:

```text
apply reviewed content into repo files
update README / source-of-truth / roadmap / indexes / changelogs
run project validation
commit and push to the correct branch
report changed files and verification results
handoff to checker port
```

Sync should stay simple:

```bash
git status --short --branch
<project validation command>
git add -A
git commit -m "docs: ..."
git push
gh pr view ...
gh pr checks --watch
```

Do not:

```text
re-invent requirements
skip checker review
merge PRs
modify secrets
perform production/destructive actions
```

---

## 9. E port: verification / PR-CI checker

Primary skill examples:

```text
project-verification-review-port
ai-workflow-verification-port
```

Auxiliary skills:

```text
requesting-code-review
github-pr-workflow
github-code-review
ai-method-wheel
systematic-debugging
```

Responsibilities:

```text
review maker output against A-port brief
review source-pack coverage
review repo diff and allowed paths
run validation
check PR and CI
detect authority violations
prepare owner decision brief
return work to A/C/D when blocked
```

Do not:

```text
do maker work
accept “looks good” without evidence
merge PRs unless explicitly owner-authorized
let Codex maker self-certify completion
```

---

## 10. F port: owner decision

The owner is not another maker. The owner should receive:

```text
clear decision needed
recommended default
verification evidence
risk summary
alternatives
exact requested action
```

Good owner questions are decision-ready:

```text
merge / request changes / pause / authorize next phase / grant access / reject scope
```

Bad owner questions ask the human to debug the agent’s half-finished reasoning.

---

## 11. Long-output rule

For long prompts, source packs, theory packages, review reports, and owner briefs:

```text
write Markdown files and send paths/attachments
```

Do not paste massive context into chat. Chat should carry concise summaries and file handles.

---

## 12. Repository placement rule

Project-specific skill stacks belong in the project repo:

```text
skills/project-demand-control-port/SKILL.md
skills/project-source-pack-port/SKILL.md
skills/project-theory-codex-port/SKILL.md
skills/project-repo-landing-port/SKILL.md
skills/project-verification-review-port/SKILL.md
```

Generalized patterns belong in the method-wheel repo:

```text
.ai/methods/multi-port-skill-stack.md
.agents/skills/ai-workflow-*/SKILL.md
.codex/skills/ai-workflow-*/SKILL.md
```

Recommended evolution:

```text
project-specific implementation → run one loop → identify reusable parts → promote generic pattern to ai-
```

---

## 13. Relationship to loop orchestration

The skill-stack model implements loop orchestration by making the following explicit:

```text
trigger
role
source context
maker/checker separation
state handoff
verification evidence
stop condition
owner gate
durable repo record
```

Without skill stacks, multi-bot workflows become context islands. With skill stacks, each port can restart in a new chat and still know its role, tools, boundaries, and next handoff.

---

## 13.1 Stacked loop layer mapping

The current workflow treats loop engineering as four stacked layers:

```text
Agent loop → Verification loop → Event-driven loop → Self-improvement loop
```

Port mapping:

| Loop layer | Port meaning | Typical artifacts |
| --- | --- | --- |
| Agent loop | C/D produce bounded work from A's routed contract. | spec, source pack, diff, PR |
| Verification loop | E checks output with tests, rubrics, review, and false-completion guard. | test-report, review-report, false-completion check |
| Event-driven loop | A/D/E runs are triggered by issue, PR, CI, cron, webhook, Telegram/Slack, or heartbeat. | runtime-loop-state, cycle-log, owner decision queue |
| Self-improvement loop | A/B/E/D improve skills/templates from traces, failures, and owner corrections. | skill-improvement proposal, PR/diff, decision record |

This means a port stack is not complete unless it defines both:

```text
execution behavior + improvement behavior
```

For recurring port failures, use:

```text
.ai/templates/self-improving-skill-loop.md
```

Do not let a self-improvement loop silently change a core port prompt. It must propose a diff and pass A/E protection gates.
