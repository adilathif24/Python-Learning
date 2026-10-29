# Day 11 — Complete Lists: Mutation, Copying and Nested Data

**Status:** Full study pack. Earn mastery through independent practice and passing tests.

## 1. Definition and purpose
A list is an ordered, mutable sequence. Mutation changes an existing list; copying creates another list object. Nested lists contain lists as elements. Use lists for ordered records that change over time; use immutable tuples for fixed records and avoid complicated nested structures when a named object or dictionary would be clearer.

## 2. Syntax and rules
```python
items = [1, 2, 3]
items[0] = 10
items.append(4)
shallow = items.copy()
matrix = [[1, 2], [3, 4]]
```
Index starts at 0; slices exclude their stop index. `append` adds one item, `extend` adds items from an iterable, `insert` adds at an index, `pop` removes and returns an item. `copy()` is shallow. Use `copy.deepcopy()` only when independent nested mutable objects are needed.

### Dry run
`a=[[1],[2]]; b=a.copy(); b[0].append(9)` produces both `a == [[1,9],[2]]` and `b == [[1,9],[2]]`, because the inner lists are shared.

## 3. Five worked examples

### Example 1 — Remove an item by value
```python
tasks = ["read", "code", "review"]
tasks.remove("code")
print(tasks)
```
Output: `['read', 'review']`. remove deletes the first matching value; it raises ValueError if absent.

### Example 2 — Safe pop
```python
items = [4, 8, 12]
last = items.pop()
print(last, items)
```
Output: `12 [4, 8]`. pop returns the removed item.

### Example 3 — Shallow versus deep copy
```python
from copy import deepcopy
original = [[1], [2]]
shallow = original.copy()
deep = deepcopy(original)
original[0].append(9)
print(shallow)
print(deep)
```
Output: `[[1, 9], [2]]` then `[[1], [2]]`. Deep copy duplicates nested lists.

### Example 4 — Filter values
```python
numbers = [3, 8, 11, 14, 20]
evens = [number for number in numbers if number % 2 == 0]
print(evens)
```
Output: `[8, 14, 20]`. A new list is built without mutating the original.

### Example 5 — Flatten a two-dimensional list
```python
matrix = [[1, 2], [3], [4, 5]]
flat = [item for row in matrix for item in row]
print(flat)
```
Output: `[1, 2, 3, 4, 5]`. The inner loop visits every element of each row.

## 4. Five practice tasks with solutions

### Task 1 — Remove all negative values
```python
values = [3, -1, 0, -5, 8]
clean = [value for value in values if value >= 0]
print(clean)
```
Output: `[3, 0, 8]`. A comprehension avoids changing a list during iteration.

### Task 2 — Rotate a list right once
```python
values = [1, 2, 3, 4]
rotated = values[-1:] + values[:-1]
print(rotated)
```
Output: `[4, 1, 2, 3]`. Slices also handle an empty list safely.

### Task 3 — Find all positions of a value
```python
values = [2, 5, 2, 7, 2]
positions = [i for i, value in enumerate(values) if value == 2]
print(positions)
```
Output: `[0, 2, 4]`. enumerate provides index and value together.

### Task 4 — Make independent nested copy
```python
from copy import deepcopy
data = [[1, 2], [3, 4]]
copy_data = deepcopy(data)
copy_data[0][0] = 99
print(data, copy_data)
```
Output: `[[1, 2], [3, 4]] [[99, 2], [3, 4]]`. Deep copy isolates nested lists.

### Task 5 — Handle absent removal safely
```python
def remove_if_present(values, target):
    if target in values:
        values.remove(target)
        return True
    return False

items = ["pen", "book"]
print(remove_if_present(items, "bag"), items)
```
Output: `False ['pen', 'book']`. Check membership before removal.

## 5. Common mistakes
- `b = a` creates an alias, not a copy.
- A shallow copy does not isolate nested mutable values.
- Mutating a list during iteration can skip elements.
- `sort()` changes a list and returns None; `sorted()` returns a new list.
- Check empty lists before using indexes or pop.

## 6. Interview questions
1. What is list mutability? Existing list contents can be changed.
2. Difference between shallow and deep copy? Shallow copies only the outer container; deep copy recursively copies nested objects.
3. Why avoid modifying a list while iterating? Index shifts may skip or repeat elements.
4. Difference between append and extend? One object versus each element of an iterable.
5. What does enumerate return? Pairs of index and item in an iterable.

## 7. Project — Task List Manager
Save as `task_list.py`.
```python
def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("Task title is required")
    tasks.append({"title": title, "done": False})

def complete_task(tasks, index):
    if not 0 <= index < len(tasks):
        raise IndexError("Task index out of range")
    tasks[index]["done"] = True

def pending_tasks(tasks):
    return [task["title"] for task in tasks if not task["done"]]

def main():
    tasks = []
    while True:
        choice = input("1 Add, 2 List pending, 3 Complete first, 4 Quit: ").strip()
        if choice == "1":
            try:
                add_task(tasks, input("Title: "))
            except ValueError as error:
                print(error)
        elif choice == "2":
            print(pending_tasks(tasks))
        elif choice == "3":
            try:
                complete_task(tasks, int(input("Index (0-based): ")))
            except (ValueError, IndexError) as error:
                print(error)
        elif choice == "4":
            break
        else:
            print("Choose 1–4")

if __name__ == "__main__":
    main()
```
Run: `python task_list.py`. Example: add "Revise Python", pending list shows it until marked complete.

### Tests — save as test_task_list.py
```python
import unittest
from task_list import add_task, complete_task, pending_tasks

class TaskListTests(unittest.TestCase):
    def test_add_pending(self):
        tasks=[]; add_task(tasks, "Study")
        self.assertEqual(pending_tasks(tasks), ["Study"])
    def test_complete(self):
        tasks=[]; add_task(tasks, "Study"); complete_task(tasks, 0)
        self.assertEqual(pending_tasks(tasks), [])
    def test_empty_title(self):
        with self.assertRaises(ValueError): add_task([], " ")
    def test_bad_index(self):
        with self.assertRaises(IndexError): complete_task([], 0)
    def test_multiple_tasks(self):
        tasks=[]; add_task(tasks,"A"); add_task(tasks,"B")
        self.assertEqual(len(pending_tasks(tasks)),2)

if __name__ == "__main__": unittest.main()
```
Run tests: `python -m unittest -v`.

## 8. Quiz and challenge
1. Is a list mutable? **Yes.**
2. Does `append([1,2])` add two items? **No, it adds one nested list.**
3. Which copy isolates nested lists? **deepcopy.**
4. What does `enumerate` provide? **Index and item.**
5. What does `pop` return? **The removed item.**

**Challenge:** Add task deletion by index and test empty, first, and invalid indexes.

## 9. Completion checklist
- [ ] I can explain mutation, aliasing, shallow copy and deep copy.
- [ ] I attempted the five tasks before reading their solutions.
- [ ] All task-list tests pass.
- [ ] I solved the challenge independently.
