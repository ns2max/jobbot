# Session Handoff — Batch Pipeline Resume (2026-08-25)

## Status: STOPPED on user command. Do NOT resume automatically. Wait for explicit user instruction to continue.

## What happened this session

1. Resumed a stalled batch of 158 pending job offers from `data/pipeline.md` (inbox URLs never evaluated).
2. Built `batch/batch-input.tsv` from all `- [ ]` entries in `data/pipeline.md` (158 offers, ids 1-158).
3. Ran `./batch/batch-runner.sh --parallel 4` repeatedly, hitting Claude session usage limits multiple times (resets roughly every ~3-5h). Re-ran with `--retry-failed --max-retries 15` after each reset.
4. Mid-session, user asked to expand scope:
   - **Whole of Canada** — already was in place (`modes/_profile.md` "Location & visa" section, hard-exclude non-Canada, city ranking Montreal > Toronto > any other Canadian city). No change needed there.
   - **New domains**: Teaching (university faculty/postdoc AND K-12 STEM/CS/robotics teaching) and Consulting (AI/ML consultant, advisory, fractional CTO) — NOT previously covered. Added.
   - **Smaller educational institutes**: colleges, polytechnics, community colleges — added.
5. User then said stop — killed the batch-runner process and all `claude -p` worker processes. Batch state is preserved and resumable.

## Config changes made (all committed to working tree, NOT yet git-committed)

- `config/profile.yml` — added 2 archetypes: "Assistant/Adjunct Professor (AI/ML/Signal Processing)" and "AI/ML Consultant (Independent or Firm)".
- `modes/_profile.md` — added archetype rows + adaptive framing + proof-point mapping for:
  - Assistant/Adjunct Professor (AI/ML)
  - AI/ML Consultant
  - K-12 STEM/CS Teacher
  - College/Polytechnic Instructor
- `portals.yml`:
  - `title_filter.positive` — added keywords for teaching (Professor, Faculty, Lecturer, Sessional Instructor, Postdoctoral, Research Chair, STEM Teacher, Computer Science Teacher, Robotics Teacher, Coding Instructor, College/Polytechnic Instructor, Community College) and consulting (AI Consultant, ML Consultant, Technical Advisor, AI Advisory, Fractional CTO, Fractional Head of AI).
  - `search_queries` — added 7 new Canada-wide WebSearch queries: faculty/professor, postdoc/research chair, sessional instructor, AI/ML consultant & advisory (x2), K-12 STEM/CS/robotics teacher, college/polytechnic instructor.

**These config changes have NOT yet been exercised** — no scan has been run against the new teaching/consulting keywords yet. That's the next step once batch processing finishes.

## Batch pipeline state (as of stop)

- Input: `batch/batch-input.tsv` — 158 offers (ids 1-158), pulled from `data/pipeline.md` pending entries.
- State: `batch/batch-state.tsv` — resumable, tracks per-offer status (completed/failed/processing).
- Last count at stop: ~73 completed, ~63 failed (mostly "session limit" errors, NOT real failures — safe to retry), 1 stuck "processing" (offer id 98, jobs.lever.co/tri — was mid-flight when killed, will show as stale "processing"; on next run this may need manual reset to "pending" or handled by rerunning with `--retry-failed`).
- Report numbers used so far: up to ~1128 (see `reports/` dir, most recent files dated 2026-08-25).
- `data/applications.md` max entry: #1038 (tracker merges have been running automatically as part of batch-runner's post-run step).

## To resume in a new session

1. Check `batch/batch-state.tsv` for current completed/failed/processing counts:
   ```bash
   awk -F'\t' 'NR>1{c[$3]++} END{for(k in c) print k, c[k]}' batch/batch-state.tsv
   ```
2. If offer #98 (or any) is stuck in "processing" from the kill, it's stale — `--retry-failed` won't touch it since it's not "failed". May need to manually edit its status in `batch/batch-state.tsv` to "failed" or delete its row so it's picked up as pending again.
3. Resume with:
   ```bash
   ./batch/batch-runner.sh --retry-failed --parallel 4 --max-retries 15
   ```
   (bump `--parallel` if user wants more concurrency — user asked for "more parallels" mid-session, only partially honored due to in-flight risk).
4. If it hits "session limit" errors again, the error message in `batch/batch-state.tsv` column 8 tells you the exact reset time (e.g. "resets 2:20am (America/Toronto)") — wait until then, then rerun the same `--retry-failed` command.
5. Once all 158 offers are completed (or maxed out on retries), run:
   ```bash
   node merge-tracker.mjs
   node verify-pipeline.mjs
   ```
6. **Then run `/career-ops scan`** to actually exercise the new teaching/consulting/K-12/whole-Canada search_queries added to `portals.yml` — this hasn't been done yet. That's a separate step from draining the existing pipeline backlog.

## Known cost concern (raised by user)

User flagged that autonomous polling (ScheduleWakeup loop, ~25min ticks) burns tokens on every wake even when there's no real progress to report, because each tick reloads full session context. Loop was stopped per user request. **Do not re-arm an autonomous polling loop without the user explicitly asking for it.** If resuming batch processing, prefer to just run it and report back once, rather than polling repeatedly.

## Files touched / untracked this session (not committed)

- `batch/batch-input.tsv`, `batch/batch-state.tsv` (gitignored, working state)
- `batch/logs/*.log` (gitignored, per-offer logs — useful for debugging specific failures)
- ~90 new files in `reports/` and matching `output/*.md` (CV + cover letter) for completed offers
- `data/applications.md`, `data/pipeline.md`, `data/scan-history.tsv` — modified by merges
- `config/profile.yml`, `modes/_profile.md`, `portals.yml` — modified for scope expansion (see above)
