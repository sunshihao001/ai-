# AI Method Wheel — Curated Workflow

This project uses a curated subset of three external skill systems:

- `obra/superpowers` — execution discipline, planning, worktrees, verification.
- `github/spec-kit` — spec-driven development: specify → plan → tasks → checklist → implement.
- `mattpocock/skills` — requirement grilling, shared language, TDD, diagnosis, review.

It also absorbs newer loop-engineering and maintainer-orchestrator patterns:

- Loop engineering — design systems that prompt/check agents instead of hand-prompting forever.
- Maker/checker separation — the agent that produces work should not be the only judge.
- Durable state — state belongs in files/GitHub/CI, not only in chat context.
- Decision-ready owner asks — ask the human only after autonomous work is prepared and evidenced.
- Harness repair — when the AI workflow fails, repair the prompt/skill/checklist and lock the failure as a regression.

The goal is not to install every skill. The goal is to compose the core behaviors into one project workflow.

## Pyramid View

### 1. Top Layer: Engineering Judgment

AI agents are tools. The hard part is knowing what to ask, which assumptions are risky, and whether the output is correct, secure, maintainable, accessible, and simple enough.

### 2. Control Layer: Loop Engineering

The operator should not be the bottleneck for every next prompt. A loop surrounds the agent:

```text
Trigger
→ maker produces work
→ separate checker grades it
→ state is written to disk/GitHub
→ maker fixes findings
→ repeat until stop condition or budget cap
```

A safe loop requires:

- explicit trigger,
- isolated branch/worktree,
- durable state file or GitHub issue/PR,
- separate checker,
- max iterations,
- budget/time cap,
- deterministic checks where possible,
- human diff reading before important merges.

### 3. Feedback Layer: Software Engineering Loop

Every serious AI coding task should run through:

```text
Idea
→ Brainstorm
→ Grill / clarify
→ ADR / PRD / spec
→ Plan / tasks / user stories
→ Codex implementation
→ TDD / tests
→ separate review/checker
→ Playwright QA
→ accessibility + security audit
→ human review
→ PR / merge
→ regression/lesson recorded
```

### 4. Skill Layer: Curated Skills

Use only the skills needed for the current phase.

## Phase 0 — Loop / Orchestration Design

Use `ai-workflow-loop-orchestrator`.

Sources:

- Loop engineering posts: trigger, maker, checker, state, stop condition, budget.
- Cursor scaling agents: planners/workers beat flat self-coordination.
- Maintainer orchestrator: control-plane should inspect, delegate, monitor, ask decisions, and report.
- Harness repair: failing runs should become prompt/skill/checklist fixes plus regression tests.

Purpose:

- Decide whether a task should be a loop at all.
- Classify work as autonomous, needs owner, or ignored by owner.
- Define maker/checker roles.
- Define durable state and stop conditions before work starts.
- Prevent uncontrolled agent sprawl and hidden token burn.

Good loop candidates:

- CI failure triage,
- dependency bump reviews,
- lint/typecheck fixes,
- missing tests,
- Playwright smoke checks,
- docs drift checks,
- issue-to-PR drafts on well-tested code.

Bad first-loop candidates:

- architecture rewrites,
- vague product work,
- auth/payments/security-sensitive code,
- destructive production changes,
- anything where done is mostly judgment.

## Phase 1 — Requirement Interrogation

Use `ai-workflow-brainstorm-grill`.

Sources:

- Superpowers: `brainstorming`
- Matt Pocock: `grill-me`, `grill-with-docs`
- Spec Kit: `clarify`

Purpose:

- Challenge vague ideas before code changes.
- Find hidden assumptions, constraints, edge cases, failure modes, and security/accessibility implications.
- Update `CONTEXT.md` when new shared language appears.

Exit criteria:

- Questions start repeating.
- Tradeoffs are explicit.
- Non-goals are documented.
- Acceptance criteria are testable.

## Phase 2 — Production Documentation

Use `ai-workflow-specify`.

Sources:

- Spec Kit: `specify`, `plan`, `tasks`, `checklist`
- Matt Pocock: `to-prd`, `to-issues`
- Superpowers: `writing-plans`

Outputs:

- `specs/<feature>/spec.md`
- `specs/<feature>/plan.md`
- `specs/<feature>/tasks.md`
- `specs/<feature>/checklist.md`
- GitHub issues
- ADRs when architecture decisions are made

## Phase 3 — Codex Execution

Use `ai-workflow-codex-issue` and `ai-workflow-tdd`.

Sources:

- Superpowers: `executing-plans`, `using-git-worktrees`, `subagent-driven-development`
- Matt Pocock: `tdd`, `diagnose`
- Spec Kit: `implement`

Purpose:

- Give Codex a narrow issue/spec, not a vague chat transcript.
- Prefer one issue per branch/worktree.
- Ask Codex to write or update tests first where practical.
- Codex is usually the maker, not the sole checker.

## Phase 4 — QA / Review / Completion

Use `ai-workflow-review-qa` and `ai-workflow-debug`.

Sources:

- Superpowers: `verification-before-completion`, `requesting-code-review`, `systematic-debugging`
- Matt Pocock: `review`, `diagnose`, `improve-codebase-architecture`
- Spec Kit: `analyze`, `checklist`

Quality gate:

- Tests pass or failures are explained.
- Playwright / E2E passes for user-facing changes.
- Accessibility has been checked for UI changes.
- Security risks have been reviewed for auth, permissions, input handling, secrets, dependencies.
- Separate checker has reviewed spec alignment and diff.
- Human reads important diffs before merge.

## Phase 5 — Harness Repair / Method Improvement

Use `ai-workflow-loop-orchestrator` plus `ai-workflow-debug`.

When an agent workflow fails, do not only fix the artifact. Improve the harness:

```text
Bad run / failed PR / bad trace
→ diagnose why the workflow allowed it
→ patch skill/prompt/template/checklist/CI
→ replay or reproduce the failure when possible
→ add regression test or checklist item
→ document the lesson
```

## GitHub-Centered Record

Use GitHub as the durable record:

- Specs and ADRs live in the repo.
- Issues describe vertical slices.
- PRs contain verification evidence.
- CI enforces objective gates.
- Method lessons become skills/templates/checklists, not only chat memories.
