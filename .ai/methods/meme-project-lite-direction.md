# Meme Project Lite Direction — Simple Professionalization Layer

This method-wheel repository is a workflow source/template repository. The user's real business project is a meme/token research project, not an AI-workflow research project and not a general programming project.

## Core Positioning

For the meme project, the goal is not to build the most complete agent operating system. The goal is:

```text
natural-language intuition
→ professional question framing
→ external source search / source pack
→ evidence-based research note
→ simple decision / next task
→ lightweight repo memory
```

The user is not a professional AI researcher or programmer. The workflow must therefore make professional methods usable through ordinary natural language, without forcing the user to operate a complex engineering system.

## Direction Adjustment

Use this repository as the main method source, but simplify it when applying it to the meme project:

- Keep the `ai-` workflow as the practical base: AGENTS.md, CONTEXT.md, research notes, specs/tasks, QA/checklist, Codex handoff when needed.
- Treat `-xunhuan` as an idea source, not the main runtime. Borrow only simple loop ideas: target, acceptance, state, stop gate, handoff, verification.
- Prefer files and short templates over many roles, many agents, or heavy protocols.
- Codex should appear only when there is a concrete repo/file/code execution task. Most meme-project work is research, synthesis, judgment support, and documentation.

## Simplicity Principle

Keep the workflow as simple as possible while preserving useful function:

```text
少概念 / 少文件 / 少角色 / 少循环
但保留：目标、证据、风险、停止点、下一步
```

Do not add complexity merely because it sounds more professional. A workflow is only useful if the user can repeatedly operate it through natural-language requests.

## Recommended Meme Project Flow

### 1. User Natural-Language Input

The user may start with a rough idea, market intuition, token name, narrative, screenshot, or question.

The assistant should translate it into a professional research question:

- What is being evaluated?
- Why does it matter for the meme project?
- What evidence would support or falsify it?
- What output should be produced?
- What should be explicitly out of scope?

### 2. Source Pack

For external knowledge tasks, first produce a compact source pack rather than jumping to conclusions.

A source pack should contain:

- source URL / title / date when available;
- short factual summary;
- key terms explained in plain language;
- relevance to the meme project;
- reliability caveats;
- facts vs interpretation clearly separated.

### 3. Research Note

Then convert the source pack into a research note:

- core judgment;
- supporting evidence;
- opposing evidence / counterexamples;
- uncertainty and risks;
- what a non-professional user should understand;
- concrete next step.

### 4. Decision / Task

Only when there is a clear action, convert the note into a small task:

- write/update a project doc;
- collect specific data;
- build a simple script or dashboard;
- create a candidate/watch/reject list;
- prepare a Codex handoff for file/code work.

### 5. Verification and Stop

Every task should have a small stop rule:

```text
Done when: <specific file/output exists and answers the question>
Stop if: evidence is insufficient, sources conflict, or human judgment is needed
Human decision needed: <exact question>
```

## Lightweight Project Structure

For a target meme project repository, prefer this small structure before adding heavier method-wheel assets:

```text
AGENTS.md
CONTEXT.md
README.md
research/
  source-packs/
  market-notes/
  theory-notes/
decisions/
specs/
tasks/
outputs/
.loop-lite/              # optional; use only for repeated or multi-step work
  TARGET.md
  ACCEPTANCE.md
  STATE.md
  HANDOFF.md
```

`.loop-lite/` is optional. Do not introduce it for one-off research notes.

## Relationship to the Full Method Wheel

Use the full method wheel only when the task justifies it:

| Situation | Use |
|---|---|
| Rough meme/token idea | Brainstorm/grill-lite + source pack |
| External professional research | Source pack + research note |
| Project strategy document | Spec-lite + decision note |
| Code/file automation | Codex issue handoff |
| Repeated maker/checker iterations | Loop-lite or full loop orchestrator |
| GitHub PR/CI work | Full GitHub-backed method |

## Pitfalls to Avoid

- Turning the meme project into an AI-workflow research project.
- Copying the whole method repository into the business repo.
- Adding many agents/ports before there is a repeatable bottleneck.
- Asking the user to understand professional jargon before helping them.
- Treating AI-generated conclusions as facts without sources.
- Letting research continue forever without a stop rule.
- Using Codex for vague thinking work; use Codex for bounded execution.

## Success Definition

This direction succeeds if the user can say something informally like:

> 我想看看这个 meme 叙事有没有潜力。

and the system reliably turns it into:

1. a clear professional question;
2. a compact source pack;
3. a research note with evidence and risks;
4. a simple decision or next task;
5. durable project files that can be reused later.
