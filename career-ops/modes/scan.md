# Mode: scan — Portal Scanner

Scans configured job portals, filters by title relevance, and adds new offers to the pipeline for later evaluation.

> **Note (v1.6+):** The default scanner (`scan.mjs` / `npm run scan`) is **zero-token** and uses structured sources: company-configured local parsers and public Greenhouse, Ashby, and Lever APIs. The Playwright/WebSearch levels described below are the **agent** flow (executed by Claude), not what `scan.mjs` does. If a company has no local parser or Greenhouse/Ashby/Lever API, `scan.mjs` will skip it; for those cases, the agent must manually run Level 1 (Playwright) or Level 3 (WebSearch).
>
> **Rule (v1.8+):** If a company's local parser succeeds at Level 0, the agent **must not** repeat that company via Playwright (Level 1) or API (Level 2). At Level 3, general queries remain active, but results from companies already covered by a parser are discarded. See [Rule: successful local parser](#rule-successful-local-parser--no-redundant-scraping).

## Recommended execution

Run as a subagent to avoid consuming main context:

```
Agent(
    subagent_type="general-purpose",
    prompt="[contents of this file + specific data]",
    run_in_background=True
)
```

## Configuration

Read `portals.yml` which contains:
- `search_queries`: WebSearch queries with `site:` filters per portal (broad discovery)
- `tracked_companies`: Specific companies with `careers_url` for direct navigation
- `tracked_companies[].parser`: Optional local parser for SSR or stable HTML pages
- `title_filter`: Positive/negative/seniority_boost keywords for title filtering

## Discovery strategy (4 levels)

### Level 0 — Local parser (CHEAPEST)

**For each company in `tracked_companies` with `parser:` configured:** run the local parser defined in `portals.yml`. This level is ideal when the careers page uses SSR or stable HTML and a local JavaScript, Python, or other runtime script already exists to extract jobs without agent help.

Recommended contract:

```yaml
- name: Example Company
  careers_url: https://example.com/careers
  scan_method: local_parser
  parser:
    command: node
    script: scripts/parsers/example-company-jobs.js
    format: jobs-json-v1
  enabled: true
```

The parser is typically company-specific and already knows the URL, selectors, and pagination. `args` is optional.

The parser must print JSON to stdout:

Array format:
```json
[
  { "title": "Senior AI Engineer", "url": "https://example.com/jobs/123", "location": "Remote" }
]
```

Object with `jobs`:
```json
{ "jobs": [{ "title": "Senior AI Engineer", "url": "https://example.com/jobs/123", "location": "Remote" }] }
```

Object with `results`:
```json
{ "results": [{ "title": "Senior AI Engineer", "url": "https://example.com/jobs/123", "location": "Remote" }] }
```

`company` is optional; if absent, `scan.mjs` uses the name from `tracked_companies`.

Save parser audit output to `data/parser-output/{company}/` (JSON in `.gitignore`; `.gitkeep` stays in git).

### Rule: successful local parser — no redundant scraping

Maintain a **`local_parser_ok`** set in memory: company names where Level 0 succeeded (script ran without fatal error, stdout was valid JSON, no timeout/crash).

| Level | If company is in `local_parser_ok` |
|-------|-------------------------------------|
| **1 — Playwright** | **Skip** — no `browser_navigate` to its `careers_url` |
| **2 — API** | **Skip** — no WebFetch of its `api:` |
| **3 — WebSearch** | Run general queries; **discard** hits whose normalized company matches `local_parser_ok` |

**Exceptions:** If parser failed → company is not in `local_parser_ok`; Levels 1 and 2 apply normally. Level 3 general queries (cross-portal `site:` queries) remain active — they discover new companies. Don't create dedicated `search_queries` for a company that has an active local parser.

**Recommended:** run `node scan.mjs` (or `npm run scan`) at the start of the agent workflow. This covers all parsers + APIs in a single zero-token step and returns which companies used `local-parser` successfully.

### Level 1 — Direct Playwright (PRIMARY)

**For each company in `tracked_companies` not in `local_parser_ok`:** navigate to its `careers_url` with Playwright (`browser_navigate` + `browser_snapshot`), read ALL visible job listings, and extract title + URL for each. Most reliable because:
- Sees the page in real time (not cached Google results)
- Works with SPAs (Ashby, Lever, Workday)
- Detects new offers instantly
- Does not depend on Google indexing

**Every company MUST have `careers_url` in portals.yml.** If missing, find it once, save it, and use it in future scans.

### Level 2 — ATS APIs / Feeds (COMPLEMENTARY)

For companies with a public API or structured feed **not in `local_parser_ok`**, use the JSON/XML response as a fast complement to Level 1.

**Supported providers:**
- **Greenhouse**: `https://boards-api.greenhouse.io/v1/boards/{company}/jobs`
- **Ashby**: `https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams`
- **BambooHR**: list `https://{company}.bamboohr.com/careers/list`; detail `https://{company}.bamboohr.com/careers/{id}/detail`
- **Lever**: `https://api.lever.co/v0/postings/{company}?mode=json`
- **Teamtailor**: `https://{company}.teamtailor.com/jobs.rss`
- **Workday**: `https://{company}.{shard}.myworkdayjobs.com/wday/cxs/{company}/{site}/jobs`

**Parsing conventions:**
- `greenhouse`: `jobs[]` → `title`, `absolute_url`
- `ashby`: GraphQL `ApiJobBoardWithTeams` with `organizationHostedJobsPageName={company}` → `jobBoard.jobPostings[]` (`title`, `id`)
- `bamboohr`: list `result[]` → `jobOpeningName`, `id`; GET detail for full JD; use `jobOpeningShareUrl` as public URL
- `lever`: root array `[]` → `text`, `hostedUrl`
- `teamtailor`: RSS items → `title`, `link`
- `workday`: `jobPostings[]` → `title`, `externalPath`

### Level 3 — WebSearch queries (BROAD DISCOVERY)

`search_queries` with `site:` filters cover portals cross-sectionally (all Ashby, all Greenhouse, etc.). Useful for discovering NEW companies not yet in `tracked_companies`, but results may be stale. After filtering hits from companies in `local_parser_ok`, remaining results are deduped with Levels 0–2.

**Execution priority:**
1. Level 0: Local parser → companies with `parser:` configured; build `local_parser_ok`
2. Level 1: Playwright → `tracked_companies` with `careers_url`, **except** `local_parser_ok`
3. Level 2: API → `tracked_companies` with `api:`, **except** `local_parser_ok`
4. Level 3: WebSearch → all `search_queries` with `enabled: true`; discard hits from `local_parser_ok` companies

Levels are additive — run in order, results merged and deduped.

## Workflow

1. **Read config**: `portals.yml`
2. **Read history**: `data/scan-history.tsv` → already-seen URLs
3. **Read dedup sources**: `data/applications.md` + `data/pipeline.md`

3.5. **Level 0 — Local parser** (`scan.mjs`, zero-token):
   Init `local_parser_ok = []`. Prefer running `node scan.mjs` once to cover all parsers + APIs.
   For each company in `tracked_companies` with `enabled: true` and existing parser script:
   a. Run `parser.command` with `parser.script` + `parser.args`
   b. Expand `{careers_url}` and `{company}` placeholders in args
   c. Read JSON from stdout
   d. Normalize each job to `{title, url, company, location}`
   e. Resolve relative URLs against `careers_url`
   f. If parser fails, log error, try ATS API fallback if available, continue (**don't** add to `local_parser_ok`)
   g. If parser succeeds, add `entry.name` to `local_parser_ok` and accumulate jobs

4. **Level 1 — Playwright scan** (parallel batches of 3–5):
   For each company in `tracked_companies` with `enabled: true`, `careers_url` defined, **not in `local_parser_ok`**:
   a. `browser_navigate` to `careers_url`
   b. `browser_snapshot` to read all job listings
   c. Navigate department sections if page has filters
   d. Extract `{title, url, company}` per listing
   e. Paginate if needed
   f. If `careers_url` fails (404, redirect), try `scan_query` fallback and note URL for update

5. **Level 2 — ATS APIs / feeds** (parallel):
   For each company in `tracked_companies` with `api:` defined, `enabled: true`, **not in `local_parser_ok`**:
   a. WebFetch the API/feed URL
   b. Use `api_provider` parser if defined; otherwise infer from domain
   c. For **Ashby**: POST with `operationName: ApiJobBoardWithTeams`, `variables.organizationHostedJobsPageName: {company}`
   d. For **BambooHR**: list → GET detail for each relevant item → extract full JD from `result.jobOpening`
   e. For **Workday**: POST `{"appliedFacets":{},"limit":20,"offset":0,"searchText":""}` and paginate
   f. Normalize to `{title, url, company}` and accumulate

6. **Level 3 — WebSearch queries** (parallel where possible):
   For each query in `search_queries` with `enabled: true`:
   a. Run WebSearch
   b. Extract `{title, url, company}` from each result
   c. **Discard** if normalized company matches `local_parser_ok`
   d. Accumulate remainder (dedup with Levels 0+1+2)

6. **Filter by title** using `title_filter` from `portals.yml`:
   - At least 1 `positive` keyword must match title (case-insensitive)
   - 0 `negative` keywords may match

6b. **Filter by location (optional)** using `location_filter` from `portals.yml`:
   - Block keywords take precedence over allow
   - Empty location on a listing → passes
   - Empty `allow` list → passes
   - Persist location as 7th column in `scan-history.tsv`

7. **Deduplicate** against 3 sources:
   - `scan-history.tsv` → exact URL already seen
   - `applications.md` → normalized company + role already evaluated
   - `pipeline.md` → exact URL already pending or processed

7.5. **Verify liveness of Level 3 WebSearch results** — BEFORE adding to pipeline:
   Level 3 results may be stale (Google caches weeks/months). For each new Level 3 URL (sequential — **NEVER Playwright in parallel**):
   a. `browser_navigate` to the URL
   b. `browser_snapshot`
   c. Classify:
      - **Active**: job title visible + role description + Apply/Submit control in main content
      - **Expired**: URL contains `?error=true`; page says "job no longer available" / "position has been filled" / "this job has expired"; or only navbar/footer visible (content < ~300 chars)
   d. If expired: record in `scan-history.tsv` with status `skipped_expired` and discard
   e. If active: continue to step 8

   Don't abort the full scan on one failure — mark as `skipped_expired` and continue.

8. **For each new verified offer that passes filters**:
   a. Add to `pipeline.md` "Pending" section: `- [ ] {url} | {company} | {title}`
   b. Record in `scan-history.tsv`: `{url}\t{date}\t{query_name}\t{title}\t{company}\tadded`

9. **Title-filtered offers**: record in `scan-history.tsv` with status `skipped_title`
10. **Duplicate offers**: record with status `skipped_dup`
11. **Expired offers (Level 3)**: record with status `skipped_expired`

## Title and company extraction from WebSearch results

WebSearch results come in format: `"Job Title @ Company"` or `"Job Title | Company"` or `"Job Title — Company"`.

Extraction patterns by portal:
- **Ashby**: `"Senior AI PM (Remote) @ EverAI"` → title: `Senior AI PM`, company: `EverAI`
- **Greenhouse**: `"AI Engineer at Anthropic"` → title: `AI Engineer`, company: `Anthropic`
- **Lever**: `"Product Manager - AI @ Temporal"` → title: `Product Manager - AI`, company: `Temporal`

Generic regex: `(.+?)(?:\s*[@|—–-]\s*|\s+at\s+)(.+?)$`

## Private URLs

If a URL is not publicly accessible:
1. Save the JD to `jds/{company}-{role-slug}.md`
2. Add to pipeline.md as: `- [ ] local:jds/{company}-{role-slug}.md | {company} | {title}`

## Scan History

`data/scan-history.tsv` tracks ALL seen URLs:

```
url	first_seen	portal	title	company	status
https://...	2026-02-10	Ashby — AI PM	PM AI	Acme	added
https://...	2026-02-10	Greenhouse — SA	Junior Dev	BigCo	skipped_title
https://...	2026-02-10	Ashby — AI PM	SA AI	OldCo	skipped_dup
https://...	2026-02-10	WebSearch — AI PM	PM AI	ClosedCo	skipped_expired
```

## Output summary

```
Portal Scan — {YYYY-MM-DD}
━━━━━━━━━━━━━━━━━━━━━━━━━━
Queries run: N
Offers found: N total
Filtered by title: N relevant
Duplicates: N (already evaluated or in pipeline)
Expired discarded: N (dead links, Level 3)
New added to pipeline.md: N

  + {company} | {title} | {query_name}
  ...

→ Run /career-ops pipeline to evaluate the new offers.
```

## careers_url management

**Rule: always use the company's own careers page URL; fall back to the ATS endpoint only if no corporate page exists.**

| ✅ Correct (corporate) | ❌ Avoid as first choice (direct ATS) |
|---|---|
| `https://careers.mastercard.com` | `https://mastercard.wd1.myworkdayjobs.com` |
| `https://openai.com/careers` | `https://job-boards.greenhouse.io/openai` |
| `https://stripe.com/jobs` | `https://jobs.lever.co/stripe` |

**Known patterns by platform:**
- **Ashby:** `https://jobs.ashbyhq.com/{slug}`
- **Greenhouse:** `https://job-boards.greenhouse.io/{slug}`
- **Lever:** `https://jobs.lever.co/{slug}`
- **BambooHR:** `https://{company}.bamboohr.com/careers/list`
- **Teamtailor:** `https://{company}.teamtailor.com/jobs`
- **Workday:** `https://{company}.{shard}.myworkdayjobs.com/{site}`

**If `careers_url` is missing:** search `"{company}" careers jobs`, navigate with Playwright to confirm, then save to portals.yml.

**If `careers_url` returns 404 or redirect:** note in output summary, try `scan_query` fallback, mark for manual update.

## portals.yml maintenance

- Always save `careers_url` when adding a new company
- Add new queries as new portals or roles are discovered
- Set `enabled: false` on queries that generate too much noise
- Adjust filter keywords as target roles evolve
- Add companies to `tracked_companies` when worth tracking closely
- Verify `careers_url` periodically — companies change ATS platforms
