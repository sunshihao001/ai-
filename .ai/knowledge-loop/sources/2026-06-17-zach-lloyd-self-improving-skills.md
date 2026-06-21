# Source Note — Zach Lloyd: Self-Improvement Loop for Skills

## Metadata

- Source ID: 2026-06-17-zach-lloyd-self-improving-skills
- Title: How to build a self-improvement loop for your Skills
- Author: Zach Lloyd (@zachlloydtweets), Warp
- URL: https://x.com/zachlloydtweets/status/2066908445425496348
- Captured at: 2026-06-17
- Source type: X article / GitHub demo / practitioner implementation
- Quality level: S1/S2 because the article links concrete GitHub workflows and skill files
- Processing status: extracted via fxtwitter article API and corroborated with raw GitHub files

## Extraction caveat

The normal X page exposed only a t.co article link. The article content was extracted through `https://api.fxtwitter.com/status/2066908445425496348`. The linked demo files were also extracted from GitHub raw URLs.

## Why this source matters

This source gives a concrete pattern for self-improving agent skills: an inner loop applies a skill to real work; an outer scheduled loop reviews feedback from past runs and proposes a diff to improve the skill.

## Core claims

1. A loop can improve the quality of an agent Skill over time from external feedback.
2. The inner loop applies the Skill to real tasks and records interactions in files, traces, Slack, GitHub, etc.
3. The outer loop runs on a schedule, observes inner-loop runs, detects feedback, and proposes a diff to the Skill file.
4. Human feedback can be a strong signal; automated graders can substitute when the goal is clear.
5. Skills are files, so improvements should be made as reviewable diffs/PRs.

## Corroborating implementation

Linked demo files confirm the pattern:

- `triage-issue/SKILL.md` classifies issues into exactly one bucket: `ready-to-implement`, `needs-info`, or `duplicate`, posts a versioned marker comment, and asks for reactions/corrections.
- `triage-new-issues.yml` runs the triage skill on every newly opened GitHub issue via `warpdotdev/oz-agent-action`.
- `improve-triage-skill/SKILL.md` searches recent triage decisions, collects reactions, replies, label drift, duplicate signals, synthesizes generalizable lessons, and opens a PR to update the skill only when evidence is strong.

## Concepts extracted

| Concept | Explanation | Evidence strength | Candidate target |
| --- | --- | --- | --- |
| Inner/outer loop | Inner loop uses a skill; outer loop improves the skill. | S1/S2 | self-improving skill loop template |
| Versioned marker comments | Outputs include hidden markers so future improvement loops can find them. | S1 | runtime-loop-state / feedback capture |
| Human correction as signal | Maintainer relabels/comments are strong feedback. | S1 | F/E feedback weighting |
| Generalizable lessons only | Do not update skills from one-off cases or weak/conflicting signals. | S1 | protective knowledge-update loop |
| PR-based skill updates | Skill changes are diffs/PRs, not silent prompt mutation. | S1 | D/E review gate |

## Fit to current Knowledge Frame

| Current frame module | Fit | Notes |
| --- | --- | --- |
| Skills as procedural memory | Strong | Confirms skills should be files that can be improved by diff/PR. |
| Protective knowledge update | Strong | Outer loop must require strong/generalizable signals before editing. |
| F-owner feedback | Strong | Human correction can be treated as high-quality ground truth. |
| E verification | Strong | Feedback weighting and PR review protect against bad skill updates. |
| Multi-port method | Strong | Inner loop maps to D/E execution; outer loop maps to A/B/E/D skill-improvement cycle. |

## Risks / caveats

- Do not let an outer loop silently mutate core skills or baseline prompts.
- Human feedback is strong but still contextual; require generalizable lessons before updating.
- Avoid treating absence of feedback as strong positive evidence.

## Recommended decision

ACCEPT_WITH_GUARDRAILS

Adopt the inner/outer self-improvement loop as a template for improving method-wheel skills and port prompts, but require A/E protection gates and PR/diff review before promotion.
