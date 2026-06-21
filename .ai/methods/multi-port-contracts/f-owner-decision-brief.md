# F端 Owner Decision Brief Template v0.1

F端不是执行端。F端是 Owner 决策门。

## 1. Owner 唯一核心

```text
只决定端口和机器不能替你负责的事情：方向、权限、风险阶段门、合并、是否进入下一阶段。
```

## 2. Owner 应该决策

```text
1. 是否继续这个方向？
2. 是否允许进入更高风险阶段？
3. 是否允许改特定路径/仓库/权限？
4. 是否合并 PR？
5. 是否从 research_only 进入 paper/live？
6. 哪个方案在商业/战略上更优？
```

## 3. Owner 不应该被问

```text
不要问“下一步怎么办”但不给证据。
不要把端口能自动判断的问题丢给 Owner。
不要让 Owner 阅读大量原始资料。
不要让 Owner 替 E端做验证。
```

## 4. 固定模板

```md
# Owner Decision Brief

## 1. 当前状态

## 2. 已完成证据

## 3. 当前卡点

## 4. 需要 Owner 决策的问题

## 5. 可选方案
### Option A
- 做什么：
- 好处：
- 风险：
- 后果：

### Option B
- 做什么：
- 好处：
- 风险：
- 后果：

## 6. 推荐方案

## 7. 如果 Owner 不回复，默认安全动作

## 8. 明确禁止动作
```

## 5. 完成标准

```text
Owner 只需要选择 approve/reject/option/access/merge，不需要重新理解全部上下文。
```
