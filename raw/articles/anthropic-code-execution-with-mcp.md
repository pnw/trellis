# Anthropic: "Code Execution with MCP: Building More Efficient Agents"

- Source URL: https://www.anthropic.com/engineering/code-execution-with-mcp
- Publisher: Anthropic (official engineering blog)
- Published: 2025-11-07 (per third-party citations; direct fetch of the original returned HTTP 403 in this session)
- Retrieved via: WebSearch aggregation plus a GitHub community discussion thread that quotes and summarizes the post (https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1780), 2026-07-07
- Capture note: direct fetch of anthropic.com and of secondary write-ups (MarkTechPost, aimultiple, theunwindai) all returned HTTP 403 in this session. Content below is reconstructed from WebSearch snippet summaries plus the GitHub discussion's direct quotation of the post's stated problem/solution — treat numeric claims as approximate pending a future direct capture.

## Problem

Direct tool calls consume substantial context: every tool definition and every tool response occupies tokens, which limits how many tools and how much intermediate data an agent can work with before the context window becomes the bottleneck.

## Solution

Instead of calling MCP tools directly through the model's context, have the agent write and execute code that calls those tools, with MCP servers presented to the agent as a discoverable filesystem/code API (the agent can list available servers and read tool-definition files, similar to browsing a directory) inside a sandboxed execution environment (reported as a sandboxed TypeScript/JS runtime in secondary coverage).

## Reported Results

- A workflow that previously consumed roughly 150,000 tokens when tool calls and intermediate data were passed directly through the model was reimplemented with code execution against filesystem-style MCP APIs at roughly 2,000 tokens — a reduction cited as approximately 98.7%.
- Secondary coverage frames this as part of a three-post 2026 trilogy from Anthropic's engineering blog: "Effective context engineering for AI agents," "Writing effective tools for AI agents," and this "Code execution with MCP" post.

## Independent Corroboration

A community-maintained MCP server for GitHub (112 tools) reported validating this pattern in production: traditional per-tool-definition token cost of ~150,000 tokens fell to ~1,200 tokens (~99.2% reduction on tool-definition overhead alone) after adopting the code-first approach, alongside large cold-start latency and memory improvements from connection pooling. See raw/articles/mcp-github-production-code-execution-results.md for the full discussion capture.

## Stated/Implied Limitations (from community discussion, not the original post directly)

- Bypassing the model's direct view of tool calls risks losing "guiding instructions" that tool descriptions/responses normally carry mid-task (a concern raised by a community reviewer, not Anthropic itself).
- The filesystem-style discovery abstraction has been called under-specified ("handwavy") by at least one MCP maintainer, who argued for protocol-level solutions (e.g., GraphQL-style introspection) instead.
- Auditability of dynamically generated/executed code is an open concern raised in community discussion.
