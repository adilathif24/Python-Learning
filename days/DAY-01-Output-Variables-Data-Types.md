# Day 01 — Output, Variables, Data Types and Input

**Status:** Full study pack published; mark mastery only after running examples, solving tasks, and completing the mini-project.

## 1. Definition

- **Output:** showing information to a user, usually with `print()`.
- **Variable:** a name that refers to a value, created with assignment such as `name = "Adil"`.
- **Data type:** describes the kind of value, such as `int`, `float`, `str`, `bool`, or `NoneType`.
- **Input:** data collected from a user with `input()`. The returned value is a string until converted.

## 2. Why, where, when — and when not

Use variables to store values that your program will reuse; data types to choose valid operations; `input()` for simple command-line interaction; and `print()` to display results. Do not rely on a variable's name to enforce its type: Python is dynamically typed. Do validate and convert user input before doing arithmetic. For production applications, input validation needs to handle malformed input and sensible limits.

## 3. Syntax and rules

```python
name = "Adil"        # str
age = 23             # int
height = 1.80        # float
is_learning = True   # bool
nothing = None       # NoneType

print(name, age)
user_name = input("Enter name: ")
age = int(input("Enter age: "))
```

Names are case-sensitive, must not start with a digit, and should use descriptive snake_case names. `input()` returns text. Convert only when the content is valid for the intended type. `type(value)` helps inspect a value's type.

### Dry run

For `quantity_text = "3"`, the value is text. `quantity = int(quantity_text)` converts it to integer 3, and `quantity * 2` produces 6. Without conversion, `"3" * 2` produces `"33"`.

## 4. Five worked examples

### Example 1 — Print a welcome message

**Question:** Display a message on two lines.

```python
print("Welcome to Python!")
print("Let's start learning.")
```

**Output**
```text
Welcome to Python!
Let's start learning.
```

**Explanation:** Each `print()` call ends with a newline by default.

### Example 2 — Store and display profile data

```python
name = "Adil"
age = 23
print(f"My name is {name} and I am {age} years old.")
```

**Output**
```text
My name is Adil and I am 23 years old.
```

**Explanation:** An f-string inserts variable values inside braces.

### Example 3 — Inspect data types

```python
count = 4
price = 49.5
title = "Notebook"
in_stock = True

print(type(count).__name__)
print(type(price).__name__)
print(type(title).__name__)
print(type(in_stock).__name__)
```

**Output**
```text
int
float
str
bool
```

**Explanation:** `type(value).__name__` prints the readable type name.

### Example 4 — Convert input before adding

```python
first_text = "12"
second_text = "8"
total = int(first_text) + int(second_text)
print(total)
```

**Output**
```text
20
```

**Explanation:** Conversion makes the plus sign perform numeric addition rather than text concatenation.

### Example 5 — Format a calculation

```python
unit_price = 12.5
quantity = 4
total = unit_price * quantity
print(f"Total: ₹{total:.2f}")
```

**Output**
```text
Total: ₹50.00
```

**Explanation:** `:.2f` formats the number to two decimal places.

## 5. Five practice tasks with complete solutions

### Task 1 — Personal introduction

**Requirement:** Store a name and city and print both.

```python
name = "Adil"
city = "Hyderabad"
print(f"{name} lives in {city}.")
```

**Output:** `Adil lives in Hyderabad.`  
**Explanation:** Variables avoid repeating literal values.

### Task 2 — Add two numbers

**Requirement:** Add two integer values stored as text.

```python
a_text = "15"
b_text = "27"
answer = int(a_text) + int(b_text)
print(answer)
```

**Output:** `42`  
**Explanation:** Convert each string before addition.

### Task 3 — Rectangle area

**Requirement:** Calculate area from width and height.

```python
width = 8
height = 5
area = width * height
print(f"Area: {area}")
```

**Output:** `Area: 40`  
**Explanation:** A variable stores the calculation result for reuse.

### Task 4 — Convert minutes to seconds

```python
minutes = 7
seconds = minutes * 60
print(seconds)
```

**Output:** `420`  
**Explanation:** Store values with meaningful names and use the correct unit conversion.

### Task 5 — Safely parse a whole number

**Requirement:** Handle text that is not an integer.

```python
raw_value = "twenty"

try:
    value = int(raw_value)
except ValueError:
    print("Please enter a whole number.")
else:
    print(f"You entered {value}.")
```

**Output**
```text
Please enter a whole number.
```

**Explanation:** `int()` raises `ValueError` for non-numeric text; the try/except keeps the program from crashing.

## 6. Common mistakes and edge cases

- Assuming `input()` returns a number; it returns `str`.
- Using `int("3.5")`; this raises `ValueError`. Use `float("3.5")` when decimals are expected.
- Confusing `=` (assignment) with `==` (comparison).
- Naming a variable `class`, `for`, or another Python keyword.
- Using unclear names such as `x1` when `monthly_rent` is more meaningful.
- Assuming `"False"` is the Boolean `False`; it is a non-empty string.
- Handling empty input or unreasonable values only after they have already been used.

## 7. Interview questions and answers

**Q1. What is a variable?** A name bound to a value/object that a program can reference.

**Q2. What does dynamically typed mean?** A name is not permanently declared with a single type; values have types at runtime and a name can be rebound to a value of another type.

**Q3. What type does `input()` return?** `str`.

**Q4. Difference between `int` and `float`?** `int` represents whole numbers; `float` represents floating-point values, including decimals.

**Q5. What is an f-string?** A string literal prefixed with `f` that can evaluate expressions inside braces.

**Q6. Why catch `ValueError` when parsing input?** User-entered text may not represent the requested number.

## 8. Real-world mini-project — Simple Bill Generator

### Requirements
Calculate a bill from item name, unit price, and quantity; reject invalid values; show subtotal and tax.

```python
def create_bill(item_name, unit_price, quantity, tax_rate=0.05):
    if not item_name.strip():
        raise ValueError("Item name cannot be empty.")
    if unit_price < 0:
        raise ValueError("Unit price cannot be negative.")
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    subtotal = unit_price * quantity
    tax = subtotal * tax_rate
    return {
        "item": item_name.strip(),
        "quantity": quantity,
        "subtotal": subtotal,
        "tax": tax,
        "total": subtotal + tax,
    }


def main():
    try:
        item = input("Item name: ").strip()
        price = float(input("Unit price: "))
        qty = int(input("Quantity: "))
        bill = create_bill(item, price, qty)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(f"Item: {bill['item']}")
    print(f"Quantity: {bill['quantity']}")
    print(f"Subtotal: ₹{bill['subtotal']:.2f}")
    print(f"Tax (5%): ₹{bill['tax']:.2f}")
    print(f"Total: ₹{bill['total']:.2f}")


if __name__ == "__main__":
    main()
```

### Sample run

```text
Item name: Notebook
Unit price: 50
Quantity: 3
Item: Notebook
Quantity: 3
Subtotal: ₹150.00
Tax (5%): ₹7.50
Total: ₹157.50
```

### Tests

Save the program as `bill_generator.py`. Run the tests below with `python -m unittest -v`.

```python
import unittest
from bill_generator import create_bill


class TestBillGenerator(unittest.TestCase):
    def test_normal_bill(self):
        self.assertAlmostEqual(create_bill("Pen", 10, 2)["total"], 21)

    def test_zero_price_boundary(self):
        self.assertEqual(create_bill("Free sample", 0, 1)["total"], 0)

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            create_bill("   ", 10, 1)

    def test_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            create_bill("Pen", -1, 1)

    def test_zero_quantity_rejected(self):
        with self.assertRaises(ValueError):
            create_bill("Pen", 10, 0)


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. What type does `input()` return?
2. What is the output of `"4" * 3`?
3. What is the difference between `int` and `float`?
4. Which operator assigns a value?
5. Why might `int(user_text)` fail?

### Answer key
1. `str`.
2. `444`.
3. Integers represent whole numbers; floats represent floating-point values.
4. `=`.
5. The text may be empty or may not represent an integer.

### Independent challenge
Extend the bill generator to support a discount percentage. Validate that the discount is between 0 and 100, apply it before tax, and write tests for 0%, 100%, invalid discount, and a normal order.

## 10. Progress checklist

- [ ] I explained output, variables, types, and input from memory.
- [ ] I ran five examples and predicted the output before execution.
- [ ] I completed five tasks without initially copying the answers.
- [ ] The project tests pass.
- [ ] I solved the independent challenge.
