# ai-

Curated AI software engineering workflow built from the core ideas of:

- Superpowers
- GitHub Spec Kit
- Matt Pocock Skills

## What This Repo Provides

- Project-level AI instructions: `AGENTS.md`
- Shared language file: `CONTEXT.md`
- Curated skills: `.agents/skills/*`
- Method wheel: `.ai/methods/ai-method-wheel.md`
- GitHub issue and PR templates
- Installer script for local agent skill directories

## Install Skills Locally

```bash
python scripts/install-ai-workflow-skills.py --overwrite
```

By default this copies skills into:

- `~/.codex/skills`
- `~/.claude/skills`

## Recommended Workflow

```text
Brainstorm / grill
→ specify / plan / tasks
→ GitHub issues
→ Codex implementation
→ TDD / QA / review
→ PR / CI / merge
```

Do not treat chat history as durable project memory. Put long-lived context into GitHub files.
