# Python Core — Topic-by-Topic Code, Explanation and Real-World Use

This companion guide explains code line by line at a beginner-friendly level. Run examples with Python 3. Each section includes what the code does, why it matters, and a practical use.

## 1. Variables, data types and conversion

**Definition:** A variable is a name that refers to a value/object. Python determines the type at runtime.

```python
name = "Adil"       # str: text
age = 23            # int: whole number
height = 1.80       # float: decimal number
is_student = True   # bool: True or False
city = None         # NoneType: no value yet

print(name, age, height, is_student, city)
print(type(age).__name__)  # int
print(int("25") + 5)       # 30
```

**Explanation:** `=` assigns a value. `type()` inspects a value's type. `input()` always returns text, so convert it before numeric calculations. Conversion can raise `ValueError` if input is invalid.

**Real-world use:** Store a customer's name, cart quantity, item price and whether an order is paid.

```python
quantity = int("3")
unit_price = 49.50
print("Order total:", quantity * unit_price)
```

## 2. Operators and conditions

**Definition:** Operators calculate or compare values. Conditions select which code path should run.

```python
price = 1200
discount = 0.10 if price >= 1000 else 0
final_price = price * (1 - discount)

if final_price >= 1000:
    category = "Premium"
else:
    category = "Standard"

print(final_price, category)  # 1080.0 Premium
```

**Explanation:** The conditional expression chooses a discount. The `if/else` statement chooses a category. `>=` compares values; `*` multiplies.

**Real-world use:** E-commerce discounts, eligibility checks, pass/fail rules and fraud-risk thresholds.

## 3. Loops

**Definition:** A loop repeats work. Use `for` to process an iterable and `while` when repetition depends on a condition.

```python
sales = [120, 80, 150]
total = 0
for sale in sales:
    total += sale
print(total)  # 350

attempts = 0
while attempts < 3:
    print("Attempt", attempts + 1)
    attempts += 1
```

**Explanation:** `total += sale` adds each sale to the running total. The while loop increments `attempts`, ensuring it eventually stops.

**Real-world use:** Summing transactions, processing records, retrying a network request a limited number of times.

## 4. Strings

**Definition:** A string is an immutable sequence of characters.

```python
customer = "  ADIL ali  "
cleaned = customer.strip().title()
print(cleaned)                 # Adil Ali
print(cleaned[0])              # A
print(cleaned[::-1])           # ilA lidA
print("2026-10-29".split("-")) # ['2026', '10', '29']
```

**Explanation:** `strip()` removes outer whitespace, `title()` changes letter case, slicing selects a range, and `split()` divides text. Strings are immutable, so these methods return new strings.

**Real-world use:** Normalising form fields, parsing dates, cleaning CSV fields and checking usernames.

## 5. Lists

**Definition:** A list is an ordered, mutable collection.

```python
tasks = ["study", "exercise"]
tasks.append("apply for jobs")
tasks[0] = "study Python"
print(tasks)
print([len(task) for task in tasks])
```

**Explanation:** `append()` adds one item; indexing reads or updates a position; a list comprehension creates a new list from each task.

**Real-world use:** Shopping carts, task lists, records returned by an API.

## 6. Tuples

**Definition:** A tuple is an ordered sequence that cannot be structurally changed after creation.

```python
coordinates = (17.05, 15.50)
latitude, longitude = coordinates
print(latitude, longitude)
```

**Explanation:** Tuple unpacking assigns each item to a variable. Tuples are useful for fixed groups of values; a tuple containing a list is not deeply immutable.

**Real-world use:** Coordinates, fixed RGB values, returning multiple results from a function.

## 7. Sets

**Definition:** A set stores unique hashable values and supports fast average-case membership checks.

```python
registered = {"A12", "B34", "A12"}
attended = {"B34", "C56"}
print(registered)              # duplicate A12 removed
print(registered & attended)   # intersection
print(registered - attended)   # registered but not attended
```

**Explanation:** `&` finds common values; `-` finds values only in the left set. Do not rely on set display order.

**Real-world use:** Deduplicating IDs, comparing attendees with registrations, checking whether a username is already used.

## 8. Dictionaries

**Definition:** A dictionary maps unique hashable keys to values.

```python
product = {"name": "Keyboard", "price": 2000, "stock": 5}
product["stock"] -= 1
print(product.get("brand", "Unknown"))

counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)
```

**Explanation:** Use a key to retrieve or update a value. `get(key, default)` avoids a missing-key error. The frequency loop increments the count for each character.

**Real-world use:** JSON/API responses, inventory records, configuration, counting events in logs.

## 9. Functions

**Definition:** A function packages reusable logic and can return a result.

```python
def calculate_total(price, quantity=1):
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    return price * quantity

print(calculate_total(100, 3))  # 300
print(calculate_total(50))      # 50
```

**Explanation:** Parameters receive input; `quantity=1` is a default; `return` sends a result back to the caller. A function is easier to test than duplicated code.

**Real-world use:** Shipping cost, tax calculation, validation, reusable business rules.

## 10. Comprehensions and modules

**Definition:** A comprehension creates a collection from an iterable. A module is a Python file that can be imported.

```python
prices = [100, 250, 75]
with_tax = [round(price * 1.18, 2) for price in prices]
print(with_tax)
```

**Explanation:** The expression is calculated for each price. Add an `if` clause when you need to filter values. Keep complex logic in a named function for readability.

**Real-world use:** Transforming data before reporting or sending it to another service.

## 11. Files and exceptions

**Definition:** File I/O reads or writes persistent data. Exceptions represent failures that can be handled.

```python
try:
    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("Python practice\n")

    with open("notes.txt", encoding="utf-8") as file:
        print(file.read())
except OSError as error:
    print("Could not access file:", error)
```

**Explanation:** `with` closes the file automatically. Catch a specific exception around the operation that may fail; do not silently hide all errors.

**Real-world use:** Save application settings, read reports, process uploaded files and handle missing files safely.

## 12. Iterators, generators and type hints

**Definition:** An iterator provides values one at a time. A generator is a convenient way to create an iterator using `yield`. Type hints document expected types.

```python
def even_numbers(limit: int):
    for number in range(limit):
        if number % 2 == 0:
            yield number

for number in even_numbers(8):
    print(number)
```

**Explanation:** `yield` returns one value and pauses the generator. It can avoid building a large list in memory. Type hints help readers and tools but are not automatically enforced at runtime.

**Real-world use:** Process large log files or database result streams in manageable chunks.

## Mini-project: order summary

```python
def order_summary(items):
    total = 0
    for item in items:
        if item["quantity"] < 0 or item["price"] < 0:
            raise ValueError("price and quantity must be non-negative")
        total += item["price"] * item["quantity"]
    return {"item_count": len(items), "total": round(total, 2)}

cart = [
    {"name": "Notebook", "price": 60, "quantity": 2},
    {"name": "Pen", "price": 10, "quantity": 3},
]
print(order_summary(cart))
```

**Expected output:** `{'item_count': 2, 'total': 150}`

**What to practise:** Add a discount, reject invalid data, write unit tests, and save the order summary to JSON.
