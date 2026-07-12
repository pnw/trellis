---
title: Three-Layer Architecture
type: construct
description: The structural foundation of the LLM Wiki pattern — raw sources, LLM-generated wiki, and schema with strict separation of concerns.
sources:
  - "[[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]"
  - "[[wiki/llm-wiki/sources/open-knowledge-format-spec]]"
related:
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
tags: [llm-wiki, architecture, knowledge-management]
created: 2026-04-16
timestamp: 2026-07-07T18:20:00Z
confidence: medium
novelty: emerging
coined_by: "Andrej Karpathy (April 2026)"
---

# Three-Layer Architecture

## Definition

The structural foundation of the [[wiki/llm-wiki/constructs/llm-wiki-pattern]]. Three layers with strict separation of concerns.

## Why It Matters

Immutability of sources enables traceability and drift detection. The schema is the most important file — without it, LLM output is inconsistent. Git version control on the whole structure provides audit trail and revert capability.

## Mechanism / Structure

### Layer 1: Raw Sources (`raw/`)

Immutable source documents — articles, papers, code repos, datasets, images. The LLM reads but **never edits** these ([[wiki/llm-wiki/invariants/raw-source-immutability]]); fidelity is the point. The layer exists for two operational purposes: re-visiting source captures (regenerating or auditing a capture against its original — see [[wiki/llm-wiki/constructs/source-isolation]]) and change detection against the upstream sources the files are copies of. They serve as the verification baseline: every claim in the wiki must trace back to a file in `raw/`. Incidental non-source assets that serve neither purpose (e.g., browser-save scripts and styles) are not part of the layer and may be pruned.

### Layer 2: The Wiki (`wiki/`)

LLM-generated markdown pages. The LLM owns everything here. Pages are typed artifacts: source captures, constructs, entities, syntheses, designs, assessments, comparisons.

Critical structural files:
- **`index.md`** — Master catalog, updated on every ingest. The LLM reads this first to navigate.
- **`log.md`** — Append-only operation log.
- **`overview.md`** — Evolving high-level synthesis.

### Layer 3: The Schema

Defines the wiki's structure, naming conventions, page templates, and operational workflows. Transforms a generic LLM into a disciplined knowledge worker. Named `CLAUDE.md` in Karpathy's setup, but the concept is agent-agnostic — in this wiki it lives in the root `schema/` directory (compact contract in `AGENTS.md`), with `.kiro/steering/` and `CLAUDE.md` as thin tool adapters referencing it.

## Distinctions

- Not just "files in folders" — the schema layer makes it a system
- Not a database — human-readable, diffable, portable
- The separation between raw (immutable) and wiki (LLM-owned) is the key architectural decision

## Evidence and Sources

- Karpathy's original design (April 2026)
- [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]] — comprehensive guide to the architecture

## Related Artifacts

- [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — the pattern this architecture supports
- [[wiki/llm-wiki/entities/open-knowledge-format]] — formalizes this structure as a portable spec
