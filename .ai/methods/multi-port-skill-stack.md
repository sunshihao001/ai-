# Multi-Port Skill Stack Method

> Status: v0.1  
> Purpose: capture the corrected loop-agent cognition that a port is not just one prompt or one skill. A port is a role-specific skill stack: identity skill + auxiliary skills + input/output protocol + verification gates.

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

In Telegram / gateway / multi-bot workflows, each bot or new conversation may have a separate context. If a port only receives a long prompt once, behavior drifts:

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

This is not merely “many bots.” It is a loop with explicit maker/checker separation, state handoff, stop conditions, and owner gates.

---

## 4. Port skill stack pattern

Each port should declare:

```text
primary skill: defines role, scope, non-goals, handoff shape
auxiliary skills: provide specific capabilities
inputs: files, briefs, source packs, issues, PRs
outputs: files, reports, diffs, commits, owner briefs
forbidden actions: safety and authority boundaries
verification: commands, CI, diff checks, review checklists
return path: when to send work back upstream
```

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
