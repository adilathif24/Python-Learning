# Day 15 — Choosing the Right Collection

**Status:** Full study pack. Demonstrate sound choices using practice and project tests.

## 1. Definition
Python's core collection types solve different problems: **list** is ordered and mutable; **tuple** is ordered and immutable; **set** stores unique hashable values; **dict** maps hashable keys to values. Choosing a structure affects clarity, correctness, and performance.

## 2. Selection guide
- Choose **list** for ordered sequences, duplicates, and index access.
- Choose **tuple** for fixed records or multiple return values.
- Choose **set** for uniqueness and membership.
- Choose **dict** for lookups by key, named attributes, and counters.
- Use **collections.Counter** for frequency counts and **deque** for queues.
Do not choose only by habit. Ask whether order, mutability, duplicates, key lookup, and item removal matter.

## 3. Syntax and complexity intuition
```python
names = ["Ali", "Ali", "Maya"]       # ordered, duplicates
point = (3, 5)                       # fixed record
unique_names = set(names)            # unique items
scores = {"Ali": 85, "Maya": 91}    # key to value
```
Typical average membership: list O(n), set/dict O(1) average. Sorting a list is typically O(n log n). These are average/common-case guidelines, not a promise for every workload.

Dry run: use a list to preserve a task sequence, a set to check whether a tag has been seen, and a dictionary to retrieve a task's status by ID.

## 4. Five worked examples

### Example 1 — Preserve order with a list
```python
queue = ["A", "B", "A"]
print(queue[1], len(queue))
```
Output: `B 3`. The list retains position and duplicates.

### Example 2 — Unique values with a set
```python
tags = {"python", "python", "sql"}
print(len(tags))
```
Output: `2`. Repeated values collapse into one.

### Example 3 — Named data with a dict
```python
employee = {"id": 7, "name": "Ali"}
print(employee["name"])
```
Output: `Ali`. A key communicates the meaning.

### Example 4 — Fixed pair as tuple
```python
coordinate = (10, 20)
x, y = coordinate
print(x + y)
```
Output: `30`. A tuple holds a fixed coordinate pair.

### Example 5 — Fast frequency tally
```python
from collections import Counter
print(Counter(["red", "blue", "red"]))
```
Output: `Counter({'red': 2, 'blue': 1})`. Counter is purpose-built for counts.

## 5. Five tasks with solutions

### Task 1 — Remove duplicates but preserve order
```python
values = [3, 1, 3, 2, 1]
seen, result = set(), []
for value in values:
    if value not in seen:
        result.append(value)
        seen.add(value)
print(result)
```
Output: `[3, 1, 2]`. The list preserves order while the set tracks membership.

### Task 2 — Lookup by ID
```python
users = {101: "Ali", 102: "Maya"}
print(users.get(102, "Unknown"))
```
Output: `Maya`. A dict is a natural mapping.

### Task 3 — FIFO queue with deque
```python
from collections import deque
queue = deque(["first", "second"])
queue.append("third")
print(queue.popleft())
```
Output: `first`. Deque supports efficient operations at both ends.

### Task 4 — Count frequency
```python
from collections import Counter
print(Counter("banana")["a"])
```
Output: `3`. Counter simplifies tallying.

### Task 5 — Immutable record
```python
user_record = ("Adil", "active")
name, status = user_record
print(name, status)
```
Output: `Adil active`. A tuple is suitable for a small fixed record, though a dataclass may communicate intent better in larger code.

## 6. Common mistakes
- Set iteration order should not be relied on for presentation.
- Lists make membership checks linear in list length.
- Dict keys must be hashable.
- A tuple does not deeply freeze mutable objects inside it.
- A Counter or deque may communicate intent better than a manual list algorithm.

## 7. Interview Q&A
1. List vs tuple? **Lists are mutable; tuples are immutable sequences.**
2. List vs set? **List maintains order/duplicates and supports indexing; set stores unique values with fast membership.**
3. When use dict? **When each value is looked up by a meaningful key.**
4. Why use deque for queue? **Efficient appends and pops at both ends.**
5. What is Counter? **A dict-like tool for counting hashable elements.**

## 8. Project — Course Enrollment Report
Save as `enrollment_report.py`.
```python
from collections import Counter

def enrollment_report(enrollments):
    if any(not isinstance(course, str) or not course.strip() for course in enrollments):
        raise ValueError("Course names must be non-empty strings")
    counts = Counter(course.strip().casefold() for course in enrollments)
    unique_courses = sorted(counts)
    return {"counts": dict(counts), "unique_courses": unique_courses}

def main():
    courses = ["Python", "SQL", "Python", "React", "SQL"]
    report = enrollment_report(courses)
    print("Counts:", report["counts"])
    print("Unique:", report["unique_courses"])

if __name__ == "__main__": main()
```
Sample output: counts Python:2, SQL:2, React:1 (normalised to lowercase).

### Tests — test_enrollment_report.py
```python
import unittest
from enrollment_report import enrollment_report

class EnrollmentTests(unittest.TestCase):
    def test_count(self): self.assertEqual(enrollment_report(["Python","Python"])["counts"]["python"],2)
    def test_case_normalized(self): self.assertEqual(enrollment_report(["SQL","sql"])["counts"]["sql"],2)
    def test_unique_sorted(self): self.assertEqual(enrollment_report(["B","A"])["unique_courses"],["a","b"])
    def test_empty(self): self.assertEqual(enrollment_report([])["unique_courses"],[])
    def test_invalid(self):
        with self.assertRaises(ValueError): enrollment_report([" "])

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Need ordered duplicates? **List.**
2. Need unique membership? **Set.**
3. Key-based lookup? **Dict.**
4. Fixed sequence? **Tuple, depending on semantic needs.**
5. Count elements? **Counter or dictionary.**

**Challenge:** Model a library checkout with a dict keyed by book ID, a set of available IDs, and a list of checkout events. Explain why each type fits its role.

## Real-world use cases — where, when and how
1. **Ordered playlist:** Where: media list. When order and duplicates matter. How: use a list.
2. **Fixed coordinate:** Where: geometry. When a pair should not change. How: use a tuple and unpack it.
3. **Unique tags:** Where: search filters. When duplicates should collapse. How: use a set.
4. **Lookup by identifier:** Where: products/users. When a key retrieves a record. How: use a dictionary keyed by ID.
5. **FIFO jobs:** Where: worker queues. When first-in jobs run first. How: use collections.deque rather than pop(0) on a list.


## 10. Completion
- [ ] I can justify a collection choice for a real use case.
- [ ] I solved all tasks and ran project tests.
- [ ] I completed the challenge.
