# Trellis Instantiation Interview

How an agent creates a new downstream wiki from this repository. This is an intent brief for a wiki instance: interrogate, confirm, then build. Run it when someone says "create a new wiki from trellis" or points a fresh repository here.

Design rationale: [[wiki/llm-wiki/designs/trellis-repo-design]] and [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]] (in this repo's lab wiki). Adaptation guidance for project wikis specifically: [[wiki/llm-wiki/designs/project-wiki-application-guide]].

## Step 1 — Interview

Ask, then confirm the answers back before building. Keep it to one pass.

1. **Goal** (required, one sentence). A wiki cannot exist without a single stated goal. Many topics are fine; multiple goals are not — content serving a different goal belongs in a different wiki, cross-referenced. Push back on multi-goal answers until one goal survives.
2. **Page types.** Which subset of the registry (`schema/page-types/registry.md`) does this wiki need? Small wikis usually start with `source-capture`, `synthesis`, `design`, `decision`; add `construct`/`entity`/`assessment`/`comparison`/`invariant` when the workload warrants. The subset can grow later — adding a type is vendoring one more file.
3. **Link format.** Root-relative wikilinks (default, rename-resilient) or standard markdown relative links (better for plain-GitHub rendering). This choice propagates into the seeded conventions.
4. **Agents.** Which of claude-code / kiro / codex operate this wiki? Determines which adapter files to seed (CLAUDE.md wrapper, `.kiro/` steering, etc.).
5. **Peers.** Which other wikis will this one reference? At minimum usually `trellis` itself (for method cross-references). Record repo URLs.
6. **Optional features.** Local search index (`scripts/qmd-index.sh` + SessionStart hook)? Episodic log (`wiki/episodes.md`)?

## Step 2 — Build the instance

In the target repository:

1. Vendor `schema/` (drop per-type files for unchosen types; keep `registry.md` intact — it documents the full vocabulary including types not adopted) and `scripts/`.
2. Write `wiki-manifest.yaml` from `seed/manifest-template.yaml` with the interview answers, `upstream.repo` pointing here, and `upstream.pin` set to this repo's current commit.
3. Seed `wiki/` from `seed/pages/` — `overview.md` must state the goal verbatim from the interview.
4. Generate `AGENTS.md` from `seed/agents-md-template.md` (the instance owns it from then on — it is seeded, not inherited) plus the chosen agent adapters.
5. Run `python3 scripts/lint.py` — must pass with 0 errors before first use.
6. First `wiki/log.md` entry: instantiated from trellis at `<commit>`, with the interview answers summarized.

## Step 3 — Upgrades (for the life of the instance)

The canonical upgrade prompt, verbatim:

> Diff trellis `schema/` and `scripts/` from our pinned commit to upstream HEAD. Figure out what changed that matters for the slice this wiki uses (see `wiki-manifest.yaml`), apply it, run lint, bump the pin, and log what you did.

Breadcrumbs available: the manifest pin (makes "what changed" a concrete diff), per-type schema files (the diff reads by type), trellis's `wiki/moves.log` and decision pages (the "why", when it exists). There is no migration-note contract and no changelog beyond git — the executing agent supplies judgment.
