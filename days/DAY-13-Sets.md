# Day 13 — Sets and Set Operations

**Status:** Full study pack. Complete the tasks and project before marking mastery.

## 1. Definition
A **set** is an unordered collection of unique hashable elements. It removes duplicates and supports union, intersection, difference, and symmetric difference. A `frozenset` is an immutable set.

## 2. Why, where, when
Use sets for de-duplicating data, membership testing, permission tags, unique visitors, and comparing groups. Do not use a set when order or duplicate counts matter; use a list or Counter instead. Set elements must be hashable, so a list cannot be a set element.

## 3. Syntax and rules
```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference
empty = set() # not {}
```
Sets have no positional indexing. Use `add`, `update`, `discard` (safe if missing), and `remove` (raises KeyError if missing). `{}` creates an empty dict, not a set.

Dry run: {1,2,3} ∩ {2,3,4} = {2,3}.

## 4. Five worked examples

### Example 1 — Remove duplicates
```python
values = [3, 1, 3, 2, 1]
print(sorted(set(values)))
```
Output: `[1, 2, 3]`. A set keeps only distinct values; sorted makes output order explicit.

### Example 2 — Intersection
```python
python_students = {"Ali", "Maya", "Ravi"}
java_students = {"Maya", "Ravi", "Noor"}
print(sorted(python_students & java_students))
```
Output: `['Maya', 'Ravi']`. Intersection keeps shared elements.

### Example 3 — Difference
```python
a = {"read", "write", "admin"}
b = {"read"}
print(sorted(a - b))
```
Output: `['admin', 'write']`. Difference finds elements in a but not b.

### Example 4 — Add and discard
```python
tags = {"python"}
tags.add("testing")
tags.discard("missing")
print(sorted(tags))
```
Output: `['python', 'testing']`. discard does not fail if the value is absent.

### Example 5 — Subset check
```python
required = {"read", "write"}
assigned = {"read", "write", "export"}
print(required <= assigned)
```
Output: `True`. The assigned permissions include all required permissions.

## 5. Five tasks with solutions

### Task 1 — Common interests
```python
a = {"cricket", "music", "coding"}
b = {"music", "travel", "coding"}
print(sorted(a & b))
```
Output: `['coding', 'music']`.

### Task 2 — Unique words
```python
text = "python makes learning python useful"
words = set(text.split())
print(len(words))
```
Output: `4`. There are four distinct words.

### Task 3 — Symmetric difference
```python
print(sorted({1,2,3} ^ {3,4,5}))
```
Output: `[1, 2, 4, 5]`. Items unique to either set are returned.

### Task 4 — Safe membership
```python
allowed = {"viewer", "editor"}
role = "admin"
print(role in allowed)
```
Output: `False`. Membership is a direct set operation.

### Task 5 — Create an empty set
```python
items = set()
items.add("first")
print(items == {"first"})
```
Output: `True`. `set()` creates an empty set.

## 6. Common mistakes
- `{}` is an empty dict, not set.
- Sets are unordered; never assume display order.
- Duplicate values disappear.
- Mutable lists/dicts cannot be set elements.
- `remove` may raise KeyError; use `discard` when absence is acceptable.

## 7. Interview Q&A
1. What makes a set unique? **Each element appears at most once.**
2. Difference between union and intersection? **Union combines; intersection keeps shared items.**
3. Can a set contain a list? **No; lists are unhashable.**
4. Difference between remove and discard? **remove raises KeyError if absent; discard does not.**
5. When not to use a set? **When order or duplicates/counts matter.**

## 8. Project — Permission Checker
Save as `permission_checker.py`.
```python
def missing_permissions(required, granted):
    required_set = set(required)
    granted_set = set(granted)
    return required_set - granted_set

def can_access(required, granted):
    return not missing_permissions(required, granted)

def main():
    required = {"read", "write"}
    granted = set(input("Enter permissions separated by commas: ").split(","))
    granted = {item.strip() for item in granted if item.strip()}
    missing = missing_permissions(required, granted)
    print("Access granted" if not missing else f"Missing: {sorted(missing)}")

if __name__ == "__main__": main()
```
Sample input: `read,write` → `Access granted`.

### Tests — test_permission_checker.py
```python
import unittest
from permission_checker import missing_permissions, can_access

class PermissionTests(unittest.TestCase):
    def test_access_all(self): self.assertTrue(can_access({"read"},{"read","write"}))
    def test_missing(self): self.assertEqual(missing_permissions({"read","write"},{"read"}), {"write"})
    def test_empty_grants(self): self.assertFalse(can_access({"read"},set()))
    def test_no_required(self): self.assertTrue(can_access(set(),set()))
    def test_duplicates_removed(self): self.assertTrue(can_access(["read","read"],["read"]))

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Empty set syntax? **`set()`.**
2. Shared items operation? **Intersection.**
3. Items unique to either set? **Symmetric difference.**
4. Can a set be indexed? **No.**
5. Safe removal if absent? **discard.**

**Challenge:** Compare two lists of course enrollments and report shared, unique-to-A, and unique-to-B courses.

## Real-world use cases — where, when and how
1. **De-duplication:** Where: imported records. When only unique tags matter. How: convert values to a set, then sort if display order matters.
2. **Permission checks:** Where: access control. When a role must include all required capabilities. How: use subset tests or set difference.
3. **Course overlap:** Where: enrollment reports. When comparing two cohorts. How: intersection returns shared courses/students.
4. **Diffing records:** Where: reconciliation. When values missing from one list must be found. How: use set difference in each direction.
5. **Visited nodes:** Where: graph traversal. When repeat visits must be avoided. How: track seen nodes in a set.


## 10. Completion
- [ ] I can explain set uniqueness and all four operations.
- [ ] I completed examples, tasks and project.
- [ ] Tests pass and challenge is done.
