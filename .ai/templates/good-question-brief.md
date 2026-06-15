# Demand Grilling Brief

Use this template before writing a spec, GitHub issue, Codex handoff, or maintainer-orchestrator task when the request is vague, risky, product-facing, or requires agent-loop routing.

## 1. Original Ask

Quote or summarize the raw user request.

## 2. Improved Agent-Usable Question

```text
Given <current context/state>, for <user/operator>, change/decide <specific target>, while preserving <constraints/non-goals>. Success means <objective acceptance criteria>. Verify by <specific checks/evidence>. If blocked, ask <exact owner question>.
```

## 3. Semantic Divergence and Problem World

Use when the ask is complex, strategic, research-heavy, or about the method/workflow itself.

- problem_world:
- solution_world:
- shared_phenomena:
- concept_map_seed:
- issue_tree_seed:
- unchosen_branches:
- current_convergence_slice:

## 4. Search / Recall Plan

Do not mechanically search the user's surface words. Translate intent first.

- owner_surface_terms:
- interpreted_information_need:
- professional_concept_family:
- retrieval_failure_mode:
- query_transformation_strategy:
- search_query_variants:
- query_drift_risk:
- internal_sources_to_check:
- external_sources_to_check:
- not_applicable_reason, if no external search:

## 5. Intent and Alternatives

- True goal:
- User-proposed solution or actual goal:
- Simpler/safer alternatives:
- Recommended default:
- Why now:

## 6. Context and Constraints

- Repo/system:
- Current state:
- Existing docs/ADRs/AGENTS.md/CONTEXT.md:
- Related modules/files:
- Risky modules:
- External dependencies:
- Compatibility constraints:

## 7. Scope and Non-Goals

### In Scope

- 

### Out of Scope

- 

### Must Not Change

- 

## 8. Assumptions and Risks

- [confirmed] 
- [unconfirmed] 
- [risky] 

Risk areas to check:

- Product/user expectation:
- Permissions/authorization:
- Privacy/data exposure:
- Security/abuse:
- Accessibility:
- Operations/deploy/rollback:
- Cost/performance:

## 9. Acceptance Criteria

- [ ] 

## 10. Verification Plan

- Unit tests:
- Integration tests:
- Typecheck/lint/build:
- E2E / Playwright:
- Manual QA:
- Accessibility:
- Security:
- CI evidence:
- Live proof, if applicable:

## 11. Agent Execution Classification

- Classification: Autonomous / Needs owner / Ignored by owner
- Handoff target: more questions / spec / GitHub issue / Codex task / maintainer-orchestrator / owner decision
- Maker:
- Checker:
- Durable state location:
- Authority boundary:
  - May edit files: yes/no
  - May create branch: yes/no
  - May push branch: yes/no
  - May open PR: yes/no
  - May merge: yes/no
  - May deploy/release: yes/no
  - May access secrets/credentials: yes/no
  - May delete data/resources: yes/no
- Requires owner approval before:

## 12. Loop Stop Conditions

- Max maker/checker loops:
- Time/token/cost budget:
- Success condition:
- Stop condition:
- No-progress guard:
- Blocker brief required when:

## 13. Critique Prompts

- What assumption is weakest?
- What simpler interpretation exists?
- What is the highest-risk module or workflow touched?
- What would be unsafe to automate?
- How could an agent falsely claim success?
- What proof would convince a skeptical maintainer?
- What decision truly requires the owner?

## 14. Missing High-Value Questions

Ask the fewest questions that change scope, safety, routing, authority, or verification.

1. 
2. 
3. 

## 15. Next Stage

Ready for:

- [ ] More questions
- [ ] Spec
- [ ] GitHub issue
- [ ] Codex
- [ ] Maintainer-orchestrator
- [ ] Owner decision

Reason:
