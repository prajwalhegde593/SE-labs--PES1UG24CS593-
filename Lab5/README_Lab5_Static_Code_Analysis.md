# Lab 5 — Static Code Analysis

## Overview

This lab applies static code analysis to the **Employee Payroll System** using three Python code-quality and security tools:

- **Bandit** — identifies common security issues in Python code.
- **Pylint** — checks code quality, potential bugs, naming, documentation, and maintainability.
- **Flake8** — checks Python style and formatting, including PEP 8 violations.

The objective is to analyze the starter code, document the initial findings, fix the reported issues, and retain before-and-after reports to demonstrate the improvements.

## Repositories

- **Assigned starter repository:** https://github.com/SETAPESU26/L5_44_employee_payroll_system
- **Submission repository:** https://github.com/prajwalhegde593/SE-labs--PES1UG24CS593-

## Project Structure

The repository should contain the original project files and the following lab deliverables. Adjust report filenames to match the files actually saved in your repository.

```text
Lab5/
├── employee_payroll_system.py
├── README.md
├── bandit_before.txt
├── bandit_after.txt
├── pylint_before.txt
├── pylint_after_bandit.txt
├── flake8_before.txt
└── flake8_after_pylint.txt
```

Keep only report files you actually generated. Do not create empty or fabricated reports to match this example.

## Tools and Requirements

- Python 3
- A virtual environment (`venv` or `.venv`) is recommended
- Bandit
- Pylint
- Flake8

Install the tools in your active virtual environment:

```powershell
python -m pip install bandit pylint flake8
```

On Windows PowerShell, activate the environment first if needed:

```powershell
.\.venv\Scripts\Activate.ps1
```

If your environment directory is named `venv`, use `.\venv\Scripts\Activate.ps1` instead.

## Running the Analysis

Run commands from the directory containing `employee_payroll_system.py`.

### 1. Bandit — Security Analysis

Generate a baseline report:

```powershell
python -m bandit -r employee_payroll_system.py -f txt -o bandit_before.txt
```

After applying security fixes, generate the updated report:

```powershell
python -m bandit -r employee_payroll_system.py -f txt -o bandit_after.txt
```

Review the findings and confirm the updated report no longer contains the issues identified in the baseline. A clean report does not prove that the program is completely secure; it means Bandit did not report findings under that run's configuration.

### 2. Pylint — Code Quality

Generate the baseline report:

```powershell
python -m pylint employee_payroll_system.py > pylint_before.txt 2>&1
```

After improving the code, generate the updated report:

```powershell
python -m pylint employee_payroll_system.py > pylint_after.txt 2>&1
```

Review the final score and verify that the fixes preserve intended behavior. During this lab, the reported Pylint score reached **10.00/10**.

### 3. Flake8 — Style and Formatting

Generate the baseline report:

```powershell
python -m flake8 employee_payroll_system.py > flake8_before.txt 2>&1
```

After formatting fixes, generate the updated report:

```powershell
python -m flake8 employee_payroll_system.py > flake8_after.txt 2>&1
```

An empty output file indicates that Flake8 reported no violations for this file with the installed configuration. Confirm the command's result and inspect the report before recording the outcome.

## Issues Addressed

The initial analysis identified issues in the following areas:

| Tool | Finding / issue category | Corrective action |
|---|---|---|
| Bandit | Use of `eval()` | Replace dynamic evaluation with explicit, validated calculations. |
| Bandit | MD5 used for a digest | Use SHA-256 for the employee identifier digest where a cryptographic digest is needed. |
| Bandit | `random.randint()` used for a security-sensitive value | Use a security-oriented source such as `secrets` when unpredictability is required. |
| Bandit | Shell command execution through `os.system()` | Avoid shell execution when a direct Python operation is sufficient. |
| Bandit | Broad exception handling / silent failure | Validate inputs and handle expected exceptions explicitly. |
| Pylint | Missing function docstrings | Add concise docstrings describing function behavior. |
| Pylint | Non-standard function naming | Use `snake_case` for function names and update call sites. |
| Pylint | Mutable default argument | Use `None` as the default and create a new list inside the function when needed. |
| Pylint | Comparison with `None` | Use identity checks such as `value is None`. |
| Pylint | Unused variables and imports | Remove unused names when they are not required. |
| Pylint | File handling and encoding | Use a context manager and specify an appropriate encoding. |
| Flake8 | Line too long (`E501`) | Split the statement across multiple lines without changing behavior. |
| Flake8 | Trailing whitespace (`W291`) | Remove spaces at the ends of affected lines. |

This table summarizes the categories encountered during the lab. Keep only the fixes present in your final source code, and adjust descriptions to match your actual implementation.

## Validation

After all changes, run the tools again:

```powershell
python -m bandit -r employee_payroll_system.py
python -m pylint employee_payroll_system.py
python -m flake8 employee_payroll_system.py
```

Also run the payroll program with the test inputs supplied by your lab or project. Static analysis does not replace functional testing.

## Commit History

Keep the changes in separate stages so the progression is clear:

1. **Bandit stage** — fix security findings and save the updated Bandit report.
2. **Pylint stage** — improve code quality and documentation, then save the updated Pylint report.
3. **Flake8 stage** — fix style and formatting findings, then save the updated Flake8 report.

Suggested commit messages:

```text
Fix security issues identified by Bandit
Improve code quality based on Pylint
Fix Flake8 formatting issues
```

Inspect the commit history with:

```powershell
git log --oneline
```

## Reflection

This lab demonstrates that static analysis tools serve different but complementary purposes. Bandit focuses on common security risks, Pylint highlights code-quality and maintainability concerns, and Flake8 enforces style and formatting rules. Running the tools iteratively makes problems easier to isolate and allows each set of changes to be reviewed independently.

A clean static-analysis report is not a guarantee that the application is bug-free or secure. The final code should still be tested for correct payroll calculations, valid input handling, and expected behavior.

## Notes

- Do not commit the virtual environment. Add `.venv/` and/or `venv/` to `.gitignore`.
- Preserve the original source behavior unless a change is needed to correct a demonstrated issue.
- Keep before-and-after reports generated from the actual source code.
- Ensure the README, reports, and commit history match the files submitted in the repository.
