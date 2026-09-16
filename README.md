# SE-Labs-PES1UG24CS593

Software Engineering laboratory deliverables for **PES1UG24CS593**.

## Project

- Problem Statement: 58
- Title: Digital Art Commission & Watermarking Portal
- Domain: Media, Events & Community
- Primary Actors: Client Buyer, Digital Artist
- Supporting Actor: Payment Gateway

## Labs

- [Lab 1](Lab1/README.md) — Requirements Engineering and UML Use-Case Modelling
- [Lab 2](Lab2/README.md) — Agile Backlog Creation and Sprint Simulation in Jira
- [Lab 3](Lab3/README.md) — Component Modelling and Architectural Pattern Selection

## Lab 2 summary

The Lab 1 functional requirements were scoped to a single epic, **Epic 1 — WIP Draft Upload & Watermark
Protection**, holding six user stories worth 34 story points on the Fibonacci scale.

Two sprints were simulated in Jira (28 Aug – 11 Sep, two weeks each): Sprint 1 committed and completed
19 points, Sprint 2 committed and completed 15. All 34 points were delivered and the epic closed with
an empty backlog.

## Lab 3 summary

Three architectural styles were compared against the Lab 1 requirements and the **Layered Architecture**
was selected. The system is modelled as seven components across Presentation, Business Logic and Data
Access layers, with nine named interfaces in provided/required notation and two external systems.

The decision rests on two properties of this scenario: FR-005 requires payment verification, entitlement
creation and download authorisation to agree at all times, which a single transaction boundary
guarantees and a distributed design does not; and FR-001 requires that no unwatermarked draft ever
reaches the buyer, which one enforced code path from upload to publication makes structural.
