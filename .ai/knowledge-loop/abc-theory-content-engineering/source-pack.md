# Source Pack｜A/B/C 知识循环体系结构

## 任务边界

当前只做“知识循环体系结构”层的 C 端长理论梳理。

不做：
- 直接代码实现
- 完整 D/E/F 执行系统设计
- 把 Fractals / dbskill / Spec Kit 当成新底座
- 发明平行新工作流

要做：
- 把 A端 + B端 + C端相关理论统一纳入内容工程
- 把散乱理论、半成品理论、命令映射、外部参考放入可分级结构
- 输出可长期复用的内容工程结构和 L0-L5 分级体系

## 用户偏好

- 用户不是专业工程团队或 AI 专业工作人员。
- 用户只想输入关键想法，剩下研究、理论、准备、执行推进由 AI 循环完成。
- 默认复用现成 skill / workflow / 成熟 repo，不要看见新东西就自己造轮子。
- A端使用最多，是 dominant front door。
- 常见理论循环是 A → B → C。
- 长内容、提示词、理论草案应成文件，不要散在聊天里。

## A端当前定义

A端是主入口 / Intent-to-Spec Control Gate / Demand-Control Plane。

职责：
- 接住自然语言想法
- 保留原始意图
- 澄清目标、边界、非目标
- 做 `/dbs-good-question`、`/dbs-goal`、`/dbs-deconstruct` 类型的前置处理
- 判断是否进入 B / C / D / E / F
- 先路由现成 skill，避免 AI 自己造轮子
- 输出可承接文件，如 raw-ideas、good-question、goal-audit、concept-deconstruction、boundary

## B端当前定义

B端是证据 / 对标 / source pack 层。

职责：
- 根据 A端问题框架补证据
- 用 `/dbs-benchmark`、外部搜索、source pack、evidence log
- 不做泛搜索，不从模糊问题直接扩散
- 输出 benchmark-notes、source-pack、evidence-log、rejected-sources
- 为 C端长理论合成提供压缩材料

## C端当前定义

C端是理论合成 / 长文结构化层。

职责：
- 把 A/B 产物合成为理论
- 处理散乱理论、半成品理论、冲突观点
- 生成 theory-index、theory-outline、theory-draft、article-draft、framework-map、open-questions
- 按成熟度分级 L0-L5
- 不凭空造新底座，必须吸收进现有 A/B/C 内容工程

## dbskill 桥接位置

- `/dbs`：命令家族入口 / router
- `/dbs-good-question`：A端问题澄清
- `/dbs-goal`：A端目标审计
- `/dbs-deconstruct`：A端概念拆解，也可辅助 C端结构
- `/dbs-diagnosis`：A端判断问题是否成立
- `/dbs-benchmark`：B端对标研究
- `/dbs-learning`：把课题拆成连续文章，用于长期理论研究
- `/dbs-content-system`：当材料规模足够时，把内容重构成持续生长的内容资产工程
- `/dbs-save`、`/dbs-restore`、`/dbs-report`：状态保存、恢复、报告

吸收原则：dbskill 是命令家族，不是新底座；命令应映射到 A/B/C，而不是替代方法轮。

## Fractals 桥接位置

Fractals 适合作为后续执行层参考：
- 递归任务协调器
- 自相似任务树
- root / child / leaf task
- isolated git worktree
- agent swarm
- batch polling
- 审核计划树后执行

当前边界只吸收其理论：当 A/B/C 理论成熟后，可进入 D端的 Fractals-style recursive execution。

## Spec Kit / brainstorming / demand-grilling 桥接位置

- `superpowers:brainstorming`：A端前门需求拷问、方案分叉、隐含假设挖掘
- Spec Kit：clarify / spec / plan / tasks 的规格化脊柱
- demand-grilling / `dbs-good-question`：把粗想法变成可批判、可验证、可路由的问题

它们增强 A端，不替代 A/B/C。

## 外部文章参考边界

链接：`https://x.com/dontbesilent/status/2061724612753555590?s=20`

已验证可见信息：
- 标题方向：`2 天，2 亿 token，dontbesilent 内容资产工程系统｜已免费开源`
- 摘要方向：把本地大量内容资产搭成可以继续运行的“内容结构化系统”

限制：没有完整正文。必须标记 `needs_full_text`，不能臆造文章细节。

## 现有内容工程结构参考

推荐结构：

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

## 理论分级体系

- L0：原始碎片
- L1：可理解观点
- L2：局部理论
- L3：端口模型
- L4：知识循环结构
- L5：可复用内容工程模块

每条理论要标注：端口、成熟度、状态、推荐落点、下一步动作。

## 期望输出标题

`A/B/C 知识循环体系结构｜C端长理论梳理 v1`
