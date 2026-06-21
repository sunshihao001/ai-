# LoopFlow starter loops → 方法轮化映射

## 目的

把 LoopFlow 的四个 starter loop 改成更贴合用户方法轮的循环入口。

LoopFlow 不是要替代 A/B/C/D/E/F，而是要把**循环控制、gate、budget、memory、worktree** 放在正确的位置。

## 映射原则

- LoopFlow 不承担 owner 决策。
- LoopFlow 不替代 Hermes A 端。
- LoopFlow 只负责把循环做稳：谁做、谁审、什么时候停、怎样回写。

## 四个 starter loop 的建议定位

### 1. A-port demand loop

旧文件：`debt-audit.yaml`

新 name：`a-port-demand-gate`

定位：

- **主阶段**：A
- **目标**：把模糊请求收束成可执行需求 brief
- **输出**：目标、边界、缺口、非目标、验收条件、下一阶段
- **gate**：只要 brief 还在发散、还在自说自话、还没形成可验证问题，就不 PASS

### 2. B-source pack sync loop

旧文件：`docs-sync.yaml`

新 name：`b-source-pack-sync`

定位：

- **主阶段**：B
- **目标**：把外部 repo、文档、链接、安装信息、事实证据压成 source pack
- **输出**：来源清单、安装面、运行面、缺失项、证据边界
- **gate**：只要来源不齐、证据边界不清、还在靠猜测，就不 PASS

### 3. C-theory synthesis loop

旧文件：`release-check.yaml`

新 name：`c-theory-synthesis`

定位：

- **主阶段**：C
- **目标**：把 A/B 的边界与 source pack 合成为可交付理论、方案或内容工程正文
- **输出**：结构化理论、端口映射、归位规则、未决问题、下一轮提示词
- **gate**：只要理论里混入未经验证的安装/运行声称，就不 PASS

### 4. E-verification gate loop

旧文件：`test-and-fix.yaml`

新 name：`e-verification-gate`

定位：

- **主阶段**：E
- **目标**：验证实现、安装、文档、工作流修改是否真的成立
- **输出**：证据、diff、命令、失败点、是否需要返工
- **gate**：只要没有真实命令输出、没有 diff 验证、没有独立复核，就不 PASS

## 为什么这样改

因为用户的真实工作方式是：

```text
A 端先定题
B 端拿来源
C 端出理论
D 端落地执行
E 端做证据门
F 端做 owner 决策
```

LoopFlow 的 starter loops 如果还停留在通用 tech-debt / docs-sync / release-check / test-and-fix，就太像“通用运维 loop”，不够贴合用户的 A/B/C 工作方式。

把它们改成方法轮化命名后，LoopFlow 更像一个**循环控制器**，而不是一个抽象的通用自动化工具。

## 推荐执行关系

- `a-port-demand-gate`：A 端的需求门
- `b-source-pack-sync`：B 端的来源压缩门
- `c-theory-synthesis`：C 端的理论合成门
- `e-verification-gate`：E 端的真实证据门

D 端执行不要放进 LoopFlow 的默认 starter loop 里，而应交给 `codex-workflows` 或其他明确执行器。

## 一句话版

- A：需求门
- B：source pack 门
- C：理论合成门
- E：证据验证门

LoopFlow 的任务，是把这些门变成可重复、可记忆、可预算控制的循环。