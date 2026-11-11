import math

from hypothesis import given, settings, strategies as st
from scholarship_awards import parse_applicant, marks_average, payable_award

# Number-like text, including the special values float() accepts.
number_text = st.one_of(
    st.from_regex(r"\A-?[0-9]{0,6}(\.[0-9]{0,3})?\Z"),
    st.floats(allow_nan=True, allow_infinity=True).map(str),
    st.sampled_from(["nan", "inf", "-inf", "1e999", "1_000", " 5 "]),
)
# Text built from the separators the functions split on, so the fuzzer hits
# near-valid input such as ":", "a:b:c", "1,,2" or "5000|".
separator_text = st.from_regex(r"\A[a-z0-9 .:,|-]{0,12}\Z")
any_input = st.text() | st.none() | separator_text


def is_valid_marks(m):
    return isinstance(m, (int, float)) and math.isfinite(m) and 0 <= m <= 100


# ------------------------------------------------------------ parse_applicant
@settings(max_examples=500)
@given(any_input)
def test_parse_applicant_no_crash(s):
    try:
        result = parse_applicant(s)
    except Exception as e:
        assert False, f"parse_applicant crashed with: {e!r}"
    # Either rejected (None) or a named category with marks from 0 to 100.
    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
        and isinstance(result[0], str) and result[0] != ""
        and is_valid_marks(result[1])
    )


@settings(max_examples=300)
@given(st.sampled_from(["merit", "sports", "arts", "", " "]), number_text)
def test_parse_applicant_marks_in_range(category, marks):
    try:
        result = parse_applicant(f"{category}:{marks}")
    except Exception as e:
        assert False, f"parse_applicant crashed with: {e!r}"
    assert result is None or is_valid_marks(result[1]), f"accepted marks {result[1]!r}"


@given(st.sampled_from(["merit", "sports", "arts"]),
       st.integers(min_value=0, max_value=100))
def test_parse_applicant_valid(category, marks):
    assert parse_applicant(f" {category} : {marks}") == (category.title(), marks)


# -------------------------------------------------------------- marks_average
@settings(max_examples=500)
@given(any_input)
def test_marks_average_no_crash(s):
    try:
        result = marks_average(s)
    except Exception as e:
        assert False, f"marks_average crashed with: {e!r}"
    # Either rejected (None) or an average that is itself a valid mark.
    assert result is None or is_valid_marks(result)


@settings(max_examples=300)
@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1, max_size=6))
def test_marks_average_rejects_out_of_range(values):
    csv = ",".join(str(v) for v in values)
    try:
        result = marks_average(csv)
    except Exception as e:
        assert False, f"marks_average crashed with: {e!r}"
    if all(0 <= v <= 100 for v in values):
        assert result == sum(values) // len(values)
    else:
        assert result is None, f"accepted out-of-range marks {values}"


# -------------------------------------------------------------- payable_award
@settings(max_examples=500)
@given(any_input)
def test_payable_award_no_crash(s):
    try:
        result = payable_award(s)
    except Exception as e:
        assert False, f"payable_award crashed with: {e!r}"
    assert result is None or (isinstance(result, (int, float))
                              and math.isfinite(result) and result >= 0)


@settings(max_examples=300)
@given(number_text, number_text)
def test_payable_award_is_finite_and_non_negative(award, deduction):
    try:
        result = payable_award(f"{award}|{deduction}")
    except Exception as e:
        assert False, f"payable_award crashed with: {e!r}"
    assert result is None or (math.isfinite(result) and result >= 0), \
        f"payable_award returned {result!r}"


@given(st.integers(min_value=0, max_value=100000),
       st.integers(min_value=0, max_value=100000))
def test_payable_award_valid(award, deduction):
    expected = max(round(award * 1.18 - deduction, 2), 0)
    assert payable_award(f"{award}|{deduction}") == expected
