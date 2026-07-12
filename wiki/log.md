# Operation Log

<!-- Append-only. Newest first. -->

## 2026-07-12

* **Bootstrap**: Repository created by executing the bootstrap plan in [[wiki/llm-wiki/designs/trellis-repo-design]]. All initial content arrived from `pnw/ai-research` at commit `3c5908840f2fb13a543ebb602b4acfaa84ae96a5` (branch `claude/wiki-assessment-critique-uzse03`): the `wiki/llm-wiki/` and `wiki/agent-context/` topics (76 pages), their cited raw sources (35 files plus PDF siblings), `raw/repos/` operational snapshots, and the schema/scripts/adapters layer. Cross-repo copies do not preserve git history; this entry is the provenance record, and `ai-research`'s `wiki/moves.log` tombstones every departed page with a `moved-to trellis::` forwarding address.
* **Schema**: Granulated `schema/page-types.md` into `schema/page-types/` — one standalone normative file per type plus `registry.md` (vocabulary, location rules, extensibility, decision tree). Schema files carry no rationale back-references; substantial change rationale goes to `decision` pages, discovered by archaeology.
* **Schema**: Ratified the cross-wiki independence rule in `schema/page-format.md` (owner decision, 2026-07-12): citing a peer wiki's source-capture imports its `evidence` tier at face value, but wikis operated by the same owner and agents count as one source for independence — no cross-repo self-corroboration. Documented peer-link syntax and outbound-only responsibility in `schema/conventions.md`.
* **Create**: Wrote the distribution layer — `seed/interview.md` (instantiation interview), `seed/manifest-template.yaml`, `seed/agents-md-template.md`, `seed/pages/` skeletons — plus `wiki-manifest.yaml` (upstream form, no `upstream:` block), `scripts/movelog.sh`, and this repo's `AGENTS.md`/adapter files. Updated `scripts/lint.py` to skip `::` peer links and exclude `episodes.md` from graph metrics.
* **Create**: Wrote [[wiki/overview]] (states the single goal and the two health axes), assembled [[wiki/index]] from the migrated topics, and carried the method-side backlog and meta-experiment log into [[wiki/roadmap]].
