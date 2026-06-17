# Multi-Port Internal Skill Blueprint

> Status: v0.1 proposal  
> Scope: fill the internal capability stack of each A/B/C/D/E/F port before updating individual Telegram bot prompts.  
> Principle: a port is not a slogan. A port is a role contract + internal skill modules + evidence gates + handoff templates.

## 0. Why this file exists

The current port prompts define identities, but many ports are still too hollow internally. To make the multi-port system executable, each port needs a **stack of key skills** that together implement its core responsibility.

Use this file as the composition map before generating or updating per-port prompt/skill files.

```text
port = core contract + internal skill modules + auxiliary Hermes/GitHub skills + input/output templates + self-check gates
```

Do not update bot prompts directly from this file until the owner approves the port-stack direction.

## 1. Skill categories

Each port should declare skills in these categories:

```text
Core identity skill      What this port uniquely owns.
Input-router skill       How this port classifies incoming material.
Reasoning skill          How this port thinks/derives outputs.
Artifact skill           What file/report it produces.
Handoff skill            How it sends work downstream/upstream.
Verification skill       How it checks its own boundary without becoming E.
Improvement skill        How repeated failures become proposed skill/template updates.
Auxiliary tool skills    Existing Hermes/GitHub/research/Codex skills it may load.
```

## 2. A端 — Demand / Control Plane

### Unique core

```text
Decide what to do and why; turn raw owner intent into a routable, bounded, checkable execution contract.
```

A is the **Intent-to-Spec Control Gate**. It should implement earlier GitHub/external-theory findings around requirements engineering, problem framing, router/supervisor agents, maker-checker boundaries, human-in-the-loop risk gates, and context governance.

### Internal skill modules

```text
A0-port-identity-contract
  Defines A as Demand-Control Plane; forbids long research, theory writing, repo landing, self-review.

A1-input-recognition-router
  Classifies input as ordinary task, knowledge update, repo/code task, diagnostic, control command, state query, owner decision, or skill invocation.

A2-demand-grilling-rewrite
  Converts vague asks into operational questions with goal, context, non-goals, assumptions, risks, acceptance criteria.

A3-requirements-elicitation
  Uses requirements-engineering lenses: stakeholder, user story, edge case, NFR, security/ops/accessibility, business/risk constraints.

A4-spec-spine-placement
  Decides which Spec Spine artifact is needed: constitution/governance, spec.md, clarification, plan.md, tasks.md, checklist, analyze report, PR/ADR.

A5-authority-risk-boundary
  Defines forbidden actions, sensitive permissions, owner approval boundary, rollback and stop conditions.

A6-routing-matrix
  Chooses next port: B evidence, C theory/spec, D landing, E verification, F owner. States return-to-upstream conditions.

A7-maker-checker-design
  Selects maker/checker, success evidence, same-failure escalation rule, and false-completion traps.

A8-knowledge-frame-gate
  For articles/repos/X/Reddit: creates Initial Knowledge Frame, B Search Strategy Request, absorption criteria, ACCEPT/PARTIAL/WATCH/REJECT/ESCALATE decision.

A9-owner-decision-brief
  Produces decision-ready F brief only when human judgment is truly needed.

A10-self-improvement-router
  If a workflow failure repeats, routes to self-improving skill loop with proposal diff, not silent baseline mutation.
```

### Auxiliary skills to combine

```text
dbs-good-question              # demand grilling / professional question rewrite
ai-method-wheel                # repo-backed loop method and protective updates
maintainer-orchestrator        # autonomous vs owner-needed classification, maker/checker orchestration
external-skill-repository-analysis # GitHub/repo/workflow source absorption
github-repo-management         # locate repos/remotes/current state
github-issues                  # convert clarified work into issue slices
github-pr-workflow             # PR/CI state routing when needed
codex                          # command-shape awareness, not direct maker execution
systematic-debugging           # when request is a failure/diagnostic
```

### Primary artifacts

```text
Demand-Control Brief
Initial Knowledge Frame
Search Strategy Request for B
Spec Spine Placement Decision
Routing Brief
Owner Decision Brief
```

### Minimum output gate

A is complete only if it names:

```text
goal + current baseline + protected invariants + target artifact + next port + maker/checker + verification evidence + stop/rollback rule
```

## 3. B端 — Source Pack / Evidence Compression

### Unique core

```text
Decide what evidence/context the work is based on; compress distributed sources into a traceable Source Pack.
```

B should be read-only by default. It does not write theory, does not call Codex, and does not update repo baseline.

### Internal skill modules

```text
B0-port-identity-contract
  Defines read-only evidence/context role and forbidden actions.

B1-source-scope-parser
  Reads A brief and determines required source classes: repo files, docs, GitHub issues/PRs, web/X/Reddit, PDFs, videos, codebase, prior knowledge-loop files.

B2-search-strategy-brief
  Before broad research, proposes where to search, why, expected evidence, exclusions, and quality criteria for A Gate 1.

B3-source-acquisition
  Collects sources using allowed tools/channels; records unavailable/login-gated channels as caveats.

B4-source-quality-grading
  Classifies S1/S2/S3/S4, primary vs secondary, corroborated vs speculative, stale vs current.

B5-evidence-extraction
  Extracts claims, examples, commands, architecture patterns, constraints, contradictions, and unknowns.

B6-coverage-matrix
  Maps sources to A's questions, Spec Spine sections, and C/D/E needs; marks gaps explicitly.

B7-context-compression
  Produces low-noise source pack with summaries, citations/paths, handles to full artifacts, and no huge verbatim dumps.

B8-knowledge-fit-report
  For method updates, reports fit to current baseline and recommends REJECT/WATCH/EXPERIMENT/PARTIAL/ACCEPT/ESCALATE.

B9-return-upstream-gap-report
  Returns to A when scope is unclear, evidence insufficient, source access blocked, or owner authorization is needed.
```

### Auxiliary skills to combine

```text
codebase-inspection            # repo inventory/LOC/language/context
external-skill-repository-analysis # external repos/skill packs/workflow repos
ai-method-wheel                # knowledge-loop/source-pack rules
github-repo-management         # clone/fetch/remotes/files
github-issues                  # issue context when source of truth is GitHub
web / browser / x_search       # external source retrieval if available
ocr-and-documents              # PDFs/scans/images
youtube-content                # video/transcript sources
arxiv / blogwatcher / llm-wiki # deeper research channels when relevant
```

### Primary artifacts

```text
Search Strategy Brief
Source Pack
Coverage Matrix
Evidence Index
Knowledge Fit Report
Gap/Blocker Report
```

### Minimum output gate

B is complete only if it records:

```text
sources searched + sources not searched + quality grades + extracted claims + coverage/gaps + recommended next route
```

## 4. C端 — Theory / Solution / Codex-Orchestration Maker

### Unique core

```text
Form the theory/solution package from A's brief and B's evidence; prepare bounded Codex work when appropriate.
```

C is a maker, but usually not a repo-landing maker. It creates reviewable theory/spec/handoff packages. It should not commit or modify target repo baseline unless explicitly promoted through D.

### Internal skill modules

```text
C0-port-identity-contract
  Defines theory/spec/Codex-orchestration maker role and forbidden repo-landing actions.

C1-brief-source-ingestion
  Reads A Demand-Control Brief and B Source Pack; verifies evidence sufficiency before drafting.

C2-theory-synthesis
  Builds conceptual model, architecture, workflow, assumptions, alternatives, tradeoffs, and falsification points.

C3-spec-spine-drafting
  Drafts or updates proposed spec.md, plan.md, research.md, data-model.md, contracts, quickstart, tasks outline, or checklist proposal.

C4-codex-command-selection
  Chooses `codex exec`/`review`/`apply` pattern, sandbox, allowed paths, input prompt file, output report, and background/foreground mode.

C5-bounded-worker-prompting
  Writes Codex handoff with one vertical slice, allowed files, non-goals, verification commands, stop rules, and output shape.

C6-multi-file-deep-package
  For deep theory work, outputs a package directory instead of one shallow draft; includes master framework, coverage matrix, risk gates, D landing plan, E review checklist, run report.

C7-self-check-and-coverage
  Checks whether all A/B questions are covered, unknowns are marked, and no unsupported claims are promoted.

C8-return-upstream-rules
  Returns to B if evidence is insufficient; returns to A if goal/scope/authority is unclear; returns to F for risk/permission.
```

### Auxiliary skills to combine

```text
codex                          # command/sandbox/output orchestration
ai-method-wheel                # spec/codex/loop method
maintainer-orchestrator        # worker boundary and owner decision shaping
plan                           # planning/spec discipline when available
test-driven-development        # TDD task framing
systematic-debugging           # when solution is a bug/debug theory
spike                          # throwaway validation experiments
external-skill-repository-analysis # for theory based on external repos
```

### Primary artifacts

```text
Theory Package
Spec/Plan Draft
Codex Handoff Prompt
D-Port Landing Plan
E-Port Review Checklist
Coverage/Self-Check Report
```

### Minimum output gate

C is complete only if it provides:

```text
reviewable package + source coverage + assumptions/risks + D landing boundary + E review checklist + return conditions
```

## 5. D端 — Repo Landing / Implementation Maker

### Unique core

```text
Land already-approved artifacts into repository state safely, with validation and commit/PR handoff.
```

D is the repo mutation port. It should not invent theory direction and should not merge.

### Internal skill modules

```text
D0-port-identity-contract
  Defines repo-landing maker role; forbids theory invention, self-review, merges, secrets, destructive actions.

D1-handoff-validation
  Confirms A/C/E approval source, allowed files, target branch, baseline cleanliness, rollback point.

D2-file-change-planning
  Maps approved artifacts to concrete repo paths and edits; checks protected paths and scope.

D3-safe-edit-application
  Applies changes using patch/write tools, not blind shell scripts; preserves existing content and indexes.

D4-codex-execution-wrapper
  If using Codex, runs bounded command with sandbox/path/output controls and captures report.

D5-project-validation
  Runs repo-specific validation: method-wheel validator, tests, lint, typecheck, diff check, link/file checks.

D6-git-pr-handoff
  Stages, commits, pushes, opens/updates PR when appropriate; records commit, branch, PR/check status.

D7-landing-report
  Summarizes changed files, verification commands/outputs, risks, rollback, next E route.

D8-return-upstream-rules
  Returns to A/C if artifact is ambiguous, to E if validation needs review, to F if permission/merge/risk needed.
```

### Auxiliary skills to combine

```text
github-pr-workflow             # branch/commit/push/PR/CI
github-repo-management         # remotes, repo state, clone/fork
codex                          # bounded maker worker when needed
requesting-code-review         # pre-commit review/quality gates
ai-method-wheel                # repo-backed method state
systematic-debugging           # validation failure triage
```

### Primary artifacts

```text
Repo Diff
Commit
PR / PR Update
Landing Report
Validation Output
Rollback Note
```

### Minimum output gate

D is complete only if it records:

```text
clean baseline before work + changed files + validation output + commit/PR handle + next E review request
```

## 6. E端 — Verification / Review / PR-CI Checker

### Unique core

```text
Prove whether the artifact, theory package, or repo diff is valid with independent evidence.
```

E is not a maker. It can run read-only analysis and checks; it should not fix unless a separate D task is created.

### Internal skill modules

```text
E0-port-identity-contract
  Defines independent checker role and forbids maker work/self-certification.

E1-theory-package-review
  Reviews C outputs against A brief and B source pack: coverage, unsupported claims, contradictions, risk, feasibility.

E2-spec-spine-analyze
  Read-only consistency check: spec.md ↔ plan.md ↔ tasks.md ↔ checklist ↔ AGENTS/constitution ↔ tool policy.

E3-diff-scope-review
  Reviews D diff against allowed paths, non-goals, protected baseline, and source artifacts.

E4-verification-command-runner
  Runs or checks deterministic evidence: tests, lint, typecheck, build, validator, PR checks, CI, Playwright when relevant.

E5-security-risk-authority-review
  Checks secrets, permissions, production/destructive risk, owner boundary, trading/API/wallet/swap gates.

E6-false-completion-guard
  Detects missing tests, invented outputs, stale state, unchecked checkboxes, maker self-review, broad unverified claims.

E7-decision-classifier
  Outputs PASS / PASS_WITH_CAVEAT / BLOCK / RETURN_TO_A / RETURN_TO_B / RETURN_TO_C / RETURN_TO_D / OWNER_DECISION_NEEDED.

E8-owner-decision-brief-builder
  Converts unresolved risk into F-ready decision brief with recommendation, alternatives, evidence, rollback.
```

### Auxiliary skills to combine

```text
requesting-code-review         # security/quality review gates
github-code-review             # PR/diff review comments
github-pr-workflow             # PR checks/CI status
ai-method-wheel                # maker/checker and protection rules
systematic-debugging           # root-cause validation failures
test-driven-development        # test quality review
codebase-inspection            # structural/diff context
```

### Primary artifacts

```text
Theory Review Report
Spec Analyze Report
Diff Review Report
Verification Report
Risk Register
Owner Decision Brief
```

### Minimum output gate

E is complete only if it gives:

```text
verdict + evidence handles + commands/results + risks + exact return route or owner decision needed
```

## 7. F端 — Owner Decision Gate

### Unique core

```text
Decide only the human-risk choices: direction, permission, stage gate, baseline promotion, merge/release, and business-risk acceptance.
```

F is the user/owner interface. It should not receive raw chat dumps or half-finished reasoning.

### Internal skill modules

```text
F0-owner-role-contract
  Defines owner as decision gate, not routine maker/checker.

F1-decision-brief-reader
  Reads E/A decision brief and identifies the exact requested decision.

F2-option-comparison
  Compares recommended default, alternatives, costs, risks, rollback.

F3-authorization-boundary
  Approves/denies risky actions: merge, production, credentials, data deletion, baseline promotion, broad scope expansion.

F4-decision-recording
  Records decision in repo/GitHub/decision file so future ports can continue without asking again.

F5-feedback-to-method-loop
  If owner corrects the process, routes correction into self-improvement/protective knowledge-update loop.
```

### Auxiliary skills to combine

```text
owner-decision-brief template
ai-method-wheel                # owner gate principles
github-pr-workflow             # merge/PR/check status visibility when needed
maintainer-orchestrator        # decision-ready owner ask pattern
```

### Primary artifacts

```text
Owner Decision Record
Authorization / Denial
Stage-Gate Result
Merge / Request Changes / Pause Decision
Method Feedback Note
```

### Minimum output gate

F decision is complete only if it records:

```text
chosen option + scope of authorization + expiry/conditions + rollback expectation + next port route
```

## 8. Cross-port skill dependency graph

```text
A uses DBS + method-wheel + maintainer-orchestrator to create the execution contract.
B uses research/repo/source skills to create evidence.
C uses planning/Codex/theory skills to create a reviewable package.
E1 checks C before D mutates repo.
D uses GitHub/Codex/landing skills to change repo safely.
E2 checks D diff/CI after landing.
F authorizes only unresolved risk/stage gates.
```

## 9. Minimum viable port-stack files to create next

Do not start by rewriting all prompts. First create/upgrade these repo skill docs:

```text
.agents/skills/port-a-demand-control/SKILL.md
.agents/skills/port-b-source-pack/SKILL.md
.agents/skills/port-c-theory-codex/SKILL.md
.agents/skills/port-d-repo-landing/SKILL.md
.agents/skills/port-e-verification-review/SKILL.md
.agents/skills/port-f-owner-decision/SKILL.md
```

Each should link to this blueprint and its port contract. After one real loop, promote only proven reusable parts into stable bot prompts.

## 10. Protection rule

This blueprint is a proposal layer. It should strengthen port internals without silently rewriting the current bot prompts or baseline port contracts. Promotion requires:

```text
A decision: PARTIAL_ACCEPT or ACCEPT
E consistency check: pass or pass-with-caveat
Owner approval: required before pushing new initialization prompts to each Telegram bot
```
