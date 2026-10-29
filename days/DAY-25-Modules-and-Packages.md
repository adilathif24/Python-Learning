# Day 25 — Modules and Packages

**Status:** Full study pack. Practice imports and run the project tests before marking mastery.

## 1. Definition
A **module** is a Python file that can define reusable variables, functions and classes. A **package** groups related modules under a common namespace. Imports allow code reuse and separation of responsibilities.

## 2. Why, where, when
Use modules to separate validation, calculations, persistence and application logic. Use packages when the project has several related modules. Keep modules small and cohesive; avoid circular imports and avoid executing a script's interactive main flow merely because another file imports it.

## 3. Syntax and rules
```python
import math
from pathlib import Path
from mymodule import add

if __name__ == "__main__":
    print("Run as a script")
```
Python searches import locations including the script directory and configured paths. The `__name__ == "__main__"` guard protects script-only behavior from running on import. Avoid naming your file after standard-library modules such as `json.py` or `random.py`.

## 4. Five worked examples
### Example 1 — Import a module
```import math
print(math.sqrt(81))
```
Output: `9.0`. Namespace prefix avoids ambiguity.

### Example 2 — Import a specific function
```from math import ceil
print(ceil(3.2))
```
Output: `4`. The function is available directly.

### Example 3 — Alias an import
```import statistics as stats
print(stats.mean([2,4,6]))
```
Output: `4`. An alias shortens repeated module names.

### Example 4 — Safe main guard
```def add(a,b): return a+b
if __name__ == "__main__":
    print(add(2,3))
```
When run as a script prints 5; imported as a module, the print does not execute.

### Example 5 — Inspect module location
```import json
print(json.__name__)
```
Output: `json`. Modules expose metadata.

## 5. Five practice tasks with solutions
### Task 1 — Generate a random integer
```import random
print(random.randint(1, 6))
```
Output is an integer from 1 through 6 inclusive. Random output varies.

### Task 2 — Parse ISO date
```from datetime import date
print(date.fromisoformat("2026-01-15"))
```
Output: `2026-01-15`.

### Task 3 — Use pathlib
```from pathlib import Path
p=Path("notes.txt")
print(p.suffix)
```
Output: `.txt`.

### Task 4 — Split helper into its own module
Create `math_helpers.py`:
```def multiply(a,b): return a*b
```
Create `main.py` in same folder:
```from math_helpers import multiply
print(multiply(6,7))
```
Output: `42`. Keep files together for this simple import.

### Task 5 — Main guard
```def greet(): return "Hello"
if __name__ == "__main__":
    print(greet())
```
Run directly → `Hello`; import does not print it. This prevents side effects on import.

## 6. Common mistakes
- Circular imports make initialization order difficult.
- Shadowing standard modules with filenames such as `email.py`, `json.py`.
- Import-time code causing unwanted side effects.
- Confusing a module file with a package directory.
- Unclear broad wildcard imports can overwrite names.

## 7. Interview Q&A
1. What is a module? **A Python file containing reusable definitions.**
2. What is a package? **A namespace grouping modules.**
3. Why main guard? **Separate direct execution from import.**
4. Why avoid circular imports? **They complicate module initialization and may expose partially initialized objects.**
5. What is an alias import? **Assign a short local name with `as`.**

## 8. Project — Modular Calculator
Create these files in one folder.

`calculator_ops.py`
```python
def calculate(a, op, b):
    if op not in {"+","-","*","/"}: raise ValueError("Unsupported operator")
    if op == "+": return a+b
    if op == "-": return a-b
    if op == "*": return a*b
    if b == 0: raise ZeroDivisionError("Divide by zero")
    return a/b
```

`main.py`
```python
from calculator_ops import calculate

def main():
    try:
        a=float(input("First: ")); op=input("Operator: ").strip(); b=float(input("Second: "))
        print(calculate(a,op,b))
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")

if __name__ == "__main__": main()
```
Run `python main.py`; enter 4, *, 3 → 12.0.

### Tests — `test_calculator_ops.py`
```python
import unittest
from calculator_ops import calculate

class CalculatorOpsTests(unittest.TestCase):
    def test_add(self): self.assertEqual(calculate(1,"+",2),3)
    def test_subtract(self): self.assertEqual(calculate(5,"-",2),3)
    def test_multiply(self): self.assertEqual(calculate(3,"*",4),12)
    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError): calculate(4,"/",0)
    def test_operator(self):
        with self.assertRaises(ValueError): calculate(2,"%",2)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What is a module? **A reusable Python file.**
2. Why use from-import? **To import selected names.**
3. What main guard checks? **Whether the file is being run as the main program.**
4. Why avoid `json.py` as a filename? **It can shadow the standard json module.**
5. What causes circular imports? **Modules depending on one another during import.**
**Challenge:** Turn the calculator into a package with an `__init__.py` and add a second module for input validation.

## 10. Completion
- [ ] I understand imports and main guard.
- [ ] The modular calculator works and all tests pass.
- [ ] I completed the package challenge.
