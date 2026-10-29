# Day 10 — Function Fundamentals: Default Arguments, Scope, Docstrings and Validation

> **Status:** Next — complete the examples and tasks before moving on.  
> **Prerequisites:** `def`, parameters, arguments, `return`, positional arguments, keyword arguments, `*args`, and `**kwargs`.

## 1. Definition

A **function** is a named, reusable block of code that performs a particular task. Parameters are the names in the function definition; arguments are the actual values supplied when calling the function.

This lesson strengthens functions by teaching default values, positional and keyword calling, scope, docstrings, and argument validation.

## 2. Why, where and when to use these concepts

- **Default arguments:** use when a sensible value should be used if the caller omits an argument, such as a default tax rate or greeting.
- **Keyword arguments:** use when clarity matters or a function has several parameters.
- **Scope:** understand where a variable can be accessed. Prefer local variables and explicit return values over unnecessary global state.
- **Docstrings:** document what a function does, its arguments and its return value.
- **Validation:** reject invalid inputs early with clear messages or exceptions.
- Do not use mutable objects such as lists as default arguments unless you deliberately understand the shared-object behaviour. Prefer `None` and create a new list inside the function.

## 3. Syntax

```python
def function_name(required_parameter, optional_parameter="default"):
    """Explain what the function does."""
    # function body
    return result

value = function_name("required value")
value2 = function_name("required value", optional_parameter="custom")
```

Rules:
1. Required parameters normally come before parameters with default values.
2. Positional arguments are matched by position; keyword arguments are matched by parameter name.
3. Variables created inside a function are normally local to that function.
4. `return` sends a value back to the caller; `print()` only displays it.
5. Validate assumptions at the function boundary.

---

## 4. Five worked examples

### Example 1 — Default argument

**Problem:** Greet a person. If no name is provided, use “Guest”.

**Complete code**
```python
def greet(name="Guest"):
    """Return a friendly greeting for a person."""
    return f"Hello, {name}!"

print(greet())
print(greet("Adil"))
```

**Output**
```text
Hello, Guest!
Hello, Adil!
```

**Explanation:** `name="Guest"` supplies a fallback value. `greet()` uses it; `greet("Adil")` replaces it. The function returns a string, and `print()` displays it.

### Example 2 — Positional and keyword arguments

**Problem:** Calculate the price after a discount.

**Complete code**
```python
def discounted_price(price, discount_percent=0):
    """Return a price after applying a percentage discount."""
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")
    return price * (1 - discount_percent / 100)

print(discounted_price(1000, 10))
print(discounted_price(price=2000, discount_percent=25))
print(discounted_price(price=500))
```

**Output**
```text
900.0
1500.0
500.0
```

**Explanation:** The first call uses positions; the second names each argument; the third relies on the default discount of zero. The checks reject impossible prices and discounts.

### Example 3 — Local scope

**Problem:** Show that a function's local variable does not replace a variable outside it.

**Complete code**
```python
message = "Outside function"

def show_message():
    message = "Inside function"
    print(message)

show_message()
print(message)
```

**Output**
```text
Inside function
Outside function
```

**Explanation:** The assignment inside the function creates a local variable named `message`. The outer variable remains unchanged.

### Example 4 — Docstring and return value

**Problem:** Create a function that calculates the area of a rectangle and documents itself.

**Complete code**
```python
def rectangle_area(length, width):
    """Return the area of a rectangle.

    Args:
        length: Rectangle length, greater than or equal to zero.
        width: Rectangle width, greater than or equal to zero.

    Returns:
        The area as a number.
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")
    return length * width

print(rectangle_area(5, 3))
print(rectangle_area.__doc__)
```

**Output**
```text
15
Return the area of a rectangle.

    Args:
        length: Rectangle length, greater than or equal to zero.
        width: Rectangle width, greater than or equal to zero.

    Returns:
        The area as a number.
```

**Explanation:** The triple-quoted string immediately after `def` is the docstring. It is accessible through `__doc__`. Validation happens before calculation.

### Example 5 — Safe list default

**Problem:** Return a user's tasks without sharing a mutable default list between calls.

**Complete code**
```python
def make_task_list(tasks=None):
    """Return a new list containing the supplied tasks."""
    if tasks is None:
        tasks = []
    return list(tasks)

first = make_task_list()
second = make_task_list(["Study Python"])
first.append("Practise functions")

print(first)
print(second)
```

**Output**
```text
['Practise functions']
['Study Python']
```

**Explanation:** `None` means no list was supplied. A fresh list is created for each call. `list(tasks)` also makes a shallow copy of a supplied iterable.

---

## 5. Five practice tasks — each with full solution

### Task 1 — Personalised greeting

**Requirements:** Accept a name and an optional greeting word. Default greeting is `Hello`.

**Sample output**
```text
Hello, Adil!
Welcome, Sara!
```

**Solution**
```python
def greet_person(name, greeting="Hello"):
    """Return a greeting for a person."""
    return f"{greeting}, {name}!"

print(greet_person("Adil"))
print(greet_person("Sara", greeting="Welcome"))
```

**Explanation:** The second parameter has a default. The second call overrides it using a keyword argument.

### Task 2 — Convert kilometres to miles

**Requirements:** Use 1 kilometre = 0.621371 miles. Reject negative distance.

**Sample output**
```text
6.214 miles
```

**Solution**
```python
def km_to_miles(kilometres):
    """Convert a non-negative distance from kilometres to miles."""
    if kilometres < 0:
        raise ValueError("Distance cannot be negative.")
    return kilometres * 0.621371

print(f"{km_to_miles(10):.3f} miles")
```

**Explanation:** Validate first, calculate second, return the result. The formatted string shows three decimal places.

### Task 3 — Calculate an order total

**Requirements:** Accept subtotal and optional delivery fee (default 0). Reject negative amounts.

**Sample output**
```text
1050
```

**Solution**
```python
def order_total(subtotal, delivery_fee=0):
    """Calculate subtotal plus delivery fee."""
    if subtotal < 0 or delivery_fee < 0:
        raise ValueError("Amounts cannot be negative.")
    return subtotal + delivery_fee

print(order_total(1000, delivery_fee=50))
```

**Explanation:** The named argument makes the call easier to understand. The returned number can be reused elsewhere.

### Task 4 — Use local scope and return a result

**Requirements:** Add two numbers using a local variable named `total`. Do not use a global variable.

**Sample output**
```text
15
```

**Solution**
```python
def add_numbers(a, b):
    """Return the sum of two numbers."""
    total = a + b
    return total

answer = add_numbers(7, 8)
print(answer)
```

**Explanation:** `total` belongs to the function. The caller receives the result through `return`.

### Task 5 — Validate a percentage

**Requirements:** Return `True` only if a score is between 0 and 100 inclusive.

**Sample output**
```text
True
False
False
```

**Solution**
```python
def is_valid_score(score):
    """Return whether score is within the inclusive 0–100 range."""
    return isinstance(score, (int, float)) and not isinstance(score, bool) and 0 <= score <= 100

print(is_valid_score(85))
print(is_valid_score(120))
print(is_valid_score(-2))
```

**Explanation:** The range check accepts both endpoints. The type check prevents strings and booleans from being treated as ordinary scores.

---

## 6. Real-world project — Order Total Calculator

### Purpose

A small shop needs to calculate a customer's order total, apply an optional discount, and optionally add delivery. This is an educational console program, not a payment system.

### Complete runnable code

Save as `day10_order_total_calculator.py`.

```python
def calculate_order_total(subtotal, discount_percent=0, delivery_fee=0):
    """Calculate the final order total after discount and delivery.

    Args:
        subtotal: Order amount before discount; must be non-negative.
        discount_percent: Discount percentage from 0 to 100.
        delivery_fee: Non-negative delivery charge.

    Returns:
        Final amount after discount plus delivery.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")
    if delivery_fee < 0:
        raise ValueError("Delivery fee cannot be negative.")

    discount_amount = subtotal * discount_percent / 100
    discounted_subtotal = subtotal - discount_amount
    return discounted_subtotal + delivery_fee


def main():
    """Collect order values and display the total."""
    try:
        subtotal = float(input("Enter subtotal: "))
        discount = float(input("Enter discount percentage (0-100): "))
        delivery = float(input("Enter delivery fee: "))

        total = calculate_order_total(
            subtotal,
            discount_percent=discount,
            delivery_fee=delivery,
        )

        print(f"Final order total: ₹{total:.2f}")
    except ValueError as error:
        print(f"Invalid order: {error}")


if __name__ == "__main__":
    main()
```

### Example run

```text
Enter subtotal: 1000
Enter discount percentage (0-100): 10
Enter delivery fee: 50
Final order total: ₹950.00
```

### How it works

1. `calculate_order_total()` validates all amounts.
2. It calculates the discount as `subtotal * discount_percent / 100`.
3. It subtracts the discount and adds delivery.
4. `main()` reads input and calls the calculation function.
5. `try/except` displays a clear message if input conversion or validation fails.
6. The `if __name__ == "__main__":` guard runs `main()` only when this file is executed directly.

### Test cases

| Subtotal | Discount | Delivery | Expected result |
|---:|---:|---:|---:|
| 1000 | 10 | 50 | 950 |
| 500 | 0 | 0 | 500 |
| 100 | 100 | 20 | 20 |
| -1 | 10 | 0 | Raises validation error |
| 100 | 101 | 0 | Raises validation error |
| 100 | 10 | -5 | Raises validation error |

### Limitations and improvements

- Uses floating-point arithmetic for a learning exercise; production money calculations should use `decimal.Decimal`.
- Does not save orders or process payments.
- Could be improved with a product cart, receipt, unit tests, and persistent storage.

---

## 7. Common mistakes

### Mistake 1 — Put a required parameter after a default parameter

Incorrect:
```python
# def order_total(delivery_fee=0, subtotal):  # SyntaxError
#     return subtotal + delivery_fee
```

Correct:
```python
def order_total(subtotal, delivery_fee=0):
    return subtotal + delivery_fee

print(order_total(100, 10))
```

### Mistake 2 — Expect `print()` to return a value

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)  # None
```

Use `return a + b` if the caller needs the result.

### Mistake 3 — Modify a global variable unnecessarily

Prefer passing a value into a function and returning the result rather than relying on hidden global state.

### Mistake 4 — Use a list as a default argument

Avoid `def add_item(item, items=[]):`. That list can be shared between calls. Use `items=None` and create a new list inside the function.

### Mistake 5 — Skip validation

Invalid values can silently produce nonsensical results. Validate boundaries before performing calculations.

---

## 8. Interview questions and answers

**Q1. What is a default argument?**  
A parameter value used when the caller does not supply that argument.

**Q2. What is the difference between a parameter and an argument?**  
A parameter is a name in the function definition; an argument is the value passed during a call.

**Q3. What is local scope?**  
A local variable is created inside a function and is normally accessible only within that function.

**Q4. Why should mutable default arguments be avoided?**  
The same mutable object can be reused across calls, causing unexpected shared state. Use `None` and create the object inside the function.

**Q5. What is a docstring?**  
A string literal at the beginning of a module, class or function that documents its purpose and behaviour.

**Q6. What is the difference between `return` and `print()`?**  
`return` sends a value to the caller; `print()` displays text to the console.

**Q7. Why validate function arguments?**  
To detect invalid values early and produce predictable results and clear errors.

**Q8. What does `if __name__ == "__main__":` do?**  
It runs the guarded code when the file is executed directly, but not when the file is imported as a module.

---

## 9. Revision quiz

1. What value does `greet()` use if `name="Guest"` is the default?
2. In `discounted_price(price=100, discount_percent=5)`, which arguments are keyword arguments?
3. Does assigning to a local variable normally change an outer variable with the same name?
4. Why is `items=None` safer than `items=[]` as a default?
5. What is the difference between a docstring and a comment?
6. Why does a function often return a value instead of printing it?

**Answers:** 1. `Guest`. 2. Both. 3. No. 4. It avoids reusing one mutable list across calls. 5. A docstring documents an object and is available at runtime; a comment is explanatory source text. 6. Returned values can be stored, tested, combined, or passed to another function.

## 10. Independent challenge

Extend the Order Total Calculator so it:
- accepts a coupon discount and a delivery fee;
- rejects non-numeric input and negative amounts;
- prints a receipt showing subtotal, discount amount, delivery fee, and final total;
- uses at least three small functions;
- includes five test cases.

Do not mark Day 10 complete until you can explain and run the examples, solve the tasks independently, and test the project.
