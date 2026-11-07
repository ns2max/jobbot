#!/usr/bin/env python3
"""University Affairs jobs (universityaffairs.ca/search-jobs/) -> JSON for career-ops local-parser.

The page renders all current postings (~500) server-side in one request; the keyword
parameter is ignored, so filter locally on the title (titles start with the discipline).
Prints [{title,url,company,location}] to stdout. Zero tokens, plain HTTP.
"""
import html, json, re, sys, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
      "Accept-Language": "en-CA"}
URL = "https://universityaffairs.ca/search-jobs/"
RELEVANT = re.compile(
    r"machine learning|artificial intell|\bAI\b|computer|computing|data science|electrical|signal|audio|"
    r"music tech|computer music|music information|sound|acoustic|speech|robot|software|embedded|sensor|cyber|digital|intelligen|neural|human.computer|"
    r"information (tech|science)|mechatronic|supercomput|postdoc|research chair|\bCRC\b|"
    r"statistic", re.I)
# faculty-wide admin / unrelated to the profile
EXCLUDE = re.compile(r"president|vice-chancellor|dean\b|provost|librarian|registrar|coach|nursing|veterinar|"
                     r"mechanical|civil|chemical|biolog|neuroscience|epidemiolog|constitutional|law\b|planning|"
                     r"indigenous|library and information|bioprocess|geograph|urban|biomechanic|muscle|pharmac|kinesiolog|"
                     r"philosoph|german|aging|droit|gouvernance|governance|world of work|monde du travail|"
                     r"intelligence and national security|durabilit|protein", re.I)

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


def main():
    req = urllib.request.Request(URL, headers=UA)
    page = urllib.request.urlopen(req, timeout=45).read().decode("utf8", "ignore")
    out = []
    for blk in re.findall(r'<div class="job__block[^"]*".*?(?=<div class="job__block[ "]|$)', page, re.S):
        blk = re.sub(r"<svg.*?</svg>", "", blk, flags=re.S)
        href = re.search(r'href="([^"]*job_id=(\d+))"', blk)
        if not href:
            continue
        cells = [re.sub(r"\s+", " ", html.unescape(c)).strip()
                 for c in re.findall(r">\s*([^<>]+?)\s*<", blk) if c.strip()]
        # cells: title, institution, 'Location', province, 'Posting date', date
        if len(cells) < 4:
            continue
        title, inst = cells[0], cells[1]
        loc = cells[cells.index("Location") + 1] if "Location" in cells else "Canada"
        if not RELEVANT.search(title) or EXCLUDE.search(title):
            continue
        title, loc = norm(title, loc)
        out.append({"title": title, "url": f"{URL}?job_id={href[2]}", "company": inst, "location": loc})
    json.dump(out, sys.stdout)


if __name__ == "__main__":
    main()
