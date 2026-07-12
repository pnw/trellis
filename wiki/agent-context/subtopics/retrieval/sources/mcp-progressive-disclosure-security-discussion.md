---
title: Progressive Disclosure in MCP Servers — Design and Security Discussion
type: source-capture
evidence: expert-analysis
description: A ModelContextProtocol-Security discussion proposing a three-meta-tool progressive disclosure design (used in production by GitHub's own MCP server) plus named security concerns about secure-by-default flags and secret exposure via process lists.
sources:
  - "[[raw/articles/mcp-progressive-disclosure-security-discussion.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]]"
tags: [agent-context, mcp, tool-use, security]
created: 2026-07-07
timestamp: 2026-07-07T20:00:00Z
status: draft
---

# Progressive Disclosure in MCP Servers — Design and Security Discussion

## Source Identity

- Publisher: ModelContextProtocol-Security GitHub organization, community discussion
- URL: https://github.com/orgs/ModelContextProtocol-Security/discussions/3
- Thread initiated: 2025-07-23 by Kurt Seifried

## Core Contribution

Documents a three-meta-tool progressive-disclosure design for MCP servers with many tools, as actually implemented in GitHub's own MCP server, alongside named security concerns about the design's defaults.

## Key Claims

- Large API surfaces (50+ tools) cause cognitive overload, poor tool selection, wasted context, and degraded performance for MCP clients.
- Proposed mechanism: `list_available_toolsets` (enumerate groups), `get_toolset_tools` (inspect a group before enabling it), `enable_toolset` (activate at runtime) — three tools rather than the two-tool discover/execute pattern documented elsewhere in this wiki (see [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]]).
- GitHub's own MCP server groups tools into "repos," "issues," "pull_requests," "actions," etc., and reports 60-80% context-window reduction.
- Security concerns raised: the `--read-only` flag inverts secure-by-default (an opt-in `--allow-edit` would be safer); secrets passed as environment variables remain visible in process lists (CWE-214), a risk modern containerization reduces but does not eliminate.

## Evidence and Results

The 60-80% context reduction figure is presented without a disclosed measurement methodology in what could be recovered for this capture. The security concerns are qualitative engineering arguments (grounded in a named CWE) rather than measured incident data.

## Limitations and Caveats

- No resolution is recorded for the `--read-only`/`--allow-edit` default-security disagreement as of this capture.
- Adoption beyond GitHub's own server is unconfirmed — a participant (@robertmclaws) explicitly asks whether wider adoption is happening, without a documented answer in the thread.

## Reliability Notes

Tiered `expert-analysis`: a named security researcher (Kurt Seifried) initiating and moderating a technical discussion with a real production implementation (GitHub's MCP server) as the worked example, on a forum specifically dedicated to MCP security. Not `empirical-primary` because the token-reduction figure lacks disclosed methodology and the security claims are argumentative rather than incident-measured.

## Important References and Linked Material

- Contrast with the two-tool pattern already documented at [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]].

## Contribution Routing

- Adds a third, security-conscious variant (three meta-tools, real production grouping) to [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]], plus a security caveat this wiki's existing coverage of the pattern lacked entirely.

## Extraction Notes

Retrieved via direct WebFetch; content is a tool-generated summary of a discussion spanning July 2025 through mid-2026, not a verbatim transcript.
