# Python Functions: `*args` (Arbitrary Positional Arguments)

> **Status:** Learning guide. Run the examples and project locally before treating the topic as mastered.

## 1. Definition

In Python, `*args` lets a function accept any number of positional arguments. Python collects those extra positional arguments into a **tuple** inside the function.

“args” is a conventional name, not a keyword. The asterisk (`*`) is what enables this behavior, so `*values` or `*emails` works too.

### Professional interview definition

“`*args` is Python’s variable-length positional-argument mechanism. It allows a function to accept zero or more positional arguments, which Python packs into a tuple. It is useful when the number of inputs is not known in advance, such as aggregating values, processing a variable number of records, or writing flexible helper functions.”

## 2. Syntax

```python
def function_name(*args):
    for value in args:
        print(value)

function_name("Python", "Java", "SQL")
```

Output:
```text
Python
Java
SQL
```

### How it works

1. The caller supplies positional values.
2. Python gathers those values into a tuple named `args`.
3. The function can loop through, count, validate, or process the tuple.
4. If no values are supplied, `args` is an empty tuple: `()`.

## 3. Why and where to use it

Use `*args` when a function genuinely needs to accept a variable number of positional inputs. Examples include:
- adding any number of values;
- collecting several email addresses for validation;
- formatting messages with a variable number of values;
- passing variable arguments to another function;
- building small utilities where callers may provide zero, one, or many items.

Do not use it automatically. If a function always needs exactly two inputs, explicit parameters such as `def add(a, b):` are clearer.

## 4. Seven worked examples

### Example 1 — Accept any number of values

```python
def show_values(*args):
    print(args)
    print(type(args))

show_values("Python", "Java", "SQL")
```

Output:
```text
('Python', 'Java', 'SQL')
<class 'tuple'>
```

**Explanation:** All three positional values are stored in a tuple. The tuple is created by Python; you do not need to build it manually.

### Example 2 — No arguments, one argument, or many

```python
def show_items(*items):
    print(f"Count: {len(items)}")
    for item in items:
        print(item)

show_items()
show_items("Notebook")
show_items("Notebook", "Pen", "Bottle")
```

Output:
```text
Count: 0
Count: 1
Notebook
Count: 3
Notebook
Pen
Bottle
```

**Explanation:** The same function supports all three cases. With no arguments, `items` is an empty tuple.

### Example 3 — Calculate a total

```python
def calculate_total(*numbers):
    return sum(numbers)

print(calculate_total(10, 20))
print(calculate_total(10, 20, 30, 40))
print(calculate_total())
```

Output:
```text
30
100
0
```

**Explanation:** `sum()` accepts the tuple of numbers. An empty tuple sums to zero. This example expects numeric inputs; strings or other incompatible types can raise `TypeError`.

### Example 4 — Find the average safely

```python
def calculate_average(*numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print(calculate_average(10, 20, 30))
print(calculate_average())
```

Output:
```text
20.0
None
```

**Explanation:** The empty-input check prevents division by zero. Returning `None` clearly signals that an average was not available; another design could raise `ValueError`, depending on the API contract.

### Example 5 — Your email collection example, improved

```python
def collect_emails(*emails):
    accepted = []

    for email in emails:
        email = email.strip()

        # A deliberately simple check for this learning example.
        if email.count("@") == 1 and " " not in email:
            accepted.append(email)
            print("Accepted:", email)
        else:
            print("Rejected:", email)

    return accepted


result = collect_emails(
    "syedadil24@gmail.com",
    "  adil@example.com  ",
    "not-an-email",
    "two@@signs.com",
)

print("Final list:", result)
```

Output:
```text
Accepted: syedadil24@gmail.com
Accepted: adil@example.com
Rejected: not-an-email
Rejected: two@@signs.com
Final list: ['syedadil24@gmail.com', 'adil@example.com']
```

**Explanation:** The function accepts any number of email-like strings, trims surrounding whitespace, and returns a new list. This check is **not full email validation**: it does not guarantee that an address exists or can receive mail. Production applications should use a suitable validation approach and, when necessary, verify ownership by sending a confirmation email.

### Example 6 — Combine fixed parameters with `*args`

```python
def announce_event(event_name, *attendees):
    print(f"Event: {event_name}")
    print(f"Attendee count: {len(attendees)}")
    for attendee in attendees:
        print(f"- {attendee}")

announce_event("Python Workshop", "Adil", "Sara", "Ravi")
```

Output:
```text
Event: Python Workshop
Attendee count: 3
- Adil
- Sara
- Ravi
```

**Explanation:** The first positional argument fills `event_name`; remaining positional arguments are collected in `attendees`. The fixed parameter must be supplied before the extra positional arguments in this call.

### Example 7 — Unpack a list into positional arguments

```python
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

values = [2, 3, 4]
print(multiply(*values))
```

Output:
```text
24
```

**Explanation:** The `*` in the function definition collects arguments. The `*` in the call `multiply(*values)` does the reverse: it unpacks the list into separate positional arguments, effectively calling `multiply(2, 3, 4)`.

## 5. Important distinction: `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Accepts | Extra positional arguments | Extra keyword arguments |
| Stored as | Tuple | Dictionary |
| Example call | `f(10, 20)` | `f(name="Adil", age=23)` |
| Typical definition | `def f(*args):` | `def f(**kwargs):` |

Example:
```python
def describe(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

describe("Python", "SQL", level="beginner", active=True)
```

Output:
```text
Positional: ('Python', 'SQL')
Keyword: {'level': 'beginner', 'active': True}
```

Parameter ordering rule: in a function signature, regular parameters come before `*args`; `**kwargs` comes after them. Keyword-only parameters can follow `*args`.

## 6. Common mistakes and edge cases

1. **Thinking `args` is a special keyword:** it is just a conventional variable name; the asterisk matters.
2. **Expecting a list:** `args` is a tuple.
3. **Forgetting empty input:** `*args` can contain zero values.
4. **Confusing definition and call syntax:** `def f(*args)` collects; `f(*sequence)` unpacks.
5. **Using it when fixed parameters are clearer:** use explicit parameters when the required count is known.
6. **Assuming the email example fully validates email addresses:** it only performs a basic filter.
7. **Mixing up `*args` and `**kwargs`:** one handles positional values; the other handles named keyword values.

## 7. Real-world use cases

- **Email or notification utility:** accept multiple recipients, validate each, then pass accepted addresses to a mail service.
- **Shopping cart:** calculate the subtotal of a variable number of item prices.
- **Event registration:** accept a fixed event name and any number of attendee names.
- **Logging and formatting:** pass variable values to a helper that builds a message.
- **Test helpers:** create reusable test functions that compare a variable number of values.

In production, define expected types, validate inputs, document behavior for zero arguments, and avoid hiding required parameters inside `*args`.

## 8. Seven interview questions with answers

### Q1. What is `*args` in Python?
**Answer:** It allows a function to receive a variable number of positional arguments. Python collects them into a tuple.

### Q2. Is `args` a reserved word?
**Answer:** No. It is a convention. `*values` and `*emails` work the same way.

### Q3. What is the type of `args`?
**Answer:** A tuple. For example, `f(1, 2)` with `def f(*args)` receives `(1, 2)`.

### Q4. What happens when the caller passes no arguments?
**Answer:** The function receives an empty tuple, `()`. Code should handle that case if the operation requires at least one value.

### Q5. What is the difference between `*args` and `**kwargs`?
**Answer:** `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary.

### Q6. Can `*args` be used with normal parameters?
**Answer:** Yes. For example, `def greet(title, *names):` takes one required positional parameter and collects the remaining positional arguments in `names`.

### Q7. What is the difference between `func(*args)` in a definition and `func(*values)` in a call?
**Answer:** In a definition, the asterisk collects extra positional arguments into a tuple. In a call, it unpacks an iterable so its elements are passed as separate positional arguments.

## 9. Five practice tasks — questions and solutions

Try each question first, then compare your answer.

### Task 1: Sum all numbers
**Question:** Write `sum_numbers(*numbers)` that returns the sum of any number of numeric arguments.

**Answer / full code:**
```python
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(5, 10, 15))  # 30
print(sum_numbers())           # 0
```

### Task 2: Count strings longer than five characters
**Question:** Write a function that accepts any number of words and returns how many have more than five characters.

**Answer / full code:**
```python
def count_long_words(*words):
    return sum(1 for word in words if len(word) > 5)

print(count_long_words("Python", "SQL", "function", "Java"))  # 2
```

### Task 3: Find the largest number
**Question:** Return the largest supplied number. Decide what should happen for empty input.

**Answer / full code:**
```python
def largest_number(*numbers):
    if not numbers:
        raise ValueError("Provide at least one number")
    return max(numbers)

print(largest_number(4, 18, 2, 11))  # 18
# largest_number() raises ValueError
```

### Task 4: Remove duplicate names while preserving order
**Question:** Accept any number of names and return unique names in their original order.

**Answer / full code:**
```python
def unique_names(*names):
    result = []
    seen = set()

    for name in names:
        if name not in seen:
            seen.add(name)
            result.append(name)

    return result

print(unique_names("Adil", "Sara", "Adil", "Ravi"))
# ['Adil', 'Sara', 'Ravi']
```

### Task 5: Create a formatted message
**Question:** Write `format_message(prefix, *items)` that returns the prefix followed by all items separated by commas.

**Answer / full code:**
```python
def format_message(prefix, *items):
    return f"{prefix}: {', '.join(str(item) for item in items)}"

print(format_message("Topics", "Python", "SQL", "DSA"))
# Topics: Python, SQL, DSA
print(format_message("Topics"))
# Topics:
```

## 10. Small project: Email List Collector

### Project goal
Build a command-line program that receives several email-like values, trims whitespace, filters obvious invalid inputs, removes duplicates, and displays a final accepted list. This demonstrates `*args`, loops, strings, sets, lists, functions, and return values.

### Full project code

Save as `email_collector.py`:

```python
def is_basic_email_candidate(value):
    """Perform a simple educational check, not full email validation."""
    value = value.strip()

    return (
        bool(value)
        and value.count("@") == 1
        and " " not in value
        and not value.startswith("@")
        and not value.endswith("@")
    )


def collect_emails(*emails):
    """Return cleaned, basic-check-passing email candidates without duplicates."""
    accepted = []
    seen = set()

    for raw_email in emails:
        email = raw_email.strip()

        if not is_basic_email_candidate(email):
            print(f"Rejected: {raw_email!r}")
            continue

        # Case-insensitive duplicate detection for this simple example.
        key = email.casefold()
        if key in seen:
            print(f"Duplicate skipped: {email}")
            continue

        seen.add(key)
        accepted.append(email)
        print(f"Accepted: {email}")

    return accepted


def main():
    submitted_emails = [
        " syedadil24@gmail.com ",
        "adil@example.com",
        "not-an-email",
        "syedadil24@gmail.com",
        "two@@signs.com",
        "team@example.org",
    ]

    final_emails = collect_emails(*submitted_emails)

    print("\n--- Final email list ---")
    for number, email in enumerate(final_emails, start=1):
        print(f"{number}. {email}")

    print(f"\nAccepted unique candidates: {len(final_emails)}")


if __name__ == "__main__":
    main()
```

### Expected output

```text
Accepted: syedadil24@gmail.com
Accepted: adil@example.com
Rejected: 'not-an-email'
Duplicate skipped: syedadil24@gmail.com
Rejected: 'two@@signs.com'
Accepted: team@example.org

--- Final email list ---
1. syedadil24@gmail.com
2. adil@example.com
3. team@example.org

Accepted unique candidates: 3
```

### Project walkthrough
1. `main()` defines a list of sample input values.
2. `collect_emails(*submitted_emails)` unpacks the list, passing each element as a separate positional argument.
3. The function strips outer whitespace and calls the basic-check helper.
4. A set tracks normalized keys so duplicate candidates are skipped efficiently.
5. A list preserves the accepted email strings and their insertion order.
6. The function returns the accepted list; `main()` prints the results.

### Complexity
For `n` submitted email strings and total character count `C`, the loop performs approximately **O(C)** string-processing work on average, with set membership generally **O(1)** average per item. Additional storage is **O(n)** for the accepted list and duplicate set.

### Limitations and improvements
- The check is intentionally basic and does not prove that an address is deliverable.
- The example uses hard-coded values; a next step is to accept user input from the command line.
- A production system should use appropriate validation, safe handling of personal data, and confirmation workflows where ownership matters.
- Add automated tests for empty strings, whitespace, missing or repeated `@`, duplicate values with different capitalization, and an empty input list.


## 11. Debugging your email-validator attempt

This section records the common mistakes from the practice attempt and the corrected full program.

### What needed fixing?

1. **Check the current email, not the list:** use `if "@" not in removed_spaces:`, not `if "@" not in accepted_value:`. The list contains accepted emails; `removed_spaces` is the current string.
2. **Call `count()` on the string:** use `removed_spaces.count("@") > 1`. `"@".count` is a method reference and does not count the characters in the email.
3. **Append to the list:** use `accepted_value.append(removed_spaces)`, not `removed_spaces.append(accepted_value)`. Strings do not have a list-style `append()` method.
4. **Create the accepted list inside the function:** this gives each call a fresh result list and avoids carrying old results into later calls.
5. **Return inside the function:** `return accepted_value` must be indented within the function body. Code after the function call should print the returned list.
6. **Call the function, not the list:** use `print(email_val(...))`, not `accepted_value()`.
7. **Reject invalid values with `continue`:** after printing a rejection, skip to the next email so the invalid value is not accepted.

### Corrected full code

**Question:** Accept any number of email strings, trim leading/trailing spaces, reject values without `@` or with more than one `@`, store the accepted values in a list, return that list, and print it.

```python
def email_val(*emails):
    accepted_value = []

    for i in emails:
        removed_spaces = i.strip()

        if "@" not in removed_spaces:
            print("Rejected: missing @ ->", repr(removed_spaces))
            continue

        if removed_spaces.count("@") > 1:
            print("Rejected: more than one @ ->", repr(removed_spaces))
            continue

        accepted_value.append(removed_spaces)
        print("Successfully added:", removed_spaces)

    return accepted_value


final_emails = email_val(
    " syedadil24@gmail.com ",
    "invalid-email",
    "adil@@gmail.com",
    "  hello@example.com  ",
)

print("Final accepted list:", final_emails)
```

**Expected output:**

```text
Successfully added: syedadil24@gmail.com
Rejected: missing @ -> 'invalid-email'
Rejected: more than one @ -> 'adil@@gmail.com'
Successfully added: hello@example.com
Final accepted list: ['syedadil24@gmail.com', 'hello@example.com']
```

### Real-world explanation

- **Where:** a beginner contact-list or registration form exercise.
- **Why:** it demonstrates collecting multiple values, cleaning user input, applying simple rules, and returning the results.
- **When:** use this pattern when a function must process zero or more submitted values.
- **Limitation:** this only checks the number of `@` characters. For example, `@gmail.com` may pass. This is not complete email-address validation.

### Five practice checks

1. **Question:** What does `*emails` contain? **Answer:** A tuple of the positional arguments passed to the function.
2. **Question:** Why use `strip()`? **Answer:** To remove whitespace at the beginning and end of each submitted string.
3. **Question:** Why use `continue` after rejection? **Answer:** To skip the append statement for that invalid value and move to the next email.
4. **Question:** Why is `accepted_value.append(removed_spaces)` correct? **Answer:** The accepted list stores each cleaned email string.
5. **Question:** What does `return accepted_value` do? **Answer:** It sends the completed list back to the caller so it can be stored or printed.

## 12. Final revision checklist

You are ready to move on when you can explain and demonstrate all of these without copying:
- [ ] Define `*args` and explain why it creates a tuple.
- [ ] Write a function that accepts zero, one, or many arguments.
- [ ] Combine fixed parameters with `*args`.
- [ ] Explain collection (`def f(*args)`) versus unpacking (`f(*items)`).
- [ ] Compare `*args` with `**kwargs`.
- [ ] Explain the edge case for empty input.
- [ ] Run the project, test edge cases, and explain its limitations.
