# Trellis Wiki Agent Contract

This is **Trellis**, the upstream repository for the Trellis wiki method: a structured-markdown, agent-maintained knowledge-base practice descended from the llm-wiki pattern. This file is the canonical cross-agent contract for Codex, Kiro, Claude Code, and other coding agents operating this repository.

The repo has two surfaces with a hard boundary:

- **Distributable** — `schema/` (normative page format, per-type specs, conventions, workflows), `scripts/` (lint, move-log helper, search-index refresh), and `seed/` (the instantiation layer). Downstream wikis vendor these. Nothing in them may depend on this repo's research content.
- **The lab** — `wiki/` and `raw/`: a working research wiki whose single goal is to **develop and evidence the wiki method itself, through its own operation**. Its subject is knowledge-base practice (the llm-wiki pattern lineage, agent context/retrieval/memory research, this method's own designs and operational evidence). Downstream wikis never inherit lab content; they reach it by cross-wiki reference.

The contract states the rules compactly. The detailed reference lives in `schema/` — `page-format.md`, `page-types/` (one normative file per type plus `registry.md`), `conventions.md`, `structure.md`, `ingest.md`, `lint.md`. Read the relevant `schema/` file before creating or auditing pages; `schema/` is authoritative for detail.

Kiro-specific steering and skills live under `.kiro/` and are thin wrappers referencing `schema/`. Claude-specific loading lives in `CLAUDE.md`. Do not duplicate this file or `schema/` files into tool-specific manifests.

## Core Mission

- Develop, evidence, and distribute the Trellis wiki method. Schema/workflow/tooling evolution is object-level work here — governed by `[[wiki/llm-wiki/designs/wiki-self-experimentation]]`, evidenced per `[[wiki/llm-wiki/constructs/operational-evidence]]`, with verdicts recorded as assessments.
- Keep the lab's research workload real: method findings only mean something while genuine research flows through this wiki. A practices lab with no content is a terrarium.
- Preserve provenance: every substantive wiki claim traces to a raw source or source-capture page.
- **Breadcrumbs over rails.** Every workflow here assumes an agent with judgment as the executor. Artifacts exist to make judgment cheap and auditable — never to replace it with pipelines, taxonomies, or required linkage. Determinism is reserved for what is already mechanical (git, the move log, the deterministic lint tier).
- Schema files are normative and **standalone** — no back-references to rationale. When a schema change weighs alternatives or rests on overturnable assumptions, record why in a `decision` page in the lab wiki; discovery is decision archaeology, not linkage.
- Downstream instances and peers are declared in `wiki-manifest.yaml`. This wiki maintains only its **outbound** links (including `peer::` links); inbound links are the linking wiki's problem. Every move or delete of a wiki/raw file gets a line in `wiki/moves.log` — that is the forwarding-address contract peers rely on.

## Directory Contract

- `raw/` contains source documents. Never edit raw files in place — fidelity is the point. New raw files may be added during ingest.
- `wiki/` contains agent-maintained markdown pages for the lab.
- `schema/` is the shared, agent-agnostic schema layer — canonical for all agents and for downstream instances; change it only with user agreement, and record substantial rationale as a decision page.
- `scripts/` contains maintenance tooling (`lint.py`, `movelog.sh`, `qmd-index.sh`).
- `seed/` contains the instantiation layer: `interview.md` (how an agent creates a new downstream wiki), `manifest-template.yaml`, `agents-md-template.md`, and `pages/` seed meta-pages.
- `.kiro/` contains Kiro-specific adapters referencing `schema/`.
- `wiki-manifest.yaml` declares this wiki's goal, page types, agents, and peers.

Wiki structure:

- `wiki/index.md` is the master catalog. Update it on every ingest.
- `wiki/log.md` is the append-only change journal, newest-first.
- `wiki/moves.log` is the mechanical move/delete record with tombstone dispositions (`scripts/movelog.sh` prints candidate lines).
- `wiki/episodes.md` (optional) holds narrative accounts of unbounded activity — deep dives, corrections, retrospectives. Routine ingests do not qualify.
- `wiki/overview.md` is the high-level synthesis; it states this wiki's single goal.
- `wiki/roadmap.md` is the forward-looking backlog, including the meta-experiment log.
- `wiki/{topic}/{type-folder}/` and `wiki/{topic}/subtopics/{subtopic}/` as defined in `schema/structure.md`.

## Artifact Model

Topic-first typed artifact graph. Allowed page types:

```yaml
type: source-capture | construct | entity | synthesis | design | assessment | comparison | decision | invariant | roadmap
```

The first seven are descriptive (evidence-graded); `decision` and `invariant` are normative (asserted); `roadmap` is a planning type (a pruned backlog of intended work — asserted, provenance-free, `sources` not required). Types also divide into three instigator tiers (`schema/page-types/registry.md`, Instigator Tiers): source-captures are ingest-instigated; interpretive pages (construct, entity, synthesis, comparison, assessment) are created by agent judgment or user request when their trigger fires — ingest is an occasion for interpretation, not a justification; authored pages (design, decision, invariant) are user-instigated. `roadmap` sits outside the tiers (structural — required by a container). Folder and frontmatter type must agree, except for skeleton-placed pages (`wiki/roadmap.md`; a design directory's subsidiary pages). A design is a **directory**, not a single file — `design.md` plus a scoped `design/phase` type and `roadmap`-typed `later.md`/`obligations.md` (`schema/page-types/design.md`, Directory Form; registry Scoped Types). If a page strongly matches multiple types, split it. Do not add a new page type without asking the user first.

## Page Format

Every ordinary wiki page uses YAML frontmatter per `schema/page-format.md`. Required: `title`, `type`, `description`, `sources`, `created`, `timestamp`. `source-capture` pages also require `evidence`; `construct`, `design`, and `entity` pages require `novelty`; `invariant` pages require `enforcement`. `roadmap` and scoped `design/phase` pages are exempt from `sources` (planning types assert intended work, not evidence) and carry no epistemic fields.

Epistemic fields split across two layers (two-axis model — see `schema/page-format.md`): `evidence` rates the source in isolation at ingest; `confidence` on non-source pages is derived from the evidence tiers and *independence* of cited sources. Wikis operated by the same owner and agents count as one source for independence — no cross-repo self-corroboration.

## Linking And Citations

- Use wikilinks relative to the repository root: `[[wiki/topic/type-folder/page-name]]`; root pages as `[[wiki/overview]]`, `[[wiki/index]]`, `[[wiki/log]]`.
- Cross-wiki links use a peer prefix — a target of the form `ai-research::wiki/topic/page` — resolved through `wiki-manifest.yaml`'s `peers` block (`schema/conventions.md`, Cross-Wiki Links). `scripts/lint.py` skips them; checking them is an on-demand agent task using the peer's `wiki/moves.log`.
- `source-capture` pages cite exact raw files with extensions, e.g. `[[raw/articles/source-slug.md]]`. Other page types normally cite source-capture pages.
- Every factual claim, data point, or referenced finding in page bodies should link to a source.

## Ingest Workflow

Per `schema/ingest.md`, two-staged. Stage 1 — capture: acquire raw copy → source-capture with `evidence` tier and routing candidates; bounded, source-isolated, delegable to a capture agent with no vault context. Stage 2 — review and routing, vault-aware, consuming the capture rather than the raw source: discuss (unless autonomous) → decide promotions per the instigator tiers → route to typed artifacts → detect contradictions (adjudicated downstream, never in the capture) → backlink audit → re-derive `confidence` → update `wiki/index.md` → refresh search index (`scripts/qmd-index.sh`, best-effort) → append to `wiki/log.md`.

## Query Workflow

1. Read `wiki/index.md` first.
2. For concept-level lookups, try `qmd search "<query>" -c wiki`, falling back to `Grep`/`Glob`/`Read` against `wiki/` (always works, no setup).
3. Read only the relevant pages; synthesize with wikilink citations.
4. If the answer is reusable, offer to save it as a wiki page.

For requests about creating or upgrading a downstream wiki: start with `seed/interview.md` (instantiation) or the upgrade prompt in `[[wiki/llm-wiki/designs/trellis-repo-design]]` (inheritance). For applying the method to a project codebase, see `[[wiki/llm-wiki/designs/project-wiki-application-guide]]` and `[[wiki/llm-wiki/designs/project-wiki-template]]`.

## Lint Workflow

1. Run `python3 scripts/lint.py` for the deterministic tier.
2. Perform the judgment tiers by reading pages (`schema/lint.md`), including: does new content serve this wiki's single goal?
3. Report results in the conversation; do not write report files.
4. Append a lint entry to `wiki/log.md`.

## Agent TODO Sections

`TODO(agent)` headings mark transient human commentary for later triage — read the TODO body and nearby context, then act, ask, or leave unchanged, per the same rules as the wider method.

## Cross-Agent Portability Rules

- `AGENTS.md` is canonical for shared behavior; `schema/` is canonical for detailed reference. No canonical content may live only in a tool-specific directory.
- `CLAUDE.md` imports this file with `@AGENTS.md` and contains only Claude-specific notes.
- `.kiro/` remains a thin Kiro adapter referencing `schema/`.
- Keep root always-on instructions compact; avoid duplicated manifests.
