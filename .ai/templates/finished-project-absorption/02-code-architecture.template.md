# {PROJECT_NAME} — Code Architecture

> B2 axis: executable implementation / module model / state flow

---

## 1. Executable entrypoints

| Entrypoint | Path | Purpose | Invocation |
|---|---|---|---|
| `{ENTRYPOINT}` | `{PATH}` | `{PURPOSE}` | `{COMMAND}` |

## 2. Main modules

| Module / file | Role | Reads | Writes | Notes |
|---|---|---|---|---|
| `{MODULE}` | `{ROLE}` | `{READS}` | `{WRITES}` | `{NOTES}` |

## 3. Core data flow

```text
{INPUT}
→ {MODULE_OR_STEP_1}
→ {MODULE_OR_STEP_2}
→ {OUTPUT_ARTIFACTS}
```

## 4. Configuration and state

| State/config file | Owner | Lifecycle | Risk |
|---|---|---|---|
| `{FILE}` | `{OWNER}` | `{CREATE_UPDATE_DELETE}` | `{RISK}` |

## 5. Install / update / uninstall behavior

- Install path: `{INSTALL_BEHAVIOR}`
- Update path: `{UPDATE_BEHAVIOR}`
- Uninstall / rollback path: `{ROLLBACK_BEHAVIOR}`
- Profile/global writes: `{PROFILE_OR_GLOBAL_WRITES}`

## 6. Tests and release evidence

| Evidence | Path / command | Result / meaning |
|---|---|---|
| `{TEST}` | `{PATH_OR_COMMAND}` | `{RESULT}` |

## 7. Architecture risks

- `{RISK_1}`
- `{RISK_2}`
