# Self-Improving Skill Loop Template

Use this when a recurring agent Skill, port prompt, checker rubric, or workflow template should improve from real run feedback.

Professional framing:

```text
Inner loop applies the skill. Outer loop observes inner-loop outcomes and proposes reviewable skill improvements.
```

## 1. Inner Loop

Purpose: run the current skill on real work and record enough evidence for later improvement.

Required:

- Skill/template name:
- Skill version:
- Trigger: manual / GitHub issue / PR / schedule / webhook / message:
- Input source:
- Output artifact:
- Marker/comment/version field:
- Feedback channel: reactions / comments / label drift / review report / test report / owner decision:

Inner-loop rules:

- [ ] Include a version marker in outputs when possible.
- [ ] Record the exact skill/template version used.
- [ ] Record result, evidence, and feedback channel in runtime loop state.
- [ ] Do not self-edit the skill during the inner loop.

## 2. Feedback Signals

Classify feedback strength:

| Signal | Weight | Notes |
| --- | --- | --- |
| Maintainer/owner correction | Strong | Treat as high-quality but still contextual. |
| Checker/test/review failure | Strong | Must be reproducible or linked to evidence. |
| Explicit user comment | Strong/Moderate | Strong if specific, moderate if vague. |
| Reaction/downvote | Moderate | Useful but ambiguous without explanation. |
| Silence/no feedback | Weak positive | Never enough alone for a skill update. |

## 3. Outer Loop

Purpose: periodically review inner-loop runs and propose improvements only from generalizable lessons.

Outer-loop steps:

1. Collect recent runs for the skill/template.
2. Extract feedback signals and evidence.
3. Cluster repeated issues or corrections.
4. Convert only strong/repeated patterns into generalizable lessons.
5. Propose a diff to the skill/template or checker rubric.
6. Route diff through A/E protection gates.
7. Merge/promote only after review; otherwise keep as experiment/watch.

## 4. Generalizable Lesson Test

A lesson is valid only if it describes:

```text
When <category of case appears>, handle it as <policy>, because <evidence>.
```

Reject lessons that are only:

```text
Issue #123 was wrong.
One user disliked this.
The model felt uncertain.
A single ambiguous case happened once.
```

## 5. A/E Protection Gate

Before editing the skill/template baseline:

- [ ] Current baseline and rollback point identified.
- [ ] Feedback evidence is strong or repeated.
- [ ] Lesson is generalizable.
- [ ] Proposed change is a diff/PR, not silent mutation.
- [ ] Maker/checker separation remains intact.
- [ ] Owner approval requested for broad/risky principle changes.
- [ ] Same uncertainty repeated 3 times triggers owner brief, not auto-rewrite.

## 6. Output

```md
# Skill Improvement Proposal

- Skill/template:
- Current version:
- Proposed version:
- Evidence window:
- Feedback signals:
- Generalizable lessons:
- Proposed diff summary:
- Risk:
- Rollback:
- A-port decision: REJECT / WATCH / EXPERIMENT / PARTIAL_ACCEPT / ACCEPT / ESCALATE
- E-port verification:
```
