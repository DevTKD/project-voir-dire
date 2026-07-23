# Project Voir Dire

**Voir dire** (vwar-DEER) is the legal process of questioning potential jurors to evaluate their suitability for trial.

`project-voir-dire` is a Python backend learning project that models the early scoring engine of a fictional jury consulting firm, **Prevail Analytics**.

## Project goal

Build an explainable, rule-based system that uses synthetic juror data and case context to estimate whether a juror may lean plaintiff-friendly or defense-friendly in a fictional civil trial.

The project is being developed incrementally, with a planned path toward an API layer, persistence, authentication, testing, and CI/CD.

## 🏁 Version 1 Complete

Version 1 of Project Voir Dire is now complete. This milestone marks the end of the initial rule-based scoring engine — a working, runnable prototype that takes a case context and juror profiles, evaluates answers against weighted questions, and produces an interpretable score with a visual output.

Version 2 will focus on expanding the system toward an API layer, persistence, authentication, testing, and CI/CD.

---

## Latest update

### July 23, 2026

- Added `main.py` as the full end-to-end demo entry point for Version 1:
  - Sets up the case **Caldwell v. Northbridge Medical Center** (`medical_malpractice`, retained by defense) with six weighted `CaseQuestion` entries.
  - Defines two juror profiles (`BasicProfile`) and their corresponding answer sets.
  - Introduced `display_score_bar()` — renders a normalized 0–100 bar with `█`/`░` fill and Defense / Neutral / Plaintiff axis labels.
  - Introduced `display_breakdown()` — prints each case question, the juror's answer, and whether the trigger matched with its weight.
  - Runs both evaluations and prints a formatted console report.
- Updated `scorer.py`:
  - Score now starts at `50` (neutral baseline) instead of `0`.
  - Final score is clamped to the range `[0, 100]`.
- Added `RetainingParty` enum to `case.py` (`PLAINTIFF` / `DEFENSE`) and wired it into `CaseProfile`.

## Changelog

### 2026-07-23

- Added `main.py` with full case setup, juror profiles, answer sets, score bar, and breakdown display.
- Added `RetainingParty` enum to `case.py`.
- Updated `scorer.py` to use a neutral baseline of `50` and clamp output to `[0, 100]`.
- Marked Version 1 as complete.

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
├── main.py
├── case.py
├── evaluation.py
├── juror.py
├── scorer.py
└── README.MD
```

## Version 2 milestones

- Wrap the scoring engine in a FastAPI layer.
- Add persistence (database storage for cases, jurors, and evaluations).
- Introduce authentication.
- Add validation and normalization for profile field values.
- Expand scoring rules beyond exact trigger-answer matches.
- Introduce tests for profile validation and scoring logic.
- Set up CI/CD pipeline.
