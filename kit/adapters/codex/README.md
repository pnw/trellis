# Codex Adapter

Codex discovers repository instructions through `AGENTS.md` and reusable
workflows through installed skill directories. Merge
`../../templates/repository/AGENTS.md` into target repository guidance, create
`trellis.yaml` when declarative routing is useful, and install only the skills
that project needs. Keep full specifications out of `AGENTS.md`; a triggered
skill reads the selected specification only when its workflow requires it. No
additional Codex-specific steering file is required.
