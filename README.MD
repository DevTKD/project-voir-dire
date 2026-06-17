# Project Voir Dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to evaluate their suitability for trial.

`project-voir-dire` is a Python backend learning project that models the early scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Project goal

Build an explainable, rule-based system that uses synthetic juror data and case context to estimate whether a juror may lean plaintiff-friendly or defense-friendly in a fictional civil trial.

The project is being developed incrementally, with a planned path toward an API layer, persistence, authentication, testing, and CI/CD.

## Latest update

### June 16, 2026

- Added dataclass-based domain models for juror and case data.
- Implemented `juror.py` profile models:
  - `BasicProfile` with core demographic and background fields.
  - `EnhancedProfile` with supplemental screening fields.
- Updated `case.py` models:
  - Added `CaseQuestion` with `field`, `trigger_answer`, and `weight`.
  - Updated `CaseProfile` with `case_type`, `jurisdiction`, and `questions` (`list[CaseQuestion]`).

## Changelog

### 2026-06-16

- Documented and aligned model changes for `CaseQuestion` and `CaseProfile` in `README.MD`.

## Current project structure

```text
Project-Voir-Dire/
├── case.py
├── juror.py
└── README.MD
```


## Next development milestones

- Add validation and normalization for profile field values.
- Expand case attributes that influence juror scoring.
- Build a scoring function with transparent rule-based output.
- Introduce tests for profile validation and scoring logic.
