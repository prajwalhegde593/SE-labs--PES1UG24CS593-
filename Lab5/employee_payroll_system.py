"""Employee payroll computation and salary disbursement module."""

import hashlib
import json
import secrets
from pathlib import Path
from typing import Dict, List, Optional

PayrollRecord = Dict[str, object]

PAYROLL_RECORDS: Dict[str, PayrollRecord] = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}


def process_salary(
    emp_id: str,
    bonus: float,
    transaction_logs: Optional[List[str]] = None,
) -> bool:
    """Credit a non-negative bonus and record the transaction."""
    if emp_id not in PAYROLL_RECORDS or bonus < 0:
        return False

    if transaction_logs is None:
        transaction_logs = []

    PAYROLL_RECORDS[emp_id]["base_salary"] = (
        float(PAYROLL_RECORDS[emp_id]["base_salary"]) + bonus
    )
    transaction_logs.append(
        f"Credited bonus {bonus:.2f} to employee id {emp_id}"
    )
    return True


def deduct_penalty(emp_id: str, penalty: float) -> bool:
    """Deduct a non-negative penalty from a known employee's base salary."""
    if emp_id not in PAYROLL_RECORDS or penalty < 0:
        return False

    current_salary = float(PAYROLL_RECORDS[emp_id]["base_salary"])
    if penalty > current_salary:
        return False

    PAYROLL_RECORDS[emp_id]["base_salary"] = current_salary - penalty
    return True


def check_bonus_eligibility(emp_id: str, min_base: float = 4000.0) -> bool:
    """Return whether a known employee meets the salary threshold."""
    record = PAYROLL_RECORDS.get(emp_id)
    if record is None:
        return False
    return float(record["base_salary"]) >= min_base


def compute_net_salary(
    emp_id: str,
    deduction_rate: Optional[float] = None,
) -> float:
    """Compute net salary using the employee's tax rate or a validated rate."""
    record = PAYROLL_RECORDS.get(emp_id)
    if record is None:
        raise ValueError(f"Unknown employee ID: {emp_id}")

    base_salary = float(record["base_salary"])
    tax_rate = (
        float(record["tax_rate"])
        if deduction_rate is None
        else deduction_rate
    )
    if not 0.0 <= tax_rate <= 1.0:
        raise ValueError("Deduction rate must be between 0 and 1.")

    return round(base_salary * (1.0 - tax_rate), 2)


def generate_employee_hash(emp_id: str) -> str:
    """Return a stable SHA-256 digest for an employee identifier."""
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_payroll_token() -> str:
    """Generate a cryptographically secure, four-digit payroll token."""
    return f"{secrets.randbelow(9000) + 1000}"


def export_payroll_sheet(filename: str = "payroll_sheet.json") -> Path:
    """Export payroll records as JSON and return the output path."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(PAYROLL_RECORDS, output_file, indent=2)
        output_file.write("\n")
    return output_path


def main() -> None:
    """Run a small demonstration of the payroll functions."""
    process_salary("EMP101", 350.0)
    deduct_penalty("EMP102", 100.0)

    print("Is EMP101 eligible:", check_bonus_eligibility("EMP101"))
    print("Net salary:", compute_net_salary("EMP101"))
    print("Employee Hash:", generate_employee_hash("EMP101"))
    print("Payroll Token:", generate_payroll_token())
    print("Payroll summary exported to:", export_payroll_sheet())


if __name__ == "__main__":
    main()
