# Framework and dependency-management decision — Lab 09

## Decision for demonstrator
Use Python 3.10+ standard-library HTTP server and SQLite. No third-party runtime dependency. This minimizes lab setup friction and exposes the Client–Server, application-service and persistence boundaries.

## Production direction
Before production, evaluate Django (integrated authentication, ORM, migrations, admin) or FastAPI (typed API contracts and OpenAPI) against team skills and hosting constraints. Neither is established as the original project's selected framework.

## Trade-offs
- Chosen now: no package installation; transparent SQL; simple reproducibility.
- Accepted costs: limited routing, authentication middleware, migration tooling, hardening and operations.
- Not production-ready: do not expose publicly or use real personal data.
- Dependency management: record Python version; isolate future packages in a virtual environment; pin tested versions in `requirements.txt`; review licenses and security advisories.

## Alternatives
Django provides integrated administration/auth but more framework configuration. FastAPI provides API typing/docs but requires dependencies and a persistence/migration decision. Node/Express is viable but no supplied evidence establishes team advantage.

The decision is limited to this demonstrator.
