# Architecture

## 1. Purpose
Agent Management System (AMS) coordinates AI agents without treating conversation history as the canonical project state. It starts as a file-based, Git-versioned system. Automated model orchestration, databases, dashboards, and direct server execution are outside the initial implementation unless Agent Alpha explicitly approves a later architecture change.

## 2. Role hierarchy and authority

### Agent Alpha — project owner and decision authority
- Receives project goals, constraints, and decisions from the user.
- Owns project direction, high-level architecture, roadmap, phases, execution-unit boundaries, dependencies, shared contracts, and material scope changes.
- Approves missions and acceptance criteria for execution managers.
- Resolves questions escalated by Managers when a decision exceeds their authority.
- Reviews Manager reports and maintains concise project-level status.
- Normally does not implement code.

### Agent Manager — execution coordinator, not project architect
- Receives an approved mission from Alpha and coordinates delivery.
- Checks the Project Graph and Information Index, then prepares bounded Task Contracts and context packages.
- Assigns implementation, inspection, testing, and other technical work to available Technical Agents.
- Tracks dependencies, reviews Technical Agent evidence, requests focused corrections, and reports results to Alpha.
- Keeps assignments within the approved scope and maintains task/index records.
- Must not define or change architecture, project-wide design, roadmap, phases, ownership boundaries, cross-unit contracts, or material scope. These decisions require Agent Alpha's explicit approval.
- Must not replace delegation with conversational explanations or end-user terminal instructions. If a real Technical Agent/runtime is unavailable, report the assignment as blocked to Alpha; do not simulate execution or claim that an agent was used.
- If mission input is materially ambiguous, first inspect existing artifacts, then ask Agent Alpha a concise question before dispatching affected work. Manager does not resolve project-level ambiguity by guessing.

### Technical Agent — scoped executor
- Receives a bounded Task Contract from its assigned Manager.
- Inspects relevant state, performs focused analysis/implementation, and verifies acceptance criteria.
- Uses actual repository tools when available. If human-run terminal execution is required, prepares focused commands for Manager to relay and waits for actual output before claiming success.
- Reports files, diffs, commits, commands actually run, verification evidence, unresolved items, and status to Manager.
- Does not change architecture, expand scope, or take cross-unit decisions. Escalates uncertainty to Manager.

## 3. Communication and work flow
User ↔ Agent Alpha ↔ Agent Manager ↔ Technical Agent(s) ↔ Agent Manager ↔ Agent Alpha

In the initial release, the user may relay messages and run commands in a real terminal. This is a transport/execution constraint, not permission for Manager to bypass Technical Agents. When an agent runtime is unavailable, Manager reports the capability gap rather than pretending the assignment was executed.

## 4. Project Graph and Project Information Index
The Project Graph describes components, relationships, dependencies, ownership, and task location.

The Project Information Index records what project information has already been collected, where it is stored, what it covers, when it was observed, and whether it remains valid. It is a lightweight lookup/metadata layer and must not duplicate all source content.

Manager checks these artifacts before requesting context. Technical Agents collect only missing, task-relevant information and record reusable results through the agreed workflow.

## 5. Context package policy
- Reuse existing, still-valid artifacts first.
- Identify task-relevant files from the graph and task scope.
- Group independent inspection commands into one focused collection step when practical.
- Prefer targeted excerpts over full file dumps.
- Archives may be used for transfer, but archive contents should not automatically be pasted into model context.
- Request more information only for a material unknown, contradiction, or changed file.
- Do not repeat a request when the same valid output is already available.
- Record reusable results in the Index after successful collection.

## 6. State and lifecycle
Task states: draft, ready, in_progress, blocked, review, completed, cancelled.

A task is completed only when its acceptance criteria are supported by evidence. An agent's claim alone is not verification. Proposed commands are not executed commands; static inspection is not a runtime test; an unobserved action is not a completed delegation.

A handoff preserves task identity and scope, current state and last verified checkpoint, completed actions and evidence, files changed, commands run and actual relevant outputs, decisions and assumptions, blockers, and the next action.

## 7. Contracts
YAML is the human-editable contract format. JSON Schema files provide machine-readable validation definitions where present. Shared contracts evolve only through an explicitly approved change; Manager may not unilaterally redefine cross-project contracts.

## 8. Security and execution
The initial release does not autonomously run commands, access servers, or call model APIs. Users run generated commands themselves when no connected execution mechanism is available. The role hierarchy still applies: Manager assigns work to Technical Agents, and Technical Agents prepare and verify technical actions. If the actual runtime cannot perform a required step, report it as blocked.

Commands that delete data, change permissions broadly, expose secrets, alter production services, or make irreversible changes require clear risk explanation and appropriate confirmation.

Never store credentials, private keys, API tokens, or .env files in the public repository.
