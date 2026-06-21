# Frame Update Proposal — Protective Loop Engineering Absorption

- Date: 2026-06-17
- Status: PARTIAL_ACCEPT
- Gate: A-port demand/control + E-port consistency review
- Baseline protected: `911281d docs: add PR watch loop learning source` on branch `docs/hermes-codex-orchestration`
- Rollback method: revert this proposal commit or reset affected `.ai/knowledge-loop/` and `.ai/templates/` files to baseline commit.

## A-port demand-grilling intake

Problem this update solves:

```text
The method wheel needs to absorb new AI workflow knowledge quickly, but the current working version must not be overwritten by a wrong, viral, or premature idea.
```

Current assumption challenged:

```text
Earlier knowledge-loop notes treated accepted concepts as candidates for method updates, but did not explicitly separate the stable baseline from candidate/experiment layers.
```

Workflow area affected:

- A-port: stronger knowledge-frame gate, baseline protection, fit decision.
- B-port: stronger source-quality and corroboration checks before promotion.
- D-port: land proposals first, not destructive baseline rewrites.
- E-port: verify consistency and scope drift before promotion.
- F/Owner: only needed for broad/risky framework changes.

Blind-absorption risk:

```text
A single article could reframe the method wheel, weaken maker/checker separation, remove stop conditions, or blur the human owner boundary. The current version might be lost without a rollback point.
```

Evidence required before baseline update:

- Source quality S1/S2, or S3 corroborated by S1/S2.
- Fit decision recorded as ACCEPT or PARTIAL_ACCEPT.
- E-port consistency check passes.
- Change is narrow and rollbackable.
- Broad principle changes are escalated to owner.

## Protective small-loop design

```text
0. Snapshot current baseline.
1. A-port asks what problem/source/assumption/workflow area/risk/evidence is involved.
2. B-port checks quality and corroboration when evidence is insufficient.
3. A-port records REJECT / WATCH / EXPERIMENT / PARTIAL_ACCEPT / ACCEPT / ESCALATE.
4. D-port lands first in proposal/frame-update/template candidate files.
5. E-port checks consistency with current method-wheel invariants.
6. Promote only narrow verified updates; otherwise keep candidate and preserve baseline.
```

## Method-wheel invariants protected by E-port

These must not be weakened by future learning updates:

- A-port controls goal/context/scope/assumptions/risks/route.
- B-port supplies evidence/source packs, not uncontrolled search drift.
- Maker and checker remain separated.
- Loops require durable state, feedback, verification, stop conditions, and escalation rules.
- Human owner gives broad direction and key approvals, not step-by-step micromanagement.
- Social sources cannot override stronger primary/official sources.
- Baseline docs are rollbackable before promotion.

## Decisions for currently absorbed sources

| Source | Quality | A-port decision | Promotion scope | Protection note |
| --- | --- | --- | --- | --- |
| `2026-06-17-addy-osmani-loop-engineering` | S2 | ACCEPT | Baseline concept: loop = system with automation/worktrees/skills/connectors/subagents/state + maker/checker | Do not turn into unattended-autonomy claim. |
| `2026-06-17-yupi996-loop-engineering-ralph-overbaking` | S3 with S2/S3 support | PARTIAL_ACCEPT | Add anti-overbaking, durable goal file, stop hook/condition concepts | Keep Ralph specifics as candidate until primary docs are verified. |
| `2026-06-17-pandatalk8-goal-loop-workflows` | S3 | PARTIAL_ACCEPT | Use Goal/Loop/Workflow as operating vocabulary | Do not treat `/goal` `/loop` `/workflows` command semantics as universal. |
| `2026-06-17-yanhua-design-loops-not-prompts` | S3 + Addy S2 support | PARTIAL_ACCEPT | Absorb human-role framing: design loops, not manual prompt micromanagement | Keep owner as engineer/judgment holder, not passive button-presser. |
| `2026-06-17-freeman1266-loop-engineering-pr-watch` | S2.5/S3 with caveat | ACCEPT_WITH_CAVEAT | Add PR Watch Loop pattern and same-failure escalation rule | Exact user-provided X body was unavailable; use related accessible sources only. |

## E-port consistency result

Pass with constraints.

No accepted source requires replacing the current method-wheel frame. The correct action is additive/narrow:

- preserve current V4 repo-backed loop orchestration baseline;
- add protective promotion gates;
- add same-failure escalation to generic loop template;
- keep source-specific caveats in knowledge-loop notes.

## Promotion decision

PARTIAL_ACCEPT this frame update into the knowledge loop and templates.

Do not rewrite the core method-wheel baseline from these five sources alone. Future sources should use this protective loop before promotion.
