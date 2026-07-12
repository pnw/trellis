---
title: Open Knowledge Format (OKF)
type: entity
description: "Google's OKF v0.1 (June 2026): formalizes the LLM wiki pattern into a portable, vendor-neutral spec. Markdown + YAML frontmatter, minimal required fields, designed for agent/human interop."
sources:
  - "[[wiki/llm-wiki/sources/open-knowledge-format-spec]]"
related:
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/entities/andrej-karpathy]]"
tags: [okf, llm-wiki, standards, knowledge-management]
created: 2026-07-02
timestamp: 2026-07-04T21:23:00Z
confidence: medium
novelty: emerging
aka: ["OKF", "Open Knowledge Format v0.1"]
---

# Open Knowledge Format (OKF)

## Identity

OKF is an open specification from Google Cloud (v0.1, published June 12, 2026) that formalizes the [[wiki/llm-wiki/constructs/llm-wiki-pattern]] into a portable, interoperable standard. It defines minimal conventions for representing knowledge as plain markdown files with [[wiki/llm-wiki/entities/yaml-frontmatter]] — human-readable, agent-parseable, diffable in version control, and portable across tools and organizations.

Core thesis: **a format, not a platform**. No SDK, no runtime, no central authority.

## Relevance to the Wiki

This wiki is largely OKF-conformant. Key alignment:
- Markdown + YAML frontmatter as the core representation
- Directory hierarchy with progressive disclosure (index files)
- Chronological history (log files)
- Cross-linking between concepts
- Designed for both human curation and agent authoring

Intentional divergences:
1. **Wikilinks over standard markdown links** — `[[wiki/llm-wiki/entities/open-knowledge-format]]` instead of `[Title](topic/page-name.md)` for rename resilience
2. **`sources` instead of `resource`** — richer provenance semantics than OKF's single `resource` field

## Associated Artifacts

### Specification Details

**Required frontmatter:** Only `type` is required in OKF. Recommended: `title`, `description`, `resource`, `tags`, `timestamp`.

**Bundle structure:** Self-contained directory tree of markdown files with optional `index.md` and `log.md`.

**Conformance (v0.1):** A bundle is conformant if every non-reserved `.md` file has parseable YAML frontmatter with a non-empty `type` field.

**Design principles:** Minimally opinionated, producer/consumer independence, format not platform.

### Limitations

1. Tedious to hand-author (optimized for machine authoring + human review)
2. No query semantics (storage format only)
3. Flat type system (unregistered free-form string)
4. No schema validation beyond `type`
5. Link semantics are implicit (untyped directed edges)
6. v0.1 maturity (draft, may change)
7. No conflict resolution for multi-producer bundles
8. Progressive disclosure depends on index quality

### Tooling Ecosystem (as of July 2026)

- Reference enrichment agent (Google, open source)
- Static HTML visualizer (Google, bundled with spec)
- OWOX Model Canvas (free visual editor)
- Google Cloud Knowledge Catalog (can ingest OKF)

### Links

- [OKF v0.1 Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [Google Cloud blog announcement](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
- [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
- [OWOX Model Canvas](https://model.owox.com)

## Notes

- OKF is the formal spec for what Karpathy's pattern describes informally
- Key addition over informal LLM wikis: a conformance model, the `type` primitive, cross-org exchange semantics
- Related standards: Obsidian vaults, AGENTS.md/CLAUDE.md, data catalogs (Dataplex, Unity Catalog), llms.txt
