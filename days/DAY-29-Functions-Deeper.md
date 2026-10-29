# Day 29 — Advanced Functions, Scope, Type Hints and Contracts

**Status:** Full study pack. Complete the tasks and tests before marking mastery.

## 1. Definition
Advanced function design includes flexible arguments, closures/scope, type hints, and contracts. A type hint documents expected types and supports static analysis but Python does not automatically enforce it at runtime.

## 2. Why / where / when
Use explicit contracts and type hints in team code, libraries and APIs. Use `*args`/`**kwargs` only for genuine flexibility; prefer named parameters for predictable interfaces. Use closures when a function needs to remember local state. Do not rely on hints alone to validate untrusted values.

## 3. Syntax
```python
def area(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return width * height
```
Hints are metadata for readers/tools; runtime validation is a separate responsibility. `None` defaults are often useful for mutable inputs; create a fresh object within the function.

## 4. Five worked examples
### Example 1 — Type hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
print(greet("Adil"))
```
Output: `Hello, Adil`. The annotations document the expected contract.

### Example 2 — Keyword-only parameter
```python
def create_user(name, *, active=True):
    return {"name": name, "active": active}
print(create_user("Ali", active=False))
```
Output: `{'name': 'Ali', 'active': False}`. The star forces active to be passed by keyword.

### Example 3 — Safe mutable default
```python
def add(value, items=None):
    if items is None: items=[]
    items.append(value)
    return items
print(add(1), add(2))
```
Output: `[1] [2]`. A new list is created per call.

### Example 4 — Closure
```python
def make_counter():
    count=0
    def next_value():
        nonlocal count
        count += 1
        return count
    return next_value
counter=make_counter()
print(counter(), counter())
```
Output: `1 2`. nonlocal modifies the enclosing function's variable.

### Example 5 — Return contract
```python
def divide(a: float, b: float) -> float:
    if b == 0: raise ValueError("b cannot be zero")
    return a/b
print(divide(8,2))
```
Output: `4.0`. Explicit error contract prevents a silent invalid result.

## 5. Five tasks with solutions
### Task 1 — Validate typed score
```def parse_score(value: str) -> int:
    score=int(value)
    if not 0 <= score <= 100: raise ValueError("Score must be 0–100")
    return score
print(parse_score("85"))
```
Output: `85`. Type annotation documents text input and integer output.

### Task 2 — Keyword-only formatting
```def format_price(amount, *, currency="INR"):
    return f"{currency} {amount:.2f}"
print(format_price(10,currency="INR"))
```
Output: `INR 10.00`.

### Task 3 — Return named stats
```def stats(values):
    if not values: raise ValueError("values required")
    return {"min":min(values),"max":max(values),"count":len(values)}
print(stats([2,4,8]))
```
Output: `{'min': 2, 'max': 8, 'count': 3}`.

### Task 4 — Use a callable
```def apply_twice(function, value):
    return function(function(value))
print(apply_twice(lambda n:n+1,3))
```
Output: `5`. Functions are first-class values and can be passed as arguments.

### Task 5 — Avoid mutable defaults
```def build_tags(tag, tags=None):
    if tags is None: tags=[]
    tags.append(tag)
    return tags
print(build_tags("python"))
```
Output: `['python']`.

## 6. Common mistakes
- Type hints do not force runtime type checks.
- Missing return paths can return None unexpectedly.
- Mutable default values can leak state between calls.
- Global state makes tests interfere with each other.
- Over-flexible `kwargs` can hide misspelled option names.

## 7. Interview Q&A
1. Are type hints enforced by Python? **Not automatically at runtime.**
2. What is a closure? **An inner function retaining access to enclosing-scope variables.**
3. What does nonlocal do? **Rebinds a variable from an enclosing non-global scope.**
4. What is keyword-only parameter? **Must be supplied by name.**
5. How avoid mutable default bugs? **Use None and initialize inside the function.**

## 8. Project — Configurable Report Generator
Save as `report_generator.py`.
```python
from typing import Iterable

def build_report(values: Iterable[float], *, title: str = "Report", precision: int = 2) -> str:
    if not isinstance(title, str) or not title.strip(): raise ValueError("title required")
    if not isinstance(precision, int) or isinstance(precision, bool) or not 0 <= precision <= 6:
        raise ValueError("precision must be 0–6")
    numbers=list(values)
    if any(not isinstance(n,(int,float)) or isinstance(n,bool) for n in numbers):
        raise TypeError("values must be numeric")
    total=sum(numbers)
    average=total/len(numbers) if numbers else 0
    return f"{title.strip()}\nCount: {len(numbers)}\nTotal: {total:.{precision}f}\nAverage: {average:.{precision}f}"

def main():
    print(build_report([10,20,30],title="Sales",precision=1))

if __name__ == "__main__": main()
```
Output: Sales, Count 3, Total 60.0, Average 20.0.

### Tests — `test_report_generator.py`
```python
import unittest
from report_generator import build_report

class ReportTests(unittest.TestCase):
    def test_total(self): self.assertIn("Total: 60.00",build_report([10,20,30]))
    def test_empty(self): self.assertIn("Count: 0",build_report([]))
    def test_title(self): self.assertTrue(build_report([1],title="X").startswith("X"))
    def test_precision_range(self):
        with self.assertRaises(ValueError): build_report([1],precision=9)
    def test_type_check(self):
        with self.assertRaises(TypeError): build_report(["a"])

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Do hints enforce types? **No.**
2. What does nonlocal target? **An enclosing local scope.**
3. How make a parameter keyword-only? **Place it after *.**
4. Why avoid mutable defaults? **Shared object can persist across calls.**
5. What is a contract? **Documented/checked expectations for inputs and outputs.**
**Challenge:** Add a minimum/maximum range option as keyword-only values and test invalid ranges and empty data.

## 10. Completion
- [ ] I understand hints, scope and keyword-only arguments.
- [ ] Project tests pass.
- [ ] I completed the challenge.
