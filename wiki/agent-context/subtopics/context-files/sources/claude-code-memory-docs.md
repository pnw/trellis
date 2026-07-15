---
title: "Source: Claude Code Memory Docs"
type: source-capture
evidence: official-docs
description: "Official Claude Code documentation for CLAUDE.md loading, AGENTS.md imports, @ imports, path-scoped rules, and memory behavior."
sources:
  - "[[raw/articles/claude-code-memory-docs.md]]"
related:
  - "[[designs/agent-context-portability]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
tags: [agent-context, context-engineering, claude-code, agents]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
---

# Claude Code Memory Docs

## Source Identity

- Raw source: [[raw/articles/claude-code-memory-docs.md]]
- Source type: official documentation
- Author(s): Anthropic
- Original URL: https://code.claude.com/docs/en/memory
- Scope: Claude Code CLAUDE.md files, imports, path-scoped rules, AGENTS.md interop, and memory behavior

## Core Contribution

Anthropic documents Claude Code's persistent instruction system as CLAUDE.md-centered, with explicit support for importing AGENTS.md rather than reading AGENTS.md directly. It also documents imports, directory walking, `.claude/rules/`, path-scoped YAML rules, and the recommendation to keep files concise.

## Key Claims

- CLAUDE.md files are context, not enforced configuration.
- Claude Code reads CLAUDE.md, not AGENTS.md.
- A repository can create `CLAUDE.md` containing `@AGENTS.md` so Claude and other tools share the same canonical instructions.
- CLAUDE.md imports use `@path/to/import`, are expanded at launch, and can recurse up to four hops.
- Imported files still enter the context window at launch.
- Claude loads CLAUDE.md files by walking up the directory tree from the working directory.
- Claude can organize larger projects with `.claude/rules/`.
- `.claude/rules/` files can be path-scoped with YAML frontmatter using `paths`.
- Anthropic recommends targeting under 200 lines per CLAUDE.md file.

## Implications

Claude is well-suited to a thin-wrapper pattern because `CLAUDE.md` can import canonical AGENTS.md content. However, the pointer is not merely a semantic instruction; it should use Claude's import syntax. A wrapper that only says "read AGENTS.md" is weaker because it relies on agent compliance rather than documented import expansion.

## Contribution Routing

- Creates: `[[designs/agent-context-portability]]`
- Updates: `[[wiki/agent-context/subtopics/context-files/entities/agents-md]]`

