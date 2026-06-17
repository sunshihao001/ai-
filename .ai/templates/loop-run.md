# Loop Run Template

Use this for any AI loop that may run more than one maker/checker iteration.

## 1. Trigger

- Manual / scheduled / GitHub issue / PR / CI failure / trace failure:
- Source URL or issue:
- Owner:

## 2. Goal

State the desired end state in checkable terms.

```text

```

## 3. Work Classification

- [ ] Autonomous
- [ ] Needs owner
- [ ] Ignored by owner

Reason:

```text

```

## 4. Durable State

Where progress is recorded:

- [ ] GitHub issue:
- [ ] PR:
- [ ] `specs/<feature>/`:
- [ ] ADR:
- [ ] QA checklist:
- [ ] other:

## 5. Maker

Who produces work:

```text
Codex / Claude / Hermes / human / other
```

Worker instruction:

```text
You are a repository worker. Do not create subworkers or delegate.
Work only on the assigned issue/spec.
Read AGENTS.md, CONTEXT.md, relevant specs, and QA checklist.
Produce PR-ready work with tests and verification evidence.
```

## 6. Checker

Who grades work separately from maker:

```text
review agent / CI / tests / Playwright / security audit / human
```

Checker rubric:

- [ ] Spec alignment
- [ ] Tests meaningful
- [ ] Lint/typecheck/build
- [ ] Playwright/E2E when relevant
- [ ] Accessibility when relevant
- [ ] Security when relevant
- [ ] No unnecessary scope expansion
- [ ] Diff is readable by human

## 7. Stop Conditions

Set before starting.

- Max maker/checker loops:
- Time cap:
- Token/cost cap:
- Success condition:
- Failure condition:

Example:

```text
Stop after 2 maker/checker loops.
Success requires tests + lint + typecheck + checklist + no major checker findings.
If still failing, stop and write a blocker brief.
```

## 8. Evidence Required

- [ ] Test output
- [ ] CI URL
- [ ] PR URL
- [ ] Screenshots/logs if UI/runtime
- [ ] Security/a11y notes if applicable
- [ ] Rollback plan

## 8.1 Knowledge-Update Protection Gate

Use this subsection when the loop absorbs an external article, X/Reddit thread, repo, video, or method source that may change the AI workflow.

- Current baseline / rollback point:
- Source quality: S1 / S2 / S3 / S4
- A-port decision: REJECT / WATCH / EXPERIMENT / PARTIAL_ACCEPT / ACCEPT / ESCALATE
- Proposed target: source note / synthesis / frame-update / template / method doc / skill
- E-port consistency result: pass / pass-with-caveat / block
- Promotion scope: additive candidate / narrow update / baseline change / owner approval required

Protection checks:

- [ ] Baseline is identified before update.
- [ ] Social-source caveats are preserved.
- [ ] Maker/checker separation remains intact.
- [ ] Stop conditions and escalation rules remain explicit.
- [ ] Owner boundary is not weakened.
- [ ] Change is rollbackable.

Repeated-uncertainty rule: if the same evidence gap or contradiction appears in 3 rounds, stop and produce an owner decision brief instead of rewriting the current frame.

## 9. Owner Decision Brief

Only fill this after autonomous work is complete or truly blocked.

```text
Decision needed:
Recommended default:
Alternatives:
Evidence:
Risk:
Rollback:
Exact action requested:
```

## 10. Harness Repair Notes

If the loop failed, record how to prevent recurrence.

```text
Failure:
Root cause in workflow:
Skill/template/checklist/CI change:
Regression test/check added:
```
