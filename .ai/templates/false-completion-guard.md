# False Completion Guard

Use this after any maker, coding agent, orchestrator, or loop claims `complete`, `done`, `all passing`, or `ready to merge`.

Principle:

```text
Agent says complete ≠ complete.
Complete means state + tests + review + scope + owner gates all pass.
```

## Required checks

Before accepting completion, E-port or the controlling A-port must verify:

- [ ] `feature-list.json` has no pending required feature.
- [ ] `test-report.json` is absent only if tests are explicitly not applicable; otherwise `overall=pass`.
- [ ] `review-report.json` is absent only if review is explicitly not applicable; otherwise `overall=pass`.
- [ ] `blockers.json` / `missing_info.json` has no pending `human_action` blocker.
- [ ] Git diff is inside allowed scope.
- [ ] No protected baseline file was changed without A/E approval.
- [ ] Maker and checker were not the same unchecked agent.
- [ ] Stop conditions were satisfied rather than bypassed.
- [ ] Rollback or recovery path is recorded.

## False-completion traps

Reject or downgrade completion if any of these occur:

```text
- The agent reports success but tests were not actually run.
- Some work items remain pending.
- A test/report file says fail but the agent says complete.
- Review findings remain pending.
- The diff contains opportunistic refactor outside scope.
- The loop changed core workflow/baseline files without a protection gate.
- The same failure/uncertainty repeated 3 times and the loop did not escalate.
```

## Output format

```md
# False Completion Check

- Run ID:
- Claimed complete by:
- Claim accepted? yes / no / accepted-with-caveat

## State checks
- feature list:
- test report:
- review report:
- blockers:
- git diff scope:
- baseline protection:

## Evidence

```text
<commands, report paths, CI links, log excerpts>
```

## Decision

- ACCEPT completion
- REJECT completion and route to D/E/F
- ESCALATE to owner

## Next route

- Port:
- Reason:
- Required action:
```
