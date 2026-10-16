# Lab 5 — Static Code Analysis

https://github.com/prajwalhegde593/SE-labs--PES1UG24CS593-.git

## Files
- `employee_payroll_system.py`: cleaned implementation based on the assigned repository's original script.
- `issues.md`: issue table and fixes.
- `reflection.md`: reflection answers.
- `reports/`: placeholders explaining how to capture genuine before/after tool output.

## Run in Windows PowerShell
Open this folder in VS Code, then run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8
python employee_payroll_system.py
```

If PowerShell blocks activation, use Command Prompt and run:
```bat
.venv\Scripts\activate.bat
```

## Capture baseline reports
Before replacing the original script, run the tools against the original file and save the reports:
```powershell
python -m pylint employee_payroll_system.py *> reports\before_pylint.txt
python -m bandit -r employee_payroll_system.py *> reports\before_bandit.txt
python -m flake8 employee_payroll_system.py *> reports\before_flake8.txt
```

## Capture final reports
After copying the cleaned script into the repository:
```powershell
python -m pylint employee_payroll_system.py *> reports\after_pylint.txt
python -m bandit -r employee_payroll_system.py *> reports\after_bandit.txt
python -m flake8 employee_payroll_system.py *> reports\after_flake8.txt
```
These commands capture the actual output from your installed versions. Do not submit placeholder text as tool output.

## Suggested three commits
Make each commit after the relevant changes and reports have been checked:
```bash
git add employee_payroll_system.py reports/before_bandit.txt reports/after_bandit.txt
git commit -m "Fix security issues identified by Bandit"

git add employee_payroll_system.py reports/before_pylint.txt reports/after_pylint.txt
git commit -m "Improve code quality based on Pylint"

git add employee_payroll_system.py reports/before_flake8.txt reports/after_flake8.txt issues.md reflection.md
git commit -m "Apply Flake8 style fixes and document lab findings"
```
For a clearer history, ideally make each commit contain only that tool's relevant changes, rather than staging the same final file for every commit. The commands above are a simple outline; use `git add -p` if your instructor expects genuinely separate, incremental commits.

