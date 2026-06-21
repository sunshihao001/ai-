# E-Port Completeness Checklist: {PROJECT_NAME} B2 Pack

> Purpose: prevent shallow adoption of a mature external project.

---

## 1. Required B2 coverage

- [ ] Theory / doctrine is documented with source evidence.
- [ ] Code architecture names concrete entrypoints, modules, state/config flow.
- [ ] Source repo layout is separated from generated target-project scaffold.
- [ ] Command / artifact model lists reads, writes, source-of-truth status, and gates.
- [ ] Extension / ecosystem model covers integrations, presets/plugins/workflows, trust boundaries.
- [ ] Tests / release / packaging / operational safety evidence is recorded.
- [ ] Fit/non-fit table maps parts to A/B/B2/C/D/E/F/Harness/Skill insertion points.
- [ ] Risks, rollback boundaries, and forbidden shortcuts are explicit.
- [ ] Final decision uses `ADOPT`, `BRIDGE`, `MERGE`, `PATTERN_ONLY`, `WATCH`, or `REJECT AS BASELINE`.

## 2. Anti-shallow-adoption questions

1. Did we inspect code, not only README and marketing docs?
2. Did we distinguish project theory from implementation mechanics?
3. Did we distinguish source repo structure from generated scaffold?
4. Did we identify all profile/global writes before install or runtime use?
5. Did we avoid promoting external commands that bypass A/B/C/E/F gates?
6. Did we define objective verification before baseline changes?
7. Did we define rollback before adoption?

## 3. E verdict

```text
PASS / FAIL / PARTIAL — {REASON}
```

## 4. Required repair before A decision

- `{REPAIR_1}`
- `{REPAIR_2}`

## 5. Verification evidence

| Check | Command / file | Result |
|---|---|---|
| `{CHECK}` | `{COMMAND_OR_FILE}` | `{RESULT}` |
