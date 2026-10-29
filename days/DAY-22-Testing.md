# Day 22 — Testing and Assertions

**Status:** Full study pack. Run the tests yourself before marking mastery.

## 1. Definition
A **test** checks whether code behaves as expected for chosen inputs. An **assertion** expresses a condition that must be true. A **unit test** checks a small unit, often a function, independently from unrelated services.

## 2. Why, where, when
Tests protect behavior during refactoring, expose edge cases, and document contracts. Use `unittest` or `pytest` for repeatable test suites. Use assertions for internal invariants/debugging, not as the only validation for untrusted production input because Python can disable assert statements with optimization.

## 3. Syntax and rules
```python
def add(a,b): return a+b
assert add(2,3) == 5
```
A `unittest.TestCase` test method starts with `test_`; use `assertEqual`, `assertTrue`, `assertRaises` and related methods. Test normal paths, boundaries, invalid inputs, and regressions.

## 4. Five worked examples
### Example 1 — Plain assert
```python
def is_even(n): return n % 2 == 0
assert is_even(4)
print("Passed")
```
Output: `Passed`. Assertion succeeds for an even input.

### Example 2 — Assert equality
```python
def area(w,h): return w*h
assert area(3,4) == 12
print("Area test passed")
```
Output: `Area test passed`.

### Example 3 — unittest simple test
```python
import unittest
def multiply(a,b): return a*b
class Tests(unittest.TestCase):
    def test_multiply(self): self.assertEqual(multiply(3,4),12)
if __name__ == "__main__": unittest.main()
```
Run as a file: reports one passing test. unittest discovers methods beginning with test_.

### Example 4 — Check expected exception
```python
import unittest
def positive(n):
    if n <= 0: raise ValueError("positive required")
    return n
class Tests(unittest.TestCase):
    def test_zero_rejected(self):
        with self.assertRaises(ValueError): positive(0)
if __name__ == "__main__": unittest.main()
```
Expected: test passes because ValueError is raised.

### Example 5 — Parameterized subtests
```python
import unittest
def square(n): return n*n
class Tests(unittest.TestCase):
    def test_values(self):
        for n, expected in [(0,0),(2,4),(-3,9)]:
            with self.subTest(n=n): self.assertEqual(square(n), expected)
if __name__ == "__main__": unittest.main()
```
Expected: all subtests pass.

## 5. Five practice tasks with solutions
### Task 1 — Test a boundary
```python
def eligible(age): return age >= 18
assert eligible(18) is True
assert eligible(17) is False
print("Passed")
```
Output: `Passed`.

### Task 2 — Test empty list
```python
def safe_first(values): return values[0] if values else None
assert safe_first([]) is None
print("Passed")
```
Output: `Passed`.

### Task 3 — Test invalid percentage
```python
import unittest
def discount(value):
    if not 0 <= value <= 100: raise ValueError
    return value
class Tests(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(ValueError): discount(101)
if __name__ == "__main__": unittest.main()
```
Expected: one test passes.

### Task 4 — Verify sorted order
```python
values = [3,1,2]
result = sorted(values)
assert result == [1,2,3]
assert values == [3,1,2]
print("Passed")
```
Output: `Passed`.

### Task 5 — Regression test
```python
def count_digits(n): return len(str(abs(n)))
assert count_digits(0) == 1
assert count_digits(-123) == 3
print("Passed")
```
Output: `Passed`. The tests lock in the zero and negative-number rules.

## 6. Common mistakes
- Testing only happy paths.
- Assertions with no meaningful failure message.
- Tests that depend on execution order or real external services.
- Mocking everything so that the real behavior is never tested.
- Forgetting to rerun all tests after a code change.

## 7. Interview Q&A
1. Unit test? **Checks one small behavior in isolation.**
2. Regression test? **Prevents an old bug from reappearing.**
3. What is a boundary test? **Tests near a limit.**
4. Difference between assert and unittest assertion? **Both check assumptions; unittest gives structured test reporting and richer assertion methods.**
5. Why test invalid input? **To verify failures are safe and understandable.**

## 8. Project — Test a Score Validator
Save as `score_validator.py`.
```python
def grade(score):
    if not isinstance(score, (int,float)) or isinstance(score,bool): raise TypeError("numeric score required")
    if not 0 <= score <= 100: raise ValueError("score must be 0–100")
    if score >= 90: return "A"
    if score >= 75: return "B"
    if score >= 60: return "C"
    return "Needs improvement"

if __name__ == "__main__":
    try: print(grade(float(input("Score: "))))
    except (ValueError, TypeError) as error: print(f"Invalid score: {error}")
```
Sample input 91 → A. Save tests as `test_score_validator.py`.

```python
import unittest
from score_validator import grade
class GradeTests(unittest.TestCase):
    def test_a_boundary(self): self.assertEqual(grade(90),"A")
    def test_b_boundary(self): self.assertEqual(grade(75),"B")
    def test_zero(self): self.assertEqual(grade(0),"Needs improvement")
    def test_high_invalid(self):
        with self.assertRaises(ValueError): grade(101)
    def test_type_invalid(self):
        with self.assertRaises(TypeError): grade("80")
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. How should unittest methods be named? **test_ prefix.**
2. What checks an exception? **assertRaises.**
3. What is a regression test? **Prevents old bug from returning.**
4. Should only normal inputs be tested? **No, test boundaries and invalid inputs too.**
5. Why avoid order-dependent tests? **They become fragile and hard to isolate.**
**Challenge:** Add tests for fractional scores, score 0, 100, -0.01, and 100.01.

## Real-world use cases — where, when and how
1. **Checkout calculations:** Where: shopping systems. When prices/discounts affect money. How: test ordinary totals, zero discount, full discount and invalid amounts.
2. **User access:** Where: account rules. When thresholds determine allowed actions. How: test the exact boundary and both sides.
3. **File import:** Where: ETL-style app scripts. When external files may be missing/malformed. How: create temporary files and test expected exceptions.
4. **Database operations:** Where: application storage. When inserts/updates/deletes must be correct. How: use an in-memory database and verify state after each operation.
5. **Bug prevention:** Where: any maintained codebase. When a fixed defect could return. How: retain a failing test case as a regression test.


## 10. Completion
- [ ] I can write tests for normal, boundary, error cases.
- [ ] All test code runs.
- [ ] I added a regression test for a bug.
