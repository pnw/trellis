---
name: scaffold-trellis-wiki
description: Create a new Trellis Wiki bundle from the standalone specification and optional kit templates. Use when a user asks to initialize, scaffold, seed, or add a Trellis Wiki to a repository.
---

# Scaffold a Trellis Wiki

1. Before semantic Wiki work, ensure the complete Wiki specification selected
   by the project is in active context. Resolve it from an explicit user
   selection, `trellis.wiki.specification` in `trellis.yaml`, or,
   in this repository, `../../../specs/wiki.md`. Prefer an immutable
   version-tagged URL. Do not reload while its full text remains in active
   context; reload after compaction before further semantic work.
2. Confirm the wiki's single governing goal, scope, and target directory. Ask
   only for decisions that materially change the result.
3. Create the minimum bundle first: `index.md`, `overview.md`, and `raw/`.
   Use `../../templates/wiki/bundle/` as editable starting material. When the
   user selects optional routing, merge `../../templates/repository/AGENTS.md`
   into repository guidance and create or update `trellis.yaml` with only the
   Wiki mapping, using `../../templates/repository/trellis.yaml` as a reference.
4. Create topic and type directories only when the initial content needs them.
5. Add optional `log.md`, `moves.log`, search, or tool adapters only when the
   user selects them. Record installed features and adapters in the optional
   Wiki manifest mapping. Never create `roadmap.md` or `episodes.md`.
6. Use relative Markdown links and record the selected Wiki and OKF versions in
   the root index.
7. Run `python3 ../../scripts/lint.py wiki <path-to-wiki>` when available.
8. Report the created structure and any optional kit components installed.

The specification defines conformance. Do not copy workflow instructions into
the wiki's normative content.
