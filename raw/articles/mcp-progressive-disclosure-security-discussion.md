# Progressive Disclosure in MCP Servers — Design and Security Discussion

- Source URL: https://github.com/orgs/ModelContextProtocol-Security/discussions/3
- Publisher: ModelContextProtocol-Security GitHub organization, community discussion thread
- Retrieved via: WebFetch (direct, successful), 2026-07-07

## Problem Statement

Thread initiated by Kurt Seifried (Jul 23, 2025): large API surfaces create tool-selection problems for AI models. Traditional MCP servers expose 50+ tools simultaneously, causing cognitive overload, poor tool selection, wasted context-window space, and degraded performance.

## Proposed Solution: Three Discovery Meta-Tools

1. `list_available_toolsets` — enumerates all possible tool groups and their status.
2. `get_toolset_tools` — shows tools within a specific category before enabling it.
3. `enable_toolset` — dynamically activates a toolset at runtime.

GitHub's own MCP server implementation organizes tools into logical groups ("repos," "issues," "pull_requests," "actions,") allowing selective enablement based on task requirements.

## Reported Benefits

Reduces cognitive load on the model, improves tool-selection accuracy, shrinks context-window usage by an estimated 60-80%, and lets a server expose hundreds of tools without overwhelming clients.

## Security Discussion

- **@ekovalets** (Oct 2, 2025) raised two concerns: the `--read-only` flag design violates "secure by default" (an `--allow-edit` opt-in would be preferable); and environment variables used for secrets remain visible in process lists, risking exposure through system monitoring.
- **@kurtseifried** (Dec 11, 2025) contextualized the secrets concern as CWE-214 (invocation with visible sensitive information), noting modern containerized systems reduce but do not eliminate the risk.
- **@robertmclaws** (Dec 9, 2025) asked whether adoption is occurring, indicating ongoing community interest in the pattern's trajectory.
