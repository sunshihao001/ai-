# Fractals Long Theory: A-Port Boundary and C/D/E Bridge

## 1. Executive summary

本理论 note 的结论固定为：

```text
PARTIAL_ACCEPT + BRIDGE
```

`fractals` 对 AI Method Wheel 的价值不是“吸收一个运行时”或“新增一个 A-port 技能”，而是把它的递归 classify/decompose/branch-shaping 思想桥接进 Method Wheel 的逻辑端口设计中。

核心边界是：

```text
A may classify, decompose, and compare candidate branches.
A must stop before execution planning becomes implementation orchestration.
A transfers to C when the branch shape, boundary, and verification question are stable enough for theory generation.
```

换成 Method Wheel 语言：

- A-port 可以做需求分类、候选分支生成、边界拷问、路线比较、停止/转交判断。
- A-port 不可以创建 worktree、不可以调 CLI、不可以调度 batch、不可以运行 leaf task、不可以拥有 server/API execution 行为。
- C-port 接收 A 产出的稳定 branch shape、scope boundary、non-goals、verification question，然后生成理论、计划、架构、任务切片。
- D-port 才是 bounded maker execution。
- E-port 才是 checker / verification / false-completion guard。
- F/owner 只在 broad persistence-model change、baseline change、risky governance change、broad execution scope 时介入。

`fractals` 应被记录为 recursive task-orchestration reference，而不是 Method Wheel baseline runtime。

## 2. Source-grounded understanding of Fractals

### Evidence facts

基于已检查文件，`TinyAGI/fractals` 是一个 recursive agentic task orchestrator。README 明确描述它会把 high-level task 生长成 self-similar tree of executable subtasks，并在 isolated git worktrees 中运行 leaf tasks。

它有两个阶段：

```text
PLAN:
user task
→ classify atomic/composite
→ decompose composite nodes
→ recursively build task tree
→ review tree

EXECUTE:
workspace path
→ git init / worktree creation
→ batch leaf execution
→ Claude/Codex CLI execution
→ status polling / propagation
```

关键源码事实：

- `src/llm.ts`
  - 提供 `classify(task, lineage)`。
  - 提供 `decompose(task, lineage)`。
  - 使用 structured output。
  - prompt 明确要求“when in doubt, choose atomic”，避免过度拆解。
  - lineage 被传入模型，避免重复拆已经被 ancestor 限定过的范围。

- `src/orchestrator.ts`
  - `plan(task, maxDepth)` 递归构造树。
  - 达到 `maxDepth` 时强制 atomic。
  - atomic node 标为 `ready`。
  - composite node 调用 `decompose()` 生成 children。
  - 注释明确说明 planning phase only, no execution。
  - 还包含 `leaves()`、`findTask()`、`isSubtreeDone()`、`propagateStatus()`。

- `src/executor.ts`
  - leaf task 通过 Claude 或 Codex CLI 执行。
  - 执行前调用 `createWorktree()`。
  - prompt 带 lineage 和 sibling awareness。
  - Codex/Claude invocation 属于 runtime execution 行为。

- `src/workspace.ts`
  - 初始化 workspace。
  - 执行 `git init`。
  - 创建 `.worktrees/<taskId>`。
  - 可 remove worktree。

- `src/batch.ts`
  - 实现 depth-first batch。
  - breadth-first 和 layer-sequential 是 roadmap/fallback 概念。
  - batch 的语义是 execution ordering，不是需求澄清。

- `src/server.ts`
  - Hono server 暴露 `/api/decompose`、`/api/workspace`、`/api/execute`、`/api/tree`、`/api/leaves` 等接口。
  - session 是单一 in-memory session。
  - `/api/decompose` 调 `plan()`。
  - `/api/workspace` 初始化 workspace。
  - `/api/execute` 创建 batches 并执行 leaf tasks。
  - `/api/tree` 和 `/api/leaves` 用于状态读取。

- `src/types.ts`
  - `TaskKind = "atomic" | "composite"`。
  - `TaskStatus = "pending" | "decomposing" | "ready" | "running" | "done" | "failed"`。
  - `BatchStrategy = "depth-first" | "breadth-first" | "layer-sequential"`。
  - `Session.phase = "idle" | "decomposing" | "planning" | "executing" | "done"`。

### Interpretation

`fractals` 的最强方法价值在于“先构造任务树，再执行 leaf tasks”。但 Method Wheel 不能把这一整套 runtime 吸收到 A-port，因为 A-port 的职责是 intent / scope / boundary / route judgment，不是 execution orchestration。

所以应把 `fractals` 拆成两类：

```text
可吸收的思想:
classify
decompose
lineage-aware branch shaping
atomic/composite判断
branch comparison
depth limit
over-decomposition guard

不可吸收到 A 的 runtime:
worktree creation
CLI spawning
batch execution
server execution endpoints
leaf task execution
swarm behavior
```

## 3. A-port maximum safe boundary

A-port 的最大安全边界是：

```text
A-port may automatically classify an input, decompose it into candidate conceptual branches, compare those branches for risk/usefulness/verifiability, ask at most the next blocking clarification question when needed, and decide whether to stop, refine, or transfer to C.

A-port must stop before any branch becomes an executable task plan, before choosing runtime execution mechanics, before assigning leaf workers, before creating durable execution state, and before invoking tools that mutate project state.
```

更具体地说，A 可以做：

- 判断输入是 atomic 还是 composite。
- 如果 composite，生成 2-5 个 candidate branches。
- 标注 primary branch、secondary branch、risky branch、out-of-scope branch。
- 识别 missing acceptance criteria。
- 识别 missing verification question。
- 识别是否需要 B-port source evidence。
- 识别是否应进入 C-port theory/planning。
- 识别是否需要 F/owner decision。
- 产出 A→C transfer packet。

A 不可以做：

- 把 branch 转成 leaf execution queue。
- 为 branch 创建 worktree。
- 调 Claude/Codex/OpenCode CLI。
- 设置 batch strategy。
- 开启 server/API execution。
- 运行 implementation。
- 把 decomposition 视为 execution permission。
- 把“任务树已清楚”误判为“可以自动执行”。

A-port 的自动 looping 只能是 reasoning loop，不是 execution loop。它可以递归地问“这个想法是不是还需要拆？”但不能递归地派发“这个 leaf 现在由谁执行？”

## 4. A-port automatic loop shape

安全的 A-port loop 应该长这样：

```text
input
→ classify: atomic / composite / unclear
→ if unclear: ask one blocking question or route to B for evidence
→ if atomic: check acceptance + verification question
→ if composite: generate candidate branches
→ compare branches by scope, risk, dependency, verifiability
→ select route:
   - continue A if boundary still unstable
   - route to B if evidence missing
   - transfer to C if branch shape is stable
   - escalate to F if owner decision is required
→ stop
```

这个 loop 的关键是 stop condition。

推荐 stop condition：

```text
A stops when:
1. branch shape is stable enough to name primary/secondary/non-goal branches;
2. scope boundary is explicit enough to prevent accidental implementation expansion;
3. verification question is clear enough for C/E to design checks;
4. further A questions would mostly change wording, not route.
```

A-loop 最多可以做 1-2 轮自动 refinement。超过这个范围，通常说明问题不是需要更多 automatic branching，而是需要 owner decision、B-port evidence、或 C-port theory。

A-port transfer packet 应包含：

```text
- original user intent
- atomic/composite judgment
- selected branch shape
- rejected branches / non-goals
- unresolved assumptions
- acceptance criteria draft
- verification question
- risk notes
- recommended next port: B / C / F
```

这就是 A 可以从 `fractals` 借来的“树形思考”。它不是 `fractals` 的 execution tree，而是 Method Wheel 的 decision tree。

## 5. C-port responsibilities after A transfer

C-port 接收 A 的 transfer packet 后，负责把 branch shape 转成 theory、plan、architecture、contracts、tasks 的中间层。C 不是 maker，但 C 可以生成足够明确的 maker-ready documents。

C-port 应负责：

- 将 A 的 branch shape 转成 coherent theory。
- 解释为什么这些 branches 是正确边界。
- 把 candidate branches 映射到 spec / plan / tasks。
- 定义 dependency model，但不执行 dependencies。
- 定义 data/contracts/quickstart artifacts。
- 识别哪些任务应成为 D-port bounded slices。
- 设计 E-port verification strategy。
- 记录 ADR 或 Method Wheel rule 的候选文本。
- 明确哪些发现需要 flow-back 到 spec，哪些只 flow-forward 到 implementation。

C 可以吸收 `fractals` 的这些部分：

```text
recursive planning theory
atomic/composite classification
lineage-aware context
max-depth / over-decomposition guard
branch comparison
dependency-aware thinking
review-before-execution principle
```

C 不应吸收成 runtime 的部分：

```text
workspace creation
worktree management
CLI execution
batch running
server endpoint execution
status polling as runtime operation
```

C 的输出应该是 documents / plans / contracts，不是 running processes。

A→C 的合理转交点是：

```text
当 A 已经稳定了 branch shape、boundary、verification question，
但还没有进入 implementation task orchestration 时，转交 C。
```

C→D 的合理转交点是：

```text
当 C 已经把理论和计划压缩成 bounded implementation slice，
并且 D 可以在明确 scope、files、tests、acceptance criteria 下执行时，转交 D。
```

## 6. D-port and E-port boundaries

### D-port boundary

D-port 是 maker execution。它可以处理 bounded repo changes，但必须受 spec、issue、allowed paths、tests、review gates 约束。

如果未来 Method Wheel 借鉴 `fractals` 的 execution ideas，只能进入 D-port 或 D-adjacent execution harness，且仍需 E/F gates。

D-port 可拥有：

- bounded implementation。
- test-first or test-backed changes。
- isolated branch/worktree，前提是 harness 允许。
- file edits。
- dependency changes，前提是 scope 明确。
- local commands。
- PR preparation。
- maker logs。

但 D-port 不应自我扩权。它不能因为 C 生成了 branch tree，就自动决定执行全部 branches。D 执行的是 issue/spec slice，不是整个 recursive tree。

### E-port boundary

E-port 是 checker / verification。它负责判断 D 的输出是否符合 spec、acceptance criteria、tests、security/accessibility constraints、Method Wheel boundary。

E-port 可拥有：

- pre-implementation artifact review。
- post-implementation diff review。
- tests / lint / typecheck / Playwright / accessibility / security checks。
- false-completion guard。
- spec alignment verification。
- method boundary audit。
- regression capture。
- “是否 over-absorbed fractals-like runtime”的检查。

E-port 可借鉴 `fractals` 的状态思想，但只能作为 verification model：

```text
planned
ready
running
done
failed
```

在 Method Wheel 中，这些状态不能替代 tests、review、CI、human approval。状态传播只能说明过程位置，不能证明质量。

### D/E split

D 产出，E 检查。D 可以报告结果，E 不能只相信报告。E 应读取 artifacts、diffs、logs、tests，并给出 independent judgment。

这对应 Method Wheel 的 maker/checker separation，也是防止 `fractals` 被过度吸收的关键规则。

## 7. Permanent forbidden actions for A

A-port 永久禁止以下行为：

1. 创建、删除、清理、切换 worktree。
2. 初始化 workspace 或执行 `git init`。
3. 运行 leaf task。
4. 调用 Claude/Codex/OpenCode 等 CLI 执行 maker 工作。
5. 设置或运行 batch schedule。
6. 启动 server/API execution endpoint。
7. 维护 runtime session 作为执行真源。
8. 把 branch decomposition 转成 task queue 并自动派发。
9. 选择 execution provider。
10. 合并 branch、解决冲突、回写 implementation。
11. 将 experimental orchestrator runtime 提升为 Method Wheel baseline。
12. 把 `fractals` 当成 downloadable skill。
13. 用“递归拆解”绕过 spec、plan、tasks、checklist、E verification、F owner gate。
14. 在没有 B-port evidence 或 C-port theory 的情况下修改 baseline method docs。
15. 静默改变 port boundaries。

A-port 可以提出：

```text
“这里可能需要 D-port execution harness。”
```

但 A-port 不可以执行：

```text
“现在创建 worktree 并派发 leaf workers。”
```

这个差别必须永久保留。

## 8. Branching heuristics inspired by Fractals

`fractals` 的 classify/decompose prompt 有几个可借鉴的启发：

### 1. Prefer atomic when uncertain

当不确定是否应该拆，选择 atomic。过度拆解会制造 coordination overhead。

Method Wheel 规则：

```text
When in doubt, A should prefer a smaller bounded question over a larger recursive tree.
```

### 2. Split only independent concerns

只有当任务包含 2+ independent concerns 时才拆。

A-port 可问：

```text
这些分支是否真的可以独立判断、独立验证、独立推进？
```

如果答案是否，说明不该拆成多个 branches。

### 3. Keep branch count small

`fractals` decompose prompt 要求 minimum number of subtasks，最多 7，不 padding。Method Wheel 的 A-port 更应保守：默认 2-5 个 candidate branches。

推荐：

```text
2 branches: clear binary route
3 branches: normal ambiguous product/method decision
4-5 branches: broad idea exploration
>5 branches: likely needs C theory or B evidence, not more A branching
```

### 4. Use lineage to avoid repetition

lineage-aware context 的核心价值是防止重复拆 ancestor scope。

A-port transfer packet 应保留：

```text
root intent
current branch
ancestor constraints
already rejected scopes
current unresolved question
```

### 5. Depth limit

A-port 不应无限递归。推荐最大 2 层：

```text
Level 0: user intent
Level 1: candidate branches
Level 2: only for one selected branch if needed
```

超过 2 层通常进入 C-port planning。

### 6. Branch comparison dimensions

A-port 可按这些维度比较 branches：

- usefulness
- risk
- reversibility
- verification cost
- dependency uncertainty
- owner decision requirement
- implementation blast radius
- evidence gap
- Method Wheel baseline impact

### 7. Diversity without orchestration

A-port 的 branching 是 epistemic diversity，不是 worker parallelism。

```text
Good:
“这里有三个解释路线，哪一个最符合目标？”

Bad:
“这里有三个 leaf tasks，现在并发执行。”
```

## 9. Relationship to Spec Kit and existing Method Wheel

Method Wheel 已有 spec spine：

```text
constitution/governance
→ spec.md
→ clarification answers
→ plan.md
→ research/data/contracts/quickstart
→ tasks.md
→ checklists
→ E-port analyze
→ D/Codex bounded implementation
→ E-port verification
→ PR/ADR/handoff
```

`fractals` 不应替代这个 spine。它只能增强 spine 前后的某些动作。

对应关系：

```text
fractals classify/decompose
→ A clarification and route judgment

fractals recursive plan tree
→ C planning theory and task-shaping, not direct execution

fractals review-before-execute
→ Spec Kit checklist / E-port analyze

fractals leaf execution
→ D bounded implementation only after spec/tasks exist

fractals status propagation
→ E progress visibility, not quality proof

fractals batch strategy
→ D/E harness design, not A-port control
```

Spec Kit 的优势是 artifact discipline。`fractals` 的优势是 recursive branch-shaping。两者结合时，Spec Kit 必须保持主脊柱，`fractals` 只能提供分支启发。

正确整合方式：

```text
A: classify/decompose ambiguity
B: supply source evidence when needed
C: turn stable branch shape into spec/plan/tasks/checklist
D: execute bounded slices
E: verify artifacts and output
F: approve baseline/risky changes
```

错误整合方式：

```text
A: receive vague request
→ recursive decomposition
→ execution tree
→ worktrees
→ CLI workers
→ batch execution
```

这会跳过 Spec Kit spine，并把 A 变成 runtime orchestrator。

## 10. Recommended durable Method Wheel rule

建议加入 Method Wheel 的永久规则：

```text
Fractals-like Recursive Orchestration Rule

When evaluating an external recursive agent/orchestration project, Method Wheel may absorb its reasoning patterns only after separating planning semantics from execution mechanics.

A-port may classify, decompose, and compare candidate branches for intent clarification and route judgment.

A-port must stop before branch decomposition becomes implementation orchestration.

C-port owns theory, planning, dependency modeling, contracts, and task slicing.

D-port owns bounded maker execution.

E-port owns independent verification, false-completion checks, and method-boundary audit.

Execution mechanics such as worktree creation, CLI spawning, batch scheduling, server execution endpoints, leaf task execution, swarm behavior, and merge/backpropagation must never be promoted into A-port.

No fractals-like runtime becomes Method Wheel baseline without B evidence, C synthesis, E verification, and F owner approval.
```

短版 rule：

```text
Absorb recursive reasoning, not recursive execution.
```

## 11. Verification checklist

用于检查未来是否 over-absorbed `fractals`-like projects：

- [ ] 是否把 evidence facts 和 interpretation 分开记录？
- [ ] 是否明确该项目是 runtime / orchestrator / framework / skill / pattern？
- [ ] 是否确认 A 只做 classify/decompose/compare/route？
- [ ] 是否禁止 A 创建 worktree？
- [ ] 是否禁止 A 调 CLI worker？
- [ ] 是否禁止 A 调度 batch？
- [ ] 是否禁止 A 运行 leaf task？
- [ ] 是否禁止 A 维护 execution session？
- [ ] 是否有 A→C transfer rule？
- [ ] 是否有 C→D bounded slice rule？
- [ ] 是否有 E-port independent verification？
- [ ] 是否保留 Spec Kit artifact spine？
- [ ] 是否需要 F/owner approval 才能改 baseline？
- [ ] 是否记录 non-goals？
- [ ] 是否避免把 external runtime 当 downloadable skill？
- [ ] 是否避免推荐安装或运行 external runtime？
- [ ] 是否说明 logical ports 不等于 physical bot splitting？
- [ ] 是否定义 stop condition 和 max depth？
- [ ] 是否说明 status propagation 不等于 quality verification？
- [ ] 最终决策是否仍为 `PARTIAL_ACCEPT + BRIDGE`？

## 12. Open evidence gaps

当前理论足够支持 Method Wheel boundary decision，但仍有 evidence gaps：

- `/tmp/fractals/web/` 未检查。
- `/tmp/fractals/src/index.ts` 未检查。
- `/tmp/fractals/src/print.ts` 未检查。
- tests / CI / release automation 未检查。
- runtime behavior 未通过实际运行验证。
- UI 是否支持 task editing 或更复杂 review flow 未确认。
- README 中部分 roadmap 尚未实现，不应当作现有能力。
- README 和源码对 model 名称存在可能差异；这不影响 Method Wheel boundary，但不应过度引用具体 model 作为结论依据。
- batch strategy 目前只有 depth-first 实现，breadth-first 和 layer-sequential 不应被描述为已实现能力。
- single in-memory session 的限制说明它不是成熟 multi-session baseline runtime。

这些 gaps 不阻止当前结论，因为当前结论不是 runtime adoption，而是 method-level partial absorption。

## 13. Final decision

最终决定：

```text
PARTIAL_ACCEPT + BRIDGE
```

含义：

```text
Accept:
- recursive classify/decompose thinking
- atomic/composite judgment
- lineage-aware branch shaping
- branch comparison
- over-decomposition guard
- review-before-execution principle

Bridge:
- A uses branching only for clarification and route judgment
- C turns stable branch shape into theory/planning/tasks
- D handles bounded maker execution
- E handles independent verification
- F approves broad/risky baseline changes

Reject as A baseline:
- worktree creation
- CLI spawning
- batch scheduling
- leaf execution
- swarm behavior
- server/API execution ownership
- runtime promotion
```

Key boundary:

```text
A may classify, decompose, and compare candidate branches.
A must stop before execution planning becomes implementation orchestration.
A transfers to C when the branch shape, boundary, and verification question are stable enough for theory generation.
```