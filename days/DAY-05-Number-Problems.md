# Day 05 — Number Problems and Patterns

**Status:** Full study pack published. Verify by solving tasks and running the tests before marking mastery.

## 1. Definition

Number problems use arithmetic, loops, remainders and comparisons to analyse numeric values. Common patterns include factorial, prime checking, Fibonacci sequences, digit counting/sum/reversal, numeric palindrome, Armstrong numbers, GCD and LCM.

## 2. Why, where and when

These problems develop loop control and algorithmic thinking, and appear in entry-level interviews, validation tasks and numeric utilities. Use modulo (`%`) to inspect a final digit or divisibility; use integer division (`//`) to remove a final digit. Use built-ins and standard libraries in production when they are clearer and better tested; implement algorithms manually while learning or when a custom rule is required.

## 3. Syntax and rules

- `n % 10` obtains the last decimal digit of a non-negative integer.
- `n //= 10` removes its last digit.
- Factorial: (n! = 1 \times 2 \times \cdots \times n), with (0! = 1).
- A prime is an integer greater than 1 with exactly two positive divisors.
- Fibonacci begins commonly with 0, 1, then each term is the previous two terms' sum.
- A numeric palindrome reads the same forward and backward, such as 121.
- An Armstrong number equals the sum of each digit raised to the number of digits (153 = 1³ + 5³ + 3³).
- GCD is the greatest common divisor; for positive integers, LCM(a,b) = a // GCD(a,b) * b.

### Dry run: reverse 352

Start reverse=0, n=352. Digit 2: reverse=2, n=35. Digit 5: reverse=25, n=3. Digit 3: reverse=253, n=0. Final reverse is 253.

## 4. Five worked examples

### Example 1 — Factorial

```python
n = 5
result = 1
for value in range(2, n + 1):
    result *= value
print(result)
```
**Output:** `120`  
**Explanation:** Multiply integers 2, 3, 4 and 5. The initial value 1 handles n=0 and n=1.

### Example 2 — Prime number

```python
n = 29
if n < 2:
    is_prime = False
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1
print("Prime" if is_prime else "Not prime")
```
**Output:** `Prime`  
**Explanation:** Testing divisors only up to the square root is enough because a factor above the square root pairs with one below it.

### Example 3 — Fibonacci sequence

```python
count = 7
a, b = 0, 1
sequence = []
for _ in range(count):
    sequence.append(a)
    a, b = b, a + b
print(sequence)
```
**Output:** `[0, 1, 1, 2, 3, 5, 8]`  
**Explanation:** Multiple assignment updates the pair to the next two consecutive terms.

### Example 4 — Sum digits and reverse

```python
number = 5082
n = number
digit_sum = 0
reverse = 0
while n > 0:
    digit = n % 10
    digit_sum += digit
    reverse = reverse * 10 + digit
    n //= 10
print(digit_sum)
print(reverse)
```
**Output**
```text
15
2805
```
**Explanation:** Modulo extracts the last digit; floor division removes it.

### Example 5 — GCD and LCM

```python
a, b = 18, 24
x, y = a, b
while y:
    x, y = y, x % y
gcd = x
lcm = 0 if a == 0 or b == 0 else abs(a // gcd * b)
print(gcd)
print(lcm)
```
**Output**
```text
6
72
```
**Explanation:** Euclid's algorithm repeatedly replaces (x, y) with (y, x % y).

## 5. Five practice tasks with complete solutions

### Task 1 — Count digits, including zero

```python
def count_digits(n):
    return len(str(abs(n)))

print(count_digits(0))
print(count_digits(-9012))
```
**Output**
```text
1
4
```
**Explanation:** Zero has one digit, and the sign is not a digit.

### Task 2 — Numeric palindrome

```python
def is_palindrome(n):
    if n < 0:
        return False
    original = n
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10 + n % 10
        n //= 10
    return original == reversed_number

print(is_palindrome(1221))
print(is_palindrome(123))
```
**Output**
```text
True
False
```
**Explanation:** Compare the reversed integer with the original; this definition treats negative numbers as not palindromes.

### Task 3 — Armstrong number

```python
def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == n

print(is_armstrong(153))
print(is_armstrong(154))
```
**Output**
```text
True
False
```
**Explanation:** Each digit is raised to the total digit count.

### Task 4 — Find all primes up to a limit

```python
def primes_up_to(limit):
    result = []
    for n in range(2, limit + 1):
        prime = True
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            result.append(n)
    return result

print(primes_up_to(15))
```
**Output:** `[2, 3, 5, 7, 11, 13]`  
**Explanation:** Each candidate is tested for divisors up to its square root.

### Task 5 — GCD and LCM function

```python
from math import gcd

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)

print(gcd(21, 28))
print(lcm(21, 28))
```
**Output**
```text
7
84
```
**Explanation:** For application code, Python's standard-library `math.gcd` is reliable; the LCM formula avoids multiplying both full operands first.

## 6. Common mistakes and edge cases

- Prime numbers start at 2; 0 and 1 are not prime.
- Factorial is undefined for negative integers in this basic exercise.
- Zero has one digit; handle it deliberately.
- Negative signs should not be included when counting decimal digits.
- Reverse-as-integer drops leading zeros: reversing 120 yields 21, not 021.
- Floating-point values are not integers; validate the input domain.
- LCM is 0 if either operand is 0; handle this before dividing by GCD.
- Test values just below, at and above meaningful boundaries.

## 7. Interview questions and answers

**Q1. How do you check a prime efficiently?** Test divisors from 2 up to the square root, stopping as soon as a factor is found.

**Q2. Why does factorial start with 1?** One is the multiplicative identity; zero would make every product zero.

**Q3. Why use `n % 10` and `n // 10` for digits?** The first extracts the last digit and the second removes it.

**Q4. What is the GCD?** The greatest positive integer that divides both inputs (with conventions depending on zero/sign cases).

**Q5. How are Fibonacci terms generated?** Each new term is the sum of the previous two.

**Q6. What is an Armstrong number?** A non-negative integer equal to the sum of its digits each raised to the number of digits.

## 8. Real-world mini-project — Number Analysis Toolkit

Save as `number_toolkit.py`. It exposes testable functions and a small command-line menu.

```python
def analyze_number(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Enter an integer.")
    digits = str(abs(n))
    digit_sum = sum(int(d) for d in digits)
    is_palindrome = n >= 0 and digits == digits[::-1]
    return {
        "number": n,
        "digits": len(digits),
        "digit_sum": digit_sum,
        "is_even": n % 2 == 0,
        "is_palindrome": is_palindrome,
    }


def main():
    raw = input("Enter an integer: ").strip()
    try:
        number = int(raw)
    except ValueError:
        print("Invalid input: enter a whole number.")
        return

    result = analyze_number(number)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```

### Sample run

```text
Enter an integer: 1221
number: 1221
digits: 4
digit_sum: 6
is_even: False
is_palindrome: True
```

### Tests

Save as `test_number_toolkit.py`; run `python -m unittest -v`.

```python
import unittest
from number_toolkit import analyze_number


class TestNumberToolkit(unittest.TestCase):
    def test_normal_palindrome(self):
        self.assertTrue(analyze_number(1221)["is_palindrome"])

    def test_zero_boundary(self):
        result = analyze_number(0)
        self.assertEqual(result["digits"], 1)
        self.assertTrue(result["is_even"])

    def test_negative_number(self):
        result = analyze_number(-42)
        self.assertEqual(result["digit_sum"], 6)
        self.assertFalse(result["is_palindrome"])

    def test_odd_number(self):
        self.assertFalse(analyze_number(7)["is_even"])

    def test_non_integer_rejected(self):
        with self.assertRaises(TypeError):
            analyze_number(2.5)


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. Is 1 prime?
2. What is 0!?
3. How do you extract the final digit of 839?
4. What is the GCD of 18 and 24?
5. Is 153 an Armstrong number?

### Answer key
1. No.
2. 1.
3. `839 % 10 == 9`.
4. 6.
5. Yes: 1³ + 5³ + 3³ = 153.

### Independent challenge
Write a function that accepts a non-negative integer and returns its digits sorted ascending. Test 0, repeated digits, a large number, and a negative input.

## 10. Progress checklist

- [ ] I can explain prime, factorial, Fibonacci, palindrome, Armstrong, GCD and LCM.
- [ ] I ran all examples and tasks.
- [ ] Project unit tests pass.
- [ ] I solved the independent challenge and explained complexity.
