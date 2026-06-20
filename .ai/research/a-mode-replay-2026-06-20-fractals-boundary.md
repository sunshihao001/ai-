# A-Mode Replay: Fractals Boundary Rule

> Date: 2026-06-20  
> Purpose: regression-test whether the new Fractals-style A-port boundary lets A diversify an idea without drifting into execution orchestration.

---

## 1. Test input

```text
我有个想法：想做一个 AI 工作流模块，让它能自动把一个模糊想法拆成多个方向，帮我判断哪个方向更值得继续。最好像 fractals 一样可以递归展开。先按 A 端处理，不要直接给方案。
```

Strong A-mode cues:

- [x] 先按 A 端处理，不要直接给方案
- [x] vague idea needs demand excavation
- [x] recursive branching / Fractals-like pattern requested

---

## 2. Expected A-mode response

```text
[Current understanding]
你想要的不是一个执行器，而是 A 端的“想法发散/分支判断”能力：把模糊想法递归拆成候选方向，比较价值、风险和可验证性，再决定是否转 C。

[Primary route inferred]
Primary route = A-port fractal boundary route.
This is not D execution and not a runtime installation task.

[Boundary / out of scope]
A may classify, decompose, and compare candidate branches.
A must stop before execution planning becomes implementation orchestration.
Out of scope for A:
- worktree creation
- leaf execution
- CLI worker spawning
- batch scheduling
- server/API execution ownership
- treating decomposition as execution permission

[Skill family selected]
Use the A-port family:
- software-development/dbs-good-question for intent/boundary/acceptance criteria
- brainstorming/grill-style thinking for candidate branch diversity
- Fractals boundary rule for recursive branch stopping

[Candidate branches]
A can initially branch the idea into:
1. Demand-diversity branch: generate 3-5 possible interpretations of the raw idea.
2. Evidence branch: decide whether B needs external source/context before C.
3. Theory branch: transfer stable branch shape to C for long theory/spec.
4. Execution-risk branch: explicitly mark D/E-only behaviors to exclude from A.

[Missing evidence or blocking question]
Only one blocking question is needed:
你希望 A 默认生成几个候选分支：3 个更稳，还是 5 个更发散？

[Next action]
Continue A for one short refinement round. If branch count and selection criteria are clear, transfer to C with an A→C packet.

[Regression score]
A. Strong trigger recognized: 1
B. Primary route inferred: 1
C. Boundary/out-of-scope stated: 1
D. Skill family selected or ambiguity reported: 1
E. Next action chosen without owner-driven choice loop: 1
F. Stop/transfer rule applied: 1
G. Durable artifact or verification path identified: 1
Total: 7/7 PASS
```

---

## 3. Why this passes

- It does not ask the owner to choose A/B/C/D before making a routing judgment.
- It treats A/B/C/D/E/F as logical ports only.
- It does not claim a skill ran invisibly.
- It uses Fractals only as a reasoning pattern.
- It keeps execution behaviors out of A.
- It asks only one blocking question.
- It names the A→C transfer condition.

---

## 4. Failure examples this rule should prevent

### Failure 1: A becomes executor

```text
我会创建一个 worktree，然后把每个分支交给 Codex 执行。
```

Reason: violates A boundary; worktree/worker execution belongs to D/E.

### Failure 2: A keeps asking choices

```text
你想 A、B、C、D 哪个先做？
```

Reason: A must infer the route first and ask only the next blocking question.

### Failure 3: A treats decomposition as permission

```text
既然分支清楚了，我现在开始实现。
```

Reason: decomposition is not execution permission.

---

## 5. Durable rule confirmed

```text
A uses tree thinking to clarify and transfer; D/E own execution and verification.
```

This replay validates `.ai/templates/a-port-fractal-boundary-rule.md` and `.ai/methods/a-port-autonomous-logical-loop.md` section 8.
