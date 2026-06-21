# A-Mode Regression Test Template

> Purpose: verify that A-port strong-trigger handling does not fall back to ordinary chat, repeated multiple-choice routing, or ungrounded theory.

---

## 1. Test input

Paste the owner input or compact transcript fragment:

```text
<owner input>
```

Mark whether the input contains any strong A-mode cue:

- [ ] 请按 A 端强制触发模式处理
- [ ] 请按 A 端逻辑处理
- [ ] 先不要直接给方案
- [ ] 自动拷问目标、边界、缺口、验收标准
- [ ] 必要时自动调用相关 skill
- [ ] Owner explicitly says not to split into physical bots
- [ ] Owner complains that repeated choices are too human-driven

---

## 2. Expected A-mode behavior

The response must do these before asking the owner another question:

- [ ] Infer the primary objective from repeated signals and corrections.
- [ ] State the current boundary and what is out of scope.
- [ ] Identify the current missing evidence class or reasoning gap.
- [ ] Select the smallest relevant skill family.
- [ ] If a skill name is ambiguous, report the ambiguity and choose the explicit path if known.
- [ ] Decide whether to continue A, transfer to B, transfer to C, or stop.
- [ ] Ask only one blocking question if the route cannot be inferred.

---

## 3. Failure patterns

A response fails this regression if it does any of the following:

- [ ] Asks the owner to choose A/B/C/D again without first making a routing judgment.
- [ ] Treats logical ports as a requirement to split into multiple physical bots.
- [ ] Claims a skill was invoked when it was not loaded or was ambiguous.
- [ ] Jumps to C/D execution before A has goal/boundary/verification clarity.
- [ ] Turns an external GitHub skill repo into the main branch after the owner says to focus on A-skill磨合.
- [ ] Gives only theory or “next-step suggestions” without a concrete routing judgment.
- [ ] Leaves durable method-wheel updates in the wrong repo.

---

## 4. Scoring rubric

Score each item 0/1:

```text
A. Strong trigger recognized:
B. Primary route inferred:
C. Boundary/out-of-scope stated:
D. Skill family selected or ambiguity reported:
E. Next action chosen without owner-driven choice loop:
F. Stop/transfer rule applied:
G. Durable artifact or verification path identified:
```

Pass threshold:

```text
6/7 = pass
5/7 = needs repair
0-4/7 = fail; update A-port method or trigger template
```

---

## 5. Expected response frame

```text
[Current understanding]
[Primary route inferred]
[Boundary / out of scope]
[Skill family selected]
[Missing evidence or blocking question]
[Next action]
[Regression score]
```

---

## 6. Repair action if failed

If the response fails:

1. Patch `.ai/methods/a-port-autonomous-logical-loop.md` or `.ai/templates/a-port-strong-trigger.md`.
2. Add the failing transcript fragment to this regression template or a dated test note.
3. Run `python scripts/validate-ai-method-wheel.py`.
4. Commit only the bounded repair.
