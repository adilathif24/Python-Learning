# Day 27 — Comprehensions and Built-ins

**Status:** Full study pack. Complete practice and tests before marking mastery.

## 1. Definition
A **comprehension** concisely constructs a list, set, or dictionary by iterating over an iterable, optionally filtering values. Built-ins such as `enumerate`, `zip`, `sum`, `min`, `max`, `any`, and `all` express common operations.

## 2. Why / where / when
Use comprehensions for simple transformations and filters; use an ordinary loop when logic has multiple steps or side effects. Use `enumerate` for indexes, `zip` for aligned sequences, and `any/all` for Boolean checks. Avoid dense nested comprehensions that are harder to read than loops.

## 3. Syntax
```python
squares = [n*n for n in range(5)]
evens = {n for n in range(10) if n % 2 == 0}
mapping = {n: n*n for n in range(4)}
```
Comprehensions create a new collection. `zip` stops at the shortest input unless `strict=True` is used in supported Python versions.

## 4. Five worked examples
### Example 1 — List comprehension
```python
squares = [n*n for n in range(1, 5)]
print(squares)
```
Output: `[1, 4, 9, 16]`.

### Example 2 — Filter with condition
```python
values = [2, 5, 8, 11, 14]
print([n for n in values if n % 2 == 0])
```
Output: `[2, 8, 14]`.

### Example 3 — Dictionary comprehension
```python
words = ["python", "sql"]
print({word: len(word) for word in words})
```
Output: `{'python': 6, 'sql': 3}`.

### Example 4 — enumerate
```python
for index, fruit in enumerate(["apple","pear"], start=1):
    print(index, fruit)
```
Output: `1 apple` then `2 pear`.

### Example 5 — zip and any/all
```python
names = ["Ali","Maya"]
scores = [80,95]
print(list(zip(names,scores)))
print(any(score >= 90 for score in scores))
print(all(score >= 60 for score in scores))
```
Output: `[('Ali', 80), ('Maya', 95)]`, then True, then True.

## 5. Five tasks with solutions
### Task 1 — Normalise names
```python
names = [" ali ", "MAYA", " Noor "]
print([name.strip().title() for name in names])
```
Output: `['Ali', 'Maya', 'Noor']`.

### Task 2 — Set of unique initials
```python
names = ["Adil","Ali","Maya"]
print({name[0].upper() for name in names})
```
Output is set containing A and M (display order not guaranteed).

### Task 3 — Map scores to pass/fail
```python
scores = {"Ali":80,"Noor":45}
print({name: ("Pass" if score >= 50 else "Fail") for name,score in scores.items()})
```
Output maps Ali to Pass and Noor to Fail.

### Task 4 — Pair lists
```python
products = ["Pen","Book"]
prices = [10,50]
print({name:price for name,price in zip(products,prices)})
```
Output: `{'Pen': 10, 'Book': 50}`.

### Task 5 — Find extremes safely
```python
values = []
if values: print(min(values), max(values))
else: print("No values")
```
Output: `No values`. min/max require non-empty inputs unless defaults are provided.

## 6. Common mistakes
- Dict comprehensions overwrite duplicate keys.
- Sets do not guarantee display order.
- zip silently truncates to the shortest input by default.
- min/max on an empty iterable raises ValueError.
- Overly complex comprehensions are hard to maintain.

## 7. Interview Q&A
1. What is a comprehension? **A compact construct to build a collection from an iterable.**
2. Why use enumerate? **To get index and item together.**
3. What does zip do? **Pairs items from iterables in parallel.**
4. any vs all? **any requires one true item; all requires every item true.**
5. When avoid comprehensions? **When the transformation is complex or clarity suffers.**

## 8. Project — Marks and Sales Summary
Save as `summary_report.py`.
```python
def summarize(scores, sales):
    if any(not 0 <= value <= 100 for value in scores.values()):
        raise ValueError("Scores must be 0–100")
    if any(value < 0 for value in sales.values()):
        raise ValueError("Sales cannot be negative")
    return {
        "passed": sorted(name for name, score in scores.items() if score >= 50),
        "score_by_name": {name: score for name, score in scores.items()},
        "sales_total": sum(sales.values()),
        "top_product": max(sales, key=sales.get) if sales else None,
    }

def main():
    report = summarize({"Ali":80,"Maya":45},{"Pen":100,"Book":250})
    for key,value in report.items(): print(f"{key}: {value}")

if __name__ == "__main__": main()
```
Sample: passed = ['Ali']; sales_total = 350; top_product = Book.

### Tests — `test_summary_report.py`
```python
import unittest
from summary_report import summarize

class SummaryTests(unittest.TestCase):
    def test_total(self): self.assertEqual(summarize({},{"A":2,"B":3})["sales_total"],5)
    def test_passed(self): self.assertEqual(summarize({"Ali":70},{"A":1})["passed"],["Ali"])
    def test_empty_sales(self): self.assertIsNone(summarize({}, {})["top_product"])
    def test_invalid_score(self):
        with self.assertRaises(ValueError): summarize({"A":101},{})
    def test_negative_sale(self):
        with self.assertRaises(ValueError): summarize({}, {"A":-1})

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What does enumerate return? **Index/item pairs.**
2. What does zip do with unequal lengths by default? **Stops at shortest iterable.**
3. Which built-in sums values? **sum.**
4. What does any mean? **At least one condition is true.**
5. Why keep complex logic out of comprehensions? **Readability.**
**Challenge:** Extend report with average score and tie-aware highest sales products; test empty data and ties.

## 10. Completion
- [ ] I can write list, set and dict comprehensions.
- [ ] I understand enumerate, zip, min/max, any/all.
- [ ] Project tests pass.
