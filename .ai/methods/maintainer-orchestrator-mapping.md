# Maintainer Orchestrator Mapping

Source: `steipete/agent-scripts`, commit `448cfa9`, skill `skills/maintainer-orchestrator/SKILL.md`.

Installed copies:

- `.agents/skills/maintainer-orchestrator/SKILL.md` — upstream skill copy.
- `.agents/skills/maintainer-orchestrator/openai.yaml` — upstream OpenAI metadata.
- `.codex/skills/maintainer-orchestrator/SKILL.md` — Codex-facing adaptation.
- `.ai/external/steipete-agent-scripts/maintainer-orchestrator/` — reference snapshot.

## What This Skill Is

`maintainer-orchestrator` is a **control-plane maintainer skill**. It is not primarily a coding skill. Its job is to coordinate repository maintenance through workers until work reaches a proof-backed, decision-ready state.

Core loop:

```text
inspect repository queue
→ classify item
→ delegate bounded work
→ monitor worker state
→ intervene only on evidence
→ prepare decision-ready PR/issue/release
→ ask owner only for exact remaining decision
→ record/report outcome
```

## Concrete Requirements Extracted From the Skill

### 1. Repository Scope And Ledger

The orchestrator needs a current repository ledger. It must know:

- which repositories are in scope;
- which are archived/suppressed/ignored;
- current open issues and PRs;
- CI state;
- latest release;
- package metadata;
- unreleased changelog.

Mapping in this repo:

- Use `GitHub Issues`, `PRs`, `docs/adr/`, `specs/`, and `.ai/templates/loop-run.md` as durable state.
- For multi-repo use, add a portfolio ledger such as `.ai/portfolio-ledger.md` or an external private ops ledger.

### 2. Queue Classification

Every item is classified as:

- `Autonomous`: clear, bounded, reproducible, verifiable.
- `Needs owner`: product/security/privacy/access/live-proof/destructive decision.
- `Ignored by owner`: only if explicitly named by owner.

Mapping in this repo:

- Add this classification to issue triage and `loop-run.md`.
- `ai-workflow-loop-orchestrator` decides whether Codex should work or whether the owner must decide.

### 3. Control-Plane Ownership

Only the root orchestrator may:

- create/reuse/assign/rename worker threads;
- steer workers;
- manage portfolio triage;
- archive/retire worker lanes.

Workers must not:

- create subworkers;
- delegate;
- manage other chats;
- expand scope.

Mapping in this repo:

- `ai-workflow-loop-orchestrator` = root control plane.
- `ai-workflow-codex-issue` / Codex = repository worker.
- Worker prompts must explicitly say: `Do not create subworkers or delegate.`

### 4. Decision-Ready Queue Rule

Do not ask the owner from a rough issue or unprepared PR.

Before asking, the worker/orchestrator should do all autonomous work:

- inspect/reproduce;
- root cause;
- implement bounded candidate if appropriate;
- add tests/docs/changelog;
- run live proof and review;
- push/prepare PR if authorized;
- get CI green if possible.

Then ask only for:

- land prepared PR;
- delete/close;
- provide exact access step;
- choose between documented alternatives;
- grant explicit waiver.

Mapping in this repo:

- Use `.ai/templates/owner-decision-brief.md`.
- PR template must include proof and exact remaining decision.
- Hermes/Claude should not ask you vague questions after work is still autonomously solvable.

### 5. Monitoring Protocol

Before steering a worker:

1. Read latest worker state.
2. Treat newest thread-local instruction as authoritative.
3. Determine active / blocked / completed / idle.
4. Do nothing if active worker is making coherent progress.

Intervene only on:

- explicit blocker;
- completed/no work;
- repeated no-progress failures with concrete correction;
- wrong repo/item;
- unauthorized mutation;
- destructive/security/release-gate risk;
- gross divergence.

Mapping in this repo:

- Do not constantly re-prompt Codex while it is working.
- Poll via GitHub state, PR comments, CI logs, and worker summary.
- Use `loop-run.md` to record intervention reason.

### 6. Authorization Boundaries

The skill separates permissions:

- triage;
- monitoring;
- implementation;
- push/PR update;
- CI rerun/fix;
- merge/close;
- release/version/tag/publish.

Mapping in this repo:

- Every Codex handoff should include explicit authorization.
- Default safe boundary: local edit + tests + summary.
- Push/merge/release require explicit user approval.

### 7. Worker Contract

Workers must:

- read full issue/PR discussion, repo instructions, docs, code;
- reproduce/root cause before accepting patch;
- rewrite when cleaner bounded design exists;
- add regression coverage;
- run focused/full tests;
- run live/end-to-end proof for the affected boundary;
- run review/autoreview;
- push/fix CI/merge only when authorized;
- return clean `main` after authorized landing.

Mapping in this repo:

- `ai-workflow-codex-issue` should carry these requirements.
- `docs/qa/checklist.md` and PR template capture proof.

### 8. Live Proof Gate

Live proof is not optional for runtime/user-facing changes.

Evidence can include:

- command used;
- final candidate commit;
- real built/installed artifact;
- real service/account/device/provider where applicable;
- redacted response class or observed state transition.

If access is unavailable, finish everything else and ask for exact access or waiver.

Mapping in this repo:

- Add live proof to QA checklist.
- Do not treat mocks/docs/fixtures as full replacement for external integrations.

### 9. Public/Secret Safety Gates

The upstream skill has strong gates for public model identifiers and secrets:

- never expose private/internal identifiers;
- do not echo questionable identifiers;
- audit diffs/logs/artifacts before public mutation;
- never print credentials;
- credential discovery stays in the worker that needs it.

Mapping in this repo:

- Keep secret scan in CI.
- Keep `AGENTS.md` secret rules.
- For public reports, use generic descriptions for unknown/private identifiers.

### 10. Release Gate

Release requires:

- explicit release authorization;
- empty effective issue/PR queue or explicit ignored items;
- green CI;
- live proof/waiver;
- clean checkout;
- justified SemVer version;
- verified tag/GitHub Release/package artifact.

Mapping in this repo:

- Release is a separate loop, not implied by merge.
- Add release spec/runbook when a real project needs publishing.

## Where It Fits In The Existing AI Method Wheel

```text
Requirement grilling
  ↓
Spec / plan / tasks / issue
  ↓
Maintainer Orchestrator classifies item
  ↓
Autonomous? → delegate to Codex worker
Needs owner? → prepare decision brief
Ignored? → record explicit owner exception
  ↓
Worker executes bounded task
  ↓
Checker / QA / CI / live proof
  ↓
Decision-ready owner brief or autonomous merge boundary
  ↓
PR / release / closeout
  ↓
Harness repair if the loop failed
```

## Practical Use In This Repo

Use `maintainer-orchestrator` when the task is larger than one direct coding issue, for example:

- multiple issues/PRs need triage;
- a queue must be prepared for merge/release;
- multiple Codex workers may run;
- you need owner decisions but only after proof is prepared;
- release gating matters;
- a recurring maintenance loop is needed.

Do **not** use it for a tiny one-shot edit. For those, use `ai-workflow-codex-issue` directly.

## Recommended Handoff Prompt

```text
Use maintainer-orchestrator as the root control plane.

Scope:
- Repository: <owner/repo>
- Queue: issues/PRs matching <criteria>
- Authorization: triage + local implementation only / push allowed / CI fix allowed / merge not allowed / release not allowed

Rules:
- Classify each item as Autonomous, Needs owner, or Ignored by owner.
- Delegate only bounded Autonomous items to Codex workers.
- Workers must not subdelegate.
- Do not ask the owner until the item is decision-ready.
- Use owner-decision-brief.md for every owner question.
- Record durable state in GitHub/specs/PRs, not chat.
```
