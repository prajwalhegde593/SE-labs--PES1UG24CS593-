"""Lab 6 - code (line) coverage tests for scholarship_awards.py.

Goal: execute at least 90% of the statements in scholarship_awards.py.
One test per typical outcome of each function.

Run:
    coverage run -m pytest CodeCoverageTest_PES1UG24CS583_scholarship_awards.py
    coverage report -m
"""
import pytest
from scholarship_awards import award_amount, is_eligible, application_status


# -------------------------------------------------------------- award_amount
def test_below_cutoff_marks():
    assert award_amount("merit", 70, "low", False) == 0


def test_unknown_category_rejected():
    with pytest.raises(ValueError):
        award_amount("music", 80, "low", False)


def test_negative_marks_rejected():
    with pytest.raises(ValueError):
        award_amount("merit", -1, "low", False)


def test_renewal_lowers_cutoff():
    # merit cutoff 75 - 5 for renewal = 70; 80 marks -> 10 above, low rate 100
    assert award_amount("merit", 80, "low", True) == 1000


def test_other_income_rate():
    # arts cutoff 65; 70 marks -> 5 above, rate 60
    assert award_amount("arts", 70, "medium", False) == 300


def test_high_marks_low_income_bonus():
    # merit cutoff 75; 95 marks -> 20 above, rate 100 + 40 + 20 = 160
    assert award_amount("merit", 95, "low", False) == 3200


# --------------------------------------------------------------- is_eligible
def test_is_eligible():
    assert is_eligible(90, 0, False) is True


def test_special_quota_eligible():
    assert is_eligible(50, 2, True) is True


def test_low_attendance_not_eligible():
    assert is_eligible(60, 0, False) is False


# -------------------------------------------------------- application_status
def test_renewal_application_open():
    assert application_status(35, True, False) == "open"


def test_new_application_closing():
    assert application_status(10, False, False) == "closing"


def test_paper_application_closed():
    assert application_status(10, False, True) == "closed"
