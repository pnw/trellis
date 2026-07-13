# Lint Workflow

Agent-agnostic workflow for health-checking the wiki. This file is part of the shared `schema/` layer referenced by `AGENTS.md`.

Lint has two tiers: deterministic checks run by `scripts/lint.py`, and judgment checks performed by an agent reading pages. Lint results are reported in the conversation and fixed or triaged there — they are **not** durable documents; never write report files.

## Deterministic Tier — `python3 scripts/lint.py`

The script exits non-zero when errors are present.

### 🔴 Errors
- **Broken wikilinks** — `[[...]]` targets that don't resolve to a file (repository-root path, with `.md` appended for wiki pages)
- **Invalid type** — `type` field not in the registry: `source-capture`, `construct`, `entity`, `synthesis`, `design`, `assessment`, `comparison`, `decision`, `invariant`
- **Missing required frontmatter** — `title`, `type`, `description`, `sources`, `created`, `timestamp`
- **Missing or invalid evidence tier** — `type: source-capture` without a valid `evidence` value (`empirical-primary`, `empirical-secondary`, `official-docs`, `expert-analysis`, `vendor-claim`, `llm-generated`)
- **Misplaced epistemic fields** — `confidence` on a source-capture, or `evidence` on a non-source page
- **Source-capture in wrong location** — `type: source-capture` pages not in a `sources/` directory
- **Non-source in sources directory** — pages in a `sources/` directory without `type: source-capture`
- **Folder/type mismatch** — non-source pages not in the folder matching their frontmatter type
- **Missing novelty** — `construct`, `design`, or `entity` pages without a `novelty` field
- **Missing or invalid enforcement** — `type: invariant` without a valid `enforcement` value (`automated`, `manual`, `convention`, `external`, `unenforced`), or `enforcement` on a non-invariant page

### 🟡 Warnings
- **Confidence above ceiling** — declared `confidence` exceeding the derivation rules in `schema/page-format.md` (approximated from frontmatter: cited capture tiers, external URL domains, llm-generated grouping)
- **Orphan pages** — no incoming wikilinks from any page other than `wiki/index.md` or `wiki/log.md` (the log is an append-only journal, not a discovery path — a page mentioned only in a log entry is still effectively unreachable from content navigation)
- **Stale low-confidence pages** — `confidence: low` and `timestamp` older than 30 days

### 📊 Stats
The script ends with informational `stats:` lines — page counts by type, and per-topic capture vs derived counts with a derived-per-capture ratio. These are observability for the judgment tier and for tracking composition drift over time; they are **never findings and never targets** (`schema/page-types/registry.md`, Instigator Tiers — no page-count quota exists). Read them alongside judgment checks like thin topics or missing constructs, as context rather than verdicts.

## Judgment Tier — agent review

- **Contradictions** — conflicting claims between pages (cite both pages and the underlying raw sources)
- **Non-independent corroboration** — sources sharing authorship or commercial interest, or deriving from one another, counted as independent (circular reporting)
- **Cross-vault synthesis inside a source-capture** — capture body importing, endorsing, or reconciling claims from other pages (source-isolation violation)
- **Mixed-role pages** — pages answering multiple type questions (candidates for splitting)
- **Missing constructs** — concepts referenced in text with no dedicated construct page
- **Thin topics** — topics with only source-captures and no higher-order artifacts
- **Suggested ingests** — references in source-capture "Important References" sections worth capturing

## Output

Report findings in the conversation, ordered errors → warnings → judgment findings, with concrete fixes (e.g., "create page for X", "add link from A to B", "lower confidence on C to medium"). Fix mechanical errors directly when the fix is unambiguous.

Append to `wiki/log.md` under today's date heading: `* **Lint**: Wiki health check — X errors, Y warnings.`

## Rules

- Treat `wiki/{topic}/subtopics/{subtopic}/...` as valid when the terminal containing folder matches the page type.
- Do not flag `index.md`, `log.md`, `overview.md`, or `roadmap.md` for type or structure violations — they follow their own conventions.
- For contradictions, cite both pages and the underlying `raw/` sources.
