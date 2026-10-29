# Python Core — Professional Interview Workbook

Use this answer structure in interviews: **definition → mechanism → complete example → output → real-world use → trade-off/edge case**. Type every example, run it, and explain it without reading.

## 1. Variables, types, conversion and mutability
**Definition:** A variable is a name bound to an object. Python is dynamically typed; objects have runtime types. Assignment binds names and does not necessarily copy objects.
**Syntax:** `name = value`; conversion: `int("42")`; type hint: `def total(qty: int) -> int:`.
### Seven complete examples
```python
# 1. Values and runtime types
name, age, active = "Adil", 23, True
print(type(name).__name__, type(age).__name__, type(active).__name__)
# str int bool

# 2. Conversion
quantity = int("4")
print(quantity * 25)  # 100

# 3. Assignment versus equality
status = "paid"
print(status == "paid")  # True

# 4. None identity
result = None
print(result is None)  # True

# 5. Aliasing a mutable object
first = [10, 20]
second = first
second.append(30)
print(first)  # [10, 20, 30]

# 6. Shallow copy
first = [10, 20]
second = first.copy()
second.append(30)
print(first, second)  # [10, 20] [10, 20, 30]

# 7. Type-annotated reusable function
def calculate_total(quantity: int, unit_price: float) -> float:
    return quantity * unit_price
print(calculate_total(3, 12.5))  # 37.5
```
**Explanation:** `=` binds a name, `==` compares values, and `is` checks identity. Type hints document intended types but do not automatically validate input at runtime. A shallow copy duplicates the outer collection but retains references to nested objects.
**Real-world use:** Validate quantities, prices, IDs and user input before calculations or database operations.
### Seven interview questions and professional answers
1. **Is Python statically or dynamically typed?** Python is dynamically typed: names may be rebound to objects of different types, and type checking occurs at runtime.
2. **Is Python strongly typed?** Generally yes; unrelated types are not silently interchangeable, so `"2" + 2` raises `TypeError`.
3. **Assignment vs equality?** `=` binds a name; `==` compares values.
4. **What is mutability?** Mutable objects can change after creation; lists/dictionaries are mutable, while strings/tuples are immutable.
5. **`is` vs `==`?** Equality versus identity; use `is None` for a None check.
6. **Why use type hints?** Better documentation, editor support and static analysis; they do not replace runtime validation.
7. **Why can aliasing cause bugs?** Multiple names can refer to the same mutable object, so mutation through one name affects the others.
### Five practice questions with answers and code
1. Convert text and add 5: `print(int("45") + 5)  # 50`
2. Safely parse an integer:
```python
def parse_int(text):
    try: return int(text)
    except ValueError: return None
print(parse_int("abc"))  # None
```
3. Show aliasing: `a=[1]; b=a; b.append(2); print(a)  # [1, 2]`
4. Make an independent shallow copy: `a=[1]; b=a.copy(); b.append(2); print(a,b)  # [1] [1, 2]`
5. Validate a discount:
```python
def discounted_price(price: float, rate: float) -> float:
    if price < 0 or not 0 <= rate <= 1:
        raise ValueError("Invalid price or rate")
    return price * (1 - rate)
print(discounted_price(1000, .1))  # 900.0
```

## 2. Operators and conditional logic
**Definition:** Operators calculate or compare values; conditionals select execution paths from Boolean expressions. **Syntax:** `if condition: ... elif other: ... else: ...`.
### Seven examples
```python
# 1. Eligibility
age = 22
print("Eligible" if age >= 18 else "Not eligible")
# 2. Branch order
score = 82
if score >= 90: grade = "A"
elif score >= 75: grade = "B"
else: grade = "C"
print(grade)  # B
# 3. Boolean combination
print(True and False)  # False
# 4. Short circuit prevents unsafe access
user = None
if user is not None and user["active"]: print("Active")
else: print("No active user")
# 5. Membership
print("admin" in {"admin", "editor"})  # True
# 6. Conditional expression
price = 1200
print(price * .9 if price >= 1000 else price)  # 1080.0
# 7. Guard clauses
def withdraw(balance, amount):
    if amount <= 0: raise ValueError("Amount must be positive")
    if amount > balance: raise ValueError("Insufficient funds")
    return balance - amount
print(withdraw(500, 125))  # 375
```
**Explanation/use:** Guard clauses reject invalid states early. Short-circuiting can avoid evaluating a later expression. Real systems use these patterns for permissions, eligibility, discounts and transaction rules.
### Seven interview Q&A
1. **How do `and` and `or` work?** They short-circuit and return an operand, not necessarily a Boolean.
2. **What is truthiness?** Empty collections, zero, empty strings and `None` are falsy.
3. **Why order branches carefully?** The first matching branch executes.
4. **Why use guard clauses?** They make preconditions explicit and reduce nesting.
5. **What does `in` test?** Membership in a collection or sequence.
6. **Can comparisons be chained?** Yes: `0 <= score <= 100`.
7. **When avoid a conditional expression?** When nested logic harms readability.
### Five solved practice tasks
1. Range check: `n=12; print(1 <= n <= 20)  # True`
2. Pass/fail: `score=76; print("Pass" if score >= 40 else "Fail")`
3. Safe division:
```python
def divide(a, b):
    if b == 0: raise ZeroDivisionError("Denominator cannot be zero")
    return a / b
print(divide(10, 2))  # 5.0
```
4. Validate username: `name="adil_24"; print(bool(name) and len(name)>=5)  # True`
5. Member pricing:
```python
def final_price(price, member):
    return price * (0.9 if member else 1)
print(final_price(200, True))  # 180.0
```

## 3. Loops and iteration
**Definition:** A loop repeats work over an iterable (`for`) or while a condition remains true (`while`). Use `break` to exit and `continue` to skip to the next iteration.
### Seven examples
```python
# 1. range stop is exclusive
for n in range(1, 4): print(n)  # 1, 2, 3
# 2. Accumulator
total = 0
for n in range(1, 6): total += n
print(total)  # 15
# 3. while loop with progress
count = 3
while count > 0:
    print(count)
    count -= 1
# 4. enumerate provides index and value
for index, name in enumerate(["Maya", "Ravi"], start=1):
    print(index, name)
# 5. break and continue
for n in range(1, 6):
    if n == 2: continue
    if n == 5: break
    print(n)  # 1, 3, 4
# 6. Nested loop
for row in range(2):
    for col in range(2): print(row, col)
# 7. Process records
orders = [{"total": 80}, {"total": 120}, {"total": 40}]
print(sum(order["total"] for order in orders))  # 240
```
**Real-world use:** Iterate over logs, orders, API pages and records; use limits/timeouts for retry loops.
### Seven interview Q&A
1. **For vs while?** Iterable-driven versus condition-driven repetition.
2. **What is `range(1,5)`?** 1 through 4.
3. **Break vs continue?** Exit loop versus skip current iteration.
4. **Infinite loop?** Termination condition never becomes false or cannot be reached.
5. **Why enumerate?** Avoid maintaining an index manually.
6. **Generator expression?** Produces values lazily without an intermediate list.
7. **Nested-loop complexity?** Often O(n²) when both loops range over n items.
### Five solved practice tasks
1. Sum 1–10: `print(sum(range(1, 11)))  # 55`
2. Count evens: `values=[2,5,8,11,14]; print(sum(x%2==0 for x in values))  # 3`
3. Countdown: `for n in range(5,0,-1): print(n)`
4. Maximum:
```python
values = [7, 2, 19, 4]
largest = values[0]
for value in values[1:]:
    if value > largest: largest = value
print(largest)  # 19
```
5. Multiplication table: `n=4; [print(f"{n} x {i} = {n*i}") for i in range(1,6)]`

## 4. Strings and collections
**Definition:** Strings are immutable Unicode sequences; lists are ordered/mutable; tuples ordered/immutable; sets hold unique hashable values; dictionaries map hashable keys to values.
### Seven examples
```python
# 1. Normalize input
print("  Adil@Example.com ".strip().lower())  # adil@example.com
# 2. Filter list
print([p for p in [100,250,75,400] if p >= 200])  # [250, 400]
# 3. Tuple unpacking
x, y = (12, 30)
print(x, y)  # 12 30
# 4. Deduplicate
print(sorted(set([1,2,2,3,1])))  # [1, 2, 3]
# 5. Safe dictionary lookup
employee = {"id": 101, "name": "Maya"}
print(employee.get("department", "Not assigned"))
# 6. Count frequencies
from collections import Counter
print(Counter("banana"))
# 7. Sort by key
products = [{"name":"Pen","price":10},{"name":"Book","price":50}]
print([p["name"] for p in sorted(products, key=lambda p:p["price"])])
```
**Real-world use:** Normalize form input, deduplicate imports, index records by ID and summarize event counts.
### Seven interview Q&A
1. **Why are strings immutable?** Operations create new strings, supporting predictable value semantics.
2. **List vs tuple?** Mutable changing collection versus fixed sequence.
3. **Set vs list?** Uniqueness and efficient average membership versus order/duplicates.
4. **How do dictionaries work?** Hash-table mapping with average-case O(1) access under typical conditions.
5. **What is hashable?** An object with a stable hash and consistent equality behaviour.
6. **Why use `dict.get`?** Missing keys return a default rather than raising `KeyError`.
7. **What is a shallow copy?** Copies the outer container, not nested objects.
### Five solved practice tasks
1. Normalize: `print("  PYTHON ".strip().lower())  # python`
2. Sorted unique: `print(sorted(set([4,2,4,1])))  # [1,2,4]`
3. Word frequency: `print(Counter("python sql python".split()))`
4. Default lookup: `print({}.get("theme","light"))  # light`
5. Sort products: `print(sorted(products,key=lambda p:p["price"]))`

## 5. Functions, scope and reusable design
**Definition:** Functions package reusable behaviour. Parameters define inputs; return values communicate results. Small, single-purpose functions are easier to test.
### Seven examples
```python
# 1. Return a result
def square(n: int) -> int: return n*n
print(square(5))  # 25
# 2. Default argument
def greet(name, greeting="Hello"): return f"{greeting}, {name}"
print(greet("Adil"))
# 3. Keyword arguments
def create_user(name, active=True): return {"name":name,"active":active}
print(create_user(name="Maya",active=False))
# 4. Avoid mutable defaults
def add_item(item, items=None):
    if items is None: items=[]
    items.append(item)
    return items
print(add_item("pen"))  # ['pen']
# 5. *args
def total(*numbers): return sum(numbers)
print(total(2,3,5))  # 10
# 6. **kwargs
def profile(**fields): return fields
print(profile(name="Maya",role="Developer"))
# 7. Separate logic from printing
def calculate_total(prices): return sum(prices)
print(calculate_total([10,20,30]))  # 60
```
**Real-world use:** Reusable validation, pricing, transformations and service logic.
### Seven interview Q&A
1. **Parameter vs argument?** Definition name versus passed value.
2. **Return vs print?** Return sends data to caller; print writes output.
3. **Default argument?** Used when caller omits a parameter; avoid mutable defaults.
4. **`*args`/`**kwargs`?** Collect extra positional arguments into tuple and keyword arguments into dictionary.
5. **Scope?** Name visibility; Python uses LEGB lookup.
6. **Pure function?** Output depends only on inputs and has no observable side effects.
7. **Why decompose into functions?** Testability, reuse, readability and fault isolation.
### Five solved practice tasks
1. Even check: `def is_even(n): return n%2==0; print(is_even(8))`
2. Largest of three: `def largest(a,b,c): return max(a,b,c)`
3. Simple interest:
```python
def simple_interest(p, rate, years):
    return p * rate * years / 100
print(simple_interest(10000,5,2))  # 1000.0
```
4. Email plausibility:
```python
def looks_like_email(value):
    return "@" in value and "." in value.rsplit("@",1)[-1]
print(looks_like_email("a@example.com"))  # True; not full email validation
```
5. Order summary:
```python
def order_summary(items):
    return {"quantity":sum(x["quantity"] for x in items),
            "subtotal":sum(x["price"]*x["quantity"] for x in items)}
print(order_summary([{"price":10,"quantity":2}]))
```

## 6. Files, exceptions, modules and maintainability
**Definition:** Files persist data; exceptions represent abnormal conditions; modules organise reusable code. Context managers release resources reliably.
### Seven examples
```python
from pathlib import Path
# 1. Write file
Path("notes.txt").write_text("Interview prep\n", encoding="utf-8")
# 2. Read file
print(Path("notes.txt").read_text(encoding="utf-8").strip())
# 3. Handle expected conversion error
def parse_int(value):
    try: return int(value)
    except ValueError: return None
print(parse_int("x"))  # None
# 4. Raise a meaningful error
def validate_price(price):
    if price < 0: raise ValueError("Price cannot be negative")
    return price
# 5. Context manager
with open("notes.txt", encoding="utf-8") as file:
    first_line = file.readline()
print(first_line.strip())
# 6. Import module
from math import ceil
print(ceil(4.2))  # 5
# 7. Application entry point
def main(): print("Application started")
if __name__ == "__main__": main()
```
**Real-world use:** Read configuration, process exports, recover from malformed input and organise code by responsibility.
### Seven interview Q&A
1. **Why `with open`?** It closes the file even if an exception occurs.
2. **What is an exception?** An object representing an error or exceptional condition.
3. **Why catch specific exceptions?** To avoid hiding unrelated defects.
4. **What is a module?** A Python file that can define reusable functions/classes/values.
5. **Entry-point guard?** Distinguishes direct execution from import.
6. **Why pathlib?** Cross-platform object-oriented path operations.
7. **Should every exception be caught?** No; catch where meaningful recovery is possible.
### Five solved practice tasks
1. Write/read file with `Path("practice.txt").write_text("Done", encoding="utf-8"); print(Path("practice.txt").read_text(encoding="utf-8"))`
2. Safe integer parser: use `parse_int` above.
3. Reject negative price: use `validate_price` above.
4. Check existence: `print(Path("practice.txt").exists())`
5. Entry point: use the `main` example above.

## Project question: validated order summary
**Question:** How would you calculate order totals and reject invalid inputs?
**Professional answer:** Validate at the boundary, isolate calculation logic, return structured results, use `Decimal` for currency, and test normal/invalid cases. Production payment and inventory changes require persistence and transactional safeguards.
```python
from decimal import Decimal
def calculate_order_total(items):
    if not items:
        raise ValueError("An order must contain items")
    total = Decimal("0")
    for item in items:
        quantity = item.get("quantity")
        price = Decimal(str(item.get("unit_price", "0")))
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if price < 0:
            raise ValueError("Price cannot be negative")
        total += price * quantity
    return total
order = [{"quantity":2,"unit_price":"45.50"},{"quantity":3,"unit_price":"10.00"}]
print(calculate_order_total(order))  # 121.00
```
**Project follow-ups:** Why Decimal? To avoid common binary floating-point representation issues in money. What tests? Empty order, zero/negative quantity, negative price, decimal prices and valid multiple items. Complexity? O(n) time and O(1) additional working space excluding input.
