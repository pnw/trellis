---
title: "OpenAI Codex Docs: Custom Instructions with AGENTS.md"
source: https://developers.openai.com/codex/guides/agents-md
retrieved: 2026-07-06
authors: OpenAI
published: unknown
updated: unknown
---

Codex reads AGENTS.md files before doing work. Codex builds an instruction chain once per run or launched TUI session.

At global scope, Codex reads `AGENTS.override.md` from the Codex home directory if it exists; otherwise it reads `AGENTS.md`. It uses only the first non-empty file at that level.

At project scope, Codex starts at the project root and walks down to the current working directory. In each directory it checks for `AGENTS.override.md`, then `AGENTS.md`, then filenames configured in `project_doc_fallback_filenames`. Codex includes at most one file per directory.

Codex concatenates discovered files from root to current directory, so more local files appear later in the prompt and override earlier guidance by recency. Codex skips empty files and stops adding files once the combined size reaches `project_doc_max_bytes`, which defaults to 32 KiB.

Codex supports alternate instruction filenames through `project_doc_fallback_filenames`, but filenames not on the fallback list are ignored for instruction discovery.

OpenAI recommends verifying the setup by asking Codex to summarize current instructions or show active instruction files, and troubleshooting by checking overrides, fallback names, truncation, and the active `CODEX_HOME`.

