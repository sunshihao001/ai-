# CONTEXT.md — Shared Project Language

Use this file to preserve shared terms, domain concepts, architectural boundaries, and repeated project decisions discovered through `grill-with-docs` style questioning.

## Domain Terms
- **Hermes-Orchestrated Codex**: Hermes remains the demand/control/checker layer and invokes Codex CLI as a bounded maker worker using explicit command patterns.
- **Source Pack**: a compact Hermes-built context file used for long Codex theory generation to avoid broad uncontrolled `--add-dir` crawling.

## Core Modules
- TBD

## Existing Conventions
- Long theory generation should use `codex exec` with `--sandbox read-only`, `--output-last-message`, stdin prompt files, and usually a source pack.
- Repo landing should use a separate Codex run with explicit allowed paths, then Hermes checks diff, validation, commit, push, and PR/CI.

## Known Risks / Things Agents Often Get Wrong
- Saying “use Codex” without choosing the command shape, sandbox, output mode, and checker path.
- Letting Codex crawl huge knowledge bases for long theory tasks instead of giving it a compact source pack.
- Letting Codex act as both maker and final checker.

## Decisions That Should Not Be Re-litigated
- TBD
