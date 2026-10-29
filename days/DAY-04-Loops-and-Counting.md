# Day 04 — Loops and Counting

**Status:** Full lesson pack published. Mark mastery only after completing practice, project, tests and quiz.

## 1. Definition

A **loop** repeats code. A `for` loop processes each item in an iterable; a `while` loop repeats while its condition is true. A **counter** tracks how many times something happens. An **accumulator** combines values, for example a running sum. `break` exits a loop and `continue` skips to the next iteration.

## 2. Why, where and when

Use `for` for iterables and known ranges, such as calculating totals or processing records. Use `while` when you continue until a condition changes, such as a menu or input retry. Use counters for counts and accumulators for sums/products. Use `break` to stop after a result is found; use `continue` to skip selected items. Avoid loops that never change the condition, and prefer built-ins like `sum()` when they express the goal more clearly.

## 3. Syntax and rules

```python
for item in iterable:
    print(item)

for n in range(1, 6):  # 1 through 5; stop is exclusive
    print(n)

count = 0
while count < 3:
    print(count)
    count += 1
```

`range(start, stop, step)` excludes `stop`. Indentation defines the loop body. In a `while` loop, make sure a state variable changes so that termination can eventually happen.

### Dry run

```python
total = 0
for n in range(1, 4):
    total += n
print(total)
```
Trace: n=1 → total=1; n=2 → total=3; n=3 → total=6; then the loop ends and prints 6.

## 4. Five worked examples

### Example 1 — Count 1 to 5

```python
for n in range(1, 6):
    print(n)
```
**Output**
```text
1
2
3
4
5
```
**Explanation:** The stop value 6 is excluded.

### Example 2 — Sum values

```python
total = 0
for n in range(1, 6):
    total += n
print(total)
```
**Output:** `15`  
**Explanation:** The accumulator retains the sum from earlier iterations.

### Example 3 — Countdown

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
```
**Output**
```text
3
2
1
Go!
```
**Explanation:** Decrementing the counter makes the condition eventually false.

### Example 4 — Skip even values

```python
for n in range(1, 8):
    if n % 2 == 0:
        continue
    print(n)
```
**Output**
```text
1
3
5
7
```
**Explanation:** `continue` skips the remainder of that iteration.

### Example 5 — Find a target

```python
values = [4, 8, 12, 16]
target = 12
for value in values:
    if value == target:
        print("Found")
        break
else:
    print("Not found")
```
**Output:** `Found`  
**Explanation:** The loop's `else` runs only if no `break` occurs.

## 5. Five practice tasks with complete solutions

### Task 1 — Multiplication table

```python
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```
**Sample output:** first line `7 x 1 = 7`; final line `7 x 10 = 70`.  
**Explanation:** `range(1, 11)` generates ten multipliers.

### Task 2 — Count digits

```python
number = -50720
digit_count = len(str(abs(number)))
print(digit_count)
```
**Output:** `5`  
**Explanation:** Convert the absolute integer to text; the minus sign is not a digit.

### Task 3 — Factorial

```python
n = 5
result = 1
if n < 0:
    print("Invalid: factorial needs a non-negative integer")
else:
    for value in range(2, n + 1):
        result *= value
    print(result)
```
**Output:** `120`  
**Explanation:** Multiply numbers from 2 through n. Starting at 1 handles 0! and 1!.

### Task 4 — Find maximum without max()

```python
values = [12, 3, 27, 8, 19]
if not values:
    print("Empty list")
else:
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    print(largest)
```
**Output:** `27`  
**Explanation:** Track the largest value seen so far.

### Task 5 — Validate a choice using while

```python
choices = ["", "x", "2"]
index = 0
choice = ""
while choice not in {"1", "2", "3"} and index < len(choices):
    choice = choices[index]
    index += 1
if choice in {"1", "2", "3"}:
    print(f"Accepted: {choice}")
else:
    print("No valid choice entered")
```
**Output:** `Accepted: 2`  
**Explanation:** A bounded loop avoids an infinite retry in this simulation.

## 6. Common mistakes and edge cases

- `range(1, 5)` stops at 4, not 5.
- Forgetting to update a `while` counter can create an infinite loop.
- Initialising a product accumulator to 0 makes every multiplication result 0; use 1 for factorial-like products.
- Counting digits in a negative integer should ignore the sign.
- An empty collection has no first element; check before using index 0.
- `break` exits only the nearest loop.
- Off-by-one errors: test 0, 1, and exact start/stop boundaries.

## 7. Interview questions and answers

**Q1. Difference between `for` and `while`?** `for` iterates over an iterable; `while` repeats based on a condition.

**Q2. What does `range(1, 5)` produce?** 1, 2, 3, 4.

**Q3. Difference between a counter and accumulator?** A counter typically counts events; an accumulator combines values into a running result.

**Q4. What is the difference between `break` and `continue`?** `break` exits the nearest loop; `continue` skips to the next iteration.

**Q5. How do you avoid an infinite `while` loop?** Ensure its condition can become false and add sensible limits for user-driven retries.

**Q6. What does a loop's `else` mean?** It runs if the loop finishes normally, without a `break`.

## 8. Real-world mini-project — Menu-Driven Expense Tracker

Save as `expense_tracker.py`. It keeps expenses in memory, displays a menu, lists entries and calculates a total.

```python
def run_menu(commands):
    expenses = []
    output = []
    for command, value in commands:
        if command == "add":
            if not isinstance(value, (int, float)) or value < 0:
                output.append("Invalid amount")
            else:
                expenses.append(float(value))
                output.append("Expense added")
        elif command == "list":
            output.append(f"Expenses: {expenses}")
        elif command == "total":
            output.append(f"Total: {sum(expenses):.2f}")
        elif command == "quit":
            output.append("Goodbye")
            break
        else:
            output.append("Unknown command")
    return output


def main():
    expenses = []
    while True:
        print("\n1. Add expense  2. List  3. Total  4. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            raw = input("Amount: ").strip()
            try:
                amount = float(raw)
                if amount < 0:
                    print("Amount cannot be negative")
                else:
                    expenses.append(amount)
                    print("Expense added")
            except ValueError:
                print("Enter a valid number")
        elif choice == "2":
            print(expenses if expenses else "No expenses")
        elif choice == "3":
            print(f"Total: ₹{sum(expenses):.2f}")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Choose 1, 2, 3, or 4")


if __name__ == "__main__":
    main()
```

### Sample run
```text
1. Add expense  2. List  3. Total  4. Quit
Choose: 1
Amount: 120
Expense added
Choose: 3
Total: ₹120.00
Choose: 4
Goodbye
```

### Tests

Save as `test_expense_tracker.py`; run `python -m unittest -v`.

```python
import unittest
from expense_tracker import run_menu


class TestExpenseTracker(unittest.TestCase):
    def test_add_and_total(self):
        result = run_menu([("add", 10), ("add", 2.5), ("total", None)])
        self.assertEqual(result[-1], "Total: 12.50")

    def test_negative_amount(self):
        self.assertEqual(run_menu([("add", -1)])[0], "Invalid amount")

    def test_unknown_command(self):
        self.assertEqual(run_menu([("x", None)])[0], "Unknown command")

    def test_quit_stops_later_commands(self):
        result = run_menu([("quit", None), ("add", 4)])
        self.assertEqual(result, ["Goodbye"])

    def test_empty_total(self):
        self.assertEqual(run_menu([("total", None)]), ["Total: 0.00"])


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. What values are produced by `range(2, 6)`?
2. What makes a `while` loop stop?
3. Why initialise factorial result to 1?
4. What is the difference between `break` and `continue`?
5. What edge case should a maximum-finding loop handle?

### Answer key
1. 2, 3, 4, 5.
2. Its condition becomes false or a control statement exits the loop.
3. One is the multiplicative identity; multiplying by zero would always result in zero.
4. `break` exits; `continue` moves to the next iteration.
5. An empty collection.

### Independent challenge
Extend the expense tracker with a fifth menu option to remove an expense by its 1-based position. Handle empty lists and out-of-range positions, and add tests for both edge cases.

## 10. Progress checklist

- [ ] I can choose between `for` and `while` and explain why.
- [ ] I ran five examples and predicted the outputs.
- [ ] I completed five practice tasks.
- [ ] Project tests pass.
- [ ] I solved the independent challenge.

## Real-world use cases — where, when and how
1. **Batch processing:** Where: CSV/data imports. When: every row needs handling. How: iterate over rows and validate each one.
2. **Totals and averages:** Where: finance reports. When: many amounts must be aggregated. How: use an accumulator or a built-in such as sum.
3. **Retries:** Where: CLI prompts. When: an input may be invalid. How: use a bounded while loop with a clear exit path.
4. **Search:** Where: contact/task lists. When: the first matching record is enough. How: scan with for and stop with break.
5. **Menu applications:** Where: local utilities. When: the user performs multiple operations. How: repeat choices until a quit command is received.

