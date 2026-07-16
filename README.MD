# Project Voir Dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to evaluate their suitability for trial.

`project-voir-dire` is a Python backend learning project that models the early scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Project goal

Build an explainable, rule-based system that uses synthetic juror data and case context to estimate whether a juror may lean plaintiff-friendly or defense-friendly in a fictional civil trial.

The project is being developed incrementally, with a planned path toward an API layer, persistence, authentication, testing, and CI/CD.

## Latest update

### July 16, 2026

- Updated `evaluation.py` so `Evaluation` stores:
  - the `juror` (`BasicProfile`)
  - the `case` (`CaseProfile`)
  - an `answers` dictionary keyed by question field
  - a persisted `juror_score` value (default `0`)
- Implemented `juror_score(evaluation: Evaluation)` in `scorer.py` to:
  - iterate through `evaluation.case.questions`
  - match each juror answer to `trigger_answer`
  - add matching `weight` values into a total score
  - write the computed total back to `evaluation.juror_score`
  - return the computed score

## Changelog

### 2026-07-16

- Documented completed scoring behavior in `scorer.py`, including question/answer trigger matching and weighted totals.
- Documented `Evaluation` fields in `evaluation.py`, including answers storage and persisted `juror_score`.

### 2026-07-02

- Added `scorer.py` and documented the initial scoring module scaffold.
- Updated the project structure to include `scorer.py`.

### 2026-06-24

- Documented the new evaluation model and updated the project structure.

### 2026-06-16

- Documented and aligned model changes for `CaseQuestion` and `CaseProfile` in `README.MD`.

## Current project structure

```text
Project-Voir-Dire/
├── case.py
├── evaluation.py
├── juror.py
├── scorer.py
└── README.MD
```


## Next development milestones

- Add validation and normalization for profile field values.
- Expand case attributes that influence juror scoring.
- Expand scoring rules beyond exact trigger-answer matches.
- Introduce tests for profile validation and scoring logic.
