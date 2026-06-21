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
  context-projection.md
  tool-policy.md
  command-router.md
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
| `context-projection.md` | A | What was selected for model-visible context and why |
| `tool-policy.md` | A/E/F | Tool/path/permission policy and sensitive-action approvals |
| `command-router.md` | A | Classification of user inputs, slash/local commands, diagnostics, and state queries |
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
  input_type: "ordinary_task | control_command | state_query | diagnostic | skill_invocation | owner_decision | knowledge_update"
  operational_question: ""
  success_condition: ""
  non_goals: []

truth_model:
  durable_log: "cycle-log.md / transcript / PR / issue"
  runtime_state: "state.yaml / repo / reports / owner decisions"
  model_visible_context: "context-projection.md"
  rule: "Transcript is evidence, runtime state is truth, context is projection."

harness_policy:
  command_router: "command-router.md"
  tool_policy: "tool-policy.md"
  markdown_context_rules:
    AGENTS: "workspace instruction context"
    SKILL: "task procedure context"
    specs: "bounded task context"
    logs: "projected evidence, not raw prompt dump"

environment:
  sandbox: "local | worktree | container | remote-vm | cloud-agent | none"
  allowed_paths: []
  forbidden_paths: []
  network_policy: "allowed | restricted | blocked | owner_approval_required"
  required_tools: []
  validation_commands: []

hooks_middleware:
  before_model: []
  before_tool: []
  after_tool: []
  after_model: []
  compaction: "manual | threshold | disabled"
  continuation: "manual | stop-hook | scheduled | disabled"
  false_completion_guard: true

context_rot_mitigation:
  large_output_policy: "preview + handle"
  compaction_threshold: ""
  progressive_disclosure: true
  stale_state_check: true

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

## context-projection.md skeleton

```md
# Context Projection

- Run ID:
- Projection time:
- Next action:

## Source of truth checked
- repo/file state:
- runtime state:
- GitHub issue/PR:
- reports:
- owner decisions:

## Included in model-visible context
- recent turns:
- selected files/docs:
- summaries:
- evidence previews:
- AGENTS/SKILL/spec context:

## Excluded or compacted
- large logs:
- stale transcript spans:
- old plans:
- irrelevant files:

## Handles to full artifacts
- logs:
- raw outputs:
- reports:
```

## command-router.md skeleton

```md
# Command Router

| Input | Classification | Route | Model prompt? | Notes |
| --- | --- | --- | --- | --- |
| `/status` | state_query | local runtime state | no | deterministic answer |
| `/audit` | diagnostic | local audit/check | no | do not ask model to guess |
| ordinary request | ordinary_task | A-port brief/model | yes | after context projection |
```

## tool-policy.md skeleton

```md
# Tool Policy

- Allowed paths:
- Forbidden paths:
- Sensitive tools/actions:
- Requires owner approval:
- Requires E-port review:
- Validation after side effect:
- Rollback path:
```
