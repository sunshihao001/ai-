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
    '.ai/methods/multi-port-skill-stack.md',
    '.ai/methods/a-port-autonomous-logical-loop.md',
    '.ai/methods/abc-knowledge-loop-theory.md',
    '.ai/methods/finished-project-absorption.md',
    '.ai/methods/skill-repository-intake-policy.md',
    '.ai/methods/updated-workflow-after-finished-project-absorption.md',
    '.ai/methods/spec-kit-bridge-layer.md',
    '.ai/methods/spec-kit-runtime-integration-plan.md',
    '.ai/methods/spec-kit-hermes-wrapper-adapter.md',
    'scripts/generate-spec-kit-hermes-adapter.py',
    '.ai/generated/spec-kit-hermes-adapter/manifest.json',
    '.ai/generated/spec-kit-hermes-adapter/report.md',
    '.ai/generated/spec-kit-hermes-adapter/e-review.md',
    '.ai/generated/spec-kit-hermes-adapter/wrappers/speckit-analyze.md',
    '.ai/generated/spec-kit-hermes-adapter/wrappers/speckit-implement.md',
    '.ai/research/spec-kit-runtime/experiment-2026-06-20.md',
    '.ai/methods/hermes-codex-role-split.md',
    '.ai/research/spec-kit/00-index.md',
    '.ai/research/spec-kit/01-theory-and-doctrine.md',
    '.ai/research/spec-kit/02-code-architecture.md',
    '.ai/research/spec-kit/03-project-structure-and-scaffold.md',
    '.ai/research/spec-kit/04-command-and-artifact-model.md',
    '.ai/research/spec-kit/05-extension-and-ecosystem-model.md',
    '.ai/research/spec-kit/06-fit-to-ai-method-wheel.md',
    '.ai/research/spec-kit/07-absorption-decision.md',
    '.ai/research/spec-kit/08-b2-completeness-audit.md',
    '.ai/research/spec-kit/09-source-evidence-appendix.md',
    '.ai/research/spec-kit/10-write-surface-and-rollback.md',
    '.ai/research/spec-kit/e-completeness-checklist.md',
    '.ai/research/fractals/00-index.md',
    '.ai/research/fractals/01-source-facts.md',
    '.ai/research/fractals/02-c-port-bridge-analysis.md',
    '.ai/research/fractals/03-a-port-diversity-subroutine.md',
    '.ai/research/fractals/04-theory-and-decision.md',
    '.ai/research/fractals/05-a-port-boundary-brief.md',
    '.ai/research/fractals/06-progress-and-resume.md',
    '.ai/research/fractals/07-current-state-and-resume-guide.md',
    '.ai/research/fractals/08-external-summary.md',
    '.ai/research/fractals/09-long-theory.md',
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
    '.ai/templates/a-port-strong-trigger.md',
    '.ai/templates/a-port-clarify-loop.md',
    '.ai/templates/abc-knowledge-loop.md',
    '.ai/templates/abc-knowledge-loop-codex-handoff.md',
    '.ai/templates/a-mode-regression-test.md',
    '.ai/templates/a-mode-evolution-log.md',
    '.ai/templates/finished-project-absorption/00-index.template.md',
    '.ai/templates/finished-project-absorption/01-theory-and-doctrine.template.md',
    '.ai/templates/finished-project-absorption/02-code-architecture.template.md',
    '.ai/templates/finished-project-absorption/03-project-structure-and-scaffold.template.md',
    '.ai/templates/finished-project-absorption/04-command-and-artifact-model.template.md',
    '.ai/templates/finished-project-absorption/05-extension-and-ecosystem-model.template.md',
    '.ai/templates/finished-project-absorption/06-fit-to-ai-method-wheel.template.md',
    '.ai/templates/finished-project-absorption/07-absorption-decision.template.md',
    '.ai/templates/finished-project-absorption/e-completeness-checklist.template.md',
    '.ai/research/a-mode-replay-2026-06-19-complex-skill-routing.md',
    '.ai/research/a-mode-replay-2026-06-20-fractals-boundary.md',
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
    'AGENTS.md': ['GitHub', 'Codex', 'test', 'A-mode'],
    '.ai/methods/ai-method-wheel.md': ['grill', 'spec', 'Codex', 'review'],
    '.ai/methods/a-port-autonomous-logical-loop.md': ['logical', 'A-mode', 'skill', 'B', 'C'],
    '.ai/methods/abc-knowledge-loop-theory.md': ['A/B/C 互相驱动知识循环', '证据压缩', '理论综合'],
    '.ai/methods/finished-project-absorption.md': ['B2', 'Finished Project Absorption', 'theory', 'scaffold'],
    '.ai/methods/skill-repository-intake-policy.md': ['SKILL_LAYER', 'PATTERN_ONLY', 'B2', 'control plane'],
    '.ai/methods/updated-workflow-after-finished-project-absorption.md': ['B2 Finished Project Absorption', 'Updated Method Wheel', 'Spec Kit', 'ADOPT'],
    '.ai/methods/spec-kit-bridge-layer.md': ['constitution', 'speckit.implement', 'A/B/C/D/E/F', 'analyze'],
    '.ai/methods/spec-kit-runtime-integration-plan.md': ['temporary HERMES_HOME', 'sandbox', 'cangwei', 'runtime experiment'],
    '.ai/methods/spec-kit-hermes-wrapper-adapter.md': ['NEEDS WRAPPER', 'profile-safe', 'speckit-implement', 'manifest'],
    'scripts/generate-spec-kit-hermes-adapter.py': ['repo-local', 'disabled-handoff-only', 'COMMAND_POLICY', 'writes_active_hermes_profile'],
    '.ai/generated/spec-kit-hermes-adapter/manifest.json': ['disabled-handoff-only', 'writes_active_hermes_profile', 'speckit-implement'],
    '.ai/generated/spec-kit-hermes-adapter/report.md': ['No Hermes profile writes', 'speckit-implement', 'disabled-handoff-only'],
    '.ai/generated/spec-kit-hermes-adapter/e-review.md': ['PASS FOR REPO-LOCAL REVIEW', 'DO NOT PROMOTE YET', 'speckit-implement'],
    '.ai/generated/spec-kit-hermes-adapter/wrappers/speckit-analyze.md': ['read-only', 'Method Wheel Guardrails', 'not installed'],
    '.ai/generated/spec-kit-hermes-adapter/wrappers/speckit-implement.md': ['Disabled Raw Execution Notice', 'disabled-handoff-only', 'A/B/C/E/F gates'],
    '.ai/research/spec-kit-runtime/experiment-2026-06-20.md': ['NEEDS WRAPPER', 'Path.home()', 'speckit-*', 'cangwei'],
    '.ai/methods/hermes-codex-role-split.md': ['Hermes = control plane', 'Codex', 'bounded', 'handoff'],
    '.ai/research/spec-kit/00-index.md': ['Finished Project Absorption Pack', 'B2', 'Spec Kit'],
    '.ai/research/spec-kit/02-code-architecture.md': ['specify-cli', 'INTEGRATION_REGISTRY', 'workflow'],
    '.ai/research/spec-kit/06-fit-to-ai-method-wheel.md': ['B2 Finished Project Absorption', 'ADOPT', 'BRIDGE'],
    '.ai/research/spec-kit/07-absorption-decision.md': ['PARTIAL_ACCEPT_EXPAND', 'ADOPT', 'BRIDGE', 'REJECT AS BASELINE'],
    '.ai/research/spec-kit/08-b2-completeness-audit.md': ['PARTIAL PASS', 'E-port checklist', 'v0.2 hardening'],
    '.ai/research/spec-kit/09-source-evidence-appendix.md': ['Evidence table', 'auditable', 'source path'],
    '.ai/research/spec-kit/10-write-surface-and-rollback.md': ['write-surface', 'rollback', 'profile/global'],
    '.ai/research/spec-kit/e-completeness-checklist.md': ['PARTIAL PASS', 'rollback', 'Verification evidence'],
    '.ai/research/fractals/00-index.md': ['Fractals Theory Pack', '08-external-summary', 'Evidence boundary'],
    '.ai/research/fractals/02-c-port-bridge-analysis.md': ['task orchestration system', 'not a drop-in skill', 'Explicit exclusions from A-port'],
    '.ai/research/fractals/03-a-port-diversity-subroutine.md': ['Safe A-port-adjacent subset', 'Forbidden subset', 'classify'],
    '.ai/research/fractals/04-theory-and-decision.md': ['PARTIAL_ACCEPT', 'BRIDGE', 'not a simple skill'],
    '.ai/research/fractals/05-a-port-boundary-brief.md': ['maximum safe boundary', 'Forbidden Actions', 'Transfer Rule'],
    '.ai/research/fractals/08-external-summary.md': ['PARTIAL_ACCEPT + BRIDGE', 'recursive task-orchestration reference', 'Current safe boundary'],
    '.ai/research/spec-kit/e-completeness-checklist.md': ['PARTIAL PASS', 'rollback', 'Verification evidence'],
    '.ai/templates/a-port-strong-trigger.md': ['A 端强制触发模式', 'A/B/C', 'skill'],
    '.ai/templates/a-port-clarify-loop.md': ['A 端拷问澄清循环', 'route', 'stop or continue'],
    '.ai/templates/abc-knowledge-loop.md': ['A/B/C 互相驱动', 'knowledge loop', 'route'],
    '.ai/templates/abc-knowledge-loop-codex-handoff.md': ['A/B/C theory-generation', 'Codex', 'handoff'],
    '.ai/templates/a-mode-regression-test.md': ['regression', 'A-mode', 'skill', 'choice'],
    '.ai/templates/a-mode-evolution-log.md': ['evolution', 'absorption decision', 'Source Pack', 'verification'],
    '.ai/templates/finished-project-absorption/00-index.template.md': ['Finished Project Absorption Pack', 'B2', 'E completeness check'],
    '.ai/templates/finished-project-absorption/02-code-architecture.template.md': ['Executable entrypoints', 'Configuration and state', 'rollback'],
    '.ai/templates/finished-project-absorption/04-command-and-artifact-model.template.md': ['Command inventory', 'Artifact lifecycle', 'Quality gates'],
    '.ai/templates/finished-project-absorption/06-fit-to-ai-method-wheel.template.md': ['ADOPT', 'BRIDGE', 'PATTERN_ONLY'],
    '.ai/templates/finished-project-absorption/e-completeness-checklist.template.md': ['Anti-shallow-adoption', 'PASS / FAIL / PARTIAL', 'rollback'],
    '.ai/research/a-mode-replay-2026-06-19-complex-skill-routing.md': ['7/7', 'replay-first repair', 'software-development/dbs-good-question'],
    '.ai/research/a-mode-replay-2026-06-20-fractals-boundary.md': ['7/7 PASS', 'A-port fractal boundary route', 'decomposition is not execution permission'],
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
