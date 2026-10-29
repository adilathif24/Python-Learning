# Python from Basics to Functions and Lists

> **Purpose:** Revision notes based on the Python topics practised so far. Explanations are in English, with runnable examples, real-world uses, practice questions, interview answers, and the Name Management mini-project.
>
> **AI assistance disclosure:** This guide was prepared with AI assistance using the learner's practice code and questions. AI helped organise concepts, explain errors, and generate practice material. Run every example, understand it, and adapt it yourself; disclose AI assistance honestly when sharing this repository.

## Learning roadmap covered

1. Output, variables, data types, input, and operators
2. Conditions: `if`, `elif`, `else`
3. Loops: `for` and `while`
4. Counters and accumulators
5. Number problems: sum, multiplication tables, factorial, prime, Fibonacci, digit counting
6. Strings: vowels and consonants
7. Swapping values
8. Functions: `def`, parameters, arguments, calling, and `return`
9. Lists, indexes, membership, `append()`, `remove()`, and `len()`
10. Mini-project: add, delete, restore, and view names

---

## 1. Python basics

### Output with `print()`

**Definition:** `print()` displays information in the terminal.

```python
print("Hello, Python!")
print(10)
```

**Where/why:** Display results, debugging messages, and user-friendly program output.

### Variables

A **variable** is a name that refers to a value.

```python
name = "Adil"
age = 23
height = 5.11
is_learning = True

print(name)
print(age)
print(height)
print(is_learning)
```

Python infers the type from the assigned value. Common types are `str` (text), `int` (whole number), `float` (decimal number), and `bool` (`True`/`False`).

### Input

`input()` reads text typed by the user. Convert it when you need a number.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name)
print("Next year you will be", age + 1)
```

### Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | addition | `3 + 2 == 5` |
| `-` | subtraction | `3 - 2 == 1` |
| `*` | multiplication | `3 * 2 == 6` |
| `/` | division | `5 / 2 == 2.5` |
| `//` | floor division | `5 // 2 == 2` |
| `%` | remainder | `5 % 2 == 1` |
| `**` | power | `2 ** 3 == 8` |
| `==` | equality comparison | `3 == 3` is `True` |
| `!=` | not equal | `3 != 4` is `True` |
| `>`, `<` | greater/less than | `5 > 2` |
| `and`, `or`, `not` | logical operators | combine or invert conditions |

**Real-world use:** Variables store prices, names, scores, counts, and calculation results. Operators calculate totals and test rules.

## 2. Conditions

**Definition:** Conditions let a program choose which code to execute based on whether an expression is true or false.

**Syntax:**

```python
if condition:
    # runs if condition is true
elif another_condition:
    # runs if the first condition is false and this is true
else:
    # runs if no earlier condition is true
```

**Example — pass/fail**

```python
marks = 72
if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

**Why/where:** Validate marks, check eligibility, decide discounts, and handle whether a requested name exists.

**Common mistake:** `=` assigns a value; `==` compares two values.

## 3. Loops

### `for` loop

A `for` loop repeats code for each item in an iterable, or over a range of numbers.

```python
for i in range(1, 6):
    print(i)
```

Output: `1 2 3 4 5`, each on a separate line.

- `range(1, 6)` starts at 1 and stops before 6.
- `range(5)` gives 0 through 4.
- `range(5, 0, -1)` counts down 5, 4, 3, 2, 1.

### `while` loop

A `while` loop repeats while its condition remains true. Make sure something changes so the loop can stop.

```python
a = 1
while a <= 5:
    print(a)
    a += 1
```

**Common mistake:** If `a` never changes, `a <= 5` may stay true forever, creating an infinite loop.

### Counter vs accumulator

- **Counter:** counts how many times something occurs; often increases by 1.
- **Accumulator:** keeps a running total; adds each new value.

```python
count = 0
total = 0
for number in range(1, 6):
    count += 1
    total += number
print("Count:", count)  # 5
print("Total:", total)  # 15
```

**Real-world use:** Count transactions, total a bill, sum scores, and process rows of data.

## 4. Worked coding examples

### Example 1 — Sum from 1 to 10

```python
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
```

**Explanation:** Start the accumulator at zero. Each loop adds the current number. `range(1, 11)` includes 1 through 10 because the stop value is excluded.

### Example 2 — Multiplication table

```python
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

**Explanation:** The loop multiplier changes from 1 to 10; the product is recalculated each time.

### Example 3 — Factorial using a loop

**Definition:** The factorial of a non-negative integer `n`, written `n!`, is the product of all positive integers from 1 to `n`. By definition, `0! = 1`.

```python
def factorial(n):
    if n < 0:
        return None  # factorial is not defined for negative integers here
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120
print(factorial(0))  # 1
```

**Dry run for 5:** result starts at 1; multiply by 1 → 1, by 2 → 2, by 3 → 6, by 4 → 24, by 5 → 120.

**Important correction:** A function should return the calculated value, such as `return result`, not `return factorial` (which refers to the function itself).

### Example 4 — Prime-number check

A **prime number** is an integer greater than 1 with exactly two positive divisors: 1 and itself.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(12))  # False
print(is_prime(1))   # False
```

**Explanation:** Values below 2 are not prime. If any divisor from 2 through the square root divides evenly, the number is not prime.

### Example 5 — Fibonacci sequence

Each Fibonacci value after the first two is the sum of the previous two. This example prints the first 8 values.

```python
a, b = 0, 1
for _ in range(8):
    print(a, end=" ")
    a, b = b, a + b
# 0 1 1 2 3 5 8 13
```

**Explanation:** At each step, move the second value into the first and calculate the next pair. The underscore `_` is used when the loop variable itself is not needed.

### Example 6 — Count digits

```python
n = abs(12345)
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print(count)  # 5
```

**Explanation:** Integer floor division by 10 removes the last digit each time. The loop condition is `n > 0`, not `n < 0`, because the number is made non-negative with `abs()`. Zero is handled separately.

### Example 7 — Count vowels and consonants

```python
text = "python by me"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
```

**Explanation:** `ch` is the current character. Test `ch in vowels`, not `text in vowels`. `isalpha()` skips spaces and punctuation.

### Example 8 — Swap using a third variable

```python
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)  # 20 10
```

**Explanation:** Store the first value in `temp` so it is not lost when assigning `b` to `a`.

### Example 9 — Swap without a third variable

Python supports tuple unpacking:

```python
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10
```

**Explanation:** The right-hand values are evaluated before assigning the new values to the left-hand variables.

## 5. Functions

**Definition:** A function is a named, reusable block of code that performs a task.

**Syntax:**

```python
def function_name(parameters):
    # function body
    return result  # optional

answer = function_name(arguments)
```

- `def` begins the definition.
- A **parameter** is the variable listed in the definition.
- An **argument** is the actual value passed when calling the function.
- The colon `:` and indentation are required.
- The function body runs when the function is called.
- `return` passes a value back to the caller; `print()` only displays a value.
- If no explicit return value is provided, Python returns `None`.

### Example — function with a parameter and return value

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7
```

Here, `a` and `b` are parameters; `3` and `4` are arguments.

### Example — function with no parameters

```python
def say_hello():
    print("Hello!")

say_hello()
```

### Why use functions?

- Reuse code without repeating it.
- Break a large problem into smaller tasks.
- Give operations meaningful names.
- Test and debug one part at a time.
- Keep programs easier to read and maintain.

**Real-world use:** Functions can validate a form, calculate an invoice, count records, add a contact, or retrieve a report.

## 6. Lists

**Definition:** A list is an ordered, mutable collection. It can hold multiple values and may contain duplicates.

```python
names = ["Adil", "Syed", "Ali"]
print(names[0])  # Adil
```

### Common operations

```python
names.append("Athif")       # add at the end
names.remove("Syed")        # remove first matching value
print(len(names))           # count current items
print("Ali" in names)       # membership check
print("Ravi" not in names)  # absent?
```

- Indexing starts at zero.
- `append(value)` adds one item at the end.
- `remove(value)` removes the first matching value and raises `ValueError` if missing.
- `len(list)` returns the number of current items.
- `in` and `not in` test membership.
- List indexes shift after an earlier item is removed.

**Real-world use:** Lists can store task names, product names, students, or results while a program runs. A normal list is in memory; it does not automatically save to a file or database.

## 7. Name Management mini-project

This beginner project practises functions, conditions, lists, membership, and counting.

```python
names = []
deleted = []
restore = []

def addname(name):
    if name not in names:
        names.append(name)
        print("New name added =", name)
    else:
        print("Name already exists")

def removename(name):
    if name in names:
        names.remove(name)
        deleted.append(name)
        print("Name successfully deleted =", name)
    else:
        print("No suitable name to delete")

def restoreName(name):
    if name in names:
        print("Name already exists in active names")
    elif name in deleted:
        deleted.remove(name)
        names.append(name)
        restore.append(name)
        print("Restored successfully =", name)
    else:
        print("No deleted name found to restore")

def viewname():
    print("Active names:", names)
    print("Total active names:", len(names))
    print("Deleted names:", deleted)
    print("Total currently deleted:", len(deleted))
    print("Restoration history:", restore)

addname("syed adil")
addname("syed")
addname("adil")
addname("ali")
addname("athif")
removename("syed adil")
removename("adil")
viewname()
restoreName("syed adil")
restoreName("adil")
viewname()
```

### What each list means

- `names`: currently active names.
- `deleted`: names removed from the active list and not yet restored.
- `restore`: history of names successfully restored.

### Important behaviour to understand

1. A name must be active before it can be deleted.
2. A name must be in `deleted` before it can be restored.
3. A restored name is removed from `deleted`, appended to `names`, and logged in `restore`.
4. The active count is `len(names)`; it is not the total number of names ever added.
5. Checking `name in names` before restoration avoids duplicate active names.
6. Passing an explicit name is safer and clearer than depending on a list index that may change after deletion.

**Real-world limitation:** This is a practice program. Its lists disappear when Python exits. A real application may use a database, validation, unique record IDs, permissions, and an audit log.

## 8. Five practice questions with solutions

Try each problem before opening the solution.

### Q1. Print numbers from 1 to 10 using a loop

```python
for i in range(1, 11):
    print(i)
```

**Explanation:** The stop argument is excluded, so use 11 to include 10.

### Q2. Calculate the sum of numbers from 1 to n

```python
n = 5
total = 0
for i in range(1, n + 1):
    total += i
print(total)  # 15
```

**Explanation:** `total` is an accumulator; every loop adds the current value.

### Q3. Write a function that multiplies two numbers

```python
def multiply(a, b):
    return a * b

print(multiply(4, 5))  # 20
```

**Explanation:** The function returns the result so the caller can use it.

### Q4. Add a name only if it is not already present

```python
names = ["Adil", "Ali"]
name = "Syed"
if name not in names:
    names.append(name)
print(names)  # ['Adil', 'Ali', 'Syed']
```

**Explanation:** Membership check prevents adding the same exact string twice.

### Q5. Safely delete a name

```python
names = ["Adil", "Syed", "Ali"]
target = "Syed"
if target in names:
    names.remove(target)
else:
    print("Name not found")
print(names)  # ['Adil', 'Ali']
```

**Explanation:** Check existence before calling `remove()`.

## 9. Interview questions and answers

1. **What is Python?** A high-level, general-purpose programming language.
2. **What is a variable?** A name referring to a value.
3. **What does `print()` do?** Displays output.
4. **What does `input()` return?** A string; convert it to `int` or `float` when numeric input is required.
5. **Difference between `/` and `//`?** `/` performs true division; `//` performs floor division.
6. **What does `%` do?** Returns the remainder after division.
7. **What is a condition?** An expression used to decide which branch runs.
8. **Difference between `=` and `==`?** Assignment versus equality comparison.
9. **What is a loop?** A way to repeat code.
10. **Difference between `for` and `while`?** `for` iterates over items/ranges; `while` repeats while a condition is true.
11. **What is an infinite loop?** A loop whose stopping condition never becomes false.
12. **What is a counter?** A variable used to count occurrences or iterations.
13. **What is an accumulator?** A variable that keeps a running result such as a sum.
14. **What is factorial?** The product of positive integers up to a non-negative integer, with `0! = 1`.
15. **What is a prime number?** An integer greater than 1 with exactly two positive divisors.
16. **What is Fibonacci sequence?** A sequence where each term is the sum of the previous two.
17. **What is a function?** A reusable named block of code.
18. **What does `def` do?** Defines a function.
19. **Parameter vs argument?** A parameter is named in the definition; an argument is passed in the call.
20. **What is `return`?** It passes a result back to the caller and exits the function.
21. **Difference between `print` and `return`?** Displaying output versus returning a value for later use.
22. **What is a list?** An ordered, mutable collection.
23. **What does `append()` do?** Adds one item to the end.
24. **What does `remove()` do?** Removes the first matching value; missing values raise `ValueError`.
25. **What does `len()` do?** Counts current items in a collection.
26. **What does `in` mean?** Checks membership.
27. **Why can a list index change after deletion?** Items to the right shift left.
28. **Why keep deleted and restored lists?** To demonstrate state changes and simple restoration history.
29. **What happens if a function has no explicit return?** It returns `None`.
30. **How can the name project be improved?** Add a menu, validation, tests, persistent storage, and unique IDs for real records.

## 10. Common beginner mistakes

| Mistake | Fix |
|---|---|
| Missing colon after `if`, `for`, `while`, or `def` | Add `:` and indent the body |
| Incorrect indentation | Use consistent indentation, usually 4 spaces |
| Using `=` instead of `==` in a condition | Use equality comparison `==` |
| Forgetting to update a `while` loop variable | Update the variable so the loop can stop |
| Using `while n < 0` to process a positive number | Check the intended condition, e.g. `n > 0` |
| Returning the function name instead of the answer | Return the calculated variable/value |
| Checking `text in vowels` instead of `ch in vowels` | Test the current character inside the loop |
| Removing a missing list value | Check membership first |
| Assuming indexes stay fixed after deletion | Inspect the updated list or pass the target value |
| Confusing current count with lifetime total additions | State exactly what each count measures |

## 11. Suggested revision method

1. Type each example yourself and run it.
2. Predict output before execution.
3. Change the input and test boundary cases: zero, negative numbers, empty lists, duplicates, and missing values.
4. Explain each line in English: purpose, input, condition, operation, and output.
5. Solve the five practice questions without looking at answers first.
6. Extend the mini-project with a menu: Add, Delete, Restore, View, Exit.
7. Next topics after this stage: strings in more depth, tuples, sets, dictionaries, file handling, exceptions, and then problem-solving/DSA.

---

## AI assistance disclosure

This guide was drafted and organised with AI assistance based on the learner's practice code and questions. AI helped explain concepts, correct mistakes, and prepare examples and interview practice. The learner should run, review, adapt, and understand the material and be transparent about AI assistance when sharing it publicly.
