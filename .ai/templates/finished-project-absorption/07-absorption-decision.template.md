# Absorption Decision: {PROJECT_NAME}

> Decision date: {DATE}  
> Based on B2 pack: `{B2_PACK_PATH}`  
> Decision owner: {OWNER}

---

## 1. Decision

Choose one or more:

```text
ADOPT / BRIDGE / MERGE / PATTERN_ONLY / WATCH / REJECT AS BASELINE
```

Decision:

```text
{DECISION}
```

## 2. Rationale

```text
{RATIONALE}
```

## 3. Accepted parts

| Part | Decision | Landing target | Verification |
|---|---|---|---|
| `{PART}` | `{DECISION}` | `{TARGET_FILE_OR_PORT}` | `{CHECK}` |

## 4. Rejected or deferred parts

| Part | Reason | Revisit condition |
|---|---|---|
| `{PART}` | `{REASON}` | `{CONDITION}` |

## 5. Required Method Wheel changes

- `{CHANGE_1}`
- `{CHANGE_2}`

## 6. Rollback boundary

If this decision causes drift or unsafe behavior, rollback by:

```text
{ROLLBACK_PLAN}
```

## 7. E/F gate status

- E completeness check: pass / fail / partial
- E verification command(s): `{COMMANDS}`
- F owner approval needed: yes / no
- F decision: pending / approved / rejected
