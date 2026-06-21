# L0 自然语言表达层样本集

- 目的：测试系统能否先接住 Owner 的普通自然语言表达，再把它治理成项目语言。
- 作用：验证 L0 是否真的能抽取 Utterance / Intent / Entities / Context / Confidence / Ambiguity / Missing Slots / Candidate Project Terms。
- 适用：A 口正式基线前的样本测试；也可用于 A bot prompt 回归验证。

---

## 1. 样本总原则

L0 先做的是“理解自然语言表达本身”，不是直接做项目决策。

L0 输出必须包含：

```md
## Natural Language Understanding
- Utterance：用户原话
- Intent：目标 / 问题 / 概念 / 控制 / 决策 / 执行 / 验证
- Entities：对象、端口、repo、文件、技能、概念
- Context Used：本轮用到的上下文
- Confidence：high / medium / low
- Ambiguity：...
- Missing Slots：...
- Candidate Project Terms：...
- Clarification Needed：yes / no
```

### L0 处理规则

- 不要立刻改写成完整需求。
- 不要把用户说法直接替换成系统术语。
- 不要在自然语言层就跳到 D 口执行。
- 当置信度低或歧义高时，先标出来，再进入 A 口治理。
- 如果存在项目内专有词，先写入候选术语，而不是随意替换。

---

## 2. 样本 A：明显目标型，但仍是自然语言

### 用户原话

> 我觉得这个端很重要，要把它放进项目里。

### 期望 L0 识别

- Intent：目标 / 判断
- Entities：这个端、项目
- Confidence：medium
- Ambiguity：
  - “这个端”指什么不明确
  - “放进项目里”是文档、提示词、模块、还是流程不清楚
- Missing Slots：
  - 具体对象
  - 放入方式
  - 放入后的用途
- Candidate Project Terms：
  - A 口
  - 意图治理端
  - 需求拷问端

### 不合格表现

- 直接把它当作“已确认的功能需求”
- 直接生成实现方案
- 不保留原话

---

## 3. 样本 B：关于不确定感的表达

### 用户原话

> 这个还不够清楚。

### 期望 L0 识别

- Intent：问题 / 状态判断
- Entities：这个
- Confidence：low
- Ambiguity：
  - “这个”到底是 A 口、B 口、理论、还是文档
  - “不够清楚”是概念不清、边界不清、还是流程不清
- Missing Slots：
  - 对象名称
  - 不清楚的维度
- Candidate Project Terms：
  - 概念未定义
  - 边界未清楚
  - 术语未统一

### 合格表现

- 标出这是一个低置信输入
- 提醒需要补对象
- 交给 A 口做进一步澄清

---

## 4. 样本 C：对理论专业度的评价

### 用户原话

> 后面理论生成不专业。

### 期望 L0 识别

- Intent：问题 / 评价
- Entities：后面理论生成
- Confidence：medium
- Ambiguity：
  - “不专业”是概念空、结构乱、没证据、没边界，还是没贴项目不清楚
  - “后面”指 C 口还是整个流程不清楚
- Missing Slots：
  - 不专业的具体表现
  - 哪一轮输出
  - 哪类理论
- Candidate Project Terms：
  - C 口长理论
  - 专业表达
  - 理论边界

### 合格表现

- 不直接解释“为什么不专业”
- 先把“专业”的含义拆成可治理的槽位

---

## 5. 样本 D：外部 repo / 技能能不能用

### 用户原话

> 这个 repo 里的技能能不能用。

### 期望 L0 识别

- Intent：研究请求 / 可采纳性判断
- Entities：repo、技能
- Confidence：medium
- Ambiguity：
  - “这个 repo”具体是哪一个
  - “能不能用”是直接安装、部分采用，还是只学模式不清楚
- Missing Slots：
  - repo 名称
  - 使用场景
  - 采用标准
- Candidate Project Terms：
  - ADOPT / BRIDGE / MERGE / REJECT
  - Source Pack

### 合格表现

- 先识别这是外部技能采纳问题
- 不直接进入安装或复制

---

## 6. 样本 E：关于循环的口语表达

### 用户原话

> 我想让它循环起来。

### 期望 L0 识别

- Intent：目标 / 执行意图
- Entities：它
- Confidence：low
- Ambiguity：
  - “它”是谁
  - “循环起来”是 A-F loop、单个子任务循环，还是周期性运行不清楚
- Missing Slots：
  - 对象
  - 循环类型
  - 触发条件
  - 停止条件
- Candidate Project Terms：
  - loop agent
  - Loop Contract
  - 触发 / 停止 / 回填

### 合格表现

- 把“循环起来”识别成循环意图，但不直接等于已定义 loop
- 引导进入 A 口定义 Loop Contract

---

## 7. 样本 F：概念型表达

### 用户原话

> 这个端到底是什么？

### 期望 L0 识别

- Intent：概念 / 问题
- Entities：这个端
- Confidence：low
- Ambiguity：
  - 端指端口、模块、角色、流程还是机器人不清楚
- Missing Slots：
  - 所指对象
  - 上下文
- Candidate Project Terms：
  - A 口
  - 意图治理端
  - 需求拷问端
  - 自然语言表达层

### 合格表现

- 先保留“这个端”的原话状态
- 不强行替换成任何单一术语
- 交给 A 口或 Concept Definition 继续治理

---

## 8. 样本 G：带情绪/判断的表达

### 用户原话

> 我感觉这个流程有点乱。

### 期望 L0 识别

- Intent：问题 / 状态判断
- Entities：这个流程
- Confidence：medium
- Ambiguity：
  - “乱”是顺序乱、权限乱、术语乱、还是队列乱不清楚
- Missing Slots：
  - 乱的维度
  - 当前流程名称
- Candidate Project Terms：
  - 路由混乱
  - 状态混乱
  - 术语不统一
  - Handoff 不清

### 合格表现

- 不把情绪词直接当结论
- 把“乱”拆成可检查维度

---

## 9. 样本 H：动作请求

### 用户原话

> 帮我把这个写进去。

### 期望 L0 识别

- Intent：执行请求
- Entities：这个
- Confidence：low
- Ambiguity：
  - “这个”是什么
  - 写进去哪里不清楚
- Missing Slots：
  - 目标仓库
  - 文件路径
  - 是否允许提交
- Candidate Project Terms：
  - write
  - commit
  - PR
  - repo landing

### 合格表现

- 先识别是执行请求
- 不在 L0 阶段就写文件
- 转 A 口去做执行合同

---

## 10. 样本 I：判断 + 原因混合表达

### 用户原话

> 我觉得这个方向对，但还缺证据。

### 期望 L0 识别

- Intent：判断 + 问题
- Entities：这个方向、证据
- Confidence：medium
- Ambiguity：
  - “对”是业务对、技术对、还是 Owner 感觉对不清楚
- Missing Slots：
  - 方向名称
  - 缺什么证据
- Candidate Project Terms：
  - Outcome
  - Evidence gap
  - Source Pack

### 合格表现

- 把“对”与“证据缺失”分开
- 不直接假设方向已确认

---

## 11. L0 验收表

| 检查项 | 通过标准 |
|---|---|
| 保留原话 | 输出里有 Utterance，不用系统术语替代 |
| 意图识别 | 能把自然语言分到目标 / 问题 / 概念 / 控制 / 决策 / 执行 / 验证 |
| 实体提取 | 能指出对象、端口、repo、文件、技能、概念 |
| 置信度 | 能标 high / medium / low |
| 歧义标注 | 能指出多解点 |
| 缺口标注 | 能指出还缺什么槽位 |
| 候选术语 | 能列出项目术语候选而不是乱命名 |
| 不越权 | 不在 L0 就执行、不直接下结论 |
| 可交给 A 口 | 输出能直接进入 A 口治理 |

---

## 12. 通过标准

如果一个样本满足以下条件，才算 L0 通过：

1. 能保留原话。
2. 能识别自然语言表达的意图。
3. 能提取关键实体。
4. 能标出置信度。
5. 能指出歧义和缺失槽位。
6. 能提出候选项目术语。
7. 不会提前执行或抢走 A 口职责。

---

## 13. 失败模式

以下情况都算 L0 失败：

- 把用户原话直接翻译成完整需求
- 直接替换成系统术语
- 低置信输入却装作已确认
- 不保留歧义和缺口
- 在 L0 阶段就生成执行计划
- 不输出候选项目术语
- 不知道该交给 A 口继续治理

---

## 14. 设计目的

L0 的真正目的不是“更会回答”，而是：

```text
让普通自然语言有机会被治理成项目语言
```

如果 L0 做得好，Owner 不必先学会专业表达，系统也不会因为自然语言模糊而跑偏。

---

## 15. 使用建议

把这份样本集作为：

- A bot prompt 的回归测试
- A 口正式定义的上线前检查
- B 口 Source Pack 研究前的语言澄清参考
- 新术语出现时的“是否进台账”判断依据
