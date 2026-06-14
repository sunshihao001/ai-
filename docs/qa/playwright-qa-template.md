# Playwright QA Template

Use this after implementation and before PR merge for product-facing changes.

## Scope

Feature/spec:
Issue/PR:
Environment:
Browser(s):

## Setup

```bash
# Adapt to the repo package manager and scripts from AGENTS.md
npm install
npx playwright install --with-deps
npm run test:e2e
```

## Critical path scenarios

- [ ] Happy path works from a clean state.
- [ ] Empty/loading/error states are visible and recoverable.
- [ ] Validation messages are understandable.
- [ ] Navigation/back/refresh behavior is correct.
- [ ] Mobile/small viewport behavior is acceptable.
- [ ] Screenshots or traces captured for failures.

## Suggested AI/Codex prompt

```text
Use Playwright to verify the user-facing behavior described in the spec and issue.
Do not only assert that elements exist; assert the user-visible outcome.
If a test fails, capture the trace/screenshot and diagnose before changing code.
```

## Evidence to paste into PR

```md
### Playwright QA
- Command:
- Browser:
- Result:
- Trace/screenshot:
- Notes:
```
