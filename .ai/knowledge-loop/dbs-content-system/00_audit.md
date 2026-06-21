# Content Scale & Boundary Audit

## Audit date

- 2026-06-20

## Current corpus size

- `.ai/knowledge-loop/` — 56 files discovered
- `.ai/research/` — 27 files discovered
- No existing dedicated `dbs-content-system/` directory found before creation

## Boundary conclusion

### In-scope as original source material

- `README.md`
- `AGENTS.md`
- `CONTEXT.md`
- `.ai/methods/ai-method-wheel.md`
- `.ai/methods/skill-repository-intake-policy.md`
- `.ai/methods/finished-project-absorption.md`
- `.ai/research/spec-kit/*`
- `.ai/research/fractals/*`
- `.ai/knowledge-loop/sources/*`
- `.ai/knowledge-loop/decisions/*`
- `.ai/knowledge-loop/frame-updates/*`
- `.ai/knowledge-loop/synthesis/*`

### Treat as secondary / derived material

- long synthesis notes
- already-absorbed decision docs
- wrapper-generated artifacts
- run reports

## Practical boundary rule

If a file already restates a concept that exists in a higher-trust source, keep it as context only.
Do not promote repeated summary language into the source pack unless it adds a new claim or decision.

## Audit verdict

- Corpus is large enough for a standalone content module.
- The content should be structured by reusable units, not by raw file dumping.
- A single directory is appropriate if the directory contains an explicit audit/source/unit/topic/draft chain.
