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
- Demand Control Plane upstream boundary: `.ai/methods/demand-control-plane-upstream-boundary.md`
- Demand grilling control gate: `.ai/methods/demand-grilling-control-gate.md`
- Maintainer orchestrator mapping: `.ai/methods/maintainer-orchestrator-mapping.md`
- Codex handoff template: `.ai/templates/codex-issue-handoff.md`
- Project onboarding template: `.ai/templates/project-onboarding.md`
- Loop run template: `.ai/templates/loop-run.md`
- Owner decision brief template: `.ai/templates/owner-decision-brief.md`
- First feature spec template: `specs/_template/*`
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
Upstream control-plane boundary check
→ semantic divergence / problem-world modeling
→ search-intent translation + internal/external recall
→ demand-grilling control gate / Demand Grilling Brief
→ specify / plan / tasks
→ GitHub issues
→ Codex implementation as maker
→ separate checker review
→ TDD / debugging
→ Playwright / accessibility / security QA
→ PR / CI / human review / merge
→ archive / learnback / method update
```

## GitHub as Project Memory

Do not treat chat history as durable project memory. Put long-lived context into GitHub files:

- Decisions: `docs/adr/*`
- Product specs: `specs/*`
- Shared language: `CONTEXT.md`
- Agent rules: `AGENTS.md`
- Work items: GitHub Issues
- Execution record: Pull Requests and CI logs

## Demand Grilling / Demand Control Plane v0.2

Use `.ai/methods/demand-grilling-control-gate.md`, `.ai/methods/demand-control-plane-upstream-boundary.md`, and `.ai/templates/good-question-brief.md` when a request is vague, risky, product-facing, research-heavy, about the method itself, or needs agent-loop routing.

The v0.2 model replaces the older “front gate only” view with an upstream Demand Control Plane:

```text
semantic divergence / problem-world modeling
→ search-intent translation and internal/external recall
→ intent-brainstorm-grill funnel
→ Demand Grilling Brief
→ spec / issue / Codex / maintainer-orchestrator / owner decision
→ verification / CI / review
→ archive and learnback to this AI workflow repo
```

It decides:

```text
intent → problem world → context/recall → scope → assumptions/risks → acceptance criteria → verification → autonomous/needs-owner classification → maker/checker → authority boundary → stop conditions → next stage → learnback target
```

Do not run every upstream skill as a giant questionnaire. Ask only the 1-3 highest-value questions that change scope, safety, routing, authority, or verification.

## Demand Control Plane Boundary

The demand-grilling layer is maintained as an upstream control plane in this AI workflow repository. When a real business project reveals a reusable method flaw, update this repo rather than burying the correction in that business repo.

```text
Reusable workflow protocol / template / benchmark / quality gate → this repo
Project-local evidence / adapter / trial artifact / issue / domain output → business repo
```

Use `.ai/methods/demand-control-plane-upstream-boundary.md` for the boundary and external benchmark matrix.

## Project Onboarding

Use `.ai/templates/project-onboarding.md` when connecting a real repository to this method wheel.

Recommended sequence:

```text
Read-only repo scan
→ AGENTS.md / CONTEXT.md / QA checklist
→ command contract
→ risk map
→ first spec from specs/_template
→ GitHub issue
→ Codex handoff
```

The onboarding skill is available in:

- `.agents/skills/ai-workflow-project-onboarding/SKILL.md`
- `.codex/skills/ai-workflow-project-onboarding/SKILL.md`

## Loop Orchestration

Use `.ai/templates/loop-run.md` when a task may require repeated maker/checker iterations.

The loop-orchestrator skill is available in:

- `.agents/skills/ai-workflow-loop-orchestrator/SKILL.md`
- `.codex/skills/ai-workflow-loop-orchestrator/SKILL.md`

Loop rules:

```text
Define trigger, goal, maker, checker, durable state, stop condition, and budget before running.
Keep Codex as maker for code changes.
Use a separate checker for review.
Record state in GitHub/files, not only chat.
Ask the owner only with a decision-ready brief.
```

Use `.ai/templates/owner-decision-brief.md` before asking for product/security/access/land-delete decisions.

## Maintainer Orchestrator

The upstream OpenClaw/Peter Steinberger `maintainer-orchestrator` skill is installed as a reference and mapped into this method wheel.

Files:

- `.agents/skills/maintainer-orchestrator/SKILL.md`
- `.agents/skills/maintainer-orchestrator/openai.yaml`
- `.codex/skills/maintainer-orchestrator/SKILL.md`
- `.ai/external/steipete-agent-scripts/maintainer-orchestrator/`
- `.ai/methods/maintainer-orchestrator-mapping.md`

Use it when coordinating repository queues, multiple worker threads, PR readiness, CI repair, releases, or owner decision briefs. It turns the loop-orchestrator layer into a maintainer-grade control plane:

```text
inspect → classify → delegate → monitor → decision-ready brief → report/release
```

Key rule: do not ask the owner from a rough issue or half-finished PR. First prepare the work to the decision-ready boundary, then ask for the exact remaining decision/access/waiver/land/delete action.

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
