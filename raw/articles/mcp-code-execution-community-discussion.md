# Community Discussion: "Code Execution with MCP" (Anthropic Post) Reception and Reports

- Source URL: https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1780
- Publisher: official Model Context Protocol GitHub organization, community discussion thread
- Retrieved via: WebFetch (direct, successful), 2026-07-07

## Original Anthropic Post (referenced, Nov 7, 2025)

Problem: direct tool calls consume substantial context — each tool definition and response occupies tokens, limiting agent scalability. Solution: have agents write and execute code to call tools, treating MCP servers as a discoverable filesystem where agents list directories to find available servers and read tool-definition files. (Specific token-reduction numbers were not detailed within this discussion thread itself; see [[raw/articles/anthropic-code-execution-with-mcp.md]] for the figures reported elsewhere.)

## Independent Implementation Reports

- **@olaservo** (Nov 21, 2025): Benchmarked code execution vs. direct MCP on GitHub issue analysis. On a large dataset (5,205 issues), code execution succeeded 100% of the time vs. 0% for direct MCP (context overflow). On small datasets, code execution was 3.5x faster and 67% cheaper.
- **@pietrozullo** (Nov 20, 2025): Built "code_mode" support for MCP, noting potential advantages for navigating large JSON returns.
- **@jsaldanaperez** (Apr 27, 2026): Testing across 3 languages x 2 models showed 11-15x shorter agent loops when MCP servers return many artifacts, with output-token reductions of 70-77%.

## Critical / Dissenting Views

- **@scottyak-datadog** (Nov 7, 2025): Warned that bypassing the model's direct view of tool calls strips away "guiding instructions" — MCP servers provide both data and iterative guidance normally. Proposed a dual-channel pattern separating instruction metadata from structured data.
- **@rkondra-eightfold** (Nov 24, 2025): Called the filesystem-discovery abstraction "handwavy," arguing for protocol-level solutions (e.g., GraphQL-style introspection, standardized output schemas) instead.
- **@cliffhall** (thread maintainer, Nov 7, 2025): Noted that folder-based tool discovery lacks descriptive metadata, placing a heavy burden on tool naming alone.
- **@sudhanva99-cpu** (Nov 11, 2025): Questioned how to validate dynamically generated code and handle runtime failure scenarios.
- **@caioribeiroclw-pixel** (Jun 2, 2026): Advocated for boundary records tracking schema discovery, data reads withheld from the model, generated code, and promoted outputs — enabling inspection of context routing without storing private payloads.

## Alternative Approaches Proposed in Thread

- **@xwhysi** (Nov 8, 2025): Proposed dynamic tool loading with custom interception logic instead of LLM-generated code execution.
- **@BobDickinson** (Jan 17, 2026): Built "No Code Code Mode" — directed graphs for tool orchestration without actual code execution.

## Summary Assessment

The thread shows genuine practical benefits (large-dataset success rate, speed, cost) alongside unresolved tensions: loss of inline guidance normally carried by tool responses, an underspecified discovery abstraction, and open auditability/security questions about executing model-generated code against live tools.
