# {PROJECT_NAME} — Project Structure and Scaffold

> B2 axis: distinguish source repo layout from generated target-project layout

---

## 1. Source repository layout

```text
{SOURCE_REPO_TREE}
```

Key source folders:

| Path | Meaning |
|---|---|
| `{SOURCE_PATH}` | `{MEANING}` |

## 2. Generated target scaffold

If the tool initializes or modifies a target project, document what it creates.

```text
{GENERATED_TREE}
```

| Generated path | Created by | Source template | Source-of-truth? | Notes |
|---|---|---|---|---|
| `{GENERATED_PATH}` | `{COMMAND}` | `{TEMPLATE}` | yes/no/derived | `{NOTES}` |

## 3. Template copy / render model

- Template source: `{TEMPLATE_SOURCE}`
- Render variables: `{VARIABLES}`
- Conflict behavior: overwrite / merge / skip / prompt / unknown
- Idempotency: safe / unsafe / unknown

## 4. Scaffold lifecycle

```text
init
→ update
→ extend
→ remove / rollback
```

Current understanding:

- Init: `{INIT}`
- Update: `{UPDATE}`
- Extend: `{EXTEND}`
- Rollback: `{ROLLBACK}`

## 5. Method Wheel implication

What part of this scaffold should become a reusable pattern, template, or forbidden direct install?

```text
{IMPLICATION}
```
