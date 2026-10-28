# Agent Management System

A file-based, Git-versioned framework for coordinating AI agents across software projects while minimizing repeated context collection and preserving project state across agent handoffs.

> Initial release: architecture and operational contracts. This repository does not execute AI agents automatically.

## Goals
- Keep project state outside conversation history.
- Separate project authority (Agent Alpha), execution coordination (Agent Manager), and technical implementation (Technical Agent).
- Reuse project information instead of repeatedly asking for the same files or command output.
- Keep agents extensible through profiles and shared contracts.
- Preserve work through structured execution reports and handoffs.
- Keep real-world execution under explicit human control in the initial version.

## Authority boundaries
- **Agent Alpha** owns project direction, architecture, roadmap, phases, unit boundaries, shared contracts, and material scope decisions.
- **Agent Manager** coordinates an approved mission, creates task contracts, delegates technical work to Technical Agents, reviews evidence, and reports to Alpha. Manager does not redesign the project or change architecture/scope.
- **Technical Agent** performs assigned technical work, verifies it, and returns an evidence-backed report to Manager.
- If mission input is materially ambiguous, Manager asks Alpha before dispatching affected work.
- Manager output is operational work orders and concise evidence-based status reports—not conversational filler or user-facing commands as a substitute for delegation.
- If an actual Technical Agent/runtime is unavailable, Manager reports the assignment as blocked. No role may pretend an agent ran or a command succeeded.

## Architecture
User ↔ Agent Alpha ↔ Agent Manager ↔ Technical Agent(s) ↔ Agent Manager ↔ Agent Alpha

In the initial release, the user may relay messages and run terminal commands. This is a transport/runtime limitation, not permission for Manager to bypass Technical Agents.

## Repository map
- docs/: architecture and workflow documentation.
- contracts/: shared YAML contract templates and their JSON Schemas where present.
- agents/: role profiles and responsibilities.
- project_state/: templates for project status, graph, and information index.
- tasks/: task record templates.
- reports/: execution report templates.
- handoffs/: handoff templates.
- scripts/: small validation and repository-audit utilities.
- tests/: tests for included utility scripts.

## Quick start
Requirements: Python 3.10+ and Git. The core repository uses only Python's standard library. Optional YAML validation requires PyYAML.

```bash
git clone https://github.com/sina1991/agent-management-system.git
cd agent-management-system
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_yaml.py
python -m unittest discover -s tests -v
```

On Windows, activate the virtual environment with .venv/Scripts/activate.

The validation script reports a clear message if PyYAML is not installed. To install the optional dependency directly:

```bash
python -m pip install PyYAML
```

## Operating principles
1. **AUDIT → APPLY → VERIFY**: inspect current state before edits, make a focused change, then verify it.
2. **Reuse before recollecting**: check the Information Index and existing artifacts before asking for more context.
3. **Collect in batches**: group independent inspection commands into one focused collection step when practical.
4. **Read narrowly**: an archive may contain many files, but only task-relevant content should enter an agent's context.
5. **Evidence over claims**: a task is not verified merely because an agent says it is complete.
6. **Human-controlled execution**: in this initial version, the user runs terminal commands when no supported execution runtime is available.
7. **Mandatory role separation**: Manager delegates; Technical Agents execute; Alpha decides project-level questions.
8. **Secrets stay private**: never commit API keys, passwords, private server data, or .env files.

## GitHub publication
Suggested public repository URL: https://github.com/sina1991/agent-management-system

This archive does not create or publish the GitHub repository. Create the empty repository on GitHub first, then add it as the remote and push the reviewed files:

```bash
git init
git add .
git commit -m "Initial architecture and agent contracts"
git branch -M main
git remote add origin https://github.com/sina1991/agent-management-system.git
git push -u origin main
```

If the repository already exists and contains commits, inspect its state before pushing; do not blindly overwrite remote history.
