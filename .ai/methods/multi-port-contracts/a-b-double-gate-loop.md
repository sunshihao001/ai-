# A↔B Double-Gate Loop — Knowledge Frame to Source Pack

> Purpose: make the A/B interaction AI-led without letting B become a blind search bot. A first creates a preliminary knowledge frame; B first designs the search/matching strategy; A approves or revises that strategy; only then does B execute research and return evidence for A to accept, reject, or route onward.

## One-line definition

```text
A creates and governs the Knowledge Frame; B designs and executes evidence discovery; A gates both the search strategy and the knowledge-frame absorption decision.
```

## Why this exists

A naive loop is:

```text
A has an idea → B searches → B returns links → A tries to use them.
```

That fails because B may search the wrong domains, collect noisy sources, or return evidence that is not aligned with the frame A is trying to build.

The corrected loop is:

```text
A idea → A Initial Knowledge Frame → B Search Strategy Brief → A strategy gate → B Source Pack + Knowledge Fit Report → A absorption gate → updated frame or next route.
```

This preserves the user's target: **AI leads execution while the human only steers broad direction and key decisions**.

## Roles

### A: Knowledge Frame and Loop Orchestration Control

A is not only a demand-grilling bot. In this loop A owns:

- preliminary idea/frame synthesis;
- missing-knowledge identification;
- B request generation;
- search-strategy approval;
- evidence-to-frame absorption decisions;
- loop state and next-route decisions.

A should maintain:

```text
Knowledge Frame
Loop State
Decision Log
Port Handoff Messages
```

### B: Search Strategy Analyst + Source Pack Executor

B has two stages:

```text
B1: Search Strategy Analyst
B2: Source Pack Executor
```

B must not jump directly to broad search when A is still clarifying the frame. B first returns a strategy that A can inspect.

## Double gates

### Gate 1 — Search Strategy Gate

A reviews whether B's proposed search strategy is aligned with the current knowledge frame.

A checks:

- Did B understand the frame and target?
- Are the proposed domains and keywords appropriate?
- Is the platform priority correct?
- Does B define evidence-fit criteria?
- Does B identify misleading or out-of-scope directions?
- Does the strategy support the larger loop-agent goal?

A decision options:

```text
APPROVE_SEARCH
REVISE_STRATEGY
REJECT_OR_REROUTE
ESCALATE_TO_OWNER
```

### Gate 2 — Knowledge Fit / Absorption Gate

After B executes research, A reviews whether the returned evidence should enter the knowledge frame.

A checks:

- Does the evidence fill a real frame gap?
- Is it a primary source, expert practice report, official documentation, or only noisy opinion?
- Does it add an actionable module, criterion, or workflow step?
- Does it create conflicts that need owner judgment?
- Does it move the system closer to AI-led cyclic agency?

A decision options:

```text
ACCEPT
PARTIAL_ACCEPT
REVISE_SEARCH
REJECT
ESCALATE_TO_OWNER
```

## State machine

```text
User broad direction
  ↓
A creates Initial Knowledge Frame v0.1
  ↓
A sends Search Strategy Request to B
  ↓
B returns Search Strategy Brief
  ↓
A Gate 1: approve/revise/reject strategy
  ├─ revise → B reworks strategy
  └─ approve → B executes search
        ↓
      B returns Source Pack + Knowledge Fit Report
        ↓
      A Gate 2: absorb/revise/reject evidence
        ├─ revise → B searches again with narrower scope
        ├─ partial accept → A updates frame and records gaps
        └─ accept → A updates Knowledge Frame v0.2
              ↓
            route to C theory/spec, D repo landing, E verification, or F owner
```

## A → B Search Strategy Request template

```md
# B Search Strategy Request

## From
A — Knowledge Frame and Loop Orchestration Control

## To
B — Source Pack / Search Strategy Analyst

## Loop ID
...

## Current Initial Knowledge Frame
...

## Goal
Improve this frame so it can support AI-led cyclic agency.

## Known gaps
1. ...
2. ...
3. ...

## Do not execute broad search yet
First return a Search Strategy Brief.

## Required output
1. Your understanding of the frame.
2. Recommended search domains.
3. Recommended keyword groups.
4. Platform priority: Twitter/X, Reddit, GitHub, blogs, papers, forums, video.
5. Evidence types to seek per platform.
6. Evidence-fit criteria.
7. Concepts likely to fill each frame gap.
8. Misleading / out-of-scope directions to avoid.
9. Tool/login readiness and blockers.
10. Exact next search plan if A approves.

## Return to A
A will approve, revise, or reject the strategy before execution.
```

## B → A Search Strategy Brief template

```md
# Search Strategy Brief

## 1. My understanding of A's Knowledge Frame
...

## 2. Frame gaps and needed evidence
| Gap | Evidence needed | Likely source |

## 3. Search directions
| Direction | Why search it | A module it supports |

## 4. Keyword groups
### Twitter/X
...
### Reddit
...
### GitHub
...
### Blog/Web
...
### Papers/Academic
...

## 5. Platform priority
| Platform | Priority | Evidence type | Risk |

## 6. Evidence-fit criteria
| Criterion | Explanation |

## 7. Directions not to absorb blindly
...

## 8. Execution plan if approved
- Round 1:
- Round 2:
- Round 3:

## 9. Questions for A
...
```

## B → A Source Pack + Knowledge Fit Report template

```md
# Source Pack + Knowledge Fit Report

## 1. Execution summary
...

## 2. Search coverage
| Platform | Query | Result count | High-value count | Problems |

## 3. High-value evidence
| Source | Link | Type | Core claim | Value for A | Evidence strength |

## 4. Fit to A Knowledge Frame
| A module | Supporting evidence | Suggested absorption | Risk |

## 5. New external concepts
| Concept | Source | Explanation | Absorb? |

## 6. Excluded / low-trust material
...

## 7. Recommended A-frame upgrades
...

## 8. Next search gaps
...

## 9. Raw result paths
...
```

## A Knowledge Frame Upgrade Decision template

```md
# Knowledge Frame Upgrade Decision

## Loop ID
...

## Input reviewed
- Search Strategy Brief:
- Source Pack:
- Raw results:

## Decision
ACCEPT / PARTIAL_ACCEPT / REVISE_SEARCH / REJECT / ESCALATE_TO_OWNER

## Absorbed concepts
...

## Rejected concepts and reasons
...

## Updated Knowledge Frame version
...

## Remaining gaps
...

## Next route
B补搜 / C理论生成 / D落库 / E验证 / F Owner
```

## Minimal viable implementation

Do not require full bot-to-bot automation first.

```text
v0.1: A writes handoff files; user moves them between bots.
v0.2: A can send messages to known B/C/D/E channels.
v0.3: A maintains loop_state.yaml in the repo.
v0.4: B returns structured Markdown/JSON for A to parse.
v1.0: A runs a semi-automatic, auditable, owner-gated loop.
```

## Design principle

```text
First strategy, then search.
First matching, then absorption.
A controls the frame; B supplies evidence.
AI leads the loop; the human steers broad direction and key decisions.
```
