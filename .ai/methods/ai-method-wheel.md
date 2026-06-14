# AI Method Wheel — Curated Workflow

This workflow combines selected core behaviors from:
- Superpowers
- GitHub Spec Kit
- Matt Pocock Skills

It intentionally does not install every upstream skill. It extracts only the useful core behaviors and connects them through GitHub artifacts.

## Pyramid

### Top: Human engineering judgment
Humans decide what matters, what is safe, and what is good enough to ship.

### Middle: Loop engineering
Design loops that repeatedly clarify, specify, implement, verify, review, and record.

### Bottom: Coding agents and tools
Codex, Claude, Hermes, CI, Playwright, linters, tests, security scanners.

## Standard loop
1. Requirement interrogation
2. Production spec
3. User-story / issue slicing
4. Codex implementation
5. TDD / tests / Playwright QA
6. Accessibility and security audit
7. Human review
8. PR / commit / durable record

## Core composite skills
- `ai-workflow-brainstorm-grill`: clarify/grill requirements.
- `ai-workflow-specify`: turn decisions into specs, plans, tasks, checklists, issues.
- `ai-workflow-codex-issue`: hand a bounded issue/spec to Codex.
- `ai-workflow-tdd`: enforce red/green/refactor when appropriate.
- `ai-workflow-debug`: evidence-first debugging.
- `ai-workflow-review-qa`: review, QA, a11y, security, PR readiness.

## GitHub as the connector
Hermes/Claude/chat should produce durable repo artifacts, not be the long-term source of truth.

Use:
- `AGENTS.md` for agent operating rules.
- `CONTEXT.md` for shared project language.
- `specs/<feature>/` for feature specs/plans/tasks/checklists.
- `docs/adr/` for decisions.
- GitHub Issues for work slices.
- Pull Requests for verified delivery evidence.
