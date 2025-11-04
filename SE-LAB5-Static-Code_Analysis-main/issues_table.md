# Issues Identified and Fixes — Lab 5: Static Code Analysis

| Issue Type | Tool | Line No. (Original) | Description | Fix Applied |
|-------------|------|---------------------|--------------|--------------|
| Dangerous default argument | Pylint | 8 | Used a mutable default list `logs=[]` which can cause shared data between calls | Changed to `logs=None` and initialized inside function |
| Insecure use of `eval()` | Bandit | 59 | Use of `eval()` poses a security risk | Removed `eval()` completely and replaced with safe JSON handling |
| Bare `except:` used | Bandit / Pylint | 19 | Generic exception hides real errors | Replaced with specific exception `except (KeyError, ValueError) as err:` |
| Global variable misuse | Pylint | 49 | `global stock_data` used unnecessarily | Removed `global` and passed/loaded data locally via helper functions |
| Missing docstrings | Pylint | Multiple | Functions lacked docstrings | Added clear, PEP 257-compliant docstrings for all functions |
| Improper naming convention | Pylint / Flake8 | Multiple | Function names like `addItem`, `removeItem` not in snake_case | Renamed all to snake_case (e.g., `add_item`, `remove_item`) |
| File operations missing encoding | Pylint | 26, 32 | `open()` used without specifying encoding | Used `with open(..., encoding='utf-8')` for safety |
| Long lines (E501) | Flake8 | 76, 101 | Lines exceeded 79 characters | Wrapped text and split lines to meet PEP 8 length requirement |
| Unused imports | Flake8 / Pylint | 2 | `logging` was imported but not used | Removed the unused import |
| No input validation | Manual review | Multiple | Functions accepted invalid types for item and qty | Added type checks for item (str) and qty (int/float) |

---

### ✅ Summary
- **Tools Used:** Pylint, Flake8, Bandit  
- **Initial Score:** 4.8 / 10  
- **Final Score:** 10.00 / 10  
- **Total Issues Fixed:** 10  
- **Result:** All warnings and security issues resolved. Code is now PEP 8-compliant, secure, and well-documented.
