# codex-workflows recipe → A/B/C/D/E/F 映射

## 目的

把 `codex-workflows` 视为 **Codex 执行编排层**，而不是 Hermes 的全局 skill 库。

这份映射只回答一件事：**每个 recipe 在方法轮里更适合放在哪个端口/阶段。**

## 总原则

- A 负责定题、定界、定 owner 期望。
- B 负责源包、事实、外部输入、上下文压缩。
- C 负责规格化、设计、计划、理论合成。
- D 负责实际执行、实现、落地、提交。
- E 负责验证、复核、审查、质量门。
- F 负责 owner 决策、接受、暂停、继续、归档。

`codex-workflows` 的 recipe 主要覆盖 **B/C/D/E**，A 和 F 仍然由 Method Wheel / owner 控制。

## 重点 recipe 映射

### A / B 侧

- `recipe-diagnose`
  - **主位置**：A
  - **辅助位置**：E
  - 作用：诊断问题是否成立，找出失败点、边界和真实阻塞。

- `recipe-reverse-engineer`
  - **主位置**：B
  - **辅助位置**：C
  - 作用：从现有代码里反推 PRD / Design Doc，先做 source discovery，再做文档化。

- `recipe-prepare-implementation`
  - **主位置**：C→D 之间
  - **作用**：在执行前做 readiness gate，补齐 Phase 0 / implementation readiness 缺口。
  - 这不是实现本身，而是“能不能开始实现”的门。

### C 侧

- `recipe-plan`
  - **主位置**：C
  - 作用：从 design doc 生成 work plan，必要时生成 test skeleton 的前置信息。

- `recipe-design`
  - **主位置**：C
  - 作用：把需求变成设计文档、计划文档、任务分解边界。

- `recipe-update-doc`
  - **主位置**：C→E
  - 作用：更新已有设计文档/PRD/ADR，并做一致性验证。
  - 它是“理论/文档修订 + 质量检查”的复合工具。

### D 侧

- `recipe-task`
  - **主位置**：D
  - 作用：把任务执行出来，带有 metacognitive 分析和规则选择。

- `recipe-implement`
  - **主位置**：D
  - 作用：完整实现生命周期；适合从需求到交付的主执行路径。

- `recipe-fullstack-implement`
  - **主位置**：D
  - 作用：跨前后端的完整实现编排。

- `recipe-build`
  - **主位置**：D
  - 作用：构建、修复构建、产物生成。

- `recipe-front-build`
  - **主位置**：D
  - 作用：前端构建与前端相关实现校正。

- `recipe-front-adjust`
  - **主位置**：D
  - 作用：前端调整与局部修复。

- `recipe-front-design`
  - **主位置**：C→D
  - 作用：前端设计定稿后进入实现链路。

- `recipe-front-plan`
  - **主位置**：C
  - 作用：前端范围内的计划输出。

- `recipe-add-integration-tests`
  - **主位置**：D→E
  - 作用：补集成测试 / E2E 验证资产，常作为实现与验证之间的桥。

### E 侧

- `recipe-review`
  - **主位置**：E
  - 作用：设计文档一致性、代码审查、安全审查、修正再验证。

- `recipe-front-review`
  - **主位置**：E
  - 作用：前端文档/实现的质量门与审查门。

- `recipe-add-integration-tests`
  - **副位置**：E
  - 作用：在 D 侧生成测试，在 E 侧检查测试是否真的能验证目标。

## F 侧说明

`codex-workflows` 本身不是 owner 决策层。

它可以产出：

- 可审查的 PRD
- Design Doc
- Work Plan
- Task 文件
- Review / Verification 证据

但 **F（owner 决策）** 仍然要由方法轮的控制面来完成。

也就是说：

```text
codex-workflows = 产生可验证产物
Method Wheel / Hermes = 解释这些产物是否该继续、合并、暂停、归档
```

## 一句话版

- A：`recipe-diagnose`
- B：`recipe-reverse-engineer`
- C：`recipe-design` / `recipe-plan` / `recipe-update-doc`
- D：`recipe-implement` / `recipe-task` / `recipe-build` / `recipe-fullstack-implement`
- E：`recipe-review` / `recipe-front-review` / `recipe-add-integration-tests`
- F：owner 决策，不由 recipe 自动接管

## 结论

`codex-workflows` 适合放在 Codex 执行内部，负责把 C 之后的结构化设计变成可执行、可验证、可回写的项目工件；它不应该变成 Hermes 的全局知识底座。