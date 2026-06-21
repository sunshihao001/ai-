# Synthesis — PR Watch Loop and Product Feedback Loop Patterns

## Sources

- `sources/2026-06-17-freeman1266-loop-engineering-pr-watch.md`
- `sources/2026-06-17-addy-osmani-loop-engineering.md`
- `sources/2026-06-17-pandatalk8-goal-loop-workflows.md`
- `sources/2026-06-17-yupi996-loop-engineering-ralph-overbaking.md`

## Synthesis claim

The freeman1266 / MacTalk material adds an important correction to the previous loop sources:

```text
Loop Engineering is not magic autonomy.
It is prompt logic + state + feedback + verification + exit conditions packaged into a repeatable control system.
```

This should prevent the method wheel from over-absorbing the hype version of Loop Engineering.

## Practical loop anatomy

A useful AI loop should include at least:

```text
1. Input / trigger
2. Goal / completion condition
3. State file / durable memory
4. Action policy
5. Feedback source
6. Verification mechanism
7. Exit condition
8. Escalation rule
9. Cost/budget limit
```

## PR Watch Loop pattern

Use this pattern when a PR needs ongoing CI/review maintenance:

```text
Trigger: every N minutes or after CI/review update.
State: .agent/pr-watch.md or equivalent.
Action: inspect CI, comments, conflicts; fix minimal cause in worktree.
Verification: targeted test/lint/build/Playwright.
Stop success: CI green, comments resolved, no conflict, final summary written.
Stop failure: same failure repeats 3 times, max rounds reached, or risk boundary crossed.
Escalate: owner/checker receives decision-ready brief.
```

## Product Feedback Loop pattern

Use this pattern when turning external/user feedback into one bounded product improvement:

```text
Trigger: daily or scheduled.
Sources: GitHub Issues, support logs, analytics, user feedback.
Classify: bug / UX issue / feature request.
Select: one high-frequency and verifiable issue.
Spec: mini spec with reproduction, expected behavior, acceptance criteria.
Execute: worktree implementation.
Verify: tests + Playwright / evidence.
Deliver: PR with why/what/verification/risk.
```

## Update to A/B/C/D/E/F model

| Port | Additional implication |
| --- | --- |
| A | Must define exit and escalation conditions before loop starts. |
| B | When sourcing external feedback, must classify and select one bounded issue rather than dumping many links. |
| C | Converts selected issue into mini spec or implementation plan. |
| D | Executes in isolated worktree / bounded path. |
| E | Owns CI/review/test evidence and repeated-failure detection. |
| F | Receives only decision-ready escalation, not raw loop noise. |

## Anti-hype guardrail

Do not write docs that imply:

```text
Loop replaces prompt engineering.
Loop means unattended programming.
Loop is just cron.
Loop is safe without external state and verification.
```

Instead, use:

```text
Loop productizes prompt/state/feedback/verification/exit into a repeatable control system.
```

## Candidate method updates

- Add PR Watch Loop as an example template under `.ai/templates/`.
- Add same-failure escalation rule to loop-run template.
- Add `/goal` vs `/loop` distinction to method wheel only as product-specific vocabulary, not universal command spec.
