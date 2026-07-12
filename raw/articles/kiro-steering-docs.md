---
title: "Kiro Docs: Steering"
source: https://kiro.dev/docs/steering/
retrieved: 2026-07-06
authors: Kiro
published: unknown
updated: 2026-02-18
---

Kiro steering files give Kiro persistent workspace knowledge through Markdown files. Workspace steering lives under `.kiro/steering/`; global steering lives under `~/.kiro/steering/`. Kiro prioritizes workspace steering over global steering when instructions conflict.

Kiro also supports AGENTS.md as a steering source. AGENTS.md files can be placed at the workspace root or in the global steering directory, but unlike Kiro steering files they do not support inclusion modes and are always included.

Kiro steering files use YAML frontmatter at the top of the file to configure inclusion. The documented inclusion modes are:

- `inclusion: always`: included in every Kiro interaction; default mode.
- `inclusion: fileMatch` with `fileMatchPattern`: included only when working with files matching one or more glob patterns.
- `inclusion: manual`: available on demand by referencing the steering file in chat, such as `#troubleshooting-guide`, and also available through slash-command UI.
- `inclusion: auto` with `name` and `description`: Kiro decides whether to include the file based on the user's request, similar to skills.

Kiro supports live workspace file references in steering files using `#[[file:<relative_file_name>]]`.

The Kiro best-practice guidance recommends focused files, clear names, explanatory context for decisions, examples, security hygiene, and regular maintenance.

