# LoopFlow 与 codex-workflows 在 AI Method Wheel 里的安装与归位规则

## 0. 本文件解决的问题

用户纠正过一个关键偏差：

> 当用户给出外部 workflow/code repo 并说“安装/看看怎么用”时，不要默认把它的思想抽象吸收到 Method Wheel 底层逻辑里。先看这个仓库自己怎么安装、安装到哪里、生成什么文件、暴露什么命令、运行依赖是什么，再判断它和现有工作流如何融洽运行。

本文件继续沿用这个安装优先规则，并补上今天早上的 Fractals 部件：

```text
Fractals 不是一个要被重新造进 Method Wheel 的内部理论。
Fractals 是一个已经工作的递归任务编排成品，应该作为 PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE 来处理。
```

因此本文件的第一原则是：

```text
外部 repo → 安装面审计 → 运行面定位 → 沙盒/干跑验证 → 正确表面安装 → 再写方法轮归位规则
```

而不是：

```text
外部 repo → 抽象思想 → 默认吸收到每个 skill 或底层逻辑
```

## 1. 总原则

不要把外部项目的思想“整包塞进每一个 skill”。

但也不要只停留在“抽象吸收”。**先看怎么安装、怎么运行、怎么落到项目里，再决定哪些能力进入方法轮。**

正确做法是：

- 先确认仓库的安装方式、CLI 命令、配置文件和落盘位置
- 再把它拆成可复用的*层级能力*
- 只吸收落在当前端口契约上的那一段
- 其余部分保留为参考、可选执行层或独立工具
- 如果项目本身就是“可安装工作流”，优先按安装流程落到 repo，再从 repo 中抽取稳定底层逻辑

## 2. 本次实际安装结果

目标 repo：

`C:\Users\Administrator\AppData\Local\hermes\profiles\cangwei\home\repos\ai-`

安装前备份：

`.ai/backups/external-workflow-install-20260620-192951/`

### codex-workflows

来源：`https://github.com/shinpr/codex-workflows`

安装命令：

```bash
npx codex-workflows install
```

验证命令：

```bash
npx codex-workflows status
```

实测结果：

- 已安装 v0.7.0
- 安装器报告：`.agents/ — 72 files`，`.codex/ — 25 files`
- status 报告：`116 managed files`
- 目标生成面：
  - `.agents/skills/`
  - `.codex/agents/`
  - `.codex-workflows-manifest.json`

### LoopFlow

来源：`https://github.com/faisalishfaq2005/loopflow`

初始化命令：

```bash
npx @loopflow/cli init
```

验证命令：

```bash
npx @loopflow/cli validate
npx @loopflow/cli run test-and-fix --dry-run
```

实测结果：

- 已初始化 `.loopflow/loops/`
- 生成：
  - `debt-audit.yaml`
  - `docs-sync.yaml`
  - `release-check.yaml`
  - `test-and-fix.yaml`
- validate 通过
- `test-and-fix --dry-run` 通过，能展示 maker/checker gate
- `.gitignore` 已加入：
  - `.loopflow/worktrees/`
  - `.loopflow/memory/`
  - `.loopflow/runs/`

当前限制：本机未发现 `claude` 命令，因此 LoopFlow 真实运行还不能启用；目前只完成模板初始化、验证和 dry-run。

### Fractals

来源：`TinyAGI/fractals`

Fractals 今天早上的正确分类不是“新理论 skill”，而是：

```text
PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE
```

含义：

- 不把 Fractals 重建成 Method Wheel 内部执行器；
- 不把 A 端改造成执行引擎；
- 但可以把 Fractals 作为已工作的递归任务编排成品来 sandbox 试用；
- 允许轻包装输入/输出；
- 允许把树形分解结果接回 A/B/C/D/E/F 的治理与复核链路。

Fractals 的最适合位置：

- **A**：把自然语言想法分叉成候选分支
- **B**：在递归分解前收集 context/source hints
- **C**：做递归计划、树形结构审阅、边界澄清
- **D**：如果 sandbox 批准，可执行叶子任务
- **E**：核对状态、结果、假完成防护
- **F**：owner 在执行前做计划批准

Fractals 的核心价值不是 A-port 独占，而是**全工作流的递归分解与执行分层参考**。

## 3. LoopFlow 应该放在哪里

LoopFlow 属于**循环/控制运行层**，不是业务语义层，也不是 Hermes 全局 skill 层。

它适合放在：

- **Phase -1：控制平面设计**
  - 定义 loop、maker/checker、budget、attempt limit、memory、worktree
- **Phase 3/D：执行前后**
  - 包装 bounded maker run
- **Phase 4/E：验证门**
  - PASS/FAIL gate、重试、拒绝未验证结果
- **Phase 6-7/F/学习沉淀**
  - 记录 run memory、恢复上下文、形成可追踪的 loop record

### LoopFlow 吸收规则

吸收的是这些“底层控制机制”：

- 迭代 orchestration
- maker/checker 分离
- gate-based verification
- budget/attempt 限制
- memory persistence
- optional worktree isolation

不吸收的内容：

- 具体某个业务技能的语义
- 每个 skill 的 prompt 细节
- 每个 repo 的专用命令
- 把 LoopFlow 当作 A 端主入口

### LoopFlow 使用规则

```text
A 判断是否需要循环
→ C 定义 loop 目标、gate、预算、停机条件
→ LoopFlow dry-run
→ D/LoopFlow 执行
→ E gate 验证
→ F/owner 决定继续、停止或归档
```

## 4. codex-workflows 应该放在哪里

codex-workflows 属于**Codex 运行编排层**，更接近“项目级执行框架”。

它适合放在：

- **Phase 0：仓库 onboarding**
  - install 到目标 repo
  - 生成/维护 `.agents/skills/`、`.codex/agents/`、manifest
- **Phase 1-2：需求澄清与规格化后**
  - requirement analyzer / PRD / design doc / task slicing
- **Phase 3/D：Codex 执行层**
  - 用 recipes/subagents 跑实现
- **Phase 4/E：质量门**
  - tests / lint / build / review gate
- **Phase 6/F：交付**
  - commit / PR / handoff

### codex-workflows 吸收规则

吸收的是这些“项目执行骨架”：

- requirements → design → tasks → implementation → quality gates
- separate subagent contexts
- traceable artifacts
- test skeletons / TDD / review gates
- PR-sized / multi-file change orchestration

不吸收的内容：

- 把 Codex workflows 当成新的 A 端入口
- 把它替换成方法轮总底座
- 把所有外部 recipe 原样照搬到每个项目
- 把 Codex 的 execution recipes 安装成 Hermes 全局 skill

### codex-workflows 使用规则

```text
A boundary brief
→ B source/context pack if needed
→ C design/spec/theory
→ codex-workflows recipe in Codex
→ D implementation
→ E verification
→ F owner decision / commit / PR
```

## 5. Fractals 在工作流里的位置

Fractals 不是“第三个要安装成 skill 的底座”，而是**递归分解与候选树生成的实践桥接件**。

它适合放在：

- **A**：把模糊想法变成候选分支，帮助 A 端产生更多可评估路线
- **C**：当分支形状、深度和边界已经清楚时，用递归树做规划理论
- **D**：如果 sandbox 批准，做叶子任务执行与 worktree 隔离
- **E**：做进度/结果/假完成检查

Fractals 的吸收规则：

- 允许借用 classify/decompose/branch-shaping 思路
- 不允许把 worktree、leaf execution、batch scheduling 直接塞回 A 端
- 不允许把 recursive planner 重写为 Method Wheel 自己的新轮子
- 只在 sandbox adopt 的前提下接入真实执行面

### Fractals 的正确分类

```text
PRACTICAL_BRIDGE + SANDBOX_ADOPT_CANDIDATE
```

### Fractals 不应该被当作

- 一个 A-port 的纯理论灵感来源
- 一个要重新造的执行引擎
- 一个需要拆掉重写的内部技能仓库

## 6. 两者和方法轮的关系

方法轮负责的是：

- A/B/C/Bridge 语义分工
- A 端主入口
- 非专业 Owner 的前门
- 研究 / 复用 / 合成 / 同步

LoopFlow 负责的是：

- loop control
- gate
- budget
- memory
- isolation

codex-workflows 负责的是：

- repo-level orchestration
- spec / task / implementation / verification pipeline
- subagent 组织
- Codex 工作流落地

Fractals 负责的是：

- recursive decomposition
- candidate branching
- tree-shaped planning
- sandboxed leaf-task candidate execution

三者关系：

```text
Hermes / Method Wheel = 决策与治理层
codex-workflows = Codex 执行编排层
LoopFlow = 可选循环运行层
Fractals = 递归分解与树形执行参考/桥接候选
```

## 7. 推荐安装与启用顺序

如果要把这些项目真正接入方法轮，顺序应该是：

1. **先冻结方法轮端口契约**
   - A/B/C/Bridge 各自职责先固定
2. **安装/检查 codex-workflows 到目标 repo**
   - 因为本机已有 Codex 和 Node 22，可实际使用
3. **初始化 LoopFlow 模板，但暂不默认真实运行**
   - 因为当前缺少 Claude Code CLI
4. **把 Fractals 当作实践桥接候选做 sandbox adopt 试用**
   - 先生成树，不急着执行叶子
5. **写入 A 端 placement rule**
   - 明确何时调用哪一个运行面
6. **如需真实 LoopFlow run，先安装/认证 Claude Code**

## 8. 你这个场景的判断

你不是要把每个 skill 的思想都吸进去；你要的是：

- 留住“真正能提升工作流稳定性”的那几个底层机制
- 其余的保持成可选参考，不进入默认心智负担
- 外部项目能安装就优先安装到正确表面，不要先变成内部空理论

所以最合适的吸收方式是：

- **LoopFlow = 控制运行能力**
- **codex-workflows = Codex 执行编排能力**
- **Fractals = 递归分解与树形执行桥接候选**
- **方法轮 = 语义与治理总框架**

## 9. 一句话结论

> LoopFlow 不进每个 skill，它进“可选循环运行层”；codex-workflows 不进每个 skill，它进“Codex 执行编排层”；Fractals 不进每个 skill，它进“递归分解与树形执行桥接候选”；方法轮保持 A/B/C/Bridge 的总治理框架不变，并且以后遇到外部 workflow repo，必须先做安装面审计和 dry-run，再谈思想吸收。
