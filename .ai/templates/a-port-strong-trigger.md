# A-Port Strong Trigger Template

Use this when the owner wants A-port to take over demand excavation without splitting into physical bots.

```text
请按 A 端强制触发模式处理。

现在先不要直接给方案，也不要先进入 B/C/D/E/F。
请先自动拷问我的目标、边界、缺口、验收标准。
如果当前信息不足，请继续追问。
如果需要补信息，请自动调用相关 skill，而不是只靠自然语言问答。

请遵守 A/B/C 收束规则：
目标、边界、方案、验证四项中至少 3 项达到可执行级别；
连续 2 轮没有新增有效信息就停；
最多循环 2~3 轮后强制复盘是否该转端；
如果继续追问只会改细节、不改路线，就停止循环。
```

## Runtime interpretation

When this trigger appears, the assistant should:

1. Treat A/B/C as logical roles inside the same control plane.
2. Avoid repeated multiple-choice routing loops.
3. Infer the primary route from the user’s repeated signals.
4. Select the smallest relevant skill family.
5. Ask only the next blocking question if needed.
6. Transfer to B only when evidence/source compression is missing.
7. Transfer to C only when synthesis/theory/execution packaging is ready.

## Minimal response frame

```text
[Current understanding]
[Primary route inferred]
[Boundary / out of scope]
[Skill family selected]
[Missing evidence or blocking question]
[Next action]
```
