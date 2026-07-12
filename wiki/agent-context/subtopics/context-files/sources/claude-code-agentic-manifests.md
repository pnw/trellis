---
title: "Source: Claude Code Agentic Manifests Study"
type: source-capture
evidence: empirical-primary
description: "Empirical study of 253 Claude.md files from 242 repositories, documenting common manifest structure and content."
sources:
  - "[[raw/papers/claude-code-agentic-manifests.md]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]"
tags: [agent-context, context-engineering, claude-code, agents]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
---

# Claude Code Agentic Manifests Study

## Source Identity

- Raw source: [[raw/papers/claude-code-agentic-manifests.md]]
- Source type: paper
- Author(s): Worawalan Chatlatanagulchai, Kundjanasith Thonglek, Brittany Reid, Yutaro Kashiwa, Pattara Leelaprute, Arnon Rungsawang, Bundit Manaskasemsak, Hajimu Iida
- Published: 2025-09-18
- Original URL: https://arxiv.org/abs/2509.14744
- Local PDF: `raw/papers/pdf/claude-code-agentic-manifests.pdf`
- Extracted text: `raw/papers/pdf/claude-code-agentic-manifests.txt`
- Scope: Empirical analysis of Claude Code manifest files

## Core Contribution

The paper documents the observed structure and content of real Claude Code manifests before broader AGENTS.md convergence: shallow hierarchies, one main heading, several subsections, and a mix of commands, implementation notes, and architecture.

## Key Claims

- The study analyzed 253 Claude.md files from 242 repositories.
- The initial GitHub search found 838 Claude.md files across 806 repositories.
- The authors filtered to repositories with at least 20 commits after introducing Claude.md, yielding 253 files from 242 repositories and 1,249 retrieved commits.
- The search window was February 24, 2025 to June 16, 2025.
- Agentic coding manifests provide project context, identity, and operational rules.
- The analyzed manifests typically have shallow hierarchies.
- Most files start with one H1 heading; median H2 count is 5.0 and median H3 count is 9.0.
- Deeper headings are rare: H4 appears in 37 documents, H5 in 5 documents, and H6 only once.
- Build and Run appears in 77.1% of files.
- Implementation Details appears in 71.9% of files.
- Architecture appears in 64.8% of files.
- Testing appears in 60.5% of files.
- General System Overview appears in 48.2% of files.
- AI Integration appears in 15.4% of files.
- Security appears in 8.7% of files and UI/UX appears in 8.3% of files, showing that non-functional or user-facing concerns are comparatively rare.

## Implications

Claude-specific manifests already resemble AGENTS.md content, so a canonical AGENTS.md plus a Claude import wrapper is structurally plausible. The paper also supports treating manifest maintenance as a real artifact-design problem, not merely a prompt-writing habit.

## Limitations

- The study is descriptive and does not measure task success, cost, or instruction adherence.
- The corpus focuses on Claude.md files, not AGENTS.md, Kiro steering, or multi-tool repositories.
- The extracted text is full-paper text from the local PDF, but table and two-column ordering artifacts remain in the raw extraction.

## Contribution Routing

- Creates: `[[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]]`
