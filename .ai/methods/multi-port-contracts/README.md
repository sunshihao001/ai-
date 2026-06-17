# Multi-Port Contracts v0.1

> 生成时间：2026-06-16T20:29:36
> 用法：把对应 txt 文件复制到对应 Telegram bot / Hermes 新会话中，作为端口初始化 prompt。

## 文件清单

```text
00_Demand_Grilling_Brief_多端口执行表达_v0.1.txt
A端_Demand_Control_Port_Prompt_v0.1.txt
B端_Source_Pack_Port_Prompt_v0.1.txt
C端_Theory_Codex_Port_Prompt_v0.1.txt
D端_Repo_Landing_Port_Prompt_v0.1.txt
E端_Verification_Review_Port_Prompt_v0.1.txt
F端_Owner_Decision_Brief_Template_v0.1.txt
```

## 使用顺序

```text
1. 先读 00_Demand_Grilling_Brief，理解为什么这样拆。
2. A端 bot 使用 A端 prompt。
3. B端 bot 使用 B端 prompt。
4. C端 bot 使用 C端 prompt。
5. D端 bot 使用 D端 prompt。
6. E端 bot 使用 E端 prompt。
7. F端/Owner 决策时使用 F端模板。
```

## 关键原则

```text
A管做什么和为什么。
B管根据什么资料。
C管形成什么理论/方案。
D管落到哪里和怎么改。
E管凭什么说它对。
F管是否允许进入下一阶段。
```

## A↔B 双闸门循环

A端不应把初步想法直接丢给 B端“去搜索”。当任务目标是完善知识框架或方法论时，A/B 应使用双闸门：

```text
A 初步知识框架
  → B Search Strategy Brief
  → A Gate 1 审核搜索策略
  → B Source Pack + Knowledge Fit Report
  → A Gate 2 审核是否吸收进知识框架
```

详见：

```text
.ai/methods/multi-port-contracts/a-b-double-gate-loop.md
```

这条规则服务总体目标：AI 主导执行循环，人类只负责大方向、边界和关键决策。

## 下一步建议

如果这些端口契约方向确认，下一步可以把它们同步到：

```text
1. ai- 方法论仓库：作为 method-wheel/multi-port contracts。
2. meme- 业务仓库：作为项目级 AI 操作面板和端口提示词。
3. 每个 Telegram bot 的初始化会话。
```


## Repository files

```text
.ai/methods/multi-port-contracts/00-demand-grilling-brief.md
.ai/methods/multi-port-contracts/a-demand-control-port.md
.ai/methods/multi-port-contracts/b-source-pack-port.md
.ai/methods/multi-port-contracts/c-theory-codex-port.md
.ai/methods/multi-port-contracts/d-repo-landing-port.md
.ai/methods/multi-port-contracts/e-verification-review-port.md
.ai/methods/multi-port-contracts/f-owner-decision-brief.md
```
