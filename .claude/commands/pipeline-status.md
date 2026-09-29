---
description: Regenerate and show the unified job pipeline status across career-ops and ai-job-search
---

Run the cross-tool merge script:

```bash
python3 tools/pipeline_status.py
```

Then read `data/unified-tracker.md` and report to the user:

1. Totals for each tool and the unified unique-job count (duplicate roles across both tools are already collapsed into one row under one canonical ID — career-ops's ID wins).
2. Any **ID collisions** (same ID used for two genuinely different jobs) — flag clearly; the ai-job-search side needs a fresh ID (this is a numbering accident, not a duplicate, so it's not fixed by renumbering).
3. Any **pending renumbers** (`renumber_plan` in the JSON) — real duplicate jobs still under two different IDs. Show the list, then ask before running `python3 tools/pipeline_status.py --apply-renumber`, which rewrites ai-job-search's tracker, `seen_jobs.json`, and renames every `<id>_`-prefixed file. Never run it without asking, even if the user has approved the policy generally.
4. **Stale applied/drafted** entries older than ~10 days — suggest running `career-ops`'s `followup-cadence.mjs` or `ai-job-search`'s `/outcome followup` for the relevant ones.
5. The next safe shared ID (`next_safe_id` in the JSON) if the user is about to run a new scan/scrape.

Follow the routing table and rules in the `pipeline-pm` skill for any follow-up actions the user wants to take.
