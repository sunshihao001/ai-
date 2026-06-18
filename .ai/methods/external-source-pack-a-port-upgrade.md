# 外部资料增强：A 口意图治理认知升级 Source Pack

- 日期：2026-06-18
- 目的：根据“ A 口是项目意图治理基石”的认知，搜索外部资料，吸收能增强 A-F 工作流的概念、证据和设计原则。
- 结论：外部资料整体支持当前方向，并补强了 6 个关键概念：需求工程、产品发现、上下文工程、代理编排、Human-in-the-loop、Loop Control。

---

## 0. 总结论

外部资料证明：你今天形成的判断不是孤立想法，而是同时落在几个成熟领域的交叉点上：

```text
需求工程 Requirements Engineering
+ 产品发现 Product Discovery
+ 上下文工程 Context Engineering
+ Agent 编排 Orchestration
+ Human-in-the-loop 审批治理
+ Loop Control / Handoff / Termination
= A 口意图治理端
```

这说明 A 口不应该被理解成“问问题 prompt”，而应该被理解成一个 **前置治理层 / control plane**：

- 它像需求工程一样识别业务需要、范围、假设、风险。
- 它像产品发现一样防止团队直接跳方案，先找 outcome / opportunity / experiment。
- 它像上下文工程一样决定什么信息进入模型、什么压缩、什么丢弃。
- 它像 agent 编排一样决定状态、路由、权限、预算、停止条件。
- 它像 HITL 审批一样决定哪些动作可自动做，哪些必须人批准。
- 它像 loop control 一样防止循环提前结束、无限循环或错误放大。

所以可以把 A 口再升级为：

> **Intent Governance + Context Control + Routing Policy + Human Approval Gate**

中文：

> **意图治理 + 上下文控制 + 路由策略 + 人类授权门。**

---

## 1. 外部资料一：需求工程 / Requirements Elicitation

### 来源

- Jama Software: *A Guide to Requirements Elicitation for Product Teams*
- 搜索主题：requirements elicitation, requirements engineering, assumptions, risks, stakeholder needs

### 外部资料核心观点

需求引出不是简单“问用户要什么”。它是通过与关键利益相关者沟通协作，识别：

- business need
- scope
- assumptions
- risks
- stakeholder expectations
- functional / non-functional requirements

资料强调：需求没引出清楚，会导致：

- 返工成本上升
- 用户拿不到真正需要的东西
- 项目失败概率上升
- 错误假设驱动开发

### 对 A 口的增强

这直接支持 A 口的职责：

```text
A 口不是问答，而是需求工程的前置门。
```

A 口应该借鉴需求工程，新增/强化以下字段：

- stakeholder / Owner / affected parties
- business need / project need
- scope / non-goals
- assumptions
- risks
- requirements type
- validation evidence

### 应吸收进 A 口的规则

A 口 Demand Grilling Brief 应明确区分：

```text
用户说想要的东西 ≠ 真正业务需要
方案想法 ≠ 需求
需求 ≠ 可执行任务
可执行任务 ≠ 已授权任务
```

---

## 2. 外部资料二：产品发现 / Opportunity Solution Tree

### 来源

- Product School: *Opportunity Solution Trees for Enhanced Product Discovery*
- Teresa Torres / Continuous Discovery Habits 相关资料

### 外部资料核心观点

Opportunity Solution Tree 把产品发现拆成：

```text
Outcome → Opportunities → Solutions → Experiments
```

核心思想：

- 不要直接跳 solution。
- 先明确 outcome。
- 再探索 opportunity / problem space。
- 再生成 solution。
- 最后用 experiment 验证。

资料强调：团队应该关注 outcome，不只是 output。不是“做了功能”，而是“功能是否带来用户/业务结果”。

### 对 A 口的增强

这和你的 A-F 工作流完全对齐：

```text
A 口：Outcome / Problem framing
B 口：Opportunity evidence / source pack
C 口：Solution theory / strategy
D 口：Build / execute
E 口：Experiment / verification
F 口：Decision / adoption
```

### 应吸收进 A 口的规则

A 口遇到“我要做 X”时，不应该直接把 X 当任务，而要问：

```text
X 是 outcome、opportunity、solution，还是 experiment？
```

这能防止：

- 把手段当目标
- 把方案当需求
- 把输出当成果
- 把执行当发现

---

## 3. 外部资料三：上下文工程 / Context Engineering

### 来源

- Machine Learning Mastery: *Effective Context Engineering for AI Agents*
- 搜索主题：context engineering for AI agents, context window, static/dynamic context, retrieval budget

### 外部资料核心观点

AI agent 失败往往不是模型不够强，而是上下文管理失败：

- stale history 太多
- raw tool output 太多
- redundant retrieval 太多
- 关键信号被埋没
- 上下文窗口被当成无限记忆

Context Engineering 关注：

- 什么进入上下文
- 什么压缩
- 什么按需检索
- 什么丢弃
- 静态上下文和动态上下文如何分离
- token 的 financial cost 和 cognitive cost

### 对 A 口的增强

这证明 A 口不仅是“理解用户”，还是 **上下文入口控制器**。

A 口必须决定：

```text
哪些 Owner 原话必须保留？
哪些历史状态必须压缩？
哪些资料交给 B 口检索？
哪些内容不应该传给 C/D，避免污染上下文？
哪些是当前任务必须看到的高信号 context？
```

### 应吸收进 A 口的规则

A 口生成下游任务书时，必须做 **Context Budgeting**：

- Required Context：必须传
- Optional Context：可传
- Excluded Context：禁止传
- Retrieve Later：需要时再让 B 查
- Durable State：保存到文件/仓库，不塞进 prompt

这会显著提高 C 口长理论和 D 口执行的质量。

---

## 4. 外部资料四：Agent 编排 / Production Orchestration

### 来源

- HatchWorks: *Orchestrating AI Agents in Production: The Patterns That Actually Work*

### 外部资料核心观点

生产级 agent 不是“一个大 prompt”，而是需要编排层：

- deterministic orchestration
- supervisor + specialists
- Plan → Validate → Execute
- tools as contracts
- observability first
- continuous evaluation
- human-in-the-loop as product surface

关键句：

```text
Agents decide. Orchestrators coordinate. Tools execute.
```

以及：

```text
Make orchestration deterministic; keep judgment in the agent.
```

### 对 A 口的增强

这直接支持你的 A-F 分工：

```text
A 口不是大 prompt，而是 orchestrator/control plane 的入口部分。
B/C/D/E 是 specialists。
F 是 human decision gate。
```

A 口不能自己变成万能 agent，而应该输出合同，让 specialist 端口执行。

### 应吸收进 A 口的规则

A 口应采用两阶段或三阶段：

```text
Plan → Validate → Execute
```

映射到你的系统：

```text
A：Plan / Contract
E/F：Validate / Approve
D：Execute
```

高风险任务必须先 validate/approve，再 execute。

---

## 5. 外部资料五：Human-in-the-loop / 审批治理

### 来源

- Agent Native: *Human-in-the-Loop Approval Flow Pattern for AI Agents*
- Mindra / Airia 等 HITL 相关文章

### 外部资料核心观点

高影响动作不能和低风险读取走同一执行路径。

HITL 模式强调：

- intent classifier
- policy engine
- confidence threshold
- durable approval queue
- exact payload
- operator review surface
- immutable audit trail
- approve / reject / edit

适用场景：

- purchase
- external messages
- database mutations
- code deployments
- Create / Update / Delete actions
- low confidence actions
- high-risk categories

### 对 A 口的增强

这强化了 F 口与 A 口的关系。

A 口必须识别：

```text
这个动作是 read-only，还是 CUD？
这个动作可逆吗？
风险等级是多少？
信心是否足够？
是否需要 Owner 审批？
审批内容是否锁定？
执行后是否有审计记录？
```

### 应吸收进 A 口的规则

A 口路由时新增风险分类：

- R0：只读、低风险，可自动处理
- R1：生成草案，可自动处理但需标注假设
- R2：写入本地文件，需要验证
- R3：提交 Git / PR，需要明确范围和 diff
- R4：外部发布、删除、部署、花钱、敏感数据，需要 F 口批准

这会让“Owner 决策卡”更有工程意义。

---

## 6. 外部资料六：Agent handoff / loop control / termination

### 来源

- Antigravity Lab: *AI Agent Orchestration Design Patterns — Task Decomposition, Handoffs, and Loop Control*

### 外部资料核心观点

agent 设计的难点不只是 prompt，而是：

- 怎么拆任务
- 什么上下文交给 sub-agent
- 什么不交给 sub-agent
- 怎么设计 handoff
- 怎么设计 loop termination

强 handoff 应包含：

- Goal
- Current known state
- Completion criteria
- Failure policy

资料还指出：最危险的 loop 失败不一定是无限循环，而是 **premature termination**：任务没完成却提前结束。

### 对 A 口的增强

这直接强化你的端口合同设计。

A 口给 B/C/D/E 的任务，必须包含：

- Mission / Goal
- Known State
- Completion Criteria
- Failure Policy
- Stop and Return Conditions

### 应吸收进 A 口的规则

A 口输出任何下游合同，都必须加：

```text
如果无法完成，不要硬做；返回 Blocker Brief。
```

Blocker Brief 包含：

- 卡在哪里
- 已尝试什么
- 缺什么信息/权限/证据
- 建议回 A/B/C/D/E/F 哪个口

---

## 7. 外部认知对当前 A 口定义的修正建议

基于外部资料，当前 A 口文档可以继续升级 7 个点。

### 7.1 加入 Outcome / Opportunity / Solution / Experiment 分类

新增 A 口判断：

```text
用户说的 X 是 outcome、opportunity、solution，还是 experiment？
```

价值：防止把方案当目标。

### 7.2 加入 Context Budgeting

新增字段：

```text
Required Context
Optional Context
Excluded Context
Retrieve Later
Durable State
```

价值：防止 C/D 被上下文污染。

### 7.3 加入 Risk Tier / Action Type

新增字段：

```text
Action Type: read / generate / write / commit / publish / deploy / delete
Risk Tier: R0-R4
Approval Required: yes/no
```

价值：支撑 F 口审批和 HITL。

### 7.4 加入 Plan → Validate → Execute

新增规则：

```text
高风险任务必须先计划，再验证/批准，再执行。
```

价值：防止 D 口过早落地。

### 7.5 加入 Handoff Contract 固定字段

所有端口任务都必须有：

```text
Goal
Known State
Completion Criteria
Failure Policy
Return Format
```

价值：降低端口之间的解释漂移。

### 7.6 加入 Blocker Brief

当 B/C/D/E 无法继续时，必须回传：

```text
Blocker
Tried
Missing
Risk
Suggested Route
```

价值：防止 agent 假完成。

### 7.7 加入 Premature Termination 检查

E 口要检查：

```text
是否只是看起来完成？
是否满足原始目标？
是否满足 completion criteria？
是否有真实证据？
```

价值：防止 loop 提前结束。

---

## 8. 对“你想做到什么效果”的进一步提升版表达

结合外部资料，你的目标可以升级成：

> 我想建立一个以 A 口意图治理为控制面、以 B 口证据压缩为上下文工程、以 C 口理论生成为方案层、以 D 口执行为落地层、以 E 口验证为质量门、以 F 口判断为 HITL 审批层的多端口项目运行系统。它能够把 Owner 的自然语言想法转化为 outcome / opportunity / solution / experiment 清晰分层的任务链，并通过上下文预算、风险分级、端口合同、停止条件和审计记录，支撑普通项目推进和 loop agent 自动化，而不是让 AI 在模糊意图上自行扩大混乱。

一句话：

> **我要做的是一个“意图 → 证据 → 理论 → 执行 → 验证 → 授权”的项目治理循环，而不是一个会写长回答的 AI。**

---

## 9. 建议下一步

下一步不是继续泛搜，而是把这些外部概念吸收到现有 PR 文档里：

1. 更新 `a-port-intent-governance.md`
   - 加 Outcome/Opportunity/Solution/Experiment
   - 加 Context Budgeting
   - 加 Risk Tier
   - 加 Handoff Contract
   - 加 Blocker Brief

2. 更新 `a-bot-system-prompt.md`
   - 让 A bot 每次输出都带“动作类型 + 风险等级 + 是否需要 F 口批准”
   - 让 A bot 识别 outcome/solution 混淆

3. 更新 `b-port-source-pack-request-standard.md`
   - 加入 context budget 和 source confidence

4. 新增 `external-source-pack-a-port-upgrade.md`
   - 保存本文件作为外部认知依据

5. 再跑 5 个样本验证
   - 看新增字段是否真的提高判断质量，而不是让 A 口变复杂。

---

## 10. 来源清单

- Jama Software — A Guide to Requirements Elicitation for Product Teams
- Product School — Opportunity Solution Trees for Enhanced Product Discovery
- Machine Learning Mastery — Effective Context Engineering for AI Agents
- HatchWorks — Orchestrating AI Agents in Production: The Patterns That Actually Work
- Agent Native — Human-in-the-Loop Approval Flow Pattern for AI Agents
- Antigravity Lab — AI Agent Orchestration Design Patterns: Task Decomposition, Handoffs, and Loop Control
