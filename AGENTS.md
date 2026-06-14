# AGENTS.md — AI Method Wheel Project Instructions

This repository uses a curated AI software-engineering workflow distilled from Superpowers, GitHub Spec Kit, and Matt Pocock Skills.

## Core principle
Do not treat coding agents as the hard part. The hard part is engineering judgment: asking the right questions, validating answers, recognizing brittle/unsafe/over-complex code, and knowing what is actually done.

## Source of truth
- GitHub issues/specs/PRs are durable project memory.
- Chat sessions are temporary thinking surfaces.
- Coding agents execute one bounded issue/spec at a time.

## Required workflow
1. Clarify and grill requirements before implementation.
2. Convert decisions into repo documents: `CONTEXT.md`, `specs/<feature>/spec.md`, ADRs, and GitHub issues.
3. Hand Codex one issue/spec at a time.
4. Prefer TDD where practical: failing test -> implementation -> green -> refactor.
5. Verify with lint/typecheck/tests/Playwright/a11y/security checks as applicable.
6. Open PRs with verification evidence and human-review notes.

## Codex execution rules
When using Codex, make it read:
- `AGENTS.md`
- `CONTEXT.md`
- `.ai/methods/ai-method-wheel.md`
- relevant `.agents/skills/*/SKILL.md`
- relevant `specs/<feature>/*.md`
- the GitHub issue body

Codex must not expand scope beyond the current issue. It must summarize changed files and real verification output.

## Safety
- Never commit secrets, tokens, `.env` files, credentials, or generated logs containing secrets.
- Do not modify production deployment config without an explicit spec, rollback plan, and review.
- Do not claim completion without objective verification.
