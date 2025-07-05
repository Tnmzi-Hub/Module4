# 🧮 Python Math Operations

This repository contains simple Python scripts demonstrating basic mathematical operations and recursive functions using the built-in `math` module and recursion techniques.

---

## 📄 Files & Descriptions

### 1. `math_ops.py`
A terminal-based script that:
- Prompts the user for a positive number.
- Calculates and displays:
  - ✅ Square root of the number
  - ✅ Natural logarithm (log base _e_)
  - ✅ Sine of the number in radians

🔐 **Input validation** is included to ensure the number is greater than zero, as required by `sqrt` and `log`.

---

### 2. `factorial.py`
This script:
- Calculates the factorial of a user-input integer using **recursion**.
- Handles edge cases:
  - ❗ Returns a message if the input is negative.
  - ✅ Correctly handles `0!` and `1!` by returning 1.

---

## 💡 Example Usage

### `math_ops.py`
```bash
Enter a number: 4
Square root of number: 2.0
Natural Log: 1.3862943611198906
Sine in radians: -0.7568024953079282

