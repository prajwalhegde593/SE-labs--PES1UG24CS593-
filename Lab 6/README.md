# L6_L7_44 — Scholarship Awards

Lab 6: Code and Branch Coverage

## About

A small Python module that works out scholarship award amounts by category, marks, income level and renewal, checks applicant eligibility and reports application status.

## Files

| File | Description |
|------|-------------|
| `scholarship_awards.py` | The module under test |
| `test_scholarship_awards.py` | Starter test file |

Keep all your Lab 6 work in this `LAB6` folder. Lab 7 will be added to this repo later.

Refer to the lab handout for instructions.

---

## Lab 6 submission

| | |
|---|---|
| **Student** | Prajwal Hegde · SRN PES1UG24CS583 |
| **My repo (fork of the assigned repo)** | `https://github.com/<github-username>/L6_L7_44_scholarship_awards` |
| **Assigned repo** | [github.com/SETAPESU26/L6_L7_44_scholarship_awards](https://github.com/SETAPESU26/L6_L7_44_scholarship_awards) |
| **Tools** | Python 3 · pytest 9.2.0 · coverage 7.17.0 |

### Result (for `scholarship_awards.py`)

| Stage | Tests | Line coverage | Branch coverage |
|-------|------:|--------------:|----------------:|
| Starter tests (`test_scholarship_awards.py`) | 2 | 38% | 32% |
| Code coverage tests | 12 | **100%** | 98% |
| Branch coverage tests | 45 | **100%** | **100%** |

Both targets (at least 90% line coverage, and at least 90% branch coverage) are met. All tests pass.

### Deliverables

| Deliverable | File |
|-------------|------|
| Test cases for code (line) coverage | [`CodeCoverageTest_PES1UG24CS583_scholarship_awards.py`](CodeCoverageTest_PES1UG24CS583_scholarship_awards.py) |
| Test cases for branch coverage | [`BranchCoverageTest_PES1UG24CS583_scholarship_awards.py`](BranchCoverageTest_PES1UG24CS583_scholarship_awards.py) |
| Code coverage terminal output: **before** (starter tests, 38%) | [`deliverables/screenshot_code_coverage_before.png`](deliverables/screenshot_code_coverage_before.png) |
| Code coverage terminal output: **after** (`CodeCoverageTest_…`, 100%) | [`deliverables/screenshot_code_coverage_after.png`](deliverables/screenshot_code_coverage_after.png) |
| Branch coverage terminal output: **before** (starter tests, 32%) | [`deliverables/screenshot_branch_coverage_before.png`](deliverables/screenshot_branch_coverage_before.png) |
| Branch coverage terminal output: **after** (`BranchCoverageTest_…`, 100%) | [`deliverables/screenshot_branch_coverage_after.png`](deliverables/screenshot_branch_coverage_after.png) |
| Coverage analysis | [`coverage_analysis.md`](coverage_analysis.md) |

`scholarship_awards.py` and `test_scholarship_awards.py` are unchanged from the assigned repo.

### What the tests cover

- **Code coverage tests:** one test per typical outcome of each function. Every line runs (100% line coverage), but branch mode shows one branch was never taken: high marks with a non-low income (21→23).
- **Branch coverage tests:** every `if` is taken both True and False, including that missed branch. They also test values exactly at each cutoff (75/60/65 marks, renewal −5, 15 marks above, 75% attendance, backlog limits, the 15-day closing window) and make each part of the `and` condition False on its own.

See [`coverage_analysis.md`](coverage_analysis.md) for the full explanation.

### How to run

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pytest coverage

# before: starter tests
coverage run -m pytest test_scholarship_awards.py
coverage report -m
coverage run --branch -m pytest test_scholarship_awards.py
coverage report -m

# code (line) coverage
coverage run -m pytest CodeCoverageTest_PES1UG24CS583_scholarship_awards.py
coverage report -m

# branch coverage
coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS583_scholarship_awards.py
coverage report -m
```
