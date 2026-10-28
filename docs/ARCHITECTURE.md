# Architecture

## 1. Purpose
Agent Management System (AMS) coordinates AI agents without treating conversation history as the canonical project state. It starts as a file-based, Git-versioned system. Automated model orchestration, databases, dashboards, and direct server execution are outside the initial implementation unless Agent Alpha explicitly approves a later architecture change.

## 2. Role hierarchy and authority

### Agent Alpha — project owner and decision authority
- Owns project direction, high-level architecture, roadmap, phases, execution-unit boundaries, dependencies, shared contracts, and material scope changes.
- Approves missions and acceptance criteria for execution managers.
- Makes approved decisions binding until Alpha explicitly revises them.
- Requires every operational response to state status, verified work, remaining work, next responsible actor, exact next action, and expected evidence.
- Normally does not implement code.

### Agent Manager — execution coordinator, not project architect
- Receives an approved mission from Alpha and coordinates delivery.
- Checks the Project Graph, Information Index, task records, and relevant artifacts before asking for context.
- Prepares bounded Task Contracts and task-specific context packages, delegates technical work, tracks dependencies, reviews evidence, requests focused corrections, and reports to Alpha.
- Must not define or change architecture, project-wide design, roadmap, phases, ownership boundaries, cross-unit contracts, or material scope. These decisions require Alpha's explicit approval.
- Must produce operational Work Orders and concrete next actions, not filler, vague warnings, or a description of work someone might do.
- If a real Technical Agent/runtime is unavailable, Manager must not simulate dispatch. It must still prepare copy-ready Work Orders for the approved paths when possible; only actual dispatch/execution is blocked.

### Technical Agent — scoped executor
- Receives a bounded Task Contract / Work Order from Manager.
- Inspects relevant state, performs only the assigned work, and verifies acceptance criteria.
- Uses actual repository tools when available. If human-run terminal execution is required, prepares focused commands and specifies the exact output to return.
- Reports files, diffs, commits, commands actually run, verification evidence, unresolved items, status, and the next action to Manager.
- Does not change architecture, expand scope, or take cross-unit decisions. Escalates uncertainty to Manager.

## 3. Communication and workflow
User ↔ Agent Alpha ↔ Agent Manager ↔ Technical Agent(s) ↔ Agent Manager ↔ Agent Alpha

In the initial release, the user may relay messages and run terminal commands. This is a transport/execution constraint, not permission for Manager to bypass Technical Agents. When autonomous dispatch is unavailable, Manager prepares Work Orders for user relay and clearly labels them as prepared rather than dispatched.

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
The initial release does not autonomously run commands, access servers, or call model APIs. Users run generated commands themselves when no connected execution mechanism is available. The role hierarchy still applies: Manager assigns work to Technical Agents, and Technical Agents prepare and verify technical actions. If the actual runtime cannot perform a required step, report that specific step as blocked while continuing all useful in-scope preparation.

Commands that delete data, change permissions broadly, expose secrets, alter production services, or make irreversible changes require clear risk explanation and appropriate confirmation.

Never store credentials, private keys, API tokens, or .env files in the public repository.
