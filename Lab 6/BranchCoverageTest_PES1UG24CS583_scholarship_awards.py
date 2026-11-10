"""Lab 6 - branch coverage tests for scholarship_awards.py.

Goal: take every decision (if) in scholarship_awards.py both ways (True
and False), and exercise each part of the compound condition and the
boundary values around each cutoff.

Run:
    coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS583_scholarship_awards.py
    coverage report -m
"""
import pytest
from scholarship_awards import award_amount, is_eligible, application_status


# -------------------------------------------------------------- award_amount
# if category not in CUTOFF_MARKS / if marks < 0  ->  True (error) and False
@pytest.mark.parametrize("category, marks", [
    ("music", 80),
    ("", 80),
    ("Merit", 80),     # category names are case-sensitive
    ("merit", -1),
    ("sports", -10),
])
def test_invalid_input_rejected(category, marks):
    with pytest.raises(ValueError):
        award_amount(category, marks, "low", False)


# if above <= 0  ->  True: no award (at and below each cutoff)
@pytest.mark.parametrize("category, marks, is_renewal", [
    ("merit", 0, False),
    ("merit", 70, False),
    ("merit", 75, False),     # exactly at cutoff
    ("sports", 60, False),
    ("arts", 65, False),
    ("merit", 70, True),      # renewal cutoff 70, exactly at it
    ("sports", 60, True),     # sports keeps cutoff 60 on renewal
])
def test_no_award_at_or_below_cutoff(category, marks, is_renewal):
    assert award_amount(category, marks, "low", is_renewal) == 0


# if is_renewal and category != "sports"
@pytest.mark.parametrize("category, marks, is_renewal, expected", [
    ("merit", 80, True, 10 * 100),    # True and True  -> cutoff 70
    ("arts", 70, True, 10 * 100),     # True and True  -> cutoff 60
    ("sports", 70, True, 10 * 100),   # True and False -> cutoff stays 60
    ("merit", 80, False, 5 * 100),    # False          -> cutoff stays 75
])
def test_renewal_cutoff(category, marks, is_renewal, expected):
    assert award_amount(category, marks, "low", is_renewal) == expected


# income_level == "low"  and  above > 15  (with the nested low-income bonus)
@pytest.mark.parametrize("marks, income_level, expected", [
    (76, "low", 1 * 100),        # above 1,  low:  rate 100
    (76, "medium", 1 * 60),      # above 1,  not low: rate 60
    (90, "low", 15 * 100),       # above 15: no bonus (boundary)
    (90, "high", 15 * 60),
    (91, "low", 16 * 160),       # above 16: 100 + 40 + 20
    (91, "medium", 16 * 100),    # above 16: 60 + 40, no low-income bonus
    (100, "high", 25 * 100),
])
def test_award_rates(marks, income_level, expected):
    assert award_amount("merit", marks, income_level, False) == expected


# --------------------------------------------------------------- is_eligible
@pytest.mark.parametrize("attendance, backlogs, special, expected", [
    # special quota: only backlogs matter (<= 2)
    (50, 2, True, True),
    (50, 3, True, False),
    (90, 0, True, True),
    # normal: attendance >= 75 and backlogs <= 1
    (74, 0, False, False),       # just below attendance cutoff
    (75, 0, False, True),        # exactly at attendance cutoff
    (90, 1, False, True),
    (90, 2, False, False),
    (60, 5, False, False),
])
def test_is_eligible(attendance, backlogs, special, expected):
    assert is_eligible(attendance, backlogs, special) is expected


# -------------------------------------------------------- application_status
# cutoff: renewal 30 / new 20, +10 if paper; "closing" within 15 days below
@pytest.mark.parametrize("days_left, is_renewal, is_paper, expected", [
    (20, False, False, "open"),      # new, online: cutoff 20 (boundary)
    (19, False, False, "closing"),
    (5, False, False, "closing"),    # cutoff - 15 boundary
    (4, False, False, "closed"),
    (30, True, False, "open"),       # renewal, online: cutoff 30
    (15, True, False, "closing"),
    (14, True, False, "closed"),
    (30, False, True, "open"),       # new, paper: cutoff 30
    (29, False, True, "closing"),
    (14, False, True, "closed"),
    (40, True, True, "open"),        # renewal, paper: cutoff 40
    (25, True, True, "closing"),
    (24, True, True, "closed"),
    (0, False, False, "closed"),
])
def test_application_status(days_left, is_renewal, is_paper, expected):
    assert application_status(days_left, is_renewal, is_paper) == expected
