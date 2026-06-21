# 外部资料增强：自然语言表达层 / Natural Language Expression Layer

- 日期：2026-06-18
- 目的：围绕“Owner 用自然语言表达想法，A 口把它治理成专业任务合同”这个核心，再搜索外部资料，完善 A 口的自然语言表达层设计。
- 关联 PR：`docs: formalize A-port intent governance`

---

## 0. 总结论

前面我们已经把 A 口定义成：

```text
意图治理端 / Intent Governance Port
```

但还缺一层更底层的东西：

```text
自然语言表达层 / Natural Language Expression Layer
```

也就是：Owner 不是用工程语言、产品语言、需求规格语言来表达，而是用普通自然语言表达：

- 我觉得这个很重要
- 这个端还不够清楚
- 感觉后面理论生成不专业
- 这个 repo 里的技能能不能用
- 我想让它循环起来

A 口真正的第一层能力，是把这些自然语言表达变成专业结构。

所以 A 口应从：

```text
自然语言 → 意图治理 → 端口路由
```

进一步细化成：

```text
自然语言表达
  ↓
语义解析：用户到底在表达目标、问题、概念、情绪、判断、控制命令还是方案？
  ↓
术语治理：哪些词需要定义？哪些词是本项目共享语言？
  ↓
歧义消解：哪些地方模糊、可多解、不可验证？
  ↓
专业化改写：转成可验证、可路由、可授权的任务合同
  ↓
端口路由：B/C/D/E/F
```

---

## 1. 外部资料一：Controlled Natural Language / 受控自然语言

### 来源

- Veizaga et al. 2021：*On systematically building a controlled natural language for functional requirements*
- ACM 2026：*Controlled Natural Language for Requirements Specification: A Systematic Literature Review*

### 外部资料核心观点

自然语言在需求规格中非常普遍，因为它容易被人理解；但自由自然语言容易出现：

- vagueness 模糊
- ambiguity 歧义
- incompleteness 不完整
- poor testability 难测试
- wordiness 冗长
- under-specification 规格不足
- duplication 重复
- omission 遗漏

受控自然语言 CNL 的目标是：

```text
保留自然语言可读性
同时限制语法、词汇、结构
让需求更准确、完整、可处理、可验证
```

Rimay 案例显示，CNL 可以把大量自然语言需求转成更规范的需求表达，并且保持业务人员可理解。

### 对 A 口的增强

A 口不应该要求 Owner 一开始就说专业话。

但 A 口应该把 Owner 的自然语言逐步转成 **受控自然语言式任务表达**。

也就是：

```text
自由自然语言 Free NL
  ↓
受控自然语言 Controlled NL
  ↓
结构化任务合同 Structured Contract
```

### 可吸收规则

A 口输出的“专业化改写”应遵循固定句式：

```text
Given <当前状态/上下文>, for <用户/对象>, decide/change <具体对象>, while preserving <约束/非目标>. Success means <可观察完成标准>. Verify by <证据>. If blocked, ask Owner <一个具体问题>.
```

这就是你项目里的“受控自然语言”。

---

## 2. 外部资料二：自然语言到形式规格 / NL → Formal Specification

### 来源

- Emergent Mind：Natural-Language-to-Formal-Specification Mappings
- Böschen et al.：Bridging the Gap between Natural Language Requirements and Formal Specifications
- OpenReview：Formal Specifications from Natural Language

### 外部资料核心观点

自然语言到形式规格不是一步完成，而是多阶段管线：

```text
Natural Language
  ↓
NLP preprocessing
  ↓
Semantic / intermediate representation
  ↓
Formal abstraction / DSL / logic
  ↓
Validation / consistency checking
  ↓
Traceability
```

关键点：

- 先提取 subject / predicate / modifier / temporal / domain terms
- 再转成中间语义表示
- 再转成可验证形式
- 全程要保留 traceability
- 需要 human-in-the-loop correction

### 对 A 口的增强

A 口不一定要做数学形式化，但可以借鉴这个分层：

```text
用户原话
  ↓
自然语言语义槽位
  ↓
项目工作定义
  ↓
任务合同
  ↓
验证标准
  ↓
端口路由
```

### 可吸收规则

A 口要新增 **Natural Language Slot Extraction**：

```md
## Natural Language Slots
- Actor：谁在做 / 谁受影响？
- Intent：想达成什么？
- Object：对象是什么？
- Action：要判断、改变、生成、验证还是保存？
- Constraint：不能改变什么？必须保留什么？
- Evidence：什么能证明它对？
- Time / Stage：这是当前阶段、长期目标还是下一步？
- Risk：如果误解会造成什么后果？
```

这些槽位是 A 口从自然语言到任务合同的中间层。

---

## 3. 外部资料三：DDD Ubiquitous Language / 统一语言

### 来源

- Martin Fowler / Eric Evans：Ubiquitous Language
- NDepend：Checking DDD Ubiquitous Language
- Qlerify：What is Ubiquitous Language?

### 外部资料核心观点

DDD 的 Ubiquitous Language 强调：

- 开发者、业务专家、文档、代码使用同一套语言
- 语言不是一次性创建的，会随理解变化而演化
- 代码、文档、对话应该反映同一套领域概念
- 软件无法很好处理歧义，所以领域语言必须严谨
- 领域专家应该指出不适合表达业务理解的术语；开发者应该注意会绊倒设计的歧义和不一致

### 对 A 口的增强

你现在的问题非常接近 DDD 的“统一语言”问题。

你的 A 口应该维护一个项目语言层：

```text
Owner 原话词汇
  ↓
A 口工作定义
  ↓
B/C/D/E/F 统一使用
  ↓
写入文档/仓库/代码/提示词
```

例如：

- “需求拷问端”是否等于 “A 口”？
- “意图治理端”是否是正式术语？
- “loop agent”在本项目里是否包含 Owner 决策？
- “长理论专业”具体指什么？

这些不能每轮随便换词。

### 可吸收规则

A 口新增 **Project Language Ledger**：

```md
# Project Language Ledger

## Term
{术语}

## Owner Original Phrase
{用户原话}

## Working Definition
{本项目采用的定义}

## Bounded Context
在哪个端口/项目上下文有效

## Allowed Synonyms
可接受同义词

## Forbidden Confusions
不能混淆成什么

## Downstream Usage
B/C/D/E/F 怎么用这个词

## Status
candidate / accepted / revised / deprecated
```

---

## 4. 外部资料四：NLP Intent / Entity / Context / Session

### 来源

- Zendesk：NLP chatbots and AI agents
- PolyAI：How AI agents understand customer intent from queries
- 其他 NLP agent 资料

### 外部资料核心观点

NLP agent 理解用户输入时通常拆：

- Utterance：用户具体说法
- Intent：用户想达成的目的
- Entity：重要细节，如对象、时间、编号、地点
- Context：会话上下文参数
- Session：完整对话过程
- Confidence：是否足够确定
- Human handoff：不确定或高风险时交给人

PolyAI 还强调：好 agent 必须知道“自己不理解”，也就是低置信时要澄清或转人工。

### 对 A 口的增强

这可以变成 A 口自然语言表达层的基础结构：

```text
Utterance：保留 Owner 原话
Intent：识别 Owner 真正目的
Entities：提取关键对象/端口/仓库/技能/概念
Context：关联当前项目状态和历史文档
Session：记录本轮从原话到合同的转换
Confidence：判断能不能继续路由
Handoff：低置信或高风险时交 F 口/继续 A
```

### 可吸收规则

A 口每次自然语言处理都应有：

```md
## Natural Language Understanding
- Utterance：用户原话
- Intent：目标/问题/概念/控制/决策/执行/验证
- Entities：涉及对象、端口、repo、文件、技能、概念
- Context Used：本轮用了哪些上下文
- Confidence：high / medium / low
- Clarification Needed：yes / no
```

---

## 5. 自然语言表达层在 A-F 系统中的位置

新的整体结构应该是：

```text
L0 自然语言表达层
  - 用户原话
  - 意图识别
  - 实体/对象提取
  - 术语候选
  - 置信度
  - 歧义点

L1 A 口意图治理层
  - Goal Audit
  - Good Question
  - Concept Definition
  - Outcome/Opportunity/Solution/Experiment
  - Risk Tier
  - Context Budget

L2 B 口证据压缩层
  - Source Pack
  - Search Strategy Brief
  - 支持/反驳/修正

L3 C 口理论生成层
  - 基于 A+B 的长理论
  - 不泛写

L4 D 口执行层
  - 执行合同
  - 文件/代码/PR

L5 E 口验证层
  - 验证是否做对
  - 防假完成

L6 F 口授权层
  - ACCEPT / PARTIAL / REVISE / REJECT
```

这说明：自然语言表达层不是 A 口旁边的一个小功能，而是 A 口之前的入口层。

---

## 6. 对 A 口文档的具体升级建议

### 6.1 在 A 口正式定义前面加一节：L0 自然语言表达层

新增字段：

```md
## L0 Natural Language Expression Layer

A 口首先处理的是 Owner 的自然语言表达，而不是已经整理好的需求。

每次输入必须先抽取：
- Utterance
- Intent
- Entities
- Context Used
- Confidence
- Ambiguity
- Missing Slots
- Candidate Project Terms
```

### 6.2 在 A bot prompt 加“自然语言理解元数据”

每次输出开头先给：

```md
## Natural Language Understanding
- Utterance：...
- Intent：...
- Entities：...
- Context Used：...
- Confidence：high / medium / low
- Clarification Needed：yes / no
```

然后再给 A 口元数据。

### 6.3 新增 Project Language Ledger 文档

建议新增：

```text
.ai/methods/project-language-ledger.md
```

用来记录 A-F 方法轮里的核心术语：

- A 口
- 需求拷问端
- 意图治理端
- loop agent
- Source Pack
- C 口长理论
- Handoff Contract
- Blocker Brief
- Owner 判断卡

### 6.4 在 B 口 Source Pack 请求里加入语言字段

```md
## Language / Term Questions
- 哪些词需要外部定义？
- 哪些词是用户自造/项目内术语？
- 哪些词可能与外部资料含义冲突？
```

---

## 7. 对“你要做到的效果”的再升级表达

之前目标是：

> 意图 → 证据 → 理论 → 执行 → 验证 → 授权

加入自然语言表达层后，应该变成：

> **自然语言 → 共享语言 → 意图治理 → 证据压缩 → 理论生成 → 执行落地 → 验证审查 → Owner 授权。**

更完整表达：

> 我想建立一个能接住 Owner 普通自然语言表达的 A-F 项目运行系统。它首先保留原话、识别意图、抽取对象、发现歧义、沉淀项目统一语言；然后由 A 口把这些自然语言表达转成可验证、可路由、可授权的任务合同；再由 B 口补证据，C 口生成有根理论，D 口执行，E 口验证，F 口决策。这个系统的关键不是让 Owner 先说专业话，而是让系统有能力把普通话逐步治理成专业项目语言。

一句话：

> **我要做的是让普通自然语言成为项目循环的入口，而不是项目混乱的来源。**

---

## 8. 来源清单

- Veizaga et al. 2021 — *On systematically building a controlled natural language for functional requirements*
- ACM Computing Surveys 2026 — *Controlled Natural Language for Requirements Specification: A Systematic Literature Review*
- Emergent Mind — *Natural-Language-to-Formal-Specification Mappings*
- Böschen et al. — *Bridging the Gap between Natural Language Requirements and Formal Specifications*
- Martin Fowler / Eric Evans — DDD Ubiquitous Language
- NDepend — *Checking DDD Ubiquitous Language with NDepend*
- Qlerify — *What is Ubiquitous Language?*
- Zendesk — *What are NLP chatbots and how do they work?*
- PolyAI — *How do AI agents understand customer intent from queries?*
