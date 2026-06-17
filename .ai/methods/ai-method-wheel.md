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

### 2. Control Layer: Stacked Loop Engineering

The operator should not be the bottleneck for every next prompt. A loop surrounds the agent, but the current method now treats "loop" as a **stack of control loops**, not one repeated agent call:

```text
Agent loop
→ Verification loop
→ Event-driven loop
→ Self-improvement / hill-climbing loop
```

Professional A-port question:

```text
Which loop layer are we designing, checking, or improving?
```

Layer meanings:

| Layer | Purpose | Main owner |
| --- | --- | --- |
| Agent loop | A bounded maker uses tools to complete one task. | C/D |
| Verification loop | A checker applies tests, rubrics, review, false-completion checks, and feedback. | E |
| Event-driven loop | GitHub issues, PRs, CI, cron, webhooks, Slack/Telegram, or heartbeat triggers start runs. | A/D/E |
| Self-improvement loop | Run traces, review failures, owner corrections, and feedback propose diffs to skills/templates/harness. | A/B/E/D/F |

A safe loop requires:

- explicit trigger,
- input routing before model prompting,
- isolated branch/worktree when changing code,
- runtime state under `.ai/loop-runs/<run-id>/` or equivalent GitHub issue/PR,
- separation of durable log, app/runtime state, and model-visible context,
- context projection before each model call,
- separate maker and checker,
- false-completion guard,
- max iterations,
- budget/time cap,
- deterministic checks where possible,
- harness policy checks before tool side effects,
- human/owner review for sensitive actions and broad framework changes,
- self-improvement changes as reviewable diffs, never silent mutation.

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

## Phase 5 — Harness Repair / Self-Improving Skills

Use `ai-workflow-loop-orchestrator`, `ai-workflow-debug`, and `.ai/templates/self-improving-skill-loop.md`.

When an agent workflow fails, do not only fix the artifact. Improve the harness with an inner/outer loop:

```text
Inner loop: skill/template runs on real work and records versioned output + feedback.
Outer loop: scheduled or manual review extracts generalizable lessons and proposes a diff.
A/E gates: accept, experiment, watch, reject, or escalate before baseline changes.
```

Repair flow:

```text
Bad run / failed PR / bad trace / owner correction
→ collect feedback signal and evidence
→ decide whether the lesson is generalizable
→ propose a skill/prompt/template/checklist/CI diff
→ E-port verifies the change and rollback path
→ owner approves broad/risky principle changes
→ merge/promote or keep as experiment/watch
```

Never silently mutate core skills, port prompts, or baseline workflow docs. Self-improvement means **reviewable diffs**, not hidden prompt drift.

## Multi-Port Skill Stack Layer

When a loop spans multiple Telegram bots, profiles, agents, or new conversations, do not rely on a long prompt alone. Use a port skill stack:

```text
port = port identity prompt + primary port skill + auxiliary skills + input/output protocol + verification checklist
```

Typical ports:

```text
A demand/control
B source-pack/context compression
C theory/draft maker
D repo landing/implementation
E verification/PR-CI checker
F owner decision
```

The primary skill defines identity and boundaries. Auxiliary skills provide capabilities such as requirement grilling, source inspection, Codex invocation, GitHub PR workflow, code review, or debugging. See `.ai/methods/multi-port-skill-stack.md`.

### A↔B Double-Gate Knowledge-Frame Loop

When the work is about improving a method, concept system, or knowledge frame, A must not send B a vague "go search" request. Use a two-gate loop:

```text
A creates Initial Knowledge Frame
→ B returns Search Strategy Brief
→ A Gate 1 approves/revises search strategy
→ B executes research and returns Source Pack + Knowledge Fit Report
→ A Gate 2 accepts/partially accepts/rejects evidence for the frame
→ A updates the Knowledge Frame or routes to C/D/E/F
```

This keeps AI execution dominant while avoiding uncontrolled research drift. The owner supplies broad direction and key decisions; A controls the frame and gates; B supplies evidence and fit analysis. See `.ai/methods/multi-port-contracts/a-b-double-gate-loop.md`.

## Hermes-Orchestrated Codex Command Layer

Codex should not be treated as a vague separate chat or an all-purpose executor. For this method wheel:

```text
Hermes = demand clarification, control plane, command orchestrator, checker, PR/CI coordinator
Codex = bounded maker worker invoked through specific CLI commands
GitHub/CI = durable state and objective verification
Owner = product/security/access/merge/release decision maker
```

Use `.ai/methods/hermes-codex-command-orchestration.md` for command selection. Common patterns:

```text
Long theory generation → codex exec + read-only + output-last-message + source pack + background
Repo landing → codex exec + workspace-write + explicit allowed paths + post-run validation
Review → codex review as second opinion, not final checker
Patch mode → generate diff → Hermes review → codex apply → validation
```

A lesson from live use: broad `--add-dir` over large knowledge bases can make Codex spend time expanding source material instead of producing the target artifact. For long theory work, Hermes should first create a compact source pack, then ask Codex to generate from that pack.

## Harness Control Surface / Context Projection

For coding-agent work, the harness is part of the product. A model may propose actions, but the harness/control plane decides what is routed, what context is visible, what tool calls execute, and what state is true.

Use `.ai/templates/harness-control-surface.md` when designing or auditing long-running agent work.

Core split:

```text
Durable log = what happened.
Runtime/app state = what is true now.
Model-visible context = selected projection for the next step.
```

Do not send every input to the model as ordinary prompt text. A-port should first classify whether the input is:

```text
ordinary user request / control command / state query / diagnostic / skill invocation / owner decision / knowledge-frame update
```

Markdown files are also context interfaces, not raw text dumps:

```text
AGENTS.md = workspace instruction context
SKILL.md = task procedure context
specs/plans = bounded implementation context
logs/transcripts = durable evidence that must be projected/summarized
```

## Knowledge Loop / Learning Reserve

Learning articles, social threads, repos, videos, and external methodology sources should not remain one-off chat notes. Store and process them through `.ai/knowledge-loop/`:

```text
inbox → sources → synthesis → frame-updates → decisions → method docs/templates
```

Use this loop when a new article or thread may change the method wheel. A owns the Knowledge Frame and absorption decisions; B supplies search strategy and Source Pack evidence; C/D/E/F only act after the source has a recorded fit/decision. This prevents raw link dumps, over-absorbing viral concepts, and one-time knowledge loss.

## GitHub-Centered Record

Use GitHub as the durable record:

- Specs and ADRs live in the repo.
- Issues describe vertical slices.
- PRs contain verification evidence.
- CI enforces objective gates.
- Method lessons become skills/templates/checklists, not only chat memories.
- External learning sources and knowledge-frame updates live in `.ai/knowledge-loop/`.
