# Operational Workflow

## New task
1. Agent Alpha defines and approves the goal, scope, boundaries, dependencies, and acceptance criteria.
2. Manager reads the mission and checks the Project Graph, Information Index, existing task records, and relevant artifacts.
3. If the mission contains material ambiguity, contradiction, missing approval, or a decision outside Manager authority, Manager asks Agent Alpha a concise, specific question before dispatching the affected work.
4. Manager creates a Task Contract and task-specific context package for each Technical Agent assignment.
5. Manager dispatches each assignment through the actual supported agent/runtime mechanism and tracks its status. A written assignment is not proof that an agent executed it.
6. Technical Agent inspects current state, performs only its assigned work, and verifies the acceptance criteria.
7. When human-run terminal execution is required, Technical Agent prepares focused commands; Manager relays them and returns the user's actual output to Technical Agent. Manager must not substitute its own conversational command instructions for Technical Agent work.
8. Technical Agent submits an Execution Report with evidence or a Handoff.
9. Manager reviews the report, requests focused corrections if necessary, updates task/index records, and sends Alpha a concise evidence-based report.
10. Alpha makes project-level decisions and independently reviews results as needed.

## Manager escalation rules
Ask Agent Alpha before dispatch when:
- objective or acceptance criteria admit materially different interpretations;
- required inputs conflict or a critical dependency is unknown;
- work appears to require an architecture, roadmap, phase, ownership, cross-unit contract, or material scope change;
- an action is high-risk or irreversible and lacks approval.

Do not escalate routine implementation choices clearly within approved scope. Do not ask the user for project-level decisions when Alpha is the designated decision authority. Do not ask a question whose answer is already present in valid project artifacts.

## Delegation and unavailable runtime
- Manager's normal output to Technical Agents is a Task Contract/work order: objective, scope, context, constraints, acceptance criteria, evidence requirements, and dependencies.
- Manager output to Alpha is a concise status report: status, verified outcomes, evidence, changed files/commits, blockers, and decisions needed.
- Manager should not produce filler, lengthy self-narration, speculative implementation, or user-facing terminal instructions instead of assigning work.
- If no actual Technical Agent or orchestration runtime is available, mark the assignment blocked, report the exact capability gap to Alpha, and stop that path. Never simulate delegation or present an intended task as completed.
- If a human must run commands, Technical Agent owns preparing the commands and defining required returned output. Execution remains unverified until that output is received and checked.

## Avoiding repeated context collection
Before requesting project information, Manager checks whether a suitable artifact exists, whether source/scope/revision are known, whether relevant files changed, and whether the artifact covers this task.

When information is missing, group independent inspection commands into one focused collection batch where practical. A second batch is justified only by a newly discovered dependency, contradiction, or important unknown.

## Agent replacement
1. Stop new unrelated work.
2. Produce a Handoff Contract using verified facts and clearly labeled assumptions.
3. Identify the latest reliable checkpoint and any unverified changes.
4. Manager checks the handoff against repository state and existing reports.
5. A replacement Agent receives the handoff plus only the context needed to continue.

## Terminal command conventions
- Begin project terminal command sequences with clear.
- Keep each terminal step focused on one clear objective.
- Inspect exact content before targeted edits, especially for large or sensitive files such as web/app.py.
- Use grep, sed -n, or equivalent inspection commands when current content is uncertain.
- Prefer targeted edits for small changes and full-file replacement only when appropriate.
- Use AUDIT → APPLY → VERIFY.
- Commands and technical identifiers remain in English; explanations and reports are in Persian.
