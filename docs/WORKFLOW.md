# Operational Workflow

## New task
1. Agent Alpha defines and approves the goal, scope, boundaries, dependencies, acceptance criteria, and final deliverables.
2. Manager reads the mission and checks the Project Graph, Information Index, task records, and relevant artifacts.
3. Manager resolves routine details within scope. If material ambiguity or a decision beyond Manager authority remains, Manager asks Alpha one concise, specific question before dispatching the affected work.
4. Manager creates a Task Contract and task-specific context package for each Technical Agent assignment.
5. Manager uses the actual supported agent/runtime mechanism when available. If it is unavailable, Manager still prepares complete, copy-ready Work Orders for the user to relay; these must be labeled prepared, not dispatched.
6. Each Work Order states the objective, exact scope, relevant files and branch, ordered steps, constraints, acceptance criteria, evidence to return, and reporting destination.
7. Technical Agent inspects current state, performs only assigned work, and verifies acceptance criteria.
8. When human-run terminal execution is required, Technical Agent prepares the focused commands and identifies the exact output to return. Manager relays the commands/output between the user and Technical Agent. Proposed commands are not executed commands.
9. Technical Agent submits an Execution Report with evidence or a Handoff.
10. Manager reviews evidence, requests focused corrections when needed, updates task/index records, and sends Alpha a concise report with verified outcomes and the exact next action.
11. Alpha issues an explicit pass, fail, or inconclusive decision and states the next phase/action.

## Actionable response contract
Every operational response from Alpha, Manager, and Technical Agents must specify:
- current status;
- work actually completed and evidence;
- work remaining;
- next responsible role/person;
- exact next action;
- expected output and acceptance criteria;
- real blockers and the specific step they prevent.

Do not use vague conclusions, filler, open-ended offers, or speculative success claims. Do not merely announce a limitation if useful in-scope work can still be completed. Separate prepared, assigned, attempted, executed, and verified states.

## Manager delegation and dual-path work
- Manager delegates technical work and returns operational Work Orders, not a long explanation of what a Technical Agent might do.
- When the mission requires different execution routes, Manager must create one separate copy-ready Work Order per route (for example, terminal-based repair and direct GitHub repair), with independent scope, steps, acceptance criteria, and evidence.
- If actual autonomous dispatch is unavailable, Manager states that honestly but still prepares Work Orders for user relay. Only the actual dispatch/execution step is blocked; Work Order preparation is not.
- A written Work Order is not proof that an agent executed it. Never simulate agent activity or claim a test passed without actual output.
- Do not ask the user to make project-level decisions assigned to Alpha. Escalate only decisions outside the approved scope.

## Avoiding repeated context collection
Before requesting project information, Manager checks whether a suitable artifact exists, whether its source/scope/revision are known, whether relevant files changed, and whether the artifact covers this task.

When information is missing, group independent inspection commands into one focused collection batch where practical. A second batch is justified only by a newly discovered dependency, contradiction, or important unknown.

## Agent replacement
1. Stop new unrelated work.
2. Produce a Handoff Contract using verified facts and clearly labeled assumptions.
3. Identify the latest reliable checkpoint and any unverified changes.
4. Manager checks the handoff against repository state and existing reports.
5. A replacement Agent receives the handoff plus only the context needed to continue.

## Terminal command conventions
- Begin project terminal command sequences with `clear`.
- Keep each terminal step focused on one clear objective.
- Inspect exact content before targeted edits, especially for large or sensitive files such as `web/app.py`.
- Use `grep`, `sed -n`, or equivalent inspection commands when current content is uncertain.
- Prefer targeted edits for small changes and full-file replacement only when appropriate.
- Use `AUDIT → APPLY → VERIFY`.
- Commands and technical identifiers remain in English; explanations and reports are in Persian.
