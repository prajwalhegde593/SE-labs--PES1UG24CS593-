# Static Analysis Findings — Employee Payroll System

Line numbers below refer to the **original** `employee_payroll_system.py` in the assigned repository. Exact tool messages can vary slightly by tool version; run the baseline commands to capture your actual reports.

| Issue | Type | Original line(s) | Description / risk | Fix approach |
|---|---|---:|---|---|
| Dynamic `eval()` | Security (high) | 388–394, especially 392 | Evaluating a string as Python code can execute attacker-controlled expressions. Bandit commonly flags this as B307. | Removed `eval`; accept a numeric deduction rate and validate it is between 0 and 1. |
| Shell command built from filename | Security (medium) | 404–412, especially 412 | `os.system()` concatenates user-controlled filename data into a shell command, creating command-injection risk. Bandit may flag B605. | Removed shell execution; use `pathlib.Path` for file output and print a status message. |
| Hard-coded secret | Security (medium) | 414–431, especially 415 and 431 | A master secret is embedded in source and printed to the console. This exposes a credential and is not needed by the demonstration. | Removed the hard-coded secret and its print statement. |
| Weak MD5 digest | Security / cryptography | 396–398 | MD5 is not appropriate when a cryptographic hash is required. Bandit may flag B324 depending on context/version. | Replaced MD5 with SHA-256. Note: hashing an employee ID is not authentication or password storage. |
| Mutable default argument | Correctness / maintainability | 352 | `transaction_logs=[]` is shared between calls, so data can unexpectedly persist between invocations. | Default to `None` and create a fresh list when needed. |
| Bare `except` and swallowed error | Correctness | 363–371 | The code catches every exception and silently ignores failures, hiding bugs and invalid employee IDs. | Validate employee ID and penalty, return `False` on invalid input, and make successful deductions explicit. |
| `== None` comparison | Style / correctness | 377 | PEP 8 recommends identity comparison with `is None`. | Use a dictionary lookup and `record is None`. |
| Unused imports and variable | Style / maintainability | 338, 340, 375 | `math` and `statutory_buffer` are unused; unused code adds noise. | Removed unused import and variable. |
| File opened without a context manager | Reliability | 404–410 | If writing raises an exception, the file may not be closed cleanly. | Use `with Path.open(...)` so the file is closed reliably. |
| Non-cryptographic random token | Security | 400–402 | `random` is not designed for security-sensitive tokens. | Use `secrets` to generate a token. |
| Naming, formatting, and missing documentation | Style | Throughout | CamelCase function name, inconsistent blank lines, and missing docstrings trigger style/quality warnings. | Use snake_case, docstrings, type hints, and consistent formatting. |

## Verification notes

- The updated code removes the unsafe `eval()` and shell-command execution patterns, fixes the mutable default, removes the embedded secret, validates salary inputs, and improves file handling.
- Line numbers in the reports will differ after editing.
- Do not claim a specific final Pylint score until you run Pylint locally and save its actual output.
