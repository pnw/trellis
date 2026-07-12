---
title: YAML Frontmatter
type: entity
description: "A metadata convention placing a YAML block between triple-dashed lines at the top of a markdown file. Popularized by Jekyll (2008), now ubiquitous in static site generators, knowledge bases, and agent-readable formats like OKF."
sources:
  - https://jekyllrb.com/docs/front-matter/
  - https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter
  - "[[wiki/llm-wiki/sources/open-knowledge-format-spec]]"
related:
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
tags: [standards, knowledge-management, file-formats]
created: 2026-07-05
timestamp: 2026-07-05T13:04:00Z
confidence: medium
novelty: established
aka: ["front matter", "YAML front matter", "frontmatter", "FM"]
---

# YAML Frontmatter

## Identity

YAML frontmatter is a convention — not a formal standard — for embedding structured metadata at the top of a plain-text file (typically markdown). It takes the form of a valid YAML block delimited by triple-dashed lines (`---`):

```yaml
---
title: Example Page
type: construct
tags: [knowledge-management, agents]
created: 2026-07-05
---

# Page content starts here
```

The term "front matter" is borrowed from publishing, where it refers to the material preceding the main body of a book (title page, copyright notice, table of contents). In the markdown world, it serves the same purpose: metadata *about* the content that comes before the content itself.

## Origin

- **Popularized by**: Jekyll (Ruby static site generator), created by Tom Preston-Werner (GitHub co-founder) in 2008
- **Convention, not standard**: There is no RFC, W3C spec, or formal standard body governing frontmatter. Jekyll's documentation is the closest thing to a canonical definition. As Stack Overflow puts it: "If Jekyll didn't invent YAML Front Matter, they were one of the first notable projects to feature it."
- **Rule**: The frontmatter block must be the very first thing in the file, with no preceding whitespace or content

## Relevance to the Wiki

This wiki uses frontmatter on every page as the primary machine-readable metadata layer. It serves three functions:

1. **Classification**: `type`, `tags`, `confidence`, `novelty` — what kind of artifact this is and how reliable it is
2. **Discovery**: `title`, `description` — enables index generation and agent routing without reading the body
3. **Provenance**: `sources`, `created`, `timestamp` — where claims come from and when they were last updated

In the [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]], frontmatter functions as the "dense pass" — an agent can parse it (~50 tokens) to assess relevance before committing to read the full page body (~300-1500 tokens).

## Adoption

| System | How It Uses Frontmatter |
|--------|------------------------|
| Jekyll (2008) | Original popularizer. Any file with frontmatter is "special" and gets processed. |
| Hugo, Gatsby, Eleventy, Astro | Static site generators following Jekyll's convention |
| Obsidian | Personal knowledge management; uses frontmatter for metadata, tags, aliases |
| GitHub Docs | Authoring convention for all documentation pages |
| OKF v0.1 (2026) | Only `type` is required; `title`, `description`, `resource`, `tags`, `timestamp` recommended |
| Cursor .mdc rules | YAML frontmatter for scoping rules by glob pattern |
| This wiki | 7 required fields; type-specific extensions for constructs, entities, designs |

## Notes

- YAML was chosen over alternatives (TOML, JSON) because it's the most human-readable for key-value metadata and doesn't require quoting simple strings
- Some tools support TOML frontmatter (`+++` delimiters) or JSON frontmatter (`{}`), but YAML is dominant
- The convention's simplicity is its strength: any language can parse it with a YAML library + a 3-line delimiter splitter
- OKF's minimal conformance requirement — "parseable YAML frontmatter with a non-empty `type` field" — demonstrates how little structure is needed to make a file machine-navigable
