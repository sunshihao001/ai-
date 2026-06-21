---
name: ai-workflow-project-onboarding
description: "Use when connecting a real software repository to this AI method wheel. Scans the repo, creates project-specific AGENTS.md/CONTEXT.md/spec scaffolding, extracts commands, and prepares the first GitHub issue-to-Codex workflow."
---

# AI Workflow: Project Onboarding

Use this skill before asking Codex or another coding agent to implement real work in a repository.

## Goal

Turn an existing code repository into a repo that agents can safely operate on by creating durable project memory and verifiable execution paths.

## Inputs

- Repository URL or local path.
- Primary goal for the repository.
- Known constraints: deployment target, stack, owners, risk areas.
- Optional first feature/bug to implement.

## Procedure

### 1. Read-only reconnaissance

Do not edit files yet. Inspect:

- Directory structure.
- Languages/frameworks/package managers.
- Build/test/lint/typecheck commands.
- Existing CI workflows.
- Existing docs, ADRs, runbooks, specs.
- Deployment/runtime scripts.
- Test coverage shape: unit, integration, E2E, Playwright, smoke checks.
- Security-sensitive areas: auth, payments, secrets, migrations, production config.

### 2. Produce project memory

Create or update:

- `AGENTS.md` — agent rules, commands, forbidden actions, PR rules.
- `CONTEXT.md` — domain language, modules, entities, conventions, common traps.
- `docs/adr/README.md` if ADRs do not exist.
- `specs/README.md` if specs do not exist.
- `docs/qa/checklist.md` if QA rules do not exist.

### 3. Extract command contract

Document exact commands:

- Install dependencies.
- Run unit tests.
- Run integration tests.
- Run E2E/Playwright.
- Run lint/typecheck/format.
- Run app locally.
- Build production artifacts.
- Perform smoke checks.

If unknown, write `UNKNOWN` and create a follow-up issue. Do not invent commands.

### 4. Risk map

Create a concise risk map in `CONTEXT.md` or `docs/qa/checklist.md`:

- High-risk modules.
- Files agents must not modify without explicit approval.
- Data migration rules.
- Secrets handling rules.
- External API/payment/auth boundaries.

### 5. First feature path

If a first feature/bug is provided, create:

- `specs/<feature>/spec.md`
- `specs/<feature>/plan.md`
- `specs/<feature>/tasks.md`
- `specs/<feature>/checklist.md`
- GitHub issue draft using `.github/ISSUE_TEMPLATE/feature.yml` fields.
- Codex handoff using `.ai/templates/codex-issue-handoff.md` or `docs/handoffs/issue-to-codex.md`.

### 6. Verification

Before finishing:

- Run `python scripts/validate-ai-method-wheel.py` if present.
- Confirm `git status` only contains intended onboarding files.
- If GitHub is available, create a PR for onboarding instead of pushing to main.

## Output format

Report:

- Files created/updated.
- Commands discovered.
- Unknowns that need human answers.
- Risks and forbidden actions.
- Next recommended issue/Codex handoff.
