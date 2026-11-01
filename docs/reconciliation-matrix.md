# Phase 2 reconciliation matrix — Lab 11

| Requirement/model | Design | Implementation | Test/evidence | Status |
|---|---|---|---|---|
| FR1 verified club listing | API contract/data model | `GET /api/clubs` | empty-search verified-only test | Implemented |
| FR2 search by name/category/keyword | UC-01/API contract | service + SQLite adapter | match/category tests | Implemented; performance unmeasured |
| FR3 club information | API detail route/UI | contact/description in result; detail API | verified detail test | Partial; dedicated detail page absent |
| BR1 public verified-only | integrity/ADR-002 | `verified=1` list/detail | unverified exclusion tests | Implemented/tested |
| QS1 ≤3 sec | ADR-001 | indexed SQLite query | timed benchmark pending | Not verified |
| QS3 90% within 2 min | user profile/wireframe | search UI | 3-person study pending | Not verified |
| QS4 reject unauthorized writes | security scenario | no write endpoints | authorization tests pending | Not implemented |
| FR5–FR7 administration/booking | CRC/domain/business rules | absent | tests absent | Deferred |
| BR3 no double-booking | transaction design | no booking schema/service | concurrency test pending | Designed only |
| QS2 99% availability | ADR-001 | local single-process demo | monitoring/failure test pending | Not verified |

Do not edit Phase 1 models to hide differences. Record the deliberately narrow implementation scope and preserve unimplemented requirements as gaps.
