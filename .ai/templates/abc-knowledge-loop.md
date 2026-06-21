# A/B/C Mutual Knowledge Loop Prompt

Use this when you want A, B, and C to form a **closed knowledge loop**:

- A does demand control and route judgment
- B compresses evidence and source context
- C synthesizes theory / plan / package
- the loop repeats until the idea is actionable

---

```text
你现在进入 A/B/C 互相驱动的知识循环。

目标不是只在 A 端拷问，而是让 A、B、C 形成一个闭环：
- A：负责目标、边界、非目标、约束、验收标准、转端判断
- B：负责证据、来源、上下文压缩、缺口标注、可引用材料
- C：负责理论综合、方案形状、可执行包、风险与验证设计

循环规则：

1. 先由 A 做 routing judgment，不要先让我选 A/B/C。
2. 如果缺证据，A 立刻转 B；如果证据足够但方案未成形，转 C；如果方案未成形但需要补证据，可 B↔C 往返。
3. A 负责判断是否继续循环；B 负责告诉我们还缺什么证据；C 负责告诉我们还缺什么结构。
4. 每轮只推进一个最关键缺口，避免一次性问太多。
5. 不要把普通 skill 仓库误判成 B2 成品项目；默认先按 skill 层或 pattern-only 处理。
6. 不要把工作流说明本身当成任务目标；先把初步想法压实到可执行。
7. 连续两轮没有新增有效信息，就停止并收束。
8. 2~3 轮后如果只是在改细节、不在改路线，就停止并给出转端建议。
9. 如果问题最终需要执行，转 D；需要验证，转 E；需要 owner 决策，转 F。

输出格式固定为：

[Current understanding]
[Primary route inferred]
[A: goal / boundary / stop rule]
[B: evidence / missing context]
[C: theory / plan / package]
[Confirmed]
[Still missing]
[Next best question]
[Next action]
[Stop or continue]
```

---

## Suggested response behavior

- A should ask the sharpest blocking question.
- B should only supply evidence or missing source context.
- C should only synthesize what A+B can already support.
- Do not keep the loop in A if B or C is the actual blocker.
- Do not keep the loop in B if the missing piece is actually a route decision.
- Do not keep the loop in C if the missing piece is evidence, not synthesis.

## Recommended use

Use this prompt for one chat / one run where you want the assistant to continuously move:

```text
A → B → C → A → ...
```

until the idea is mature enough to hand off to D/E/F or to stop.