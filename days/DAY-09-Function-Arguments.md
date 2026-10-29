# Day 09 — Function Argument Patterns

**Status:** Full study pack published. Complete coding practice, tests and challenge before marking mastery.

## 1. Definition

A **positional argument** is matched to a parameter by its position. A **keyword argument** matches by parameter name. `*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.

## 2. Why, where and when

Use positional arguments for straightforward required inputs and keyword arguments when a call benefits from clarity, especially for optional settings. Use `*args` when a function genuinely accepts a variable number of positional inputs (e.g. summing scores). Use `**kwargs` for extensible named options, wrappers and configuration. Avoid accepting arbitrary arguments when the function has a stable, known contract; explicit parameters improve autocomplete, validation and documentation.

## 3. Syntax and rules

```python
def describe(name, city="Hyderabad"):
    return f"{name} lives in {city}"

def total(*args):
    return sum(args)

def build_profile(**kwargs):
    return kwargs

print(describe("Adil", city="Ongole"))
print(total(1, 2, 3))
print(build_profile(role="developer", active=True))
```

Rules:
- Required parameters normally come before parameters with defaults.
- Positional arguments must be supplied before keyword arguments in a normal call.
- Each parameter may be assigned only once per call.
- `*args` is a tuple; `**kwargs` is a dictionary.
- When forwarding values, `func(*items)` unpacks positional values and `func(**mapping)` unpacks keyword values.

### Dry run

Calling `total(10, 20, 30)` collects the values into `args = (10, 20, 30)`; `sum(args)` returns 60.

## 4. Five worked examples

### Example 1 — Positional arguments

```python
def subtract(a, b):
    return a - b

print(subtract(10, 3))
```
**Output:** `7`  
**Explanation:** The first value binds to `a`, the second to `b`.

### Example 2 — Keyword arguments

```python
def create_user(name, city):
    return f"{name} — {city}"

print(create_user(city="Hyderabad", name="Adil"))
```
**Output:** `Adil — Hyderabad`  
**Explanation:** Keyword arguments bind by name, so call order can differ.

### Example 3 — Default value

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Adil"))
print(greet("Adil", greeting="Welcome"))
```
**Output**
```text
Hello, Adil!
Welcome, Adil!
```
**Explanation:** The default is used only when the argument is omitted.

### Example 4 — Variable positional values with args

```python
def average(*numbers):
    if not numbers:
        raise ValueError("Provide at least one number")
    return sum(numbers) / len(numbers)

print(average(10, 20, 30))
```
**Output:** `20.0`  
**Explanation:** All positional arguments are collected in a tuple.

### Example 5 — Variable keyword values with kwargs

```python
def show_settings(**settings):
    for key, value in sorted(settings.items()):
        print(f"{key}={value}")

show_settings(theme="dark", retries=3)
```
**Output**
```text
retries=3
theme=dark
```
**Explanation:** Keyword arguments form a dictionary; sorting keys gives stable display order.

## 5. Five practice tasks with complete solutions

### Task 1 — Build a full name

```python
def full_name(first, last):
    return f"{first.strip()} {last.strip()}"

print(full_name(" Syed ", "Ali "))
```
**Output:** `Syed Ali`  
**Explanation:** Positional arguments bind to the first and last parameters respectively.

### Task 2 — Calculate an order total

```python
def order_total(price, quantity=1, discount=0):
    if price < 0 or quantity < 1 or not 0 <= discount <= 100:
        raise ValueError("Invalid order")
    return price * quantity * (1 - discount / 100)

print(f"{order_total(100, quantity=3, discount=10):.2f}")
```
**Output:** `270.00`  
**Explanation:** Keyword arguments make optional settings readable.

### Task 3 — Sum any number of values

```python
def sum_values(*values):
    return sum(values)

print(sum_values(2, 4, 6, 8))
```
**Output:** `20`  
**Explanation:** The tuple of arguments is passed to `sum()`.

### Task 4 — Merge configuration options

```python
def configure(default_timeout=10, **options):
    settings = {"timeout": default_timeout, "retries": 2}
    settings.update(options)
    return settings

print(configure(5, retries=4, debug=True))
```
**Output:** `{'timeout': 5, 'retries': 4, 'debug': True}`  
**Explanation:** Explicit default parameters handle common settings; `kwargs` supports additional options.

### Task 5 — Forward a list and a dictionary

```python
def multiply(a, b, scale=1):
    return a * b * scale

numbers = [3, 4]
options = {"scale": 2}
print(multiply(*numbers, **options))
```
**Output:** `24`  
**Explanation:** The asterisk operators unpack a list and a mapping into arguments.

## 6. Common mistakes and edge cases

- Defining a required parameter after a default parameter causes a syntax error.
- Passing a value positionally and by keyword can assign the same parameter twice and raise `TypeError`.
- `args` and `kwargs` are conventional names; the asterisks create their behavior.
- `*args` does not contain a list by default; it is a tuple.
- `**kwargs` keys are strings and should match valid parameter names when unpacked into a function.
- Avoid mutable default values like `items=[]`; use `None` and create a new list inside the function.
- Too much flexibility can hide invalid calls; validate accepted options.

## 7. Interview questions and answers

**Q1. What is the difference between positional and keyword arguments?** Positional arguments bind by order; keyword arguments bind by parameter name.

**Q2. What are `*args`?** A tuple containing extra positional arguments.

**Q3. What are `**kwargs`?** A dictionary containing extra keyword arguments.

**Q4. Can a function use both?** Yes; a common signature is `def f(required, *args, option=True, **kwargs)`.

**Q5. What does argument unpacking do?** It passes items from an iterable as positional arguments or mapping entries as keyword arguments.

**Q6. Why avoid mutable defaults?** A default object is created once when the function is defined and can retain state across calls.

## 8. Real-world mini-project — Email List Collector

This example collects, normalizes and de-duplicates email addresses. It demonstrates flexible arguments while keeping validation intentionally simple; it is not a full RFC email parser or proof that an address exists.

```python
def normalize_email(value):
    if not isinstance(value, str):
        raise TypeError("Email must be text")
    cleaned = value.strip().casefold()
    if not cleaned or cleaned.count("@") != 1:
        raise ValueError(f"Invalid email format: {value!r}")
    local, domain = cleaned.split("@")
    if not local or "." not in domain or domain.startswith(".") or domain.endswith("."):
        raise ValueError(f"Invalid email format: {value!r}")
    if any(char.isspace() for char in cleaned):
        raise ValueError(f"Invalid email format: {value!r}")
    return cleaned


def collect_emails(*addresses, allow_duplicates=False, **metadata):
    normalized = [normalize_email(address) for address in addresses]
    if not allow_duplicates:
        normalized = list(dict.fromkeys(normalized))
    return {"emails": normalized, "metadata": metadata}


def main():
    raw = input("Enter emails separated by commas: ")
    addresses = [part.strip() for part in raw.split(",") if part.strip()]
    try:
        result = collect_emails(*addresses, source="cli")
    except (ValueError, TypeError) as error:
        print(f"Invalid input: {error}")
        return
    print("Emails:", result["emails"])
    print("Metadata:", result["metadata"])


if __name__ == "__main__":
    main()
```

### Sample run

```text
Enter emails separated by commas: ADIL@example.com, test@example.org, adil@example.com
Emails: ['adil@example.com', 'test@example.org']
Metadata: {'source': 'cli'}
```

### Tests

Save as `email_collector.py` and `test_email_collector.py`; run `python -m unittest -v`.

```python
import unittest
from email_collector import collect_emails, normalize_email


class TestEmailCollector(unittest.TestCase):
    def test_normalize_case_and_spaces(self):
        self.assertEqual(normalize_email(" ADIL@Example.com "), "adil@example.com")

    def test_dedupe_preserves_order(self):
        result = collect_emails("a@example.com", "b@example.com", "a@example.com")
        self.assertEqual(result["emails"], ["a@example.com", "b@example.com"])

    def test_duplicates_can_be_allowed(self):
        result = collect_emails("a@example.com", "a@example.com", allow_duplicates=True)
        self.assertEqual(len(result["emails"]), 2)

    def test_invalid_address(self):
        with self.assertRaises(ValueError):
            normalize_email("not-an-email")

    def test_keyword_metadata(self):
        result = collect_emails("a@example.com", source="test")
        self.assertEqual(result["metadata"]["source"], "test")


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. What type is `args`?
2. What type is `kwargs`?
3. What does `f(*[2, 3])` do?
4. What does `f(**{"name": "Adil"})` do?
5. Why should mutable defaults be avoided?

### Answer key
1. Tuple.
2. Dictionary.
3. Passes 2 and 3 as positional arguments.
4. Passes `name="Adil"` as a keyword argument.
5. They are shared across calls and may retain accidental state.

### Independent challenge
Add a required `source` keyword-only argument and optional `max_emails` limit to the collector. Reject excess emails and write tests for omitted source, exact limit and over-limit input.

## 10. Progress checklist

- [ ] I can distinguish positional, keyword, defaults, `*args` and `**kwargs`.
- [ ] I tried all examples and tasks before viewing the solutions.
- [ ] The email collector tests pass.
- [ ] I completed the independent challenge.

## Real-world use cases — where, when and how
1. **Configurable reports:** Where: analytics/reporting tools. When callers choose optional formats. How: keyword arguments make options explicit.
2. **Math utilities:** Where: shared helpers. When a function needs a variable number of values. How: collect positional values with *args and validate the count.
3. **CLI settings:** Where: utilities. When a command has optional named settings. How: keyword-only parameters prevent ambiguous calls.
4. **Decorators/wrappers:** Where: logging and timing. When another function's call must be forwarded. How: accept and forward *args and **kwargs.
5. **Metadata collection:** Where: simple integration layers. When optional labels vary. How: collect named options with **kwargs but reject unknown keys where possible.



## Learner Practice — Order Summary with `**kwargs`

### Code

```python
# Customer details: name, city, product and quantity
def order_summary(**cdetails):
    for key, value in cdetails.items():
        print(f"{key}: {value}")
    return cdetails


print(order_summary(name="syed", product="earphones", quantity="1", city="ongole"))
print("-------------")
print(order_summary(name="adil", product="bike", quantity="1", city="chennai"))
print("-------------")
print(order_summary(name="ali", product="car", quantity="1", city="banglore"))
```

### What it teaches

- `**cdetails` collects any keyword arguments into a dictionary.
- `cdetails.items()` lets the loop access each key and its value.
- The function prints each detail and returns the dictionary.
- `print(order_summary(...))` prints the returned dictionary after the function has printed each field, so the details appear twice in different formats.

### Sample output

```text
name: syed
product: earphones
quantity: 1
city: ongole
{'name': 'syed', 'product': 'earphones', 'quantity': '1', 'city': 'ongole'}
-------------
name: adil
product: bike
quantity: 1
city: chennai
{'name': 'adil', 'product': 'bike', 'quantity': '1', 'city': 'chennai'}
-------------
name: ali
product: car
quantity: 1
city: banglore
{'name': 'ali', 'product': 'car', 'quantity': '1', 'city': 'banglore'}
```

### Recruiter-style review

**Good:** The function correctly uses `**kwargs`, loops through the dictionary, and returns the collected data.

**Improve:**
1. Use consistent capitalization for names and cities (for example, `"Syed"` and `"Ongole"`).
2. Use `quantity=1` as an integer rather than `quantity="1"` as a string if you will calculate totals later.
3. If the goal is only to display the summary, you can omit `return cdetails` and the outer `print()`. If you need the dictionary for later processing, keep the return and assign it to a variable.
4. For a real order system, validate required fields and ensure quantity is a positive integer.

### Cleaner version

```python
def order_summary(**cdetails):
    required = {"name", "city", "product", "quantity"}
    missing = required - cdetails.keys()
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(sorted(missing))}")

    if not isinstance(cdetails["quantity"], int) or cdetails["quantity"] < 1:
        raise ValueError("quantity must be a positive integer")

    for key, value in cdetails.items():
        print(f"{key}: {value}")

    return cdetails


order = order_summary(
    name="Syed",
    city="Ongole",
    product="Earphones",
    quantity=1,
)
print("Returned order:", order)
```

### Practice tasks

1. Add a `price` keyword and pass it as a number.
2. Calculate `total = price * quantity`.
3. Display only `name`, `product`, and `total` in a formatted order receipt.
4. Call the function without `city` and check that validation reports the missing field.
5. Pass quantity as `0` and verify that the function rejects it.
