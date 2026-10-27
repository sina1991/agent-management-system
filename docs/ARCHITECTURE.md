# Architecture

## 1. Purpose

Agent Management System (AMS) coordinates AI agents without treating conversation history as the canonical project state. It starts as a file-based, Git-versioned system. Automated model orchestration, databases, dashboards, and direct server execution are out of scope for the initial version.

## 2. Components

### Agent Alpha — global project owner
- Receives project goals and decisions from the user.
- Owns and approves the high-level architecture and delivery phases.
- Defines execution units, boundaries, dependencies, and acceptance criteria.
- Receives reports from execution managers and maintains the concise project status.
- Handles decisions beyond the manager's authority.
- Normally does not implement code.

### Agent Manager — execution-unit manager
- Receives approved missions from Alpha.
- Inspects the Project Graph and Information Index before requesting context.
- Plans the minimum useful context package for each Technical Agent.
- Splits missions where needed and selects suitable Agent profiles.
- Reviews execution reports and asks for correction or replacement when needed.
- Detects repeated information requests, duplicated work, excessive context, and scope drift.
- Updates task status and reusable information records.
- Reports outcomes and blockers to Alpha.
- Produces a handoff package if execution cannot continue.

### Technical Agent
- Receives its task only from the Manager.
- Inspects relevant project state, graph position, dependencies, and existing artifacts.
- Collects required context in one batch where practical; performs follow-up collection only when a real gap or contradiction is discovered.
- Performs focused analysis and implementation.
- Gives the user copy-ready terminal commands in small, clearly scoped steps; the user runs them and returns actual output.
- Uses `AUDIT → APPLY → VERIFY`.
- Makes obvious, low-risk decisions within scope and reports them to the Manager.
- Escalates architecture changes, risky actions, and scope changes to the Manager.
- Reports verified outcomes and unresolved items, or creates a handoff.

### Other optional profiles
Architecture, Coding, QA, Repository Analyst, Security, Documentation, DevOps, and Planning Agents can be added without changing the core role boundaries.

## 3. Communication boundaries

```text
User <-> Agent Alpha
          |
          v
     Agent Manager <-> Technical Agent(s)
          ^                  |
          |                  v
          +---- reports   User-run terminal
```

The user relays messages and runs real commands in the initial workflow. The Manager's valid coordination counterpart is Alpha and the Technical Agents assigned to its unit. The Technical Agent accepts work from its Manager and reports completion to that Manager.

## 4. Project Graph and Project Information Index

The Project Graph describes components, relationships, dependencies, ownership, and task location.

The Project Information Index records what project information has already been collected, where it is stored, what it covers, when it was observed, and whether it is still believed to be valid. The Index is a lightweight lookup/metadata layer; it must not duplicate all source content.

The Manager is responsible for using these artifacts to avoid repeated collection. The Technical Agent is not forced through a rigid context-gathering ritual; it should make progress and the Manager corrects inefficient behavior.

## 5. Context package policy

- Reuse existing, still-valid artifacts first.
- Identify task-relevant files from the graph and task scope.
- Group independent inspection commands into a single focused collection step when practical.
- Prefer targeted excerpts over full file dumps.
- Archives may be used for transfer, but archive contents should not automatically be pasted into the model context.
- Request further information only for a material unknown, contradiction, or changed file.
- Do not repeat a request when the same valid output is already available.
- Record reusable results in the Index after successful collection.

## 6. State and lifecycle

Task states: `draft`, `ready`, `in_progress`, `blocked`, `review`, `completed`, `cancelled`.

A task is `completed` only when its acceptance criteria are supported by evidence. An agent's claim alone is not verification.

Handoff should preserve:
- task identity and scope;
- current state and last verified checkpoint;
- actions completed and evidence;
- files changed;
- commands run and actual relevant outputs;
- decisions and assumptions;
- blockers and remaining work;
- next recommended action.

## 7. Contracts

YAML is the human-editable contract format. JSON Schema files provide machine-readable validation definitions. The initial contracts are intentionally small and can evolve with explicit version changes.

## 8. Security and execution

The initial release does not autonomously run commands, access servers, or call model APIs. Users run generated commands themselves. Commands that delete data, change permissions broadly, expose secrets, alter production services, or make irreversible changes require clear risk explanation and appropriate confirmation.

Never store credentials, private keys, API tokens, or `.env` files in the public repository.
