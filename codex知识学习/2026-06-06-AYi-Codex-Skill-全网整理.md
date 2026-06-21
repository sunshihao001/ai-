# 我把全网的 Codex Skill 扒了一遍：最该装的几个、安装方法、资源仓库都整理好了

- 来源类型：X Article / X Post
- 作者：AYi（@AYi_AInotes）
- 原帖链接：https://x.com/AYi_AInotes/status/2063283898419749193
- Article 链接：https://x.com/AYi_AInotes/article/2063283898419749193
- 发布时间：2026-06-06 15:36（X 页面显示）
- 抓取时间：2026-06-17
- 主题归档：Codex / Codex Skill / Agent Skill / AI 编程工作流

## 已抓取到的原文摘要

> 我把全网的 Codex Skill 扒了一遍：最该装的几个、安装方法、资源仓库都整理好了，看这一篇就够了！
>
> 先说结论：装对 create-plan + gh-fix-ci 和几个核心 curated Skill，Codex 立刻从会写代码的聊天机器人变成靠谱的工程师团队。
>
> 这篇我把全网挖到的整理成五块——必 star 的仓库、按场景分的神级 Skill、保姆级安装、进阶组合技、持续追更的资源……

## 搜索结果补充摘要

搜索结果中该 Article 的描述为：

> 先说结论：装对 create-plan + gh-fix-ci 和几个核心 curated Skill，Codex 立刻从会写代码的聊天机器人变成靠谱的工程师团队。 这篇我把全网挖到的整理成五块——必 star 的仓库、按场景分的神级 Skill、保姆级安装、进阶组合技、持续追更的资源，以及装哪几个、去哪……

## 初步知识点

1. 文章关注点是 **Codex Skills 的选择、安装、资源仓库和组合使用**。
2. 作者明确强调：`create-plan` + `gh-fix-ci` 是关键组合。
3. 文章把 Codex 从“会写代码的聊天机器人”升级为“靠谱工程师团队”的路径，归因于正确安装和组合 Skill。
4. 这与当前 AI Method Wheel 中的“需求门控 → 计划 → Codex Maker → CI/Checker → PR/ADR”路线高度相关。

## 对本仓库方法轮的潜在启发

- 不应无脑安装大量 Codex Skill，而应先做 **核心 Skill 抽取与本地化适配**。
- `create-plan` 可映射到本项目的：
  - Demand Grilling Brief 之后的计划生成层；
  - spec / issue / ADR 前置结构化层；
  - Codex 执行前的任务边界定义。
- `gh-fix-ci` 可映射到本项目的：
  - E 端 checker；
  - CI 失败自动修复；
  - PR 验证闭环。
- Codex Skill 的价值不只是“能力插件”，更像是把 Codex 命令和工程流程封装成可复用的命令框架。

## 抓取状态

- `web_extract(status URL)`：成功获取帖子摘要，但不是完整 Article。
- `web_extract(article URL)`：失败，返回空内容。
- Browser 自动打开失败：当前 Hermes 浏览器环境缺少 Chrome，提示需要 `agent-browser install`。

## 待补全

后续如果能通过登录态浏览器、X Article 可访问页面、第三方镜像、作者其他发布渠道或手动复制原文获取完整内容，需要补充：

1. 必 star 仓库清单。
2. 按场景分类的 Codex Skill 列表。
3. 安装命令。
4. 进阶组合技。
5. 持续追更资源。
6. 对本项目 AI Method Wheel 的正式决策：哪些吸收为 skill，哪些只作参考，哪些禁用。

## 本目录规则

本文件位于 `codex知识学习/`。以后读取、分析、摘录、总结 **Codex 相关文章** 时，都应优先保存到本目录。
