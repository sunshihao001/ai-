# Source Note — Yanhua: Design Loops, Not Prompts

## Metadata

- Source ID: 2026-06-17-yanhua-design-loops-not-prompts
- Title: 设计循环，而不是写提示词
- Author: Yanhua (@yanhua1010)
- URL: https://x.com/yanhua1010/status/2066456682725888317
- Captured at: 2026-06-17
- Source type: social article / practitioner commentary
- Quality level: S3, references Addy Osmani's Loop Engineering article
- Processing status: extracted

## Why this source matters

This source directly states the transition from Harness Engineering to Loop Engineering: people should stop acting as manual prompt writers and start designing the loops that prompt and coordinate agents. It reinforces the user's direction that humans should only guide broad goals while AI leads cyclic execution.

## Core claims

1. Harness Engineering was a transition: humans stop writing code directly and design the track agents run on.
2. Loop Engineering goes further: humans do not manually prompt agents turn-by-turn; they design the loops that prompt agents.
3. Peter Steinberger and Boris Cherny both frame the new work as designing loops, not prompts.
4. The point is not to become a passive button-presser; the operator still remains an engineer responsible for loop design and judgment.
5. The referenced article is Addy Osmani's "Loop Engineering".

## Evidence / examples

- Search result excerpt: "搭的时候记着，你是奔着继续当工程师去的，不是奔着当那个只负责按启动键的人。"
- Search result excerpt from Yanhua profile: Loop Engineering arose from Peter Steinberger's sentence that you should design loops that prompt coding agents; Boris Cherny similarly says he lets loops prompt Claude and decide next steps.
- Yanhua explicitly references Addy Osmani, "Loop Engineering", 2026-06-07.

## Concepts extracted

| Concept | Explanation | Evidence strength | Candidate target |
| --- | --- | --- | --- |
| Design loops, not prompts | Human role shifts from manual prompting to loop design. | S3 + Addy S2 | ai-method-wheel / A-port |
| Harness → Loop transition | Harness is the environment; loop is the recurring controller over agents. | S3 + Addy S2 | loop-orchestrator docs |
| Engineer, not button-presser | Humans still own judgment, design, risk and review. | S3 | owner/A-port principles |
| Loop prompts agents | The system prompts agents and decides next step rather than user micromanagement. | S3 + Addy S2 | A-port control plane |

## Fit to current Knowledge Frame

| Current frame module | Fit | Notes |
| --- | --- | --- |
| A-port Goal Engineering & Loop Control | Strong | A becomes loop designer/control plane. |
| Multi-port loop agents | Strong | Loops can prompt B/C/D/E ports instead of the user. |
| Human Owner role | Strong | Owner remains direction/risk judge, not per-step prompter. |
| Knowledge Loop | Strong | Learning updates should be loop-managed, not ad hoc. |

## Risks / caveats

- This is a social interpretation of Addy's article; use Addy/primary sources for stronger claims.
- Avoid reducing the human role too far; the source explicitly warns against becoming only a start-button operator.

## Recommended decision

PARTIAL_ACCEPT

Absorb the human-role framing: AI can lead cyclic execution, but the human/owner remains the engineer of goals, boundaries, risk, and review.

## Raw excerpt / summary

Visible X excerpt: the article title is "设计循环，而不是写提示词". It says Harness Engineering suggested humans would design the track agents run on; Loop Engineering is a further step. The search excerpt ends with the warning: build loops as someone who intends to remain the engineer, not merely the person pressing go.
