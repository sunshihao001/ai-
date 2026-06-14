---
name: ai-workflow-debug
description: "Use when tests fail, behavior is broken, or production symptoms need diagnosis. Follow systematic debugging before changing code."
version: 1.0.0
author: Curated from superpowers systematic-debugging and mattpocock diagnose
license: MIT
---

# AI Workflow: Systematic Debugging

## Rule
Do not guess-fix. Diagnose first.

## Process
1. Reproduce or collect evidence.
2. State observed behavior vs expected behavior.
3. List hypotheses ranked by likelihood.
4. Add instrumentation or narrow tests if needed.
5. Identify root cause.
6. Apply the smallest fix.
7. Add regression test.
8. Verify the fix and nearby behavior.

## Output Template
```md
# Diagnosis
## Symptom
## Evidence
## Expected
## Hypotheses
## Root Cause
## Fix
## Regression Test
## Verification
```
