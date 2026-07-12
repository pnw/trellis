---
title: Agentic Search
type: construct
description: Retrieval performed by an agent iteratively calling generic search primitives (glob, grep, read) directly over a raw corpus, gathering evidence step by step, instead of pre-computing an index, embedding store, or bespoke retrieval schema.
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/windsurf-fast-context-architecture]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/github-copilot-embedding-model-2026]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/sourcegraph-context-engineering-hybrid]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/qmd]]"
  - "[[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]"
tags: [agent-context, retrieval, embeddings, coding-agents]
created: 2026-07-07
timestamp: 2026-07-07T22:15:00Z
confidence: low
novelty: emerging
aka: ["grep-based search", "tool-driven search", "glob-and-grep retrieval"]
coined_by: "Practitioner usage at Anthropic, circa 2025 — not a general industry consensus (see Corrigendum)"
---

# Agentic Search

## Definition

Agentic search is a retrieval pattern where the agent itself, using generic file-search primitives (glob, grep, read, list-directory), iteratively explores a raw corpus at query time — listing likely files, searching for exact names/strings/identifiers, reading promising files, and following references — rather than consulting a pre-built index, embedding store, or bespoke retrieval schema. The model does not receive one static bundle of retrieved content up front; it keeps asking for more evidence as it learns what it needs. [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]

## Why It Matters

Every other retrieval strategy in this wiki's `agent-context` topic — [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]], the meta-tool pattern, compiled graphs — assumes *some* pre-built artifact (an index, a manifest, a vector store, a typed edge set) has to be constructed and maintained before an agent can retrieve efficiently. Agentic search is the degenerate case that assumes none of that: it requires zero build step and zero maintenance, at the cost of per-query search latency and reliance on the corpus itself being greppable (meaningful file names, in-body text matching what a query would use).

It matters here because it is reportedly the reason Anthropic removed vector search from Claude Code in May 2025. [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]

## Corrigendum (2026-07-07)

The claim that Cursor, Windsurf, Cline, Devin, and Sourcegraph Amp converged on the same pure-grep choice — captured in the initial version of this page from a single aggregated secondary source — does not hold up against those vendors' own documentation and was **overstated**. Direct vendor-level research found:

- **Cursor** is explicitly hybrid: a Merkle-tree-synced embeddings pipeline (Turbopuffer vector DB) alongside grep, with the agent choosing per query shape. [[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]]
- **Windsurf** is embeddings-first ("Fast Context" RAG), with no grep-first framing found in vendor-adjacent coverage. [[wiki/agent-context/subtopics/retrieval/sources/windsurf-fast-context-architecture]]
- **GitHub Copilot** is embeddings-first with a lexical (TF-IDF) fallback triggered by diff size — the inverse framing of "grep by default." [[wiki/agent-context/subtopics/retrieval/sources/github-copilot-embedding-model-2026]]
- **Sourcegraph Amp** uses structural code-graph (SCIP) indexing — neither pure grep nor embeddings, a third category. [[wiki/agent-context/subtopics/retrieval/sources/sourcegraph-context-engineering-hybrid]]

The corrected picture (full detail in [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]): Claude Code's pure-grep design is real and distinctive, but it is the **exception**, not the industry norm. The actual 2026 consensus across vendors is **hybrid retrieval** — grep/agentic search for exact matches, embeddings or structural indexing for conceptual/relational queries, selected per query shape. This construct remains valid as a description of what Claude Code (and, per Cursor's own docs, Cursor's "Instant Grep" mode) does — it should not be read as evidence of a general industry abandonment of embeddings.

## Mechanism / Structure

Reported operational loop: `glob` for likely files -> `grep` exact names, strings, routes, errors, flags -> `read` promising files -> follow imports/references -> inspect tests -> run the code, repeating as understanding deepens. [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]

Stated rationale for abandoning the embeddings-based alternative was not primarily about retrieval quality but about operational cost: vector indexes go stale as the corpus changes, embedding pipelines introduce their own security/permission surface, and reliability suffered relative to a much simpler mechanism. [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]

## Distinctions

- Not the same as the progressive disclosure model ([[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]) — that model still assumes an index/dense/full staged artifact; agentic search has no staged artifact at all, only live tool calls against the raw corpus.
- Not a rejection of retrieval augmentation in general — reported industry commentary alongside this shift cautions that narrow, well-defined queries over very large corpora can still benefit from embeddings, typically exposed as a callable tool inside the same agentic loop rather than as a static upfront context bundle.
- Not necessarily applicable beyond corpora an agent can efficiently glob/grep — a corpus with meaningless filenames, no in-body keyword overlap with likely queries, or requiring cross-lingual/semantic matching is a weaker fit.
- Distinct from (but compatible with) local hybrid search tools like `qmd` ([[wiki/agent-context/subtopics/retrieval/entities/qmd]]), which add lexical+semantic+rerank retrieval on top of a markdown corpus rather than relying on the raw filesystem search primitives alone.

## Evidence and Sources

- Primary grounding: reported removal of vector search from Claude Code (May 2025) — [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]. This claim remains single-source and unverified against Anthropic's own documentation directly (WebFetch to anthropic.com was blocked throughout this research pass); treat "outperformed everything" as a strong practitioner account, not a settled benchmark.
- The broader "industry converged on grep-only" framing is **corrected**, not corroborated, by direct vendor research — see the Corrigendum above and [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]. Confidence is `low` accordingly: the one claim this construct can support with any confidence (Claude Code specifically) is itself unverified against a primary source, and the generalization it was initially built on turned out to be wrong.

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the staged-artifact alternative this construct forgoes
- [[wiki/agent-context/subtopics/retrieval/entities/qmd]] — a concrete tool that adds structured hybrid search back on top of a raw markdown corpus without full embedding-RAG infrastructure
- [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] — where this construct is evaluated as an option for this wiki specifically

## Open Questions

- Does this actually generalize to prose/markdown knowledge bases (frontmatter, wikilinks, natural-language descriptions), or is the evidence specific to source-code retrieval, where identifiers and file structure carry more of the semantic load than in prose?
- ~~Verify the claimed abandonment of vector search at Cursor, Windsurf, Cline, Devin, and Sourcegraph Amp against each vendor's own documentation~~ — resolved 2026-07-07: false for Cursor, Windsurf, and GitHub Copilot (all embeddings-first or hybrid per their own material); Sourcegraph Amp uses structural indexing, not grep. See Corrigendum. Cline and Devin remain unverified against primary sources.
- At what corpus size or query-vocabulary mismatch (query terms not appearing verbatim in the corpus) does agentic search's recall degrade enough to need a semantic layer?
- Verify Anthropic's own "outperformed everything" claim for Claude Code against Anthropic's own documentation directly — every attempt to fetch anthropic.com in this research pass was blocked, so even the one claim this construct rests on is not yet primary-sourced.
