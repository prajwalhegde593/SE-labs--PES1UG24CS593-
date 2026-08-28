# Lab 2 — Agile Backlog Creation and Sprint Simulation in Jira

Continuation of Lab 1. Scoped as instructed to a single epic with six user stories, prioritised,
estimated with Fibonacci story points, and run through two simulated one-week sprints.

## Deliverables

1. `Lab2_Backlog_Epics_Stories.docx`
   - One Epic mapped to the Lab 1 functional requirements
   - Six User Stories in "As a / I want / So that" form
   - Priority, Fibonacci story points and FR/UC traceability for every story
   - PDF copy: `Lab2_Backlog_Epics_Stories.pdf`

2. `Lab2_Sprint_Plan_and_Reflection.docx`
   - Sprint 1 and Sprint 2 goals, contents and end-of-sprint status
   - Velocity table, Planning Poker record, burndown analysis
   - Answers to the four reflection questions
   - PDF copy: `Lab2_Sprint_Plan_and_Reflection.pdf`

3. `Lab2_Burndown_Charts.pdf`
   - Guideline vs remaining values for both sprints
   - PNG copy: `Lab2_Burndown_Charts.png`

4. `Lab2_Jira_Import.csv`
   - Bulk-import file creating the epic and all six stories with points, priorities and parent links

5. `screenshots/`
   - Jira evidence: backlog with the epic, story point assignments, active sprint board, burndown charts

## Epic

**Epic 1 — WIP Draft Upload & Watermark Protection** (34 story points, 6 stories)
Traces to FR-001, FR-003 and FR-004; covers UC-03 Upload WIP Draft, UC-04 Apply Watermark and
UC-05 Review WIP & Provide Feedback.

| Story | Priority | SP | Sprint |
|---|---|---|---|
| 1.1 Upload a versioned WIP draft | Highest | 8 | Sprint 1 |
| 1.2 Apply a diagonal watermark to every draft | Highest | 8 | Sprint 1 |
| 1.3 Notify the buyer when a draft is ready | Medium | 3 | Sprint 1 |
| 1.4 Keep originals in private storage | Highest | 5 | Sprint 2 |
| 1.5 Fail closed if watermarking fails | High | 5 | Sprint 2 |
| 1.6 Review a watermarked draft | High | 5 | Sprint 2 |

## Sprint outcome

| Sprint | Duration | Committed | Completed |
|---|---|---|---|
| Sprint 1 | 2 weeks | 19 | 19 |
| Sprint 2 | 2 weeks | 15 | 15 |

All 34 story points were delivered across the two sprints; the epic closed with an empty backlog.
Both sprints ran 28 Aug – 11 Sep and were simulated in a single session, so the burndown lines drop
on the first day while the guideline slopes across the full timebox.

## Running it in Jira

1. Create a **Company-managed Scrum** project named `Digital Art Commission` with key **DIG**.
2. Import the backlog: Settings → System → External system import → CSV → upload `Lab2_Jira_Import.csv`.
   Map `Issue Id` → Issue Id, `Issue Type` → Issue Type, `Summary` → Summary, `Description` → Description,
   `Priority` → Priority, `Story Points` → Story Points, `Parent` → Parent, `Labels` → Labels.
   Leave `Sprint` unmapped and drag stories into sprints by hand. Mapping `Issue Id` is mandatory,
   otherwise the epic-to-story parent links are not created.
   With only seven rows, creating the epic and stories by hand is also perfectly quick.
3. **Sprint 1**: drag stories 1.1, 1.2 and 1.3 into the sprint (19 points), start it, move every card
   To Do → In Progress → Done, and complete the sprint.
4. **Sprint 2**: create a sprint with stories 1.4, 1.5 and 1.6 (15 points), start it, move all three to
   Done, and complete the sprint. The epic closes with an empty backlog.
5. **Burndown**: Reports → Burndown Chart, estimation statistic set to Story Points, for each sprint.

## Screenshots to capture

- `01-backlog-epic.jpeg` — backlog with the epic panel open, the epic and its six stories visible
- `02-story-points.jpeg` — story point badges and priorities across the epic's child work items
- `03-sprint-board.jpeg` — active sprint board with cards across To Do, In Progress and Done
- `04-burndown-sprint2.jpeg` — burndown for Sprint 2

A Sprint 1 burndown screenshot is still worth adding: Reports → Burndown Chart → select DAC Sprint 1,
estimation statistic Story Points.

## Project Details

- SRN: PES1UG24CS593
- Problem Statement: 58
- Project: Digital Art Commission & Watermarking Portal
- Domain: Media, Events & Community
- Target Actors: Client Buyer, Digital Artist, Payment Gateway
