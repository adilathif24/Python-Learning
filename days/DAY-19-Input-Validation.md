# Day 19 — Input Validation

**Status:** Full study pack published. Complete boundary tests and the challenge before marking mastery.

## 1. Definition
Input validation checks whether data meets expected type, format, range and business rules before the program uses it. Parsing converts raw text to a target type; validation checks whether the parsed value is acceptable.

## 2. Why, where, when
Validate form values, command-line arguments, file data, quantities, prices and API input at the system boundary. Give a clear correction message. Do not assume client-side validation is enough for a server; validate again in trusted code. Avoid catching every exception without distinguishing invalid input from programming bugs.

## 3. Syntax and rules
```python
raw = input("Age: ").strip()
try:
    age = int(raw)
except ValueError:
    print("Enter a whole number")
else:
    if not 0 <= age <= 120:
        print("Age out of range")
    else:
        print("Accepted")
```
Separate conversion errors from business-rule failures. Test below, at and above each boundary. Decide how empty strings, whitespace, negative values and decimals should behave.

## 4. Five worked examples
### Example 1 — Parse an integer safely
```python
raw = "23"
try: age = int(raw)
except ValueError: print("Invalid integer")
else: print(age)
```
Output: `23`. Conversion succeeds.

### Example 2 — Validate range
```python
score = 100
print("valid" if 0 <= score <= 100 else "invalid")
```
Output: `valid`. Both endpoints are allowed.

### Example 3 — Validate a non-empty name
```python
name = "   "
if name.strip(): print("Accepted")
else: print("Name required")
```
Output: `Name required`. Whitespace is not meaningful input.

### Example 4 — Validate quantity
```python
quantity = 3
if isinstance(quantity, int) and not isinstance(quantity, bool) and quantity > 0:
    print("Valid quantity")
else:
    print("Invalid quantity")
```
Output: `Valid quantity`. bool is a subclass of int, so explicitly reject bool when needed.

### Example 5 — Validate email-like input (basic)
```python
def basic_email_check(value):
    value = value.strip()
    return value.count("@") == 1 and "." in value.rsplit("@", 1)[-1] and not any(ch.isspace() for ch in value)
print(basic_email_check("a@example.com"))
```
Output: `True`. This is a basic form check, not full email standard validation.

## 5. Five tasks with solutions
### Task 1 — Parse a price
```python
def parse_price(raw):
    try: price = float(raw)
    except ValueError: raise ValueError("Price must be numeric")
    if price < 0: raise ValueError("Price cannot be negative")
    return price
print(parse_price("12.50"))
```
Output: `12.5`. Parsing and range validation are separate.

### Task 2 — Require a username
```python
def validate_username(value):
    value = value.strip()
    if not 3 <= len(value) <= 16: raise ValueError("Length must be 3–16")
    if not value.isascii() or not value.replace("_","a").isalnum(): raise ValueError("Use letters, digits and underscore")
    return value
print(validate_username("adil_01"))
```
Output: `adil_01`. Constraints are explicit.

### Task 3 — Validate percentage
```python
def validate_percent(number):
    if not 0 <= number <= 100: raise ValueError("Percent must be 0–100")
    return number
print(validate_percent(100))
```
Output: `100`. The boundary is inclusive.

### Task 4 — Limited retries
```python
answers = ["bad", "12", "8"]
valid = None
for answer in answers:
    try:
        value = int(answer)
        if value > 0: valid = value; break
    except ValueError:
        pass
print(valid)
```
Output: `12`. Invalid values are skipped and the first valid positive integer is accepted.

### Task 5 — Validate a date format
```python
from datetime import datetime
def parse_date(raw):
    try: return datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError as error: raise ValueError("Date must be valid YYYY-MM-DD") from error
print(parse_date("2026-01-05"))
```
Output: `2026-01-05`. strptime checks format and calendar validity.

## 6. Common mistakes
- Calling int/float on untrusted input without handling ValueError.
- Accepting negative values when the domain forbids them.
- Forgetting boundary values.
- Using a regex/string check as a complete security control.
- Returning unclear errors that do not tell the user how to fix input.
- Over-catching exceptions can hide programming defects.

## 7. Interview Q&A
1. Parsing vs validation? **Parsing converts; validation checks rules.**
2. Why validate server-side? **Client checks can be bypassed.**
3. What is a boundary test? **Test immediately below, at, and above a limit.**
4. Why not catch Exception everywhere? **It may hide unexpected bugs.**
5. What does fail-fast mean? **Reject invalid values early, near the boundary.**

## 8. Project — Bill and Discount Calculator
Save as `validated_bill.py`.
```python
def calculate_bill(price, quantity, discount_percent):
    if price < 0: raise ValueError("Price cannot be negative")
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    if not 0 <= discount_percent <= 100: raise ValueError("Discount must be 0–100")
    subtotal = price * quantity
    discount = subtotal * discount_percent / 100
    return {"subtotal":subtotal, "discount":discount, "total":subtotal-discount}

def main():
    try:
        price = float(input("Unit price: "))
        quantity = int(input("Quantity: "))
        discount = float(input("Discount %: "))
        bill = calculate_bill(price, quantity, discount)
    except ValueError as error:
        print(f"Invalid input: {error}"); return
    for key, value in bill.items(): print(f"{key}: ₹{value:.2f}")

if __name__ == "__main__": main()
```
Sample: price 100, quantity 2, discount 10 gives total ₹180.00.

### Tests — `test_validated_bill.py`
```python
import unittest
from validated_bill import calculate_bill

class BillTests(unittest.TestCase):
    def test_normal(self): self.assertEqual(calculate_bill(100,2,10)["total"],180)
    def test_zero_discount(self): self.assertEqual(calculate_bill(20,1,0)["total"],20)
    def test_full_discount(self): self.assertEqual(calculate_bill(20,1,100)["total"],0)
    def test_negative_price(self):
        with self.assertRaises(ValueError): calculate_bill(-1,1,0)
    def test_invalid_discount(self):
        with self.assertRaises(ValueError): calculate_bill(10,1,101)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What does input return? **str.**
2. Which error often signals failed int conversion? **ValueError.**
3. What does fail-fast validation do? **Rejects bad values immediately.**
4. Should 100 be valid for a 0–100 percentage? **Yes, if inclusive.**
5. Why separate parsing from range checks? **They are different failure conditions.**
**Challenge:** Add a maximum order total and test just below, exactly at, and above the limit.

## Real-world use cases — where, when and how
1. **Registration form:** Where: web or CLI signup. When a required name or age is collected. How: strip text, parse integer and validate allowed range.
2. **Checkout:** Where: shopping software. When price, quantity and discount are entered. How: reject negatives and out-of-range percentages before calculation.
3. **CSV imports:** Where: bulk data processing. When cells may be blank or malformed. How: validate field presence/type and report the row that failed.
4. **API boundary:** Where: backend endpoints. When client payloads are untrusted. How: validate fields on the server even if UI validation exists.
5. **Retry prompt:** Where: command-line utilities. When the user can correct a mistake. How: retry a bounded number of times and give a precise correction message.


## 10. Completion
- [ ] I can explain parsing, type checks, boundaries and retries.
- [ ] All project tests pass.
- [ ] I solved the independent challenge.
