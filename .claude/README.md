# Claude/Claude Code Integration

This repo keeps canonical skills in `.agents/skills/`.

Install them into Claude Code with:

```bash
python scripts/install-ai-workflow-skills.py --target ~/.claude/skills --overwrite
```

Use Claude primarily for:

- requirements grilling
- ADR/spec writing
- review and QA reasoning
- architecture critique

Use Codex primarily for bounded issue/spec implementation.
