# AI Method Wheel — Curated Workflow

This project uses a curated subset of three external skill systems:

- `obra/superpowers` — execution discipline, planning, worktrees, verification.
- `github/spec-kit` — spec-driven development: specify → plan → tasks → checklist → implement.
- `mattpocock/skills` — requirement grilling, shared language, TDD, diagnosis, review.

The goal is not to install every skill. The goal is to compose the core behaviors into one project workflow.

## Pyramid View

### 1. Top Layer: Engineering Judgment
AI agents are tools. The hard part is knowing what to ask, which assumptions are risky, and whether the output is correct, secure, maintainable, accessible, and simple enough.

### 2. Loop Layer: Feedback System
Every serious AI coding task should run through a loop:

```text
Idea
→ Brainstorm
→ Grill / clarify
→ ADR / PRD / spec
→ Plan / tasks / user stories
→ Codex implementation
→ TDD / tests
→ Playwright QA
→ accessibility + security audit
→ human review
→ PR / merge
```

### 3. Skill Layer: Curated Skills
Use only the skills needed for the current phase.

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
- Human reads the diff before merge.

## GitHub-Centered Record
Use GitHub as the durable record:
- Specs and ADRs live in the repo.
- Issues describe vertical slices.
- PRs contain verification evidence.
- CI enforces objective gates.
