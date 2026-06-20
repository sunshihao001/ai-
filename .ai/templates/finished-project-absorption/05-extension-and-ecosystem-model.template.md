# {PROJECT_NAME} — Extension and Ecosystem Model

> B2 axis: integrations, plugins, presets, workflows, bundles, trust boundaries

---

## 1. Extension surfaces

| Surface | Mechanism | Install path | Trust boundary | Notes |
|---|---|---|---|---|
| `{SURFACE}` | `{MECHANISM}` | `{PATH}` | `{TRUST_BOUNDARY}` | `{NOTES}` |

## 2. Ecosystem catalog

| Item type | Examples | Discovery mechanism | Versioning |
|---|---|---|---|
| `{TYPE}` | `{EXAMPLES}` | `{DISCOVERY}` | `{VERSIONING}` |

## 3. Conflict resolution model

How does the project handle conflicts between defaults, presets, extensions, existing files, and user changes?

```text
{CONFLICT_MODEL}
```

## 4. Security and operational risks

- Global writes: `{GLOBAL_WRITES}`
- Profile/user-home writes: `{PROFILE_WRITES}`
- Network execution: `{NETWORK_EXECUTION}`
- Secrets/cookies/tokens: `{SECRET_TOUCHPOINTS}`
- Rollback quality: `{ROLLBACK_QUALITY}`

## 5. Method Wheel integration stance

```text
Do not install or promote ecosystem pieces until B2 + E + F have checked profile targeting, rollback, and command gating.
```

Candidate stance:

| Ecosystem part | Stance | Why |
|---|---|---|
| `{PART}` | ADOPT/BRIDGE/MERGE/PATTERN_ONLY/WATCH/REJECT | `{WHY}` |
