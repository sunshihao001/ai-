# ai-

Curated AI software engineering workflow built from the core ideas of:

- Superpowers
- GitHub Spec Kit
- Matt Pocock Skills

This repo intentionally extracts the core behaviors instead of installing every upstream skill.

## What This Repo Provides

- Project-level AI instructions: `AGENTS.md`
- Shared project language: `CONTEXT.md`
- Curated portable skills: `.agents/skills/*`
- Codex project skills: `.codex/skills/*`
- Method wheel: `.ai/methods/ai-method-wheel.md`
- Codex handoff template: `.ai/templates/codex-issue-handoff.md`
- GitHub issue and PR templates
- QA gate: `docs/qa/checklist.md`
- Lightweight GitHub Actions validation
- Installer script for local agent skill directories

## Install Skills Locally

```bash
python scripts/install-ai-workflow-skills.py --overwrite
```

By default this copies skills into:

- `~/.codex/skills`
- `~/.claude/skills`

The repository remains the durable source of truth. Local installs are convenience copies.

## Recommended Workflow

```text
Brainstorm / grill requirements
→ specify / plan / tasks
→ GitHub issues
→ Codex implementation
→ TDD / debugging
→ Playwright / accessibility / security QA
→ PR / CI / human review / merge
```

## GitHub as Project Memory

Do not treat chat history as durable project memory. Put long-lived context into GitHub files:

- Decisions: `docs/adr/*`
- Product specs: `specs/*`
- Shared language: `CONTEXT.md`
- Agent rules: `AGENTS.md`
- Work items: GitHub Issues
- Execution record: Pull Requests and CI logs

## Codex Handoff

Use `.ai/templates/codex-issue-handoff.md` when giving Codex one bounded issue to implement.

The expected handoff pattern is:

```text
Read AGENTS.md, CONTEXT.md, the linked spec, the linked issue, and Codex skill docs.
Implement exactly one issue.
Run verification.
Return files changed, commands run, results, and risks.
```

## QA Gate

Use `docs/qa/checklist.md` before merging AI-generated or AI-assisted work. It covers:

- Spec alignment
- Test quality
- Playwright/E2E
- Accessibility
- Security
- Operations
- Human review
