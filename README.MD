# Project Voir Dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to evaluate their suitability for trial.

`project-voir-dire` is a Python backend learning project that models the early scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Project goal

Build an explainable, rule-based system that uses synthetic juror data and case context to estimate whether a juror may lean plaintiff-friendly or defense-friendly in a fictional civil trial.

The project is being developed incrementally, with a planned path toward an API layer, persistence, authentication, testing, and CI/CD.

## Latest update

### June 24, 2026

- Added `evaluation.py` to connect a juror profile with a case profile and store the resulting `juror_score`.
- Kept the dataclass-based domain model split across:
  - `juror.py` for juror profile data.
  - `case.py` for case context and screening questions.

## Changelog

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
└── README.MD
```


## Next development milestones

- Add validation and normalization for profile field values.
- Expand case attributes that influence juror scoring.
- Build a scoring function with transparent rule-based output.
- Introduce tests for profile validation and scoring logic.
