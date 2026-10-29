# Day 07 — Lists in Python

**Status:** Full lesson pack published. Complete practice, tests and challenge before marking mastery.

## 1. Definition

A **list** is an ordered, mutable collection that can contain repeated values and values of different types. Lists support indexing, slicing, iteration and methods such as `append()`, `extend()`, `insert()`, `remove()`, `pop()` and `sort()`.

## 2. Why, where and when

Use lists for sequences such as shopping items, scores, tasks, or records that need order and updates. Use a tuple for a fixed grouping, a set for uniqueness/membership, and a dictionary for key-to-value lookups. Lists are not the best choice for fast membership checks in very large collections or for queue operations that remove from the front repeatedly.

## 3. Syntax and rules

```python
items = ["pen", "book", "bag"]
items.append("pencil")
items.insert(1, "notebook")
items.remove("book")
last = items.pop()
print(items, last)
```

- Indexing starts at 0; negative indices count from the end.
- Slicing returns a new list; the list itself can be modified.
- `append(x)` adds one item; `extend(iterable)` adds each item.
- `sort()` mutates a list and returns `None`; `sorted(list)` returns a new sorted list.
- Assignment such as `b = a` creates an alias, not a copy.
- A shallow copy duplicates only the outer list; nested mutable elements remain shared.

### Dry run

`values = [2, 4]`; `values.append(6)` → [2, 4, 6]; `values[1] = 9` → [2, 9, 6]. The original list is changed.

## 4. Five worked examples

### Example 1 — Indexing and slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
```
**Output**
```text
10
50
[20, 30, 40]
```
**Explanation:** The slice stop index is excluded.

### Example 2 — Append versus extend

```python
a = [1, 2]
a.append([3, 4])
b = [1, 2]
b.extend([3, 4])
print(a)
print(b)
```
**Output**
```text
[1, 2, [3, 4]]
[1, 2, 3, 4]
```
**Explanation:** `append` stores its argument as one item; `extend` iterates over it.

### Example 3 — Remove safely using pop

```python
tasks = ["study", "practice", "revise"]
removed = tasks.pop(1)
print(removed)
print(tasks)
```
**Output**
```text
practice
['study', 'revise']
```
**Explanation:** `pop(index)` returns the removed element.

### Example 4 — Sort and preserve the original

```python
scores = [70, 45, 90, 60]
ordered = sorted(scores)
print(ordered)
print(scores)
```
**Output**
```text
[45, 60, 70, 90]
[70, 45, 90, 60]
```
**Explanation:** `sorted()` returns a new list and leaves the input unchanged.

### Example 5 — Copy versus alias

```python
original = [1, 2, 3]
alias = original
copy = original.copy()
alias.append(4)
print(original)
print(copy)
```
**Output**
```text
[1, 2, 3, 4]
[1, 2, 3]
```
**Explanation:** The alias points to the same list; the copy is a separate outer list.

## 5. Five practice tasks with complete solutions

### Task 1 — Sum scores

```python
scores = [75, 80, 90, 65]
print(sum(scores))
```
**Output:** `310`  
**Explanation:** `sum()` accumulates numeric values.

### Task 2 — Remove duplicates while preserving order

```python
values = [3, 1, 3, 2, 1, 4]
unique = []
for value in values:
    if value not in unique:
        unique.append(value)
print(unique)
```
**Output:** `[3, 1, 2, 4]`  
**Explanation:** Append a value only when it has not appeared earlier. This simple approach is not the fastest for very large lists.

### Task 3 — Find the second-largest distinct value

```python
values = [10, 30, 20, 30, 10]
distinct = sorted(set(values))
if len(distinct) < 2:
    print("No second-largest distinct value")
else:
    print(distinct[-2])
```
**Output:** `20`  
**Explanation:** The set removes duplicates; sorted order makes the second-largest distinct item available at index -2.

### Task 4 — Reverse without changing the original

```python
values = [1, 2, 3, 4]
reversed_values = values[::-1]
print(reversed_values)
print(values)
```
**Output**
```text
[4, 3, 2, 1]
[1, 2, 3, 4]
```
**Explanation:** Slicing creates a reversed shallow copy.

### Task 5 — Validate an index

```python
items = ["a", "b", "c"]
index = 4
if 0 <= index < len(items):
    print(items[index])
else:
    print("Index out of range")
```
**Output:** `Index out of range`  
**Explanation:** Validate before indexing to avoid `IndexError`.

## 6. Common mistakes and edge cases

- An empty list has no element at index 0.
- Calling `remove(x)` for an absent value raises `ValueError`.
- Calling `pop()` on an empty list raises `IndexError`.
- `list.sort()` returns `None`; do not write `sorted_values = items.sort()`.
- `b = a` is aliasing, not copying.
- `copy()` is shallow; nested objects may still be shared.
- Modifying a list while iterating over it can skip items; build a new list or iterate over a copy.
- Lists support unhashable values, so they cannot themselves be set elements or dictionary keys.

## 7. Interview questions and answers

**Q1. Is a list mutable?** Yes; elements can be added, removed or replaced.

**Q2. Difference between `append` and `extend`?** Append adds one object; extend adds each item from an iterable.

**Q3. Difference between `sort()` and `sorted()`?** `sort()` modifies a list in place and returns `None`; `sorted()` returns a new sorted list.

**Q4. What is aliasing?** Multiple names refer to the same object.

**Q5. What is a shallow copy?** A copy of the outer container that retains references to the same nested objects.

**Q6. When should you use a set instead?** When uniqueness and fast membership checks are more important than preserving duplicates and positional indexing.

## 8. Real-world mini-project — Shopping Cart

Save as `shopping_cart_list.py`. The cart supports adding items, removing items, and calculating totals.

```python
def add_item(cart, name, price, quantity=1):
    if not name.strip():
        raise ValueError("Item name is required.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    cart.append({"name": name.strip(), "price": float(price), "quantity": quantity})


def remove_item(cart, name):
    for index, item in enumerate(cart):
        if item["name"].casefold() == name.casefold():
            return cart.pop(index)
    return None


def cart_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


def main():
    cart = []
    while True:
        print("\n1 Add  2 List  3 Total  4 Remove  5 Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                name = input("Item name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                add_item(cart, name, price, quantity)
                print("Added")
            except ValueError as error:
                print(f"Invalid item: {error}")
        elif choice == "2":
            for item in cart:
                print(item)
            if not cart:
                print("Cart is empty")
        elif choice == "3":
            print(f"Total: ₹{cart_total(cart):.2f}")
        elif choice == "4":
            removed = remove_item(cart, input("Item name: "))
            print("Removed" if removed else "Item not found")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Choose 1–5")


if __name__ == "__main__":
    main()
```

### Sample result
Adding 2 notebooks at ₹40 each produces a cart total of ₹80.00.

### Tests

Save as `test_shopping_cart_list.py`; run `python -m unittest -v`.

```python
import unittest
from shopping_cart_list import add_item, remove_item, cart_total


class TestShoppingCart(unittest.TestCase):
    def test_add_and_total(self):
        cart = []
        add_item(cart, "Notebook", 40, 2)
        self.assertEqual(cart_total(cart), 80)

    def test_remove_item(self):
        cart = []
        add_item(cart, "Pen", 10)
        self.assertIsNotNone(remove_item(cart, "pen"))
        self.assertEqual(cart, [])

    def test_remove_missing_item(self):
        self.assertIsNone(remove_item([], "unknown"))

    def test_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            add_item([], "Pen", -1)

    def test_invalid_quantity_rejected(self):
        with self.assertRaises(ValueError):
            add_item([], "Pen", 2, 0)


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. Are lists mutable?
2. What is the difference between `append` and `extend`?
3. What does `list.sort()` return?
4. Does `b = a.copy()` deep-copy nested lists?
5. What exception can `pop()` on an empty list raise?

### Answer key
1. Yes.
2. Adds one object versus adding every item from an iterable.
3. `None`.
4. No, it is a shallow copy.
5. `IndexError`.

### Independent challenge
Add a quantity-update method to the cart, reject an unknown item, and test updating an item, zero quantity, and updating an empty cart.

## 10. Progress checklist

- [ ] I can explain list indexing, slicing, methods, sorting, copying and aliasing.
- [ ] I tried all examples and tasks before reading solutions.
- [ ] Shopping-cart tests pass.
- [ ] I completed the independent challenge.

## Real-world use cases — where, when and how
1. **Shopping cart:** Where: checkout. When: items need ordered updates. How: append product records and sum item totals.
2. **Task queue:** Where: simple task manager. When: ordered work is shown. How: store task records in a list and update completion flags.
3. **Score analysis:** Where: class reports. When: scores are collected in order. How: filter or aggregate values and preserve the raw list.
4. **API result processing:** Where: web clients. When: a JSON array is returned. How: iterate and build a filtered list of valid records.
5. **History/undo:** Where: small interactive apps. When: prior actions must be recorded. How: append events and pop the latest event when undoing.

