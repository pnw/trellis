---
title: ObjectGraph (.og)
type: entity
description: "A file format (Dubey, 2026) that reconceives documents as typed directed knowledge graphs for agent traversal. Strict Markdown superset with progressive disclosure, role scoping, and a two-primitive query protocol."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]]"
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
tags: [agent-context, file-formats, knowledge-graph, progressive-disclosure]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: medium
novelty: exploratory
aka: ["ObjectGraph", ".og format", "OG format"]
---

# ObjectGraph (.og)

## Identity

A file format proposed by Mohit Dubey and Open Gigantic (April 2026) that reconceives documents as typed, directed knowledge graphs to be *traversed* rather than strings to be *injected*. Designed as a strict superset of Markdown — every .md file is a valid .og file — requiring no infrastructure beyond a two-primitive query protocol.

- **Created by**: Mohit Dubey, Open Gigantic
- **Published**: 2026-04-30
- **Paper**: https://arxiv.org/abs/2604.27820
- **Format**: Text-based, Markdown superset
- **Key innovation**: Progressive Disclosure Model with `::index`, `::dense`, and `::full` content layers

## Relevance to the Wiki

ObjectGraph formalizes the [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]] and proposes a solution via the [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]. While this wiki doesn't use .og format directly, the constructs it introduces (index routing, dense summaries, typed edges, LLM-as-Router) directly inform [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]].

The key lesson: you don't need .og format to get the benefits. OKF + generated indexes achieves similar routing with standard Markdown.

## Associated Artifacts

### Format Primitives

| Block | Purpose | Tokens |
|-------|---------|--------|
| `::meta` | File metadata (title, version, domain, scope) | ~15 |
| `::schema` | Declared node types, edge types, scope levels | ~20 |
| `::index` | Routing table: node IDs, types, scopes, confidence, keywords | ~30 |
| `::node[id=X]` | A semantic knowledge unit with typed content blocks | Variable |
| `::dense` | Compressed keyword summary (~12 tokens/node) | ~12 |
| `::full` | Complete prose explanation | ~180 |
| `::edges` | Typed directed relationships (`:requires`, `:precedes`, `:see-also`) | ~10 |
| `::warning` | Critical safety information (never skipped) | Variable |
| `::assertion` | Executable validation logic | Variable |

### Query Protocol

Two primitives (exposed as MCP tools or function-calling schemas):
1. **`search_index`** — Agent reads ::index, LLM selects relevant nodes
2. **`resolve_context`** — Fetches node content at appropriate depth, auto-following `:requires` edges

### Performance

- 92% mean token reduction (2,340 → 187 tokens per query)
- 36.5× reduction in multi-turn workflows at turn 5
- No statistically significant accuracy degradation (p > 0.05)
- Task accuracy *improves* on 7/8 task types (less-is-more effect)

### Comparison with OKF

| Dimension | ObjectGraph | OKF v0.1 |
|-----------|-------------|----------|
| Approach | New format (Markdown superset) | Convention on standard Markdown |
| Index | `::index` block (mandatory) | `index.md` file (optional) |
| Dense layer | `::dense` per node | `description` field in frontmatter |
| Typed edges | `::edges` with labels | Implicit (link semantics from prose) |
| Role scoping | `scope` attribute per node | Not specified |
| Query protocol | Defined (`search_index` + `resolve_context`) | Not specified (storage only) |
| Tooling required | Transpiler for existing docs | None |
| Adoption | Paper-stage | Google-backed, community adoption |

## Notes

- Backward compatibility is the key design decision: no migration needed, benefits accrue incrementally as `::` blocks are added
- The transpiler (Markdown → .og) uses a hybrid approach: deterministic structural extraction (Stage 1) + bounded LLM metadata synthesis for `::dense` blocks (Stage 2) + fidelity verification (Stage 3)
- No standards body governance — fragmentation risk if adopted without coordination
- Published one month before OKF (April vs. June 2026) — different teams solving similar problems
