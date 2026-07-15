---
name: lint
description: Health-check the wiki for contradictions, orphans, broken links, and gaps. Use when the user asks to lint or audit the wiki.
---

# Lint (Kiro adapter)

Follow the canonical, agent-agnostic lint workflow in `schema/wiki/lint.md`: run `python3 scripts/lint.py` for the deterministic tier, perform the judgment tier by reading pages, report results in the conversation (never write report files), and append a one-line count entry to `wiki/log.md`. Do not add check definitions here.

#[[file:schema/wiki/lint.md]]
