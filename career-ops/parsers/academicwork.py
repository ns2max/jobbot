#!/usr/bin/env python3
"""CAUT AcademicWork (academicwork.ca) -> JSON for career-ops local-parser.

Server-rendered keyword search, no auth. Usage:
  python3 parsers/academicwork.py "machine learning" "audio" ...
Prints [{title,url,company,location}] to stdout. Zero tokens, plain HTTP.
"""
import html, json, re, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
      "Accept-Language": "en-CA"}
BASE = "https://www.academicwork.ca"
# search matches body text too, so re-check the title/employer snippet for relevance
RELEVANT = re.compile(
    r"machine learning|artificial intell|\bAI\b|computer (science|engineering)|computing|data science|"
    r"electrical|signal|audio|music tech|computer music|music information|sound|acoustic|speech|robot|software|embedded|sensor|cyber|digital|"
    r"intelligen|neural|human.computer|information (tech|science)|mechatronic|supercomput", re.I)
EXCLUDE = re.compile(r"president|vice-chancellor|dean\b|provost|librarian|registrar|coach|nursing|veterinar|"
                     r"mechanical|civil|chemical|biolog|neuroscience|epidemiolog|constitutional|law\b|planning|"
                     r"indigenous|library and information|bioprocess|geograph|urban|biomechanic|muscle|pharmac|"
                     r"kinesiolog|philosoph|german|aging|droit|gouvernance|governance|breeding|agricultur|"
                     r"intelligence and national security|protein|sunflower", re.I)

PROVINCES = {"Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
             "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island",
             "Quebec", "Saskatchewan", "Yukon", "Canada"}
TITLE_OK = re.compile(r"professor|faculty|lecturer|postdoc|research chair|chair|professeur|stage", re.I)


def norm(title, region):
    """Append ', Canada' to Canadian provinces (the scanner's location filter allows 'Canada') and tag
    titles that lack a title_filter keyword (e.g. 'Tenure-Track Position in AI for Health')."""
    if region in PROVINCES:
        region = f"{region}, Canada"
    if not TITLE_OK.search(title):
        title = f"Faculty position: {title}"
    return title, region


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25).read().decode("utf8", "ignore")


def parse(page):
    jobs = []
    for blk in re.split(r'(?=<a[^>]*href="https://www\.academicwork\.ca/jobs/)', page)[1:]:
        m = re.match(r'<a[^>]*href="(https://www\.academicwork\.ca/jobs/[^"]+)"[^>]*>(.*?)</a>', blk, re.S)
        if not m:
            continue
        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m[2]))).strip()
        head = blk[:2500]
        emp = re.search(r'/institution/[^"]+"[^>]*>(.*?)</a>', head, re.S)
        reg = re.search(r"Region:\s*<strong>(.*?)</strong>", head, re.S)
        region = html.unescape(reg[1]).strip() if reg else "Canada"
        title, region = norm(title, region)
        desc = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", head[m.end():])))
        jobs.append({
            "_text": title + " " + desc[:400],
            "title": title,
            "url": m[1],
            "company": html.unescape(re.sub(r"<[^>]+>", "", emp[1])).strip() if emp else "",
            "location": region,
        })
    return jobs


def main(queries):
    seen, out = set(), []
    for q in queries:
        for p in range(1, 6):
            page = get(f"{BASE}/search?" + urllib.parse.urlencode({"search": q, "page": p}))
            items = parse(page)
            for j in items:
                if j["url"] in seen:
                    continue
                seen.add(j["url"])
                if RELEVANT.search(j.pop("_text")) and not EXCLUDE.search(j["title"]):
                    out.append(j)
            if len(items) < 10:
                break
            time.sleep(0.4)
    json.dump(out, sys.stdout)


if __name__ == "__main__":
    main(sys.argv[1:] or ["machine learning", "artificial intelligence"])
