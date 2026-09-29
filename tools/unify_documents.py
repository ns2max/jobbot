#!/usr/bin/env python3
"""
Moves resume + cover-letter pairs for above-threshold, not-yet-applied roles
out of each tool's own folder and into the unified jobbot/resumes/ and
jobbot/cover-letters/ folders, renamed to a single consistent scheme:

    resumes/{id}_{company-slug}_{role-slug}.{ext}
    cover-letters/{id}_{company-slug}_{role-slug}.{ext}

"Above threshold" mirrors each tool's own recommend-to-apply bar:
  - career-ops: score >= 4.0/5, status == "Evaluated" (evaluated, not yet applied)
  - ai-job-search: fit_rating >= 80/100 (the equivalent bar), status == "drafted"
    (drafted = documents generated, not yet applied)

Each tool keeps a record of what it did:
  - career-ops has no path column in applications.md (only a ✅/❌ CV marker) --
    left untouched; a short tag is appended to the Notes column pointing at the
    new location.
  - ai-job-search's job_search_tracker.csv DOES store cv_file/cover_letter_file
    paths -- these are rewritten to point at the unified location.

This is a MOVE (not copy): after running, the unified folders are the only
place these files live. Re-run any time after new evaluations to sweep newly
above-threshold, unapplied roles.

Usage: python3 tools/unify_documents.py [--dry-run]
"""
import csv
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAREER_OPS = ROOT / "career-ops"
AI_JOB_SEARCH = ROOT / "ai-job-search"
RESUMES = ROOT / "resumes"
COVER_LETTERS = ROOT / "cover-letters"

CO_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([\d-]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*([\d.]+)/5\s*\|\s*(\S+)\s*\|\s*(\S*)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$"
)

CO_THRESHOLD = 4.0
AJS_THRESHOLD = 80.0


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "unknown"


def find_career_ops_candidates():
    path = CAREER_OPS / "data" / "applications.md"
    candidates = []
    if not path.exists():
        return candidates
    for line in path.read_text(encoding="utf-8").splitlines():
        m = CO_ROW_RE.match(line.strip())
        if not m:
            continue
        num, date, company, role, score, status, cv, report, notes = m.groups()
        if status != "Evaluated":
            continue
        try:
            if float(score) < CO_THRESHOLD:
                continue
        except ValueError:
            continue
        candidates.append({"id": int(num), "company": company, "role": role, "notes": notes})
    return candidates


def find_ai_job_search_candidates():
    path = AI_JOB_SEARCH / "job_search_tracker.csv"
    candidates = []
    if not path.exists():
        return candidates
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("status") != "drafted":
                continue
            try:
                if float(r.get("fit_rating") or 0) < AJS_THRESHOLD:
                    continue
            except ValueError:
                continue
            if not (r.get("id") or "").strip().isdigit():
                continue
            candidates.append(
                {
                    "id": int(r["id"]),
                    "company": r.get("company", ""),
                    "role": r.get("role", ""),
                    "cv_file": r.get("cv_file", ""),
                    "cover_letter_file": r.get("cover_letter_file", ""),
                }
            )
    return candidates


def move_career_ops_docs(candidates, dry_run):
    moved = []
    out_dir = CAREER_OPS / "output"
    if not out_dir.exists():
        return moved
    for c in candidates:
        jid = c["id"]
        slug = f"{jid}_{slugify(c['company'])}_{slugify(c['role'])}"
        for f in sorted(out_dir.glob(f"{jid}-*")):
            is_cover = "coverletter" in f.name
            dest_dir = COVER_LETTERS if is_cover else RESUMES
            dest = dest_dir / f"{slug}{f.suffix}"
            print(f"[career-ops] {f.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
            if not dry_run:
                shutil.move(str(f), str(dest))
            moved.append(c)
    return moved


def move_ai_job_search_docs(candidates, dry_run):
    moved = []
    path_updates = {}
    for c in candidates:
        jid = c["id"]
        slug = f"{jid}_{slugify(c['company'])}_{slugify(c['role'])}"
        for field, src_field, dest_dir, tag in (
            ("cv_file", "cv_file", RESUMES, "resume"),
            ("cover_letter_file", "cover_letter_file", COVER_LETTERS, "cover-letter"),
        ):
            rel = c.get(src_field, "")
            if not rel:
                continue
            src = AI_JOB_SEARCH / rel
            new_paths = []
            for f in sorted(src.parent.resolve().glob(src.stem + ".*")):
                dest = dest_dir / f"{slug}{f.suffix}"
                if f.resolve() == dest.resolve():
                    new_paths.append(Path(os.path.relpath(dest, AI_JOB_SEARCH)))
                    continue  # already in place from a prior run -- not a move
                print(f"[ai-job-search] {f.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
                if not dry_run:
                    shutil.move(str(f), str(dest))
                new_paths.append(Path(os.path.relpath(dest, AI_JOB_SEARCH)))
            if new_paths:
                path_updates[(jid, field)] = str(sorted(new_paths, key=lambda p: p.suffix)[0])
        moved.append(c)
    return moved, path_updates


def update_ai_job_search_csv(path_updates, dry_run):
    if not path_updates or dry_run:
        return
    csv_path = AI_JOB_SEARCH / "job_search_tracker.csv"
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if not (r.get("id") or "").strip().isdigit():
            continue
        jid = int(r["id"])
        for field in ("cv_file", "cover_letter_file"):
            key = (jid, field)
            if key in path_updates:
                r[field] = path_updates[key]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"ai-job-search/job_search_tracker.csv: updated {len(path_updates)} path reference(s)")


def tag_career_ops_notes(moved, dry_run):
    if not moved or dry_run:
        return
    path = CAREER_OPS / "data" / "applications.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    ids = {c["id"] for c in moved}
    out = []
    tagged = 0
    for line in lines:
        m = CO_ROW_RE.match(line.strip())
        if m and int(m.group(1)) in ids and "[docs: unified]" not in line:
            line = line[:-2].rstrip() + " [docs: unified] |"
            tagged += 1
        out.append(line)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"career-ops/data/applications.md: tagged {tagged} row(s) with [docs: unified]")


def main():
    dry_run = "--dry-run" in sys.argv
    RESUMES.mkdir(exist_ok=True)
    COVER_LETTERS.mkdir(exist_ok=True)

    co_candidates = find_career_ops_candidates()
    ajs_candidates = find_ai_job_search_candidates()

    print(f"career-ops: {len(co_candidates)} above-threshold unapplied role(s)")
    print(f"ai-job-search: {len(ajs_candidates)} above-threshold unapplied role(s)")
    print()

    co_moved = move_career_ops_docs(co_candidates, dry_run)
    ajs_moved, path_updates = move_ai_job_search_docs(ajs_candidates, dry_run)

    tag_career_ops_notes(co_moved, dry_run)
    update_ai_job_search_csv(path_updates, dry_run)

    print()
    print(f"{'[DRY RUN] would move' if dry_run else 'Moved'} {len(co_moved)} career-ops pair(s), {len(ajs_moved)} ai-job-search pair(s)")


if __name__ == "__main__":
    main()
