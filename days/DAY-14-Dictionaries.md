# Day 14 — Dictionaries and Nested Data

**Status:** Full study pack. Finish examples, tasks and tests before marking mastery.

## 1. Definition
A **dictionary** maps unique, hashable keys to values. It is mutable and preserves insertion order in modern Python. Nested dictionaries/lists model structured records such as user profiles, inventory, and API payloads.

## 2. Why, where, when
Use dictionaries for fast lookup by a meaningful key, configuration settings, counters, and JSON-like records. Use a list when order and duplicate items are central; use a set for uniqueness only. Choose simple, consistent key types and use `dict.get()` when a key may be missing.

## 3. Syntax and rules
```python
person = {"name": "Adil", "age": 23}
person["city"] = "Hyderabad"
age = person.get("age")
for key, value in person.items():
    print(key, value)
```
- `d[key]` raises KeyError when missing.
- `get(key, default)` returns a fallback without adding a key.
- Keys must be hashable; values may be mutable.
- `update` merges entries; `pop` removes and returns a value.
- Use `setdefault` sparingly, as it inserts a default for missing keys.

Dry run: `inventory["pen"] = inventory.get("pen", 0) + 1` initializes missing count to 0 and increments to 1.

## 4. Five worked examples

### Example 1 — Read and update
```python
student = {"name": "Ali", "score": 70}
student["score"] += 5
print(student["score"])
```
Output: `75`. Keys access and update values.

### Example 2 — Safe missing key
```python
profile = {"name": "Adil"}
print(profile.get("city", "Not provided"))
```
Output: `Not provided`. get avoids KeyError.

### Example 3 — Count items
```python
words = ["py", "sql", "py", "java", "py", "sql"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
```
Output: `{'py': 3, 'sql': 2, 'java': 1}`. The first occurrence starts at zero.

### Example 4 — Read nested data
```python
user = {"name": "Maya", "address": {"city": "Ongole", "pin": "523001"}}
print(user["address"]["city"])
```
Output: `Ongole`. Each key resolves the next nested object.

### Example 5 — Dict comprehension
```python
squares = {n: n*n for n in range(1, 5)}
print(squares)
```
Output: `{1: 1, 2: 4, 3: 9, 4: 16}`. A comprehension generates key/value pairs.

## 5. Five tasks with solutions

### Task 1 — Word frequency
```python
text = "red blue red green blue red"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq["red"], freq["blue"])
```
Output: `3 2`. Each occurrence increments its key.

### Task 2 — Merge settings
```python
defaults = {"theme": "light", "retries": 2}
user = {"theme": "dark"}
settings = {**defaults, **user}
print(settings)
```
Output: `{'theme': 'dark', 'retries': 2}`. Later mappings override earlier keys.

### Task 3 — Update nested data
```python
order = {"customer": "Ali", "items": [{"name": "Pen", "qty": 1}]}
order["items"][0]["qty"] += 2
print(order["items"][0]["qty"])
```
Output: `3`. First locate the list, then its dictionary item.

### Task 4 — Select a field safely
```python
record = {"name": "Asha", "age": 27}
print(record.get("email", "unknown"))
```
Output: `unknown`. A fallback is used when the key is absent.

### Task 5 — Invert a one-to-one mapping
```python
codes = {"IN": "India", "JP": "Japan"}
reverse = {country: code for code, country in codes.items()}
print(reverse["India"])
```
Output: `IN`. This assumes values are unique.

## 6. Common mistakes
- Direct access to missing keys raises KeyError.
- A dictionary key must be hashable.
- Duplicate keys in a literal overwrite earlier values.
- Nested mutation changes the underlying nested object.
- Inverting a dictionary loses information if values repeat.
- `get` does not insert a missing key; `setdefault` does.

## 7. Interview Q&A
1. What is a dictionary? **A mutable key/value mapping.**
2. Is insertion order preserved? **Yes, in Python 3.7+ language guarantees.**
3. `get` versus bracket access? **get supports a default; brackets raise KeyError when missing.**
4. Must values be hashable? **No, keys must be hashable; values can be lists/dicts.**
5. When is a dict comprehension useful? **Creating a mapping from iterable data with a rule.**

## 8. Project — Inventory Manager
Save as `inventory_manager.py`.
```python
def restock(inventory, name, quantity):
    name = name.strip().casefold()
    if not name: raise ValueError("Item name required")
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    inventory[name] = inventory.get(name, 0) + quantity
    return inventory[name]

def sell(inventory, name, quantity):
    name = name.strip().casefold()
    if quantity <= 0: raise ValueError("Quantity must be positive")
    available = inventory.get(name, 0)
    if quantity > available: raise ValueError("Insufficient stock")
    inventory[name] = available - quantity
    return inventory[name]

def main():
    stock = {}
    restock(stock, "Pen", 10)
    print("Stock:", stock)
    sell(stock, "Pen", 3)
    print("After sale:", stock)

if __name__ == "__main__": main()
```
Output: `Stock: {'pen': 10}` then `After sale: {'pen': 7}`.

### Tests — test_inventory_manager.py
```python
import unittest
from inventory_manager import restock, sell

class InventoryTests(unittest.TestCase):
    def test_restock(self):
        stock = {}; self.assertEqual(restock(stock, "Pen", 3), 3)
    def test_accumulate(self):
        stock = {}; restock(stock,"Pen",2); self.assertEqual(restock(stock,"pen",3),5)
    def test_sell(self):
        stock={"pen":5}; self.assertEqual(sell(stock,"PEN",2),3)
    def test_insufficient_stock(self):
        with self.assertRaises(ValueError): sell({"pen":1},"pen",2)
    def test_invalid_quantity(self):
        with self.assertRaises(ValueError): restock({}, "pen", 0)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Missing key with brackets? **KeyError.**
2. Can a list be a dictionary key? **No, it is unhashable.**
3. Does get insert a key? **No.**
4. What does items() provide? **Key/value pairs.**
5. What is a nested dictionary? **A dict with another dict as a value.**

**Challenge:** Add a low-stock report showing inventory items with quantity below a user-supplied threshold.

## Real-world use cases — where, when and how
1. **User profile:** Where: forms/API data. When fields are named. How: map field names to validated values.
2. **Inventory counts:** Where: stock tools. When quantities are retrieved by SKU. How: use SKU as key and increment values.
3. **Frequency counter:** Where: logs or word analysis. When occurrences matter. How: update counts with get(key, 0) + 1.
4. **Configuration:** Where: app startup. When named settings have defaults. How: merge user settings over defaults and validate types.
5. **Nested API payload:** Where: web services. When objects contain nested address/items fields. How: validate each level before indexing.


## 10. Completion
- [ ] I can explain dict access, update, counting and nesting.
- [ ] I solved all tasks and tested the project.
- [ ] I completed the challenge.
