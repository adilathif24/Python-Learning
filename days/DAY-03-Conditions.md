# Day 03 — Conditions in Python

**Status:** Study pack published; mark mastery only after completing the practice, project, tests, and quiz.

## 1. Definition

A **condition** is an expression Python evaluates as truthy or falsy to decide which code path to execute. Conditional statements let a program make decisions based on input or current data.

- `if`: runs its block when its condition is true.
- `elif`: checks another condition only when previous branches did not run.
- `else`: catches the remaining case when no earlier branch matched.
- **Nested condition:** an `if` statement inside another conditional block.
- **Logical operators:** `and` (both conditions must be true), `or` (at least one must be true), and `not` (reverses truth value).

## 2. Why, where, and when to use conditions

Use conditions when a program must choose an outcome: access control, eligibility, price discounts, input validation, grading, shipping, or transaction rules. Use `elif` for mutually exclusive alternatives and combine simple tests with `and`/`or`. Use nesting when the second decision only makes sense after the first passes. Avoid deeply nested conditions; prefer early returns or small named functions as programs grow.

## 3. Syntax and rules

```python
if condition:
    # runs when condition is true
    ...
elif another_condition:
    # checked only if earlier branches were false
    ...
else:
    # runs when none of the above matched
    ...
```

Rules:
- A colon (`:`) ends each branch header.
- Indentation defines the block; use consistent four-space indentation.
- Branches are evaluated top to bottom. Only the first matching branch in an `if/elif/else` chain runs.
- `else` has no condition.
- `and`, `or`, and `not` return truth values in Boolean expressions. `and` and `or` short-circuit.
- Compare boundaries deliberately: `age >= 18` includes 18, while `age > 18` excludes it.

### Dry run

For `score = 75`:
1. `score >= 90` → false.
2. `score >= 70` → true.
3. Print `B grade`; later branches are skipped.

## 4. Five worked examples

### Example 1 — Positive, negative, or zero

**Question:** Classify an integer.

```python
number = -4

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Expected output**
```text
Negative
```

**Explanation:** The first test is false, the second true, so the `elif` branch runs.

### Example 2 — Even or odd

**Question:** Decide whether a number is divisible by two.

```python
number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Expected output**
```text
Odd
```

**Explanation:** The remainder from `17 % 2` is 1, not 0.

### Example 3 — Grade boundaries

**Question:** Assign a grade from a score between 0 and 100.

```python
score = 80

if not 0 <= score <= 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("Needs improvement")
```

**Expected output**
```text
B
```

**Explanation:** Validate the range first, then check thresholds from highest to lowest so a score of 95 cannot be captured by a lower threshold.

### Example 4 — Login rule using logical operators

**Question:** Allow a user when the account is active and the password is correct.

```python
account_active = True
password_correct = False

if account_active and password_correct:
    print("Login successful")
else:
    print("Login denied")
```

**Expected output**
```text
Login denied
```

**Explanation:** `and` requires both conditions to be true.

### Example 5 — Nested shipping decision

**Question:** Free shipping is available for orders of at least ₹1,000, but only for members.

```python
is_member = True
order_total = 1200

if is_member:
    if order_total >= 1000:
        print("Free shipping")
    else:
        print("Member shipping fee applies")
else:
    print("Standard shipping fee applies")
```

**Expected output**
```text
Free shipping
```

**Explanation:** The order threshold is checked only after the member check succeeds.

## 5. Five practice tasks with complete solutions

Try each question before reading its solution.

### Task 1 — Voting eligibility

**Requirement:** Print eligible when age is at least 18; otherwise print not eligible.  
**Sample:** age = 17 → `Not eligible`

```python
age = 17

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

**Explanation:** The boundary age 18 is included because the comparison is `>=`.

### Task 2 — Number range

**Requirement:** Print `In range` if a value is from 1 through 10 inclusive.  
**Sample:** value = 10 → `In range`

```python
value = 10

if 1 <= value <= 10:
    print("In range")
else:
    print("Out of range")
```

**Explanation:** Chained comparisons make both boundaries explicit.

### Task 3 — Largest of two numbers

**Requirement:** Print the greater number, or report equality.  
**Sample:** a = 8, b = 8 → `Equal`

```python
a = 8
b = 8

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Equal")
```

**Explanation:** Equality is handled as its own remaining case.

### Task 4 — Discount check

**Requirement:** Apply a 10% discount when the purchase is at least ₹2,000; otherwise no discount.  
**Sample:** total = 2500 → payable = 2250.00

```python
total = 2500

if total < 0:
    print("Invalid total")
elif total >= 2000:
    payable = total * 0.90
    print(f"Payable: {payable:.2f}")
else:
    print(f"Payable: {total:.2f}")
```

**Expected output**
```text
Payable: 2250.00
```

**Explanation:** Invalid negative values are rejected before calculating a discount.

### Task 5 — Password length and account status

**Requirement:** An account can log in only if it is active and the password has at least 8 characters.  
**Sample:** active = True, password = `python123` → `Login allowed`

```python
active = True
password = "python123"

if active and len(password) >= 8:
    print("Login allowed")
else:
    print("Login denied")
```

**Explanation:** Both checks must pass. Real applications must verify passwords securely; this example only teaches conditional logic.

## 6. Common mistakes and edge cases

- **Wrong branch order:** checking `score >= 60` before `score >= 90` makes the A-grade branch unreachable for qualifying scores.
- **Boundary error:** `age > 18` excludes age 18; use `age >= 18` if 18 is eligible.
- **Using `=` instead of `==`:** `=` assigns; `==` compares.
- **Incorrect logical operator:** use `and` when all conditions must pass; use `or` when any one may pass.
- **Missing colon or inconsistent indentation:** Python raises a syntax/indentation error.
- **Invalid types:** comparing text such as `"eighteen"` directly with an integer raises `TypeError`; convert and validate user input.
- **Truthiness surprises:** empty strings and zero are falsy, but non-empty strings (including `"False"`) are truthy.
- **Negative values and exact boundaries:** test just below, at, and just above every threshold.

## 7. Interview questions and answers

**Q1. What is the purpose of `if`?**  
It conditionally executes a block when the expression evaluates to true.

**Q2. What is the difference between `if` and `elif`?**  
`if` starts the decision chain; `elif` adds another test that is evaluated only if earlier branches did not match.

**Q3. Can more than one branch in the same `if/elif/else` chain run?**  
No. At most one branch runs; Python stops at the first matching branch.

**Q4. What is the difference between `and` and `or`?**  
`and` requires both sides to be truthy; `or` requires at least one side to be truthy. Both short-circuit.

**Q5. When would you use a nested condition?**  
When an inner decision should be checked only after an outer prerequisite passes, such as checking order amount only for eligible members.

**Q6. Why should validation come before business rules?**  
It prevents invalid input from accidentally receiving a normal outcome and makes errors easier to reason about.

**Q7. What is a boundary test?**  
A test for values just below, exactly at, and just above a threshold.

## 8. Real-world mini-project — Eligibility Checker

### Requirements
- Ask for age and exam score.
- Eligibility requires age from 18 through 35 inclusive and score at least 60.
- Reject non-integer age/score and score outside 0–100.
- Show a clear decision and test normal, boundary, and invalid inputs.

### Complete runnable code

Save as `eligibility_checker.py` and run with `python eligibility_checker.py`.

```python
def check_eligibility(age, score):
    """Return an eligibility result after validating input ranges."""
    if not isinstance(age, int) or isinstance(age, bool):
        return "Invalid age: enter a whole number."
    if not isinstance(score, int) or isinstance(score, bool):
        return "Invalid score: enter a whole number."
    if age < 0:
        return "Invalid age: age cannot be negative."
    if not 0 <= score <= 100:
        return "Invalid score: enter a score from 0 to 100."

    if 18 <= age <= 35 and score >= 60:
        return "Eligible"
    return "Not eligible"


def main():
    try:
        age = int(input("Enter age: ").strip())
        score = int(input("Enter exam score (0-100): ").strip())
    except ValueError:
        print("Invalid input: age and score must be whole numbers.")
        return

    print(check_eligibility(age, score))


if __name__ == "__main__":
    main()
```

### Sample run

```text
Enter age: 22
Enter exam score (0-100): 75
Eligible
```

### Tests — normal, boundary, invalid

Save as `test_eligibility_checker.py` next to the project file and run `python -m unittest -v`.

```python
import unittest
from eligibility_checker import check_eligibility


class TestEligibilityChecker(unittest.TestCase):
    def test_normal_eligible(self):
        self.assertEqual(check_eligibility(22, 75), "Eligible")

    def test_score_below_threshold(self):
        self.assertEqual(check_eligibility(22, 59), "Not eligible")

    def test_age_lower_boundary(self):
        self.assertEqual(check_eligibility(18, 60), "Eligible")

    def test_age_upper_boundary(self):
        self.assertEqual(check_eligibility(35, 60), "Eligible")

    def test_age_outside_range(self):
        self.assertEqual(check_eligibility(36, 90), "Not eligible")

    def test_invalid_score_range(self):
        self.assertIn("Invalid score", check_eligibility(22, 101))

    def test_negative_age(self):
        self.assertIn("Invalid age", check_eligibility(-1, 80))

    def test_non_integer_value(self):
        self.assertIn("Invalid age", check_eligibility("twenty", 80))


if __name__ == "__main__":
    unittest.main()
```

The function tests the decision logic directly. The interactive `main()` additionally handles text that cannot be converted to integers.

## 9. Revision quiz

Answer before checking the key.

1. Which branch runs when every `if` and `elif` condition is false?
2. What does `18 <= age <= 35` mean?
3. Should a score of 90 get grade A if the code checks `score >= 60` first?
4. When do you use `and` instead of `or`?
5. Why validate a score before evaluating eligibility?

### Answer key
1. `else`, if present.
2. Age is at least 18 and at most 35, including both endpoints.
3. No; the lower threshold would match first. Check higher thresholds first.
4. When every condition must be true.
5. To reject invalid data before applying business rules.

### Independent challenge
Extend the eligibility checker so applicants aged 18–25 with a score of at least 80 receive `Priority eligible`. All other eligible applicants should receive `Eligible`. Add tests for ages 17, 18, 25, 26, and scores 79, 80, and 100.

## 10. Progress checklist

- [ ] I can explain `if`, `elif`, `else`, nesting, and logical operators without reading.
- [ ] I ran all five worked examples and predicted their outputs first.
- [ ] I solved the five tasks before checking their solutions.
- [ ] I ran the mini-project and all unit tests.
- [ ] I completed the quiz and independent challenge.

**Completion rule:** Do not mark Day 03 complete until practice has been attempted, the tests pass, and the learner can explain branch order and boundary choices.
