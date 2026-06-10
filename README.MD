# project-voir-dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to determine their suitability for a trial.

`project-voir-dire` is a Python backend learning project that simulates the core scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Latest additions

- Added dataclass-based domain models for juror and case data.
- Implemented `juror.py` profile models:
  - `BasicProfile` with core demographic and background fields:
    - `age_range`, `gender`, `marital_status`, `num_of_children`
    - `education_level`, `occupation`, `employment_status`, `income_range`
    - `homeownership_status`, `military_status`, `prior_jury_service`
  - `EnhancedProfile` with supplemental screening fields:
    - `business_owner`, `union_member`, `prior_law_enforcement`
    - `legal_professional`, `government_employee`, `prior_witness_experience`
- Implemented `case.py` with `CaseProfile` dataclass:
  - `case_type`
  - `questionnaire_fields`

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

- Add validation and normalization for profile field values.
- Expand case attributes that influence juror scoring.
- Build a scoring function with transparent rule-based output.
- Introduce tests for profile validation and scoring logic.
