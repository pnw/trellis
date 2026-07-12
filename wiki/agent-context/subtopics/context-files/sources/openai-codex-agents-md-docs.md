---
title: "Source: OpenAI Codex AGENTS.md Docs"
type: source-capture
evidence: official-docs
description: "Official OpenAI documentation for Codex AGENTS.md discovery, precedence, override files, byte limits, and fallback filenames."
sources:
  - "[[raw/articles/openai-codex-agents-md-docs.md]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
tags: [agent-context, context-engineering, codex, agents]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
---

# OpenAI Codex AGENTS.md Docs

## Source Identity

- Raw source: [[raw/articles/openai-codex-agents-md-docs.md]]
- Source type: official documentation
- Author(s): OpenAI
- Original URL: https://developers.openai.com/codex/guides/agents-md
- Scope: Codex AGENTS.md discovery, precedence, overrides, fallback filenames, and verification

## Core Contribution

OpenAI documents Codex's AGENTS.md discovery chain: global files, project-root-to-working-directory discovery, override files, configurable fallback filenames, and a default combined instruction limit.

## Key Claims

- Codex reads AGENTS.md files before work begins.
- At global scope, Codex reads `AGENTS.override.md` if present, otherwise `AGENTS.md`.
- At project scope, Codex checks each directory from project root to working directory.
- In each project directory, Codex checks `AGENTS.override.md`, then `AGENTS.md`, then configured fallback filenames.
- Codex includes at most one instruction file per directory.
- More local files appear later in the concatenated prompt and override earlier guidance by order.
- The default combined instruction cap is `project_doc_max_bytes = 32 KiB`.
- Alternate instruction names require `project_doc_fallback_filenames`.

## Implications

Codex can participate in cross-platform context if AGENTS.md is canonical. It can also be configured to read alternate canonical filenames, but that requires user or project Codex configuration; an unconfigured `KIRO.md`, `STEERING.md`, or `.kiro/steering/*.md` file is invisible to Codex's documented discovery path.

## Contribution Routing

- Creates: `[[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]]`
- Updates: `[[wiki/agent-context/subtopics/context-files/entities/agents-md]]`

