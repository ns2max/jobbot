---
description: Run a job search across both career-ops and ai-job-search, score everything, and present one merged results section
---

Follow the "Running a job search" section of the `pipeline-pm` skill exactly:

1. `node scan.mjs` in `career-ops/` (broad AI/tech net, zero-token API scan).
2. The `/scrape` workflow in `ai-job-search/` (local/regional portals + LinkedIn + freehire).
3. `python3 tools/pipeline_status.py` from the jobbot root to catch anything either tool just found that the other already tracks, before scoring.
4. Score each tool's queue with its own native evaluation (career-ops `oferta`/`batch`, ai-job-search `/rank`). Assign new IDs from `next_safe_id` in the unified tracker JSON, not from either tool's own counter alone.
5. `python3 tools/pipeline_status.py` again to fold results in and catch fresh duplicates between the two tools' new finds.
6. Present **one** results table to the user, sourced from `data/unified-tracker.md`, sorted by score — not two separate per-tool write-ups. Call out anything scoring below 4.0/5 as a discourage-applying case per both tools' own ethical-use rules.
7. If `renumber_plan` is non-empty afterward, tell the user and ask before running `--apply-renumber`.
8. `python3 tools/unify_documents.py` to sweep any newly above-threshold, unapplied CV/cover-letter pairs into `resumes/`/`cover-letters/`.
