# Lab 6 — Code and Branch Coverage Analysis: `scholarship_awards.py`

Tools: pytest 9.2.0, coverage.py 7.17.0. Figures are for `scholarship_awards.py` (37 statements, 26 branches).

## Summary

| Stage | Test file | Tests | Line coverage | Branch coverage | Missing |
|-------|-----------|------:|--------------:|----------------:|---------|
| Starter | `test_scholarship_awards.py` | 2 | 38% | 32% | lines 6, 8, 11, 15–23, 28, 30, 35–45 |
| Code coverage | `CodeCoverageTest_PES1UG24CS583_scholarship_awards.py` | 12 | **100%** | 98% | branch 21→23 |
| Branch coverage | `BranchCoverageTest_PES1UG24CS583_scholarship_awards.py` | 45 | **100%** | **100%** | none |

Screenshots (in [`deliverables/`](deliverables/)):

| | Before (starter tests) | After |
|---|---|---|
| Code (line) coverage | [`screenshot_code_coverage_before.png`](deliverables/screenshot_code_coverage_before.png) (38%) | [`screenshot_code_coverage_after.png`](deliverables/screenshot_code_coverage_after.png) (100%) |
| Branch coverage | [`screenshot_branch_coverage_before.png`](deliverables/screenshot_branch_coverage_before.png) (32%) | [`screenshot_branch_coverage_after.png`](deliverables/screenshot_branch_coverage_after.png) (100%) |

## Step 1: starter tests (38% line, 32% branch)

The starter tests check only one below-cutoff award and one normal eligible student. They never reach:
- the error checks (unknown category, negative marks)
- the renewal cutoff and the income-based rates
- special-quota and low-attendance eligibility
- `application_status`, at all

## Step 2: code (line) coverage, 100% lines but 98% branches

`CodeCoverageTest_…` has one test per typical outcome:

- **`award_amount`:** below cutoff, unknown category, negative marks, renewal cutoff, a non-low income rate, and high marks with the low-income bonus.
- **`is_eligible`:** normal eligible, special quota, low attendance.
- **`application_status`:** open (renewal), closing (new), closed (paper).

Every line runs, so **line coverage is 100%**. Run with `--branch`, the same tests give **98%** and report one missing branch, **21→23**:

```python
if above > 15:
    rate = rate + 40
    if income_level == "low":   # line 21
        rate += 20              # line 22
return above * rate             # line 23
```

The only high-marks test used a **low** income, so the inner `if` on line 21 was never False. Nothing checked that a non-low-income student with high marks gets 100 per mark, not 120. Line coverage cannot show this, because no line is skipped; only a branch is. It's the same situation as the handout's `calculate_discount` example.

## Step 3: branch coverage, 100%

`BranchCoverageTest_…` takes **every decision both ways** and tests the values right at each cutoff:

| Function | Decision | True / False cases |
|----------|----------|--------------------|
| `award_amount` | `category not in CUTOFF_MARKS` | "music", "", "Merit" (case-sensitive) / merit, sports, arts |
| | `marks < 0` | -1, -10 / 0 and above |
| | `is_renewal and category != "sports"` | merit/arts renewal (True) / sports renewal (second part False), not renewal (first part False) |
| | `above <= 0` | exactly at cutoff (75, 60, 65, renewal 70) / 1 mark above |
| | `income_level == "low"` | "low" / "medium", "high" |
| | `above > 15` | 16 or more above / exactly 15 above (boundary) |
| | `income_level == "low"` (inside `above > 15`) | low → rate 160 / **medium → rate 100 (the missed branch 21→23)** |
| `is_eligible` | `is_special_quota` | 2 backlogs eligible, 3 not / normal students |
| | `attendance < 75` | 74 / exactly 75 |
| | `backlogs <= 1` / `backlogs <= 2` | at and just over each limit |
| `application_status` | `is_renewal`, `is_paper` | all four combinations: cutoffs 20, 30, 30, 40 |
| | `days_left >= cutoff` | exactly at each cutoff / one day below |
| | `days_left >= cutoff - 15` | exactly 15 below the cutoff (closing) / 16 below (closed) |

## Observations

- **100% line coverage was not complete testing.** The code-coverage tests ran every line but missed a whole rule: there is no low-income bonus for other income levels. Branch coverage found it immediately.
- **Branch coverage is not condition coverage.** coverage.py treats `is_renewal and category != "sports"` as one decision. The branch tests also make each part False on its own (sports renewal; non-renewal), which coverage.py does not report separately.
- **Boundary values** (exactly at the cutoff, exactly 15 above it, 75% attendance, 1 vs 2 backlogs, the closing window) found no failures. All 45 tests pass.
- **Behaviour worth confirming with the spec:** category names are case-sensitive (`"Merit"` raises `ValueError`), and any income level other than `"low"` (including misspellings) gets the standard rate.

## Commands

```
coverage run -m pytest test_scholarship_awards.py
coverage report -m
coverage run --branch -m pytest test_scholarship_awards.py
coverage report -m

coverage run -m pytest CodeCoverageTest_PES1UG24CS583_scholarship_awards.py
coverage report -m

coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS583_scholarship_awards.py
coverage report -m
```
