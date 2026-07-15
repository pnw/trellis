---
title: "Source: Kiro Steering Docs"
type: source-capture
evidence: official-docs
description: "Official Kiro documentation for steering files, inclusion modes, AGENTS.md support, scopes, and file references."
sources:
  - "[[raw/articles/kiro-steering-docs.md]]"
related:
  - "[[designs/agent-context-portability]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
tags: [agent-context, context-engineering, kiro, agents]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
---

# Kiro Steering Docs

## Source Identity

- Raw source: [[raw/articles/kiro-steering-docs.md]]
- Source type: official documentation
- Author(s): Kiro
- Updated: 2026-02-18
- Original URL: https://kiro.dev/docs/steering/
- Scope: Kiro steering files, scopes, inclusion modes, AGENTS.md support, and steering-file references

## Core Contribution

Kiro's steering docs define a richer context-routing layer than plain AGENTS.md: workspace/global steering files, YAML frontmatter inclusion modes, manual and automatic inclusion, file-match routing, and live workspace file references.

## Key Claims

- Workspace steering lives under `.kiro/steering/`; global steering lives under `~/.kiro/steering/`.
- Workspace steering has priority over global steering when instructions conflict.
- Kiro supports AGENTS.md at workspace root or in the global steering location.
- AGENTS.md in Kiro is always included and does not support Kiro inclusion modes.
- Steering files support `inclusion: always`, `inclusion: fileMatch`, `inclusion: manual`, and `inclusion: auto`.
- `fileMatch` uses `fileMatchPattern`; `auto` uses `name` and `description`.
- Steering files can reference live workspace files with Kiro's escaped file-reference syntax, written as `#\[\[file:<relative_file_name>\]\]`.

## Implications

Kiro is the strongest of the surveyed tools for first-class conditional context routing. For cross-platform projects, Kiro steering can act as a thin router to canonical content, but its advanced inclusion modes will not transfer directly to Codex's AGENTS.md discovery or Claude's CLAUDE.md imports.

## Contribution Routing

- Creates: `[[designs/agent-context-portability]]`
- Updates: `[[wiki/agent-context/subtopics/context-files/entities/agents-md]]`
