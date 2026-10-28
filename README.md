# Agent Management System

A file-based, Git-versioned framework for coordinating AI agents across software projects while minimizing repeated context collection and preserving project state across agent handoffs.

> Initial release: architecture and operational contracts. This repository does not execute AI agents automatically.

## Goals

- Keep project state outside conversation history.
- Separate global planning (Agent Alpha), execution coordination (Agent Manager), and implementation (Technical Agent).
- Reuse project information instead of repeatedly asking for the same files or command output.
- Keep agents extensible through profiles and shared contracts.
- Preserve work through structured execution reports and handoffs.
- Keep real-world execution under explicit human control in the initial version.

## Canonical architecture

The architecture and operating rules agreed for the current design are documented in [docs/FINAL_ARCHITECTURE.fa.md](docs/FINAL_ARCHITECTURE.fa.md).

The document defines role boundaries, approval authority, communication paths, bootstrap rules, message contracts, task lifecycle, terminal command conventions, verification requirements, and safe escalation.

## Architecture overview

~~~text
Human User <-> Agent Alpha
                   |
                   | approved plan / decisions
                   v
              Agent Manager
                   |
                   | scoped task instructions
                   v
             Technical Agent
                   |
                   | command request, if direct access is unavailable
                   v
       Human runs commands and returns actual output
                   |
                   v
             Technical Agent
                   |
                   | evidence-backed execution report
                   v
              Agent Manager
                   |
                   | status, blockers, decisions needed
                   v
                Agent Alpha
                   |
                   v
              Human User
~~~

The user manually relays messages between independent chats. This does not change the intended recipient of a message. The Manager does not communicate directly with the human user. The Technical Agent may interact with the user only in a limited way to resolve real execution blockers, such as terminal errors.

## Repository map

- `docs/`: architecture and workflow documentation.
- `contracts/`: shared YAML contract templates and their JSON Schemas.
- `agents/`: role profiles and responsibilities.
- `project_state/`: templates for project status, graph, and information index.
- `tasks/`: task record templates.
- `reports/`: execution report templates.
- `handoffs/`: handoff templates.
- `scripts/`: small validation and repository-audit utilities.
- `tests/`: tests for included utility scripts.

## Quick start

Requirements: Python 3.10+ and Git. The core repository uses only Python's standard library. Optional YAML validation requires `PyYAML`.

~~~bash
git clone https://github.com/sina1991/agent-management-system.git
cd agent-management-system
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_yaml.py
python -m unittest discover -s tests -v
~~~

On Windows, activate the virtual environment with `.venv\\Scripts\\activate`.

The validation script reports a clear message if `PyYAML` is not installed. To install the optional dependency directly:

~~~bash
python -m pip install PyYAML
~~~

## Operating principles

1. **AUDIT → APPLY → VERIFY**: inspect current state before edits, make a focused change, then verify it.
2. **Reuse before recollecting**: check the Information Index and existing artifacts before asking for more context.
3. **Collect in batches**: group independent inspection commands into one focused collection step when practical.
4. **Read narrowly**: an archive may contain many files, but only task-relevant content should enter the model context.
5. **Evidence over claims**: a task is not considered verified merely because an agent says it is complete.
6. **Human-controlled execution**: in this initial version, the user runs terminal commands and returns their actual output when direct execution access is unavailable.
7. **Explicit role boundaries**: Alpha owns global architecture and Unit Agent definitions; Manager coordinates approved work; Technical implements scoped tasks.
8. **Secrets stay private**: never commit API keys, passwords, private server data, or `.env` files.

## Project status

Architecture documentation is being submitted for review through a Pull Request. A document or PR being present does not mean it has been merged or that all implementation profiles, schemas, and tests have already been synchronized and verified.
