# Demand Control Plane — Upstream Boundary and External Benchmarks

The demand-grilling layer is an independent control plane, not an internal module of any one business repository.

A business repository may serve as a trial field, but the product boundary, reusable protocol, benchmark research, and quality gates belong in the AI workflow repository.

```text
AI workflow repo
  owns: Demand Control Plane protocol, templates, benchmarks, quality gates, skill mappings, version evolution

Business/project repo
  owns: minimal adapter, project-specific brief, trial artifacts, issues, handoffs, validators, domain outputs
```

## Why This Boundary Exists

When a half-built project receives a full method wheel, the workflow can become larger than the project. The correct pattern is:

```text
project reality > method wheel
upstream control layer evolves separately
business repos keep only the smallest necessary pointer and adapter
lessons learned in projects flow back upstream
```

## What Belongs Upstream

Keep these in this AI workflow repository:

- Demand Control Plane module map.
- Demand-grilling / clarification protocol.
- Skill orchestration rules.
- External framework benchmarks.
- Reusable templates.
- Validation / quality-gate design.
- Method-harness repair lessons.
- Cross-project routing rules.

## What Belongs in a Business Repo

Only add project-local artifacts when they directly support the current work:

- A minimal pointer to the upstream method.
- A Project Continuation Brief or equivalent current-state map.
- A project-specific Demand Grilling Brief.
- Issue / Codex handoff for a bounded task.
- Local validators that protect project artifacts.
- Domain outputs: specs, research notes, samples, code, tests, ADRs.

Do not copy the whole method wheel into a business repo.

## External Benchmark Matrix

| Source | Type | What to absorb | Boundary |
|---|---|---|---|
| GitHub Spec Kit | Open-source SDD toolkit | `constitution → specify → clarify → plan → tasks → analyze → implement`; specs become executable | Best for software builds; too heavy to dump wholesale into every repo |
| Jama Software SDD | Requirements / traceability methodology | Spec as authoritative source; SDD as context engineering; traceability and compliance evidence | Regulated-engineering framing can be heavier than needed for small projects |
| JetBrains Junie spec-driven workflow | IDE agent practice | `requirements.md → plan.md → tasks.md`; persistent files guide agents | IDE-focused; not a whole cross-project control plane |
| GSD Core | Spec-driven multi-agent framework | Discuss → Plan → Execute → Verify → Ship; fresh context; `.planning/` artifacts | Strong reference for persistent state and verification |
| OpenSpec | Brownfield-friendly SDD framework | proposal / specs / design / tasks; spec delta review; persistent context | Good model for existing repos and iterative changes |
| Grill Me / Matt Pocock-derived skills | Plan interrogation skill | One question per turn; recommended answer; decision tree; inspect repo before asking | Strong front-gate lens, not a full workflow by itself |
| Mistral PRD-to-ticket workflow | Agentic PRD pipeline | transcript → PRD → development tickets → Linear/Jira | Needs owner review before tickets become execution truth |
| ProdMap / PRD-agent products | Productized context layer | Knowledge base + agent context + PRDs + compliance/architecture grounding | Product pages are market evidence, not proof of effectiveness |

## MQL5 / Domain Trial Field Note

MQL5 Chinese Articles and Forum are useful when the current trial field is trading strategy research:

- `https://www.mql5.com/zh/articles`
- `https://www.mql5.com/zh/forum`
- `https://www.mql5.com/zh/articles/8410`
- `https://www.mql5.com/zh/articles/16973`
- `https://www.mql5.com/zh/articles/13506`

Absorb these for domain constraints:

- simple systems beat complexity and overfitting;
- indicators are usually observer/assistant tools, not proof of edge;
- strategy claims need expected payoff, profit factor, drawdown, consecutive losses, long tests, and realistic costs;
- AI can augment an existing rule system but should not bypass risk, labeling, data, testing, and execution boundaries.

Evidence boundary:

```text
MQL5 sources can constrain a trading trial field.
They do not define the Demand Control Plane product boundary.
They do not prove a trading strategy works.
```

## Demand Control Plane Modules

The independent control plane should evolve around these modules:

1. **Constitution / Principles** — project-independent operating principles and hard boundaries.
2. **Discovery / Grill** — one-question-at-a-time interrogation, recommended answers, decision tree, repo inspection before asking.
3. **Clarify / Specify** — goal, users, non-goals, assumptions, risks, acceptance, verification.
4. **Plan / Tasks** — implementation or research plan with bounded vertical slices.
5. **Issue / Ticket** — GitHub / Linear / Jira conversion with traceable scope.
6. **Persistent Context** — file-backed state, not chat memory.
7. **Verify / Analyze** — consistency checks, tests, CI, artifact-consumer checks, false-success traps.
8. **Archive / Learnback** — project trial lessons update the upstream method harness.

## Routing Rule

When a project exposes a reusable method flaw:

```text
project-local artifact: minimal pointer + evidence of the trial
upstream AI workflow repo: method correction, template, benchmark, validator, or skill change
```

Do not bury reusable workflow corrections inside the business repo that happened to reveal them.
