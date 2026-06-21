# C-port Prompt: Detailed Theory for LoopFlow + codex-workflows Integration

You are the C-port theory synthesizer for the user's AI Method Wheel.

## Context

The owner is a non-professional AI enthusiast. They do not want every external skill or workflow repository to be abstractly absorbed into the Method Wheel. They want external finished repositories/products to be inspected, installed, and placed into the correct runtime surface when appropriate.

The owner corrected a recurring failure mode:

- Bad behavior: seeing a workflow repo and immediately summarizing its “bottom-layer logic” into the Method Wheel.
- Desired behavior: first inspect the repo's own installation commands, generated files, CLI commands, runtime assumptions, and target surface; then decide how to install/use it harmoniously with the existing A/B/C/Bridge workflow.

Two repositories were inspected and installed/adapted in the Method Wheel repo:

1. `https://github.com/faisalishfaq2005/loopflow`
2. `https://github.com/shinpr/codex-workflows`

Local target repo:

`C:\Users\Administrator\AppData\Local\hermes\profiles\cangwei\home\repos\ai-`

## Evidence from installation

Local environment:

- Node: `v22.22.3`
- npm: `10.9.8`
- Codex CLI available
- Claude Code CLI not found in PATH
- Git available

Commands executed:

```bash
npx codex-workflows install
npx @loopflow/cli init
npx codex-workflows status
npx @loopflow/cli validate
npx @loopflow/cli run test-and-fix --dry-run
```

Observed results:

- `codex-workflows` installed v0.7.0.
- Install reported `.agents/ — 72 files`, `.codex/ — 25 files`, total 97 files installed.
- Status reported 116 managed files.
- LoopFlow initialized `.loopflow/loops/debt-audit.yaml`, `docs-sync.yaml`, `release-check.yaml`, `test-and-fix.yaml`.
- LoopFlow validation passed.
- LoopFlow dry-run displayed maker/checker prompts and `VERDICT: PASS/FAIL` gate format.
- `.gitignore` was updated for `.loopflow/worktrees/`, `.loopflow/memory/`, `.loopflow/runs/`.

## Source facts to preserve

### LoopFlow

- Package: `@loopflow/cli`
- Binary: `loopflow`
- Requirements: Node 18+, Claude Code installed/authenticated for real runs.
- Commands:
  - `npx @loopflow/cli init`
  - `npx @loopflow/cli validate [name]`
  - `npx @loopflow/cli run <name> --dry-run`
  - `npx @loopflow/cli run <name>`
- Generated surface: `.loopflow/loops/*.yaml`, memory/run/worktree data during real runs.
- Theory: maker/checker separation, verification gates, budgets, iteration caps, memory persistence, optional worktree isolation.

### codex-workflows

- Package: `codex-workflows`
- Binary: `codex-workflows`
- Requirements: Node >= 22, Codex CLI.
- Commands:
  - `npx codex-workflows install`
  - `npx codex-workflows status`
  - `npx codex-workflows update --dry-run`
  - `npx codex-workflows update`
- Generated surface: `.agents/skills/`, `.codex/agents/`, managed-file manifest.
- Codex usage: `$recipe-*` invocations inside Codex CLI.
- Theory: requirements → design → task decomposition → TDD implementation → quality checks; subagent context separation; traceable artifacts.

## Required output

Write a detailed Markdown theory document to:

`.ai/external-workflows/loopflow-codex-workflows-c-port-theory.md`

The document must be in Chinese and contain:

1. **核心结论**
   - Do not absorb every repo's ideas into Method Wheel by default.
   - Installation-first, runtime-surface-first, then theory placement.

2. **三层关系**
   - Method Wheel / Hermes = A-port control and owner-facing governance.
   - codex-workflows = Codex-side execution orchestration.
   - LoopFlow = optional loop runner / maker-checker gate / budgeted retry layer.

3. **为什么不应该安装成 Hermes 全局 skill**
   - Explain that global skill installation would confuse the control plane, Codex execution plane, and LoopFlow runtime plane.
   - Explain that installing into target repo is different from copying all workflows into Hermes.

4. **A端判断流程**
   - Raw external repo link → inspect install surface → inspect runtime assumptions → check local prerequisites → choose target surface → dry-run/sandbox → install → verify → write placement rule.

5. **环节定位**
   - A/B/C/Bridge/D/E/F mapping for each tool.
   - Codex-workflows placement: after A/B/C, before D/E, inside Codex execution.
   - LoopFlow placement: C defines loop goal/gate; D/LoopFlow executes; E verifies; F/Owner decides.

6. **运行规则**
   - When to use codex-workflows.
   - When to use LoopFlow.
   - When not to use either.

7. **当前安装状态**
   - Include exact installed paths and verification results.
   - Note that LoopFlow real execution requires Claude Code, which is not currently found.

8. **给未来 AI 的底层提示修正规则**
   - Replace “external repo → abstract absorption” with “external repo → install-surface audit → runtime placement → sandbox install → placement rule”.

9. **Owner next-step guidance**
   - Give the non-professional owner simple reply options, such as:
     - “继续，把 codex-workflows 的 recipe 映射到 A/B/C/D/E/F”
     - “继续，把 LoopFlow 四个 starter loop 改成我的方法轮 loop”
     - “先暂停，只保留安装状态”

## Constraints

- Do not fabricate commands or results.
- Distinguish installed-now, initialized-now, dry-run-only, and blocked-by-missing-Claude-Code.
- Keep A as the dominant front door.
- Keep bridge-over-build: use finished repo/project surfaces where appropriate, do not rebuild them as internal theory.
