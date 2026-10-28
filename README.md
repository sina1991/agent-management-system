# Agent Management System

A file-based, Git-versioned framework for coordinating three AI-agent roles across independent conversations while minimizing repeated context collection and preserving project state across handoffs.

> Current status: the public repository and initial scaffold exist. The repository defines the roles and contracts; it does not automatically orchestrate AI agents or share conversation histories.

## Goals

- Keep canonical project state outside conversation history.
- Separate global planning (`Agent Alpha`), execution coordination (`Agent Manager`), and implementation (`Technical Agent`).
- Reuse project information instead of repeatedly asking for the same files or command output.
- Preserve work through structured task contracts, execution reports, and handoffs.
- Keep real-world execution under explicit human control in the initial version.

## Three roles

- **Agent Alpha:** communicates with the user, plans and approves architecture and milestones, delegates approved missions to Manager, reviews progress, and owns global project status.
- **Agent Manager:** receives approved missions from Alpha, prepares task-specific context, directs Technical Agent, checks evidence, maintains reusable records, and reports to Alpha.
- **Technical Agent:** accepts tasks from Manager, inspects and changes the project within scope, verifies results, and returns an Execution Report or Handoff to Manager.

## Three-chat workflow

See [docs/CHAT_BOOTSTRAP.md](docs/CHAT_BOOTSTRAP.md) for the required startup protocol and [docs/WORKFLOW.md](docs/WORKFLOW.md) for the operating workflow.

1. In the first chat, ask the Agent to inspect this repository. It must summarize the verified components briefly and ask you to confirm activation as Alpha.
2. In the second chat, explicitly activate Manager and pass it Alpha's approved mission.
3. In the third chat, explicitly activate Technical Agent and pass it Manager's Task Contract and focused context package.
4. Transfer concise mission/report messages between chats. The chats do not automatically see one another's history.
5. Treat GitHub as the shared file reference, not as proof that all chats can access it. Each chat must verify actual access.
6. In the initial version, the user runs terminal commands and returns the real output.

## Architecture and state

- `agents/`: role profiles.
- `contracts/`: YAML templates and JSON Schemas for tasks, execution reports, and handoffs.
- `project_state/`: current project status, Project Graph, and Project Information Index.
- `docs/`: architecture, bootstrap, repository layout, and workflow.
- `tasks/`, `reports/`, `handoffs/`: locations for persistent work records.
- `scripts/`, `tests/`: repository audit, YAML validation, and scaffold tests.

## Operating principles

1. **AUDIT -> APPLY -> VERIFY**: inspect current state before edits, make a focused change, then verify it.
2. **Reuse before recollecting**: check the Information Index and existing artifacts before asking for more context.
3. **Collect in batches**: group independent inspection commands into one focused collection step when practical.
4. **Read narrowly**: only task-relevant content should enter the model context.
5. **Evidence over claims**: an agent's claim alone does not verify completion.
6. **Human-controlled execution**: the user runs commands and returns actual output in the initial version.
7. **Secrets stay private**: never commit credentials, private keys, API tokens, or private server data.

## Local validation

Requirements: Python 3.10+ and Git. YAML validation requires `PyYAML`.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_yaml.py
python -m unittest discover -s tests -v
```

## Repository

Public repository: https://github.com/sina1991/agent-management-system

Changes should be reviewed, validated, and committed through the normal Git workflow. Do not force-push or overwrite remote history without an explicit reason and review.
