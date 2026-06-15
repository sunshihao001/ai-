# Demand Control Plane v0.2 — Demand Grilling Control Gate

Demand Grilling is no longer just a requirements-clarification step inside a project. It is the front door of an independent **Demand Control Plane**: a reusable upstream workflow layer that turns ambiguous human intent into durable, criticizable, verifiable artifacts and routes work to the right maker/checker loop.

This document replaces the older narrow view of “demand grilling as a front gate” with the integrated v0.2 model:

```text
surface ask
→ semantic divergence and problem-world modeling
→ search-intent translation and internal/external recall
→ intent-brainstorm-grill funnel
→ Demand Grilling Brief
→ spec / issue / Codex / maintainer-orchestrator / owner decision
→ verification / CI / review
→ archive and learnback to the upstream method harness
```

## 1. Product Boundary

The Demand Control Plane is upstream. It is not an internal module of any one business repository.

```text
AI workflow repository
  owns: protocol, templates, benchmark research, quality gates, skill mappings, version evolution

Business/project repository
  owns: minimal adapter, project-specific brief, trial artifacts, issues, handoffs, validators, domain outputs
```

Use `.ai/methods/demand-control-plane-upstream-boundary.md` for the explicit boundary and external benchmark matrix.

### Business Repo Rule

When a real project exposes a reusable method flaw:

```text
project-local artifact: minimal pointer + evidence of the trial
upstream AI workflow repo: method correction, template, benchmark, validator, or skill change
```

Do not bury reusable workflow corrections inside the business repo that happened to reveal them.

## 2. Core Claim

Do not run every upstream skill as a giant checklist. Use one control plane that selectively combines the needed lenses and produces one durable brief or artifact.

The user should not see a pile of skill outputs. The user should see a coherent control result:

```text
What is the real problem?
What is known from project context and external sources?
What should not be built or automated?
What is the smallest convergence slice?
Who is maker and checker?
What evidence proves progress?
Where does the result live?
What gets routed next?
```

## 3. External Frameworks Absorbed

The v0.2 model absorbs these external patterns:

| Source | Absorbed behavior | Boundary |
|---|---|---|
| GitHub Spec Kit | `constitution → specify → clarify → plan → tasks → analyze → implement`; specs are executable artifacts | Strong target shape for software builds; do not dump full ceremony into every repo |
| Jama Software SDD | spec as authoritative source; context engineering; traceability; compliance evidence | Useful principle: the spec/context contract is the main human artifact |
| JetBrains Junie | `requirements.md → plan.md → tasks.md`; persistent docs guide agents | Good lightweight pattern for agent control files |
| GSD Core | Discuss → Plan → Execute → Verify → Ship; fresh context; persistent `.planning/` artifacts | Strong reference for long-running loops and verification |
| OpenSpec | proposal / specs / design / tasks; spec delta review; brownfield-friendly iteration | Best analogy for half-built/brownfield projects |
| Grill Me / Matt Pocock-derived skills | one question per turn; recommended answer; decision tree; inspect repo before asking | Core interrogation lens, not a full control plane alone |
| Mistral PRD-to-ticket workflow | transcript → PRD → development tickets → Linear/Jira | Shows productizable PRD-to-ticket pipeline; requires owner review |
| MQL5 Chinese Articles / Forum | domain trial-field constraints for trading projects | Constrains trading trials; does not define this product boundary |

## 4. Control Plane Modules

The Demand Control Plane v0.2 has eight modules.

### 4.1 Constitution / Principles

Define non-negotiable operating principles before routing work:

```text
project reality > method wheel
no code from vague asks
spec/context before implementation
maker is not sole checker
state lives in files/GitHub/CI
owner decisions are decision-ready, not raw confusion
business repos stay lean; reusable method corrections go upstream
```

### 4.2 Semantic Divergence / Problem-World Modeling

Before converging on one “highest-value question,” model the problem world.

Required outputs when the ask is complex, strategic, research-heavy, or about the method itself:

```text
problem_world
solution_world
shared_phenomena
concept_map_seed
issue_tree_seed
unchosen_branches
current_convergence_slice
```

This prevents the demand side from collapsing too early into a task sorter.

### 4.3 Search-Intent Translation and Recall

Do not mechanically search the user’s words. Translate intent first.

Required pre-search block when external or internal research is needed:

```text
owner_surface_terms
interpreted_information_need
professional_concept_family
retrieval_failure_mode
query_transformation_strategy
search_query_variants
query_drift_risk
```

Search both:

```text
internal sources: repo docs, AGENTS.md, CONTEXT.md, ADRs, prior specs, issues, session/project memory when available
external sources: docs, frameworks, forums, articles, codebases, product examples, domain-specific sources
```

For trading/MQL5 trial fields, include `https://www.mql5.com/zh/articles` or state `not_applicable_reason`.

### 4.4 Discovery / Grill

Use the `intent-brainstorm-grill` funnel, combining brainstorming and grill-me discipline:

```text
1. Goal — what outcome should change, not what feature is imagined?
2. Users / operators — who uses, configures, reviews, and bears consequences?
3. Boundaries / non-goals — what is explicitly out of scope?
4. Assumptions — what hidden premises must be true?
5. Failure modes — how can this fail, mislead, or require downgrade?
6. Options — compare simpler / safer / phased alternatives.
7. Acceptance criteria — define verifiable inputs, outputs, tests, and must-nots.
```

Grill discipline:

```text
one question at a time
include a recommended answer
inspect repo/docs before asking if tools can answer it
walk dependency branches in order
record locked decisions
```

### 4.5 Clarify / Specify

Produce a durable Demand Grilling Brief using `.ai/templates/good-question-brief.md`.

The brief must cover or explicitly mark unknown:

```text
original ask
improved agent-usable question
intent and alternatives
context and constraints
scope and non-goals
assumptions and risks
acceptance criteria
verification plan
agent execution classification
maker/checker split
authority boundary
loop stop conditions
critique prompts
missing high-value questions
next stage
```

### 4.6 Plan / Tasks / Issue

Route only after the brief is good enough.

```text
Ready for spec → create spec/plan/tasks/checklist
Ready for GitHub issue → create bounded vertical-slice issue
Ready for Codex → provide exact repo context, issue/spec, commands, authority boundary
Ready for maintainer-orchestrator → classify queue, PRs, workers, CI, owner decisions
Ready for owner decision → ask only the remaining decision/access/waiver/land/delete question
```

### 4.7 Verify / Analyze

Acceptance criteria without proof are incomplete.

Verification may include:

```text
tests / lint / typecheck / build
Playwright / a11y / security / ops checks
CI / PR checks
artifact existence and downstream consumer checks
runtime skill audit: loaded / executed / referenced_only / conditional_not_executed / forbidden
subprotocol evidence: activation_plan / execution_evidence / output_consumed_by
manual review by a separate checker
```

Do not claim “used” when the state is only `listed_only`, `installed`, or `loaded_reference`.

### 4.8 Archive / Learnback

When the workflow succeeds or fails, update the right layer:

```text
business repo: project-specific evidence, trial artifact, issue, handoff, local validator, domain output
AI workflow repo: reusable method correction, template, benchmark, quality gate, skill mapping, version note
```

A project that reveals a method flaw is a trial field. The method correction belongs upstream.

## 5. Execution-State Vocabulary

Use these states precisely:

```text
listed_only: mentioned in docs/templates/plans, no real run or object
installed: available in the environment or repository
loaded_reference: read as a support file or reference
activated: selected as the runtime gate for this run
executed: produced the required artifact or performed the required action
output_consumed: downstream artifact/tool/issue/validator used the output
workflow_integrated: future runs route through it by default
referenced_only: cited as pattern or external inspiration, not executed
conditional_not_executed: intentionally not executed because gated/not applicable
forbidden: explicitly not allowed in this run
```

## 6. Skill / Lens Selection

### Method or Workflow Boundary Problem

Use:

```text
Demand Control Plane boundary
semantic divergence
external benchmark search
runtime skill audit
learnback routing
```

Output:

```text
upstream method correction + minimal project pointer
```

### Pure Product Idea

Use:

```text
brainstorming
grill-me
clarify
dbs-good-question
```

Focus: goal, user, alternatives, non-goals, acceptance.

### Existing Repository Feature

Use:

```text
grill-with-docs
project context docs
clarify
review-quality gate
```

Focus: current behavior, conventions, risky modules, tests, migration.

### Codex Implementation Candidate

Use:

```text
bounded spec/issue
codex execution loop
TDD verification loop
separate checker
```

Focus: exact files/specs, tests, commands, stop conditions.

### Repository Queue / Multi-PR Work

Use:

```text
maintainer-orchestrator
loop-orchestrator
GitHub handoff
owner decision brief
```

Focus: classification, delegation, monitoring, PR readiness, CI/live proof, release gate.

### High-Risk Work

Use:

```text
security/a11y/ops review
owner decision brief
rollback plan
waiver gate
```

Focus: human authorization and irreversible side effects.

## 7. Routing Rules

Route to `Need more questions` when:

```text
target user or desired outcome is unclear
acceptance criteria cannot be tested
authority boundary is unknown for risky actions
safety/security/product direction requires owner judgment
```

Route to `Ready for spec` when:

```text
goal and scope are clear enough
unknowns can be tracked as assumptions/open questions
work needs design before implementation
```

Route to `Ready for GitHub issue` when:

```text
task is a vertical slice
acceptance criteria are objective
one maker can own it
```

Route to `Ready for Codex` when:

```text
issue/spec is bounded
repo context and commands are known
verification is defined
Codex authority is limited to implementation branch work
```

Route to `Ready for maintainer-orchestrator` when:

```text
multiple issues/PRs/workers exist
queue classification or monitoring is needed
owner asks should be decision-ready rather than raw
```

Route to `Ready for owner decision` when:

```text
remaining blocker is product/security/access/merge/release/delete judgment
autonomous preparation is already done or impossible without that decision
```

## 8. Stop Conditions

A target-driven cyclic-agent run must not stop after merely producing recommendations. Once the owner gives a goal, the Demand Control Plane should continue selecting the next slice, executing it, writing durable artifacts, verifying them, and looping until the goal is complete or a real blocker/owner decision is reached.

Do **not** stop at:

```text
recommendation only
static route only
"next step would be..."
"if you want, I can..."
```

The control gate is complete when:

```text
Demand Grilling Brief or upstream method artifact exists
next stage is selected
unresolved questions are reduced to the smallest high-value set
no implementation starts from raw ambiguous chat
verification or owner-decision path is explicit
```

Stop and ask the owner when a missing answer changes:

```text
safety
authority
scope
product direction
verification reality
irreversible side effects
```

## 9. Trading / MQL5 Trial-Field Guard

When the trial field is trading strategy research, apply extra constraints:

```text
observer / labeling / risk-reviewer positioning by default
no automatic trading execution without explicit owner decision
MQL5 Articles are implementation and risk references, not proof of edge
Market/forum claims are hypotheses, not validity evidence
strategy maturity requires samples, falsification, ablation, cost/slippage/drawdown evidence
```

Useful MQL5 source contract:

```text
https://www.mql5.com/zh/articles
https://www.mql5.com/zh/forum
```

If not used in an MQL5/strategy-related run, state why.

## 10. Version Conclusion

Demand Control Plane v0.2 is an upstream AI workflow product layer.

Business repositories are trial fields and consumers, not the home for reusable demand-side product-boundary work.

The v0.2 upgrade replaces the older “front gate only” view with a full loop:

```text
semantic divergence
→ search/recall
→ grill/clarify
→ spec/issue/handoff
→ verify/analyze
→ archive/learnback
```
