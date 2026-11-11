# L6_L7_44 — Scholarship Awards

Lab 7: Fuzz Testing

## About

A small Python module that parses applicant records, averages marks and works out the payable award after a deduction.

## Files

| File | Description |
|------|-------------|
| `scholarship_awards.py` | The code under test |
| `test_scholarship_awards.py` | Starter test file |

Refer to the lab handout for instructions.

---

## Lab 7 submission

| | |
|---|---|
| **Student** | Prajwal Hegde · SRN PES1UG24CS593 |
| **My repo (fork of the assigned repo)** | `https://github.com/<github-username>/L6_L7_44_scholarship_awards` |
| **Assigned repo** | [github.com/SETAPESU26/L6_L7_44_scholarship_awards](https://github.com/SETAPESU26/L6_L7_44_scholarship_awards) |
| **Tools** | Python 3 · Hypothesis · pytest |

### Deliverables

| # | Deliverable | File |
|---|-------------|------|
| 1 | PDF document with the screenshots | [`Lab7_FuzzTesting_Screenshots.pdf`](Lab7_FuzzTesting_Screenshots.pdf) |
| 2 | Fixed application script | [`scholarship_awards.py`](scholarship_awards.py) |
| 3 | Updated test file (Hypothesis) | [`test_scholarship_awards.py`](test_scholarship_awards.py) |

The individual screenshots are also in [`deliverables/`](deliverables/), one per step (2, 4, 5, 6).

### Result

| Run | Buggy code | Fixed code |
|-----|-----------|------------|
| `python scholarship_awards.py` with invalid input | Crashes with a traceback | Prints "Invalid input…" and continues |
| `pytest test_scholarship_awards.py` (8 Hypothesis tests) | **7 failed**, 1 passed | **8 passed** |

### Bugs found by fuzzing

| Function | Failing input | Problem |
|----------|---------------|---------|
| `parse_applicant` | `''`, `':'`, `None` | Crash (ValueError, AttributeError) |
| `parse_applicant` | `'merit:101.0'` | Marks over 100 accepted |
| `marks_average` | `''`, `None` | Crash (ValueError, AttributeError) |
| `marks_average` | `'-1'` | Negative marks accepted |
| `payable_award` | `''`, `'\|'`, `None` | Crash (ValueError, AttributeError) |
| `payable_award` | `'0\|nan'` | Returns `nan` |
| `payable_award` | `'1\|1'` | Returns `0.17999999999999994` instead of `0.18` |

### Fixes

- Every function returns `None` for input it cannot interpret instead of crashing: non-strings, the wrong number of parts, and empty or invalid values.
- Numbers must be plain ASCII decimals. This rejects signs, `nan`, `inf`, `1e999`, `1_000` and Unicode digits.
- Marks must be 0–100; category must be letters.
- `payable_award` rounds to 2 decimal places and never returns less than 0.0.
- `main()` prints a clear "Invalid input" message instead of crashing, and stops cleanly if input ends.

### How to run

```powershell
pip install hypothesis pytest

python scholarship_awards.py
python -m pytest test_scholarship_awards.py -v
```
