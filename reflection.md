 # Reflection — Lab 5: Static Code Analysis

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were the naming convention problems and missing docstrings. These only required small changes to make the code follow Python’s PEP 8 style guidelines. The hardest issues were the use of the `eval()` function and the global variable. Removing `eval()` required understanding that it could execute unsafe code, so I replaced it with secure data handling using JSON. Replacing the `global` keyword meant refactoring how the data was stored and passed between functions, which took more careful thought.

---

### 2. Did the static analysis tools report any false positives? If so, describe one example.
Yes, there were a few minor false positives. For example, Pylint flagged very small things like line length or indentation even though they didn’t affect program behavior. These were more about formatting rather than actual coding problems. However, fixing them still improved readability and consistency, making the code look cleaner and more professional.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?
I would integrate tools like **Pylint**, **Flake8**, and **Bandit** into a **Continuous Integration (CI)** pipeline using **GitHub Actions**. That way, every time new code is pushed, the repository automatically runs these tools and reports any issues. I would also set them up in my local development environment (such as VS Code or GitHub Codespaces) so that I can see warnings in real-time before committing my code.

---

### 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?
After applying the fixes, the code became much more organized, readable, and secure. I added proper docstrings, consistent function names, and safer file handling with encoding. The use of `with open()` improved reliability, and removing `eval()` eliminated potential security risks. The final Pylint score improved from **4.8/10 to 10.00/10**, showing a major enhancement in overall code quality, maintainability, and robustness.




