---
name: ai-workflow-project-onboarding
description: "Use when connecting a real software repository to this AI method wheel. Scans the repo, creates project-specific AGENTS.md/CONTEXT.md/spec scaffolding, extracts commands, and prepares the first GitHub issue-to-Codex workflow."
---

# Codex Skill: Project Onboarding

Use when a repository needs to be prepared for Codex execution.

## Strict rules

- Start with read-only reconnaissance.
- Do not invent build/test commands. Mark unknowns explicitly.
- Do not read or print secrets from `.env`, credentials, key files, or production configs.
- Do not make product changes during onboarding.
- Prefer a PR over direct commits to `main`.

## Tasks

1. Inspect repo structure and identify stack.
2. Extract install/build/test/lint/typecheck/E2E commands.
3. Create/update `AGENTS.md` with project-specific agent rules.
4. Create/update `CONTEXT.md` with domain language and module map.
5. Create/update `docs/qa/checklist.md` with verification requirements.
6. Create spec scaffolding under `specs/`.
7. Prepare a first issue-to-Codex handoff if a feature/bug is provided.

## Completion criteria

- Onboarding files exist and are specific to the repo.
- Unknowns are listed as unknowns.
- Risk areas and forbidden actions are documented.
- Validation script passes if the repo contains one.
