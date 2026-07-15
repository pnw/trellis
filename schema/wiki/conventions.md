# Wiki Conventions

Agent-agnostic naming, linking, and meta-file conventions. This file is part of the shared `schema/` layer referenced by `AGENTS.md`.

## Naming

- Filenames: kebab-case (e.g., `attention-mechanism.md`)
- Cross-references: repository-root wikilinks (e.g., `[[wiki/llm-wiki/constructs/llm-wiki-pattern]]`, `[[wiki/token-economics/syntheses/token-cost-optimization]]`). Root-level wiki pages keep the `wiki/` prefix: `[[wiki/overview]]`, `[[wiki/log]]`.
- Source references in frontmatter: use repository-root wikilinks for vault files, including exact raw file extensions (e.g., `[[raw/articles/source-slug.md]]`), and use bare URLs for external sources.

## Linking

All internal cross-references use repository-root wikilinks:

- Pages in subdirectories: `[[wiki/topic/type-folder/page-name]]` (e.g., `[[wiki/llm-wiki/constructs/llm-wiki-pattern]]`)
- Pages in subtopics: `[[wiki/topic/subtopics/subtopic/type-folder/page-name]]`
- Root-level wiki pages: `[[wiki/page-name]]` (e.g., `[[wiki/overview]]`, `[[wiki/log]]`, `[[wiki/roadmap]]`)
- Design dossiers: `[[designs/design-slug]]` — the dossier root, resolving to its `design.md`. Wiki pages never link into dossier internals (`schema/design/dossier.md`, Linking Rules).
- Never use bare filenames for pages in subdirectories — always include the topic prefix

This format eliminates ambiguity (no collision risk from duplicate filenames), is trivial to lint (path maps directly to file), and keeps links compact.

## Index Format (`wiki/index.md`)

- Grouped by topic, subtopic when present, then type
- One line per page: `* [[wiki/topic/type-folder/page-name]] — description`
- The only frontmatter in `index.md` is `okf_version: "0.1"`
- Update on every ingest

## Log Format (`wiki/log.md`)

- **No frontmatter**
- Entries are newest-first, grouped under date headings (`## YYYY-MM-DD`)
- Each entry is a bullet with a bold operation word: `* **Ingest**: description`
- Add to an existing date heading if one exists for today; otherwise create a new one at the top

## Agent TODO Commentary

Use `TODO(agent)` headings for transient human commentary that an agent should triage later.

```md
### TODO(agent)

Check whether this claim is still true.
```

- The heading text must be exactly `TODO(agent)`.
- Use the heading level that matches the local context. The TODO belongs to the nearest preceding section with a higher-level heading.
- The TODO body is freeform prose. Do not require YAML, IDs, status fields, or other metadata.
- A `TODO(agent)` section is not durable page content. It is a breadcrumb for later agent action.

When processing `TODO(agent)` sections:

- Search wiki/source files for Markdown headings whose text is exactly `TODO(agent)`.
- Read the TODO body, the containing section, and any nearby source context needed to understand it.
- Triage the TODO into the appropriate action: update the page, verify or research the claim, create a durable task, ask the user, or do nothing.
- If acted on in any capacity, remove the entire `TODO(agent)` section and report what happened.
- If not acted on, leave the `TODO(agent)` section unchanged so it remains available for a later pass.

## Query Handling

For queries against the wiki: read `wiki/index.md` first to find relevant pages. For concept-level lookups where the exact wording is unknown, try `qmd search "<query>" -c wiki` (or `qmd query` where embeddings have been generated) before falling back to `Grep`/`Glob` directly against `wiki/` — that fallback always works and needs no setup, so treat `qmd` as an optimization, not a dependency. See `designs/knowledge-surfacing-design/design.md` (Approach 0 / B2) and `wiki/agent-context/subtopics/retrieval/entities/qmd.md`. Then read the relevant pages and synthesize an answer with `[[wiki/topic/type-folder/page-name]]` citations. If the answer is valuable, offer to save it as a new wiki page.

## Project Application Handling

For requests about applying this wiki to a codebase or agentic implementation workflow:

- Start with [[designs/project-wiki-application-guide]].
- Use [[designs/project-wiki-template]] as the default adaptation structure.
- For multi-agent implementation, use [[designs/multi-agent-project-wiki-pattern]] as the primary coordination model.
- Pull supporting concepts on demand from `agent-context/`, `intent-compiler/`, and `token-economics/`.
- Prefer project-local context for codebase-specific facts; promote lessons back into this research wiki only when they generalize.

## Cross-Wiki (Peer) Links

- A wikilink whose target starts with `<peer>::` points into another wiki, e.g. a link target of `ai-research::wiki/intent-compiler/designs/intent-refinement-stage`. The peer name resolves through the `peers` block of `wiki-manifest.yaml`.
- Unprefixed wikilinks are always intra-wiki.
- **Outbound-only responsibility:** a wiki lints and maintains only its own outbound links. Inbound links are the linking wiki's problem. When checking outbound peer links, follow the peer's `wiki/moves.log` for forwarding addresses; there is no cross-wiki lint tool by design.
- `scripts/lint.py` skips `::` targets; peer-link checking is an on-demand agent task.
