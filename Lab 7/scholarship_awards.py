"""Scholarship award helpers, hardened against invalid input.

Every function returns None for input it cannot interpret, instead of
crashing or returning a meaningless value (nan, inf, negative marks), so
callers (and main) can report the problem to the user.
"""
import re

GST_RATE = 1.18
MAX_MARKS = 100

# Plain ASCII decimal numbers only: rejects '', signs, exponents ('1e999'),
# 'nan', 'inf', underscores ('1_000') and non-ASCII digits, all of which
# float()/int() would otherwise accept or crash on.
MARKS_PATTERN = re.compile(r"[0-9]{1,3}(\.[0-9]{1,2})?")
INT_MARKS_PATTERN = re.compile(r"[0-9]{1,3}")
AMOUNT_PATTERN = re.compile(r"[0-9]{1,9}(\.[0-9]{1,2})?")


def _split_two(text, sep):
    """Split text on sep into exactly two stripped parts, or return None."""
    if not isinstance(text, str):
        return None
    parts = text.split(sep)
    if len(parts) != 2:
        return None
    return parts[0].strip(), parts[1].strip()


def parse_applicant(text):
    """Parse 'category:marks' into (Category, marks); None if invalid."""
    pair = _split_two(text, ':')
    if pair is None:
        return None
    category, marks_text = pair
    # Category: one or more words made of letters only.
    if not category or not category.replace(" ", "").isalpha():
        return None
    if not MARKS_PATTERN.fullmatch(marks_text):
        return None
    marks = float(marks_text)
    if marks > MAX_MARKS:
        return None
    return category.title(), marks


def marks_average(marks_csv):
    """Whole-number average of marks such as '72,85,90'; None if invalid."""
    if not isinstance(marks_csv, str):
        return None
    values = []
    for part in marks_csv.split(','):
        part = part.strip()
        if not INT_MARKS_PATTERN.fullmatch(part):
            return None
        value = int(part)
        if value > MAX_MARKS:
            return None
        values.append(value)
    return sum(values) // len(values)


def payable_award(text):
    """Award plus 18% minus deduction for 'award|deduction', never below 0; None if invalid."""
    pair = _split_two(text, '|')
    if pair is None:
        return None
    award_text, deduction_text = pair
    if not (AMOUNT_PATTERN.fullmatch(award_text) and AMOUNT_PATTERN.fullmatch(deduction_text)):
        return None
    total = round(float(award_text) * GST_RATE - float(deduction_text), 2)
    return max(total, 0.0)


def _ask(prompt):
    """Read one line of input; None if input has ended (e.g. Ctrl+Z / Ctrl+D)."""
    try:
        return input(prompt)
    except EOFError:
        return None


def main():
    print("==== Running parse_applicant ====")
    user_input = _ask("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    if result is None:
        print("Invalid input: expected a category and marks from 0 to 100 like merit:82.")
    else:
        print("Category and Marks:", result)

    print("\n==== Running marks_average ====")
    user_input = _ask("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    if result is None:
        print("Invalid input: expected whole marks from 0 to 100 separated by commas like 72,85,90.")
    else:
        print("Average Marks:", result)

    print("\n==== Running payable_award ====")
    user_input = _ask("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    if result is None:
        print("Invalid input: expected two non-negative amounts like 5000|500.")
    else:
        print("Payable Award:", result)


if __name__ == "__main__":
    main()
