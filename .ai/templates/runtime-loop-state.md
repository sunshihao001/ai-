# Runtime Loop State Template

Borrowed from the useful parts of HarnessCode, adapted to the AI Method Wheel A/B/C/D/E/F model.

Use this directory shape for any long-running or multi-agent loop:

```text
.ai/loop-runs/<run-id>/
  state.yaml
  feature-list.json
  test-report.json
  review-report.json
  blockers.json
  owner-decisions.json
  cycle-log.md
  handoff.md
```

## Port mapping

| Runtime file | Owner port | Purpose |
| --- | --- | --- |
| `state.yaml` | A | Goal, scope, makers/checkers, stop conditions, route, baseline/rollback point |
| `feature-list.json` | A/D | Work items, dependencies, status, changed files |
| `test-report.json` | E | Test/lint/typecheck/build/Playwright results |
| `review-report.json` | E | Spec compliance, security/a11y/ops/diff review findings |
| `blockers.json` | A/F | Missing info and human-action blockers |
| `owner-decisions.json` | F | Decisions requested, recommended default, alternatives, final owner answer |
| `cycle-log.md` | A/E | Per-cycle agent, action, evidence, result, next route |
| `handoff.md` | A/D/E | Final summary for another agent/human to resume |

## state.yaml skeleton

```yaml
schema_version: 1
run_id: "YYYY-MM-DD-short-name"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
owner: "user"
classification: "Autonomous | Needs owner | Ignored by owner"

baseline:
  branch: ""
  commit: ""
  protected_files: []
  rollback_plan: ""

goal:
  raw_intent: ""
  operational_question: ""
  success_condition: ""
  non_goals: []

ports:
  A:
    role: "demand/control"
    output: "Demand-Control Brief"
  B:
    role: "source/evidence"
    output: "Source Pack / Knowledge Fit Report"
  C:
    role: "theory/spec"
    output: "Theory Package / Spec Draft"
  D:
    role: "repo landing/maker"
    output: "Diff / PR-ready changes"
  E:
    role: "verification/checker"
    output: "Test + Review Evidence"
  F:
    role: "owner decision"
    output: "Decision Brief Answer"

stop_conditions:
  max_loops: 3
  time_cap: ""
  cost_cap: ""
  success: ""
  failure: ""
  same_failure_rule: "Stop after same failure or uncertainty repeats 3 times."

current_route:
  next_port: ""
  reason: ""
  required_input: ""
  expected_output: ""
```

## feature-list.json skeleton

```json
{
  "features": [
    {
      "id": 1,
      "module": "",
      "description": "",
      "status": "pending",
      "dependencies": [],
      "acceptance_criteria": [],
      "changed_files": [],
      "maker": "D",
      "checker": "E"
    }
  ]
}
```

## blockers.json skeleton

```json
{
  "missing_items": [
    {
      "id": "",
      "desc": "",
      "action_type": "human_action | auto_action",
      "status": "pending | done | skip",
      "blocks_features": [],
      "owner_question": "",
      "recommended_default": ""
    }
  ]
}
```
