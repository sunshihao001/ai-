# A-Mode Evolution Log Template

> Purpose: preserve A-mode drift, feedback, external knowledge, and skill-routing lessons as reviewable method-wheel evolution candidates.

---

## 1. Trigger / Signal

```text
<owner correction, failed response, external source, skill ambiguity, or replay result>
```

Signal type:

- [ ] A-mode drift / repeated choice loop
- [ ] Skill invocation ambiguity
- [ ] External knowledge candidate
- [ ] Source Pack / evidence gap
- [ ] Replay-first repair result
- [ ] Owner dissatisfaction route decision
- [ ] dbskill save / restore / report support case

---

## 2. Current baseline

Relevant files / skills / contracts:

- `.ai/methods/a-port-autonomous-logical-loop.md`
- `.ai/templates/a-mode-regression-test.md`
- `.ai/research/a-mode-replay-*.md`
- `.ai/knowledge-loop/*`
- relevant `SKILL.md` files

What the baseline currently says:

```text
<short baseline summary>
```

---

## 3. Candidate lesson

What should change?

```text
<new durable rule or concept>
```

Why is this not just a one-off chat preference?

```text
<reason>
```

---

## 4. Evidence and source quality

Evidence:

- Transcript / replay:
- Source Pack:
- External repo/article:
- Verification output:

Evidence level:

```text
S1 official/source code/reproducible repo
S2 expert workflow/example
S3 practitioner case
S4 weak/general commentary
SESSION replay/correction
```

---

## 5. Absorption decision

A-port decision:

```text
ACCEPT / PARTIAL_ACCEPT / WATCH / REVISE_SEARCH / REJECT / ESCALATE
```

Decision reason:

```text
<why>
```

Protected invariants:

- Logical ports by default; no physical bot split unless owner chooses.
- A-mode must infer route before asking another branch question.
- Skill ambiguity must be reported explicitly.
- B-source evidence precedes external skill adoption.
- D/E/F boundaries are not replaced by dbskill save/restore/report.

---

## 6. Landing plan

Target artifact:

- [ ] Method doc
- [ ] Template
- [ ] Port contract
- [ ] Skill reference
- [ ] Knowledge-loop source/synthesis/decision
- [ ] Validation script

Verification:

```bash
python scripts/validate-ai-method-wheel.py
```

---

## 7. Follow-up gaps

```text
<remaining questions or next learning loop>
```
