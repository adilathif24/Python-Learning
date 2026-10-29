# Python Core Concepts: Beginner to Advanced


> **Professional interview preparation:** For structured syntax, complete code examples, interview-ready explanations, seven solved interview Q&As and five practice tasks with solutions, also use the [Professional Interview Workbook](core/Professional-Interview-Workbook.md).

This is the Python-language track. OOP and DSA have separate guides. Each topic includes an interview-ready definition, explanation, use cases, solved examples, tasks, and answers.

## How to study
Read the definition aloud, type the code, predict output, run it, test edge cases, then explain why the solution works. Complexity figures are typical and assume standard Python data structures.

## 1. Variables, types, input and conversion
**Interview definition:** A variable is a name bound to an object. A type determines the operations and behaviour supported by that object. Python is dynamically typed.
**Use / where / when:** Store program state; choose types according to the data and required operations. `input()` returns a string, so convert validated numeric input before arithmetic.
**Real-world example:** A shopping cart stores product names, quantities, prices and availability.
### 7 solved examples
1. `age = 23; print(type(age).__name__)` → `int`.
2. `price = 49.5; print(type(price).__name__)` → `float`.
3. `name = 'Adil'; print(name.upper())` → `ADIL`.
4. `active = True; print(not active)` → `False`.
5. `quantity = int('12'); print(quantity + 3)` → `15`.
6. `value = None; print(value is None)` → `True`.
7. `product = {'name': 'Pen', 'price': 10}; print(product['price'])` → `10`.
### 5 practice questions with answers
1. Convert `'45'` to an integer and add 5. **Answer:** `int('45') + 5` → `50`.
2. What type does `input()` return? **Answer:** `str`.
3. What is `None` used for? **Answer:** To represent absence of a value or no result.
4. Is `x = 2` the same as `x == 2`? **Answer:** No; assignment versus comparison.
5. What happens in `int('abc')`? **Answer:** `ValueError`; validate or catch expected conversion errors.

## 2. Operators and conditions
**Definition:** Operators calculate values or compare them; conditions choose which branch executes.
**Use / where / when:** Use arithmetic for calculations, comparison for rules, and `if/elif/else` for decisions. Parentheses improve readability.
**Real-world example:** A checkout applies a discount when the subtotal reaches a threshold.
### 7 solved examples
1. `print(7 + 3)` → `10`.
2. `print(7 / 2)` → `3.5`.
3. `print(7 // 2)` → `3`.
4. `print(7 % 2)` → `1`.
5. `print(2 ** 4)` → `16`.
6. `n = 8; print('even' if n % 2 == 0 else 'odd')` → `even`.
7. `score = 82; print('pass' if score >= 40 else 'fail')` → `pass`.
### 5 practice questions with answers
1. Check whether 15 is divisible by 3 and 5. **Answer:** `15 % 3 == 0 and 15 % 5 == 0` → `True`.
2. What does `%` return? **Answer:** The remainder.
3. What is `//`? **Answer:** Floor division.
4. Write a positive/negative/zero check. **Answer:** `if n > 0: ... elif n < 0: ... else: ...`.
5. Why does branch order matter? **Answer:** The first matching branch is executed; broad conditions can hide narrower ones.

## 3. Loops and ranges
**Definition:** A loop repeats a block. `for` iterates over an iterable; `while` repeats while a condition remains true.
**Use / where / when:** Use `for` to process items or a known sequence; use `while` when stopping depends on a condition. Make sure loops progress toward termination.
**Real-world example:** Process each transaction to calculate total sales.
### 7 solved examples
1. `for i in range(1, 4): print(i)` → 1, 2, 3.
2. `print(sum([2, 3, 4]))` → 9.
3. `total = 0; for n in [2, 3, 4]: total += n; print(total)` → 9.
4. `count = 0; for n in [1, 2, 3, 4]: count += n % 2 == 0; print(count)` → 2.
5. `n = 3; while n > 0: print(n); n -= 1` → 3, 2, 1.
6. `for n in range(5):
    if n == 2: continue
    print(n)` → prints 0, 1, 3, 4.
7. `for n in range(10):
    if n == 3: break
    print(n)` → prints 0, 1, 2.
### 5 practice questions with answers
1. Sum 1 through 10. **Answer:** `sum(range(1, 11))` → `55`.
2. Print a 5-times table. **Answer:** `for i in range(1, 11): print(5, '*', i, '=', 5*i)`.
3. Count digits in 1234 using a loop. **Answer:** repeatedly use `n //= 10`, incrementing a counter; result `4` (handle zero separately).
4. `range(2, 6)` produces what? **Answer:** 2, 3, 4, 5.
5. `break` versus `continue`? **Answer:** Exit the loop versus skip the current iteration.

## 4. Strings
**Definition:** A string is an immutable sequence of Unicode characters.
**Use / where / when:** Use strings for text, identifiers and messages. Normalise case/whitespace only when the problem's rules require it.
**Real-world example:** Clean a form field before comparing usernames or parsing a log line.
### 7 solved examples
1. `s = 'python'; print(s[0])` → `p`.
2. `print(s[1:4])` → `yth`.
3. `print(s[::-1])` → `nohtyp`.
4. `print('  hi '.strip())` → `hi`.
5. `print('a,b,c'.split(','))` → `['a', 'b', 'c']`.
6. `print('-'.join(['2026', '10', '29']))` → `2026-10-29`.
7. `word = 'level'; print(word == word[::-1])` → `True`.
### 5 practice questions with answers
1. Count vowels in `hello`. **Answer:** `sum(ch in 'aeiou' for ch in 'hello')` → `2`.
2. Reverse `python`. **Answer:** `'python'[::-1]` → `nohtyp`.
3. Check a palindrome ignoring case/spaces. **Answer:** `t = ''.join(c.lower() for c in s if c.isalnum()); t == t[::-1]`.
4. What does `strip()` do? **Answer:** Removes leading/trailing whitespace by default.
5. Why can't a string character be assigned by index? **Answer:** Strings are immutable; create a new string instead.

## 5. Lists
**Definition:** A list is an ordered, mutable sequence that can hold references to objects of different types.
**Use / where / when:** Use for ordered collections that may change. Index access is O(1), searching O(n), and inserting at the front O(n) in typical Python lists.
**Real-world example:** Keep a user's ordered tasks or a set of daily readings.
### 7 solved examples
1. `a = [3, 1, 2]; print(a[0])` → `3`.
2. `a.append(4); print(a)` → `[3, 1, 2, 4]`.
3. `print(a[-1])` → `4`.
4. `print(a[1:3])` → `[1, 2]`.
5. `a.remove(1); print(a)` → `[3, 2, 4]`.
6. `print(sorted([4, 1, 3]))` → `[1, 3, 4]`.
7. `nums = [1, 2, 3]; print([n*n for n in nums])` → `[1, 4, 9]`.
### 5 practice questions with answers
1. Find the largest without `max()`. **Answer:** initialise `best = nums[0]`, scan the rest and update when greater; check empty input.
2. Remove duplicates while preserving order. **Answer:** `list(dict.fromkeys(items))` for hashable values.
3. Reverse a list in place. **Answer:** `items.reverse()`.
4. `append(x)` versus `extend(xs)`? **Answer:** append adds one object; extend adds each element from an iterable.
5. What is a list slice? **Answer:** A new list containing a selected range of elements.

## 6. Tuples
**Definition:** A tuple is an ordered sequence that cannot be structurally changed after creation.
**Use / where / when:** Use for fixed groups such as coordinates or returning multiple related values. A tuple is not deeply immutable if it contains mutable objects.
**Real-world example:** Store an (x, y) coordinate.
### 7 solved examples
1. `point = (2, 5)`.
2. `print(point[0])` → `2`.
3. `x, y = point; print(x, y)` → `2 5`.
4. `single = (4,)` — comma makes a one-item tuple.
5. `print((1, 2) + (3,))` → `(1, 2, 3)`.
6. `print((1, 2) * 2)` → `(1, 2, 1, 2)`.
7. `person = ('Adil', 23); name, age = person` — unpack values.
### 5 practice questions with answers
1. How make a one-item tuple? **Answer:** `(5,)`.
2. Can a tuple be reassigned by index? **Answer:** No.
3. Tuple versus list? **Answer:** Tuple is immutable; list is mutable.
4. Can a tuple contain a list? **Answer:** Yes, but the list inside can still mutate.
5. What is unpacking? **Answer:** Assigning iterable elements to multiple variables, e.g. `a, b = (1, 2)`.

## 7. Sets
**Definition:** A set is an unordered collection of unique hashable elements.
**Use / where / when:** Use for uniqueness, membership checks, intersections and differences. Do not rely on set iteration order.
**Real-world example:** Find unique visitor IDs or shared skills between candidates.
### 7 solved examples
1. `print(set([1, 1, 2]))` → `{1, 2}` (display order may vary).
2. `print(2 in {1, 2, 3})` → `True`.
3. `print({1, 2} | {2, 3})` → `{1, 2, 3}`.
4. `print({1, 2} & {2, 3})` → `{2}`.
5. `print({1, 2} - {2, 3})` → `{1}`.
6. `s = {1, 2}; s.add(3)` adds 3.
7. `print(len(set('banana')))` → `3`.
### 5 practice questions with answers
1. Remove duplicates from a list (order not required). **Answer:** `list(set(items))`.
2. Find common values. **Answer:** `set(a) & set(b)`.
3. Why can't a list be a set element? **Answer:** Lists are unhashable.
4. `remove` versus `discard`? **Answer:** `remove` raises KeyError if absent; `discard` does not.
5. How preserve order while deduplicating? **Answer:** Track a `seen` set and append unseen items to a result list.

## 8. Dictionaries
**Definition:** A dictionary maps hashable keys to values.
**Use / where / when:** Use when values need to be retrieved by a key or when counting/grouping. Average-case lookup is O(1).
**Real-world example:** Map product IDs to product details or count log events.
### 7 solved examples
1. `user = {'name': 'Adil', 'age': 23}`.
2. `print(user['name'])` → `Adil`.
3. `print(user.get('city', 'Unknown'))` → `Unknown`.
4. `user['age'] = 24` updates a value.
5. `user['active'] = True` inserts a key.
6. `for key, value in user.items(): print(key, value)` iterates pairs.
7. `counts = {};` then for each `ch` use `counts[ch] = counts.get(ch, 0) + 1` to count frequencies.
### 5 practice questions with answers
1. Count words in a list. **Answer:** increment `counts[word] = counts.get(word, 0) + 1`.
2. What happens on a missing key with `d[key]`? **Answer:** `KeyError`.
3. What does `get()` provide? **Answer:** Optional default for missing keys.
4. Can dictionary keys be mutable lists? **Answer:** No; keys must be hashable.
5. How combine dictionaries? **Answer:** `merged = {**a, **b}`; duplicate keys from `b` override `a`.

## 9. Functions
**Definition:** A function is a reusable block that can accept arguments and return a result.
**Use / where / when:** Use functions to remove repetition, isolate logic and make code testable. Prefer one clear responsibility per function.
**Real-world example:** Reuse a shipping-cost calculation across checkout screens.
### 7 solved examples
1. `def greet(): return 'Hello'`.
2. `def add(a, b): return a + b`.
3. `def square(n): return n*n`.
4. `def power(n, exp=2): return n**exp`.
5. `def is_even(n): return n % 2 == 0`.
6. `def total(*nums): return sum(nums)`.
7. `def describe(**data): return data`.
### 5 practice questions with answers
1. Write factorial. **Answer:** `def fact(n): return 1 if n <= 1 else n * fact(n-1)` after validating `n >= 0`.
2. `return` versus `print`? **Answer:** return sends a value to the caller; print displays text.
3. What is a parameter? **Answer:** A named input in a function definition.
4. What are `*args`? **Answer:** Collect extra positional arguments into a tuple.
5. Why avoid `def f(items=[])`? **Answer:** The same mutable default is reused; use `None` then create a new list.

## 10. Comprehensions, modules and files
**Definition:** Comprehensions build collections concisely; modules organise reusable code; file I/O persists information.
**Use / where / when:** Use comprehensions for clear transformations/filtering, modules to separate responsibilities, and context managers for resource-safe file access.
**Real-world example:** Filter active users and save a report to a file.
### 7 solved examples
1. `[n*n for n in range(5)]` → squares.
2. `[n for n in range(10) if n % 2 == 0]` → evens.
3. `{n: n*n for n in range(3)}` → mapping of numbers to squares.
4. `{n % 3 for n in range(10)}` → unique remainders.
5. `import math; print(math.sqrt(25))` → `5.0`.
6. `with open('notes.txt', 'w', encoding='utf-8') as f: f.write('Hello')` writes text.
7. `with open('notes.txt', encoding='utf-8') as f: text = f.read()` reads text.
### 5 practice questions with answers
1. Why use `with open`? **Answer:** It reliably closes the file.
2. What does mode `w` do? **Answer:** Opens for writing and truncates existing content.
3. What is a module? **Answer:** A Python file that can be imported.
4. Why use a virtual environment? **Answer:** To isolate project dependencies.
5. When is a comprehension less suitable? **Answer:** When logic is complex or nested enough to reduce readability.

## 11. Exceptions and debugging
**Definition:** Exceptions represent execution-time failures; debugging identifies and fixes defects.
**Use / where / when:** Catch specific expected exceptions at boundaries such as parsing input or reading files. Do not hide unrelated bugs with a broad silent catch.
**Real-world example:** Show a helpful message if a user types text into an age field.
### 7 solved examples
1. `int('x')` raises ValueError.
2. `10 / 0` raises ZeroDivisionError.
3. `try: age = int('23')` succeeds.
4. Catch `ValueError` around `int(user_input)`.
5. `raise ValueError('age must be non-negative')` rejects invalid data.
6. `finally` runs for cleanup whether an exception occurred or not.
7. A traceback shows the call path and error location.
### 5 practice questions with answers
1. Syntax vs runtime error? **Answer:** Invalid grammar vs exception during execution.
2. What is a logic error? **Answer:** Code runs but produces an incorrect result.
3. Why catch specific exceptions? **Answer:** To handle expected failures without masking unrelated bugs.
4. What does `finally` do? **Answer:** Executes cleanup code on normal or exceptional exit.
5. Debugging steps? **Answer:** Reproduce, inspect, isolate, fix, then add a regression test.

## 12. Iterators, generators and advanced core Python
**Definition:** An iterable can provide an iterator; an iterator returns values one at a time; a generator is a convenient iterator often created with `yield`.
**Use / where / when:** Use generators for streams or large datasets when lazy iteration saves memory. Use type hints and tests to document and verify interfaces.
### 7 solved examples
1. `iter([1, 2])` creates an iterator.
2. `next(iter([10, 20]))` → `10`.
3. `def nums(): yield 1; yield 2` creates a generator function.
4. `(n*n for n in range(4))` is a generator expression.
5. `def add(a: int, b: int) -> int: return a + b` documents types.
6. `@property` lets a method be accessed attribute-style.
7. A decorator can wrap a function to add logging or timing behaviour.
### 5 practice questions with answers
1. List vs generator? **Answer:** A list stores all values; a generator yields values lazily.
2. What does `yield` do? **Answer:** Produces a value and suspends generator execution.
3. Are type hints enforced at runtime automatically? **Answer:** No, not by Python itself.
4. Why use tests? **Answer:** To verify expected behaviour and catch regressions.
5. What does `functools.wraps` help with? **Answer:** Preserving wrapped function metadata such as name and docstring.

## Core Python final project
Build a command-line contact manager with functions, lists/dictionaries, input validation, JSON persistence, modules, and unit tests. Document setup, examples, limitations and design decisions in a README.