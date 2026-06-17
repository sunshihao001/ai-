#!/usr/bin/env python
"""Validate that the curated AI method-wheel scaffolding is present and usable."""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'AGENTS.md',
    'CONTEXT.md',
    '.ai/methods/ai-method-wheel.md',
    '.ai/methods/maintainer-orchestrator-mapping.md',
    '.ai/methods/meme-project-lite-direction.md',
    '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/feature.yml',
    'docs/adr/README.md',
    'specs/README.md',
    'docs/qa/playwright-qa-template.md',
    'docs/qa/accessibility-checklist.md',
    'docs/qa/security-checklist.md',
    'docs/handoffs/issue-to-codex.md',
    '.ai/templates/project-onboarding.md',
    '.ai/templates/codex-issue-handoff.md',
    '.ai/templates/loop-run.md',
    '.ai/templates/owner-decision-brief.md',
    '.ai/templates/good-question-brief.md',
    '.codex/skills/dbs-good-question/SKILL.md',
    '.agents/skills/dbs-good-question/SKILL.md',
    '.ai/research/latest-ai-methodology-sources.md',
    'specs/_template/spec.md',
    'specs/_template/plan.md',
    'specs/_template/tasks.md',
    'specs/_template/checklist.md',
]

REQUIRED_SKILLS = [
    'ai-workflow-brainstorm-grill',
    'ai-workflow-specify',
    'ai-workflow-codex-issue',
    'ai-workflow-tdd',
    'ai-workflow-debug',
    'ai-workflow-review-qa',
    'ai-workflow-project-onboarding',
    'ai-workflow-loop-orchestrator',
    'maintainer-orchestrator',
]

REQUIRED_MARKERS = {
    'AGENTS.md': ['GitHub', 'Codex', 'test'],
    '.ai/methods/ai-method-wheel.md': ['grill', 'spec', 'Codex', 'review'],
    'docs/handoffs/issue-to-codex.md': ['AGENTS.md', 'CONTEXT.md', 'GitHub issue', 'verification'],
}


def fail(message: str) -> None:
    print(f'ERROR: {message}', file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    missing += [f'.agents/skills/{name}/SKILL.md' for name in REQUIRED_SKILLS if not (ROOT / '.agents' / 'skills' / name / 'SKILL.md').is_file()]
    if missing:
        fail('missing required files:\n' + '\n'.join(f'- {p}' for p in missing))

    for path, markers in REQUIRED_MARKERS.items():
        text = (ROOT / path).read_text(encoding='utf-8')
        absent = [m for m in markers if m.lower() not in text.lower()]
        if absent:
            fail(f'{path} is missing markers: {absent}')

    print('AI method wheel validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
