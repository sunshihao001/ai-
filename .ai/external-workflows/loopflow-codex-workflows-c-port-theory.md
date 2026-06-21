# LoopFlow + codex-workflows 的 C-port 理论

## 核心结论

不要默认把外部仓库的想法“吸收到 Method Wheel 里”。正确顺序是先看安装面，再看运行面，再决定放进哪一层理论与哪个运行表面。

这次对 `loopflow` 与 `codex-workflows` 的处理，结论不是“把它们当成新的内部原理”，而是：

1. 先识别它们各自的安装目标和生成物。
2. 再确认本地前置条件和实际可运行边界。
3. 最后才决定它们在 Method Wheel 里该放在哪个端口、哪个层级、哪个工作流阶段。

这就是安装优先、运行表面优先、理论归位在后。

## 三层关系

### 1. Method Wheel / Hermes

这是 A 端控制面和面向 owner 的治理层。

职责是：

- 定义问题入口。
- 选择工作流。
- 决定是否进入 B/C/D/E/F。
- 设定边界、预算、验证标准、回写位置。

### 2. codex-workflows

这是 Codex 侧的执行编排层。

它不是 Method Wheel 的“底层哲学”，而是 Codex 执行面上的 recipe / agent / task 编排。

### 3. LoopFlow

这是可选的 loop runner。

它提供 maker/checker gate、预算、迭代上限、记忆、可选 worktree 隔离，适合做有明确验收门的循环执行。

## 为什么不应该安装成 Hermes 全局 skill

把外部仓库直接安装成 Hermes 全局 skill，会把三个平面混在一起：

- 控制平面：A 端负责定题、定界、定验证。
- 执行平面：Codex 负责 recipe 驱动的实现。
- 运行平面：LoopFlow 负责循环、门禁、重试和状态。

如果把它们都塞进 Hermes 全局 skill，问题会变成：

- 控制面被误写成执行面。
- 执行面被误写成方法论本体。
- 运行时规则被误写成永久治理规则。

这会让人误以为“只要看见一个 workflow repo，就要把它的全部逻辑复制到 Method Wheel”。这正是需要修正的失败模式。

安装到目标 repo，和把所有 workflow 复制进 Hermes，是两件完全不同的事。

前者是在正确表面上落地。
后者是在错误层级上抽象。

## A 端判断流程

正确流程是：

1. 原始外部仓库链接。
2. 先看安装面。
3. 再看运行假设。
4. 检查本地前置条件。
5. 决定目标表面。
6. 做 dry-run / sandbox。
7. 安装。
8. 验证。
9. 再写 placement rule。

这里 A 是主门。

没有经过 A 的判断，不应该直接进入“我要把它写进方法轮”的动作。

## 环节定位

### A / B / C / D / E / F 映射

| 工具 | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Method Wheel / Hermes | 主控制面 | 接收源包/压缩上下文 | 理论定稿前判断 | 选择落地表面 | 监督验证 | owner 决策 |
| codex-workflows | 入口治理和选择 | 可读取上下文 | 需求拆解后的 Codex recipe 入口 | Codex 执行编排 | 质量检查与状态回写 | owner 最终确认 |
| LoopFlow | 是否需要 loop 的判断 | 可承接输入材料 | loop 目标、gate、预算定义 | 实际循环执行 | 每轮 gate 验证 | owner 决定继续/停止 |

### 位置关系

`codex-workflows` 的位置是：A/B/C 之后，D/E 之前，属于 Codex 执行内部的编排层。

`LoopFlow` 的位置是：C 先定义 loop 目标和 gate，D 负责执行，E 负责验证，F 由 owner 决定是否继续、收敛或停止。

## 运行规则

### 什么时候用 codex-workflows

适合：

- Codex CLI 可用，且任务需要 recipe 化执行。
- 需要把需求拆成 analyzer / planner / executor / verifier 这种稳定角色。
- 需要把工作结果写进 `.codex/agents/`、`.codex/skills/` 这类 Codex 表面。
- 需要 TDD、任务分解、质量检查、子代理上下文隔离。

不适合：

- 把它当成 Hermes 的全局思想替身。
- 把外部 repo 的 recipe 直接当成 Method Wheel 的终极原理。

### 什么时候用 LoopFlow

适合：

- 任务本身就是循环型。
- 需要 maker/checker 分离。
- 需要 dry-run 先看门禁格式。
- 需要预算、迭代上限、记忆、worktree 隔离。

不适合：

- 没有明确 gate 的纯探索任务。
- 缺少可运行前置条件。
- 只想写一个理论总结，不打算实际跑 loop。

### 什么时候都不用

都不用的情况包括：

- 只是要整理方法论，不需要执行器。
- 任务只需要 owner 决策，不需要循环。
- 本地前置条件不足，真实运行会徒增噪音。

## 当前安装状态

### codex-workflows

状态：已安装。

已确认生成面：

- `.agents/`，安装结果显示 72 个文件。
- `.codex/`，安装结果显示 25 个文件。
- 合计 97 个文件已安装。
- `codex-workflows status` 显示 116 个 managed files。

可用命令：

- `npx codex-workflows install`
- `npx codex-workflows status`
- `npx codex-workflows update --dry-run`
- `npx codex-workflows update`

### LoopFlow

状态：已初始化。

已生成：

- `.loopflow/loops/debt-audit.yaml`
- `.loopflow/loops/docs-sync.yaml`
- `.loopflow/loops/release-check.yaml`
- `.loopflow/loops/test-and-fix.yaml`

已验证：

- `npx @loopflow/cli validate` 通过。
- `npx @loopflow/cli run test-and-fix --dry-run` 通过 dry-run，且显示 maker/checker prompts 与 `VERDICT: PASS/FAIL` gate 格式。
- `.gitignore` 已更新，包含 `.loopflow/worktrees/`、`.loopflow/memory/`、`.loopflow/runs/`。

未完成：

- LoopFlow 真实执行未跑。
- 真实执行要求 Claude Code 已安装并认证。
- 当前环境未找到 Claude Code，因此真实运行被阻塞。

### 本地前置条件

- Node：`v22.22.3`
- npm：`10.9.8`
- Codex CLI：可用
- Claude Code CLI：未在 PATH 中找到
- Git：可用

## 给未来 AI 的底层提示修正规则

把下面这条旧倾向删掉：

- `external repo -> abstract absorption`

换成这条：

- `external repo -> install-surface audit -> runtime placement -> sandbox install -> placement rule`

这条规则的含义很简单：

- 先确认仓库是“怎么装”。
- 再确认它“在哪里跑”。
- 再确认它“需要什么”。
- 最后才决定“要不要进入 Method Wheel 的长期知识结构”。

## Owner 下一步

可直接回复下面任意一句：

- `继续，把 codex-workflows 的 recipe 映射到 A/B/C/D/E/F`
- `继续，把 LoopFlow 四个 starter loop 改成我的方法轮 loop`
- `先暂停，只保留安装状态`

