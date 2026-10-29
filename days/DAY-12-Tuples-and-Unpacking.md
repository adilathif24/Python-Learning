# Day 12 — Tuples and Unpacking

**Status:** Full study pack. Practice and test before marking mastery.

## 1. Definition
A **tuple** is an ordered, immutable sequence. **Unpacking** assigns the elements of an iterable to multiple variables. Tuples suit fixed records and multiple return values; use lists when the sequence must be modified.

## 2. When and why
Use tuples for coordinates, fixed RGB colors, function returns, and dictionary keys when all contained values are hashable. A tuple is only shallowly immutable: a mutable object inside it can still change. Avoid a tuple when named fields would be clearer; consider a dataclass or named tuple for structured records.

## 3. Syntax and rules
```python
point = (3, 4)
single = (5,)  # comma is essential
x, y = point
first, *middle, last = (1, 2, 3, 4)
```
- Parentheses are often optional; commas create the tuple.
- A one-element tuple needs a trailing comma.
- Unpacking requires matching counts unless starred unpacking is used.
- `a, b = b, a` swaps names without a temporary variable.

Dry run: `x, y = (10, 20)` binds x to 10 and y to 20.

## 4. Five worked examples

### Example 1 — Create a tuple
```python
dimensions = (1920, 1080)
print(dimensions[0], dimensions[1])
```
Output: `1920 1080`. Indexing works like other sequences.

### Example 2 — Single-item tuple
```python
value = (7,)
print(type(value).__name__, len(value))
```
Output: `tuple 1`. The comma creates a tuple.

### Example 3 — Unpack coordinates
```python
point = (4, 9)
x, y = point
print(f"x={x}, y={y}")
```
Output: `x=4, y=9`. Two elements bind to two names.

### Example 4 — Starred unpacking
```python
first, *middle, last = [10, 20, 30, 40, 50]
print(first, middle, last)
```
Output: `10 [20, 30, 40] 50`. The starred name receives a list.

### Example 5 — Swap values
```python
a, b = 3, 8
a, b = b, a
print(a, b)
```
Output: `8 3`. Python evaluates the right-hand side before assigning.

## 5. Five tasks with solutions

### Task 1 — Return quotient and remainder
```python
def divide(a, b):
    if b == 0: raise ValueError("b cannot be zero")
    return divmod(a, b)
q, r = divide(17, 5)
print(q, r)
```
Output: `3 2`. The result tuple is unpacked.

### Task 2 — Extract the middle values
```python
head, *body, tail = ["A", "B", "C", "D"]
print(body)
```
Output: `['B', 'C']`. Starred unpacking absorbs remaining elements.

### Task 3 — Loop over coordinate pairs
```python
points = [(1, 2), (3, 4)]
for x, y in points:
    print(x + y)
```
Output: `3` then `7`. Each pair is unpacked during iteration.

### Task 4 — Make an immutable record
```python
student = ("Adil", 85)
name, score = student
print(f"{name}: {score}")
```
Output: `Adil: 85`. Fixed data is easy to pass together.

### Task 5 — Handle expected tuple size
```python
record = (7, 8, 9)
if len(record) == 3:
    x, y, z = record
    print(x + y + z)
```
Output: `24`. Validate the shape before unpacking when input size is uncertain.

## 6. Common mistakes
- `(7)` is an int; `(7,)` is a tuple.
- Assigning an element in a tuple raises TypeError.
- Too few/many values during ordinary unpacking raises ValueError.
- A tuple containing a list can indirectly change because the list remains mutable.
- Unpacking external data should validate length and types.

## 7. Interview Q&A
1. Are tuples mutable? **No, their element references cannot be reassigned.**
2. How do you make a single-element tuple? **Add a trailing comma.**
3. What is unpacking? **Assigning iterable items to multiple names.**
4. Can tuples be dictionary keys? **If all elements are hashable.**
5. What is starred unpacking? **A target with * collects remaining values into a list.**

## 8. Project — Coordinate Distance
Save as `coordinate_distance.py`.
```python
from math import hypot

def distance(point_a, point_b):
    if len(point_a) != 2 or len(point_b) != 2:
        raise ValueError("Each point needs x and y")
    x1, y1 = point_a
    x2, y2 = point_b
    return hypot(x2 - x1, y2 - y1)

def main():
    print(f"Distance: {distance((0, 0), (3, 4)):.2f}")

if __name__ == "__main__": main()
```
Output: `Distance: 5.00`.

### Tests — test_coordinate_distance.py
```python
import unittest
from coordinate_distance import distance

class DistanceTests(unittest.TestCase):
    def test_345_triangle(self): self.assertEqual(distance((0,0),(3,4)),5)
    def test_same_point(self): self.assertEqual(distance((1,1),(1,1)),0)
    def test_negative_coordinates(self): self.assertEqual(distance((-1,0),(2,0)),3)
    def test_wrong_shape(self):
        with self.assertRaises(ValueError): distance((1,), (2,3))
    def test_decimal(self): self.assertAlmostEqual(distance((0,0),(1,1)),2**0.5)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz
1. What makes a singleton tuple? **A comma.**
2. What does starred unpacking collect? **Remaining values in a list.**
3. Can a tuple be reassigned by index? **No.**
4. How swap variables? **`a, b = b, a`.**
5. What exception on unpack-size mismatch? **ValueError.**

**Challenge:** Extend distance to a 3D point and test both valid and invalid tuple lengths.

## 10. Completion
- [ ] I can create tuples and unpack fixed and variable lengths.
- [ ] I completed all examples and tasks.
- [ ] Tests pass and challenge works.
