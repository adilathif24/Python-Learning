# Day 17 — Loop Mastery: break, continue, Nested Loops and Menus

**Status:** Full study pack. Do not mark complete until practice and project tests are passed.

## 1. Definition
Loop control changes the normal iteration flow. `break` exits the nearest loop; `continue` skips the remainder of the current iteration; nested loops run one loop inside another. A sentinel loop continues until a stop value is entered.

## 2. Why and when
Use `break` to stop searching after a match, `continue` to skip invalid/unwanted records, nested loops for grids or pair combinations, and sentinel loops for interactive menus. Avoid unnecessary nesting because it increases complexity. A menu should always provide a clear exit path.

## 3. Syntax and mental model
```python
for row in range(3):
    for col in range(2):
        print(row, col)
```
Outer loop selects a row; inner loop runs through all columns for each row. Total iterations are 3 × 2 = 6.

## 4. Five worked examples
### Example 1 — break on target
```python
for n in [2, 4, 7, 8]:
    if n % 2:
        print("First odd:", n)
        break
```
Output: `First odd: 7`. Break terminates the loop once found.

### Example 2 — continue on invalid item
```python
values = [3, -1, 4, 0, 8]
for value in values:
    if value <= 0: continue
    print(value)
```
Output: 3, 4, 8 on separate lines. Non-positive values are skipped.

### Example 3 — multiplication grid
```python
for row in range(1, 3):
    for col in range(1, 4):
        print(row * col, end=" ")
    print()
```
Output: `1 2 3` then `2 4 6`. Each inner loop builds a row.

### Example 4 — loop else
```python
for n in [2, 4, 6]:
    if n == 5: break
else:
    print("No target found")
```
Output: `No target found`. Else executes if no break happened.

### Example 5 — sentinel loop
```python
commands = ["add", "show", "quit"]
for command in commands:
    if command == "quit": break
    print(command)
```
Output: `add`, then `show`. Quit stops the loop.

## 5. Five tasks with solutions
### Task 1 — Print a 3x3 grid
```python
for _ in range(3):
    print("* * *")
```
Output is three rows of three stars. Use an outer loop for rows.

### Task 2 — First divisible by 7
```python
values = [5, 10, 14, 21]
for value in values:
    if value % 7 == 0:
        print(value); break
```
Output: `14`. First match stops the search.

### Task 3 — Skip vowels
```python
word = "python"
for char in word:
    if char in "aeiou": continue
    print(char, end="")
print()
```
Output: `pythn`. Continue skips vowels.

### Task 4 — Count pair combinations
```python
pairs = 0
for a in [1, 2, 3]:
    for b in ["x", "y"]:
        pairs += 1
print(pairs)
```
Output: `6`. Every first-list item combines with each second-list item.

### Task 5 — Retry a bounded sequence
```python
attempts = ["bad", "bad", "ok"]
for attempt_number, result in enumerate(attempts, start=1):
    if result == "ok":
        print("Success on", attempt_number); break
else:
    print("Failed")
```
Output: `Success on 3`. Enumerate counts attempts.

## 6. Common mistakes
- `break` exits only the innermost loop.
- Infinite loops need an exit condition.
- A continue before a counter update can accidentally prevent progress.
- Nested loops multiply work; consider complexity for large inputs.
- Menu input should handle unknown choices and exit gracefully.

## 7. Interview Q&A
1. Break vs continue? **Exit loop vs skip current iteration.**
2. What is a nested loop? **A loop inside another loop.**
3. What does loop else mean? **It runs if the loop finished without break.**
4. Why bound retry loops? **Prevent endless retry and improve usability.**
5. How many operations in two ranges m and n? **About m × n inner iterations.**

## 8. Project — Educational ATM Simulator
Save as `atm_simulator.py`.
```python
def process_commands(balance, commands):
    if balance < 0: raise ValueError("Initial balance cannot be negative")
    results = []
    for command, amount in commands:
        if command == "quit":
            results.append("Goodbye"); break
        if command == "balance":
            results.append(f"Balance: {balance:.2f}")
        elif command == "deposit":
            if amount <= 0: results.append("Invalid amount")
            else:
                balance += amount; results.append("Deposit successful")
        elif command == "withdraw":
            if amount <= 0: results.append("Invalid amount")
            elif amount > balance: results.append("Insufficient funds")
            else:
                balance -= amount; results.append("Withdrawal successful")
        else: results.append("Unknown command")
    return balance, results

def main():
    balance = 100.0
    while True:
        print("1 Balance 2 Deposit 3 Withdraw 4 Quit")
        choice = input("Choice: ").strip()
        if choice == "1": print(f"Balance: ₹{balance:.2f}")
        elif choice in {"2", "3"}:
            try: amount = float(input("Amount: "))
            except ValueError:
                print("Enter a number"); continue
            balance, messages = process_commands(balance, [("deposit" if choice=="2" else "withdraw", amount)])
            print(messages[0])
        elif choice == "4": print("Goodbye"); break
        else: print("Invalid option")

if __name__ == "__main__": main()
```
Example: balance ₹100, withdraw ₹30 → withdrawal successful and balance ₹70.

### Tests — `test_atm_simulator.py`
```python
import unittest
from atm_simulator import process_commands

class ATMTests(unittest.TestCase):
    def test_deposit(self): self.assertEqual(process_commands(10,[("deposit",5)])[0],15)
    def test_withdraw(self): self.assertEqual(process_commands(10,[("withdraw",4)])[0],6)
    def test_insufficient(self): self.assertEqual(process_commands(3,[("withdraw",4)])[0],3)
    def test_invalid_deposit(self): self.assertEqual(process_commands(10,[("deposit",0)])[0],10)
    def test_quit_stops(self): self.assertEqual(process_commands(10,[("quit",0),("deposit",5)])[0],10)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Which statement skips the iteration? **continue.**
2. What ends a loop immediately? **break.**
3. Why use sentinel loops? **Repeat until a stop value.**
4. Nested loops with 4 × 5 values? **20 inner runs.**
5. When does loop else execute? **When no break ends the loop.**
**Challenge:** Add an attempt limit and lockout after three failed simulated PIN checks, with tests.

## Real-world use cases — where, when and how
1. **ATM/menu flow:** Where: command-line tools. When users make several choices. How: loop until the quit option is selected, handle unknown choices and bound retries.
2. **Batch processing:** Where: imported records. When each row needs checking. How: iterate through all rows and record outcomes.
3. **Search optimization:** Where: item or user lookup. When the first matching record is enough. How: use break to stop unnecessary iterations.
4. **Data filtering:** Where: log processing. When invalid/irrelevant entries should be skipped. How: use continue to skip only that record.
5. **Grid/pair generation:** Where: schedules and combinations. When each row needs comparison against each column. How: use nested loops and estimate the n×m work.


## 10. Completion
- [ ] I can trace break, continue, loop else and nested loops.
- [ ] I completed tasks and ATM tests.
- [ ] I solved the lockout challenge.
