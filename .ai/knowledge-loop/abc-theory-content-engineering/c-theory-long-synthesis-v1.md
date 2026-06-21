# A/B/C 知识循环体系结构｜C端长理论梳理 v1

## 0. 本轮边界

本轮只整理“知识循环体系结构”层。

这不是执行系统设计，也不是新的工作流底座。它的任务是把 A端、B端、C端相关的理论、半成品想法、命令映射、递归工作流参考，统一放入一个可长期维护的内容工程结构中。

本轮明确不做：

- 不做直接代码实现。
- 不做 D/E/F 的完整执行系统设计。
- 不把 Fractals、dbskill、Spec Kit 当成新底座。
- 不发明一套平行于 AI Method Wheel 的新工作流。
- 不臆造 X 文章正文，只使用已验证可见摘要。

本轮可以做：

- 明确 A端、B端、C端各自的理论位置。
- 明确 A → B → C 作为常见知识循环。
- 把 dbskill、Fractals、Spec Kit 放到桥接位置，而不是替代底座。
- 给散乱理论建立 L0-L5 成熟度分级。
- 给后续内容工程提供文件结构和下一轮 C端提示词。

当前可见外部文章边界：

- 链接：`https://x.com/dontbesilent/status/2061724612753555590?s=20`
- 已验证可见标题方向：`2 天，2 亿 token，dontbesilent 内容资产工程系统｜已免费开源`
- 已验证可见摘要方向：把本地大量内容资产搭成可以继续运行的“内容结构化系统”
- 状态：`needs_full_text`
- 限制：不能根据标题和摘要推断正文细节。

## 1. 总结论

A/B/C 知识循环体系的核心不是“多几个机器人”，而是把一个模糊想法变成可积累、可检索、可审查、可继续推进的知识资产。

最小闭环是：

```text
A端接住想法
→ A端澄清目标、边界、非目标
→ B端补证据、对标、资料压缩
→ C端做理论合成、结构化、分级
→ 回到 A端决定吸收、重搜、继续写、落库或暂缓
```

其中 A端是 dominant front door。用户最常接触 A端，因为用户通常只想输入关键想法，不想自己完成资料研究、理论梳理、内容结构化和后续推进。

A端不是简单聊天入口，而是“意图到规格”的控制闸门。它决定这个想法是否成立、边界在哪里、应该交给 B 搜证据，还是交给 C 做理论合成。

B端不是泛搜索工具，而是 source pack 层。它根据 A端给出的框架去找证据、做对标、压缩上下文，并标注可信度、缺口和不应吸收的材料。

C端不是资料抓取端，也不是落库端。它负责把 A/B 产物合成理论包，把散的概念变成结构，把半成熟观点分级，把下一步问题交回 A端或交给后续端口。

因此，A → B → C 是常见理论循环：

- A 决定“这个问题是什么”。
- B 回答“它基于什么资料和证据”。
- C 生成“它可以被怎样理解、组织和复用”。

## 2. A端理论

A端定位：主入口 / Intent-to-Spec Control Gate / Demand-Control Plane。

A端的核心问题是：用户这句话到底要变成什么？

A端要保护用户原始意图，同时防止 AI 从一句模糊话直接跳到执行。A端先做需求拷问、目标审计、概念拆解、边界确认，再决定是否进入 B/C/D/E/F。

### A端核心职责

- 接住自然语言想法。
- 保留原始意图，不提前替用户换题。
- 澄清目标、边界、非目标。
- 判断当前缺的是问题定义、资料证据、理论合成、落库执行、验证审查，还是 owner 决策。
- 优先路由现成 skill 和 repo 约定，避免 AI 自己造轮子。
- 输出可承接文件，如 `raw-ideas.md`、`good-question.md`、`goal-audit.md`、`concept-deconstruction.md`、`boundary.md`。

### A端理论条目

| 理论 | 端口 | 成熟度 | 状态 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| A端是 dominant front door | A | L4 | 已确立 | `00_intent/boundary.md` | 写入 A端总原则 |
| A端是 Intent-to-Spec Control Gate | A | L3 | 已确立 | `00_intent/good-question.md` | 固化为问题说明模板 |
| A端负责保留原始意图 | A | L2 | 可用 | `00_intent/raw-ideas.md` | 建立原始想法记录格式 |
| A端先路由现成 skill | A | L3 | 已确立 | `30_command_mapping/skill-router-matrix.md` | 建立命令到端口映射表 |
| A端控制知识框架吸收 | A | L4 | 已确立 | `40_review/decision-notes.md` | 建立 ACCEPT / PARTIAL_ACCEPT / REJECT 决策记录 |
| A端防止 B 泛搜索 | A/B | L4 | 已确立 | `10_b_port/search-strategy.md` | 使用 A↔B 双闸门 |
| A端防止 C 硬写理论 | A/C | L3 | 可用 | `40_review/maturity-check.md` | C端输入不足时退回 A/B |

### A端对非专业用户的意义

用户不需要一开始就会写 spec、issue、prompt、source pack。用户只需要把想法说出来。A端负责把“我想做这个”变成“这个任务的目标、边界、证据需求、下一步端口是什么”。

## 3. B端理论

B端定位：证据 / 对标 / source pack 层。

B端的核心问题是：这个理论或判断基于什么？

B端不是搜索越多越好。B端要根据 A端给出的知识框架和缺口，先设计搜索策略，再执行资料收集和压缩。B端产物应该让 C端不需要翻大量原始材料，就能开始做理论合成。

### B端核心职责

- 根据 A端问题框架补证据。
- 先返回 Search Strategy Brief，必要时等待 A端批准。
- 做 source pack、benchmark notes、evidence log、rejected sources。
- 标注资料可信度、覆盖范围、冲突和缺口。
- 压缩材料给 C端，而不是把原始资料堆给 C端。
- 标出低信任、不可吸收、需要全文确认的材料。

### B端理论条目

| 理论 | 端口 | 成熟度 | 状态 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| B端是 source pack 层 | B | L3 | 已确立 | `10_b_port/source-pack.md` | 固化 Source Pack 模板 |
| B端先策略后搜索 | A/B | L4 | 已确立 | `10_b_port/search-strategy.md` | 使用 Search Strategy Brief |
| B端不从模糊问题泛搜索 | B | L3 | 已确立 | `10_b_port/boundary.md` 或 `search-strategy.md` | 写入禁止事项 |
| B端输出 evidence log | B | L2 | 可用 | `10_b_port/evidence-log.md` | 建立证据索引格式 |
| B端输出 rejected sources | B | L2 | 可用 | `10_b_port/rejected-sources.md` | 保存不吸收原因 |
| B端为 C端压缩上下文 | B/C | L3 | 已确立 | `10_b_port/source-pack.md` | 增加 Input Package for C端 |
| 外部 X 文章仅可用摘要 | B/C | L1 | 待补证 | `10_b_port/evidence-log.md` | 标记 `needs_full_text` |

### B端对非专业用户的意义

用户不需要自己判断一堆链接能不能用。B端负责把资料变成“哪些支持当前框架、哪些不支持、哪些只是噪音、哪些还缺全文”的清单。

## 4. C端理论

C端定位：理论合成 / 长文结构化层。

C端的核心问题是：这些想法和资料如何变成可复用理论？

C端消费 A端的问题框架和 B端的 Source Pack，然后生成 theory-index、theory-outline、theory-draft、article-draft、framework-map、open-questions。C端不负责抓资料，不负责落库，不负责最终审查。

### C端核心职责

- 把 A/B 产物合成为理论。
- 处理散乱理论、半成品理论、冲突观点。
- 标注哪些结论有证据支持，哪些只是推理。
- 按 L0-L5 给理论成熟度分级。
- 生成可进入内容工程的文件。
- 给 D端留下可能的落库计划，但不直接做 D/E/F 完整设计。
- 给 E端留下审查清单，但不自审通过。

### C端理论条目

| 理论 | 端口 | 成熟度 | 状态 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| C端是理论合成层 | C | L3 | 已确立 | `20_c_port/theory-draft.md` | 固化 C端理论包模板 |
| C端处理散乱和半成品理论 | C | L2 | 可用 | `20_c_port/theory-index.md` | 建立理论条目索引 |
| C端负责 L0-L5 分级 | C | L4 | 已确立 | `40_review/maturity-check.md` | 每条理论必须标成熟度 |
| C端不凭空造新底座 | C | L3 | 已确立 | `20_c_port/open-questions.md` | 资料不足时退回 A/B |
| C端可输出 framework map | C | L3 | 可用 | `20_c_port/framework-map.md` | 建立 A/B/C 关系图 |
| C端输出下一轮提示词 | C/A | L2 | 可用 | `20_c_port/open-questions.md` | 交回 A端或下一轮 C端 |
| C端不能替代 E端审查 | C/E | L2 | 可用 | `40_review/revision-list.md` | 后续需要独立 review |

### C端对非专业用户的意义

用户最终看到的不是一堆碎片，而是一份可读、可维护、可继续扩展的理论文档。C端把“说得通的想法”升级成“能被别人接着做的内容工程”。

## 5. A→B→C 循环机制

A → B → C 是当前最常见的知识循环。

基础流程：

```text
用户输入关键想法
→ A端保存原始意图
→ A端澄清目标、边界、非目标
→ A端形成 Initial Knowledge Frame
→ A端判断需要证据，交给 B端
→ B端先给 Search Strategy Brief
→ A端批准、修改或拒绝搜索策略
→ B端执行资料收集，生成 Source Pack + Knowledge Fit Report
→ A端决定吸收、部分吸收、重搜或拒绝
→ C端基于 A/B 产物生成理论包
→ A端决定进入下一轮研究、继续 C端写作、暂缓、或后续交给 D/E/F
```

这个循环的关键不是“让 B 搜，让 C 写”，而是两个控制点：

1. A端控制搜索策略，避免 B 泛搜索。
2. A端控制资料吸收，避免把不成熟概念直接写进方法论。

### A↔B 双闸门在循环中的位置

```text
A Initial Knowledge Frame
→ B Search Strategy Brief
→ A Gate 1: APPROVE_SEARCH / REVISE_STRATEGY / REJECT_OR_REROUTE / ESCALATE_TO_OWNER
→ B Source Pack + Knowledge Fit Report
→ A Gate 2: ACCEPT / PARTIAL_ACCEPT / REVISE_SEARCH / REJECT / ESCALATE_TO_OWNER
→ C Theory Package
```

### C端回流 A端的情况

C端不应该把所有内容都写成“已完成”。遇到以下情况要回流：

- Source Pack 不足：退回 B端补证据。
- 目标或边界不清：退回 A端重写问题框架。
- 资料冲突未决：交回 A端做吸收决策。
- 只有标题摘要、没有正文：标记 `needs_full_text`，不得臆造。
- 理论已成形但未审查：等待后续 E端审查，不直接落库。

## 6. 内容工程文件结构

推荐把 A/B/C 知识循环体系放在一个可持续生长的内容工程目录中。

建议结构：

```text
content-engineering/
  00_intent/
    raw-ideas.md
    good-question.md
    goal-audit.md
    concept-deconstruction.md
    boundary.md

  10_b_port/
    search-strategy.md
    source-pack.md
    benchmark-notes.md
    evidence-log.md
    rejected-sources.md

  20_c_port/
    theory-index.md
    theory-outline.md
    theory-draft.md
    article-draft.md
    framework-map.md
    open-questions.md

  30_command_mapping/
    dbskill-command-map.md
    spec-kit-bridge.md
    fractals-execution-reference.md
    skill-router-matrix.md

  40_review/
    decision-notes.md
    revision-list.md
    maturity-check.md
    conflicts.md

  50_archive/
    final-theory.md
    report.md
    restore-anchor.md
```

### 每层用途

`00_intent/` 保存 A端产物。这里记录用户原话、问题澄清、目标审计、概念拆解和边界。

`10_b_port/` 保存 B端产物。这里记录搜索策略、source pack、对标资料、证据日志和被拒绝资料。

`20_c_port/` 保存 C端产物。这里记录理论索引、理论大纲、长理论草稿、文章草稿、框架图和开放问题。

`30_command_mapping/` 保存桥接关系。这里说明 dbskill、Spec Kit、Fractals 等外部能力如何映射到 A/B/C，而不是替代 A/B/C。

`40_review/` 保存判断和审查。这里记录吸收决策、修改清单、成熟度检查和理论冲突。

`50_archive/` 保存阶段性成品。这里放最终理论、可交付报告和恢复锚点。

## 7. 理论分级表

L0-L5 用来判断一个想法应该放在哪里、能不能进入框架、下一步要做什么。

| 等级 | 名称 | 判断标准 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- |
| L0 | 原始碎片 | 只有一句话、灵感、链接、命令名，还不能独立理解 | `00_intent/raw-ideas.md` | 由 A端澄清 |
| L1 | 可理解观点 | 能读懂大意，但证据、边界、适用场景不足 | `00_intent/good-question.md` 或 `20_c_port/theory-index.md` | 标注假设，交 A/B 补边界或证据 |
| L2 | 局部理论 | 能解释一个局部问题，但还不能成为端口模型 | `20_c_port/theory-outline.md` | 交 C端整理结构 |
| L3 | 端口模型 | 已能说明某端口职责、输入、输出、禁止事项 | `20_c_port/framework-map.md` | 补命令映射和审查规则 |
| L4 | 知识循环结构 | 已能描述 A/B/C 如何循环、回流、吸收、分级 | `20_c_port/theory-draft.md` | 进入成熟度审查 |
| L5 | 可复用内容工程模块 | 已有稳定文件结构、模板、分级、桥接和下一步提示词 | `50_archive/final-theory.md` | 可作为后续项目模板复用 |

### 理论条目标注模板

每条理论都应使用同一套字段：

```md
## 理论名称

- 端口：A / B / C / A-B / B-C / A-B-C
- 成熟度：L0 / L1 / L2 / L3 / L4 / L5
- 状态：raw / candidate / accepted / partial / needs_evidence / needs_full_text / rejected
- 推荐落点：...
- 下一步动作：...
- 证据来源：...
- 风险或限制：...
```

### 当前关键理论分级总表

| 理论 | 端口 | 成熟度 | 状态 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| A端是 dominant front door | A | L4 | accepted | `00_intent/boundary.md` | 写入总原则 |
| A → B → C 是常见理论循环 | A-B-C | L4 | accepted | `20_c_port/framework-map.md` | 画出循环机制 |
| B端必须先策略后搜索 | A-B | L4 | accepted | `10_b_port/search-strategy.md` | 固化双闸门 |
| C端负责理论合成和 L0-L5 分级 | C | L4 | accepted | `20_c_port/theory-draft.md` | 建立理论索引 |
| dbskill 是命令家族不是新底座 | A/B/C | L3 | accepted | `30_command_mapping/dbskill-command-map.md` | 做命令映射 |
| Spec Kit 增强 A端规格化 | A | L3 | accepted | `30_command_mapping/spec-kit-bridge.md` | 映射 clarify/spec/plan/tasks |
| Fractals 是后续执行层参考 | D参考 | L2 | partial | `30_command_mapping/fractals-execution-reference.md` | 只保留桥接，不展开 D/E/F |
| X 内容资产工程文章 | B/C | L1 | needs_full_text | `10_b_port/evidence-log.md` | 补全文后再吸收 |
| `/dbs-content-system` 可启发内容工程 | A/C | L2 | candidate | `30_command_mapping/dbskill-command-map.md` | 只吸收“内容结构化系统”方向 |

## 8. dbskill / Fractals / Spec Kit 的桥接位置

这三类能力都不是新底座。它们是桥接件、增强件或后续参考。

### dbskill 桥接位置

dbskill 是命令家族和能力入口，适合映射到 A/B/C。

| 命令 | 桥接端口 | 用途 | 成熟度 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| `/dbs` | A | 命令家族入口 / router | L2 | `30_command_mapping/dbskill-command-map.md` | 标注为入口，不替代 A端 |
| `/dbs-good-question` | A | 问题澄清 | L3 | `00_intent/good-question.md` | 固化为 A端常用前置处理 |
| `/dbs-goal` | A | 目标审计 | L2 | `00_intent/goal-audit.md` | 建立目标审计文件 |
| `/dbs-deconstruct` | A/C | 概念拆解，也可辅助理论结构 | L2 | `00_intent/concept-deconstruction.md` | 拆概念后交 C端整理 |
| `/dbs-diagnosis` | A | 判断问题是否成立 | L2 | `00_intent/boundary.md` | 用于边界和问题成立性 |
| `/dbs-benchmark` | B | 对标研究 | L3 | `10_b_port/benchmark-notes.md` | 作为 B端证据来源 |
| `/dbs-learning` | C | 长期理论学习文章 | L2 | `20_c_port/article-draft.md` | 用于连续理论输出 |
| `/dbs-content-system` | C | 内容资产工程启发 | L2 | `20_c_port/framework-map.md` | 只吸收结构化方向 |
| `/dbs-save` `/dbs-restore` `/dbs-report` | A/C | 状态保存、恢复、报告 | L2 | `50_archive/restore-anchor.md` | 作为状态管理参考 |

吸收原则：

```text
dbskill 是命令家族，不是知识循环底座。
命令应被映射到 A/B/C，而不是替代 A/B/C。
```

### Fractals 桥接位置

Fractals 当前只作为后续执行层参考，不进入本轮完整设计。

可吸收的理论方向：

- 递归任务协调器。
- 自相似任务树。
- root / child / leaf task。
- isolated git worktree。
- agent swarm。
- batch polling。
- 审核计划树后执行。

本轮桥接方式：

| 理论 | 端口 | 成熟度 | 状态 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| Fractals-style recursive execution | D参考 | L2 | partial | `30_command_mapping/fractals-execution-reference.md` | 只写参考，不做 D端完整设计 |
| root / child / leaf task | D参考 | L1 | candidate | `30_command_mapping/fractals-execution-reference.md` | 等 A/B/C 成熟后再判断 |
| isolated git worktree | D/E参考 | L1 | candidate | `30_command_mapping/fractals-execution-reference.md` | 暂不展开 |

吸收原则：

```text
Fractals 不是 A/B/C 的新底座。
它只回答“理论成熟后，后续执行可能如何递归展开”。
```

### Spec Kit / brainstorming / demand-grilling 桥接位置

Spec Kit、brainstorming、demand-grilling 都主要增强 A端。

| 能力 | 桥接端口 | 用途 | 成熟度 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| `superpowers:brainstorming` | A | 前门需求拷问、方案分叉、隐含假设挖掘 | L2 | `00_intent/good-question.md` | 作为 A端辅助技能 |
| Spec Kit `clarify` | A | 澄清需求 | L3 | `30_command_mapping/spec-kit-bridge.md` | 映射到 A端 |
| Spec Kit `spec / plan / tasks` | A→D参考 | 规格化脊柱 | L2 | `30_command_mapping/spec-kit-bridge.md` | 本轮只桥接，不展开执行 |
| demand-grilling / `/dbs-good-question` | A | 把粗想法变成可批判、可验证、可路由的问题 | L3 | `00_intent/good-question.md` | 固化为 A端默认入口 |

吸收原则：

```text
它们增强 A端，不替代 A/B/C。
```

## 9. 未成熟理论与待研究问题

### 未成熟理论

| 问题 | 端口 | 当前成熟度 | 状态 | 推荐落点 | 下一步动作 |
| --- | --- | --- | --- | --- | --- |
| X 内容资产工程文章的完整方法 | B/C | L1 | needs_full_text | `10_b_port/evidence-log.md` | 获取全文后由 B端重做 Source Pack |
| `/dbs-content-system` 与本项目内容工程的关系 | C | L2 | candidate | `20_c_port/open-questions.md` | 只吸收“内容结构化系统”方向，避免替代底座 |
| Fractals 是否适合进入 D端执行 | D参考 | L1 | deferred | `30_command_mapping/fractals-execution-reference.md` | 等 A/B/C 定型后另开 D端设计 |
| A端如何避免过度控制导致循环变慢 | A | L2 | open | `40_review/conflicts.md` | 需要更多案例 |
| B端搜索策略粒度 | A/B | L2 | open | `10_b_port/search-strategy.md` | 需要模板化搜索策略 |
| C端理论包深度标准 | C | L2 | candidate | `40_review/maturity-check.md` | 建立最小可用理论包标准 |
| L0-L5 与实际文件流转的关系 | A/B/C | L3 | candidate | `40_review/maturity-check.md` | 用真实材料测试一次 |

### 待研究问题

1. A端什么时候应该直接交给 C端，而不是先让 B端补证据？
2. B端 Source Pack 的最小充分标准是什么？
3. C端输出单篇长文和输出多文件 Theory Package 的分界线是什么？
4. 哪些 dbskill 命令应该成为 A端默认前置处理？
5. `/dbs-content-system` 的完整方法是否能补充当前内容工程结构？
6. X 文章全文是否包含可验证的文件结构、流程、命令或案例？
7. L0-L5 分级是否需要增加“证据等级”字段，例如 S1-S4？
8. 当 C端发现理论冲突时，是先写 conflicts，还是退回 A端决策？
9. A/B/C 内容工程是否需要一个 `index.md` 汇总所有理论条目？
10. 什么时候才允许从 A/B/C 进入 D/E/F 后续执行？

### 本轮不解决的问题

- 不设计完整 D端 repo landing。
- 不设计完整 E端验证系统。
- 不设计完整 F端 owner decision 流程。
- 不把 Fractals 扩展成执行引擎。
- 不把 Spec Kit 扩展成完整项目管理流程。
- 不把 dbskill 重写成统一底座。

## 10. 下一轮提示词

下面提示词可用于下一轮 C端继续加工。本提示词假设已经有本文件、`goal.md`、`source-pack.md` 作为输入。

```md
# C端任务｜A/B/C 知识循环体系结构 v2 深化

请基于以下文件继续执行 C端理论深化：

- `.ai/knowledge-loop/abc-theory-content-engineering/goal.md`
- `.ai/knowledge-loop/abc-theory-content-engineering/source-pack.md`
- `.ai/knowledge-loop/abc-theory-content-engineering/c-theory-long-synthesis-v1.md`

## 任务目标

把 v1 中的 A/B/C 知识循环体系进一步整理成可落库的多文件 Theory Package。

## 严格边界

- 只处理 A/B/C 知识循环和内容工程结构。
- 不做 D/E/F 完整执行系统设计。
- 不把 Fractals / dbskill / Spec Kit 当成新底座。
- 不发明平行新工作流。
- 不臆造 X 文章正文；如果没有全文，继续标记 `needs_full_text`。

## 必须输出

1. `00_master_framework.md`：总框架。
2. `01_theory_index.md`：理论索引，每条理论标注端口、成熟度、状态、推荐落点、下一步动作。
3. `02_abc_loop_mechanism.md`：A → B → C 循环机制。
4. `03_content_engineering_structure.md`：内容工程文件结构。
5. `04_command_bridge_map.md`：dbskill / Fractals / Spec Kit 桥接图。
6. `05_maturity_l0_l5.md`：理论分级体系。
7. `06_open_questions.md`：未成熟理论与待研究问题。
8. `99_run_report.md`：本轮输入、输出、限制、未解决问题。

## 输出要求

- 用中文。
- 适合非专业用户阅读。
- 不只口头总结，必须是可直接进入文件的 Markdown。
- 每条理论必须标注：端口、成熟度、状态、推荐落点、下一步动作。
- 明确 A端是 dominant front door。
- 明确 A → B → C 是常见理论循环。

## 质量标准

- 不新增未经来源支持的理论底座。
- 不把桥接工具写成主系统。
- 不把未验证资料写成确定结论。
- 能被 A端拿去做下一轮吸收决策。
- 能被后续 D端安全落库，但本轮不执行落库。
```

