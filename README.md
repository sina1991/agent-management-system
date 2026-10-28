# Agent Management System

A file-based, Git-versioned framework for coordinating AI agents across software projects while minimizing repeated context collection and preserving project state across agent handoffs.

> Initial implementation: independent conversations use versioned repository files as shared references. The system does not automatically orchestrate agents or share chat histories.

## Canonical architecture

The authoritative architecture and operating protocol is [docs/FINAL_ARCHITECTURE.fa.md](docs/FINAL_ARCHITECTURE.fa.md).

It defines the role boundaries, approval authority, communication paths, bootstrap method, message contracts, task lifecycle, project state, terminal command conventions, evidence-based verification, and escalation rules.

## Three-agent flow

~~~text
Human User <-> Agent Alpha
                   |
                   | approved plan / decisions
                   v
              Agent Manager
                   |
                   | scoped task assignment
                   v
             Technical Agent
                   |
                   | terminal commands if direct access is unavailable
                   v
       Human runs commands and returns actual output
                   |
                   v
             Technical Agent
                   |
                   | evidence-backed report
                   v
              Agent Manager
                   |
                   | status / blockers / decisions needed
                   v
                Agent Alpha
                   |
                   v
              Human User
~~~

The user manually relays messages between independent chats. The message's named recipient does not change during relay. Manager communicates only with Alpha and assigned agents; it must not directly ask the human for instructions or report to them. Technical may interact with the human only in a limited operational way to resolve execution blockers.

## Repository map

- `docs/`: canonical architecture, bootstrap, and workflow documentation.
- `agents/`: role profiles and responsibilities.
- `contracts/`: YAML templates and JSON Schemas for tasks, execution reports, and handoffs.
- `project_state/`: project status, Project Graph, and Project Information Index.
- `tasks/`, `reports/`, `handoffs/`: persistent work records.
- `scripts/`, `tests/`: repository audit, YAML validation, and scaffold tests.

## Quick start and validation

Requirements: Python 3.10+ and Git. YAML validation requires `PyYAML`.

~~~bash
git clone https://github.com/sina1991/agent-management-system.git
cd agent-management-system
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_yaml.py
python -m unittest discover -s tests -v
~~~

On Windows, activate the environment with `.venv\\Scripts\\activate`.

## Operating principles

1. **AUDIT -> APPLY -> VERIFY:** inspect current state before editing, make a focused change, then verify it.
2. **Reuse before recollecting:** check the Information Index and existing artifacts before requesting information again.
3. **Evidence over claims:** an agent's claim alone does not verify completion.
4. **Approved scope:** Manager acts autonomously only within Alpha's approved plan.
5. **Explicit communication boundaries:** Alpha communicates with the human; Manager reports only to Alpha; Technical reports to Manager.
6. **Human-controlled execution:** when direct runtime access is unavailable, the user executes commands and returns actual output.
7. **Secrets stay private:** never commit API keys, passwords, private keys, or `.env` files.

## Current change status

The architecture document, role profiles, bootstrap/workflow docs, task and execution-report contracts, project-state records, and scaffold tests are being aligned in [Pull Request #5](https://github.com/sina1991/agent-management-system/pull/5).

The changes have been read back from GitHub, but automated tests have not yet been executed in a Python runtime. Do not treat the PR as merged until GitHub confirms the merge.
