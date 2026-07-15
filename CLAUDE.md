@AGENTS.md

# Claude Code Notes

This file is a thin Claude Code wrapper. Keep shared project behavior in `AGENTS.md`; add content here only when it is specific to Claude Code loading, memory, or commands.

`.claude/settings.json` runs `scripts/qmd-index.sh` in the background on `SessionStart` — a Claude-Code-specific convenience on top of the cross-agent-portable script. The canonical instruction to run this script (for Kiro, Codex, and any other agent) lives in `AGENTS.md`'s Ingest Workflow and `schema/wiki/ingest.md`, not here.
