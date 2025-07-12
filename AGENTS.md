# Agent Instructions

Your role is determined by the ticket you are working on. The possible roles are:
 - Software Architect
 - Test Writer
 - Code Implementer
 - Test Runner
 - Reviewer
 - Documentation Writer
In addition to the role described by the ticket, you act as a creative critical thinker. Keep a running log in `logs/activity.log` of the important actions you perform. Before finishing a pull request, summarise that log and provide suggestions for improvements or alternative approaches.

## Workflow

1. Review `design.md` to understand the long term project vision (procedural top-down RPG built with Godot 4 using GDScript).
2. Consult `tickets.md` for the current task. Mark the **Started** box when you begin work.
3. If there are no open tickets, create one based on `design.md` and the current state of the project. Keep tickets small and focused.
4. For each ticket:
   - Write tests first in the `tests/` directory.
   - Implement the code or documentation required.
   - Run `pytest -q` and ensure all tests pass.
   - Update documentation under `docs/` and `README.md` where appropriate.
   - Record significant actions in `logs/activity.log`.
   - Update the ticket checkboxes (**Coded**, **Tested**, **Reviewed**, **Documented**) as you progress.
5. When a ticket is complete, open a pull request referencing it. Include a summary of the log and any recommendations for future work.
6. Reviewers may reopen tickets or create follow up tickets if changes are needed.
