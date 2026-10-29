# Day 21 — Exceptions in Python

**Status:** Full study pack. Complete code practice and tests before marking mastery.

## 1. Definition
An **exception** is an event raised while a program runs that interrupts normal control flow. `try/except` handles expected failures. `else` runs when the try body succeeds. `finally` runs whether an exception occurs or not. `raise` deliberately raises an exception.

## 2. Why, where, when
Handle expected failures at boundaries: parsing input, reading files, accessing dictionary keys, or calling external services. Catch specific exceptions and show useful messages. Do not use exceptions for every normal branch, and do not catch `Exception` broadly unless a boundary genuinely needs to log/recover from unexpected errors.

## 3. Syntax and rules
```python
try:
    value = int("abc")
except ValueError:
    print("Enter digits")
else:
    print(value)
finally:
    print("Finished")
```
The except matches the exception type. Else runs only if no exception was raised in try. Finally runs during normal completion and exception propagation. Never leave a `try` block so broad that it hides unrelated bugs.

## 4. Five worked examples
### Example 1 — Handle conversion failure
```python
try:
    age = int("twenty")
except ValueError:
    print("Age must be a whole number")
```
Output: `Age must be a whole number`. int cannot parse this text.

### Example 2 — Try/except/else
```python
try: result = int("42")
except ValueError: print("Invalid")
else: print(result)
```
Output: `42`. The else block runs only if conversion succeeded.

### Example 3 — Finally cleanup marker
```python
try: print("Working")
finally: print("Cleanup step")
```
Output: Working, then Cleanup step. Finally runs even if an exception propagates.

### Example 4 — Raise domain error
```python
def withdraw(balance, amount):
    if amount <= 0: raise ValueError("Amount must be positive")
    if amount > balance: raise ValueError("Insufficient balance")
    return balance - amount
print(withdraw(100, 30))
```
Output: `70`. The function enforces business rules.

### Example 5 — Preserve exception cause
```python
def parse_quantity(raw):
    try: quantity = int(raw)
    except ValueError as error:
        raise ValueError("Quantity must be an integer") from error
    return quantity
print(parse_quantity("3"))
```
Output: `3`. Exception chaining retains the underlying reason on failure.

## 5. Five tasks with solutions
### Task 1 — Dictionary-safe lookup
```python
data = {"name": "Adil"}
try: print(data["email"])
except KeyError: print("Email not available")
```
Output: `Email not available`. Missing keys raise KeyError.

### Task 2 — List-safe index
```python
items = ["a", "b"]
index = 8
try: print(items[index])
except IndexError: print("Index out of range")
```
Output: `Index out of range`.

### Task 3 — Safe division
```python
def divide(a,b):
    if b == 0: raise ZeroDivisionError("Cannot divide by zero")
    return a/b
print(divide(8,2))
```
Output: `4.0`. Reject zero explicitly.

### Task 4 — Handle two expected input errors
```python
raw = "2.5"
try: value = int(raw)
except (ValueError, TypeError): print("Enter an integer")
else: print(value)
```
Output: `Enter an integer`.

### Task 5 — Custom exception
```python
class InsufficientFundsError(Exception):
    pass

def spend(balance, amount):
    if amount > balance: raise InsufficientFundsError("Not enough funds")
    return balance - amount

try: print(spend(20, 50))
except InsufficientFundsError as error: print(error)
```
Output: `Not enough funds`. Custom exceptions model domain-specific failures.

## 6. Common mistakes
- Catching Exception hides mistakes.
- Empty except blocks silently discard failures.
- Finally should not return a value that suppresses exceptions.
- Use with for resource cleanup when working with files.
- Raise ValueError for invalid values; TypeError for wrong types, when appropriate.

## 7. Interview Q&A
1. What is an exception? **A runtime event that interrupts normal execution.**
2. What does finally do? **Runs whether an exception occurs or not.**
3. When does else execute? **When the try block completes without raising.**
4. Why catch specific errors? **So expected failures are handled without hiding unrelated bugs.**
5. Why create a custom exception? **To give a domain failure a clear, catchable type.**

## 8. Project — Safe Calculator
Save as `safe_calculator.py`.
```python
def calculate(a, operator, b):
    if operator not in {"+", "-", "*", "/"}:
        raise ValueError("Unsupported operator")
    if operator == "+": return a+b
    if operator == "-": return a-b
    if operator == "*": return a*b
    if b == 0: raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def main():
    try:
        a = float(input("First number: "))
        op = input("Operator (+ - * /): ").strip()
        b = float(input("Second number: "))
        print("Result:", calculate(a, op, b))
    except (ValueError, ZeroDivisionError) as error:
        print(f"Invalid calculation: {error}")

if __name__ == "__main__": main()
```
Example: 8, /, 2 → Result: 4.0.

### Tests — `test_safe_calculator.py`
```python
import unittest
from safe_calculator import calculate

class CalculatorTests(unittest.TestCase):
    def test_add(self): self.assertEqual(calculate(2,"+",3),5)
    def test_subtract(self): self.assertEqual(calculate(8,"-",2),6)
    def test_multiply(self): self.assertEqual(calculate(3,"*",4),12)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError): calculate(3,"/",0)
    def test_unknown_operator(self):
        with self.assertRaises(ValueError): calculate(2,"%",2)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Conversion failure type? **ValueError.**
2. Missing dictionary key? **KeyError.**
3. What runs after try even during propagation? **finally.**
4. Why not catch all exceptions? **It may hide defects.**
5. What does raise do? **Raises an exception.**
**Challenge:** Add exponentiation, reject unreasonable exponent inputs, and add tests for invalid operands/operators.

## Real-world use cases — where, when and how
1. **Input parsing:** Where: CLI programs. When text should become an integer. How: catch ValueError and show how to correct it.
2. **File access:** Where: report exports. When a file may be missing or locked. How: catch the specific OSError subtype the program can reasonably recover from.
3. **Missing records:** Where: dictionaries/database lookups. When a requested key or ID may not exist. How: use a documented fallback or raise a domain-specific error.
4. **Transaction protection:** Where: data updates. When a failed operation must not leave partial changes. How: use a transaction/context manager with rollback behavior.
5. **Domain rules:** Where: checkout or banking logic. When a value breaks a business rule. How: raise a clear ValueError or custom exception and test it.


## 10. Completion
- [ ] I can explain try/except/else/finally and raise.
- [ ] I completed all practice tasks.
- [ ] Tests pass and challenge is solved.
