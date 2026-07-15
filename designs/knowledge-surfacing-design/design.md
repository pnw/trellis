---
title: Agent Knowledge Surfacing — Progressive Disclosure Approaches
description: "Design exploration of approaches for surfacing an OKF knowledge graph to agents: static index layers, MCP-based tool discovery, and hybrid compilation strategies."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/tagrag-tag-guided-hierarchical-knowledge-graph-rag]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/qmd]]"
  - "[[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]"
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
tags: [agent-context, progressive-disclosure, architecture, okf, knowledge-management, design-patterns]
created: 2026-07-05
timestamp: 2026-07-15T12:00:00Z
status: active
---

# Agent Knowledge Surfacing — Progressive Disclosure Approaches

## Purpose

Explore concrete approaches to surfacing an OKF-conformant markdown knowledge graph to an LLM agent, with emphasis on leveraging tags and frontmatter metadata for efficient navigation. The goal: the agent retrieves only the knowledge relevant to the current task, at the minimum depth necessary, without injecting the full wiki.

## System Boundary

- **Input**: An OKF knowledge bundle (~30-200 pages) with typed frontmatter, tags, descriptions, cross-links, and directory structure
- **Consumer**: An LLM agent operating within a context window (128K–1M tokens) with tool-use capabilities
- **Output**: A minimal, task-relevant subset of the knowledge graph loaded into agent context
- **Not in scope**: Multi-agent federation, real-time indexing of external sources, embedding-based retrieval

## Core Model

All approaches share a common principle: **the agent carries a map, not the territory** (Ardalis, 2026). The question is what form the map takes and how the agent navigates from map to territory.

**Revision (2026-07-07):** a fourth, even simpler option belongs ahead of Approach A — agentic search requires no map at all. Real-world evidence surfaced since this page was first written shows the industry's actual graduation path from flat files diverges from what this page originally proposed: rather than building bespoke MCP meta-tool schemas or compiled typed-edge graphs, coding agents converged on plain grep/glob, and Karpathy's own primary guidance for this pattern recommends off-the-shelf local hybrid search over custom infrastructure. See [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] and the updated Recommendation section below.

Four approaches, from simplest to most complex:

| Approach                              | Map Format                              | Navigation Mechanism                                   | Infrastructure Required    |
| ------------------------------------- | --------------------------------------- | ------------------------------------------------------ | -------------------------- |
| 0. Agentic Search (No Index)          | None — the raw corpus itself            | glob / grep / read, iterative                          | None                        |
| A. Static Index Layers                | Generated markdown files                | File reads                                             | None (pure markdown)       |
| B. MCP Meta-Tool / Local Hybrid Search | Tool descriptions + on-demand retrieval | Tool calls (get_page, search_tags) or hybrid search    | MCP server                 |
| C. Compiled Graph with Query Protocol | Typed index + dense summaries + edges   | Two-primitive protocol (search_index, resolve_context) | Query router (lightweight) |

---

## Approach 0: Agentic Search (No Index)

### Description

The agent searches the raw corpus directly using generic file-search primitives — no generated index, no MCP server, no compiled manifest. See [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] for the full construct definition.

### Workflow

```
Query arrives
  -> Agent globs for likely files (by topic path, filename pattern)
  -> Agent greps for exact terms, tags, or identifiers across the corpus
  -> Agent reads matched files in full
  -> Agent follows wikilinks/references as needed
  -> Agent synthesizes answer with citations
```

### Existing Implementations

| System | How It Works |
|--------|-------------|
| **Claude Code** | Removed vector search/embeddings in May 2025 in favor of model-driven glob/grep/read; reported to have "outperformed everything." [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]] |
| **Cursor, Windsurf, GitHub Copilot, Sourcegraph Amp** | **Correction (2026-07-07):** an initial single-source claim that these vendors also dropped vectors does not hold up. Cursor is hybrid (grep + embeddings, agent picks per query), Windsurf and GitHub Copilot are embeddings-first, and Sourcegraph Amp uses structural code-graph indexing — see [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]] for the vendor-by-vendor detail. Claude Code's pure-grep design is real but is the exception, not the rule. |
| **The pre-split ai-research vault (2026-07-07, 114 pages)** | An entire research and maintenance pass over that vault — reviewing 114 pages, finding orphans, tracing citation chains — was conducted using exactly this pattern (Grep/Glob/Read tools against the raw `wiki/` directory), with no generated index consulted beyond `wiki/index.md` itself. (This page moved to the trellis repo in the 2026-07-12 federation split; the observation stands as dated evidence.) |

### Strengths

- Zero build, zero maintenance — nothing to regenerate, nothing to go stale.
- No embedding pipeline means no staleness, permission-surface, or reliability issues from a separate retrieval subsystem. [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]
- Directly validated at far larger scale (codebases with thousands of files) than this wiki currently needs.

### Weaknesses

- Recall depends on the corpus being greppable: query vocabulary must overlap with filenames, tags, or body text. A synonym-heavy or cross-lingual query can miss relevant pages a semantic search would catch.
- No ranking — the agent must decide relevance itself from raw matches, which costs reasoning (though not necessarily tokens, since matches are typically few).
- Evidence base for this specific claim is currently single-source in this wiki's terms (see [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] Open Questions) — treat the "outperformed everything" framing as a strong practitioner signal, not a settled benchmark.

### When to Use

- Default assumption for any wiki small enough that `Grep`/`Glob` calls stay cheap and fast — which, per the evidence above, appears to extend well past the pre-split ai-research vault's 114-page scale (as of 2026-07-07).
- When query vocabulary reliably overlaps with tags, frontmatter, filenames, or body text (true for this wiki, given its tagging and naming conventions).
- As the first thing to try before building any of Approaches A/B/C — those add infrastructure this approach doesn't need until it demonstrably falls short.

---

## Approach A: Static Index Layers

### Description

Generate materialized index files from frontmatter at ingest time. The agent reads these indexes first, then selectively reads full pages. No infrastructure beyond the wiki itself.

### Components

**Layer 0 — Steering context (always loaded):**
Minimal routing instructions telling the agent how to navigate. Equivalent to AGENTS.md. Kept under 150 lines per ETH Zurich findings.

**Layer 1 — Master index (`wiki/index.md`):**
Already exists. Topic-grouped, one line per page with description. ~500 tokens for a 32-page wiki.

**Layer 2 — Tag index (`wiki/by-tag.md`):**
Generated file grouping all pages by tag. Enables cross-cutting queries that don't align with topic structure.

```markdown
# Tag Index

## validation (3 pages)
* [[ai-research::wiki/intent-compiler/subtopics/semantic-ir/constructs/translation-validation]] — Verifying correctness of each transformation step.
* [[ai-research::wiki/intent-compiler/assessments/validation-assessment]] — What is validated, speculative, and risky.
* [[ai-research::wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]] — Validation findings routed upstream.

## knowledge-management (5 pages)
* [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — LLM agents build structured markdown wikis from raw sources.
* [[wiki/llm-wiki/constructs/three-layer-architecture]] — Raw sources, LLM-generated wiki, and schema.
...
```

**Layer 3 — Type index (`wiki/by-type.md`):**
Optional. Groups pages by artifact type for queries like "what designs exist?" or "what's assessed?"

**Layer 4 — Full page content:**
Read on demand when the agent identifies a specific page from the index layers.

### Workflow

```
Query arrives
  → Agent reads index.md OR by-tag.md (depending on query shape)
  → Agent identifies 1-5 relevant pages from descriptions
  → Agent reads those pages
  → Agent synthesizes answer with citations
```

### Existing Implementations

| System | How It Works |
|--------|-------------|
| **OKF bundles** | `index.md` at every directory level; descriptions from frontmatter. OKF spec §6. |
| **Karpathy's LLM Wiki** | Schema file instructs agent to read index first, then navigate. Pure convention. |
| **This wiki** | `wiki/index.md` + `.kiro/steering/conventions.md` (Query Handling section). |
| **llms.txt standard** (Jeremy Howard, fast.ai) | Two-tier: `llms.txt` (overview + links) and `llms-full.txt` (complete content). Agent reads the summary file first. |
| **Obsidian + Dataview** | Plugin generates virtual indexes from frontmatter; not agent-facing but same principle. |

### Token Budget

| Layer                   | Tokens (32-page wiki) | When Loaded           |
| ----------------------- | --------------------- | --------------------- |
| Steering                | ~800                  | Always                |
| Master index            | ~500                  | Every query           |
| Tag index               | ~600                  | Cross-cutting queries |
| Per-page (full)         | ~300-1500             | Only relevant pages   |
| **Typical query total** | ~2,500-4,000          | —                     |

### Strengths

- Zero infrastructure — pure markdown, works with any agent/model
- Deterministic — no LLM generation needed for indexes (scan frontmatter mechanically)
- OKF-conformant — uses standard conventions
- Auditable — indexes are versioned in git like everything else
- Works with all agent frameworks (Kiro, Claude Code, Codex, Cursor)

### Weaknesses

- No on-demand schema retrieval — agent must read full pages even if only partial content is relevant
- No role scoping — all content visible to all consumers
- Index staleness if not regenerated on every ingest (solvable with automation)
- Flat tag list — no hierarchy for navigating from general to specific

### When to Use

- Wiki under ~200 pages
- Single-agent consumer
- No existing MCP infrastructure
- Simplicity > performance optimization

---

## Approach B: MCP Meta-Tool Pattern

### Description

Expose the knowledge graph through an [[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]] server with two meta-tools implementing progressive disclosure. The agent discovers capabilities through tool descriptions and retrieves content on demand via tool calls.

### Components

**Meta-Tool 1: `discover_knowledge`**
- Description contains the complete capability index (all tags, types, and page slugs)
- When called with parameters, returns filtered subsets:
  - `discover_knowledge(tag="validation")` → pages tagged with validation
  - `discover_knowledge(type="assessment")` → all assessment pages
  - `discover_knowledge(query="token cost")` → semantic search over descriptions

**Meta-Tool 2: `read_knowledge`**
- Retrieves specific page content at various depths:
  - `read_knowledge(page="intent-compiler/validation-assessment", depth="frontmatter")` → just metadata
  - `read_knowledge(page="intent-compiler/validation-assessment", depth="summary")` → first paragraph
  - `read_knowledge(page="intent-compiler/validation-assessment", depth="full")` → complete page

### Architecture

```
┌─────────────────────────────┐
│  Agent (Claude, GPT, etc.)  │
└──────────┬──────────────────┘
           │ MCP tool calls
           ▼
┌─────────────────────────────┐
│  Knowledge MCP Server       │
│  ┌───────────────────────┐  │
│  │ discover_knowledge()  │  │  ← index in tool description
│  │ read_knowledge()      │  │  ← on-demand page retrieval
│  └───────────────────────┘  │
│  ┌───────────────────────┐  │
│  │ Frontmatter Parser    │  │  ← scans YAML at startup
│  │ Tag Index (in-memory) │  │  ← built from frontmatter
│  │ File Reader           │  │  ← serves page content
│  └───────────────────────┘  │
└─────────────────────────────┘
           │ reads
           ▼
┌─────────────────────────────┐
│  wiki/ directory (OKF)      │
└─────────────────────────────┘
```

### Existing Implementations

| System                                  | How It Works                                                                                                                                    |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Solo.io agentgateway**                | `toolMode: Search` replaces upstream tool list with `get_tool` + `invoke_tool` meta-tools. Enterprise MCP gateway. Reports 91% token reduction. |
| **Synaptic Labs Bounded Context Packs** | Two meta-tools (discovery + execution) with domain-organized agents. 85-95% token savings. Startup: ~600 tokens vs ~8,000 for 33 tools.         |
| **Anthropic Claude Skills**             | Production implementation of bounded context packs — skills load contextually based on task type. Same progressive disclosure principle.        |
| **Anthropic Code Execution with MCP**   | Presents MCP servers as a discoverable code API in a sandboxed runtime rather than routing every tool call through context directly; ~98.7% token reduction on a cited example, independently corroborated at ~99.2% on a 112-tool production GitHub MCP server. [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]] [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]] |
| **Anthropic Tool Search Tool**          | Platform feature: tools marked `defer_loading: true` become discoverable on demand instead of always-loaded; ~85% token reduction with no loss of tool-library access. [[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]] |
| **GitHub's own MCP server**             | Three meta-tools (`list_available_toolsets`, `get_toolset_tools`, `enable_toolset`) rather than the two-tool discover/execute pattern; groups tools by domain (repos, issues, pull_requests, actions); reports 60-80% context reduction. [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]] |
| **Context7 MCP**                        | Fetches current library documentation on demand rather than injecting training-data versions. Discovery + retrieval pattern.                    |
| **mcpdoc (LangChain)**                  | MCP server that serves llms.txt-based documentation to agents on demand.                                                                        |
| **Brady Gaster's Squad**                | Agent teams where each member lives in own file, reads only its own context, links to shared resources.                                         |

### Security Note

GitHub's own three-meta-tool implementation surfaced a live design disagreement: defaulting to `--read-only` inverts secure-by-default (an opt-in `--allow-edit` flag would be safer), and secrets passed as environment variables remain visible in process lists (CWE-214) — a risk containerization reduces but does not eliminate. [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]] Community reaction to code-execution-based MCP access raised a further concern specific to that variant: routing tool calls through generated code can strip out the inline guidance that tool descriptions and responses normally carry mid-task, and auditing dynamically generated/executed code is an open problem. [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]] Any Approach B implementation for this wiki should carry these forward as concrete design constraints, not defer them.

### B2: Local Hybrid Search (QMD-Style)

A meaningfully different flavor of Approach B: instead of a bespoke discover/read tool-schema, expose an actual hybrid search engine — lexical (BM25) plus vector plus LLM rerank — as an MCP server over the markdown corpus. [[wiki/agent-context/subtopics/retrieval/entities/qmd]]

This is not hypothetical: [[wiki/agent-context/subtopics/retrieval/entities/qmd]] is a real, MIT-licensed, actively maintained tool built for exactly this — on-device BM25 + vector + rerank fusion over a markdown directory, with a native MCP server, created by Shopify's Tobi Lütke. [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]] Karpathy's own primary gist on this wiki's founding pattern recommends tools like this — not a custom-built meta-tool schema or compiled graph — as the graduation path once a flat index stops scaling. [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]

**Why this matters for the B1/B2 choice:** the original discover/read meta-tool schema (B1, above) requires building and maintaining a bespoke server. QMD-style hybrid search (B2) is closer to "install a tool and point it at `wiki/`" — no custom schema design, no manifest generation, and it adds genuine semantic recall that B1's tag/frontmatter routing lacks. B2 is the stronger default when it's time to graduate past Approach 0; B1's meta-tool pattern remains more relevant when the thing being exposed is a large *heterogeneous tool library* (as in GitHub's or Anthropic's own case) rather than a *markdown knowledge corpus*.

### Token Budget

| Layer | Tokens | When Loaded |
|-------|--------|-------------|
| Meta-tool descriptions (capability index) | ~300-500 | Session start |
| Per-discovery call result | ~100-300 | Per query |
| Per-page (frontmatter only) | ~50 | When confirming relevance |
| Per-page (full) | ~300-1500 | Only when needed |
| **Typical query total** | ~1,000-2,500 | — |

### Strengths

- True on-demand retrieval — agent pays only for what it reads
- Depth control — frontmatter / summary / full reading levels
- Semantic filtering — can implement fuzzy tag matching, description search
- Extensible — add tools for link traversal, history queries, etc.
- Works with MCP-compatible clients (Claude Code, Cursor, VS Code, etc.)

### Weaknesses

- Requires running an MCP server (local process or remote service)
- Tool-call overhead — each retrieval is a round-trip
- Agent must learn the tool API (minor — tool descriptions are self-documenting)
- More complex to debug than static files
- Not portable across non-MCP agents

### When to Use

- Wiki over ~50 pages where full index injection becomes expensive
- Multi-model/multi-agent consumption of same knowledge base
- Need for depth-controlled retrieval (frontmatter vs full)
- Already using MCP infrastructure
- **B1 (custom meta-tool schema)** when the thing exposed is a large, heterogeneous tool/API library rather than a document corpus — the real-world examples (GitHub, Anthropic's own platform) are all this case.
- **B2 (QMD-style hybrid search)** when the thing exposed is specifically a markdown knowledge corpus and Approach 0's grep-based recall has started missing relevant pages due to vocabulary mismatch — no custom schema to design or maintain.

---

## Approach C: Compiled Graph with Typed Index

### Description

Compile the wiki into a format with explicit routing metadata — typed indexes, dense keyword summaries, and declared edges — enabling a two-primitive query protocol. The agent reads only the routing layer, then resolves specific nodes.

This is the [[wiki/agent-context/subtopics/retrieval/entities/objectgraph-format]] approach adapted to an OKF wiki, without requiring a format change.

### Components

**Manifest (compiled from frontmatter):**
```yaml
# wiki/.manifest.yaml (auto-generated)
nodes:
  - id: intent-compiler/validation-assessment
    type: assessment
    tags: [validation, intent-compiler]
    confidence: medium
    description: "What is validated, speculative, and risky about the intent compiler design."
    keywords: "validation|speculation|risk|evidence|gaps"
    edges:
      - target: intent-compiler/intent-compiler-design
        type: validates
      - target: intent-compiler/sources/intent-compiler-deep-research-validation
        type: sourced-from
  - id: llm-wiki/llm-wiki-pattern
    type: construct
    tags: [llm-wiki, knowledge-management, agents, curation]
    confidence: high
    description: "LLM agents build and maintain structured markdown wikis from raw sources."
    keywords: "wiki|markdown|agent|curation|ingest|query|lint"
    edges:
      - target: llm-wiki/three-layer-architecture
        type: requires
      - target: llm-wiki/open-knowledge-format
        type: formalized-by
  # ... all pages
```

**Query protocol (two primitives):**
1. `search_index(query, filters)` → returns matching node IDs + descriptions from manifest
2. `resolve_context(node_ids)` → returns full page content for requested nodes, auto-following `:requires` edges

Fusing a compact summary at each manifest node — rather than storing only a description — would apply [[wiki/agent-context/subtopics/retrieval/constructs/domain-centric-knowledge-fusion]] to this wiki's tag hierarchy.

**Tag hierarchy (optional enhancement):**
```yaml
# wiki/.tag-hierarchy.yaml
knowledge-management:
  children: [llm-wiki, okf, curation]
  description: "How to organize and maintain knowledge"
agents:
  children: [agent-handoff, loop-engineering, harness-engineering, agent-context]
  description: "Design and operation of LLM agents"
validation:
  children: [formal-methods, translation-validation]
  description: "Verifying correctness and confidence"
```

### Architecture

```
┌──────────────────────────────┐
│  Agent                       │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  Router Layer                │
│  (LLM reads manifest,       │
│   decides which nodes)       │
│                              │
│  search_index:               │
│    query → manifest scan     │
│    filter by tag/type/conf   │
│    return node descriptions  │
│                              │
│  resolve_context:            │
│    node_ids → read pages     │
│    follow :requires edges    │
│    return assembled context  │
└──────────┬───────────────────┘
           │ reads
           ▼
┌──────────────────────────────┐
│  wiki/ + .manifest.yaml      │
│  (OKF bundle, unchanged)     │
└──────────────────────────────┘
```

### Existing Implementations

| System                       | How It Works                                                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **ObjectGraph (.og format)** | `::index` block with node IDs, types, scopes, confidence, keywords. Two-primitive query protocol. 92% token reduction.                   |
| **TagRAG (ACL 2026)**        | Hierarchical domain tag chains as a DAG. Object tags linked to domain tags, knowledge fused at each level. 14.6× faster than GraphRAG.   |
| **LLM-Wiki (Tencent, 2026)** | Compiles documents into wiki pages with bidirectional links. Search/read/follow-link as tool operations. Error Book for self-correction. |
| **Google Knowledge Catalog** | Ingests OKF bundles and serves them to agents. Proprietary serving layer on open format.                                                 |

### Token Budget

| Layer                      | Tokens       | When Loaded              |
| -------------------------- | ------------ | ------------------------ |
| Manifest (32 pages)        | ~400-600     | Per query (or cached)    |
| Per-node resolution (full) | ~300-1500    | Only matched nodes       |
| Edge-traversal additions   | ~300-1000    | Auto-loaded dependencies |
| **Typical query total**    | ~1,500-3,000 | —                        |

### Strengths

- Typed edges enable automatic dependency traversal (ask for X, get its prerequisites too)
- Tag hierarchy enables "zoom" — query at general level, drill into specific
- Manifest is cheap to load (~600 tokens) and provides complete routing information
- Confidence filtering — agent can skip `low` confidence pages unless specifically asked
- Future-proof — scales to 200+ pages without linear cost growth

### Weaknesses

- Requires a compilation step (generating manifest from frontmatter)
- Typed edges must be maintained in frontmatter (extra metadata authoring burden)
- Tag hierarchy needs manual curation (not automatically derivable)
- More complex to implement than Approach A
- The "LLM-as-Router" pattern means routing quality depends on model capability

### When to Use

- Wiki at 100+ pages where flat indexes lose signal
- Complex cross-cutting queries ("what's unvalidated about knowledge management?")
- Multi-hop reasoning needed (page → its sources → contradicting sources)
- Investment in structured metadata is already being made (as in this wiki)

---

## Comparison

| Dimension             | 0: Agentic Search             | A: Static Indexes            | B: MCP Meta-Tool / Hybrid Search | C: Compiled Graph             |
| --------------------- | ------------------------------ | ---------------------------- | ---------------------------------- | ----------------------------- |
| Infrastructure        | None                            | None                         | MCP server (custom or QMD)         | Compilation script            |
| Portability           | Any agent with file tools       | Any agent                    | MCP-compatible                     | Any (manifest is just YAML)   |
| Token efficiency      | Good (only matches loaded)      | Good (2.5-4K/query)          | Best (1-2.5K/query)                | Good (1.5-3K/query)           |
| Cross-cutting queries | Via grep across tags/body       | Via tag index                | Via discovery filters or hybrid search | Via tag hierarchy + edges  |
| Depth control         | None (full file or nothing)     | None (full page or nothing)  | Yes (frontmatter/summary/full)     | Yes (dense/full)              |
| Dependency traversal  | Manual (agent follows links)    | Manual (agent follows links) | Manual (agent calls tool)          | Automatic (edges declared)    |
| Maintenance           | None                             | Auto-generate on ingest      | Server code (B1) or `qmd` reindex (B2) | Auto-generate + edge curation |
| Complexity            | Lowest                          | Low                           | Medium                             | Medium-High                   |
| Scale validated in the wild | Codebases with 1000s of files | Not independently validated at a stated ceiling | 100+ tools (GitHub, Anthropic) | Not found in production for wiki-scale corpora in this research pass |

## Recommendation for This Wiki

**Revision (2026-07-07):** the pre-split ai-research vault had just crossed 114 pages — past the ~100-page threshold this section originally named as the trigger to "graduate to Approach B." Research done at that trigger point changes the recommendation rather than just confirming the original plan.

**Current default: Approach 0 (agentic search), already in use.** This entire research and maintenance session was conducted via `Grep`/`Glob`/`Read` directly against the raw `wiki/` directory, with `wiki/index.md` consulted but no other generated index. This matches the specific choice Anthropic made for Claude Code — real, but, per vendor-level research, the exception rather than an industry-wide norm; see [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]. [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]] There is no evidence this wiki has outgrown it yet, and no build cost to keep using it — that reasoning holds regardless of how common the choice is elsewhere.

**Do not build the originally-planned `wiki/by-tag.md` / custom Approach B meta-tool server.** Neither materialized in the roughly two months since this page recommended them, and the new evidence explains why that's defensible rather than neglectful: the real-world graduation path from a flat markdown wiki is not "build a bespoke tag index or MCP schema" — it's grep-based search until it doesn't work, then an off-the-shelf local hybrid-search tool. [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]

**Concrete graduation trigger, going forward:** move to **Approach B2 (`qmd`-style local hybrid search)** the first time a real query fails under Approach 0 — i.e., an agent searches for a concept using vocabulary that doesn't appear in the matching page's tags, title, or body text, and misses it. Until that failure is observed, building B2 preemptively would itself be the ceremony this wiki's own [[ai-research::wiki/intent-compiler/constructs/process-weights]] construct warns against elsewhere. [[wiki/agent-context/subtopics/retrieval/entities/qmd]]

**Approach B1 (custom meta-tool schema) and Approach C (compiled typed-edge graph) are now lower priority than this page originally suggested.** No real-world example surfaced in this research pass of a markdown knowledge base at this scale using either — every production example found (Claude Code, Cursor and peers, QMD, Anthropic's own Tool Search Tool) exposes either raw search primitives or a hybrid-search engine, not a custom compiled graph. B1 remains relevant for a different problem this wiki doesn't have yet: exposing a large *heterogeneous tool/API library* (GitHub's and Anthropic's real examples), not a *markdown corpus*.

The ETH Zurich finding that motivated the original recommendation still holds: **less is more**. It now argues more strongly for Approach 0 than for Approach A — a generated index is itself an artifact that can drift, and per Karpathy's own community feedback, drift (not scale) was the dominant failure mode reported in a comparable production deployment. [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]

## Implementation (2026-07-08)

**This is a deliberate early graduation, not a triggered one.** The concrete trigger stated above — the first real query Approach 0 actually misses — had not fired. The owner chose to build Approach B2 anyway: the infrastructure is cheap, and with multiple agents (Claude Code, Kiro, Codex) touching this repo, having the setup reproducible from a committed script mattered more than waiting for proof of need. Recorded here so this isn't misread later as evidence that Approach 0 failed. The choice and its rejected alternatives are recorded as a decision record: [[wiki/llm-wiki/decisions/adopt-agentic-search-with-qmd]].

**What was built:**

- `scripts/qmd-index.sh` — an idempotent script (pinned to `qmd@2.5.3` via `npx`) that initializes the local index on first run and re-syncs it on every later run (`qmd update`), then attempts `qmd embed`. This script, not the index it produces, is the source of truth: any agent/session reproduces the identical setup by running it, regardless of which ephemeral container it's in.
- `.qmd/` (the derived index/database directory) is gitignored, consistent with Invariant 1 below — the wiki's canonical content is never the index, and the index is never committed.
- The cross-agent Ingest Workflow (`AGENTS.md`, `schema/wiki/ingest.md`) now runs this script as a step after every ingest. The cross-agent Query Workflow (`AGENTS.md`, `schema/wiki/conventions.md`) now says to try `qmd search`/`qmd query` before falling back to `Grep`/`Glob` — this is the actual "qmd with grep fallback" shape.
- A Claude-Code-specific `SessionStart` hook (`.claude/settings.json`) runs the script in the background at the start of each session, as a convenience on top of the cross-agent workflow step — not a replacement for it, since Kiro and Codex don't read `.claude/settings.json`.

**A real, environment-specific limitation found while testing this:** `qmd search` (BM25 lexical, no model download) worked immediately and returned good results against this wiki. `qmd embed` (and therefore `qmd query`, the hybrid/semantic mode) failed in this sandboxed session because its embedding, reranking, and query-expansion models are hosted on `huggingface.co`, which this environment's network egress policy blocks (confirmed as a proxy-level CONNECT-tunnel denial, not a Hugging Face gating issue). `scripts/qmd-index.sh` treats this as non-fatal and reports it clearly rather than failing the whole run. This is specific to this sandboxed environment's network policy, not a defect in `qmd` itself — a local machine or a more permissive environment would likely get the full hybrid pipeline. Until/unless that's available here, this wiki's actual B2 in this environment is BM25-lexical-plus-grep, not full hybrid search — worth knowing before debugging a future "why did embed hang" report from scratch. This limitation has since been ratified as a standing constraint on the whole retrieval stack: [[wiki/agent-context/subtopics/retrieval/invariants/sandbox-compatible-retrieval]].

## Invariants

1. The wiki's markdown files are never modified for agent consumption — all surfacing artifacts are generated/served alongside the canonical content
2. Index/manifest generation is deterministic (no LLM in the loop) — per ETH Zurich, LLM-generated navigation aids hurt performance
3. The agent always has access to full page content — progressive disclosure controls *when* it's loaded, not *whether* it's accessible
4. Tags remain the primary cross-cutting retrieval facet; types and topics provide complementary axes
5. No retrieval infrastructure is built ahead of an observed failure of the simpler approach beneath it (Approach 0 before A/B, B before C) — overridden once, deliberately, by explicit owner choice; see Implementation above. The invariant remains the default; overriding it should stay a conscious, recorded exception, not a habit.

## Related Constructs

- [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] — Approach 0, the no-index default
- [[wiki/agent-context/subtopics/retrieval/entities/qmd]] — the concrete tool behind Approach B2
- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the theoretical model Approaches A/B/C implement
- [[wiki/llm-wiki/entities/open-knowledge-format]] — the format specification these approaches consume
- [[wiki/llm-wiki/constructs/three-layer-architecture]] — the production architecture (raw → wiki → schema)
- [[ai-research::wiki/intent-compiler/constructs/progressive-disclosure]] — the general UX principle
- [[ai-research::wiki/intent-compiler/constructs/process-weights]] — the ceremony-scaling principle this page's revised recommendation now leans on

## Open Design Questions

1. What is the first real query that Approach 0 actually misses for this wiki — has it happened yet, or is this still precautionary?
2. Should the tag index include page `confidence` levels to help the agent prioritize, if Approach A or B is ever built?
3. ~~Verify the "Cursor/Windsurf/Cline/Devin/Sourcegraph Amp dropped vectors" claim against each vendor's own documentation~~ — resolved 2026-07-07: false for Cursor, Windsurf, and GitHub Copilot; Sourcegraph Amp uses structural indexing, not grep. See [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]. Cline and Devin remain unverified.
4. If Approach B2 (`qmd`) is adopted, does its embedding/rerank model auto-download (~2GB) conflict with this environment's constraints, and does re-indexing need to run on every ingest or only periodically?
5. Can edge metadata be inferred from existing wikilinks, or must it always be explicitly typed, if Approach C is ever justified?

## Evidence and Rationale

- ObjectGraph demonstrates 92% token reduction with progressive disclosure — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]
- TagRAG shows hierarchical tags outperform flat retrieval at 78% win rate — [[wiki/agent-context/subtopics/retrieval/sources/tagrag-tag-guided-hierarchical-knowledge-graph-rag]]
- ETH Zurich proves that auto-generated context hurts; deterministic indexes are safe — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]
- Solo.io reports 91% token reduction with MCP progressive disclosure in production — [Keeping Context and Tokens Low With Progressive Disclosure In Agentgateway](https://www.solo.io/blog/keeping-context-and-tokens-low-with-progressive-disclosure-in-agentgateway)
- Synaptic Labs: 85-95% savings with meta-tool pattern (2 tools vs 33) — [The Meta-Tool Pattern: Progressive Disclosure for MCP](https://blog.synapticlabs.ai/bounded-context-packs-meta-tool-pattern)
- OKF spec explicitly leaves tag-browsing views to consumption time (§3.1) — [[wiki/llm-wiki/sources/open-knowledge-format-spec]]
- Anthropic removed vector search from Claude Code in favor of agentic search, reportedly outperforming the prior approach — [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]
- Karpathy's own primary gist names ~100 sources/hundreds of pages as where flat indexes stop scaling, and recommends local hybrid search (`qmd`) over embedding-RAG infrastructure — [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]
- QMD's architecture and MCP integration — [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]
- Anthropic's code-execution-with-MCP pattern and independent production corroboration — [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]] [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]]
- Community reception of code-execution-with-MCP, including substantive dissent — [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]]
- GitHub's own three-meta-tool progressive disclosure implementation and named security concerns — [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]]
- Karpathy pattern: index-first navigation is established practice — [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]
