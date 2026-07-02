# Project Voir Dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to evaluate their suitability for trial.

`project-voir-dire` is a Python backend learning project that models the early scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Project goal

Build an explainable, rule-based system that uses synthetic juror data and case context to estimate whether a juror may lean plaintiff-friendly or defense-friendly in a fictional civil trial.

The project is being developed incrementally, with a planned path toward an API layer, persistence, authentication, testing, and CI/CD.

## Latest update

### July 2, 2026

- Added `scorer.py` as the home for juror scoring logic.
- Set up initial imports in `scorer.py` to use:
  - `case.py` for case context.
  - `juror.py` for juror profile data.
- Kept `evaluation.py` as the relationship model that stores a juror's score for a specific case.

## Changelog

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
- Implement `juror_score()` in `scorer.py` with transparent rule-based output.
- Introduce tests for profile validation and scoring logic.
