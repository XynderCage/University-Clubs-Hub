| Quality driver | Requirement / scenario | Architectural obligation |
|---|---|---|
| **Performance** | Club search results must be returned within 3 seconds. | Search processing should be handled centrally by the application server, with efficient database access and indexes. The request path should avoid unnecessary processing. |
| **Reliability** | 100% of successfully submitted booking decisions must be persisted correctly. | The application server must own booking processing and use reliable database transactions so completed decisions are not partially stored or lost. |
| **Scalability** | System should support increasing users and requests. | Clients should remain lightweight while shared processing is performed on the server. The server tier should be capable of increased resources or replication when load grows. |
