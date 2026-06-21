# A-Mode Replay — Complex Skill Routing / 2026-06-19

> Purpose: replay a real owner correction where A-mode drifted into choice-loop behavior, then define the expected A-mode response and score it with `.ai/templates/a-mode-regression-test.md`.

---

## 1. Compact transcript fragment

The owner gave a broad A/B/C/D/E/F method-wheel problem set and repeatedly corrected the assistant:

```text
Q1. 用户自然语言想法如何被 A端升级成专业研究问题？
Q2. B端应该如何把资料、外部文章、GitHub skill、上下文压缩成 Source Pack？
Q3. C端如何在研究态生成理论框架，又如何在执行态生成可落库方案？
Q4. 什么情况下 Owner 不满意应回 A、回 B、回 C，而不是直接进入 D？
Q5. 内部组合技能应如何分层、更新、桥接、合并、弃用？
Q6. 外部 GitHub skill 应如何判断 ADOPT / BRIDGE / MERGE / REJECT / PATTERN_ONLY？
Q7. dbskill 第二批状态链如何辅助 save / restore / report，而不替代 git、E端验证和 F端决策？

Owner signals:
- A first, but all are needed with priority.
- D / external GitHub skill evaluation is important but not the immediate main branch.
- Do not keep asking the owner to choose; automatically judge and loop until an initial target is reached.
- Do not split into physical multi-bot ports; A/B/C are logical ports.
- Focus now on A端技能之间的磨合 and correct skill invocation.
- Correct repository target is sunshihao001/ai-, not the meme project.
```

---

## 2. Strong trigger markers present

- [x] 请按 A 端强制触发模式处理
- [x] 请按 A 端逻辑处理
- [x] 先不要直接给方案
- [x] 自动拷问目标、边界、缺口、验收标准
- [x] 必要时自动调用相关 skill
- [x] Owner explicitly says not to split into physical bots
- [x] Owner complains that repeated choices are too human-driven

---

## 3. Expected A-mode response

### Current understanding

The owner is not asking for another abstract explanation of A/B/C/D. The owner is testing whether A-mode can autonomously route a complex method-wheel problem without handing every decision back to the owner.

The actual demand is:

```text
Make the AI Method Wheel’s A-port strong-trigger runtime reliable enough that broad natural-language workflow problems are converted into professional research/execution questions, routed through logical A/B/C stages, and recorded in the correct repo.
```

### Primary route inferred

Primary route:

```text
Continue A-mode, then transfer to B only for evidence/source-pack gaps, then C only for synthesis/package output.
```

Why:

- Q1 and repeated corrections are A-port runtime reliability issues.
- Q2/Q6/Trellis/fractals are B-port source/evidence candidates, but the owner explicitly deferred external repos.
- Q3 is C-port synthesis, but it should wait until A defines the route and B supplies evidence.
- Q4/Q5/Q7 are governance/routing rules that should be expressed as A-mode regression and method-wheel artifacts.

### Boundary / out of scope

In scope:

- Logical A/B/C loop behavior.
- A-mode anti-choice-loop behavior.
- Skill ambiguity reporting and explicit skill path selection.
- Correct repo placement in `sunshihao001/ai-`.
- Regression notes/templates that make future drift checkable.

Out of scope for this replay:

- Physical multi-bot split.
- Implementing Trellis or fractals.
- Turning external repos into adopted skills without B-source evaluation.
- D/Codex execution before A/B/C route maturity.
- Updating the meme project for method-wheel rules.

### Skill family selected

Minimal skill family:

```text
software-development/a-b-c-automatic-loop-control
+ software-development/dbs-good-question
+ superpowers/verification-before-completion
```

Reason:

- `a-b-c-automatic-loop-control` governs logical A/B/C loop and stop/transfer behavior.
- `software-development/dbs-good-question` converts vague demand into an agent-usable, verifiable routing contract.
- `verification-before-completion` requires evidence before claiming repo sync or validation success.

Runtime note:

```text
Bare dbs-good-question is ambiguous in this profile; use software-development/dbs-good-question for AI Method Wheel A-port work.
```

### Missing evidence or blocking question

No owner question is needed before the next action. The route is inferable.

Missing evidence class:

```text
A concrete replay artifact is needed to prove A-mode can pass its own regression rubric.
```

### Next action

Continue A-mode by creating a replay artifact, scoring the expected behavior, and updating the method-wheel repo if the replay reveals a rule gap.

Do not transfer to B yet; B is only needed after A asks for external source evaluation or GitHub skill classification.

---

## 4. Regression score for expected response

```text
A. Strong trigger recognized: 1
B. Primary route inferred: 1
C. Boundary/out-of-scope stated: 1
D. Skill family selected or ambiguity reported: 1
E. Next action chosen without owner-driven choice loop: 1
F. Stop/transfer rule applied: 1
G. Durable artifact or verification path identified: 1
```

Score:

```text
7/7 = pass
```

---

## 5. Regression lesson

A-mode should support a `replay-first repair` pattern:

```text
if owner says “继续打磨 / 可以” after an A-mode failure:
  1. do not ask a new broad choice question
  2. pick the most recent drift as the regression sample
  3. write a replay note or test artifact
  4. score the expected response
  5. patch the method/template only if a rule gap appears
  6. verify and commit the bounded repair
```

This converts subjective dissatisfaction into durable method-wheel improvement.

---

## 6. Candidate method patch

Add a short rule to `.ai/methods/a-port-autonomous-logical-loop.md`:

```text
When the owner says “继续打磨” or approves the previous repair direction after an A-mode drift, default to replay-first repair: use the last drift as a regression sample, score it, and only then patch method files. Do not ask for another broad branch choice unless the replay target is unknown.
```
