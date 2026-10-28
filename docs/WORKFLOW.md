# Operational Workflow

## Role activation
1. The user starts Alpha and provides project goals and constraints.
2. Alpha inspects available project artifacts and prepares the architecture and execution plan.
3. The user approves or requests changes to the plan.
4. Alpha sends Manager a complete approved mission and explicit scope/acceptance criteria.
5. Manager and Technical are started in independent chats using their role profiles and a task-specific handoff.
6. The user manually relays messages between chats; the named recipient of each message does not change.

## Approved-plan execution
1. Manager verifies the approval reference and reads the Project Graph, Information Index, and relevant task state.
2. Manager breaks the plan into scoped tasks with unique IDs, dependencies, acceptance criteria, and evidence requirements.
3. Manager may start tasks within the approved plan without per-task reapproval.
4. Manager may change technical details and ordering inside the approved scope, but cannot change global architecture, scope, Unit ownership, or acceptance criteria.
5. Manager sends a task assignment to Technical.
6. Technical performs `AUDIT -> APPLY -> VERIFY`, then sends an evidence-based report to Manager.
7. Manager reviews the report, requests correction if needed, updates/proposes reusable state, and reports progress or decisions needed to Alpha.
8. Alpha handles decisions outside Manager's authority and provides user-facing status.

## Communication boundaries
- Alpha communicates with the human user and Manager.
- Manager communicates with Alpha and assigned Technical Agents only. It must not ask the human for instructions or report directly to them.
- Technical reports to Manager. It may communicate with the human only for limited operational troubleshooting, such as obtaining actual terminal output.
- Unit Agent definitions and ownership remain with Alpha. Manager cannot create, remove, or redefine Unit Agent ownership.

## Avoid repeated context collection
Before requesting information, check whether a valid artifact already exists, whether its source/revision is known, whether the relevant files have changed, and whether the artifact covers the current task. Group independent inspection commands into one focused collection batch when practical.

## Terminal command conventions
- Begin each project terminal command step with `clear`, unless required diagnostic output must first be preserved.
- Use targeted `sed -i` edits only when exact current content is known.
- Use `cat > /path/to/file <<'EOF'` for full-file replacement only when appropriate.
- Inspect exact sections of large/sensitive files, including `web/app.py`, before editing.
- Use `grep`, `sed -n`, or equivalent inspection before targeted edits when content is uncertain.
- Keep each terminal step focused on one objective.
- Follow `AUDIT -> APPLY -> VERIFY`; report actual command output and tests, not assumptions.

## Blockers and handoffs
- Technical sends execution blockers to Manager.
- Manager sends decisions outside its authority to Alpha via `DECISION_REQUEST`.
- Alpha consults the user when project-level input or approval is needed.
- Record verified facts, assumptions, last verified checkpoint, remaining work, and next action in handoff records.
