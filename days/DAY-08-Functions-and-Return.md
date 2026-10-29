# Day 08 — Functions and Return Values

**Status:** Full study pack published. Confirm mastery only after coding independently and completing the project tests.

## 1. Definition

A **function** is a named, reusable block of code designed to perform a task. Define it with `def`; execute it by calling its name with parentheses. **Parameters** are names in the function definition; **arguments** are the actual values passed in a call. `return` sends a result back to the caller; `print()` displays a value to the user.

## 2. Why, where and when

Functions avoid repeated code, divide a large problem into smaller parts, make testing easier, and give behavior a clear name. Use a function when a task has a meaningful input/output or should be reused. Avoid creating a function for every trivial line when it hides the actual logic. Prefer returning values from business logic and printing only at the user-interface boundary.

## 3. Syntax and rules

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

- The function body is indented.
- A function returns `None` if it reaches the end without a `return`.
- `return` exits the current function immediately.
- A function can return any object, including a tuple or dictionary.
- Variables created inside a function are local unless scope rules say otherwise.

### Dry run

Calling `add(2, 3)` binds `a=2`, `b=3`; evaluates `a+b` to 5; returns 5 to the caller; then `print(result)` displays 5.

## 4. Five worked examples

### Example 1 — A greeting function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Adil"))
```
**Output:** `Hello, Adil!`  
**Explanation:** The argument "Adil" is assigned to parameter `name`.

### Example 2 — Return versus print

```python
def square(number):
    return number * number

answer = square(4)
print(answer)
```
**Output:** `16`  
**Explanation:** Returning makes the result available for further calculation and testing.

### Example 3 — Validate a positive value

```python
def is_positive(number):
    return number > 0

print(is_positive(5))
print(is_positive(-2))
```
**Output**
```text
True
False
```
**Explanation:** The comparison evaluates to a Boolean which the function returns.

### Example 4 — Return multiple results

```python
def divide_and_remainder(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a // b, a % b

quotient, remainder = divide_and_remainder(17, 5)
print(quotient, remainder)
```
**Output:** `3 2`  
**Explanation:** Multiple comma-separated return values are packed into a tuple and can be unpacked.

### Example 5 — Reuse a function in a loop

```python
def is_even(number):
    return number % 2 == 0

values = [1, 2, 3, 4, 5, 6]
evens = [value for value in values if is_even(value)]
print(evens)
```
**Output:** `[2, 4, 6]`  
**Explanation:** A reusable predicate keeps the filtering rule clear.

## 5. Five practice tasks with complete solutions

### Task 1 — Convert Celsius to Fahrenheit

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))
```
**Output**
```text
32.0
77.0
```
**Explanation:** The formula is encapsulated in one reusable function.

### Task 2 — Return the larger value

```python
def larger(a, b):
    return a if a >= b else b

print(larger(8, 12))
```
**Output:** `12`  
**Explanation:** The conditional expression returns whichever value is larger.

### Task 3 — Count vowels

```python
def count_vowels(text):
    return sum(char.casefold() in "aeiou" for char in text)

print(count_vowels("Python Programming"))
```
**Output:** `4`  
**Explanation:** Each membership expression contributes True (1) or False (0) to the sum.

### Task 4 — Calculate average safely

```python
def average(values):
    if not values:
        raise ValueError("At least one value is required")
    return sum(values) / len(values)

print(average([10, 20, 30]))
```
**Output:** `20.0`  
**Explanation:** Empty input is rejected to avoid division by zero.

### Task 5 — Build a display name

```python
def display_name(first, last):
    first = first.strip()
    last = last.strip()
    if not first or not last:
        raise ValueError("First and last names are required")
    return f"{first} {last}"

print(display_name("  Syed ", "Ali  "))
```
**Output:** `Syed Ali`  
**Explanation:** The function normalises whitespace and validates both required fields.

## 6. Common mistakes and edge cases

- Expecting `print()` to return the displayed text; `print()` returns `None`.
- Forgetting to return a computed value.
- Writing code in a function but never calling it.
- Returning before later statements makes those statements unreachable.
- Passing the wrong number of required arguments raises `TypeError`.
- Dividing by zero or averaging an empty list needs explicit handling.
- Prefer descriptive function and parameter names.
- Avoid changing global variables as a substitute for returning a value.

## 7. Interview questions and answers

**Q1. What is a function?** A reusable named block of code that can accept inputs and optionally return a result.

**Q2. Parameters versus arguments?** Parameters appear in a definition; arguments are values supplied when calling it.

**Q3. Difference between `return` and `print`?** Return passes a value to the caller and ends the function; print displays content but does not return it as the function result.

**Q4. What does a function return without an explicit return?** `None`.

**Q5. Why write small functions?** They isolate responsibilities, support reuse, and are easier to test and debug.

**Q6. Can a function return multiple values?** Yes; comma-separated values are returned as a tuple.

## 8. Real-world mini-project — Contact Name Manager

Save as `name_manager.py`. It validates and stores names using testable functions.

```python
def normalize_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be text.")
    cleaned = " ".join(name.split())
    if not cleaned:
        raise ValueError("Name cannot be empty.")
    return cleaned


def add_contact(contacts, name):
    cleaned = normalize_name(name)
    contacts.append(cleaned)
    return len(contacts)


def find_contacts(contacts, query):
    query = normalize_name(query).casefold()
    return [name for name in contacts if query in name.casefold()]


def main():
    contacts = []
    while True:
        print("\n1 Add  2 Search  3 List  4 Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                name = input("Full name: ")
                add_contact(contacts, name)
                print("Contact added")
            except (ValueError, TypeError) as error:
                print(f"Invalid name: {error}")
        elif choice == "2":
            try:
                query = input("Search text: ")
                matches = find_contacts(contacts, query)
                print(matches if matches else "No match")
            except ValueError as error:
                print(error)
        elif choice == "3":
            print(contacts if contacts else "No contacts")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Choose 1–4")


if __name__ == "__main__":
    main()
```

### Sample run
```text
1 Add  2 Search  3 List  4 Quit
Choose: 1
Full name: Syed Adil Ali
Contact added
Choose: 3
['Syed Adil Ali']
```

### Tests

Save as `test_name_manager.py`; run `python -m unittest -v`.

```python
import unittest
from name_manager import normalize_name, add_contact, find_contacts


class TestNameManager(unittest.TestCase):
    def test_normalize_whitespace(self):
        self.assertEqual(normalize_name("  Syed   Adil "), "Syed Adil")

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            normalize_name("  ")

    def test_add_contact_returns_count(self):
        contacts = []
        self.assertEqual(add_contact(contacts, "Adil"), 1)

    def test_case_insensitive_search(self):
        self.assertEqual(find_contacts(["Syed Adil"], "ADIL"), ["Syed Adil"])

    def test_non_string_rejected(self):
        with self.assertRaises(TypeError):
            normalize_name(123)


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. What is the difference between a parameter and an argument?
2. What does a function return if no return statement is reached?
3. Does `print(value)` return `value`?
4. Why handle an empty list in an average function?
5. What does `return a, b` produce?

### Answer key
1. Parameter is a definition name; argument is the passed value.
2. `None`.
3. No, print returns `None`.
4. Otherwise average would divide by zero.
5. A tuple containing a and b.

### Independent challenge
Add an `update_contact(old_name, new_name)` function that updates a contact safely. Define what happens for missing names and duplicate names, then write tests for both.

## 10. Progress checklist

- [ ] I can distinguish parameters, arguments, print and return.
- [ ] I completed the worked examples and tasks independently.
- [ ] The name-manager tests pass.
- [ ] I completed the independent challenge.
