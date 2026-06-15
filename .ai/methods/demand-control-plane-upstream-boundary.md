# Demand Control Plane Upstream Boundary

This file is the boundary companion to `.ai/methods/demand-grilling-control-gate.md`.

The full v0.2 protocol lives in the control-gate document. This file exists to make one rule impossible to miss:

```text
Demand Control Plane work is upstream.
Business repositories are trial fields and consumers.
```

## Ownership Split

```text
AI workflow repository
  owns: Demand Control Plane protocol, templates, benchmark research, quality gates, skill mappings, version evolution

Business/project repository
  owns: minimal adapter, project-specific brief, trial artifacts, issues, handoffs, validators, domain outputs
```

## Business Repo Minimalism

When adopting the AI Method Wheel in a half-built or domain-heavy project:

```text
project reality > method wheel
no full method dump
no template bloat
no retroactive ceremony for every historical file
only the next useful slice
```

A business repo may contain:

- a pointer to this upstream method;
- a Project Continuation Brief;
- a project-specific Demand Grilling Brief;
- issue / handoff artifacts for bounded work;
- local validators that protect project artifacts;
- domain outputs such as specs, research notes, samples, code, tests, ADRs.

It should not contain the full reusable Demand Control Plane design unless that repo is itself the AI workflow repo.

## Learnback Rule

When a project exposes a reusable method flaw:

```text
project-local artifact: minimal pointer + evidence of the trial
upstream AI workflow repo: method correction, template, benchmark, validator, or skill change
```

Examples:

```text
A trading KB reveals that MQL5 Articles must be searched for strategy/MQL5 runs → update upstream source contract and project pointer.
A project reveals loaded_reference was being reported as executed → update upstream execution-state vocabulary and validator markers.
A project reveals demand-grilling product-boundary work is bloating the business repo → move boundary/product work upstream.
```

## External Benchmark Matrix

| Source | Type | What to absorb | Boundary |
|---|---|---|---|
| GitHub Spec Kit | Open-source SDD toolkit | `constitution → specify → clarify → plan → tasks → analyze → implement`; specs become executable | Best for software builds; too heavy to dump wholesale into every repo |
| Jama Software SDD | Requirements / traceability methodology | Spec as authoritative source; SDD as context engineering; traceability and compliance evidence | Regulated-engineering framing can be heavier than needed for small projects |
| JetBrains Junie | IDE agent practice | `requirements.md → plan.md → tasks.md`; persistent files guide agents | Good lightweight docs-first loop |
| GSD Core | Spec-driven multi-agent framework | Discuss → Plan → Execute → Verify → Ship; fresh context; `.planning/` artifacts | Strong reference for persistent state and verification |
| OpenSpec | Brownfield-friendly SDD framework | proposal / specs / design / tasks; spec delta review; persistent context | Best analogy for half-built/brownfield projects |
| Grill Me / Matt Pocock-derived skills | Plan interrogation skill | One question per turn; recommended answer; decision tree; inspect repo before asking | Core interrogation lens, not a full workflow by itself |
| Mistral PRD-to-ticket workflow | Agentic PRD pipeline | transcript → PRD → development tickets → Linear/Jira | Needs owner review before tickets become execution truth |
| MQL5 Chinese Articles / Forum | Domain trial-field source | trading system development, testing, risk, AI/LLM integration into EA | Constrains trading trial fields; does not define control-plane product boundary |

## Domain Trial-Field Source Boundary

For MQL5/trading projects, use these as domain constraints:

- `https://www.mql5.com/zh/articles`
- `https://www.mql5.com/zh/forum`
- `https://www.mql5.com/zh/articles/8410`
- `https://www.mql5.com/zh/articles/16973`
- `https://www.mql5.com/zh/articles/13506`

They support:

- implementation and platform mechanics;
- indicator and EA development constraints;
- risk and backtesting discipline;
- realistic skepticism about complexity, overfitting, and automatic execution.

They do **not** prove strategy edge or define the Demand Control Plane boundary.
