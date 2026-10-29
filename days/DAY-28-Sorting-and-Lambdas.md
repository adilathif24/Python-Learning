# Day 28 — Sorting and Lambda Expressions

**Status:** Full study pack. Complete the tasks and tests before marking mastery.

## 1. Definition
Sorting arranges values in an order. `sorted(iterable, key=..., reverse=...)` returns a new list; `list.sort()` modifies a list. A **lambda** is a small anonymous function with one expression.

## 2. Why / where / when
Sort numbers, names, records, products, or API results. Use `key` to declare what should determine order. Use a lambda for a short key expression; use a named function when logic is complex or reused. Avoid sorting objects using an arbitrary string representation when a field key is clearer.

## 3. Syntax
```python
numbers = [4,1,3]
print(sorted(numbers))
people = [{"name":"Ali","age":22},{"name":"Maya","age":20}]
print(sorted(people, key=lambda person: person["age"]))
```
Sort is stable: equal keys preserve relative order. Key function is called once per item in the sorting process.

## 4. Five worked examples
### Example 1 — Ascending and descending
```python
values = [5,1,7,3]
print(sorted(values))
print(sorted(values, reverse=True))
```
Output: `[1, 3, 5, 7]` and `[7, 5, 3, 1]`.

### Example 2 — Sort by length
```python
words = ["pear","fig","watermelon"]
print(sorted(words, key=len))
```
Output: `['fig', 'pear', 'watermelon']`. The key is the length.

### Example 3 — Sort dictionaries by score
```python
students = [{"name":"Ali","score":80},{"name":"Maya","score":95}]
print([s["name"] for s in sorted(students,key=lambda s:s["score"],reverse=True)])
```
Output: `['Maya', 'Ali']`.

### Example 4 — Case-insensitive sort
```python
names = ["maya","Ali","noor"]
print(sorted(names,key=str.casefold))
```
Output: `['Ali', 'maya', 'noor']`.

### Example 5 — Multi-key sort
```python
rows = [("Ali",80),("Maya",90),("Ali",70)]
print(sorted(rows,key=lambda row:(row[0], -row[1])))
```
Output: `[('Ali', 80), ('Ali', 70), ('Maya', 90)]`. Sort name ascending and score descending inside each name.

## 5. Five tasks with solutions
### Task 1 — Sort by absolute size
```python
values = [-8,3,-2,5]
print(sorted(values,key=abs))
```
Output: `[-2, 3, 5, -8]`.

### Task 2 — Sort products by price
```python
products=[{"name":"Pen","price":10},{"name":"Book","price":50}]
print([p["name"] for p in sorted(products,key=lambda p:p["price"])])
```
Output: `['Pen', 'Book']`.

### Task 3 — Sort strings by length then alphabetically
```python
words=["pear","fig","plum","apple"]
print(sorted(words,key=lambda word:(len(word),word)))
```
Output: `['fig', 'pear', 'plum', 'apple']`.

### Task 4 — Sort without mutating source
```python
items=[3,1,2]
result=sorted(items)
print(result, items)
```
Output: `[1, 2, 3] [3, 1, 2]`.

### Task 5 — Named key alternative
```python
def score_key(student): return student["score"]
students=[{"name":"A","score":3},{"name":"B","score":1}]
print([x["name"] for x in sorted(students,key=score_key)])
```
Output: `['B', 'A']`. Named functions are suitable for reused logic.

## 6. Common mistakes
- `list.sort()` returns None.
- A lambda contains one expression, not a block of statements.
- Mixed incomparable types may raise TypeError.
- For ties, define a secondary key if order needs to be predictable.
- Sorting may be expensive for large inputs; Python's sort is generally O(n log n).

## 7. Interview Q&A
1. sorted vs sort? **New list vs in-place mutation.**
2. What is a key function? **Extracts the comparison value for each item.**
3. What is lambda? **An anonymous function expression.**
4. Is Python sort stable? **Yes.**
5. When use named function over lambda? **When reused or the logic needs a clear name.**

## 8. Project — Product Catalogue Sorter
Save as `product_sorter.py`.
```python
def sort_products(products, field="price", descending=False):
    if field not in {"name","price","rating"}: raise ValueError("Unsupported sort field")
    for product in products:
        if field not in product: raise ValueError(f"Missing field: {field}")
    return sorted(products,key=lambda product: product[field],reverse=descending)

def main():
    products=[{"name":"Pen","price":10,"rating":4.2},{"name":"Book","price":50,"rating":4.8}]
    print(sort_products(products,"price"))

if __name__ == "__main__": main()
```
Output lists Pen before Book by price.

### Tests — `test_product_sorter.py`
```python
import unittest
from product_sorter import sort_products

class SortTests(unittest.TestCase):
    def setUp(self): self.items=[{"name":"Pen","price":10,"rating":4},{"name":"Book","price":50,"rating":5}]
    def test_price(self): self.assertEqual(sort_products(self.items)[0]["name"],"Pen")
    def test_descending(self): self.assertEqual(sort_products(self.items,descending=True)[0]["name"],"Book")
    def test_name(self): self.assertEqual(sort_products(self.items,"name")[0]["name"],"Book")
    def test_invalid_field(self):
        with self.assertRaises(ValueError): sort_products(self.items,"id")
    def test_missing_field(self):
        with self.assertRaises(ValueError): sort_products([{"name":"x"}],"price")

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What does sorted return? **New sorted list.**
2. Does sort mutate? **Yes.**
3. What does key do? **Extracts sort key.**
4. Is sort stable? **Yes.**
5. Lambda body count? **One expression.**
**Challenge:** Sort students by score descending, then name ascending, and test ties.

## 10. Completion
- [ ] I can select a key and explain sort stability.
- [ ] Project tests pass.
- [ ] Tie-breaking challenge completed.
