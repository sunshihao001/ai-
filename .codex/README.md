# Codex Integration

This repo keeps canonical skills in `.agents/skills/`.

Preferred Codex context order:

1. `AGENTS.md`
2. `CONTEXT.md`
3. Relevant `specs/<feature>/*`
4. Relevant GitHub issue
5. One composite skill from `.agents/skills/*`
6. `docs/handoffs/issue-to-codex.md`

## Installing skills for Codex

Run:

```bash
python scripts/install-ai-workflow-skills.py --target ~/.codex/skills --overwrite
```

If your Codex version supports project-local skills, you may also copy the curated skills into `.codex/skills/`, but keep `.agents/skills/` as the source of truth.
