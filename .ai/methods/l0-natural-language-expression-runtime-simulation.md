# L0 自然语言表达层运行模拟验证

- 目的：用 9 个 L0 样本模拟 A bot 的实际输出，检查“普通自然语言 → 项目语言 → A 口治理”的转换是否可运行。
- 说明：这是基于当前 `a-bot-system-prompt.md` 的**人工静态模拟**，不是实际 Telegram A bot 线上调用结果。
- 结论：9 个样本均能进入 L0 结构化理解；其中 B/E/F/H 为低置信或高歧义样本，正确停在 A 口继续澄清，没有直接跳下游。

---

## 1. 评分标准

每个样本按 8 项检查：

1. 保留 Utterance
2. 识别 Intent
3. 抽取 Entities
4. 标注 Confidence
5. 标出 Ambiguity
6. 标出 Missing Slots
7. 给 Candidate Project Terms
8. 不越权执行，能进入 A 口治理

评分：

- PASS：8 项基本满足
- PARTIAL：6-7 项满足
- FAIL：少于 6 项或直接跳执行/结论

---

## 2. 样本 A：明显目标型

### User

> 我觉得这个端很重要，要把它放进项目里。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：我觉得这个端很重要，要把它放进项目里。
- Intent：目标 / 判断 / 执行倾向
- Entities：这个端、项目
- Context Used：当前 A-F 工作流、A 口意图治理端讨论
- Confidence：medium
- Ambiguity：
  - “这个端”可能指 A 口、需求拷问端、自然语言表达层或某个 bot
  - “放进项目里”可能是写文档、改 prompt、建模块、开 PR
- Missing Slots：具体对象；目标仓库/文件；是否作为候选还是正式基线
- Candidate Project Terms：A 口、意图治理端、需求拷问端、L0 自然语言表达层
- Clarification Needed：yes

## A 口元数据
- 输入类型：目标 / 执行
- 发现层级：Solution
- 动作类型：write / commit
- 风险等级：R3
- 是否需要 F 口批准：yes
- 下一端口：A

## 下一步
现在不能直接写入正式基线。先确认“这个端”具体指哪个端，以及写入方式是候选文档、A bot prompt，还是正式方法轮基线。
```

### Evaluation

PASS：正确保留原话、识别低确定对象、没有直接执行。

---

## 3. 样本 B：不确定感表达

### User

> 这个还不够清楚。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：这个还不够清楚。
- Intent：问题 / 状态判断
- Entities：这个
- Context Used：当前 A 口 / L0 / dbskill / loop agent 讨论上下文
- Confidence：low
- Ambiguity：
  - “这个”对象缺失
  - “不够清楚”可能指概念、边界、流程、权限、输出物、样本验证
- Missing Slots：对象名称；不清楚的维度；希望澄清到什么程度
- Candidate Project Terms：概念未定义、边界未清楚、术语未统一、Handoff 不清
- Clarification Needed：yes

## A 口元数据
- 输入类型：问题 / 状态
- 发现层级：Unknown
- 动作类型：generate
- 风险等级：R1
- 是否需要 F 口批准：no
- 下一端口：A

## 下一步
先不要路由 B/C/D。需要 Owner 指明“这个”指哪份文档、哪个端口或哪个概念。
```

### Evaluation

PASS：低置信处理正确，没有强行解释。

---

## 4. 样本 C：理论专业度评价

### User

> 后面理论生成不专业。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：后面理论生成不专业。
- Intent：问题 / 评价 / C 口质量诊断
- Entities：后面理论生成
- Context Used：A/B/C 工作流、C 口长理论、B Source Pack 讨论
- Confidence：medium
- Ambiguity：
  - “后面”可能指 C 口或整个下游
  - “不专业”可能指没证据、概念空、结构乱、不贴项目、不可验证
- Missing Slots：具体理论样本；不专业的表现；C 口当时输入
- Candidate Project Terms：C 口长理论、理论边界、专业表达、Source Pack、C-Theory Contract
- Clarification Needed：yes

## A 口元数据
- 输入类型：问题 / 验证
- 发现层级：Opportunity
- 动作类型：generate
- 风险等级：R1
- 是否需要 F 口批准：no
- 下一端口：A / B / C

## 下一步
先生成 C 口质量诊断问题：是否是 A 口任务书不足、B 口证据不足，还是 C 口输出结构不足。不要直接重写长理论。
```

### Evaluation

PASS：把评价词拆成诊断问题，未直接生成理论。

---

## 5. 样本 D：外部 repo 技能采纳

### User

> 这个 repo 里的技能能不能用。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：这个 repo 里的技能能不能用。
- Intent：研究请求 / 可采纳性判断
- Entities：repo、技能
- Context Used：外部技能采纳框架、ADOPT/BRIDGE/MERGE/REJECT、A-F 端口映射
- Confidence：medium
- Ambiguity：
  - repo URL 缺失
  - “能不能用”可能指直接安装、桥接、合并、只学模式或拒绝
- Missing Slots：repo 地址；目标工作流；采纳标准；是否允许写入项目
- Candidate Project Terms：External Skill Intake、Source Pack、ADOPT / BRIDGE / MERGE / REJECT
- Clarification Needed：yes unless repo already in context

## A 口元数据
- 输入类型：研究
- 发现层级：Opportunity / Solution
- 动作类型：read
- 风险等级：R0
- 是否需要 F 口批准：no for research, yes for adoption
- 下一端口：B

## 下一步
如果 repo URL 已在上下文中，转 B 口做 Source Pack；否则先补 repo 地址。不能直接安装。
```

### Evaluation

PASS：正确路由 B 口研究，区分研究和采纳授权。

---

## 6. 样本 E：循环口语表达

### User

> 我想让它循环起来。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：我想让它循环起来。
- Intent：目标 / loop agent 倾向
- Entities：它、循环
- Context Used：A-F loop、loop agent、Loop Contract
- Confidence：low
- Ambiguity：
  - “它”对象不明
  - “循环”可能是 A-F 工作流、单端口循环、cron 周期任务、agent 自主循环
- Missing Slots：循环对象；触发条件；每轮输出；停止条件；Maker/Checker；状态位置
- Candidate Project Terms：loop agent、Loop Contract、Durable State、Stop Conditions、Maker/Checker
- Clarification Needed：yes

## A 口元数据
- 输入类型：目标
- 发现层级：Outcome
- 动作类型：generate / execute later
- 风险等级：R2-R4 depending on actions
- 是否需要 F 口批准：yes before activation
- 下一端口：A

## 下一步
不能直接启动循环。先生成 Loop Contract，明确对象、触发、每轮输入输出、权限、停止条件和 Owner 介入点。
```

### Evaluation

PASS：正确阻止“无合同 loop”。

---

## 7. 样本 F：概念型表达

### User

> 这个端到底是什么？

### A bot expected output

```md
## Natural Language Understanding
- Utterance：这个端到底是什么？
- Intent：概念 / 问题
- Entities：这个端
- Context Used：A 口、L0、需求拷问端、意图治理端上下文
- Confidence：low
- Ambiguity：
  - “这个端”可能指 A 口、需求澄清端、L0 层或某个实际 bot
- Missing Slots：对象指代；希望得到定义、边界还是运行方式
- Candidate Project Terms：A 口、需求拷问端、意图治理端、L0 自然语言表达层
- Clarification Needed：yes

## A 口元数据
- 输入类型：概念
- 发现层级：Unknown
- 动作类型：generate
- 风险等级：R1
- 是否需要 F 口批准：no
- 下一端口：A

## 下一步
先做 Concept Definition Card，保留“这个端”的原话，不强行替换成单一术语。
```

### Evaluation

PASS：没有擅自替换术语。

---

## 8. 样本 G：情绪/判断表达

### User

> 我感觉这个流程有点乱。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：我感觉这个流程有点乱。
- Intent：问题 / 状态判断 / 情绪信号
- Entities：这个流程
- Context Used：A-F 工作流、端口路由、状态/队列/术语上下文
- Confidence：medium
- Ambiguity：
  - “乱”可能是顺序、权限、术语、状态、队列、交接物混乱
- Missing Slots：流程对象；乱的维度；影响是什么
- Candidate Project Terms：路由混乱、状态混乱、术语不统一、Handoff 不清、Queue 不清
- Clarification Needed：yes

## A 口元数据
- 输入类型：问题
- 发现层级：Opportunity
- 动作类型：generate
- 风险等级：R1
- 是否需要 F 口批准：no
- 下一端口：A / E

## 下一步
把“乱”拆成可检查维度：路由、权限、状态、术语、Handoff、验证。必要时交 E 口做流程审查。
```

### Evaluation

PASS：把情绪信号转成诊断维度。

---

## 9. 样本 H：动作请求

### User

> 帮我把这个写进去。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：帮我把这个写进去。
- Intent：执行请求
- Entities：这个、写进去
- Context Used：当前文档/PR/仓库上下文
- Confidence：low
- Ambiguity：
  - “这个”内容不明
  - “写进去”目标位置不明
  - 是否 commit / PR 不明
- Missing Slots：内容对象；目标路径；写入方式；是否提交；是否需要 PR
- Candidate Project Terms：write、repo landing、commit、PR、D 口执行合同
- Clarification Needed：yes unless context uniquely identifies target

## A 口元数据
- 输入类型：执行
- 发现层级：Solution / Experiment
- 动作类型：write / commit
- 风险等级：R2-R3
- 是否需要 F 口批准：yes if formal baseline or PR
- 下一端口：A / D

## 下一步
如果上下文唯一明确，可生成 D 口执行合同；否则先问目标路径和写入范围。不能在 L0 直接写。
```

### Evaluation

PASS：正确把写入请求挡在执行合同前。

---

## 10. 样本 I：判断 + 证据缺口

### User

> 我觉得这个方向对，但还缺证据。

### A bot expected output

```md
## Natural Language Understanding
- Utterance：我觉得这个方向对，但还缺证据。
- Intent：判断 / 研究请求 / 证据缺口
- Entities：这个方向、证据
- Context Used：A 口判断、B Source Pack、F Owner 决策
- Confidence：medium
- Ambiguity：
  - “方向对”是 Owner 直觉、业务判断、方法判断还是技术判断
  - 缺什么证据不明确
- Missing Slots：方向名称；证据类型；采用标准；下一步用途
- Candidate Project Terms：Evidence Gap、Source Pack、A↔B double gate、PARTIAL_ACCEPT
- Clarification Needed：yes

## A 口元数据
- 输入类型：决策 / 研究
- 发现层级：Opportunity
- 动作类型：read / generate
- 风险等级：R0-R1
- 是否需要 F 口批准：no for B research, yes for adoption
- 下一端口：B

## 下一步
把“缺证据”转成 B 口 Source Pack 请求，先查支持/反驳/修正证据，再回 A/F 判断。
```

### Evaluation

PASS：把 Owner 直觉和证据缺口分开处理。

---

## 11. 汇总评分

| 样本 | 类型 | 评分 | 关键通过点 |
|---|---|---|---|
| A | 目标/判断 | PASS | 识别对象歧义，不直接写入 |
| B | 不确定感 | PASS | 低置信，要求补对象 |
| C | 理论质量 | PASS | 拆“不专业”，不直接重写理论 |
| D | 外部 repo | PASS | 路由 B 口研究，采纳需 F |
| E | 循环 | PASS | 无 Loop Contract 不启动 loop |
| F | 概念 | PASS | 不强行替换术语 |
| G | 情绪/判断 | PASS | 把“乱”拆成诊断维度 |
| H | 执行 | PASS | 要执行合同，不直接写 |
| I | 判断+证据 | PASS | 分离 Owner 直觉和证据缺口 |

总分：9 / 9 PASS。

---

## 12. 发现的问题

虽然全部 PASS，但有 3 个需要注意的后续改进点：

1. **Clarification Needed 容易过度 yes**  
   这会让 A 口变谨慎，但可能拖慢明确上下文中的动作。后续可增加“context uniquely identifies target”规则。

2. **Candidate Project Terms 需要真实台账承接**  
   当前只是候选术语列表，还需要 `project-language-ledger.md` 承接 accepted/revised/deprecated 状态。

3. **真实 bot 可能受上下文窗口影响**  
   静态样本通过不代表真实长对话中一定稳定，需要后续在线测试。

---

## 13. 结论

L0 自然语言表达层的设计方向成立。

它能把普通自然语言先拆成：

```text
Utterance / Intent / Entities / Confidence / Ambiguity / Missing Slots / Candidate Terms
```

再交给 A 口治理，而不是直接跳到 B/C/D/E/F。

这说明当前系统已经从：

```text
需求澄清
```

进一步升级为：

```text
自然语言表达 → 项目共享语言 → 意图治理 → 端口路由
```

下一步建议：新增 `project-language-ledger.md`，让 Candidate Project Terms 有正式承接位置。
