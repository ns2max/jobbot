# Handoff: recruiter cold-outreach resumes

Last updated 2026-11-03. Read this first if you're a new Claude Code session continuing this work.

## What was asked

Nishal supplied `recruiter-outreach/recruiters.csv`: 38 Canadian ML recruiters and hiring contacts, researched 2026-10-29.
The task was to tailor a resume for each contact that has a **published email**. Contacts in his field come first.
**No resumes** for contacts reachable only on LinkedIn.

## Current state (done)

- **18 resumes** sit in `recruiter-outreach/<NN>_<org>/`. Each folder holds:
  - `Nishal_Silva_Resume.{pdf,tex,txt}`
  - `CHANGES.md`: the edits made, plus a verification checklist
- There are 19 email contacts but 18 resumes: Fetch Recruiters' Alexia and Carlos share one, and only Alexia is emailed first.
  19 contacts were skipped because they only list LinkedIn or a phone number.
- `README.md` has the send order, email addresses, the variant each recipient got, and caveats such as "use the portal first" or "already applied".
- Everything passes: 2 pages each, a clean text layer for applicant tracking systems, email and phone readable as plain text, the permanent-residency line present.
- **Nothing has been sent.** `Outreach_status` in `recruiters.csv` still reads "Not contacted" everywhere.

## How the resumes are built

`python3 recruiter-outreach/build_resumes.py` regenerates all 18 resumes.

- The source is the golden `ai-job-search/resume_generic/Nishal_Silva_ML_Research_Engineer.tex`. It is read and never compiled in place.
- The edits are exact string replacements, grouped into variant sets: `INDUSTRIAL_CV`, `AUDIO`, `SIGNAL_MED`, `FINANCE`, `EDGE`, plus `V1` (golden unchanged).
  Each recipient also gets small extras, such as a relocation note on the status line.
  The build stops if any anchor string is missing from the golden file.
- The golden layout is tight: there's a hard `\newpage` before McGill. Anything you add must save the same number of lines somewhere,
  or the resume goes to 3 pages. The script already lowers line spacing from 1.05 to 1.03 and trims a postdoc bullet in most variants.
- **LaTeX setup in a fresh cloud container:** pdflatex isn't preinstalled and tectonic isn't available. Install with:
  `apt-get update && apt-get install -y --no-install-recommends texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-plain-generic tex-gyre`

## Decisions made with Nishal

- **">90% F1" is a real result**; he confirmed it on 2026-11-03. It's the MUSMET real-time inference services figure. F1 0.76 is the separate published JAES system.
  The resumes keep the golden wording. Both knowledge graphs, `ai-job-search/CLAUDE.md` and `career-ops/modes/_profile.md` were updated to match.
- **Golden-resume rule:** keep edits to the minimum. Every change is listed in that recipient's `CHANGES.md`.
- **Commits:** don't commit or push until Nishal confirms. He sometimes has local changes to push first.
  Never rewrite history on `recruiter-outreach-resumes`; it's already pushed. Merge `main` in instead.

## Open items / next steps

1. **Skill-file conflict (needs Nishal's OK):** three files still say "never write >90% F1". They are `03-writing-style.md`, `05-cv-templates.md` and `06-cover-letter-templates.md`,
   all under `ai-job-search/.claude/skills/job-application-assistant/`. The root `CLAUDE.md` forbids editing those from the root role, so it has to happen as an ai-job-search task.
2. **Live vacancy check:** this session's network blocked every company and recruiter site, so the tailoring rests on the CSV's research.
   Re-check the live postings before sending, especially LuxTronic, Oncoustics, AAVAA and Canny Vision.
3. **Outreach emails:** not drafted yet. The CSV's `Personalization_angle` column holds a one-line hook for each contact. `cold-messages/` has earlier examples of the style.
4. **Tracking:** after each send, update `Outreach_status`, `Date_sent` and `Follow_up_date` in `recruiters.csv`.
5. **Special handling** (also in the README):
   - VANJOBS: use the vanjobs.ca portal first.
   - Kovasys: the email may be stale; use their portal.
   - Layer 6: he already applied to TD roles, so cite the requisitions in a single thread.
   - Fetch: email Alexia only.
   - LuxTronic: confirm employee vs contractor and whether they can pay him in Canada.
6. **Branches merged (2026-11-03):** this work and every `claude/*` branch were merged into `main` and pushed.
7. **Unified tracker is out of date:** run `python3 tools/pipeline_status.py` on **Nishal's computer**.
   `ai-job-search/job_search_tracker.csv` is gitignored, so a cloud checkout can't regenerate the tracker without dropping every ai-job-search row.
   During the merge, `data/unified-tracker.{md,json}` kept main's version. That version still includes ai-job-search's data,
   but it lacks career-ops jobs #1462-#1476 (the music-tech Canada sweep).
