---
title: "AI Research Wiki Operational History Snapshot"
source: repository-extract
repository: pnw/ai-research
extracted: 2026-07-08
extraction_method: "git log --shortstat on origin/main (mechanical); wiki/log.md copied verbatim (agent-authored journal); lint outputs recorded from session transcripts (observed)"
---

# AI Research Wiki Operational History Snapshot (through 2026-07-08)

Point-in-time extract of this repository's own operational record, snapshotted so source-captures citing it remain regenerable against a fixed original even as the live history grows.

## Provenance Key

- **Mechanical** — produced directly by git; verifiable by re-running the command against commit 5c911d4.
- **Journal** — verbatim copy of `wiki/log.md`, an agent-authored, owner-merged operation journal.
- **Observed** — recorded from session transcripts (lint outputs); not independently regenerable.

## Commit History (mechanical: git log --reverse --shortstat, origin/main @ 5c911d4)

```
4aa1857|2026-04-16T21:11:30-06:00|feat: init

 7 files changed, 140 insertions(+)
8659dcc|2026-07-02T21:08:36-06:00|Add a bunch of stuff

 45 files changed, 27568 insertions(+), 17 deletions(-)
c127a1d|2026-07-02T21:52:25-06:00|updated for okf compliance

 23 files changed, 226 insertions(+), 292 deletions(-)
f3beed9|2026-07-04T21:23:21-06:00|checkpoint

 24 files changed, 915 insertions(+), 156 deletions(-)
4e439c2|2026-07-04T21:58:46-06:00|refactor structure and rules

 52 files changed, 2225 insertions(+), 1591 deletions(-)
31dc086|2026-07-04T22:22:12-06:00|add novelty to designs

 4 files changed, 19 insertions(+), 10 deletions(-)
af07942|2026-07-05T21:26:13-06:00|refactors

 46 files changed, 41890 insertions(+), 44 deletions(-)
09c9840|2026-07-05T21:37:20-06:00|add way to add commentary

 1 file changed, 23 insertions(+)
79b81a5|2026-07-05T21:59:27-06:00|implement cross-agent compatibility

 25 files changed, 7958 insertions(+), 23 deletions(-)
adfe609|2026-07-05T23:05:13-06:00|research c4 diagrams and others

 92 files changed, 40642 insertions(+), 45 deletions(-)
0e35145|2026-07-06T20:55:24-06:00|Ingest effective AI SDLC research

 55 files changed, 29210 insertions(+), 9 deletions(-)
f8a9faf|2026-07-06T21:02:41-06:00|fix formatting

 3 files changed, 5 insertions(+), 237 deletions(-)
614fa1b|2026-07-06T21:30:49-06:00|deeper research on blitzy and devin

 17 files changed, 3438 insertions(+), 5 deletions(-)
00d7fe0|2026-07-06T21:37:10-06:00|fix ambiguous links

 110 files changed, 1453 insertions(+), 1451 deletions(-)
16f6464|2026-07-06T21:57:31-06:00|Refactor wiki topic structure

 117 files changed, 1434 insertions(+), 1365 deletions(-)
0a4a74c|2026-07-06T22:25:08-06:00|Ingest Blitzy docs and split product topics

 951 files changed, 33993 insertions(+), 295 deletions(-)
7c92f4f|2026-07-07T17:05:42+00:00|Capture intent refinement stage design and intent brief construct

 9 files changed, 344 insertions(+), 5 deletions(-)
fd810c6|2026-07-07T17:51:19+00:00|Adopt evidence-tier schema and agent-agnostic schema/ layer

 97 files changed, 1269 insertions(+), 722 deletions(-)
93134e4|2026-07-07T19:19:22+00:00|Add deterministic lint script, excise report pattern, prune raw assets

 851 files changed, 226 insertions(+), 8519 deletions(-)
452b341|2026-07-07T19:33:27+00:00|Add pilot implementation playbook, roadmap, and lint/orphan fixes

 19 files changed, 365 insertions(+), 14 deletions(-)
c6c1343|2026-07-07T21:10:16+00:00|Research and integrate the index-graduation strategy at 100+ pages

 25 files changed, 1033 insertions(+), 44 deletions(-)
7b3b604|2026-07-07T21:19:40+00:00|Correct overstated 'industry abandoned embeddings' claim with vendor research

 13 files changed, 420 insertions(+), 9 deletions(-)
872d1fb|2026-07-08T01:52:05+00:00|Implement QMD-based index graduation with grep fallback

 11 files changed, 111 insertions(+), 12 deletions(-)
446901c|2026-07-08T02:31:02+00:00|Propagate raw/ purpose into agent prompt, ingest rules, and architecture page

 4 files changed, 6 insertions(+), 5 deletions(-)
48cecaa|2026-07-08T02:39:22+00:00|Capture wiki purpose and expand candidate research topics

 3 files changed, 45 insertions(+), 9 deletions(-)
5c911d4|2026-07-08T02:49:41+00:00|Merge branch 'claude/wiki-review-ai-workflow-2r309f'
```

## Current State (mechanical, at 5c911d4)

- Wiki pages: 133
- Source-capture pages: 63

## Lint Results (observed, from session transcripts)

- 2026-04-16 (pre-schema, agent-run): run 1 — 0 errors, 3 warnings, 3 info; run 2 — 3 errors (meta files missing frontmatter), 1 warning, 4 info (per journal entries below)
- 2026-07-07, first scripts/lint.py run after evidence-tier adoption: 0 errors, 4 warnings, 113 pages
- 2026-07-07, retroactive confidence-ceiling audit (one-off script preceding lint.py): 27 of 113 pages carried confidence above the derivation ceiling
- 2026-07-08, after orphan-check bug fix in scripts/lint.py (parallel session): 0 errors, 1 warning, 124 pages; the fix resurfaced 6 real orphans that were then repaired
- 2026-07-08, post-integration: 0 errors, 1 warning (justified scoped-claims override), 129 pages

## Operation Journal (journal: wiki/log.md verbatim at snapshot time)

# Operation Log

<!-- Append-only. Newest first. -->

## 2026-07-08

* **Create**: Added a Purpose section to [[wiki/overview]] capturing why this wiki exists — an interview with the owner established it's primarily a personal practice reference for building their own software, with a secondary thread toward a reusable personal toolkit (not a commercial product) and direct relevance to the owner's day job as a cloud architect at a large organization. No fixed deliverable; audience is the owner, with a team as a possible future secondary audience.
* **Update**: Expanded [[wiki/roadmap]]'s Candidate New Topics from 6 items into a comprehensive, categorized survey (~20 items across Deepen Existing Topics, Enterprise/Cloud-Architecture-Specific, Personal Practice-Specific, and Meta/Wiki Process), tagged by relevance to personal vs. enterprise use given the newly-captured purpose. Superseded rather than merely appended to the prior list.
* **Implement**: Graduated the wiki's own index/retrieval strategy per owner direction — deliberately, ahead of the "wait for an observed Approach 0 failure" trigger this wiki had itself recorded. Added `scripts/qmd-index.sh` (idempotent, pinned `qmd@2.5.3` via `npx`, gitignored `.qmd/` derived index), wired it into the cross-agent Ingest Workflow (`AGENTS.md`, `schema/ingest.md`) and Query Workflow (`AGENTS.md`, `schema/conventions.md`: try `qmd search`/`qmd query`, fall back to `Grep`/`Glob`), and added a Claude-Code-specific `SessionStart` hook (`.claude/settings.json`) as a convenience layer on top of the cross-agent step (documented in `CLAUDE.md`).
* **Finding**: Directly tested `qmd` against this wiki (133 files) before committing anything. `qmd search` (BM25) worked immediately with no model download and returned good results. `qmd embed`/`qmd query` (semantic/hybrid) failed in this sandboxed session: their models are hosted on `huggingface.co`, which this environment's network egress policy blocks (confirmed as a proxy-level CONNECT-tunnel 403, not an HF gating issue). This is environment-specific, not a defect in `qmd`. Recorded in [[wiki/agent-context/subtopics/retrieval/entities/qmd]] and the Implementation section of [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] so a future agent doesn't waste time re-debugging it.

## 2026-07-07

* **Lint**: Wiki health check — 0 errors, 1 warning (pre-existing, justified scoped-claims override on [[wiki/llm-wiki/entities/open-knowledge-format]]), 124 pages checked.
* **Ingest**: Researched and captured 8 new sources on knowledge-base retrieval architecture at the scale this wiki just reached — prompted by the roadmap's flagged ~100-page threshold. Key finding: Anthropic removed vector search from Claude Code in May 2025 for grep/glob-driven "agentic search," with industry follow-on (Cursor, Windsurf, Cline, Devin, Sourcegraph Amp), and Karpathy's own primary gist recommends local hybrid search (`qmd`, by Shopify's Tobi Lütke) over embedding-RAG infrastructure once a flat index stops scaling — not the bespoke MCP meta-tool schema or compiled graph this wiki's own design page previously proposed. New sources: [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]], [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]], [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]], [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]], [[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]], [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]], [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]], [[wiki/agent-context/subtopics/retrieval/sources/mcp-progressive-disclosure-security-discussion]]. Most non-GitHub, non-Anthropic hosts (arXiv, Wikipedia, most blogs) returned HTTP 403 to WebFetch this session; captures built from WebSearch aggregation are flagged accordingly in their Reliability/Extraction Notes.
* **Create**: Added [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] construct (novelty: emerging, confidence: low pending independent corroboration) and [[wiki/agent-context/subtopics/retrieval/entities/qmd]] entity.
* **Update**: Substantially revised [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] (confidence medium → high): added Approach 0 (agentic search, no index) ahead of the original three, split Approach B into B1 (custom meta-tool schema) and B2 (QMD-style local hybrid search), added a Security Note, and rewrote the "Recommendation for This Wiki" section — the wiki's actual practice all session (Grep/Glob/Read against `wiki/`) is now the documented default, the originally-planned `wiki/by-tag.md`/custom MCP server is explicitly deprioritized with reasoning, and the concrete graduation trigger is now "the first real query Approach 0 misses" rather than a page-count threshold alone.
* **Update**: Revised [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]] (confidence medium → high) — upgraded the Anthropic "Code Execution with MCP" citation from secondhand (via a Synaptic Labs blog) to a direct capture, added the Tool Search Tool and GitHub's three-meta-tool variant as concrete implementations, and added a Security and Reliability Notes section (secure-by-default flag disagreement, secret exposure via process lists, loss of inline tool guidance, code-auditability concerns). Light-touch update to [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] noting agentic search as a no-staging alternative.
* **Update**: Resolved two [[wiki/roadmap]] self-maintenance items with the above research — the ~100-page scale-ceiling item and the unbuilt `by-tag.md` recommendation are both now "researched, no build needed yet" rather than open questions. Updated [[wiki/overview]]'s Agent Context section to name agentic search as the wiki's actual current default.
* **Correction**: A follow-up question challenged the claim that "the industry, including Anthropic's own Claude Code, moved away from embeddings toward agentic search" — the original capture had taken a single aggregated secondary source at face value for a multi-vendor claim. Direct vendor-level research found it **overstated**: Cursor is hybrid (grep + embeddings, agent-selected), Windsurf and GitHub Copilot are embeddings-first, and Sourcegraph Amp uses structural code-graph (SCIP) indexing — Claude Code's pure-grep design is real but the exception, not the industry norm. Captured 4 new sources ([[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]], [[wiki/agent-context/subtopics/retrieval/sources/windsurf-fast-context-architecture]], [[wiki/agent-context/subtopics/retrieval/sources/github-copilot-embedding-model-2026]], [[wiki/agent-context/subtopics/retrieval/sources/sourcegraph-context-engineering-hybrid]]), added [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]] as the durable corrected record, and added a Corrigendum to [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] plus corrections to [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]'s Approach 0 table and recommendation. The wiki's actual recommendation for this wiki specifically (agentic search as current default, QMD — itself hybrid — as the graduation path) is unchanged and, if anything, better grounded by this correction.
* **Maintenance**: Fixed a real bug in `scripts/lint.py`'s orphan check — it only excluded `wiki/index.md` from counting as an incoming link, so `wiki/log.md` (an append-only journal that mentions nearly every page at creation) was silently counted as legitimate discovery, masking real orphans. Updated the script and `schema/lint.md` to exclude both. This resurfaced 6 real orphans: [[wiki/agent-context/subtopics/retrieval/constructs/domain-centric-knowledge-fusion]], [[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]], [[wiki/agent-context/subtopics/retrieval/entities/objectgraph-format]], [[wiki/ai-sdlc/subtopics/productivity-evidence/sources/github-copilot-productivity-research]], [[wiki/ai-sdlc/subtopics/products/subtopics/blitzy/assessments/cloudflare-fetch-attempts]], and [[wiki/llm-wiki/entities/yaml-frontmatter]] — fixed each with a real inline body-text link from an appropriate existing page rather than a token backlink.
* **Maintenance**: Resolved 2 of the 3 long-standing "confidence above ceiling" warnings on [[wiki/architecture-diagrams/subtopics/c4/constructs/architecture-description]] and [[wiki/architecture-diagrams/subtopics/c4/entities/c4-model]] by adding frontmatter `sources` entries for sources already cited in their body text but missing from provenance — a genuine independence-count fix, not a confidence downgrade. Verified the remaining warning on [[wiki/llm-wiki/entities/open-knowledge-format]] as a justified scoped-claims override (design-intent claims about OKF's own spec).
* **Create**: Added [[wiki/intent-compiler/designs/pilot-implementation-playbook]] — a copy-paste-ready v0 pilot design merging [[wiki/intent-compiler/designs/intent-refinement-stage]], the handoff-artifact shapes from [[wiki/ai-sdlc/subtopics/products/designs/agentic-sdlc-handoff-artifacts]] and [[wiki/ai-sdlc/subtopics/products/designs/real-world-agentic-sdlc-workflows]], and the project-wiki integration point from [[wiki/llm-wiki/designs/project-wiki-template]] — previously three separate designs nobody had assembled into a runnable procedure. Includes concrete templates (AGENTS.md addition, Intent Brief, Plan-lite, Handoff-lite, Gap Note, Evaluation Scorecard), a pilot scope recommendation, and resolved defaults for the open questions blocking direct use (brief location, sync vs. async confirmation, weight-escalation trigger). Cross-linked from all three source designs.
* **Schema**: Added `wiki/roadmap.md` as a fourth special root file (alongside `index.md`, `log.md`, `overview.md`) per owner decision — a forward-looking backlog distinct from `overview.md`'s current-understanding framing, pruned as items resolve. Updated `AGENTS.md`, `schema/structure.md`, `schema/lint.md`, `schema/conventions.md`, and `scripts/lint.py` (added to `META_FILES`) to document and exempt it. Populated with a consolidated open-design-question backlog pulled from ~15 pages, candidate new topics (AI SDLC competitor gaps, agent observability/eval tooling, security/threat modeling, agent memory/provenance standards, reviewer trust calibration), and a wiki self-maintenance section (scale-ceiling threshold reached at 114 pages, an unbuilt `by-tag.md` recommendation, lint judgment-tier automation gap).
* **Update**: Propagated the ratified `raw/` purpose (re-capture audits + upstream change detection; no in-place edits; incidental assets prunable) into the Kiro agent prompt, `schema/ingest.md`, and the Layer 1 description in [[wiki/llm-wiki/constructs/three-layer-architecture]]; also corrected that page's stale Layer 3 claim that the schema lives in `.kiro/steering/` (it now lives in `schema/`).
* **Maintenance**: Excised the lint-report-to-outputs pattern — lint results are conversational, not durable documents. Removed `outputs/` from the directory contract and Kiro config, deleted the stale 2026-04-16 report, and added `scripts/lint.py` as the deterministic lint tier (frontmatter validity, wikilinks, epistemic-field placement, folder/type agreement, confidence ceilings, orphans, staleness); judgment checks remain agent work per `schema/lint.md`.
* **Maintenance**: Clarified `raw/` purpose in the contract — re-visiting source captures and upstream change detection; no in-place edits; incidental non-source assets may be pruned. Pruned ~1,000 browser-save script/style assets from `raw/articles/blitzy-platform-docs-browser-save/` (95MB → 4.1MB), keeping the saved HTML documents and markdown corpus.
* **Lint**: Wiki health check — 0 errors, 4 warnings (3 scoped-claims confidence overrides flagged for verification, 1 orphan: [[wiki/ai-sdlc/subtopics/productivity-evidence/sources/github-copilot-productivity-research]]).
* **Migration**: Created the shared `schema/` layer (`page-format`, `page-types`, `conventions`, `structure`, `ingest`, `lint`) as the agent-agnostic canonical reference, reduced `.kiro/` steering and skills to thin wrappers referencing it, and updated `AGENTS.md` — fixing the portability gap where authoritative schema semantics lived only in the Kiro adapter.
* **Schema**: Adopted the two-axis epistemic model from [[wiki/llm-wiki/designs/evidence-tier-schema]]: added required `evidence` tier (empirical-primary | empirical-secondary | official-docs | expert-analysis | vendor-claim | llm-generated) to all 50 source-capture pages and removed `confidence` from them; `confidence` on non-source pages is now derived by rule (independence-weighted ceiling). Sharpened the source-isolation invariant (epistemic, not navigational; reportage separated from capture-time assessment) and added a Reliability Notes section to the source-capture template. New lint rules cover missing tiers, misplaced fields, ceiling violations, and circular reporting.
* **Maintenance**: Re-derived `confidence` on 27 pages that exceeded the new ceiling — notably vendor/official-docs-sourced AI SDLC product pages (high → medium) and llm-generated-only intent-compiler pages (medium/high → low). Added [[wiki/llm-wiki/sources/open-knowledge-format-spec]] as independent corroboration to [[wiki/llm-wiki/constructs/llm-wiki-pattern]] and [[wiki/llm-wiki/constructs/three-layer-architecture]].
* **Ingest**: Captured [[raw/chats/epistemic-metadata-claude-code-thread.md]] and [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]] — the Claude Code thread surveying epistemic-grading frameworks and ratifying source isolation after explicit challenge.
* **Create**: Added [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]] (Admiralty, ICD 203, GRADE, Wikipedia, digital gardens, Notion/Confluence, RAG groundedness — convergent lesson: two orthogonal axes, never one scalar; trust is computed or decays, not asserted), [[wiki/llm-wiki/designs/evidence-tier-schema]] (the adopted schema), and [[wiki/llm-wiki/constructs/source-isolation]] (the ratified invariant with staging-layer rationale). Updated [[wiki/index]] and [[wiki/overview]].
* **Ingest**: Captured [[raw/chats/intent-refinement-claude-code-thread.md]] and [[wiki/intent-compiler/sources/intent-refinement-claude-code-thread]] — a Claude Code review thread assessing the wiki (research phase complete, pilot next) and refining the intent compiler after owner pushback that its real purpose is clarifying vague requirements before implementation planning.
* **Create**: Added [[wiki/intent-compiler/constructs/intent-brief]] construct (coined) — a half-page, technology-agnostic problem-space artifact with a portability test, vetoable assumptions, and acceptance-criteria derivation; the project's preferred working term over "semantic IR" for the lightweight core, with semantic IR retained as the expanded Weight-3 capture.
* **Create**: Added [[wiki/intent-compiler/designs/intent-refinement-stage]] design — the pilot-ready intent compiler kernel: interrogate → intent brief → human confirm before the plan gate, ceremony scaled to ambiguity, three-level failure classification (code≠plan, plan≠brief, brief≠intent), and an evaluation plan.
* **Update**: Restructured the weight table in [[wiki/intent-compiler/constructs/process-weights]] so intent refinement scales in first (inline questions at Weight 1, intent brief at Weight 2, semantic IR capture at Weight 3), and revised [[wiki/intent-compiler/designs/intent-compiler-design]] to route through the lightweight kernel with the full pipeline deferred pending pilot evidence. Linked [[wiki/intent-compiler/constructs/intent-brief]] from [[wiki/intent-compiler/constructs/intent-formalization]] and updated [[wiki/index]].
* **Refactor**: Split `products/` into product-specific subtopics for reverse-engineering pages: Amazon Q Developer, Blitzy, CodeRabbit, Devin, Gemini Code Assist, GitHub Copilot, GitLab Duo, and OpenAI Codex now live under `wiki/ai-sdlc/subtopics/products/subtopics/`. Kept cross-product comparison and workflow-design analyses at the shared `products/` level and updated [[wiki/index]] plus all wikilinks.
* **Ingest**: Converted the manual Blitzy documentation export into raw sources: added [[raw/articles/blitzy-platform-docs-full.md]] plus 71 split raw pages under `raw/articles/blitzy-platform-docs/`. Updated [[wiki/ai-sdlc/subtopics/products/subtopics/blitzy/sources/blitzy-platform-docs]], [[wiki/ai-sdlc/subtopics/products/designs/real-world-agentic-sdlc-workflows]], [[wiki/ai-sdlc/subtopics/products/designs/agentic-sdlc-handoff-artifacts]], [[wiki/ai-sdlc/subtopics/products/subtopics/blitzy/assessments/cloudflare-fetch-attempts]], and [[wiki/index]] to use the higher-fidelity corpus.
* **Migration**: Reorganized wiki pages into topic-local type folders and selective nested subtopics. Updated shared agent structure rules, Kiro adapter notes, wikilinks, and [[wiki/index]] so page paths now mirror both subject locality and artifact type.
* **Update**: Revised the shared agent contract and existing wikilinks to use repository-root targets. Wiki pages now link through the `wiki/` path prefix, source captures cite exact `raw/` files with extensions, and a resolver check found no missing or ambiguous wikilinks after migration.
* **Create**: Added [[wiki/ai-sdlc/subtopics/products/subtopics/blitzy/assessments/cloudflare-fetch-attempts]] assessment page to track Blitzy URLs that returned Cloudflare challenge pages during direct raw-source capture and prioritize manual exports.
* **Ingest**: Added real-world agentic SDLC design sources for Blitzy and Devin. Captured Blitzy's Technical Specification, Agent Action Plan, Project Guide, runtime validation, and PR review workflow; captured Devin's sessions, Knowledge, Playbooks, automations, PR governance, test loops, and autofix/review loop.
* **Create**: Added [[wiki/ai-sdlc/subtopics/products/designs/real-world-agentic-sdlc-workflows]] and [[wiki/ai-sdlc/subtopics/products/designs/agentic-sdlc-handoff-artifacts]] design pages. Core conclusion: production agentic SDLC systems are defined by intermediary artifacts and review gates, not just autonomous code generation.
* **Update**: Revised [[wiki/ai-sdlc/subtopics/productivity-evidence/syntheses/effective-ai-sdlc]], [[wiki/ai-sdlc/subtopics/products/comparisons/ai-sdlc-saas-offerings]], [[wiki/ai-sdlc/constructs/sdlc-context-graph]], [[wiki/ai-sdlc/constructs/validation-governance-layer]], and [[wiki/index]] to surface Blitzy/Devin patterns alongside existing SaaS and governance evidence.

## 2026-07-06

* **Ingest**: Added `ai-sdlc/` topic from autonomous deep research on effective AI SDLC. Captured DORA 2025 AI-assisted SDLC framing, GitHub Copilot productivity research, Peng et al. Copilot experiment, METR early-2025 RCT, NAV IT longitudinal Copilot case study, GenAI requirements-engineering SLR, BNY Mellon productivity-metrics study, AI maintenance-burden study, and SaaS/product pages for GitHub Copilot cloud agent, OpenAI Codex, Amazon Q Developer, Gemini Code Assist, GitLab Duo Agent Platform, and CodeRabbit.
* **Create**: Added [[wiki/ai-sdlc/subtopics/productivity-evidence/syntheses/effective-ai-sdlc]] synthesis, [[wiki/ai-sdlc/subtopics/products/comparisons/ai-sdlc-saas-offerings]] comparison, [[wiki/ai-sdlc/constructs/sdlc-context-graph]] construct, and [[wiki/ai-sdlc/constructs/validation-governance-layer]] construct. Core conclusion: AI SDLC value depends on task fit, lifecycle context, validation/governance, and downstream metrics, not code generation alone.
* **Update**: Revised [[wiki/intent-compiler/subtopics/semantic-ir/designs/semantic-ir-capture-stack]], [[wiki/overview]], and [[wiki/index]] to connect semantic IR with lifecycle context graphs, validation governance, SaaS market evidence, and mixed empirical productivity findings.
* **Create**: Added [[wiki/intent-compiler/subtopics/semantic-ir/designs/semantic-ir-capture-stack]] design page and [[wiki/intent-compiler/subtopics/semantic-ir/sources/semantic-ir-capture-stack-codex-thread]] source capture to clarify that diagrams are one semantic IR capture layer, not the full Semantic IR. Captured the copied stack as an important candidate baseline, not a definitive or comprehensive taxonomy: intent/requirements → C4 context/container views → ADRs → sequence/state diagrams → threat model → OpenAPI/IaC/tests/telemetry.
* **Update**: Revised [[wiki/intent-compiler/subtopics/semantic-ir/designs/architecture-view-pipeline]], [[wiki/architecture-diagrams/subtopics/c4/constructs/diagrams-as-architecture-ir]], [[wiki/architecture-diagrams/subtopics/c4/syntheses/architecture-diagrams-in-ai-sdlc]], [[wiki/intent-compiler/designs/intent-compiler-design]], [[wiki/intent-compiler/subtopics/semantic-ir/constructs/semantic-transformation-graph]], [[wiki/overview]], and [[wiki/index]] to route architecture views into the broader semantic IR capture stack.
* **Ingest**: Added Mermaid-focused architecture-diagram sources: official Mermaid docs, GitHub Mermaid rendering docs, MermaidSeqBench, SAGE, and MermaidFlow.
* **Create**: Added [[wiki/architecture-diagrams/subtopics/mermaid/entities/mermaid]] entity and [[wiki/architecture-diagrams/subtopics/mermaid/comparisons/structurizr-vs-mermaid-for-ai-sdlc]] comparison. Recommendation: Structurizr as canonical architecture model for AI SDLC; Mermaid as Markdown-native review, local diagram, and workflow/sequence layer.
* **Update**: Revised [[wiki/architecture-diagrams/subtopics/c4/designs/diagram-tooling-for-agentic-sdlc]], [[wiki/architecture-diagrams/subtopics/c4/constructs/diagrams-as-architecture-ir]], [[wiki/architecture-diagrams/subtopics/c4/syntheses/architecture-diagrams-in-ai-sdlc]], [[wiki/intent-compiler/subtopics/semantic-ir/designs/architecture-view-pipeline]], and [[wiki/index]] to distinguish Structurizr source-of-truth use from Mermaid distribution/local-IR use.
* **Ingest**: Added architecture-diagram research corpus for C4 and AI SDLC workflows: official C4 docs, Structurizr DSL/MCP docs, IEEE/ISO/IEC 42010, C4 multi-agent generation, MAAD architecture-design automation, LLM/software-architecture SLR, and Agentic AI in SDLC.
* **Create**: Added `architecture-diagrams/` topic with [[wiki/architecture-diagrams/subtopics/c4/entities/c4-model]], [[wiki/architecture-diagrams/subtopics/c4/constructs/architecture-description]], [[wiki/architecture-diagrams/subtopics/c4/constructs/diagrams-as-architecture-ir]], [[wiki/architecture-diagrams/subtopics/c4/designs/diagram-tooling-for-agentic-sdlc]], and [[wiki/architecture-diagrams/subtopics/c4/syntheses/architecture-diagrams-in-ai-sdlc]].
* **Create**: Added [[wiki/intent-compiler/subtopics/semantic-ir/designs/architecture-view-pipeline]] design page showing how C4/4+1-style architecture views can operate as validated intermediate representations in the intent compiler.
* **Update**: Revised [[wiki/overview]], [[wiki/index]], [[wiki/intent-compiler/designs/intent-compiler-design]], [[wiki/intent-compiler/subtopics/semantic-ir/constructs/semantic-transformation-graph]], and [[wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]] to connect architecture views, typed reverse transitions, and AI SDLC workflows.
* **Update**: Implemented cross-agent manifest strategy from [[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]] with root `AGENTS.md` as the canonical contract, `CLAUDE.md` as a Claude import wrapper, and Kiro research-agent config pointing to `AGENTS.md` as shared context.
* **Ingest**: Enriched arXiv-backed agent-context sources with full PDF downloads and extracted text: [[wiki/agent-context/subtopics/context-files/sources/agents-md-efficiency]], [[wiki/agent-context/subtopics/context-files/sources/configuration-smells-agents-md]], and [[wiki/agent-context/subtopics/context-files/sources/claude-code-agentic-manifests]].
* **Create**: Added [[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]] design page for agent-agnostic instruction files across Codex, Claude Code, and Kiro. Captured official docs sources for Codex AGENTS.md, Claude Code memory/imports, and Kiro steering, plus new empirical sources on AGENTS.md efficiency, configuration smells, and Claude Code manifests.
* **Create**: Added [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]] source capture and raw chat [[raw/chats/llm-wiki-effectiveness-codex-thread.md]] for the Codex research thread on LLM wiki use cases and AI project application.
* **Create**: Added [[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]] design page to make multi-agent coordination the primary project-template target: task graph, role pages, handoffs, evals, and error book.
* **Update**: Revised [[wiki/llm-wiki/syntheses/llm-wiki-effectiveness]] with source reconciliation notes comparing Kiro and Codex outputs, including discrepancies around source-count thresholds, workflow-first adoption, governance, and multi-agent priority.
* **Update**: Revised [[wiki/llm-wiki/designs/project-wiki-application-guide]], [[wiki/llm-wiki/designs/project-wiki-template]], [[wiki/overview]], [[wiki/index]], and `.kiro/steering/conventions.md` to route project-application requests through the multi-agent pattern.

## 2026-07-05

* **Create**: Added [[wiki/llm-wiki/syntheses/llm-wiki-effectiveness]] synthesis page from deep research on LLM wiki usefulness, content selection boundaries, failure modes (epistemic drift, library drift, stale content), and role in AI projects. Draws on effectiveness deep research, Karpathy guide, AGENTS.md research, and ETH Zurich study.

* **Create**: Added [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]] source capture from the deep research synthesis on LLM wiki effectiveness, appropriate use, content selection, and AI project application.
* **Create**: Added [[wiki/llm-wiki/designs/project-wiki-application-guide]] and [[wiki/llm-wiki/designs/project-wiki-template]] to turn the research wiki into a reusable repertoire for agentic implementation workflows and project-specific wiki adaptation.
* **Create**: Added [[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]] construct to resolve source contribution routes and ground the project template's AGENTS.md guidance in the ETH Zurich and Augment sources.
* **Update**: Revised [[wiki/overview]] and [[wiki/index]] to surface the new operational application layer and connect it to agent-context, intent-compiler, and token-economics topics.

* **Ingest**: Processed 5 sources into new `agent-context/` topic from deep research on agent knowledge surfacing. Sources: ObjectGraph (Dubey, 2026), TagRAG (Tao et al., ACL 2026), ETH Zurich context files study (Gloaguen et al., 2026), LLM-Wiki retrieval (Ming et al., 2026), Augment AGENTS.md guide (Galstian, 2026). Created source-capture pages, [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] construct, and [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] design doc exploring three approaches to surfacing OKF knowledge graphs to agents.
* **Create**: Construct pages — [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]], [[wiki/agent-context/subtopics/retrieval/constructs/context-compounding]], [[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]], [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]], [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]], [[wiki/agent-context/subtopics/retrieval/constructs/retrieval-as-reasoning]], [[wiki/agent-context/subtopics/retrieval/constructs/hierarchical-tag-chains]], [[wiki/agent-context/subtopics/retrieval/constructs/domain-centric-knowledge-fusion]], [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]].
* **Create**: Entity pages — [[wiki/agent-context/subtopics/retrieval/entities/objectgraph-format]], [[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]], [[wiki/agent-context/subtopics/context-files/entities/agents-md]].
* **Create**: [[wiki/llm-wiki/entities/yaml-frontmatter]] entity page — origin and adoption of the YAML frontmatter convention.
* **Update**: Added Inline Citation Rules to `.kiro/steering/page-format.md` — every factual claim in page body must link to its source.

## 2026-07-04

* **Migration**: Restructured the wiki around a topic-first typed artifact graph. Replaced `source-summary` with `source-capture`, replaced `concept` with `construct`, moved source captures under topic-local `sources/` directories, converted existing concept pages into topic-local construct pages, created design and assessment pages for the intent compiler, retyped `token-cost-optimization` as synthesis, updated page type steering and ingest workflow, rewrote all wikilinks to new paths, updated index, and revised overview.
* **Create**: Added [[wiki/llm-wiki/sources/open-knowledge-format-spec]] source-capture page for the OKF v0.1 specification.
* **Create**: Added [[wiki/intent-compiler/sources/intent-compiler-deep-research-validation]] as a dedicated source-capture page for the Deep Research validation report (previously folded into the design conversation source).
* **Update**: Revised `.kiro/skills/lint.md` to check for new type vocabulary, directory structure rules, and mixed-role pages.

## 2026-07-02

* **Create**: Concepts layer — created `wiki/concepts/` directory with 8 standalone concept pages extracted from existing source-oriented material: [[wiki/intent-compiler/constructs/intent-formalization]], [[wiki/intent-compiler/subtopics/semantic-ir/constructs/translation-validation]], [[wiki/intent-compiler/constructs/inference-reduction]], [[wiki/intent-compiler/constructs/agent-handoff]], [[wiki/intent-compiler/constructs/artifact-centric-process]], [[wiki/intent-compiler/constructs/progressive-disclosure]], [[wiki/intent-compiler/constructs/harness-engineering]], [[wiki/intent-compiler/constructs/loop-engineering]]. Created [[wiki/intent-compiler/constructs/process-weights]] and [[wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]] scoped to the intent compiler design.
* **Schema**: Added `novelty` (required for concept pages), `aka`, and `coined_by` fields to page-format steering doc. Scoped by type: concept pages get novelty/aka/coined_by, entity pages get aka.
* **Maintenance**: Added `novelty`, `aka`, and `related` links to existing concept pages (intent-compilation, semantic-transformation-graph).
* **Maintenance**: OKF meta-file conformance — stripped excess frontmatter from `index.md` (kept only `okf_version`), removed frontmatter from `log.md`, reversed log to newest-first with date headings and bold-word bullets, added `type`/`description`/`tags`/`created` to `overview.md`.
* **Maintenance**: OKF-aligned format conversion — restructured frontmatter across all 18 wiki pages (added `description`, `tags`, `timestamp`; removed `topic`; converted source paths to wikilinks).
* **Ingest**: Processed [Open Knowledge Format](llm-wiki/entities/open-knowledge-format.md) from OKF v0.1 spec, Google Cloud blog, and OWOX analysis. Created concept page with spec summary, gap analysis, and applicability assessment.
* **Ingest**: Processed [Intent Compiler Design Conversation](intent-compiler/sources/intent-compiler-design-conversation.md) from ChatGPT shared conversation and Deep Research validation report. Created concept pages for [[wiki/intent-compiler/constructs/intent-compilation]] and [[wiki/intent-compiler/subtopics/semantic-ir/constructs/semantic-transformation-graph]].

## 2026-06-24

* **Ingest**: Enriched paper sources with full PDF text — downloaded and converted PDFs for all 4 token economics papers; updated wiki pages with additional quantitative findings.
* **Ingest**: Processed [Beyond Functional Correctness](token-economics/sources/beyond-functional-correctness-coding-style.md) from Wang et al., 2024. Validates prompting approach in [[wiki/token-economics/sources/llm-style-token-costs]].
* **Ingest**: Processed [Code Needs Comments](token-economics/sources/code-needs-comments-augmentation.md) from Song et al., ACL 2024. Complementary to Sabetto et al. (MITRE).
* **Ingest**: Processed [Hidden Cost of Readability](token-economics/sources/hidden-cost-of-readability-formatting.md) from Pan, Sun et al., 2025.
* **Ingest**: Processed [Impact of Comments on LLM Comprehension](token-economics/sources/impact-of-comments-on-llm-comprehension.md) from Sabetto et al. (MITRE), 2025.
* **Ingest**: Processed [LLM Code Style and Token Costs](token-economics/sources/llm-style-token-costs.md) from Jim Mont, 2026. Created topic directory `wiki/token-economics/`.

## 2026-04-16

* **Lint**: Wiki health check (2nd run) — 3 errors (meta files missing frontmatter), 1 warning (single-source confidence), 4 info items.
* **Lint**: Wiki health check — 0 errors, 3 warnings, 3 info.
* **Ingest**: Re-ingested Starmorph guide with full raw source (improved source fidelity, wiki pages unchanged).
* **Ingest**: Re-ingested Starmorph guide for linked material — added Linked Material section to source summary.
* **Ingest**: Processed [Karpathy LLM Wiki Knowledge Base Guide](llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide.md) from Starmorph article. Created topic directory `wiki/llm-wiki/` and 5 initial pages.

