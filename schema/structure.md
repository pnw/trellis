# Project Structure

Agent-agnostic directory layout and organizational model. This file is part of the shared `schema/` layer referenced by `AGENTS.md`. It covers the whole repository; the wiki surface's detailed rules live under `schema/wiki/` and the design surface's under `schema/design/`.

## Two Content Surfaces

The repository carries two agent-maintained content surfaces with different governing rules:

- **The wiki** (`wiki/`, fed by `raw/`) — durable knowledge, claim-shaped and **evidence-governed**: every page's authority derives from its sources, their tiers, and their independence. Schema: `schema/wiki/`.
- **The design surface** (`designs/`) — commitments, workflow-shaped and **lifecycle-governed**: each design's authority derives from its lifecycle state (draft, active, implemented, ...), not from citation. Schema: `schema/design/dossier.md`.

Reference direction: design documents cite wiki pages freely; wiki pages link only to dossier roots (`[[designs/{slug}]]`), never into dossier internals.

## Directory Layout

- `raw/` — Source documents (papers, articles, repos, data). Exists for two purposes: re-visiting source captures (regenerating or auditing a capture against its original) and change detection against upstream sources. Never edit files in place — fidelity is the point. New files may be created here during ingest (e.g., saving a fetched URL or downloaded PDF). Incidental non-source assets serving neither purpose (browser-save scripts/styles) may be pruned.
  - `raw/articles/` — Web articles, blog posts, documentation
  - `raw/papers/` — Academic papers (markdown conversions)
  - `raw/papers/pdf/` — Original PDFs and pdfminer text extractions
  - `raw/chats/` — Conversation transcripts, chat exports
  - `raw/repos/` — Repository snapshots or extracts
  - `raw/data/` — Datasets, structured data files
- `wiki/` — LLM-generated and maintained markdown knowledge pages. The agent owns this directory entirely.
  - `wiki/index.md` — Master catalog of all wiki pages. Updated on every ingest.
  - `wiki/log.md` — Append-only operation log (change journal), newest-first.
  - `wiki/moves.log` — Mechanical record of page renames, moves, and deletions with tombstone dispositions; the forwarding addresses peer wikis follow. Covers `wiki/`, `raw/`, and design dossier roots. Generated with `scripts/movelog.sh`; dispositions are the one judgment field.
  - `wiki/episodes.md` — Optional narrative journal for bounded accounts of unbounded activity (research deep dives, corrections, session retrospectives). Routine ingests do not qualify.
  - `wiki/overview.md` — Evolving high-level synthesis across all topics (not a replacement for topic-specific syntheses).
  - `wiki/roadmap.md` — Forward-looking backlog: consolidated open design questions, candidate new topics, and wiki self-maintenance items. Distinct from `overview.md` (current understanding) by being about the future; pruned as items resolve rather than accumulated. Updated opportunistically, not on every ingest.
  - `wiki/{topic}/` — Topic subdirectories (e.g., `wiki/llm-wiki/`, `wiki/token-economics/`).
  - `wiki/{topic}/sources/` — Source-capture pages for that topic.
  - `wiki/{topic}/constructs/`, `entities/`, `syntheses/`, `assessments/`, `comparisons/`, `decisions/`, `invariants/` — Typed knowledge artifacts grouped by page type. The last two are normative (choices made, rules that must hold); the rest are descriptive.
  - `wiki/{topic}/subtopics/{subtopic}/` — Narrower topic area. Subtopics may repeat the same type folders and may nest when that materially improves navigation.
- `designs/` — The design surface: one dossier per design, per `schema/design/dossier.md`.
  - `designs/index.md` — Catalog of dossiers: one line each with description and lifecycle status.
  - `designs/{design-slug}/design.md` — The design document (required; the dossier's only external link target).
  - `designs/{design-slug}/alternatives/` — Optional fan-out of candidate variants plus a `weighing.md` adjudication document.
- `schema/` — The shared, agent-agnostic schema layer, canonical for all agents; tool adapters reference these files.
  - `schema/structure.md` — this file (repo-wide layout).
  - `schema/wiki/` — the wiki surface's schema: `page-format.md`, `page-types/` (one standalone normative file per page type plus `registry.md`), `conventions.md`, `ingest.md`, `lint.md`.
  - `schema/design/` — the design surface's schema: `dossier.md`.
- `scripts/` — Maintenance tooling (deterministic lint checker, move-log helper, search-index refresh).
- `wiki-manifest.yaml` — Per-wiki metadata: the wiki's goal, page-type subset, design-surface flag, agent adapters, peer registry, and (downstream instances only) the upstream repo and pinned commit.
- `seed/` — Upstream method repo (trellis) only: the instantiation layer — interview script, manifest and AGENTS.md templates, seed meta-pages. Not present in downstream instances.
- `.kiro/` — Kiro-specific adapter: steering wrappers, skills, settings, and agent runtime config. Contains no canonical content — steering files reference `schema/`.

## Wiki Organizational Model: Topic-First Typed Artifact Graph

The wiki has four distinct organizational axes:

| Axis | Role | Example |
|------|------|---------|
| Filesystem path | Topic/project locality plus human-visible type grouping | `wiki/intent-compiler/constructs/` |
| Frontmatter `type` | Authoritative artifact role | `type: construct` |
| Tags | Cross-cutting retrieval facets | `tags: [validation, formal-methods]` |
| Wikilinks | Graph relationships | `[[wiki/intent-compiler/constructs/process-weights]]` |

The filesystem is organized first by **topic** because that is how a human researcher navigates the vault, then by topic-local type folder because large flat topic directories are hard to scan. The page `type` field remains authoritative. Do not organize the wiki primarily by global type (no global `wiki/constructs/`, `wiki/syntheses/`, etc.).

The design surface deliberately uses a different model — **containment**: a dossier holds whatever its design needs, and a file's role comes from its position (`design.md`, `alternatives/`, assets), not from a type field. Relations within the wiki are links; relations within a dossier are structure.

## Key Principles

- One topic directory per broad subject area. Create new ones when a source doesn't fit existing topics.
- Source-capture pages live in `sources/`. Other typed artifacts live in the matching type folder: `constructs/`, `entities/`, `syntheses/`, `assessments/`, `comparisons/`, `decisions/`, or `invariants/`.
- Create subtopics under `subtopics/` when at least five pages cluster around a narrower question, when the cluster has its own sources plus downstream artifacts, or when readers would naturally seek it by name. Do not force every topic into subtopics.
- Folder and frontmatter type must agree.
- Prefer updating existing pages over creating near-duplicates.
- Every claim in wiki/ should trace back to a file in raw/.
- When new information contradicts existing content, note the contradiction explicitly and cite both sources — in a downstream synthesis or assessment, never inside a source-capture (source isolation).
- Source capture is the provenance boundary. After source capture, contributions fan out directly to any affected artifact type.
- Do not force every source through construct pages before it can update syntheses, assessments, or comparisons.
- Designs are not wiki pages: anything answering "what are we building and where is it?" belongs in a `designs/` dossier, not in a typed wiki folder.
