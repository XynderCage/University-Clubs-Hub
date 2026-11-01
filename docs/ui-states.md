# UI alternative-state specification — Lab 10

| State | Trigger | Required behaviour |
|---|---|---|
| Initial | Page opens | Clear heading, persistent labels and search controls |
| Loading | Search submitted | Announce “Searching clubs…” via polite live region |
| Results | Matches returned | Count and readable result summaries |
| Empty | No matches | Explain no verified matches; retain criteria; suggest broadening |
| Validation | Criteria too long | Field-level message; preserve input; focus invalid field |
| Error | Server/database unavailable | Plain-language retry; preserve criteria; no stack trace |
| Unauthorised | Non-admin attempts protected write | 401/403; explain permission; no state change |
| Unavailable/stale | Data source unavailable or record no longer public | Do not expose stale/private data; provide return-to-search |
| Detail not found | Unknown/unverified ID | Generic not-found; do not disclose unverified record existence |

Demonstrator implements initial/loading/results/empty/error and service-side length validation. Authentication, role denial and stale-record UI need implementation in administrative extension.
