#!/usr/bin/env python3
"""
Central PM tool for the jobbot workspace (career-ops + ai-job-search).

Reads both tools' trackers, collapses duplicate roles (same job tracked
independently by both tools) into ONE canonical row under ONE ID, and writes:
  - data/unified-tracker.md   (single results table, source-tagged)
  - data/unified-tracker.json (same rows + diagnostics + renumber plan)

career-ops is the ID authority (per ai-job-search/job_scraper/id_counter.json's
conflict_rule): when a duplicate spans both tools, the canonical ID is always
the career-ops ID.

Modes:
  python3 tools/pipeline_status.py                 # dry run: report + plan only, no writes to either tool
  python3 tools/pipeline_status.py --apply-renumber # actually renumber ai-job-search's duplicate IDs to match
                                                     # career-ops (rewrites job_search_tracker.csv, seen_jobs.json,
                                                     # and renames every <id>_-prefixed cv/cover-letter/document file)

--apply-renumber is the only mode that writes inside ai-job-search/. It is
idempotent and prints every change it makes. Never touches career-ops/.
"""
import csv
import json
import re
import shutil
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAREER_OPS = ROOT / "career-ops"
AI_JOB_SEARCH = ROOT / "ai-job-search"
OUT_DIR = ROOT / "data"

CO_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([\d-]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*([\d.]+/5|\S*)\s*\|\s*(\S+)\s*\|\s*(\S*)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$"
)

DUP_COMPANY_THRESHOLD = 0.85
DUP_ROLE_THRESHOLD = 0.75


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def similar(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def role_sim(a, b):
    return similar(a["role"], b["role"])


def is_dup(a, b):
    return similar(a["company"], b["company"]) > DUP_COMPANY_THRESHOLD and role_sim(a, b) > DUP_ROLE_THRESHOLD


def parse_career_ops():
    path = CAREER_OPS / "data" / "applications.md"
    rows = []
    if not path.exists():
        return rows, None
    max_id = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        m = CO_ROW_RE.match(line.strip())
        if not m:
            continue
        num, date, company, role, score, status, cv, report, notes = m.groups()
        if not num.isdigit():
            continue
        job_id = int(num)
        max_id = max(max_id, job_id)
        rows.append(
            {
                "id": job_id,
                "date": date,
                "company": company,
                "role": role,
                "status": status,
                "score": score,
                "source_tool": "career-ops",
                "notes": notes,
                "link": report,
            }
        )
    return rows, max_id


def parse_ai_job_search():
    path = AI_JOB_SEARCH / "job_search_tracker.csv"
    rows = []
    if not path.exists():
        return rows, None
    max_id = 0
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            raw_id = (r.get("id") or "").strip()
            if not raw_id.isdigit():
                continue
            job_id = int(raw_id)
            max_id = max(max_id, job_id)
            rows.append(
                {
                    "id": job_id,
                    "date": r.get("date", ""),
                    "company": r.get("company", ""),
                    "role": r.get("role", ""),
                    "status": r.get("status", ""),
                    "score": r.get("fit_rating", ""),
                    "source_tool": "ai-job-search",
                    "notes": r.get("notes", ""),
                    "link": r.get("source", ""),
                }
            )
    return rows, max_id


def find_id_collisions(co_rows, ajs_rows):
    """Same ID, but genuinely different jobs -- not a duplicate, a numbering accident."""
    co_by_id = {r["id"]: r for r in co_rows}
    collisions = []
    for r in ajs_rows:
        co = co_by_id.get(r["id"])
        if co and not is_dup(co, r):
            collisions.append({"id": r["id"], "career_ops": co, "ai_job_search": r})
    return collisions


def cluster_duplicates(co_rows, ajs_rows):
    """
    Group career-ops and ai-job-search rows into one cluster per real-world job.
    Each ai-job-search row is matched to at most one career-ops row: the BEST
    role-similarity match above threshold among companies that match, not the
    first one found -- two postings at the same company with similar generic
    titles (e.g. "Underwriting ML" vs "Fraud ML") must not collapse together.
    Returns list of clusters, each a dict {career_ops: [rows], ai_job_search: [rows]}.
    """
    co_used = [False] * len(co_rows)
    clusters = []
    for a in ajs_rows:
        best_ci, best_score = None, 0.0
        for ci, c in enumerate(co_rows):
            if co_used[ci]:
                continue
            if similar(a["company"], c["company"]) <= DUP_COMPANY_THRESHOLD:
                continue
            score = role_sim(a, c)
            if score > DUP_ROLE_THRESHOLD and score > best_score:
                best_ci, best_score = ci, score
        if best_ci is not None:
            co_used[best_ci] = True
            clusters.append({"career_ops": [co_rows[best_ci]], "ai_job_search": [a]})
        else:
            clusters.append({"career_ops": [], "ai_job_search": [a]})
    for ci, used in enumerate(co_used):
        if not used:
            clusters.append({"career_ops": [co_rows[ci]], "ai_job_search": []})
    return clusters


CO_APPLIED_STATUSES = {"applied", "responded", "interview", "offer", "rejected", "discarded"}
AJS_APPLIED_STATUSES = {"applied"}


def co_score_100(score_str):
    """career-ops score is 'X.X/5' -- rescale to /100 so both tools share one scale."""
    m = re.match(r"([\d.]+)/5", score_str or "")
    return round(float(m.group(1)) * 20, 1) if m else None


def ajs_score_100(score_str):
    try:
        return round(float(score_str), 1)
    except (TypeError, ValueError):
        return None


def build_unified_row(cluster):
    """Collapse a cluster into ONE row under ONE canonical ID. career-ops ID wins."""
    co = cluster["career_ops"]
    ajs = cluster["ai_job_search"]
    if co:
        primary = co[0]
        canonical_id = primary["id"]
        source = "both" if ajs else "career-ops"
        tool_tag = "c+a" if ajs else "c"
    else:
        primary = ajs[0]
        canonical_id = primary["id"]
        source = "ai-job-search"
        tool_tag = "a"

    aliases = sorted({r["id"] for r in (co + ajs) if r["id"] != canonical_id})
    statuses = []
    if co:
        statuses.append(f"{co[0]['status']} (career-ops)")
    if ajs:
        statuses.append(f"{ajs[0]['status']} (ai-job-search)")
    scores = []
    if co:
        scores.append(f"{co[0]['score']} (co)")
    if ajs:
        scores.append(f"{ajs[0]['score']} (ajs)")
    notes = " | ".join(x for x in [co[0]["notes"] if co else "", ajs[0]["notes"] if ajs else ""] if x)

    # Unified score: rescale career-ops' X/5 to /100 (its own scale, just stretched) and
    # ai-job-search's fit_rating is already /100. If both tools scored the job, average the
    # two /100 numbers -- neither tool's rubric is authoritative over the other's, so a plain
    # mean is the deliberately simple unifying rule (see SKILL.md "Unified scoring").
    co_100 = co_score_100(co[0]["score"]) if co else None
    ajs_100 = ajs_score_100(ajs[0]["score"]) if ajs else None
    parts = [x for x in (co_100, ajs_100) if x is not None]
    unified_score = round(sum(parts) / len(parts), 1) if parts else None

    # Unapplied: true only if every tool that has this job still shows a pre-apply status.
    co_unapplied = (not co) or co[0]["status"].strip().lower() not in CO_APPLIED_STATUSES
    ajs_unapplied = (not ajs) or ajs[0]["status"].strip().lower() not in AJS_APPLIED_STATUSES
    unapplied = co_unapplied and ajs_unapplied and (co or ajs)

    return {
        "id": canonical_id,
        "aliases": aliases,
        "date": (co[0]["date"] if co else ajs[0]["date"]),
        "company": primary["company"],
        "role": primary["role"],
        "status": " / ".join(statuses),
        "score": " / ".join(scores),
        "unified_score": unified_score,
        "source_tool": source,
        "tool_tag": tool_tag,
        "unapplied": unapplied,
        "notes": notes,
        "career_ops_link": co[0]["link"] if co else "",
        "ai_job_search_link": ajs[0]["link"] if ajs else "",
    }


STALE_STATUSES = {"applied", "drafted"}


def flag_stale(rows):
    return [r for r in rows if any(s in r["status"].lower() for s in STALE_STATUSES)]


def build_renumber_plan(clusters):
    """Every ai-job-search ID that must change to match its cluster's canonical (career-ops) ID."""
    plan = []
    for cl in clusters:
        if not cl["career_ops"] or not cl["ai_job_search"]:
            continue
        canonical_id = cl["career_ops"][0]["id"]
        for a in cl["ai_job_search"]:
            if a["id"] != canonical_id:
                plan.append({"old_id": a["id"], "new_id": canonical_id, "company": a["company"], "role": a["role"]})
    return plan


def apply_renumber(plan):
    """Actually rewrite ai-job-search's tracker/seen_jobs/files so its ID matches the canonical (career-ops) one."""
    if not plan:
        print("Nothing to renumber.")
        return

    csv_path = AI_JOB_SEARCH / "job_search_tracker.csv"
    rows = []
    fieldnames = None
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    id_map = {str(p["old_id"]): p["new_id"] for p in plan}
    for r in rows:
        if r.get("id") in id_map:
            new_id = id_map[r["id"]]
            print(f"tracker: id {r['id']} -> {new_id} ({r.get('company')})")
            r["id"] = str(new_id)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    seen_path = AI_JOB_SEARCH / "job_scraper" / "seen_jobs.json"
    if seen_path.exists():
        data = json.loads(seen_path.read_text(encoding="utf-8"))
        seen = data.get("seen", data)
        for url, entry in seen.items():
            if entry.get("id") in id_map.values():
                continue
            if str(entry.get("id")) in id_map:
                old = entry["id"]
                entry["id"] = id_map[str(old)]
                print(f"seen_jobs.json: {url} id {old} -> {entry['id']}")
        seen_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    for old_id, new_id in [(p["old_id"], p["new_id"]) for p in plan]:
        for folder in ["cv", "cover_letters"]:
            d = AI_JOB_SEARCH / folder
            if not d.exists():
                continue
            for f in d.glob(f"{old_id}_*"):
                new_name = f.name.replace(f"{old_id}_", f"{new_id}_", 1)
                target = d / new_name
                print(f"rename: {f.relative_to(AI_JOB_SEARCH)} -> {target.relative_to(AI_JOB_SEARCH)}")
                f.rename(target)
        apps_dir = AI_JOB_SEARCH / "documents" / "applications"
        if apps_dir.exists():
            for d in apps_dir.glob(f"{old_id}_*"):
                new_name = d.name.replace(f"{old_id}_", f"{new_id}_", 1)
                target = apps_dir / new_name
                print(f"rename dir: {d.relative_to(AI_JOB_SEARCH)} -> {target.relative_to(AI_JOB_SEARCH)}")
                d.rename(target)

    print(f"\nRenumbered {len(plan)} ai-job-search job(s) to match career-ops canonical IDs.")
    print("Re-run without --apply-renumber to confirm the unified tracker now shows single-ID rows.")


def write_markdown(unified_rows, collisions, renumber_plan, co_max, ajs_max, path):
    lines = []
    lines.append("# Unified Job Pipeline Tracker (generated -- do not hand-edit)")
    lines.append("")
    lines.append(
        f"Merged from `career-ops/data/applications.md` (max id {co_max}) and "
        f"`ai-job-search/job_search_tracker.csv` (max id {ajs_max}). "
        "Duplicate roles across both tools are collapsed into one row under one canonical ID "
        "(career-ops ID wins). Regenerate with `python3 tools/pipeline_status.py`."
    )
    lines.append("")

    if collisions:
        lines.append(f"## ⚠️ ID collisions ({len(collisions)}) -- same ID, genuinely different jobs")
        for c in collisions:
            lines.append(
                f"- `#{c['id']}`: career-ops=**{c['career_ops']['company']} / {c['career_ops']['role']}** "
                f"vs ai-job-search=**{c['ai_job_search']['company']} / {c['ai_job_search']['role']}** "
                "-- the ai-job-search job needs a fresh ID (not covered by --apply-renumber; different jobs, not a merge)"
            )
        lines.append("")

    if renumber_plan:
        lines.append(f"## Pending renumbering ({len(renumber_plan)}) -- run `python3 tools/pipeline_status.py --apply-renumber`")
        for p in renumber_plan:
            lines.append(f"- ai-job-search #{p['old_id']} -> #{p['new_id']} ({p['company']} / {p['role']})")
        lines.append("")

    unapplied_rows = [r for r in unified_rows if r["unapplied"]]
    if unapplied_rows:
        lines.append(f"## Unapplied roles ({len(unapplied_rows)}) -- sorted by unified score")
        lines.append("")
        lines.append("| ID | Tool | Company | Role | Unified Score /100 | Notes |")
        lines.append("|----|------|---------|------|---------------------|-------|")
        for r in sorted(unapplied_rows, key=lambda r: r["unified_score"] or 0, reverse=True):
            note = (r["notes"] or "").replace("|", "/")
            if len(note) > 140:
                note = note[:140] + "…"
            lines.append(f"| {r['id']} | {r['tool_tag']} | {r['company']} | {r['role']} | {r['unified_score']} | {note} |")
        lines.append("")

    lines.append("## Results")
    lines.append("")
    lines.append("| ID | Tool | Aliases | Date | Company | Role | Score | Unified /100 | Status | Notes |")
    lines.append("|----|------|---------|------|---------|------|-------|---------------|--------|-------|")
    for r in sorted(unified_rows, key=lambda r: r["id"]):
        note = (r["notes"] or "").replace("|", "/")
        if len(note) > 140:
            note = note[:140] + "…"
        aliases = ", ".join(f"#{a}" for a in r["aliases"]) or "-"
        lines.append(
            f"| {r['id']} | {r['tool_tag']} | {aliases} | {r['date']} | {r['company']} | {r['role']} | {r['score']} | "
            f"{r['unified_score']} | {r['status']} | {note} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    co_rows, co_max = parse_career_ops()
    ajs_rows, ajs_max = parse_ai_job_search()
    collisions = find_id_collisions(co_rows, ajs_rows)
    clusters = cluster_duplicates(co_rows, ajs_rows)
    unified_rows = [build_unified_row(cl) for cl in clusters]
    renumber_plan = build_renumber_plan(clusters)
    stale = flag_stale(unified_rows)

    OUT_DIR.mkdir(exist_ok=True)

    if "--apply-renumber" in sys.argv:
        apply_renumber(renumber_plan)
        # re-parse and rebuild after mutation so the written tracker reflects reality
        ajs_rows, ajs_max = parse_ai_job_search()
        collisions = find_id_collisions(co_rows, ajs_rows)
        clusters = cluster_duplicates(co_rows, ajs_rows)
        unified_rows = [build_unified_row(cl) for cl in clusters]
        renumber_plan = build_renumber_plan(clusters)
        stale = flag_stale(unified_rows)

    write_markdown(unified_rows, collisions, renumber_plan, co_max, ajs_max, OUT_DIR / "unified-tracker.md")

    def status_counts(rows):
        counts = {}
        for r in rows:
            for part in r["status"].split(" / "):
                k = part.strip() or "(blank)"
                counts[k] = counts.get(k, 0) + 1
        return counts

    result = {
        "career_ops": {"total": len(co_rows), "max_id": co_max},
        "ai_job_search": {"total": len(ajs_rows), "max_id": ajs_max},
        "unified_total": len(unified_rows),
        "next_safe_id": max(co_max or 0, ajs_max or 0) + 1,
        "id_collisions": collisions,
        "renumber_plan": renumber_plan,
        "stale_applied": [{"id": r["id"], "company": r["company"], "role": r["role"]} for r in stale],
        "unapplied": sorted(
            [
                {
                    "id": r["id"],
                    "tool": r["tool_tag"],
                    "company": r["company"],
                    "role": r["role"],
                    "unified_score": r["unified_score"],
                }
                for r in unified_rows
                if r["unapplied"]
            ],
            key=lambda r: r["unified_score"] or 0,
            reverse=True,
        ),
        "by_status": status_counts(unified_rows),
        "unified_tracker_path": str((OUT_DIR / "unified-tracker.md").relative_to(ROOT)),
    }
    (OUT_DIR / "unified-tracker.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"career-ops: {result['career_ops']['total']} rows, max id {co_max}")
    print(f"ai-job-search: {result['ai_job_search']['total']} rows, max id {ajs_max}")
    print(f"unified: {result['unified_total']} jobs (one row per real job, one ID each) -> {result['unified_tracker_path']}")
    print(f"next safe shared ID: {result['next_safe_id']}")
    if collisions:
        print(f"⚠️  {len(collisions)} ID collision(s) -- genuinely different jobs sharing an ID, see unified-tracker.md")
    if renumber_plan:
        print(f"⚠️  {len(renumber_plan)} job(s) still numbered differently across tools -- run --apply-renumber to fix")
    if stale:
        print(f"{len(stale)} application(s) sitting in applied/drafted -- candidates for follow-up")
    print(f"{len(result['unapplied'])} unapplied role(s) -- see 'Unapplied roles' in unified-tracker.md")


if __name__ == "__main__":
    main()
