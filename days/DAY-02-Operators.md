# Day 02 — Python Operators

**Status:** Full study pack published; complete the examples, tasks, project, tests and quiz before marking mastery.

## 1. Definition

An **operator** is a symbol or keyword that performs an operation on values (operands). Python has arithmetic, comparison, assignment, logical, identity, membership, and bitwise operators.

## 2. Why, where and when

Use arithmetic operators for calculations, comparisons for decisions, logical operators to combine conditions, assignment operators to update values, membership operators to check whether an item occurs in a collection, and identity operators to test whether two names refer to the same object. Prefer `==` for value equality and `is None` to check for `None`. Do not use `is` as a substitute for numeric or string equality. Bitwise operators are useful for bit flags and low-level data, but usually unnecessary for ordinary business rules.

## 3. Syntax and rules

| Category | Operators | Example |
|---|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `7 // 2 == 3` |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` | `age >= 18` |
| Assignment | `=`, `+=`, `-= `, `*= `, `/=` | `count += 1` |
| Logical | `and`, `or`, `not` | `is_active and has_access` |
| Membership | `in`, `not in` | `"py" in "python"` |
| Identity | `is`, `is not` | `result is None` |
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>` | `5 & 1` |

Division with `/` returns a float. Floor division `//` rounds down toward negative infinity. Modulo `%` gives the remainder. Parentheses make intended order explicit. Comparison operators can be chained, for example `0 <= score <= 100`.

### Dry run

For `total = 10`, then `total += 4`, the augmented assignment is equivalent to `total = total + 4`; the new value is 14.

## 4. Five worked examples

### Example 1 — Arithmetic

**Question:** Find quotient and remainder when 17 is divided by 5.

```python
a = 17
b = 5
print(a / b)
print(a // b)
print(a % b)
```

**Output**
```text
3.4
3
2
```

**Explanation:** True division returns a float, floor division returns the floor, and modulo returns the remainder.

### Example 2 — Comparison and boundaries

```python
age = 18
print(age >= 18)
print(age == 18)
print(age < 18)
```

**Output**
```text
True
True
False
```

**Explanation:** The boundary 18 satisfies both `>= 18` and `== 18`.

### Example 3 — Logical operators

```python
is_member = True
spend = 1200
free_delivery = is_member and spend >= 1000
coupon_applies = is_member or spend >= 2000
print(free_delivery)
print(coupon_applies)
print(not is_member)
```

**Output**
```text
True
True
False
```

**Explanation:** `and` requires both conditions, `or` requires at least one, and `not` reverses truth value.

### Example 4 — Membership and identity

```python
roles = ["reader", "editor"]
user_role = "editor"
result = None

print(user_role in roles)
print("admin" not in roles)
print(result is None)
```

**Output**
```text
True
True
True
```

**Explanation:** Membership checks collection contents. Identity is used here for the `None` singleton.

### Example 5 — Update a running total

```python
balance = 1000
balance += 250
balance -= 80
balance *= 2
print(balance)
```

**Output**
```text
2340
```

**Explanation:** Each augmented assignment uses the latest balance: 1000 → 1250 → 1170 → 2340.

## 5. Five practice tasks with solutions

### Task 1 — Calculate a rectangle

```python
width = 9
height = 4
perimeter = 2 * (width + height)
area = width * height
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
```

**Output**
```text
Area: 36
Perimeter: 26
```

**Explanation:** Parentheses clarify the perimeter formula.

### Task 2 — Convert seconds to minutes and seconds

```python
total_seconds = 367
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{minutes} minute(s), {seconds} second(s)")
```

**Output:** `6 minute(s), 7 second(s)`  
**Explanation:** Floor division finds whole minutes; modulo finds leftover seconds.

### Task 3 — Check range

```python
temperature = 22
print(18 <= temperature <= 26)
```

**Output:** `True`  
**Explanation:** Both endpoints are inclusive.

### Task 4 — Apply a 15% discount

```python
price = 800
discount_rate = 0.15
final_price = price * (1 - discount_rate)
print(f"₹{final_price:.2f}")
```

**Output:** `₹680.00`  
**Explanation:** The customer pays 85% of the original price.

### Task 5 — Check access

```python
account_active = True
has_permission = False
maintenance_mode = False
allowed = account_active and has_permission and not maintenance_mode
print("Allowed" if allowed else "Denied")
```

**Output:** `Denied`  
**Explanation:** An active account with no permission is denied; all required conditions must pass.

## 6. Common mistakes and edge cases

- `/` and `//` are not interchangeable.
- `//` with negative values rounds down: `-7 // 2 == -4`.
- Dividing or taking modulo by zero raises `ZeroDivisionError`.
- `^ ` is bitwise XOR, not exponentiation; exponentiation is `**`.
- `is` checks object identity, not general value equality.
- Parenthesise complex expressions and avoid relying on readers to remember precedence.
- Floats can have binary rounding effects; use `Decimal` for suitable decimal-money applications.
- `and`/`or` short-circuit and can return an operand rather than always returning a Boolean.

## 7. Interview questions and answers

**Q1. Difference between `/` and `//`?** `/` performs true division; `//` floors the quotient.

**Q2. Difference between `==` and `is`?** `==` compares values; `is` checks whether two references point to the same object.

**Q3. What does modulo do?** It returns the remainder from division.

**Q4. What is short-circuit evaluation?** Python skips evaluating the right operand when the left operand already determines the result of `and` or `or`.

**Q5. How do augmented assignments work?** They combine an operation with assignment, such as `x += 1` for updating `x`.

**Q6. Why use parentheses?** To make grouping explicit and prevent mistakes in complex expressions.

## 8. Real-world mini-project — Shopping Cart Total

The program calculates subtotal, discount eligibility and delivery fee. Free delivery is available to members with a subtotal of at least ₹1,000; a 10% discount applies at ₹2,000 or more.

```python
def calculate_cart(prices, is_member):
    if not prices:
        subtotal = 0.0
    elif any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")
    else:
        subtotal = sum(prices)

    discount = subtotal * 0.10 if subtotal >= 2000 else 0.0
    delivery_fee = 0.0 if is_member and subtotal >= 1000 else (50.0 if subtotal > 0 else 0.0)
    total = subtotal - discount + delivery_fee
    return {
        "subtotal": subtotal,
        "discount": discount,
        "delivery_fee": delivery_fee,
        "total": total,
    }


def main():
    try:
        raw = input("Enter prices separated by commas (e.g. 300,450): ").strip()
        prices = [] if not raw else [float(piece.strip()) for piece in raw.split(",")]
        member_text = input("Member? (y/n): ").strip().lower()
        if member_text not in {"y", "n"}:
            raise ValueError("Member response must be y or n.")
        bill = calculate_cart(prices, member_text == "y")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(f"Subtotal: ₹{bill['subtotal']:.2f}")
    print(f"Discount: ₹{bill['discount']:.2f}")
    print(f"Delivery: ₹{bill['delivery_fee']:.2f}")
    print(f"Total: ₹{bill['total']:.2f}")


if __name__ == "__main__":
    main()
```

### Sample run

```text
Enter prices separated by commas (e.g. 300,450): 1200,900
Member? (y/n): y
Subtotal: ₹2100.00
Discount: ₹210.00
Delivery: ₹0.00
Total: ₹1890.00
```

### Tests

Save the main file as `shopping_cart.py` and this test as `test_shopping_cart.py`. Run `python -m unittest -v`.

```python
import unittest
from shopping_cart import calculate_cart


class TestShoppingCart(unittest.TestCase):
    def test_member_free_delivery(self):
        self.assertEqual(calculate_cart([600, 400], True)["delivery_fee"], 0.0)

    def test_non_member_delivery_fee(self):
        self.assertEqual(calculate_cart([1000], False)["delivery_fee"], 50.0)

    def test_discount_boundary(self):
        self.assertEqual(calculate_cart([2000], False)["discount"], 200.0)

    def test_empty_cart(self):
        self.assertEqual(calculate_cart([], False)["total"], 0.0)

    def test_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            calculate_cart([-1], True)


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. What is `17 // 5`?
2. What is `17 % 5`?
3. Which operator checks value equality?
4. What does `not True` evaluate to?
5. What does `2 ** 3` calculate?

### Answer key
1. `3`.
2. `2`.
3. `==`.
4. `False`.
5. `8`.

### Independent challenge
Add a coupon rule: if the customer is a member **or** subtotal reaches ₹3,000, subtract an additional fixed ₹100 after percentage discount. Ensure the total can never be negative, and add tests for the exact ₹3,000 threshold and an empty cart.

## 10. Progress checklist

- [ ] I explained arithmetic, comparison, logical, assignment, membership and identity operators.
- [ ] I ran the worked examples and predicted outputs first.
- [ ] I attempted all five tasks independently.
- [ ] All shopping-cart tests pass.
- [ ] I solved the independent challenge and explained the conditions.
