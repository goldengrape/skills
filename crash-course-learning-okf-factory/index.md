---
okf_version: "0.1"
bundle: crash-course-learning-okf-factory
title: Crash Course Learning OKF Factory
description: A meta-factory that generates stateful course-learning OKF bundles for one-week, one-hour-per-day exam cramming.
timestamp: 2026-06-30T00:00:00-07:00
---

# Crash Course Learning OKF Factory

This OKF bundle is a **meta-factory**. It does not represent one course. It defines how an agent should generate a new, stateful **Course Learning OKF** from a course name, learner baseline, exam constraints, time budget, and available materials.

# Start Here

* [URD](docs/URD.md) - User requirements and acceptance criteria.
* [ADD](docs/ADD.md) - Design split, FR/DP mapping, coupling notes, and execution order.
* [TRACE](docs/TRACE.md) - Requirement to design and file links.
* [Factory Overview](factory/factory-overview.md) - What the factory is responsible for.
* [Generation Contract](factory/course-okf-generation-contract.md) - Required input and output contract.
* [Course Instance Layout](schemas/course-instance-layout.md) - The exact OKF structure generated for each course.
* [Instantiate Course OKF](playbooks/generate-new-course-okf.md) - Main playbook for creating a course instance.
* [Resume Course Session](playbooks/resume-course-session.md) - How to continue from saved learner state.
* [State Update Protocol](playbooks/update-state-after-session.md) - How the course OKF remembers progress.
* [Validation Playbook](playbooks/validate-generated-course-okf.md) - How to validate structure and output contract.
* [Quality Gate Playbook](playbooks/evaluate-generated-course-okf.md) - How to check whether generated content is course-specific and exam-ready.
* [Repair Playbook](playbooks/repair-generated-course-okf.md) - How to revise a failed generated course OKF and rerun quality checks.
* [Master Factory Prompt](templates/master-factory-prompt.md) - Copyable prompt for using this factory with an agent.

# Directory Map

* [docs/](docs/) - URD and ADD source documents.
* [factory/](factory/) - Factory-level concepts and contracts.
* [schemas/](schemas/) - File schemas for generated course OKFs.
* [playbooks/](playbooks/) - Agent procedures for generating and running course instances.
* [templates/](templates/) - Reusable templates for generated course OKF files.
* [examples/](examples/) - Small examples showing expected outputs.
* [references/](references/) - Source notes and design references.
* [analysis/](analysis/) - Evaluation and revision reports.

# Factory Promise

Given a course name and a learner baseline, the factory should produce a new OKF bundle that can:

1. Store the learner's current state in files.
2. Generate daily one-hour learning packages.
3. Record each learning session.
4. Update recall cards, misconceptions, score estimates, plan changes, and next actions.
5. Resume from saved state instead of relying on model memory.
6. Adapt future days instead of blindly following the original plan.
7. Export a final exam-cram review pack.
8. Return structural validation, content quality, repair status, and clear entrypoint.

# Citations

[1] [OKF Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)  
[2] [teach skill workspace](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach)


## Local MVP Helper

Use `tools/materialize_course_okf.py` when you need a deterministic skeleton generator for the required Course Learning OKF file tree. It creates initial state, day plans, quizzes, final-review files, `generation-output.json`, and `quality-report.json`. If quality fails and a local course seed exists, it repairs and rechecks once.
