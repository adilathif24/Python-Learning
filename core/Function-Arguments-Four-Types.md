# Python Function Arguments — Four Practical Types

This guide covers the four patterns requested: **single argument, multiple arguments, named (keyword) arguments, and arbitrary arguments**. Python also has more precise parameter categories, including default, positional-only, and keyword-only parameters.

## What is an argument?

A **parameter** is a name in a function definition. An **argument** is the value supplied when calling the function.

```python
def greet(name):       # name is a parameter
    print("Hello", name)

greet("Adil")          # "Adil" is an argument
# Output: Hello Adil
```

## 1. Single argument

A function receives one value.

```python
def square(number):
    return number * number

print(square(5))  # 25
```

**Explanation:** The argument `5` is assigned to `number`; the function returns its square. Use this pattern when an operation needs one input.

## 2. Multiple positional arguments

A function receives a known number of values matched to parameters by position.

```python
def calculate_total(price, quantity):
    return price * quantity

print(calculate_total(120, 3))  # 360
```

**Explanation:** `price=120` and `quantity=3`; the returned total is `120 * 3`. Use this when an operation needs a fixed set of inputs.

## 3. Named (keyword) arguments

Pass values by writing each parameter name. Keyword arguments can be supplied in a different order.

```python
def introduce(name, age, city):
    print(f"My name is {name}, I am {age}, and I live in {city}.")

introduce(city="Hyderabad", name="Adil", age=23)
```

Output: `My name is Adil, I am 23, and I live in Hyderabad.`

**Why use it?** Keyword arguments improve readability when a function has multiple parameters. A parameter must not receive a value twice.

## 4. Arbitrary (variable-length) arguments

### A. `*args`: arbitrary positional arguments

Python collects the extra positional values into a tuple.

```python
def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(10))          # 10
print(add_numbers(10, 20, 30))  # 60
print(add_numbers())            # 0
```

The name `numbers` is conventional; the asterisk is what makes the argument collection work.

### B. `**kwargs`: arbitrary keyword arguments

Python collects extra named values into a dictionary.

```python
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Adil", skill="Python", level="Beginner")
```

Output:
```text
name: Adil
skill: Python
level: Beginner
```

Use `*args` when the number of positional values can vary, and `**kwargs` when the number of named values can vary.

## Quick comparison

| Pattern | Example | Meaning |
|---|---|---|
| Single argument | `square(5)` | One input value |
| Multiple positional | `calculate_total(120, 3)` | Known parameters matched by position |
| Named/keyword | `introduce(name="Adil", age=23, city="Hyderabad")` | Values matched by parameter name |
| Arbitrary positional | `add_numbers(1, 2, 3)` with `*args` | Any number of positional values |
| Arbitrary keyword | `show_profile(name="Adil")` with `**kwargs` | Any number of named values |

The last two are both arbitrary arguments, but their collected types differ: `*args` creates a tuple and `**kwargs` creates a dictionary.

## Combine the patterns

```python
def register_user(username, *skills, city="Unknown", **extra_details):
    print("Username:", username)
    print("Skills:", skills)
    print("City:", city)
    print("Extra details:", extra_details)

register_user(
    "adil24", "Python", "SQL",
    city="Hyderabad", experience="Beginner", active=True
)
```

Output:
```text
Username: adil24
Skills: ('Python', 'SQL')
City: Hyderabad
Extra details: {'experience': 'Beginner', 'active': True}
```

- `username`: required parameter.
- `*skills`: gathers extra positional arguments into a tuple.
- `city="Unknown"`: default parameter.
- `**extra_details`: gathers extra keyword arguments into a dictionary.

## Seven interview questions with answers

**1. Parameter vs argument?** A parameter is defined in the function signature; an argument is passed by the caller.

**2. What is a positional argument?** A value matched to a parameter based on its position in the call.

**3. What is a keyword argument?** A value passed using the parameter name, such as `city="Hyderabad"`.

**4. What does `*args` do?** Collects extra positional arguments into a tuple.

**5. What does `**kwargs` do?** Collects extra keyword arguments into a dictionary.

**6. Can they be combined?** Yes. For example, `def f(required, *args, **kwargs):`. Default and keyword-only parameters are also possible with correct signature ordering.

**7. Should every function use arbitrary arguments?** No. Use them when the number of inputs is genuinely variable; explicit parameters are clearer for fixed inputs.

## Five practice questions with answers

### Practice 1 — Convert Celsius to Fahrenheit
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(celsius_to_fahrenheit(0))  # 32.0
```

### Practice 2 — Calculate a total price
```python
def total_price(unit_price, quantity):
    return unit_price * quantity

print(total_price(75, 4))  # 300
```

### Practice 3 — Use keyword arguments in reverse order
```python
def display_person(name, city):
    print(f"{name} lives in {city}.")

display_person(city="Ongole", name="Adil")
# Adil lives in Ongole.
```

### Practice 4 — Find the largest of arbitrary values
```python
def largest(*numbers):
    if not numbers:
        raise ValueError("Provide at least one number")
    return max(numbers)

print(largest(5, 12, 3))  # 12
```

### Practice 5 — Print arbitrary profile fields
```python
def print_profile(**fields):
    for key, value in fields.items():
        print(f"{key}: {value}")

print_profile(name="Adil", role="Learner", language="Python")
```

## Mini-project — Flexible Order Summary

This command-line example combines a required parameter, `*args`, and a keyword-only discount parameter.

```python
def order_summary(customer_name, *item_prices, discount_percent=0):
    if not item_prices:
        raise ValueError("Add at least one item price")
    if any(price < 0 for price in item_prices):
        raise ValueError("Prices cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    subtotal = sum(item_prices)
    discount = subtotal * discount_percent / 100
    final_total = subtotal - discount

    print(f"Customer: {customer_name}")
    print(f"Items: {len(item_prices)}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Final total: ₹{final_total:.2f}")


order_summary("Adil", 120, 80, 50, discount_percent=10)
```

Expected output:
```text
Customer: Adil
Items: 3
Subtotal: ₹250.00
Discount: ₹25.00
Final total: ₹225.00
```

**Real-world use:** A basic order total. A real checkout also needs tax, currency rules, inventory, payment processing, and stronger validation.

## Revision checklist

- [ ] Explain parameter vs argument.
- [ ] Write a function with one argument.
- [ ] Write a function with multiple positional arguments.
- [ ] Call a function with named/keyword arguments.
- [ ] Explain `*args` (tuple) and `**kwargs` (dictionary).
- [ ] Explain a default parameter.
- [ ] Run each example and recreate it from memory.
