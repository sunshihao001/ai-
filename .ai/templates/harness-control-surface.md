# Harness Control Surface and Context Projection

This template operationalizes the dongxi_nlp harness-series lesson:

```text
A transcript records what happened. Context decides what matters now.
Model can request. Harness decides.
Not every input is a prompt.
```

Use this template when designing or auditing a coding-agent workflow, multi-port loop, or long-running session.

## 1. Harness ownership checklist

The harness/control plane must own:

- [ ] live repo/workspace context;
- [ ] file-state baseline and freshness;
- [ ] prompt/context shape;
- [ ] tool-call validation and permission policy;
- [ ] output trimming/result previews;
- [ ] durable log and audit trail;
- [ ] runtime app state;
- [ ] context projection before model calls;
- [ ] slash/local command routing;
- [ ] delegation boundaries;
- [ ] sandbox/environment selection;
- [ ] hooks/middleware for compaction, continuation, lint/test checks, and false-completion guards;
- [ ] context-rot mitigation and progressive disclosure;
- [ ] human approval for sensitive actions.

## 2. Truth / transcript / context split

Do not conflate these:

| Layer | Meaning | Owner | Example |
| --- | --- | --- | --- |
| Durable log | What happened historically | Harness/GitHub/repo | transcript, cycle-log, tool logs |
| App/runtime state | What is true now | Harness/A-port | changed files, current goal, blockers, validation state |
| Model-visible context | What the model needs next | Harness projection | recent turns, summaries, selected evidence, AGENTS/SKILL context |

Rule:

```text
Transcript is evidence, not truth. Runtime state is truth. Model-visible context is a projection.
```

## 3. Input router

Before sending text to the model, classify input:

```text
ordinary user request → model prompt
control command → harness/local command
state query → deterministic runtime answer
diagnostics → local audit/doctor
skill invocation → load matching procedure context
owner decision → F-port decision record
```

Examples:

- `/goal`, `/status`, `/audit`, `/doctor`, `/skills`, `/compact` are not ordinary prompts.
- A typo in a command should route to command help, not become fuzzy model work.
- Diagnostics should inspect state, not ask the model to guess.

## 4. Markdown context routing

Markdown files must enter context by type, not by raw dumping.

| File type | Context layer | Loading behavior |
| --- | --- | --- |
| `AGENTS.md` | workspace instruction context | stable, scoped by repo/directory, loaded before work |
| `SKILL.md` | task procedure context | metadata visible first; body loaded only when skill applies |
| specs/plans/tasks | task/project context | loaded for bounded implementation/review |
| source notes/synthesis | knowledge-loop evidence | loaded by A/B/C when updating method frame |
| logs/transcripts | durable/audit context | summarized/projected, not blindly appended |

## 5. Context projection pipeline

Before each model call:

1. Start from durable log and runtime state.
2. Check context pressure and next action need.
3. Keep recent active turns verbatim when useful.
4. Convert large tool outputs to stable previews with handles to full artifacts.
5. Collapse completed old spans into explicit summaries.
6. Inject current app state: goal, changed files, blockers, validation, route, owner decisions.
7. Load only relevant AGENTS/SKILL/spec/source context.
8. Block or compact before context limit failure.
9. Preserve rollback/audit handles.

## 6. A-port integration

A-port should ask:

```text
Is this a user task, a runtime control request, a state query, a diagnostic, a skill invocation, or a knowledge-frame update?
```

A-port output should name:

- control surface involved;
- source of truth;
- model-visible projection;
- state files/artifacts to update;
- checker/verification evidence;
- stop/rollback rule.


## 7. Harness anatomy checklist

When auditing an agent system, check whether these harness pieces are explicit:

| Harness component | Questions |
| --- | --- |
| System prompts / instructions | Are stable rules separated from transient chat? |
| Tools / Skills / MCPs | Are tools described, scoped, and loaded only when useful? |
| Bundled infrastructure | What filesystem, sandbox, browser, git, package/runtime tools exist? |
| Orchestration logic | Who chooses subagents, handoffs, model routing, and command pattern? |
| Hooks / middleware | What runs before/after model calls and tool calls? |
| Context management | How does the harness prevent context rot and stale state? |
| Verification | Which deterministic checks, graders, tests, or review gates exist? |
| Continuation | How does long-horizon work resume without trusting stale transcript? |

## 8. Skill progression path

A repeated task should mature through this path:

```text
one-off prompt
→ reusable prompt skeleton
→ prompt library/template
→ API or batch loop
→ tool/MCP-connected workflow
→ SKILL.md with trigger, steps, checks, output shape
→ self-improving skill loop when feedback accumulates
```

Promotion rule:

```text
Do not promote a private prompt/template into a shared skill until A/E review confirms trigger conditions, verification, risk, and rollback.
```
