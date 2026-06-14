# Project Onboarding Template

Use this template when connecting a real repository to the AI method wheel.

## Repository

- URL:
- Local path:
- Owner/team:
- Primary product/service:
- Deployment target:

## Stack reconnaissance

- Languages:
- Frameworks:
- Package manager:
- Runtime versions:
- Database:
- Queue/cache/search:
- External APIs:

## Directory map

```text
<fill after scanning repo>
```

## Command contract

Do not invent commands. Mark unknown items as `UNKNOWN`.

- Install dependencies:
- Run app locally:
- Unit tests:
- Integration tests:
- E2E/Playwright:
- Lint:
- Typecheck:
- Format:
- Build:
- Smoke check:
- Security audit:

## Existing CI/CD

- CI provider:
- Workflow files:
- Required checks:
- Deploy trigger:
- Rollback method:

## Existing docs

- README:
- Architecture docs:
- ADRs:
- Runbooks:
- API docs:
- Test docs:

## Risk map

### High-risk modules

- Auth:
- Payments/billing:
- Data migrations:
- Permissions:
- Secrets/config:
- Production deployment:

### Forbidden without explicit approval

- [ ] Reading/printing secrets.
- [ ] Changing production config.
- [ ] Destructive database migrations.
- [ ] Broad architecture rewrites.
- [ ] Auth/payment/security logic changes without review.

## Agent memory files to create/update

- [ ] `AGENTS.md`
- [ ] `CONTEXT.md`
- [ ] `docs/qa/checklist.md`
- [ ] `docs/adr/README.md`
- [ ] `specs/README.md`
- [ ] `.ai/templates/codex-issue-handoff.md`
- [ ] `.codex/skills/` if Codex skills are supported.

## First feature/bug candidate

- Title:
- User story:
- Business value:
- Non-goals:
- Acceptance criteria:
- Required tests:
- QA checks:
- Security/a11y considerations:

## Output

After onboarding, produce:

1. Files created/updated.
2. Commands discovered.
3. Unknowns requiring human answers.
4. Risk/forbidden-action summary.
5. Suggested first GitHub issue.
6. Codex handoff prompt for the first issue.
