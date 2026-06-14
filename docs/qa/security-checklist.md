# Security Checklist

Use this for any change touching auth, data, external input, network calls, files, payments, secrets, or deployment.

## Data and permissions

- [ ] Authorization checks happen server-side where required.
- [ ] Users cannot access other users' data.
- [ ] Sensitive data is not logged.
- [ ] Secrets are not committed, printed, or exposed to client code.

## Input/output

- [ ] External input is validated and encoded.
- [ ] File paths/uploads are constrained.
- [ ] HTML/Markdown rendering is sanitized.
- [ ] Error messages do not leak internals.

## Dependencies and CI

- [ ] Dependency audit reviewed if dependencies changed.
- [ ] No unpinned or suspicious packages added without justification.
- [ ] CI/test commands from AGENTS.md were run.

## PR evidence

```md
### Security
- Risk area:
- Checks performed:
- Dependency changes:
- Remaining risk:
```
