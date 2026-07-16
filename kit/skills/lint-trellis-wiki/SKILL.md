---
name: lint-trellis-wiki
description: Check a Trellis Wiki for deterministic conformance and judgment-level quality. Use when a user asks to lint, validate, audit, health-check, or review a Trellis Wiki.
---

# Lint a Trellis Wiki

1. Read the complete Wiki specification selected by the project. In this
   repository, use `../../../specs/wiki.md`.
2. Run `python3 ../../scripts/lint.py wiki <path-to-wiki>` when the kit script is
   available. Treat its output as the deterministic tier.
3. Review judgment concerns the script cannot prove:
   - source captures remain source-isolated;
   - evidence tiers match within-source reliability signals;
   - construct and entity confidence follows evidence and independence;
   - synthetic pages expose tensions instead of hiding them in a scalar score;
   - decisions and invariants are asserted artifacts with the required body;
   - pages serve the purpose and scope stated in `overview.md`;
   - contradictions, stale claims, and near-duplicates are visible.
4. Report errors, warnings, and judgment findings in that order with concrete
   remedies. Do not create a durable lint report file.
5. Fix findings only when the user requested changes. If the optional log is
   installed, record a concise lint entry after changes are completed.
