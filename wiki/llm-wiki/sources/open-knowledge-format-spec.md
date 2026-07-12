---
title: "Source: Open Knowledge Format v0.1 Specification"
type: source-capture
evidence: official-docs
description: "Google Cloud's OKF v0.1 spec formalizing the LLM Wiki pattern into a portable, vendor-neutral markdown knowledge format."
sources:
  - "[[raw/articles/open-knowledge-format-spec.md]]"
related:
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
tags: [okf, llm-wiki, standards, knowledge-management]
created: 2026-07-04
timestamp: 2026-07-04T21:43:00Z
---

# Open Knowledge Format v0.1 Specification

## Source Identity

- Raw source: [[raw/articles/open-knowledge-format-spec.md]]
- Source type: specification document
- Author(s): Sam McVeety, Amir Hormati (Google Cloud Data Cloud team)
- Published: 2026-06-12
- Original URL: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
- Scope: Full specification of OKF v0.1 — bundle structure, concept documents, frontmatter schema, cross-linking, reserved filenames, conformance model

## Core Contribution

Formalizes the emergent "LLM wiki" conventions (Karpathy pattern) into an interoperable, vendor-neutral specification. Defines a minimal set of conventions for representing knowledge as plain markdown + YAML frontmatter that can be produced/consumed by any tool.

## Key Claims

- A **format, not a platform** — no SDK, no runtime, no central authority
- Only one required frontmatter field: `type`
- Recommended fields (priority order): `title`, `description`, `resource`, `tags`, `timestamp`
- Consumers MUST preserve unknown keys and MUST NOT reject unrecognized fields
- Consumers MUST tolerate broken links
- A bundle is conformant if: every non-reserved `.md` file has parseable YAML frontmatter with a non-empty `type` field

## Evidence and Results

- Published by Google Cloud as open-source specification
- Reference enrichment agent, static HTML visualizer, and sample bundles provided
- OWOX Model Canvas provides a third-party visual editor
- Community adoption already visible (duyet.net declaring OKF conformance)

## Methodology

Specification design — minimal conformance surface, progressive enhancement via optional fields, explicit versioning via `okf_version` in root index.

## Limitations and Caveats

- v0.1 maturity — draft, may change
- Flat type system (free-form string, no registry)
- No query semantics (storage format only)
- No schema validation beyond `type`
- No conflict resolution for multi-producer bundles
- Link semantics are implicit (untyped directed edges)
- Progressive disclosure depends on index quality

## Important References and Linked Material

- [OKF v0.1 Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — full spec
- [Google Cloud blog announcement](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) — official introduction
- [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) — spec, reference agent, visualizer, sample bundles
- [OWOX Model Canvas](https://model.owox.com) — free visual OKF editor
- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the informal pattern OKF formalizes

## Contribution Routing

- `[[wiki/llm-wiki/entities/open-knowledge-format]]` — primary entity page for the spec
- `[[wiki/llm-wiki/constructs/llm-wiki-pattern]]` — OKF formalizes this pattern
- `[[wiki/llm-wiki/constructs/three-layer-architecture]]` — OKF adds conformance to this architecture

## Extraction Notes

The raw file in this vault is a stub (spec content retrieved from GitHub URL). The full specification is available at the source link. The entity page [[wiki/llm-wiki/entities/open-knowledge-format]] contains the detailed summary extracted from the full spec and supplementary blog posts.
