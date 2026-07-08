# Darwin Round 6 Evaluation — Learning Contract and AI Diet

## Goal

Add a learning-control layer to the factory: L1-L9 learning stages, default L6 for A-priority concepts, AI assistance modes, productive friction, verifiability policy, evidence-level state tracking, model-vs-reality protocol, and barehand checkpoints.

## Implemented

- Added learning-contract generated directory.
- Added teacher policies for stage-aligned assessment, AI diet, productive friction, verifiability, feedback anchoring, model-vs-reality, and negative features.
- Added state files for concept evidence levels, transfer checks, barehand checkpoints, and AI assistance logs.
- Added `check_learning_stage_evidence.py` and integrated it into `quality_check_course_okf.py`.
- Added CLI `--target-learning-level` with default L6.
- Added tests for default L6, override recording, and missing-contract failure.

## Design Constraint

This revision intentionally does not make every concept target L6. A-priority concepts default to L6; B and C priorities may have lower targets unless user overrides.
