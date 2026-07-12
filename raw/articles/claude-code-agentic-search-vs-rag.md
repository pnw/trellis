# Claude Code's Move From Vector Search to Agentic Search (Grep-Based Retrieval)

- Primary reported source: Gergely Orosz, "Building Claude Code with Boris Cherny," Pragmatic Engineer newsletter — https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
- Retrieved via: WebSearch aggregation (direct WebFetch to pragmaticengineer.com returned HTTP 403 in this session; content below is the search engine's synthesized summary of the interview, corroborated by independent secondary write-ups, not a direct fetch of the original interview text)
- Corroborating secondary sources found in the same search pass (titles only, not independently fetched):
  - "AI Agents Don't Need Vector Search Anymore: Inside the Agentic Search Stack Replacing RAG in 2026" — Abdullah Grewal, Medium, May 2026 — https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f
  - "Why Claude Code is special for not doing RAG/Vector Search and instead just using tool calling (Grep, etc)" — Aram, Medium — https://zerofilter.medium.com/why-claude-code-is-special-for-not-doing-rag-vector-search-agent-search-tool-calling-versus-41b9a6c0f4d9
  - "Why Grep Beat Embeddings in Our SWE-Bench Agent (Lessons from Augment)" — Systematically Improving RAG Applications — https://567-labs.github.io/systematically-improving-rag/talks/colin-rag-agents/
  - Hacker News discussion: "I found out that Claude Code and OpenCode doesn't do vector search and embedding..." — https://news.ycombinator.com/item?id=46631689
- Retrieved: 2026-07-07

## The Change

In May 2025, Anthropic removed vector search from Claude Code — eliminating the embedding pipeline, local vector database, and chunking heuristics — and replaced them with grep-based agentic search. According to Claude Code's creator Boris Cherny, the result "outperformed everything. By a lot."

## Stated Rationale

Boris Cherny explained that early versions of Claude Code used RAG plus a local vector database, but the team found that agentic search generally worked better, and was also simpler — avoiding recurring issues around security, privacy, staleness, and reliability that the embedding pipeline introduced. Approaches tried and abandoned included local vector databases and recursive model-based indexing; both had downsides such as stale indexes and permission complexity.

## What Replaced It

Claude Code's "agentic search" is described as, functionally, glob and grep driven by the model: the agent lists directories, greps for exact names/strings/routes/errors, reads promising files, follows imports/references, inspects tests, and runs code — iteratively asking for more evidence rather than receiving one static bundle of retrieved chunks up front.

## Industry Follow-On

Cursor hired engineers involved in this decision. Windsurf, Cline, Devin, and Sourcegraph Amp are reported to have also dropped vector-based retrieval in favor of tool-driven (grep/glob) search for code understanding.

## Scope Caveat (from the broader search synthesis, not specific to Cherny's remarks)

Coverage of this topic cautions that this does not make embeddings/RAG universally obsolete: for narrow, well-defined queries over very large corpora, retrieval remains valuable, and a common recommended pattern is exposing embedding-based retrieval itself as a callable tool inside an agentic loop rather than a static upfront context bundle.
