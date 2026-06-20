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
- Maintainer orchestrator mapping: `.ai/methods/maintainer-orchestrator-mapping.md`
- Hermes → Codex command orchestration: `.ai/methods/hermes-codex-command-orchestration.md`
- Hermes / Codex role split: `.ai/methods/hermes-codex-role-split.md`
- Multi-port skill stack method: `.ai/methods/multi-port-skill-stack.md`
- A-port autonomous logical loop: `.ai/methods/a-port-autonomous-logical-loop.md`
- Finished project absorption method: `.ai/methods/finished-project-absorption.md`
- Updated workflow after finished-project absorption: `.ai/methods/updated-workflow-after-finished-project-absorption.md`
- Spec Kit bridge layer: `.ai/methods/spec-kit-bridge-layer.md`
- Spec Kit full absorption pack: `.ai/research/spec-kit/`
- Multi-port contracts: `.ai/methods/multi-port-contracts/`
- Knowledge loop / learning reserve: `.ai/knowledge-loop/`
- A-port strong trigger template: `.ai/templates/a-port-strong-trigger.md`
- A-mode regression test template: `.ai/templates/a-mode-regression-test.md`
- A-mode replay samples: `.ai/research/a-mode-replay-*.md`
- A-mode evolution log template: `.ai/templates/a-mode-evolution-log.md`
- Codex handoff template: `.ai/templates/codex-issue-handoff.md`
- Codex theory-generation handoff template: `.ai/templates/codex-theory-generation-handoff.md`
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
Loop / orchestration design
→ brainstorm / grill requirements
→ if the source is a mature external project: B2 finished-project absorption
→ specify / plan / tasks
→ GitHub issues
→ Codex implementation as maker
→ separate checker review
→ TDD / debugging
→ Playwright / accessibility / security QA
→ PR / CI / human review / merge
→ regression or method update
```

## GitHub as Project Memory

Do not treat chat history as durable project memory. Put long-lived context into GitHub files:

- Decisions: `docs/adr/*`
- Product specs: `specs/*`
- Shared language: `CONTEXT.md`
- Agent rules: `AGENTS.md`
- Work items: GitHub Issues
- Execution record: Pull Requests and CI logs

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

## Finished Project Absorption

Use `.ai/methods/finished-project-absorption.md` before absorbing mature external GitHub projects into the Method Wheel. The corrected route is:

```text
A absorption question
→ B source pack
→ B2 finished project absorption pack
→ A absorption decision
→ C bridge/method synthesis
→ D/E/F landing, verification, and approval
```

A B2 pack must understand theory, code architecture, project structure/scaffold, command/artifact model, extension ecosystem, fit/non-fit, and risks before baseline updates. Spec Kit is the first example pack at `.ai/research/spec-kit/`.

## Hermes / Codex Role Split

Use `.ai/methods/hermes-codex-role-split.md` whenever C/D/E work may involve Codex. The rule is:

```text
Hermes = control plane / orchestrator / owner-facing reasoning loop
Codex  = bounded coding or review worker, invoked only with a prepared contract
```

Entering C-port does not automatically invoke Codex. Hermes handles understanding, routing, method design, runtime-integration planning, E checks, and owner briefs. Codex is optional only for bounded code/scaffold/test/review tasks with exact scope, verification commands, and stop conditions.

## Spec Kit Bridge Layer

Use `.ai/methods/spec-kit-bridge-layer.md` only after the B2 full absorption pack exists. The accepted model is:

```text
Spec Kit = spec-driven artifact spine
AI Method Wheel = A/B/C/D/E/F control plane
```

Bridge the commands as:

```text
/speckit.constitution → F/A governance baseline
/speckit.specify      → A-port WHAT/spec candidate
/speckit.clarify      → A-port targeted ambiguity removal
/speckit.plan         → C-port HOW/package
/speckit.tasks        → D-port bounded maker queue
/speckit.analyze      → E-port read-only checker
/speckit.implement    → D-port execution only after A/B/C/E/F gates
```

Do not run broad `speckit.implement` from vague owner intent, and do not install global Hermes `speckit-*` skills without profile-path and rollback checks.

## Logical A/B/C Loop Before Physical Multi-Port Split

Use `.ai/methods/a-port-autonomous-logical-loop.md` when the owner wants A/B/C reasoning without splitting into multiple physical bots. The corrected default is:

```text
one Hermes/control-plane session
→ logical A/B/C stages
→ explicit skill routing
→ durable repo/GitHub artifacts
```

Use `.ai/templates/a-port-strong-trigger.md` to force A-mode when a vague idea needs demand excavation. Use `.ai/templates/a-mode-regression-test.md` and `.ai/research/a-mode-replay-*.md` when A-mode behavior drifts. Use `.ai/templates/a-mode-evolution-log.md` when a correction, external source, or skill-routing lesson may update the method wheel. In A-mode, do not keep asking the owner to choose A/B/C/D repeatedly. Infer the primary route, select the smallest relevant skill family, report skill ambiguity explicitly, ask only the next blocking question, and transfer to B/C only when the stop rule says the route is mature enough. When the owner says “继续打磨/可以” after a drift, use replay-first repair instead of asking for another broad branch choice.

## Multi-Port Skill Stacks

Use `.ai/methods/multi-port-skill-stack.md` only when splitting a loop-agent workflow across multiple bots, profiles, or new conversations is explicitly desired. The corrected model is:

```text
port = port identity prompt + port primary skill + auxiliary skill stack + handoff protocol + verification checklist
```

This prevents physical multi-bot workflows from becoming disconnected context islands.

Canonical port contracts are in `.ai/methods/multi-port-contracts/`. Their core split is:

```text
A = what/why, B = evidence, C = theory/plan, D = repo landing, E = proof, F = permission/decision.
```

## Knowledge Loop / Learning Reserve

Use `.ai/knowledge-loop/` for articles, X/Reddit threads, GitHub repos, videos, forum discussions, and external methodology sources that may update the method wheel. This is a continuing learning/update loop, not a one-time link dump:

```text
inbox → sources → synthesis → frame-updates → decisions → method docs/templates
```

A-port owns the knowledge frame and absorption decisions. B-port supplies search strategy and source packs. D/E only land and verify method changes after a recorded fit decision.

## Hermes-Orchestrated Codex Commands

Use `.ai/methods/hermes-codex-command-orchestration.md` when Hermes needs to call Codex CLI as a bounded worker. The corrected pattern is:

```text
Hermes clarifies and routes → Hermes writes prompt/source pack → Hermes invokes Codex command → Hermes checks output/diff/validation → GitHub/CI records evidence → owner decides.
```

For long theory generation, prefer a compact Hermes-built source pack and:

```text
codex exec -C <repo> --sandbox read-only --output-last-message <draft.md> - < <prompt.md>
```

For landing reviewed content into a repo, prefer a separate bounded worker with explicit allowed paths and `workspace-write`; use `danger-full-access` only as a gateway/sandbox fallback with clean git state and post-run review.

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
