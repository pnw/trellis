---
name: scaffold-trellis-wiki
description: Create a new Trellis Wiki bundle from the standalone specification and optional kit templates. Use when a user asks to initialize, scaffold, seed, or add a Trellis Wiki to a repository.
---

# Scaffold a Trellis Wiki

1. Read the complete Wiki specification selected by the project. In this
   repository, use `../../../specs/wiki.md`.
2. Confirm the wiki's single governing goal, scope, and target directory. Ask
   only for decisions that materially change the result.
3. Create the minimum bundle first: `index.md`, `overview.md`, and `raw/`.
   Use `../../templates/wiki/bundle/` as editable starting material. Repository
   instructions and the optional manifest live under `templates/wiki/repository/`.
4. Create topic and type directories only when the initial content needs them.
5. Add optional `log.md`, `moves.log`, search, or tool adapters only when the
   user selects them. Never create `roadmap.md` or `episodes.md`.
6. Use relative Markdown links and record the selected Wiki and OKF versions in
   the root index.
7. Run `python3 ../../scripts/lint.py wiki <path-to-wiki>` when available.
8. Report the created structure and any optional kit components installed.

The specification defines conformance. Do not copy workflow instructions into
the wiki's normative content.
