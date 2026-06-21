# {PROJECT_NAME} — Command and Artifact Model

> B2 axis: user-facing commands, artifact lifecycle, quality gates

---

## 1. Command inventory

| Command | Stage | Reads | Writes | Gate before | Gate after |
|---|---|---|---|---|---|
| `{COMMAND}` | `{STAGE}` | `{READS}` | `{WRITES}` | `{BEFORE}` | `{AFTER}` |

## 2. Artifact lifecycle

```text
{ARTIFACT_1}
→ {ARTIFACT_2}
→ {ARTIFACT_3}
```

| Artifact | Source of truth / derived | Owner | Update rule | Validation rule |
|---|---|---|---|---|
| `{ARTIFACT}` | `{TRUTH_STATUS}` | `{OWNER}` | `{UPDATE_RULE}` | `{VALIDATION}` |

## 3. Quality gates

| Gate | Checks | Blocks what? | Method Wheel mapping |
|---|---|---|---|
| `{GATE}` | `{CHECKS}` | `{BLOCKED_ACTION}` | `{PORT}` |

## 4. Error and ambiguity handling

- How unresolved questions are represented: `{UNRESOLVED_MARKER}`
- How inconsistencies are detected: `{INCONSISTENCY_MODEL}`
- How repair happens: `{REPAIR_MODEL}`

## 5. Command-to-Method-Wheel mapping

| Project command | Candidate mapping | Decision | Reason |
|---|---|---|---|
| `{COMMAND}` | A/B/B2/C/D/E/F/Harness | ADOPT/BRIDGE/MERGE/PATTERN_ONLY/WATCH/REJECT | `{REASON}` |
