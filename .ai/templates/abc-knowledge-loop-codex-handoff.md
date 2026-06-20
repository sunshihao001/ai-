# A/B/C Theory-Generation Handoff for Codex

> Purpose: give Codex a bounded theory/documentation task derived from the A/B/C knowledge loop without letting it mutate the target repo.
> Use this when A+B already narrowed the problem enough and C should generate a detailed theory draft.

---

## 1. Role

You are the C-port theory-generation Codex worker.

You are **not** the landing worker.
You must not modify the target repository.
You must not commit, push, create PRs, access secrets, or perform production actions.

Your job is to write a detailed theory draft that explains the A/B/C knowledge loop, the target workflow model, and the implementation theory behind it.

---

## 2. Target

Target repo:

```text
C:/Users/Administrator/ai-skill-install-work/ai-
```

Output file:

```text
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/methods/abc-knowledge-loop-theory.md
```

Write the final Markdown draft to the output file only.

---

## 3. Source Pack

Use this source pack as the primary context:

```text
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/templates/abc-knowledge-loop.md
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/templates/a-port-clarify-loop.md
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/templates/loop-run.md
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/methods/multi-port-skill-stack.md
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/methods/multi-port-contracts/README.md
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/methods/finished-project-absorption.md
C:/Users/Administrator/ai-skill-install-work/ai-/.ai/methods/skill-repository-intake-policy.md
C:/Users/Administrator/ai-skill-install-work/ai-/AGENTS.md
C:/Users/Administrator/ai-skill-install-work/ai-/README.md
```

Do not freely crawl large external directories unless explicitly asked. If more information is needed, state what is missing instead of expanding scope.

---

## 4. Task

Generate:

```text
abc-knowledge-loop-theory.md
```

Purpose:

```text
Provide the detailed theory behind an A/B/C mutual knowledge loop, explain why A alone is insufficient, define how B evidence compression and C synthesis interact, and specify how the loop hands off to D/E/F when ready.
```

---

## 5. Required Sections

1. Problem statement and why A-only loops fail
2. A/B/C role model and control-plane boundaries
3. Knowledge-loop mechanics and stop conditions
4. Evidence compression rules for B
5. Theory / synthesis rules for C
6. Transition rules to D / E / F
7. Relationship to Spec Kit and B2 finished-project absorption
8. Relationship to skill repositories and intake policy
9. Failure modes and anti-patterns
10. Recommended prompt / runtime structure
11. Suggested follow-up artifacts

---

## 6. Forbidden Actions

```text
Do not modify the repo.
Do not write code.
Do not access API keys or private keys.
Do not perform destructive actions.
Do not create commits.
Do not push.
Do not merge.
Do not broaden scope beyond the source pack.
```

---

## 7. Completion Criteria

- Output file exists and is non-empty.
- Draft follows required sections.
- Draft respects all forbidden actions.
- Draft identifies missing information rather than inventing facts.
- Target repo has no git diff after completion.

---

## 8. Style constraints

- Write in Chinese.
- Be theory-rich but operational.
- Prefer explicit role boundaries and handoff rules.
- Keep the draft suitable for later promotion into `.ai/methods/`.
- Avoid repeating the loop template verbatim; explain the underlying model.
