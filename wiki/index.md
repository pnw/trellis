---
okf_version: "0.1"
---

# Index

See also: [[wiki/overview]] | [[wiki/roadmap]] | [[wiki/log]]

## LLM Wiki

### Sources
* [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]] — Claude Code thread surveying epistemic-grading frameworks (Admiralty, ICD 203, GRADE, Wikipedia, product patterns), designing the two-axis evidence/confidence schema, and ratifying the source-isolation invariant.
* [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]] — Codex research thread arguing that an LLM wiki is a selective context substrate for repeated AI workflows, project reasoning, and agent memory rather than a prompt dump or live data store.
* [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]] — Comprehensive guide to Karpathy's LLM Wiki pattern covering full architecture, setup, tooling, community ecosystem, and criticisms.
* [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]] — Deep research synthesis on what LLM wikis are useful for, when to use them, what to include, failure modes, and how they factor into AI projects.
* [[wiki/llm-wiki/sources/open-knowledge-format-spec]] — Google Cloud's OKF v0.1 spec formalizing the LLM Wiki pattern into a portable, vendor-neutral markdown knowledge format.
* [[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]] — Owner reframing that ratified wiki meta-work as a first-class research goal — the wiki as pilot instance for evolving llm-wiki practice — and coined the operational-evidence stream and self-experimentation protocol.
* [[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]] — Outside-observer critique of this wiki and the owner's responding design capture: one goal per wiki, repo split, portable schema, cross-wiki references, and a log taxonomy.
* [[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]] — Owner review of the federation design ratifying the breadcrumbs-over-rails simplifications — standalone normative schema, optional decision archaeology, prompt-based inheritance — and directing the design and naming of the upstream repo.
* [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]] — Point-in-time extract of this repository's own operational record — commit history with change stats, page counts, lint results, and the verbatim operation journal — snapshotted as first-party evidence about llm-wiki practice.

### Constructs
* [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — A knowledge management pattern where an LLM agent builds and maintains a structured markdown wiki from raw sources. Introduced by Karpathy, April 2026.
* [[wiki/llm-wiki/constructs/operational-evidence]] — First-party operational records — logs, git history, lint outputs, session transcripts — used as empirical sources for evaluating and evolving the very practices that produced them.
* [[wiki/llm-wiki/constructs/source-isolation]] — The invariant that a source-capture records only what its source says plus capture-time assessment derivable from the source alone — keeping captures regenerable, corroboration independent, and maintenance write-once.
* [[wiki/llm-wiki/constructs/three-layer-architecture]] — The structural foundation of the LLM Wiki pattern — raw sources, LLM-generated wiki, and schema with strict separation of concerns.

### Entities
* [[wiki/llm-wiki/entities/andrej-karpathy]] — Creator of the LLM Wiki pattern. Former Tesla AI director, OpenAI founding member, AI educator.
* [[wiki/llm-wiki/entities/open-knowledge-format]] — Google's OKF v0.1 (June 2026): formalizes the LLM wiki pattern into a portable, vendor-neutral spec. Markdown + YAML frontmatter, minimal required fields, designed for agent/human interop.
* [[wiki/llm-wiki/entities/yaml-frontmatter]] — A metadata convention placing a YAML block between triple-dashed lines at the top of a markdown file. Popularized by Jekyll (2008), now ubiquitous in static site generators, knowledge bases, and agent-readable formats like OKF.

### Syntheses
* [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]] — What intelligence analysis, evidence-based medicine, Wikipedia, PKM practice, and knowledge products teach about grading source reliability and claim credibility in a knowledge base.
* [[wiki/llm-wiki/syntheses/llm-wiki-effectiveness]] — Integrated understanding of when LLM wikis are useful, what content belongs in them, failure modes, and their role in AI-assisted projects.

### Assessments
* [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] — First operational-evidence verdict on this wiki's practice changes — what the evidence-tier adoption, schema-layer refactor, migrations, and lint tooling actually revealed, from the repo's own record.

### Comparisons
* [[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]] — How a curated llm-wiki relates to automatic agent-memory systems (Letta, Mem0, Zep/Graphiti) — same pipeline shape, different jobs, and two ideas worth borrowing without importing the machinery.
* [[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]] — Comparison of the LLM Wiki pattern vs RAG — LLM Wiki wins at personal/team scale, RAG wins at enterprise scale.

### Designs
* [[wiki/llm-wiki/designs/evidence-tier-schema]] — This wiki's two-axis epistemic schema: a required evidence tier on source-captures and rule-derived confidence on downstream pages, adapted from Admiralty, ICD 203, and GRADE.
* [[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]] — Design pattern for adapting an LLM wiki into a shared context, coordination, handoff, and evaluation layer for multi-agent implementation projects.
* [[wiki/llm-wiki/designs/project-wiki-application-guide]] — Operational guide for using this research wiki as a repertoire of agentic workflow knowledge and adapting it into project-specific implementation wikis.
* [[wiki/llm-wiki/designs/project-wiki-template]] — Reusable structure for adapting this AI research wiki into a codebase-specific knowledge base for agentic implementation workflows.
* [[wiki/llm-wiki/designs/trellis-repo-design]] — Specification for Trellis, the upstream wiki-method repository: distributable schema/scripts/seed surface, dogfood lab wiki, upgrade prompt, and bootstrap plan.
* [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]] — Draft design for the next evolution: one goal per wiki, the wiki method extracted into the Trellis upstream repository, breadcrumb-based schema inheritance for downstream instances, and outbound-only cross-wiki references with move-log forwarding.
* [[wiki/llm-wiki/designs/wiki-self-experimentation]] — The protocol by which this wiki evolves its own knowledge-base practices as a first-class research activity — hypothesis on change, operational-evidence snapshot, verdict assessment, confidence cascade.

### Decisions
* [[wiki/llm-wiki/decisions/adopt-agentic-search-with-qmd]] — Chose grep-based agentic search as the wiki's default retrieval with QMD-style local hybrid search as the graduation path, over embedding-RAG and bespoke index infrastructure.

### Invariants
* [[wiki/llm-wiki/invariants/raw-source-immutability]] — Files under raw/ are never edited in place; fidelity is what makes re-capture audits and upstream change detection possible.

## Agent Context

### Context Files

#### Sources
* [[wiki/agent-context/subtopics/context-files/sources/agents-md-efficiency]] — Paper finding AGENTS.md associated with lower median runtime and reduced output tokens for AI coding agents on pull-request tasks.
* [[wiki/agent-context/subtopics/context-files/sources/claude-code-agentic-manifests]] — Empirical study of 253 Claude.md files from 242 repositories, documenting common manifest structure and content.
* [[wiki/agent-context/subtopics/context-files/sources/claude-code-memory-docs]] — Official Claude Code documentation for CLAUDE.md loading, AGENTS.md imports, @ imports, path-scoped rules, and memory behavior.
* [[wiki/agent-context/subtopics/context-files/sources/configuration-smells-agents-md]] — Paper cataloging common smells in AGENTS.md and CLAUDE.md files, including Lint Leakage, Context Bloat, Skill Leakage, and Conflicting Instructions.
* [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]] — ETH Zurich study finding that LLM-generated context files hurt agent performance (-0.5 to -2%) while increasing costs (+20-23%); human-curated files help marginally (+4%).
* [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]] — Industry synthesis on context file best practices: only include non-inferable details, structure for machine parsing, accept ~20% token overhead tradeoff. Cites ETH Zurich study extensively.
* [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]] — Official Kiro documentation for steering files, inclusion modes, AGENTS.md support, scopes, and file references.
* [[wiki/agent-context/subtopics/context-files/sources/openai-codex-agents-md-docs]] — Official OpenAI documentation for Codex AGENTS.md discovery, precedence, override files, byte limits, and fallback filenames.

#### Constructs
* [[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]] — The empirical question of when repository-level agent context files help coding agents versus when they add cost, redundancy, or distraction.
* [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] — The principle that agent context files should contain only information the agent cannot discover independently — custom commands, non-standard tooling, counterintuitive constraints.

#### Entities
* [[wiki/agent-context/subtopics/context-files/entities/agents-md]] — A cross-tool standard for providing AI coding agents with persistent, project-specific operational guidance. Donated to the Agentic AI Foundation (Linux Foundation) in December 2025.

#### Designs
* [[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]] — A cross-platform pattern for keeping agent instructions portable across Codex, Claude Code, Kiro, and other coding agents without duplicating drifting manifests.

### Memory

#### Sources
* [[wiki/agent-context/subtopics/memory/sources/graphiti-readme]] — Official Graphiti (Zep) README describing temporal context graphs — facts with validity windows, entities that evolve, and full provenance back to the raw episodes that produced them.
* [[wiki/agent-context/subtopics/memory/sources/letta-readme]] — Official Letta (formerly MemGPT) README positioning stateful agents with self-improving memory, agent-managed memory blocks, and memory skills for continual learning.
* [[wiki/agent-context/subtopics/memory/sources/mem0-readme]] — Official Mem0 README describing a memory layer for personalized AI — ADD-only single-pass extraction, entity linking, fused multi-signal retrieval, temporal ranking, and self-reported benchmark results.

### Retrieval

#### Sources
* [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]] — Introduces ObjectGraph (.og), a typed knowledge graph file format for agents with progressive disclosure, role-scoped access, and a two-primitive query protocol achieving 92% token reduction.
* [[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]] — Proposes LLM-Wiki, an agent-native retrieval system that compiles documents into structured wiki pages with bidirectional links and self-correction, outperforming HippoRAG 2, LightRAG, and GraphRAG.
* [[wiki/agent-context/subtopics/retrieval/sources/tagrag-tag-guided-hierarchical-knowledge-graph-rag]] — Proposes hierarchical domain tag chains for knowledge graph construction and retrieval, achieving 78% win rate over baselines with 14.6× construction efficiency vs GraphRAG.
* [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]] — Karpathy's primary gist on the LLM Wiki pattern, naming ~100 sources/hundreds of pages as where flat indexes stop scaling and recommending local hybrid search over embedding-RAG infrastructure.
* [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]] — Reports Anthropic's May 2025 removal of vector search from Claude Code in favor of grep/glob-driven agentic search, with industry follow-on at Cursor, Windsurf, Cline, Devin, and Sourcegraph Amp.
* [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]] — README for QMD, an open-source on-device hybrid (BM25 + vector + rerank) search tool for markdown knowledge bases with a native MCP server, created by Tobi Lütke.
* [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]] — Anthropic's official post proposing agents call MCP tools via generated code against a filesystem-style API rather than direct tool calls, citing ~98.7% token reduction.
* [[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]] — Anthropic's Tool Search Tool release: `defer_loading` lets tools become discoverable on demand, citing ~85% token reduction.
* [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]] — A 112-tool production MCP server for GitHub validating the code-execution-with-MCP pattern at ~99.2% tool-definition token reduction, with author-disclosed caveats.
* [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]] — Community reception of Anthropic's code-execution-with-MCP post: independent benchmarks plus substantive dissent on lost tool guidance and auditability.
* [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]] — GitHub's own three-meta-tool progressive disclosure implementation, plus named security concerns about default flags and secret exposure via process lists.
* [[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]] — Cursor's official docs describing a hybrid architecture: Merkle-tree-synced embeddings (Turbopuffer) alongside grep, agent-selected per query shape.
* [[wiki/agent-context/subtopics/retrieval/sources/windsurf-fast-context-architecture]] — Third-party coverage describing Windsurf's embeddings-first "Fast Context" RAG system, contradicting a claim that Windsurf dropped vector search.
* [[wiki/agent-context/subtopics/retrieval/sources/github-copilot-embedding-model-2026]] — GitHub's new Copilot embedding model announcement, disclosing an adaptive embeddings-with-TF-IDF-fallback architecture keyed to diff size.
* [[wiki/agent-context/subtopics/retrieval/sources/sourcegraph-context-engineering-hybrid]] — Sourcegraph's framing of 2026 retrieval consensus as hybrid (grep + embeddings + structural indexing), and Amp's own SCIP-based code-graph architecture.

#### Constructs
* [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] — Retrieval performed by an agent iteratively calling glob/grep/read directly over a raw corpus, instead of a pre-built index, embedding store, or bespoke retrieval schema.
* [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] — The phenomenon where irrelevant content in an LLM's context window actively degrades accuracy — not just wastes tokens. The 'less-is-more effect.'
* [[wiki/agent-context/subtopics/retrieval/constructs/context-compounding]] — Super-linear token cost growth in multi-turn agent loops caused by stateless API re-transmission of conversation history including previously-read documents.
* [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]] — The fundamental mismatch between linear document formats designed for human readers and the retrieval-oriented needs of LLM agents, formalized as the Full-Read Assumption.
* [[wiki/agent-context/subtopics/retrieval/constructs/domain-centric-knowledge-fusion]] — Pre-summarizing knowledge at each tag/domain level so retrieval returns synthesized global context rather than raw fragments.
* [[wiki/agent-context/subtopics/retrieval/constructs/hierarchical-tag-chains]] — Tags organized as a directed acyclic graph (DAG) with root domain tags, intermediate domain tags, and leaf object tags — enabling hierarchical knowledge retrieval.
* [[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]] — Pattern where the LLM itself semantically routes queries to relevant knowledge nodes by reading a lightweight index, replacing keyword matching or embedding similarity.
* [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]] — Two-or-more registered meta-tools (or a deferred-loading flag) replace N tool schemas, reducing startup token cost by 85–99% while enabling progressive disclosure of capabilities.
* [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — A layered reading-depth model for agent document consumption: index (routing) → dense (keywords) → full (complete content), enabling 60–95% token reduction.
* [[wiki/agent-context/subtopics/retrieval/constructs/retrieval-as-reasoning]] — Paradigm where retrieval behaves like reasoning — agents search, read, traverse links, and decide when evidence is sufficient — rather than one-shot context fetching.

#### Entities
* [[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]] — Anthropic's open protocol (2024) for connecting AI agents to tools and data sources via a standardized JSON-RPC interface. Enables progressive tool disclosure and knowledge serving.
* [[wiki/agent-context/subtopics/retrieval/entities/objectgraph-format]] — A file format (Dubey, 2026) that reconceives documents as typed directed knowledge graphs for agent traversal. Strict Markdown superset with progressive disclosure, role scoping, and a two-primitive query protocol.
* [[wiki/agent-context/subtopics/retrieval/entities/qmd]] — An open-source, on-device hybrid search tool (BM25 + vector + LLM rerank) for markdown knowledge bases with a native MCP server, created by Shopify's Tobi Lütke.

#### Comparisons
* [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]] — Vendor-by-vendor survey of Claude Code, Cursor, Windsurf, GitHub Copilot, Sourcegraph Amp, and OpenAI Codex CLI retrieval architectures, correcting an overstated "industry abandoned embeddings" framing.

#### Designs
* [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] — Design exploration of approaches for surfacing an OKF knowledge graph to agents: agentic search, static index layers, MCP-based tool discovery/hybrid search, and compiled graph strategies.

#### Invariants
* [[wiki/agent-context/subtopics/retrieval/invariants/sandbox-compatible-retrieval]] — No load-bearing step of this wiki's query workflow may require network egress at query time — every retrieval path must degrade to tools that work in a sandboxed session.

## Overview

### Syntheses
* [[wiki/overview]] — High-level synthesis of the Trellis wiki method: the llm-wiki pattern lineage, this method's schema and epistemics, agent context and retrieval, and federation.

### Roadmap
* [[wiki/roadmap]] — Forward-looking backlog: open design questions, candidate topics, self-maintenance items, and the meta-experiment log.
