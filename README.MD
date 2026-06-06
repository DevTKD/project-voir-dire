# project-voir-dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to determine their suitability for a trial.

`project-voir-dire` is a Python backend learning project that simulates the core scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Latest additions

- Added initial domain files for modeling case and juror concepts.
- Added scaffold classes for juror profile types in `juror.py`:
  - `BacisProfile` (basic profile placeholder)
  - `EnhancedProfile` (enhanced profile placeholder)
- Added starter comments in `case.py` and `juror.py` to define implementation direction.

## Current project structure

```text
Project-Voir-Dire/
├── case.py
├── juror.py
└── README.MD
```

## Project goal

The system will use synthetic juror profiles, weighted scoring rules, and explainable calculations to estimate whether a juror may lean more plaintiff-friendly or defense-friendly in a fictional civil trial scenario.

This project is being built incrementally as part of Python backend learning, with a planned path toward a REST API, persistence, authentication, testing, and CI/CD.

## Next development milestones

- Implement concrete fields and behavior for juror profiles.
- Add case attributes that influence juror scoring.
- Build a scoring function with transparent rule-based output.
- Introduce tests for profile validation and scoring logic.
