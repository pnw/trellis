---
title: Model Context Protocol (MCP)
type: entity
description: "Anthropic's open protocol (2024) for connecting AI agents to tools and data sources via a standardized JSON-RPC interface. Enables progressive tool disclosure and knowledge serving."
sources:
  - https://modelcontextprotocol.io
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]]"
  - "[[designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
tags: [agent-context, agents, standards, mcp]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: high
novelty: emerging
aka: ["MCP", "Model Context Protocol"]
---

# Model Context Protocol (MCP)

## Identity

An open protocol published by Anthropic (2024) that standardizes how AI agents connect to external tools and data sources. Uses JSON-RPC over local (stdio) or remote (Streamable HTTP) transports. Donated to the Agentic AI Foundation (Linux Foundation) alongside AGENTS.md and Goose in December 2025.

- **Created by**: Anthropic (2024)
- **Spec**: https://modelcontextprotocol.io
- **Transport**: stdio (local) or Streamable HTTP (remote)
- **Core primitives**: `tools/list`, `tools/call`, `notifications/tools/list_changed`
- **Governed by**: Agentic AI Foundation (AAIF), Linux Foundation

## Relevance to the Wiki

MCP is the enabling technology for Approach B in [[designs/knowledge-surfacing-design]] — exposing a wiki's knowledge graph through tool calls rather than static file injection. A wiki MCP server would expose `discover_knowledge` and `read_knowledge` tools, enabling depth-controlled retrieval.

MCP is also the substrate on which the [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]] operates — progressive tool disclosure is layered on top of the MCP spec (not part of it).

## Associated Artifacts

### Supported Clients (as of mid-2026)

Claude Code, Cursor, VS Code (GitHub Copilot), Windsurf, MCP Inspector, custom applications via SDKs (TypeScript, Python, Rust, Java, C#, Swift, Kotlin).

### Progressive Disclosure Support

MCP's spec defines `tools/list` and `tools/call` but does **not** include a `get_tool(name)` primitive for on-demand schema retrieval. Progressive disclosure (the [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]]) is layered on top:

- Solo.io agentgateway: `toolMode: Search` → replaces tool list with 2 meta-tools
- Synaptic Labs: Bounded Context Packs → custom discovery/execution layer
- Anthropic Claude Skills: domain-organized capability packs loaded contextually

### Related Standards

| Standard | Relationship to MCP |
|----------|-------------------|
| AGENTS.md | Static context files (complementary — instructions vs. tools) |
| OKF v0.1 | Knowledge format MCP servers could serve |
| A2A (Agent-to-Agent) | Google's protocol for agent-to-agent communication (parallel, not competing) |
| llms.txt | Static site index (no tool interaction; MCP is dynamic) |

## Notes

- MCP is the *dynamic* complement to static context files: AGENTS.md tells the agent what it should know; MCP gives it tools to discover and act
- The protocol is intentionally minimal — complexity lives in servers, not the protocol itself
- Enterprise adoption is driving extensions: authentication, rate limiting, observability (Solo.io, Google)
- For this wiki, an MCP server becomes valuable when the wiki exceeds the scale where static index injection is sufficient (~100+ pages per the design doc analysis)
