# Pattern and technique decisions — Lab 09

| Design problem | Selected technique | Participants | Benefit | Cost / verification |
|---|---|---|---|---|
| Application logic must not depend on a database driver (FR1–FR3, ADR-001) | Repository port / dependency inversion | ClubService → ClubRepository ← SQLiteClubRepository | Persistence adapter replaceable; use case isolated | Extra interface; test service with fake repository and adapter with SQLite |
| BR1 must apply consistently to list and detail | Application service plus repository-enforced filter | HTTP handler → ClubService → ClubRepository | Shared validation and visibility rule at data boundary | Avoid inconsistent duplication; test unverified exclusion for both paths |
| Failure must have stable user outcome (QS2/QS5) | Explicit HTTP error mapping | Adapter exception → handler → stable 503 | No internal exception disclosure; retryable result | Maintain mapping; simulate DB unavailable |

## Rejected pattern
**Microservices** are rejected at this stage. No measured need for independent deployment/scaling exists. Multiple services add network failure, distributed consistency, monitoring and deployment overhead. Revisit only when evidence justifies it.

## Not selected
A broad event-driven architecture is not justified solely because FR10 mentions notifications. Notification delivery is outside the selected slice.
