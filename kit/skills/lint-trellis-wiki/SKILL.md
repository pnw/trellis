---
name: lint-trellis-wiki
description: Check a Trellis Wiki for deterministic conformance and judgment-level quality. Use when a user asks to lint, validate, audit, health-check, or review a Trellis Wiki.
---

# Lint a Trellis Wiki

1. Run `python3 ../../scripts/lint.py wiki <path-to-wiki>` when the kit script is
   available. This deterministic tier does not require loading the Wiki
   specification. If the user requested only deterministic validation, report
   its output and stop.
2. Before a semantic audit, explanation, or repair, ensure the complete Wiki
   specification selected by the project is in active context. Resolve it from
   an explicit user selection,
   `trellis.wiki.specification` in `trellis.yaml`, or, in this repository,
   `../../../specs/wiki.md`. Prefer an immutable version-tagged URL and do not
   reload while its full text remains in active context. Reload after
   compaction before further semantic work.
3. Review judgment concerns the script cannot prove:
   - source captures remain source-isolated;
   - evidence tiers match within-source reliability signals;
   - construct and entity confidence follows evidence and independence,
     including same-operator wikis counting as one source and uncaptured URLs
     counting as no stronger than expert analysis;
   - synthetic pages expose tensions instead of hiding them in a scalar score;
   - decisions preserve a point-in-time choice and dispose of established
     invariants when superseded;
   - invariants are binding constraints with an origin, violation cost,
     enforcement mechanism, and meaningful removal path;
   - pages serve the purpose and scope stated in `overview.md`;
   - factual claims have inline provenance, and contradictions, stale claims,
     and near-duplicates are visible.
4. Report errors, warnings, and judgment findings in that order with concrete
   remedies. Do not create a durable lint report file.
5. Fix findings only when the user requested changes. If the optional log is
   installed, record a concise lint entry after changes are completed.
