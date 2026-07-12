---
title: "Source: ObjectGraph — From Document Injection to Knowledge Traversal"
type: source-capture
evidence: empirical-primary
description: "Introduces ObjectGraph (.og), a typed knowledge graph file format for agents with progressive disclosure, role-scoped access, and a two-primitive query protocol achieving 92% token reduction."
sources:
  - "[[raw/papers/objectgraph-document-injection-to-knowledge-traversal.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]]"
tags: [agent-context, progressive-disclosure, knowledge-graph, token-optimization, file-formats]
created: 2026-07-04
timestamp: 2026-07-04T22:43:00Z
---

# ObjectGraph — From Document Injection to Knowledge Traversal

## Source Identity

- Raw source: [[raw/papers/objectgraph-document-injection-to-knowledge-traversal.md]]
- Source type: paper
- Author(s): Mohit Dubey, Open Gigantic
- Published: 2026-04-30
- Original URL: https://arxiv.org/abs/2604.27820
- Scope: Proposes a new file format (.og) that reconceives documents as typed directed knowledge graphs for agent traversal rather than linear injection

## Core Contribution

Formalizes the "Document Consumption Problem" — the mismatch between linear document formats designed for human readers and the retrieval-oriented needs of LLM agents. Introduces ObjectGraph as a Markdown superset that enables selective node retrieval via a progressive disclosure model, achieving 60–95% token reduction without accuracy loss.

## Key Claims

- Documents designed for humans force agents to inject entire files into context, wasting 95.6% of tokens on irrelevant content (4.4% utilization rate for typical tasks)
- Context compounding in multi-turn loops makes this super-linear: a 5-turn loop with 3 document reads can compound 1,800 tokens into 15,000+
- No existing format (Markdown, JSON, YAML, TOON, llms.txt, GraphRAG, LSFS) satisfies all six required properties simultaneously
- ObjectGraph achieves 92.0% mean token reduction (2,340 → 187 tokens per query) with no statistically significant accuracy degradation (p > 0.05)
- The "less-is-more effect": removing irrelevant content not only saves tokens but improves accuracy by 2.8% due to reduced attention dilution
- ObjectGraph is a strict superset of Markdown — every .md file is valid .og, enabling incremental adoption

## Evidence and Results

**Token Reduction:**
- Mean consumption: 2,340 → 187 tokens (92.0% reduction, p < 0.001)
- Architecture B (Router/Executor): 36.5× reduction at turn 5 of multi-turn workflows (46,000 → 1,260 tokens)

**Task Accuracy (8 task types):**
- Matches or exceeds Markdown on 7/8 task types
- Dramatic improvements: Role-conditional access (+18.4%), Update detection (+30.1%), Assertion verification (+43.5%)
- Cross-node reasoning: small gap (1.8%) mitigated by explicit edge declarations

**Ablation:**
- Index routing + dense layer account for 82% of total token savings
- Edge declarations contribute remaining accuracy gains

**Transpiler Fidelity:**
- 98.7% content preservation on held-out benchmark
- No document below 0.95 deployment threshold after human review

**Human Authoring:**
- Mean burden: 2.8/7 Likert scale (18 participants)
- Participants found explicit content-type tags "more descriptive than Markdown"

## Methodology

- 240 documents across 5 classes (Skill Files, Operational Runbooks, Execution Plans, Technical Documentation, Knowledge Bases)
- 8 task types per document, each executed 5 times
- Primary model: Claude Sonnet 4.5; validation with Claude Haiku 4.5 and GPT-4o
- Baselines: Full Markdown injection, RAG with text-embedding-3-large, SkillReducer-optimised Markdown

## Limitations and Caveats

- Evaluation scale: 240 documents, carefully curated but not enterprise-scale diversity
- No multi-file federation — edges cannot reference nodes in other .og files (limits cross-repo knowledge graphs)
- No standards body or community governance yet — fragmentation risk
- No adversarial evaluation (misleading ::dense blocks or ::index entries)
- The paper makes bold claims about being the first format satisfying all six properties, but OKF (published shortly after) addresses similar concerns differently

## Important References and Linked Material

- [OKF v0.1 Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — Google's parallel effort at agent-friendly document format
- [llms.txt](https://llmstxt.org) — Earlier proposal for LLM-readable site descriptions
- [TOON format](https://toonformat.dev) — Token-Oriented Object Notation for structured data
- [FatCat (2025)](https://arxiv.org/abs/2602.02206) — Document-driven multi-agent system noting Markdown's alignment with LLM pretraining priors
- [Xiao et al. (2026)](https://doi.org/10.1145/3729486.3729495) — Trajectory reduction achieving 39.9–59.7% input token reduction on coding agents
- [MCP (Anthropic, 2024)](https://modelcontextprotocol.io) — Model Context Protocol for tool/data connections

## Contribution Routing

- Creates: `[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]` — the 3-pass reading depth model (index → dense → full)
- Creates: `[[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]]` — pattern where the LLM itself routes queries to relevant nodes
- Creates: `[[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]]` — formalization of the format mismatch
- Updates: `[[ai-research::wiki/token-economics/syntheses/token-cost-optimization]]` — adds document-level token reduction strategies

## Extraction Notes

- The paper's .og format is a strict superset of Markdown (backward compatible), unlike OKF which is a convention layer on top of standard Markdown
- The "six required properties" framework (P1: Selective Retrieval, P2: Compounding Elimination, P3: Typed Edges, P4: Role Scoping, P5: Executable Assertions, P6: Human Readability) provides a useful evaluation lens for any agent-document format
- The Progressive Disclosure Model maps directly to the wiki's existing index → page description → full page navigation pattern
