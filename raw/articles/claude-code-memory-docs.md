---
title: "Claude Code Docs: How Claude Remembers Your Project"
source: https://code.claude.com/docs/en/memory
retrieved: 2026-07-06
authors: Anthropic
published: unknown
updated: unknown
---

Claude Code uses CLAUDE.md files and auto memory to carry knowledge across sessions. CLAUDE.md files are human-written instructions for a project, user, or organization. Auto memory is written by Claude from corrections and preferences.

Claude treats CLAUDE.md and auto memory as context rather than enforced configuration. Anthropic recommends using hooks when a behavior must be blocked rather than merely requested.

CLAUDE.md files can live at managed-policy, user, project, and local scopes. Project CLAUDE.md can be placed at `./CLAUDE.md` or `./.claude/CLAUDE.md`; private local project preferences can live in `./CLAUDE.local.md`.

Claude loads CLAUDE.md files by walking up the directory tree from the working directory. CLAUDE.md and CLAUDE.local.md files in the hierarchy above the working directory load in full at launch. CLAUDE.md files under subdirectories load on demand when Claude reads files in those subdirectories.

Claude supports imports inside CLAUDE.md using `@path/to/import`. Imports are expanded and loaded into context at launch with the importing file. Relative imports resolve relative to the file containing the import. Imports can recursively import other files up to four hops.

Claude Code reads CLAUDE.md, not AGENTS.md. Anthropic recommends creating a CLAUDE.md that imports AGENTS.md when a repository already uses AGENTS.md for other coding agents. A symlink from CLAUDE.md to AGENTS.md also works where symlinks are practical.

For larger projects, Claude supports `.claude/rules/` files. Rules can be unconditional or path-scoped with YAML frontmatter using a `paths` field. Path-scoped rules load only when Claude is working with matching files, reducing noise and context usage.

Anthropic recommends keeping each CLAUDE.md under 200 lines, making instructions specific and concise, using markdown structure, and removing contradictory or stale rules.

