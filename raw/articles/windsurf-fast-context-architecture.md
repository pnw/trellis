# Windsurf (Codeium) — Fast Context Indexing Architecture

- Retrieved via: WebSearch aggregation of multiple third-party review/guide sites (no single canonical Codeium documentation page was independently fetched in this session), 2026-07-07
- Sources cited in the aggregated search results (not independently fetched): aiagentsquare.com, pinklime.io, codegen.com, programming-helper.com, myengineeringpath.dev

## Indexing Architecture

When a project is opened, Windsurf generates embeddings for files, functions, classes, and type definitions. The index is stored locally and updated incrementally as changes are made — described as a "local-first" approach to data handling.

## Retrieval System

Windsurf uses retrieval-augmented generation (RAG) to pull relevant context from across a project, described as "automatic context retrieval" that indexes the repository and uses embeddings to find relevant code for a task.

## Proprietary System: "Fast Context"

Windsurf's indexing is branded "Fast Context" — building an understanding of project architecture and dependencies without requiring manual file tagging or configuration. Cascade (Windsurf's agent) additionally tracks recent actions (file edits, terminal commands, linter warnings) to build "flow-aware" context reflecting current work.

## Performance Considerations

Reported to regularly hit 70-90% CPU usage on codebases over ~50K lines, described as a resource-intensive indexing engine.

## Relevance

This directly contradicts the framing (reported via a different, single aggregated source) that Windsurf "dropped vectors" for pure grep-based search. Windsurf's own (as described in third-party coverage) architecture is embeddings-first, not grep-first — see wiki source-capture Reliability Notes for how this is reconciled.
