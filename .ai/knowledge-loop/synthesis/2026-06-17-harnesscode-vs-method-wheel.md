# Synthesis — HarnessCode vs AI Method Wheel

## Sources

- `sources/2026-06-17-harnesscode-loop-system.md`
- `synthesis/2026-06-17-goal-loop-workflows-and-loop-engineering.md`
- `synthesis/2026-06-17-pr-watch-and-product-feedback-loop-patterns.md`
- `frame-updates/2026-06-17-protective-loop-engineering-update.md`

## High-level distinction

```text
HarnessCode = execution harness for long-running development loops
AI Method Wheel = control-plane + knowledge-frame + workflow design system
```

## What HarnessCode does well

- Central orchestrator decides next agent from runtime state.
- Requires structured PRD + tech specs before execution.
- Keeps progress in state files and logs.
- Separates coder/tester/fixer/reviewer roles.
- Refuses false completion when tests or reviews still fail.
- Supports backend swapping between OpenCode and Claude Code.

## How it differs from the user's method wheel

| Area | HarnessCode | User's method wheel |
| --- | --- | --- |
| Primary purpose | Run the development loop | Design the loop, knowledge frame, and decision gates |
| Top-level control | Central orchestrator | A-port demand/control + A↔B double gate + multi-port contract |
| Knowledge intake | PRD and tech spec files | External learning reserve, source notes, synthesis, frame updates |
| Roles | 5-agent loop | A/B/C/D/E/F ports with explicit boundaries |
| Verification | Tester + reviewer + false-completion guard | Separate checker/review/CI/QA/owner gates with broader scope |
| Update safety | Execution safety | Protective knowledge-update loop and baseline preservation |

## A-port view

HarnessCode is strong evidence that the user's A-port should keep demanding structured inputs before execution.

Questions A should ask when comparing or borrowing from HarnessCode:

- Is this a runtime harness or a method-level control plane?
- What problem does this solve that our current baseline does not?
- Does it strengthen or centralize control?
- Does it preserve our multi-port contract or collapse it?
- Which part can be borrowed without giving up our broader knowledge-loop design?

## Recommendation

PARTIAL_ACCEPT

Borrow these ideas:

- state-file-driven execution,
- PRD/spec gating,
- false-completion protection,
- explicit worker roles,
- backend abstraction.

Do not borrow wholesale:

- single central orchestrator as the only brain,
- five-role model as a replacement for A/B/C/D/E/F,
- unattended autonomy claims without the user's protective baseline gates.
