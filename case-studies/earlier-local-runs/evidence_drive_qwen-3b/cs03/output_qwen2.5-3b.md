### Phase 1: Discovery
#### docs/ARTIFACT_1.md
```markdown
# Discovery
## Known facts
- Users need a simple tool to prepare follow-up drafts from lead data.
- The system will handle CSV uploads and produce plain text follow-ups.

## Open questions
- How will the system parse the CSV?
- How will it structure the follow-up text?
- How will we handle errors and edge cases?
```

### Phase 2: PRD
#### docs/PRD.md
```markdown
# PRD

## Problem
The system shall allow users to upload a CSV file of lead data and generate a plain text follow-up draft for each lead.

## Users
Users are marketers or salespeople who need to prepare personalized follow-up emails from lead information.

## Goals and non-goals
- Goal: Provide a user-friendly interface for uploading and processing CSVs.
- Non-goal: Send the follow-up drafts to any external systems or services.

## Functional requirements (FR-01)
**Given**: A CSV file with at least two columns (e.g., 'Lead Name', 'Email', 'Phone Number').
**When**: The system processes the CSV file.
**Then**: One plain text follow-up draft is generated for each lead. Drafts are unique per lead and include all relevant lead information.

### Non-functional requirements
- **Security**: Follow all security best practices, including proper handling of CSV files and user data.
- **Performance**: Ensure the system can handle up to 100 CSV files per minute with a response time of less than 3 seconds.
- **Accessibility**: Ensure the system is accessible to users with disabilities.

## Traceability
| Functional requirement | Source document path |
|------------------------|---------------------|
| FR-01                 | docs/PRD.md         |

## Risks
- CSV parsing errors.
- User data exposure.
- Performance issues.

## Out of scope
- No sending of follow-up drafts to external systems or services.
- No integration with CRM or marketing automation platforms.
```

### Phase 3: Design Docs
#### docs/diagrams/use_case.md
```markdown
# User Story Map
## Use Case Diagram
**FR-01** is covered by this use case map. It shows the flow from user uploading a CSV to the system generating follow-up drafts.

## Diagram
```
```
```

#### docs/diagrams/architecture.md
```markdown
# Architecture Diagram
## Data Flow Diagram
**FR-01** is covered by this architecture diagram. It shows how data flows from CSV upload to follow-up draft generation.

## Diagram
```
```
```

#### docs/diagrams/sequence.md
```markdown
# Sequence Diagram
## Follow-up Draft Generation Sequence
**FR-01** is covered by this sequence diagram. It shows the sequence of steps from CSV upload to generating follow-up drafts.

## Diagram
```
```
```

### Phase 4: Guides and Rules
#### docs/README.md
```markdown
# Read Me
This document guides you through the project setup, contributing, testing, and progress tracking. Follow the order of these files:
1. [docs/SETUP.md]
2. [docs/CONTRIBUTING.md]
3. [docs/TESTING.md]
4. [docs/README.md]

## Agent Context Files
- [docs/AGENTS.md] for information about agents involved in this project.
- [docs/CODE_STYLE.md] for code style guidelines.
- [docs/NEVER_DO.md] for a never-do list (no secrets in code, no em dashes, no AI credit lines).

## Context Files
- [docs/CLAUDE.md] for Claude Code.
- [docs/CURSOR/rules/*.mdc] for Cursor.
- [docs/.github/copilot-instructions.md] for GitHub Copilot.

## Stable Doc Prefix
```
```
```

#### docs/SETUP.md
```markdown
# Setup
## Installation
- Install the required dependencies: Python, FastAPI, and any other necessary libraries.

## .env Variables
- `.env.example` provides variable names with no values.
- `.env` should be added to `.gitignore`.

## Running
- Run the application using `python main.py`.

## Testing
- Use `pytest` to run tests. Aim for a coverage of at least 80%.
- Run the demo script to see the system in action.
```

#### docs/CONTRIBUTING.md
```markdown
# Contributing
## Build and Test Commands
- Install the required dependencies: Python, FastAPI, and any other necessary libraries.
- Run the application using `python main.py`.
- Use `pytest` to run tests. Aim for a coverage of at least 80%.

## Code Style
- Follow the code style guidelines provided in [docs/CODE_STYLE.md].

## Never Do
- Do not include secrets in code.
- Do not use em dashes.
- Do not include AI credit lines.

## Read Docs/PRD.md Before Changing Behavior
```

#### docs/TESTING.md
```markdown
# Testing
## Pytest
- Use `pytest` to run tests. Aim for a coverage of at least 80%.
- Use `pytest --cov docs` to target specific directories.

## Demo Script
- Run the demo script to see the system in action.
```

#### docs/NEVER_DO.md
```markdown
# Never Do
- Do not include secrets in code.
- Do not use em dashes.
- Do not include AI credit lines.
```

#### docs/CODE_STYLE.md
```markdown
# Code Style
- Follow the code style guidelines provided in [docs/README.md].

## Never Do
- Do not include secrets in code.
- Do not use em dashes.
- Do not include AI credit lines.
```

#### docs/CLAUDE.md
```markdown
# Claude Code
- [docs/CODE_STYLE.md] for code style guidelines.
- [docs/NEVER_DO.md] for a never-do list (no secrets in code, no em dashes, no AI credit lines).

## Importing Other Files
- Use `@path` to import other files in this index.
```

#### docs/CURSOR/rules/*.mdc
```markdown
# Cursor
- [docs/README.md] for general context files.
- [docs/CONTRIBUTING.md] for contributing guidelines.
- [docs/TESTING.md] for testing instructions.

## Frontmatter
- `alwaysApply` to apply changes to all files in this folder.
- `glob` to apply changes to specific files or directories.
- `description` to provide additional context for changes.
```

#### docs/.github/copilot-instructions.md
```markdown
# GitHub Copilot Instructions
- [docs/README.md] for general context files.
- [docs/CONTRIBUTING.md] for contributing guidelines.
- [docs/TESTING.md] for testing instructions.

## Context Files
- Follow the instructions provided in [docs/README.md].
```

### Phase 5: Plan
#### docs/TASKS.md
```markdown
# Tasks
## Task 1 (