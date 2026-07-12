---
title: AGENTS.md
type: entity
description: "A cross-tool standard for providing AI coding agents with persistent, project-specific operational guidance. Donated to the Agentic AI Foundation (Linux Foundation) in December 2025."
sources:
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]]"
tags: [agent-context, agents, standards]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: high
novelty: emerging
aka: ["AGENTS.md", "agents.md", "agent context file"]
---

# AGENTS.md

## Identity

AGENTS.md is a markdown file placed at the root of a repository that provides AI coding agents with persistent, project-specific operational guidance: build commands, coding conventions, testing rules, and constraints the agent cannot infer from the codebase alone.

- **Created by**: OpenAI (for Codex)
- **Donated to**: Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, December 2025
- **Co-donated alongside**: Anthropic donating MCP, Block donating Goose
- **Spec repo**: https://github.com/agentsmd/agents.md
- **Definition**: "Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide context and instructions to help AI coding agents work on your project."

## Relevance to the Wiki

AGENTS.md is the code-repository analog of this wiki's `.kiro/steering/` directory. Both provide persistent context to an agent. The key lessons from ETH Zurich's evaluation of AGENTS.md directly inform how this wiki's steering files should be written:

- Only include [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]
- Avoid redundancy with content agents can discover independently
- Accept ~20% token overhead as the cost of human-curated guidance
- Keep files short; split at 150–200 lines

## Associated Artifacts

### Tool-Specific Variants

| File | Tool | Notes |
|------|------|-------|
| AGENTS.md | Codex, Cursor, general | Converging standard |
| CLAUDE.md | Claude Code | Built-in auto-memory; no AGENTS.md interop |
| .cursor/rules/*.mdc | Cursor | YAML frontmatter; agent-decided inclusion |
| .github/copilot-instructions.md | GitHub Copilot | Path-specific .instructions.md support |
| .windsurf/rules | Windsurf | Plain Markdown with memories |
| .kiro/steering/ | Kiro | Steering docs with `inclusion` frontmatter |

### Key Effectiveness Findings

- LLM-generated AGENTS.md: **−0.5% to −2%** task success, **+20–23%** cost — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]
- Human-curated AGENTS.md: **+4%** task success, **up to +19%** cost — same source
- No AGENTS.md (baseline): 0% / 0%

### Best Practices (from 2,500+ repo analysis)

- Start with: commands, boundaries, 1–2 counterintuitive architectural decisions
- Highest ROI: non-standard tooling, permission boundaries, "Non-Obvious Patterns"
- Avoid: architectural overviews, code style already in linters, redundant documentation
- Split at: 150–200 lines (use subdirectory AGENTS.md files for larger projects)

## Notes

- The convergence toward a single standard (AGENTS.md) from a fragmented landscape (CLAUDE.md, .cursorrules, copilot-instructions.md, Gemini.md) is ongoing but incomplete as of mid-2026
- Symlink pattern (`CLAUDE.md → AGENTS.md`) prevents drift in multi-tool teams
- The ETH Zurich finding that auto-generated files hurt performance is the strongest evidence against `claude /init` and similar auto-generation commands
