# Operational Workflow

## New task

1. Alpha approves the goal, boundaries, dependencies, and acceptance criteria.
2. Manager checks the Graph and Information Index.
3. Manager creates a Task Contract and a task-specific context package.
4. Technical Agent inspects the current state and proceeds with the task.
5. User runs requested commands and returns actual output.
6. Technical Agent verifies each step and provides an Execution Report.
7. Manager reviews the report, updates state/index, and reports to Alpha.

## Avoiding repeated context collection

Before requesting project information, the Manager checks:
- whether a suitable artifact already exists;
- whether its source, scope, and observed revision are known;
- whether the relevant files have changed since collection;
- whether the artifact actually covers this task.

When information is missing, the Manager groups independent inspection commands into one collection batch where practical. A second batch is justified only by a newly discovered dependency, a contradiction, or an important unknown.

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
- Use `AUDIT → APPLY → VERIFY`.
- Commands and technical identifiers remain in English; explanations and reports are in Persian.
