# Anthropic: "Introducing Advanced Tool Use on the Claude Developer Platform" (Tool Search Tool)

- Source URL: https://www.anthropic.com/engineering/advanced-tool-use
- Publisher: Anthropic (official engineering blog)
- Published: 2026 (exact date not confirmed; direct fetch returned HTTP 403 in this session)
- Retrieved via: WebSearch aggregation, 2026-07-07
- Capture note: direct fetch of the original post was not possible in this session (HTTP 403). Content below reflects the WebSearch engine's summarized extraction of the post, not verbatim text.

## What It Introduces

A "Tool Search Tool" capability for the Claude Developer Platform, letting Claude dynamically discover relevant tools instead of loading every tool definition into context upfront. Developers provide the full set of tool definitions to the API but mark individual tools with a `defer_loading: true` flag, making those tools discoverable on-demand rather than always-loaded.

## Reported Results

- Cited as an 85% reduction in token usage for tool-definition overhead while preserving access to the full tool library (i.e., no capability is actually removed — only its always-loaded cost).
- Framed alongside "programmatic tool calling" as part of the same advanced-tool-use release.

## Relationship to Other Anthropic Posts

Secondary coverage groups this post with "Effective context engineering for AI agents" and "Code execution with MCP" (see [[raw/articles/anthropic-code-execution-with-mcp.md]]) as a connected 2025–2026 sequence: context framework, tool design guidance, and two complementary mechanisms (code-execution-based tool access, and on-demand tool-schema discovery) for keeping large tool libraries cheap to carry.
