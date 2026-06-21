# 需求拷问端执行表达 Brief：多端口核心职责重构 v0.1

> 生成时间：2026-06-16T20:29:36
> 执行原则：先由 A端/需求拷问端把问题表达正确，再生成各端口可复制执行的 Port Contract + Prompt。

---

## 1. Original Ask / 用户原始需求

用户指出：

```text
现在发现每一个端口都没有重点搞清楚，自己的重点是什么，再深挖下对于整体流程，端口要明确自身的核心来完善。
按照需求拷问端来正确表达来做执行。
```

---

## 2. Improved Agent-Usable Question / 改写后的可执行问题

```text
Given 当前 A/B/C/D/E/F 多端口 AI 工作流已经初步分工但每个端口核心不够清楚，
for 用户正在搭建的 Hermes + Telegram 多 bot + Codex + GitHub loop workflow，
将“端口职责”重构为可复制执行的 Port Contract + Prompt 文件，
while preserving maker/checker 分离、research_only/trading 禁止边界、GitHub/repo 真源、长输出以文件交付、Owner 只做方向/权限/合并/风险决策。
Success means 每个端口都有唯一核心、输入、输出、禁止事项、退回规则、下游交付规则、验证标准和可复制 prompt。
Verify by 生成 A/B/C/D/E/F 六个端口 prompt 文件 + index 文件，并确认文件存在、行数/大小可读。
If blocked by 不清楚具体 bot 名称或未来技能安装方式，则先生成通用端口契约，不等待用户补充。
```

---

## 3. Intent and Alternatives / 真实意图与替代方案

### 真实意图

用户不是要再泛泛讨论“端口分工”，而是要让需求拷问端把任务表达正确，并把正确表达直接转化为可执行端口文件。

### 不采用的错误方式

```text
1. 不再只说 A/B/C/D/E/F 的大概职责。
2. 不再给每个端口塞一堆技能名称但没有核心产物。
3. 不再让每个端口都做完整通用助手。
4. 不再把长 prompt 粘在聊天里。
```

### 采用的方式

```text
需求拷问端先定义问题 → 明确端口唯一核心 → 生成 Port Contract → 生成可复制 Prompt → 打包交付。
```

---

## 4. Context and Constraints / 上下文与约束

```text
当前工作流：A/B/C/D/E/F 多 Telegram bot + Hermes + Codex + GitHub/repo。
用户偏好：长输出生成文件并作为附件，不粘贴长文本。
项目边界：meme/GMGN/量化项目当前 research_only / observe_only，不允许 private key、API key、swap、自动交易、实盘下单。
方法论边界：A 是需求/控制；B 是 Source Pack；C 是理论/Codex maker；D 是 repo landing；E 是 checker；F 是 Owner。
```

---

## 5. Scope and Non-Goals / 范围与非目标

### 本次要做

```text
1. 生成 A端 Demand Control Port Prompt。
2. 生成 B端 Source Pack Port Prompt。
3. 生成 C端 Theory/Codex Port Prompt。
4. 生成 D端 Repo Landing Port Prompt。
5. 生成 E端 Verification Review Port Prompt。
6. 生成 F端 Owner Decision Brief Template。
7. 生成 index 文件说明如何使用。
8. 打包为 zip，方便下载。
```

### 本次不做

```text
1. 不安装外部仓库技能。
2. 不修改 ai- 或 meme- repo。
3. 不调用 Codex 执行大型生成。
4. 不触碰交易/API/private key/swap。
5. 不创建 GitHub PR，除非用户后续明确要求同步到仓库。
```

---

## 6. Assumptions and Risks / 假设与风险

```text
[confirmed] 用户要的是需求拷问端的正确表达，而不是继续泛泛分析。
[confirmed] 长文件应作为附件输出。
[confirmed] A端应作为控制平面，而不是普通聊天端。
[unconfirmed] 每个 Telegram bot 的最终系统 prompt 是否支持很长文本。
[risky] 如果各端口 prompt 太像通用助手，会继续失焦。
[risky] 如果 C/D/E 边界不清，会出现 maker 自审或未审理论直接落库。
```

---

## 7. Acceptance Criteria / 验收标准

```text
1. 产出文件夹 multi_port_contracts_v0.1。
2. 至少包含 8 个 txt 文件：需求拷问 brief、index、A/B/C/D/E/F prompt。
3. 每个端口 prompt 都必须包含：身份、唯一核心、输入、输出、禁止事项、退回规则、下游规则、完成标准。
4. A端 prompt 必须体现 Demand Grilling Brief，而不是大问卷。
5. B端 prompt 必须体现 Source Pack，不生成最终理论。
6. C端 prompt 必须体现 Theory Package，不直接落库。
7. D端 prompt 必须体现 Repo Landing，不创造理论。
8. E端 prompt 必须体现独立 checker，不做 maker。
9. F端模板必须体现 Owner 只做方向/权限/风险/合并决策。
10. 生成 zip 文件并验证文件存在。
```

---

## 8. Verification Plan / 验证计划

```text
1. 用脚本写入所有 txt 文件。
2. 统计文件数量、大小、行数。
3. 生成 zip 包。
4. 输出可下载附件路径。
```

---

## 9. Agent Execution Classification / 执行分类

```text
Classification: Autonomous
Reason: 任务边界明确，无需修改项目 repo，无需外部权限，无高风险交易/secret 操作。
Authority Boundary: 只允许在 Hermes outputs 目录生成文件和 zip，不修改业务仓库。
Maker: 当前 Hermes 执行。
Checker: 文件存在性、数量、行数、zip 验证。
```

---

## 10. Loop Stop Conditions / 停止条件

```text
Success Stop: 所有 prompt/contract 文件和 zip 生成完成并验证存在。
No-progress Stop: 文件写入失败或路径权限失败时停止并报告。
Escalate to Owner: 只有当用户要求同步到 GitHub/repo、覆盖现有 bot prompt、或接入真实交易/API 权限时才需要 Owner 决策。
```

---

## 11. Critique Prompts / 审查问题

```text
1. 每个端口是否有唯一核心产物？
2. 是否仍有端口在抢其他端口的活？
3. 是否把 A端做成了大问卷，而不是路由控制 brief？
4. C端是否可能绕过 B端资料不足直接硬写理论？
5. D端是否可能未经过 E1 审查就落库？
6. E端是否真的独立于 maker？
7. Owner 是否只收到决策 brief，而不是原始混乱上下文？
```

---

## 12. Missing High-Value Questions / 仍可后续追问的问题

当前不阻塞执行，但后续可问：

```text
1. 每个端口对应的 Telegram bot 名称是否要写入 prompt？
2. 这些 prompt 是只用于 Telegram bot 新会话，还是也要同步进 ai- 方法论仓库？
3. 每个端口是否需要再生成精简版和完整版两个版本？
```

---

## 13. Next Stage / 下一阶段

```text
Ready for: Generate Port Contracts + Prompts
```
