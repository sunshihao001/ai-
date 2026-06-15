# Demand Grilling Control Gate

Demand grilling is the front control gate of the AI Method Wheel. In the loop-agent era, it does more than clarify product intent: it decides which agent loop, authority boundary, verification path, and owner decision route the work should enter.

## Core Claim

Do not run every upstream skill as a giant checklist. Use one control gate that combines the useful questioning perspectives and produces one durable brief.

The Demand Grilling / Demand Control Plane boundary is upstream: reusable demand-grilling protocol, templates, benchmark research, and quality gates belong in this AI workflow repository. Business repositories should keep only a minimal adapter, trial artifact, issue/handoff, project-local validator, or domain output.

See `.ai/methods/demand-control-plane-upstream-boundary.md` for the boundary and external benchmark matrix.

```text
vague ask
→ demand-grilling control gate
→ Demand Grilling Brief
→ route to spec / issue / Codex / maintainer-orchestrator / owner decision
```

## Skill Perspectives Combined

The gate combines these perspectives:

- **Superpowers `brainstorming`** — challenge the goal and compare simpler/safer approaches.
- **Matt Pocock `grill-me`** — expose vague words, missing users, boundaries, and acceptance criteria.
- **Matt Pocock `grill-with-docs`** — interrogate the ask against repo docs, current behavior, ADRs, AGENTS.md, CONTEXT.md, and risky modules.
- **Spec Kit `clarify`** — turn open questions into spec decisions, assumptions, and checklist items.
- **`dbs-good-question`** — package the result as an agent-reasonable, criticizable, verifiable brief.
- **Maintainer orchestrator** — classify work as `Autonomous`, `Needs owner`, or `Ignored by owner`; set authority boundaries and owner-decision rules.
- **Review / verification gate** — define evidence, checker responsibilities, false-success traps, and live-proof needs.

## What Changed from Traditional Requirement Clarification

Traditional clarification asks:

```text
What should be built?
Who is it for?
How do we know it is done?
```

Loop-agent clarification must also ask:

```text
Who is the maker?
Who is the checker?
What can be automated?
What requires owner authorization?
Where is durable state recorded?
How many maker/checker loops are allowed?
What evidence prevents false success?
What exact blocker/decision brief is required if the loop cannot finish?
```

## Operating Principles

1. **One brief, many lenses.** The user should see a coherent Demand Grilling Brief, not a pile of skill outputs.
2. **Ask only high-value questions.** Prefer 1-3 questions that change routing, scope, authority, or verification.
3. **Do not average all skills.** Select the needed lenses based on risk and context.
4. **No code from vague asks.** Raw chat is not a Codex handoff.
5. **Route before executing.** Decide whether the next artifact is a spec, GitHub issue, Codex task, maintainer-orchestrator item, or owner decision brief.
6. **Verification is part of the requirement.** Acceptance criteria without proof are incomplete.
7. **Authority is part of the requirement.** Editing, pushing, merging, deploying, deleting, spending money, and accessing secrets are separate permissions.

## Lens Selection

### Pure Product Idea

Use strongest lenses:

- brainstorming,
- grill-me,
- clarify,
- dbs-good-question.

Focus on goal, users, alternatives, scope, non-goals, acceptance criteria.

### Existing Repository Feature

Use strongest lenses:

- grill-with-docs,
- project context docs,
- clarify,
- review-quality gate.

Focus on current behavior, existing conventions, risky modules, tests, migration, compatibility.

### Codex Implementation Candidate

Use strongest lenses:

- dbs-good-question,
- spec-driven docs,
- codex execution loop,
- TDD verification loop.

Focus on bounded issue, exact files/specs, tests, commands, stop conditions, risks.

### Repository Queue / Multi-PR Work

Use strongest lenses:

- maintainer-orchestrator,
- loop-orchestrator,
- GitHub handoff,
- owner decision brief.

Focus on classification, delegation, monitoring, worker boundaries, PR readiness, CI/live proof, release gate.

### High-Risk Work

Use strongest lenses:

- review-quality gate,
- security/a11y/ops risk,
- maintainer-orchestrator,
- owner decision brief.

Focus on human authorization, rollback, abuse cases, data exposure, destructive operations, waiver conditions.

## Required Output: Demand Grilling Brief

Use `.ai/templates/good-question-brief.md` as the durable template. The brief must answer or explicitly mark unknown:

- Original ask.
- Improved agent-usable question.
- Intent and alternative approaches.
- Context and constraints.
- Scope and non-goals.
- Assumptions and risks.
- Acceptance criteria.
- Verification plan.
- Agent execution classification.
- Maker/checker split.
- Authority boundary.
- Loop stop conditions.
- Critique prompts.
- Missing high-value questions.
- Next stage.

## Routing Rules

Route to `Need more questions` when:

- the target user or desired outcome is still unclear,
- acceptance criteria cannot be tested,
- authority boundary is unknown for risky actions,
- safety/security/product direction requires owner judgment.

Route to `Ready for spec` when:

- the goal and scope are clear enough,
- remaining unknowns can be tracked as assumptions/open questions,
- the work needs design before implementation.

Route to `Ready for GitHub issue` when:

- the task is a vertical slice,
- acceptance criteria are objective,
- the issue can be assigned to one maker.

Route to `Ready for Codex` when:

- the issue/spec is bounded,
- repo context and commands are known,
- verification is defined,
- Codex authority is limited to implementation branch work.

Route to `Ready for maintainer-orchestrator` when:

- there are multiple issues/PRs/workers,
- queue classification or monitoring is needed,
- owner asks should be decision-ready rather than raw.

Route to `Ready for owner decision` when:

- the remaining blocker is product/security/access/merge/release/delete judgment,
- autonomous preparation is already done or impossible without that decision.

## Stop Conditions for the Gate

The gate is complete when:

- a Demand Grilling Brief exists,
- the next stage is selected,
- unresolved questions are limited to the smallest high-value set,
- no implementation starts from raw ambiguous chat.

The gate must stop and ask the owner when a missing answer changes safety, authority, scope, or verification.
