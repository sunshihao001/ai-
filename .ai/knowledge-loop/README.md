# Knowledge Loop — Learning Articles and Knowledge Reserve

> Created: 2026-06-16T22:50:21  
> Purpose: keep learning articles and external knowledge as a continuous update loop, not a one-shot dump.

## Why this directory exists

This repository is the AI Method Wheel source repository. External articles, tweets, threads, repos, videos, and forum discussions should not be treated as temporary chat context or one-off notes.

They should enter a durable loop:

```text
Capture source
→ extract source note
→ evaluate fit to current knowledge frame
→ synthesize reusable concepts
→ decide accept/partial/reject
→ update method docs/templates/port contracts
→ record remaining gaps
→ schedule next search/learning loop
```

## Directory layout

```text
.ai/knowledge-loop/
  README.md                         # this protocol
  loop-state.yaml                   # current learning/update loop state
  index.md                          # human-readable knowledge reserve index
  inbox/                            # raw links or unprocessed article notes
  sources/                          # normalized source notes, one file per source
  synthesis/                        # cross-source synthesis notes
  frame-updates/                    # proposed or accepted updates to the method wheel
  decisions/                        # A-port absorption decisions
  templates/                        # reusable templates for future loops
```

## Core principle

```text
Knowledge is not a one-time extraction. Knowledge is a maintained reserve with versioned evidence, fit decisions, follow-up gaps, and verified baseline updates.
```

For A-mode evolution, every durable change should pass this shape:

```text
feedback/source/replay
→ evolution log
→ A absorption decision
→ B Source Pack if evidence is missing
→ C synthesis if a framework update is needed
→ D/E bounded repo update and verification
→ next gap in loop-state
```

Use `.ai/templates/a-mode-evolution-log.md` for owner corrections, replay lessons, skill-routing failures, and external knowledge candidates that may change the method wheel.

## Roles in the loop

### A-port: Knowledge Frame and Loop Control

A owns:

- the current Knowledge Frame;
- learning-loop goal and scope;
- what counts as useful evidence;
- absorption decisions;
- routing to B/C/D/E/F after learning.

A must prevent over-absorption and overbaking.

### B-port: Search Strategy and Source Pack

B owns:

- how to search;
- source coverage;
- evidence quality;
- concept matching;
- Source Pack and Knowledge Fit Report.

B must not dump raw links without fit analysis.

### C/D/E/F after learning

- C turns accepted concepts into theory/spec/workflow drafts.
- D lands accepted updates into repo docs/templates/skills.
- E verifies consistency, evidence, and no scope drift.
- F/Owner approves high-level direction or risky changes.

## Standard loop

```text
1. A creates Learning Goal + Initial Knowledge Frame Gap.
2. A asks B for Search Strategy Brief if more sources are needed.
3. B returns strategy; A approves/revises.
4. B collects sources and returns Source Pack + Knowledge Fit Report.
5. A creates Knowledge Absorption Decision.
6. Accepted concepts become frame-updates/ entries.
7. D/E land and verify repo changes if needed.
8. loop-state.yaml is updated with next gaps.
```

## Source quality levels

```text
S1: official docs / primary author / tool source code / reproducible repo
S2: expert article with concrete workflow or examples
S3: practitioner social thread with specific experience
S4: generic commentary / SEO summary / weak opinion
```

Only S1–S3 should normally influence the method wheel. S4 can be listed as context but should not drive framework changes.

## Absorption decisions

```text
ACCEPT          # directly update Knowledge Frame / method docs
PARTIAL_ACCEPT  # absorb a specific concept, keep caveats
REVISE_SEARCH   # source direction was useful but incomplete
REJECT          # do not absorb
ESCALATE        # ask Owner for direction
```

## When adding a new article/source

1. Put raw link or quick note in `inbox/` if not processed yet.
2. Create a normalized note in `sources/` using `templates/source-note.md`.
3. If multiple sources support a concept, create a synthesis note in `synthesis/`.
4. If the concept should alter the method wheel, create a proposed update in `frame-updates/`.
5. A records the decision in `decisions/`.
6. Update `index.md` and `loop-state.yaml`.

## Important anti-patterns

- Do not paste huge raw articles without extracting claims.
- Do not treat a viral thread as truth without evidence level.
- Do not update method docs just because a concept sounds fashionable.
- Do not keep knowledge only in chat history.
- Do not let B search endlessly without A gates.
- Do not let C/D rewrite framework docs without an A absorption decision.
