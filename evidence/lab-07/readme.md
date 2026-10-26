# Lab 07 Evidence

## Project
University Clubs Hub

## Selected Architecture
Client–Server

## Quality Drivers
- Performance
- Reliability
- Scalability

## Alternatives Considered
- MVC
- Microservices

## Evidence Produced

- docs/architecture-options.md
- docs/quality-to-architecture.md
- models/component-architecture.*
- decisions/ADR-001-architecture.md

## Highest Architectural Risk

The central application server or database may become a bottleneck as
user traffic and search volume increase.

## Evidence for Reconsideration

The architecture will be reconsidered if:

- search cannot consistently meet the 3-second response target;
- load testing identifies the server as a bottleneck;
- one capability requires substantially different scaling; or
- independent deployment becomes necessary.
