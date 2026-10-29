# Day 20 — Debugging Fundamentals

**Status:** Full study pack published. Work through debugging tasks and tests before marking mastery.

## 1. Definition
**Debugging** is the systematic process of finding, explaining, and correcting a defect. Common categories: syntax errors prevent parsing; runtime errors occur during execution; logic errors run but produce the wrong result.

## 2. Why, where, when
Debug in scripts, APIs, data pipelines, tests and production incidents. Reproduce the problem, read the traceback, isolate a small failing case, inspect values, form a hypothesis, change one thing, and rerun tests. Avoid random edits or suppressing exceptions without understanding their cause.

## 3. Method and syntax
Use `print()` for quick local tracing, `breakpoint()` or a debugger for stepwise inspection, and unit tests for repeatable checks.
```python
def average(values):
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)
```
When the input is empty, the explicit guard provides a clear failure instead of ZeroDivisionError.

## 4. Five worked examples
### Example 1 — Fix assignment vs comparison
Bug: `if score = 10:` is invalid syntax.
```python
score = 10
if score == 10:
    print("Match")
```
Output: `Match`. Comparison uses ==.

### Example 2 — Fix off-by-one
```python
for i in range(1, 6):
    print(i)
```
Output prints 1–5. Range stop is excluded; use stop=6.

### Example 3 — Trace a running total
```python
total = 0
for n in [2, 3, 4]:
    total += n
    print("trace:", n, total)
```
Output: trace: 2 2; trace: 3 5; trace: 4 9. Each line reveals state.

### Example 4 — Fix mutable default
```python
def add_item(item, items=None):
    if items is None: items = []
    items.append(item)
    return items
print(add_item("a"), add_item("b"))
```
Output: `['a'] ['b']`. Each call gets a new list.

### Example 5 — Preserve exception context
```python
def parse_count(text):
    try: return int(text)
    except ValueError as error:
        raise ValueError("Count must be an integer") from error
print(parse_count("4"))
```
Output: `4`. Chaining preserves the original cause if conversion fails.

## 5. Five debugging tasks with solutions
### Task 1 — Prevent division by zero
```python
def safe_divide(a,b):
    if b == 0: raise ValueError("b must not be zero")
    return a/b
print(safe_divide(6,2))
```
Output: `3.0`. Guard the known invalid domain.

### Task 2 — Correct factorial
```python
def factorial(n):
    if n < 0: raise ValueError("n must be non-negative")
    result = 1
    for value in range(2,n+1): result *= value
    return result
print(factorial(5))
```
Output: `120`. Initialize product to 1 and include n.

### Task 3 — Handle an empty list
```python
def first_or_none(values):
    return values[0] if values else None
print(first_or_none([]))
```
Output: `None`. Check before indexing.

### Task 4 — Fix vowel test
```python
text = "python"
vowels = sum(char in "aeiou" for char in text.casefold())
print(vowels)
```
Output: `1`. Check each character rather than searching for the entire string.

### Task 5 — Explain traceback
```python
def get_item(items, index):
    if not 0 <= index < len(items):
        raise IndexError("index out of range")
    return items[index]
print(get_item(["a","b"],1))
```
Output: `b`. Validate the index and produce a meaningful error.

## 6. Common mistakes
- Fixing symptoms without reproducing the bug.
- Editing many lines at once and losing the cause.
- Ignoring the last line of a traceback.
- Catching broad exceptions and continuing with corrupt state.
- Not adding a regression test after a bug fix.
- Forgetting to test empty and boundary cases.

## 7. Interview Q&A
1. Syntax vs runtime vs logic errors? **Parse failure, execution failure, wrong result respectively.**
2. What is a traceback? **The call stack and error details for an unhandled exception.**
3. Why minimize a failing example? **Reduces possible causes.**
4. What is a regression test? **A test that prevents a previously fixed defect from returning.**
5. What does a debugger breakpoint do? **Pauses execution so state can be inspected.**

## 8. Project — Debugged Grade Calculator
Save as `grade_calculator.py`.
```python
def grade_for(score):
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise TypeError("score must be numeric")
    if not 0 <= score <= 100:
        raise ValueError("score must be 0–100")
    if score >= 90: return "A"
    if score >= 75: return "B"
    if score >= 60: return "C"
    return "Needs improvement"

def main():
    try:
        score = float(input("Score: "))
        print(grade_for(score))
    except (ValueError, TypeError) as error:
        print(f"Invalid score: {error}")

if __name__ == "__main__": main()
```
Sample input 88 → `B`. Thresholds are ordered highest to lowest.

### Tests — `test_grade_calculator.py`
```python
import unittest
from grade_calculator import grade_for

class GradeTests(unittest.TestCase):
    def test_top_boundary(self): self.assertEqual(grade_for(90),"A")
    def test_b_boundary(self): self.assertEqual(grade_for(75),"B")
    def test_zero(self): self.assertEqual(grade_for(0),"Needs improvement")
    def test_out_of_range(self):
        with self.assertRaises(ValueError): grade_for(101)
    def test_wrong_type(self):
        with self.assertRaises(TypeError): grade_for("90")

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Which error prevents parsing? **SyntaxError.**
2. What is a logic error? **Code executes but gives wrong result.**
3. Why add a regression test? **To prevent recurrence.**
4. What should you inspect first in a traceback? **Error type/message and relevant final frames.**
5. Why change one thing at a time? **To isolate cause and effect.**
**Challenge:** Given an incorrect prime checker, create failing tests first, fix the bug, then demonstrate the tests pass for -1, 0, 1, 2, and 9.

## Real-world use cases — where, when and how
1. **Wrong calculation:** Where: billing scripts. When totals differ from expected results. How: reproduce a small example, trace intermediate values and add regression tests.
2. **API failure:** Where: integrations. When a request fails sporadically. How: inspect status/traceback, log safe context and test timeout/error handling.
3. **Data import crash:** Where: CSV/JSON tools. When a row has malformed data. How: isolate the offending row, validate inputs and test the corrected path.
4. **Boundary defect:** Where: age/score checks. When only exact thresholds fail. How: test immediately below, at and above each boundary.
5. **Unexpected state:** Where: object-oriented apps. When state changes unexpectedly. How: inspect the method that mutates state and verify invariants with unit tests.


## 10. Completion
- [ ] I can classify errors and read a traceback.
- [ ] I completed the debugging tasks.
- [ ] All grade calculator tests pass.
- [ ] I solved the challenge with a regression test.
