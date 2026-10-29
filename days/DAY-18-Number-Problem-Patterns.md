# Day 18 — Number Problem Patterns

**Status:** Full study pack. Demonstrate reasoning on boundaries and run tests before marking mastery.

## 1. Definition
Number-pattern problems apply digit extraction, accumulators, divisibility, loops and mathematical relationships. Typical interview patterns include reversing digits, digit sums, palindromes, Armstrong numbers, GCD and LCM.

## 2. Why / where / when
These exercises develop algorithmic reasoning and careful edge-case handling. Use `% 10` to extract a last decimal digit and `// 10` to remove it. For production code, standard-library functions may be safer and clearer; implement algorithms yourself to learn logic or meet a specific constraint.

## 3. Rules and dry run
Digit extraction:
```python
digit = n % 10
n //= 10
```
For 482, digits appear as 2, then 8, then 4. To reverse, use `reverse = reverse * 10 + digit`. Handle zero and negative values explicitly.

## 4. Five worked examples
### Example 1 — Digit sum
```python
n = 583
total = 0
while n:
    total += n % 10
    n //= 10
print(total)
```
Output: `16`. Sum 3 + 8 + 5.

### Example 2 — Reverse a number
```python
n = 420
reverse = 0
while n:
    reverse = reverse * 10 + n % 10
    n //= 10
print(reverse)
```
Output: `24`. Leading zeroes of the reversed integer are not retained.

### Example 3 — Palindrome
```python
def is_palindrome(n):
    return n >= 0 and str(n) == str(n)[::-1]
print(is_palindrome(1331))
```
Output: `True`. String reversal gives a concise numeric palindrome check.

### Example 4 — Armstrong number
```python
n = 370
digits = str(n)
print(sum(int(d) ** len(digits) for d in digits) == n)
```
Output: `True`. 3³ + 7³ + 0³ = 370.

### Example 5 — GCD and LCM
```python
from math import gcd
a, b = 12, 18
g = gcd(a, b)
l = 0 if not a or not b else abs(a // g * b)
print(g, l)
```
Output: `6 36`. LCM uses the GCD relation and explicitly handles zero.

## 5. Five tasks with solutions
### Task 1 — Count digits including zero
```python
def count_digits(n): return len(str(abs(n)))
print(count_digits(0), count_digits(-120))
```
Output: `1 3`. Zero still has one digit.

### Task 2 — Sum only even digits
```python
n = 48271
total = sum(int(d) for d in str(abs(n)) if int(d) % 2 == 0)
print(total)
```
Output: `14`. Even digits are 4, 8 and 2.

### Task 3 — Check perfect square
```python
from math import isqrt
n = 144
root = isqrt(n)
print(n >= 0 and root * root == n)
```
Output: `True`. Integer square root avoids floating rounding.

### Task 4 — Generate Fibonacci
```python
def fibonacci(count):
    if count < 0: raise ValueError("count cannot be negative")
    a, b, result = 0, 1, []
    for _ in range(count):
        result.append(a); a, b = b, a+b
    return result
print(fibonacci(5))
```
Output: `[0, 1, 1, 2, 3]`. The count controls the number of terms.

### Task 5 — LCM with zero
```python
from math import gcd
def lcm(a,b):
    return 0 if a == 0 or b == 0 else abs(a // gcd(a,b) * b)
print(lcm(0, 9), lcm(4, 6))
```
Output: `0 12`. Zero is a special case.

## 6. Common mistakes
- 0 and 1 are not prime.
- Factorial is not defined for negative integers in the basic definition.
- Reverse-as-integer drops leading zeros.
- Avoid dividing by a GCD before checking whether both inputs are zero.
- Prefer integer square roots for exact square checks.
- Test 0, negative values, single digits and large integers.

## 7. Interview questions
1. Why use modulo 10? **Extract the last decimal digit.**
2. Why divide with // 10? **Remove last digit.**
3. Define Armstrong number. **Digit powers summed using the number of digits equal the number.**
4. Why test factors only up to sqrt(n)? **Factors pair, so a larger factor implies a smaller counterpart.**
5. How calculate LCM? **For nonzero integers, abs(a // gcd(a,b) * b).**

## 8. Project — Number Report
Save `number_report.py`.
```python
from math import isqrt

def number_report(n):
    if not isinstance(n, int) or isinstance(n, bool): raise TypeError("integer required")
    text = str(abs(n))
    digit_sum = sum(int(ch) for ch in text)
    reverse = int(text[::-1]) * (-1 if n < 0 else 1)
    root = isqrt(n) if n >= 0 else None
    return {"digits":len(text), "digit_sum":digit_sum, "reverse":reverse,
            "even":n%2==0, "perfect_square":root is not None and root*root==n}

def main():
    try: n = int(input("Integer: ").strip())
    except ValueError:
        print("Enter a valid integer"); return
    for key, value in number_report(n).items(): print(f"{key}: {value}")

if __name__ == "__main__": main()
```
Sample input `144` reports 3 digits, digit sum 9, reverse 441, even True, perfect square True.

### Tests — `test_number_report.py`
```python
import unittest
from number_report import number_report

class ReportTests(unittest.TestCase):
    def test_zero(self): self.assertEqual(number_report(0)["digits"],1)
    def test_square(self): self.assertTrue(number_report(144)["perfect_square"])
    def test_negative(self): self.assertFalse(number_report(-4)["perfect_square"])
    def test_reverse(self): self.assertEqual(number_report(120)["reverse"],21)
    def test_type(self):
        with self.assertRaises(TypeError): number_report(2.5)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. How handle zero digit count? **Count it as one digit.**
2. What is sum of digits of 583? **16.**
3. Is 370 Armstrong? **Yes.**
4. What is gcd(12,18)? **6.**
5. What is lcm(4,6)? **12.**
**Challenge:** Make the report show whether a number is prime, and add tests for 1, 2, 9, and a negative input.

## 10. Completion
- [ ] I solved tasks independently.
- [ ] Project tests pass.
- [ ] I completed the prime-check challenge.
