# Mode: tracker — Application Tracker

Read and display `data/applications.md`.

**Tracker format:**
```markdown
| # | Date | Company | Role | Score | Status | PDF | Report |
```

Canonical statuses: `Evaluated` → `Applied` → `Responded` → `Interview` → `Offer` / `Rejected` / `Discarded` / `SKIP`

- `Applied` = candidate submitted application
- `Responded` = recruiter/company contacted and candidate replied (inbound)

If the user asks to update a status, edit the corresponding row in applications.md.

Show statistics:
- Total applications
- By status
- Average score
- % with PDF generated
- % with report generated
