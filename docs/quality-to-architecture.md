| Quality requirement | Architecture element | Architectural response | Evidence |
|---|---|---|---|
| Performance | Client–Server boundary, Search Component, Database | Search performed centrally; database queries/indexes optimized | Search response ≤ 3 seconds |
| Reliability | Venue Request Component, Application Server, Database | Server controls booking decisions and uses reliable persistence | All successful decisions found correctly in DB |
| Scalability | Application Server | Server resources/instances may be increased as demand grows | Load test and resource-utilization results |
