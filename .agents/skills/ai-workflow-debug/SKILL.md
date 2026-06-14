---
name: ai-workflow-debug
description: Use for bugs, failing CI, flaky tests, production issues, or unexplained behavior. Diagnose with evidence before changing code.
---

# AI Workflow: Debug

Derived from Superpowers `systematic-debugging` and Matt Pocock `diagnose`.

## Process
1. Reproduce or collect evidence.
2. State observed vs expected behavior.
3. List hypotheses ranked by likelihood.
4. Test hypotheses with the smallest probe.
5. Identify root cause.
6. Apply minimal fix.
7. Add regression test or operational check.
8. Verify and document.

## Anti-patterns
- Random code changes without reproduction.
- Treating symptoms as root cause.
- Claiming fixed without rerunning the failing check.
