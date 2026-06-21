# A-Port Autonomous Logical Loop

> Status: v0.1  
> Purpose: define the corrected A/B/C operating mode for the AI Method Wheel: logical ports inside one control plane, strong A-mode trigger, automatic skill routing, and evidence-first transfer to B/C.

---

## 1. Core correction

Do not treat A/B/C as a requirement to split into multiple physical bots.

The default operating model is:

```text
one Hermes/control-plane session
→ logical A/B/C stages
→ explicit skill routing
→ durable repo/GitHub artifacts
```

Only split into multiple bots, profiles, or conversations after the owner explicitly chooses a physical separation model.

---

## 2. Why the previous behavior failed

When a user says “use A-port” but the runtime has no strong trigger, the assistant may stay in ordinary chat mode:

```text
user gives broad problem
→ assistant asks another multiple-choice question
→ user makes a choice
→ assistant asks again
→ skill stack never really takes over
```

This is a control-plane failure, not a multi-port design failure.

The fix is a strong A-mode trigger plus an anti-choice-loop rule.

---

## 3. Strong A-mode trigger

When the owner says any of the following:

```text
请按 A 端强制触发模式处理
请按 A 端逻辑处理
先不要直接给方案
先自动拷问目标、边界、缺口、验收标准
必要时自动调用相关 skill
```

then enter A-mode immediately.

A-mode means:

```text
Raw intent
→ goal / boundary / gap / acceptance criteria
→ skill route
→ current judgment
→ next smallest question or transfer
```

---

## 4. A-mode must not become owner-driven choice loops

A-mode should not repeatedly hand routing back to the owner.

Bad pattern:

```text
Which one do you choose: A/B/C/D?
Which one now?
Which one next?
```

Correct pattern:

```text
1. infer the primary objective from repeated signals and corrections
2. name the boundary and protected constraints
3. identify the missing evidence class
4. select the smallest relevant skill family
5. ask only the next blocking question if the route cannot be inferred
```

The owner may still choose, but the A-port must first provide a routing judgment.

---

## 5. Default A skill families

A-port owns intent, boundary, route, and acceptance criteria.

Default A skill family:

```text
dbs-good-question
+ brainstorming
+ grill-me
+ grill-with-docs
+ dbs-deconstruct
+ dbs-goal
+ dbs-decision
```

Use the smallest relevant subset; do not load every skill mechanically.

---

## 6. A/B/C logical split

### A = intent-to-spec control gate

A turns natural language into a professional research/execution question:

```text
Raw intent → Operational question → Routed execution contract
```

A outputs one of:

```text
Demand Grilling Brief
Routing Brief
Search Strategy Request to B
Theory Task Brief to C
Owner Decision Brief to F
```

### B = evidence and source compression

B turns external material into a source pack:

```text
articles / GitHub repos / docs / prior context
→ source list
→ core claims
→ relevant evidence
→ absorb / reject / unknown
```

### C = theory / plan package

C uses A+B to produce either:

```text
research-state theory frame
or
execution-state plan / spec / issue package
```

---

## 7. A/B/C stop rule

Stop the A/B/C loop when the route is mature enough:

```text
1. Goal, boundary, solution shape, and verification are at least 3/4 actionable.
2. Two consecutive rounds add no meaningful information.
3. After 2–3 rounds, force a review: transfer, stop, or ask one blocking question.
4. If further questioning changes only details, not route, transfer instead of looping.
```

Default transfer:

```text
A → B when evidence/source compression is missing.
A/B → C when theory or execution package is ready to synthesize.
C → D only after a bounded repo-landing task exists.
D → E for objective verification.
F only for owner-level risk/permission decisions.
```

---

## 8. Fractals-style A-port boundary

A may borrow recursive classify/decompose/branch-shaping ideas from Fractals-like orchestration systems, but only as a reasoning pattern.

Use `.ai/templates/a-port-fractal-boundary-rule.md` when an idea needs A-port diversity or recursive branching.

Fixed boundary:

```text
A may classify, decompose, and compare candidate branches.
A must stop before execution planning becomes implementation orchestration.
A transfers to C when the branch shape, boundary, and verification question are stable enough for theory generation.
```

Forbidden in A:

```text
worktree creation
leaf execution
CLI worker spawning
batch scheduling
server/API execution ownership
```

A creates an A→C transfer packet, not a maker queue.

---

## 9. External skill repos during A-mode

External GitHub skill repos are not automatically adopted.

A must first classify them as:

```text
ADOPT          use directly with minimal change
BRIDGE         wrap or translate into this method wheel
MERGE          combine with an existing internal skill/module
PATTERN_ONLY   absorb only the underlying pattern
REJECT         do not use
WATCH          keep as learning reserve, no baseline change yet
```

If the owner says “do not do this repo now; focus on A-skill磨合,” treat the repo as a deferred B-source candidate, not the current main branch.

---

## 10. Skill invocation ambiguity rule

A-mode must not pretend a skill ran.

If a skill name is ambiguous, missing, or unavailable, the response must say so and then choose the explicit known path only if the local convention is already known.

Example:

```text
dbs-good-question is ambiguous in this profile.
Use software-development/dbs-good-question for the AI Method Wheel A-port route.
```

This is not a failure to route; it is the correct routing behavior. Silent fallback is the failure.

---

## 11. Regression testing

Use `.ai/templates/a-mode-regression-test.md` when A-mode behavior drifts.

A response fails the A-mode regression if it:

```text
asks another A/B/C/D choice before making a routing judgment
claims a skill was invoked when it was ambiguous or not loaded
treats logical ports as physical bot splitting
jumps to C/D execution before A has goal/boundary/verification clarity
turns deferred external GitHub skill repos into the main branch after owner correction
```

Pass threshold: 6/7 on the regression rubric.

---

## 12. Replay-first repair after A-mode drift

When the owner says “继续打磨”, “可以”, or approves the previous repair direction after an A-mode failure, default to replay-first repair:

```text
1. do not ask a new broad A/B/C/D choice question
2. pick the most recent drift as the regression sample
3. write a replay note or test artifact
4. score the expected response against `.ai/templates/a-mode-regression-test.md`
5. patch method/template files only if a rule gap appears
6. verify and commit only the bounded repair
```

If the replay target is genuinely unknown, ask one blocking question: “which previous drift should be replayed?”

---

## 13. Evolutionary knowledge absorption

A-mode is not a static prompt. It must preserve loop evolution:

```text
owner correction / failed response / external source / replay result
→ evolution log
→ A absorption decision
→ B Source Pack if evidence is missing
→ C synthesis only after evidence is adequate
→ D/E bounded repo update and verification
→ updated baseline / next gap
```

Use `.ai/templates/a-mode-evolution-log.md` when a lesson may update the method wheel.

A-mode should distinguish:

```text
session correction      = useful replay evidence, not automatically a baseline change
external knowledge      = B-source candidate, not automatically adopted
accepted rule           = durable method/template/skill update after A decision and E verification
skill runtime feedback  = candidate skill patch or routing rule
```

Protected rule:

```text
save / restore / report can preserve and summarize state, but they do not replace git history, E-port verification, or F/owner decisions.
```

---

## 14. Output shape for A-mode

Each A-mode turn should use this compact structure:

```text
[Current understanding]
[Primary route inferred]
[Boundary / out of scope]
[Skill family invoked or selected]
[Missing evidence or blocking question]
[Next action: continue A / transfer B / transfer C / stop]
```

If the route is inferable, do not ask a multiple-choice question just to avoid deciding.

---

## 15. One-line rule

```text
A/B/C are logical stages inside one control plane; A-mode must infer, route, and invoke skill families autonomously before asking the owner for another choice.
```
