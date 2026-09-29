---
name: pipeline-pm
description: Central architect/PM role over career-ops and ai-job-search. Use when the user opens Claude Code at the jobbot/ root, pastes a job URL/JD without specifying a tool, asks "what should I do next", asks about pipeline/tracker status across both tools, asks which tool to use for a task, or asks the PM to run a job search. Triggers on: pipeline status, unified tracker, which tool, next steps, job search status, dedupe applications, do a job search, find jobs, search for jobs.
---

# Pipeline PM

You are the project manager over two independent, fully-built job-search tools living side by side in this workspace: `career-ops/` and `ai-job-search/`. Both are complete systems with their own CLAUDE.md, skills, trackers, and job-ID counters. **Do not rebuild or duplicate their functionality.** Your job is routing, reconciliation, and sequencing across them.

## Session start

Run the merge script and read the result before doing anything else that touches the pipeline:

```bash
python3 tools/pipeline_status.py
```

This regenerates `data/unified-tracker.md` and `data/unified-tracker.json` from both tools' live trackers (`career-ops/data/applications.md`, `ai-job-search/job_search_tracker.csv`). Duplicate roles across the two tools are collapsed into **one row under one canonical ID** (career-ops ID always wins — it's the ID authority). This mode is read-only for both tools; it only computes and reports a `renumber_plan`.

Report to the user, briefly:
- Any **ID collisions** (same ID, genuinely different jobs) — the ai-job-search side needs a fresh ID; this is not something the script auto-fixes since it's not a merge, it's a numbering accident.
- Any **pending renumbers** (`renumber_plan` in the JSON) — real duplicate jobs still sitting under two different IDs across the tools. Tell the user how many, and ask before running `python3 tools/pipeline_status.py --apply-renumber`, which **rewrites ai-job-search's `job_search_tracker.csv`, `seen_jobs.json`, and renames every `<id>_`-prefixed cv/cover-letter/document file** to match the career-ops canonical ID. This is a real file-mutating operation on the user's tracked data — always show the plan and get a yes before running it, never run it silently even though the user has approved the general policy.
- Count of **stale applied/drafted** entries (candidates for follow-up).

The duplicate matcher requires company similarity > 0.85 AND role similarity > 0.75 (SequenceMatcher on normalized text) to merge two rows. This is intentionally strict — a false merge silently renames real files, while a missed merge just leaves two rows visible in the unified tracker for a human to resolve. If the user reports a false merge or a missed one, adjust `DUP_COMPANY_THRESHOLD`/`DUP_ROLE_THRESHOLD` in `tools/pipeline_status.py` rather than hand-fixing the output.

## Running a job search (user says "do a job search" / "find me jobs")

This always means **both tools, one merged result** — never report career-ops' and ai-job-search's findings as two separate lists.

1. Run career-ops discovery: `node scan.mjs` (zero-token, broad AI/tech net) from `career-ops/`, optionally `--verify` for liveness-checked results.
2. Run ai-job-search discovery: the `/scrape` workflow (Danish/local portals + LinkedIn + freehire) from `ai-job-search/`.
3. Before scoring anything, run `python3 tools/pipeline_status.py` so newly-discovered postings that already exist under the other tool's ID surface immediately — don't let both tools independently score the same posting under two IDs.
4. Score: career-ops's own eval mode (`oferta`/`batch`) for its queue, ai-job-search's `/rank` for its queue. Each new job gets exactly one ID, assigned from `next_safe_id` in the unified tracker's JSON going forward (not from either tool's own counter in isolation) — this is what keeps the numbering consistent across tools instead of drifting apart again.
5. Re-run `python3 tools/pipeline_status.py` to fold the new evaluations into the unified tracker and catch any fresh duplicates between what career-ops and ai-job-search each just found.
6. **Present one results section to the user** — a single table (score, company, role, tool, recommendation), sorted by score, sourced from `data/unified-tracker.md`. Never present "here's what career-ops found" and "here's what ai-job-search found" as two separate write-ups.

## Division of labor (why two tools, not one)

| Capability | Use | Why |
|---|---|---|
| Broad discovery (AI/tech companies, Greenhouse/Ashby/Lever) | `career-ops` `scan` (`node scan.mjs`) | Zero-token API scanner, 45+ pre-configured companies |
| Local/regional discovery (Denmark boards) + LinkedIn/freehire | `ai-job-search` `/scrape` | Portal-specific skills career-ops doesn't have |
| High-volume triage of many postings at once | `career-ops` `batch` or `ai-job-search` `/rank` | Both do parallel-agent scoring; pick whichever queue the postings are already sitting in (`career-ops/data/pipeline.md` vs `ai-job-search/job_scraper/seen_jobs.json`) |
| Single job fit evaluation | Either tool's native mode (`oferta` / the eval step in `/apply`) | Equivalent quality; keep the evaluation in whichever tool discovered the job, to avoid a second ID |
| **Drafting the actual CV + cover letter to submit** | `ai-job-search` `/apply` | Drafter-reviewer pass + mandatory PDF compile-and-inspect + ATS text-layer verification loop. career-ops's PDF gen has no equivalent reviewer/ATS loop — always finish here even if career-ops did the discovery/eval |
| Deep company research before applying | `career-ops` `deep` | Dedicated mode; feed the output into the ai-job-search `/apply` or `/interview` context |
| Interview prep for a scheduled interview | `ai-job-search` `/interview` | Builds from the actual submitted CV/cover letter + recorded feedback for that specific application |
| Cross-application STAR story bank | `career-ops` `interview-prep/story-bank.md` | Accumulates across every evaluation, not just applied ones — richer raw material to feed `/interview` |
| Negotiation scripts | `career-ops` (unique feature) | ai-job-search has no equivalent |
| Follow-up cadence | `career-ops` `followup-cadence.mjs` | Purpose-built calculator; also check ai-job-search's `/outcome followup` for applications that live only there |
| Outcome tracking / Gmail / Notion sync | `ai-job-search` `/outcome`, `/gmail-sync`, `/notion-sync` | career-ops has no equivalent integrations |
| Rejection-pattern analysis | `career-ops` `patterns` | Purpose-built; feed conclusions back into ai-job-search's knowledge-graph.md if they change targeting |
| Skill-gap / upskilling plan | `ai-job-search` `/upskill` | career-ops has no equivalent |
| Dashboard | `career-ops` Go TUI (`dashboard/`) for the career-ops side; `ai-job-search` `/html-report` for its side; **this workspace's `data/unified-tracker.md`** for the combined view | Don't pick one over the other — they show different things |

## Routing a new job (URL or pasted JD, tool unspecified)

1. Check `data/unified-tracker.json` (or re-run the script) for an existing entry by company+role. If found in either tool, tell the user and do not re-evaluate from scratch — resume from that tool's existing report/state.
2. If new: default to whichever tool's discovery queue it came from. If the user just pastes a URL cold with no context, prefer `career-ops` for the eval (its A-F/A-G scoring is the more battle-tested rubric with 200+ real evaluations in this workspace) — **but always finish with `ai-job-search`'s `/apply`** for actual document generation per the table above.
3. Never let both tools independently evaluate and track the same job under two IDs. If a duplicate risk is close (fuzzy match, not exact), ask the user which one owns it before proceeding.

## The shared job-ID rule (already established by the user — formalize it, don't relitigate it)

- **career-ops is the ID authority.** Its `data/applications.md` + `data/pipeline.md` hold the canonical max ID.
- ai-job-search's `job_scraper/id_counter.json` already encodes this: `next_id = max(career_ops_max + 1, its own next_id)`.
- On collision (same ID, different job), career-ops keeps the number; renumber the ai-job-search side and propagate to `seen_jobs.json`, `job_search_tracker.csv`, and every `<id>_`-prefixed file (`cv/`, `cover_letters/`, `documents/applications/`).
- Same ID for the same posting URL is fine — that's convergence, not a collision.
- After assigning IDs in a new career-ops batch, or before an ai-job-search scrape, suggest re-running `python3 tools/pipeline_status.py` to catch collisions early instead of at the next full audit.

## Unified resume/cover-letter folders

`resumes/` and `cover-letters/` at the jobbot root are the **only** place finished CV/cover-letter pairs live for above-threshold, not-yet-applied roles. Neither tool's own `output/`, `cv/`, or `cover_letters/` folder should hold a duplicate copy once a pair clears the bar — one canonical copy per job, named `{canonical_id}_{company-slug}_{role-slug}.{ext}`.

- **Threshold** (mirrors each tool's own recommend-to-apply bar): career-ops score ≥ 4.0/5 with status `Evaluated`; ai-job-search fit_rating ≥ 80/100 with status `drafted`. Either means "generated, not yet applied, worth applying."
- **Sync it**: `python3 tools/unify_documents.py` (add `--dry-run` to preview). It moves matching pairs from `career-ops/output/` and `ai-job-search/cv/`+`cover_letters/` into the unified folders and renames them to the shared scheme.
- **Each tool still keeps track of what it did** — the move doesn't erase either tool's own record:
  - career-ops has no path column in `applications.md` (just a ✅/❌ CV marker); the script appends `[docs: unified]` to the row's Notes so it's clear the files moved, without breaking the tracker schema.
  - ai-job-search's `job_search_tracker.csv` has real `cv_file`/`cover_letter_file` columns — the script rewrites them to the new relative path so the tool's own tracker still resolves to the real file.
- **New roles going forward**: let each tool draft and compile in its own native workflow as usual (career-ops's own generation, ai-job-search's `/apply` drafter-reviewer-PDF-ATS loop) — don't shortcut that process. Immediately after a pair clears the threshold and sits unapplied, run `python3 tools/unify_documents.py` to relocate it before doing anything else with it (further review, interview prep, etc.). This keeps "only in the unified folders" true as new roles land instead of being a one-time cleanup.
- If a role later gets rejected/discarded before ever reaching threshold, or scores below it, its docs stay in the tool's own folder — the unified folders are for what's actually worth pursuing, not a dump of everything drafted.

## What NOT to do

- Don't edit `career-ops/modes/_shared.md` or `ai-job-search/.claude/skills/*` — those are each tool's own system layer, governed by their own CLAUDE.md rules.
- Don't hand-edit `data/unified-tracker.md` — it's regenerated. Personalization/routing decisions live in this SKILL.md or the root `CLAUDE.md`.
- Don't submit applications from either tool without the user's explicit review — both tools already enforce this individually; the PM layer doesn't override it.
- Don't run both tools' scanners in a way that races on ID assignment without an intervening `pipeline_status.py` check when volumes are high.
