---
title: Meta-Tool Pattern
type: construct
description: "Two registered tools (discovery + execution) replace N tool schemas, reducing startup token cost by 85–95% while enabling progressive disclosure of capabilities."
sources:
  - https://blog.synapticlabs.ai/bounded-context-packs-meta-tool-pattern
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
tags: [agent-context, agents, architecture, design-patterns, mcp]
created: 2026-07-05
timestamp: 2026-07-07T20:45:00Z
confidence: high
novelty: emerging
coined_by: "Synaptic Labs (January 2026); independently validated and extended by Anthropic (Claude Skills, Code Execution with MCP, Tool Search Tool) and GitHub's own MCP server"
aka: ["bounded context packs", "BCP", "two-tool pattern", "progressive tool disclosure"]
---

# Meta-Tool Pattern

## Definition

An architectural pattern for MCP (Model Context Protocol) servers where all available tools are exposed through exactly two registered meta-tools — a discovery tool and an execution tool — rather than registering each tool individually. The discovery tool's description contains the complete capability index; the execution tool handles invocation of any requested capability.

## Why It Matters

Enterprise MCP servers can have dozens to hundreds of tools. Registering all of them loads every schema into the context window at session start (~250 tokens per tool × 33 tools = ~8,250 tokens). Most tasks use only 2–5 tools. The meta-tool pattern reduces startup cost to ~600 tokens and loads individual schemas on demand (~150 tokens per tool requested).

## Mechanism / Structure

**Two meta-tools:**

| Tool | Purpose |
|------|---------|
| Discovery tool | Description contains capability index (all agents/tools listed). When called with parameters, returns specific tool schemas. |
| Execution tool | Accepts tool name + arguments, executes the requested tool with shared session context. |

**Three-layer architecture (Synaptic Labs):**

1. **Meta-Tools** (entry points) — the 2 tools the MCP client sees
2. **Agents** (domain containers) — group related tools by bounded context (content, search, storage, memory)
3. **Tools** (atomic operations) — individual operations within each agent

**Token savings:**

| Approach | Startup Cost | Per-Task Cost |
|----------|-------------|---------------|
| Traditional (33 tools) | ~8,000 tokens | +0 |
| Meta-Tool (2 tools) | ~600 tokens | ~150 tokens/tool requested |

For a typical 3–5 tool task: 1,050–1,350 tokens vs. 8,000+.

**Discovery tool description serves as the routing index:**
```
Agents:
canvasManager: [read, write, update, list]
contentManager: [read, update, write]
storageManager: [list, move, copy, archive, ...]
searchManager: [searchContent, searchDirectory, searchMemory]
memoryManager: [createWorkspace, loadWorkspace, ...]
```

The LLM reads this index ([[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]] pattern) and requests only the schemas it needs.

## Variants (2026-07-07 Update)

Real-world implementations have diverged into more than the original two-tool schema:

| Variant | Tool Count | Notable Implementation |
|---|---|---|
| Two-tool discover/execute | 2 | Synaptic Labs Bounded Context Packs, ObjectGraph's `search_index`/`resolve_context` |
| Three-tool list/inspect/enable | 3 | GitHub's own MCP server: `list_available_toolsets`, `get_toolset_tools`, `enable_toolset`, reporting 60-80% context reduction — [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]] |
| Deferred-loading flag (no separate meta-tool) | 0 extra tools | Anthropic's Tool Search Tool: individual tools marked `defer_loading: true` become discoverable on demand; ~85% token reduction with the full tool library still nominally available — [[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]] |
| Code execution over a filesystem-style API | 0 extra tools (code, not tool calls) | Anthropic's Code Execution with MCP: agent writes code against MCP servers presented as a discoverable filesystem; ~98.7% reduction on a cited example, independently corroborated at ~99.2% in a 112-tool production GitHub MCP server — [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]] [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]] |

The code-execution variant trades the meta-tool's explicit discovery step for letting the model navigate a directory structure directly in generated code — a materially different mechanism from the original pattern, not just a naming variant, and it inherits different risks (see Security and Reliability Notes below).

## Security and Reliability Notes

GitHub's own three-meta-tool implementation surfaced a live disagreement: defaulting to `--read-only` inverts secure-by-default (an `--allow-edit` opt-in would be safer), and secrets passed via environment variables remain visible in process lists (CWE-214) — reduced but not eliminated by containerization. [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]]

Community reaction to the code-execution variant raised a further, more fundamental concern: routing tool access through generated code can strip out the inline guidance that direct tool descriptions/responses normally carry mid-task, and auditing dynamically generated and executed code is an open problem — not a solved one. [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]] Adopt this variant deliberately, not by default.

## Distinctions

- Not the same as MCP's dynamic tool discovery (which changes tool *availability* at runtime; meta-tool keeps all tools available but loads schemas on demand)
- Not a part of the MCP spec itself — it's a design pattern layered on top
- The "bounded context" grouping (agents) follows domain-driven design principles — tools with different cognitive modes (reading vs. searching vs. writing) are separated
- Related to but independent of [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — same principle (show index first, load detail on demand) applied to tool schemas instead of documents
- Distinct from [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] — that construct forgoes any tool-schema layer entirely and searches the raw corpus with generic file primitives; this pattern is specifically about managing *tool* discovery cost, not document retrieval

## Evidence and Sources

- Synaptic Labs: 85–95% token savings; local models (8K context) become viable — [The Meta-Tool Pattern: Progressive Disclosure for MCP](https://blog.synapticlabs.ai/bounded-context-packs-meta-tool-pattern)
- Anthropic's own "Code Execution with MCP" post (Nov 2025), captured directly rather than secondhand — [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]], independently corroborated in production — [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]]
- Anthropic's Tool Search Tool (`defer_loading`), a directly shipped platform feature distinct from the code-execution variant — [[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]]
- Solo.io agentgateway: `toolMode: Search` replaces tool list with `get_tool` + `invoke_tool`, reports 91% token reduction — [Solo.io blog](https://www.solo.io/blog/mcp-progressive-disclosure)
- GitHub's own MCP server: three-meta-tool variant with real production numbers and named security caveats — [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]]
- Claude Skills: Anthropic's production implementation — skills are domain-organized capability packs that load contextually
- ObjectGraph's two-primitive protocol (`search_index` + `resolve_context`) is the document-format analog — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the broader principle these tools implement
- [[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]] — the routing mechanism operating on the discovery tool's index
- [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] — Approach B implements this pattern for knowledge bases
- [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] — the no-tool-schema alternative for document (not tool) retrieval
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] — the discovery index should contain only what aids routing
