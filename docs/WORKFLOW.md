# Operational Workflow

## Three-chat startup

1. In the first conversation, ask the new Agent to inspect and activate `agent-management-system`.
2. The Agent reads `docs/CHAT_BOOTSTRAP.md`, the three role profiles, and relevant project state from GitHub.
3. It provides a very short, bullet-point system summary based only on files it actually read.
4. It asks the user to confirm activation as Agent Alpha and waits for explicit confirmation.
5. In the second conversation, the user explicitly activates Agent Manager and supplies Alpha's approved mission.
6. In the third conversation, the user explicitly activates Technical Agent and supplies the Manager's Task Contract and focused context package.
7. Each conversation follows only its role profile. GitHub is the shared file reference; chat histories are not shared automatically.

## New task

1. Alpha approves the goal, boundaries, dependencies, and acceptance criteria.
2. Manager checks the Graph and Information Index.
3. Manager creates a Task Contract and a task-specific context package.
4. Technical Agent inspects the current state and proceeds with the task.
5. User runs requested commands and returns actual output.
6. Technical Agent verifies each step and provides an Execution Report.
7. Manager reviews the report, updates reusable records or proposes changes to the canonical state, and reports to Alpha.
8. Alpha updates global priorities and issues the next mission.

## Avoiding repeated context collection

Before requesting project information, the Manager checks:
- whether a suitable artifact already exists;
- whether its source, scope, and observed revision are known;
- whether the relevant files have changed since collection;
- whether the artifact actually covers this task.

When information is missing, the Manager groups independent inspection commands into one collection batch where practical. A second batch is justified only by a newly discovered dependency, contradiction, or important unknown.

## Agent replacement

If an Agent cannot continue:
1. Stop new unrelated work.
2. Produce a Handoff Contract using verified facts and clearly labeled assumptions.
3. Identify the latest reliable checkpoint and any unverified changes.
4. The Manager checks the handoff against repository state and existing reports.
5. A replacement Agent receives the handoff plus only the context needed to continue.

## Terminal command conventions

- Begin project terminal command sequences with `clear`.
- Keep each terminal step focused on one clear objective.
- Inspect exact content before targeted edits, especially for large or sensitive files such as `web/app.py`.
- Use `grep`, `sed -n`, or equivalent inspection commands when current content is uncertain.
- Prefer targeted edits for small changes and full-file replacement only when appropriate.
- Use `AUDIT -> APPLY -> VERIFY`.
- Commands and technical identifiers remain in English; explanations and reports are in Persian.
