# Python Core Concepts — Beginner to Advanced

Separate from OOP and DSA. Each topic includes definition, explanation, examples, real-world use, where/when/how, tasks and interview Q&A.

AI assistance was used to organise this guide. Run the examples yourself and verify your understanding.

## How to study
1. Read the definition and explanation.
2. Type each example and predict the output.
3. Change inputs and test edge cases.
4. Complete tasks without looking at answers.
5. Explain the topic aloud as if in an interview.

# 1. Variables and data types
**Definition:** A variable is a name bound to an object. A data type describes the value and supported operations.
**Explanation:** Python is dynamically typed. Common types are int, float, str, bool, list, tuple, set, dict and NoneType.
**Real-world use:** A shop may represent a product name as text, quantity as an integer, and availability as a boolean.
**Where/when/how:** Choose a type based on required operations; use meaningful names.

Seven examples:
1. age = 23
2. price = 49.5
3. name = "Adil"
4. active = True
5. skills = ["Python", "SQL"]
6. point = (4, 7)
7. profile = {"name": "Adil", "active": True}

Tasks: Create product variables; print their types; convert "125" to an integer and add 25.

Interview Q&A:
1. Is Python statically or dynamically typed? Dynamically typed; a name can refer to objects of different types.
2. Is a variable an object? More precisely, a name refers to an object.
3. What does type(10) return? The int class.
4. What does input() return? A string.
5. What is None? A value commonly used to represent no result or missing value.
6. What happens in int("hello")? ValueError.
7. Why use meaningful names? To improve readability and maintenance.

# 2. Operators
**Definition:** Operators perform arithmetic, comparison, logical and membership operations.
**Real-world use:** Checkout totals, discount rules and checking cart membership.
**Where/when/how:** Pick the operator matching the requirement; use parentheses to clarify complex expressions.

Seven examples:
1. 5 + 2 gives 7.
2. 5 / 2 gives 2.5.
3. 5 // 2 gives 2.
4. 5 % 2 gives 1.
5. 2 ** 3 gives 8.
6. 10 >= 10 gives True.
7. "py" in "python" gives True.

Tasks: Check divisibility by 3 and 5; calculate remainder; test whether a username is allowed.
Interview Q&A:
1. = versus ==? Assignment versus equality comparison.
2. / versus //? True division versus floor division.
3. What does % do? Returns remainder.
4. What does ** do? Exponentiation.
5. What is precedence? Rules determining evaluation order.
6. What is short-circuiting? and/or can stop once the result is known.
7. Why parentheses? Clear grouping and fewer precedence mistakes.

# 3. Conditions
**Definition:** Conditions select which block executes based on an expression.
**Explanation:** if, elif and else are checked in order.
**Real-world use:** Grade assignment, access checks and discounts.
**Where/when/how:** List cases first, order overlapping conditions carefully and include a fallback.

Seven examples:
1. if age >= 18: print("Adult")
2. if number % 2 == 0: print("Even")
3. if score >= 90: grade = "A"
4. if not username: print("Required")
5. if item in cart: print("In cart")
6. if 0 <= score <= 100: print("Valid")
7. if role == "admin" and active: print("Allowed")

Tasks: Grade marks; check leap year; validate age.
Interview Q&A:
1. What is elif? An additional branch checked if previous branches fail.
2. Can a list be a condition? Yes; empty is falsy and non-empty is truthy.
3. Why does order matter? The first matching branch runs.
4. What is nesting? A condition inside another condition.
5. What does and mean? Both operands must be truthy for the result to be truthy.
6. What does or mean? The result is truthy if either operand is truthy.
7. How simplify complex conditions? Use clear guard clauses and helper functions.

# 4. Loops, counters and accumulators
**Definition:** Loops repeat work. A counter counts events; an accumulator builds a result.
**Real-world use:** Process transactions to calculate total revenue.
**Where/when/how:** Use for for iterable traversal; use while when repetition depends on a condition. Ensure while loops can terminate.

Seven examples:
1. for i in range(5): print(i)
2. for item in ["a", "b"]: print(item)
3. total = 0; add each number to total.
4. count = 0; increment when a condition matches.
5. n = 3; while n > 0: n -= 1
6. Use continue to skip a selected iteration.
7. Use break to exit a loop when a target is found.

Tasks: Multiplication table; sum evens to 100; count digits; generate Fibonacci.
Interview Q&A:
1. for versus while? Iterable iteration versus condition-controlled repetition.
2. What is an infinite loop? A loop that does not reach an exit condition.
3. What does range(1, 5) produce? 1, 2, 3, 4.
4. Counter versus accumulator? Count events versus build a combined value.
5. break versus continue? Exit loop versus skip current iteration.
6. Why initialise total to zero? Zero is the additive identity.
7. What is off-by-one? A boundary error often caused by endpoint confusion.

# 5. Strings
**Definition:** A string is an immutable sequence of Unicode characters.
**Real-world use:** Clean names, process logs and normalise text.
**Where/when/how:** Use strip for surrounding whitespace, lower for case-insensitive comparison, split to divide text, join to combine pieces.

Seven examples:
1. "python".upper() gives "PYTHON".
2. "  hi  ".strip() gives "hi".
3. "python"[0] gives "p".
4. "python"[1:4] gives "yth".
5. "a,b".split(",") gives ["a", "b"].
6. "-".join(["2026", "10", "29"]) gives "2026-10-29".
7. f"Hello, {name}" inserts a value.

Tasks: Reverse a string; count vowels; palindrome; count words.
Interview Q&A:
1. Are strings mutable? No.
2. What is slicing? Selecting a sequence range with an exclusive stop.
3. What does strip do? Removes surrounding whitespace by default.
4. What does split return? A list.
5. How join strings? separator.join(iterable).
6. How reverse a string? text[::-1].
7. Why f-strings? Readable interpolation.

# 6. Lists, tuples, sets and dictionaries
**Definition:** Built-in collection types store groups of values.
**Explanation:** Lists are ordered and mutable; tuples are immutable sequences; sets contain unique hashable values; dictionaries map hashable keys to values.
**Real-world use:** Task lists, unique tags and records looked up by ID.
**Where/when/how:** Choose based on ordering, mutation, uniqueness and lookup needs.

Seven examples:
1. items = [10, 20]; items.append(30)
2. items[0] reads the first element.
3. items[1:3] returns a slice.
4. point = (3, 4)
5. set([1, 1, 2]) removes duplicates.
6. counts = {"a": 2}; counts["a"] += 1
7. profile.get("city", "Unknown") supplies a default.

Tasks: Largest value; remove duplicates preserving order; word frequencies; merge dictionaries.
Interview Q&A:
1. List versus tuple? Mutable versus immutable sequence.
2. Why use a set? Unique values and average-case efficient membership.
3. Can a list be a dict key? No, lists are unhashable.
4. Missing dictionary key? Indexing raises KeyError; get can provide a default.
5. Does a set preserve duplicates? No.
6. What is a nested list? A list containing other lists.
7. What is a shallow copy? New outer collection that can share nested objects.

# 7. Functions
**Definition:** A function is a reusable unit of code that can accept inputs and return a result.
**Real-world use:** Reuse a tax calculation across checkout features.
**Where/when/how:** Make functions when logic has a clear responsibility, needs reuse or should be tested independently.

Seven examples:
1. def greet(): return "Hello"
2. def add(a, b): return a + b
3. def power(n, exponent=2): return n ** exponent
4. add(a=2, b=3) uses keyword arguments.
5. def total(*values): return sum(values)
6. def show(**details): return details
7. def is_even(n): return n % 2 == 0

Tasks: Factorial; prime check; validate a name; refactor repeated code.
Interview Q&A:
1. What is a function? Reusable code that can accept arguments and return a result.
2. return versus print? Return passes a result; print displays it.
3. Default parameter? A value used when the argument is omitted.
4. Keyword argument? Supplied by parameter name.
5. *args and **kwargs? Common conventions for collecting extra positional and keyword arguments.
6. What is scope? Where a name can be accessed.
7. Why avoid mutable defaults? The same object is reused; use None and create a fresh object inside.

# 8. Errors, exceptions and debugging
**Definition:** Exceptions represent abnormal runtime conditions; debugging finds and fixes defects.
**Real-world use:** Show helpful messages for invalid form input.
**Where/when/how:** Catch specific expected exceptions, inspect tracebacks, isolate a small reproduction and test fixes.

Seven examples:
1. int("abc") raises ValueError.
2. 10 / 0 raises ZeroDivisionError.
3. items[99] can raise IndexError.
4. record["missing"] raises KeyError.
5. Use try/except ValueError around parsing.
6. raise ValueError("age must be non-negative") validates input.
7. finally can perform cleanup.

Tasks: Safe numeric input; validate age; test missing keys; explain a real bug.
Interview Q&A:
1. What is an exception? An event that disrupts normal execution.
2. Why catch specific exceptions? To avoid hiding unrelated bugs.
3. What does finally do? Runs during normal completion or exception handling.
4. What is a traceback? A report of the call stack and exception location.
5. What is a logic error? Code runs but gives a wrong result.
6. What is validation? Checking input against expected rules.
7. How debug? Reproduce, inspect, isolate, fix and retest.

# 9. Files, modules and environments
**Definition:** Files persist data; modules organise reusable code; virtual environments isolate dependencies.
**Real-world use:** Save contacts to JSON so they remain after exit.
**Where/when/how:** Use with open for files, json for structured data, imports for reusable code and a virtual environment per project.

Seven examples:
1. Read text with open("notes.txt", "r", encoding="utf-8").
2. Write text with mode "w" (truncates existing content).
3. Append with mode "a".
4. import math.
5. from pathlib import Path.
6. json.loads(text) parses JSON text.
7. python -m venv .venv creates a virtual environment.

Tasks: Save/load names using JSON; handle missing files; split a project into modules; document setup.
Interview Q&A:
1. Why use with open? Reliable file closure.
2. What does mode w do? Opens for writing and truncates existing content.
3. What is a module? A Python file that can be imported.
4. What is a package? A way to organise modules under a package namespace.
5. Why virtual environments? Isolate dependencies.
6. What is JSON? A text format for structured data.
7. Why avoid hard-coded absolute paths? They reduce portability.

# 10. Advanced core Python
## Iterators and generators
**Definition:** An iterator supplies values one at a time; a generator is a convenient iterator commonly created with yield.
**Use:** Process large files and streams without holding every result in memory.
Seven examples: iter([1,2,3]); next(iter([10,20])); generator using yield; squares=(n*n for n in range(5)); next() requests a value; exhausted iterators raise StopIteration; create a new generator to iterate again.
Interview Q&A: Generator vs list? Generator yields lazily. What does yield do? Produces a value and suspends execution. Lazy evaluation? Compute on demand. Why generators? Lower memory for streams. Iterable? Can provide an iterator. Iterator? Supplies successive values. Can exhausted generators restart? No, create a new one.

## Decorators and context managers
**Definition:** A decorator wraps or transforms callable behaviour; a context manager manages setup and cleanup around a block.
**Use:** Logging, timing and resource handling.
Seven examples: @staticmethod; @classmethod; a wrapper decorator; @property; with open; a context manager for a lock; functools.wraps preserves metadata.
Interview Q&A: Decorator? Callable that wraps/transforms another callable. Why use it? Reuse cross-cutting behaviour. @property? Method accessed attribute-style. classmethod receives? cls. staticmethod receives? No automatic instance/class argument. Context manager? Reliable setup/cleanup. functools.wraps? Preserves metadata.

## Type hints, tests and code quality
**Definition:** Type hints document expected types; tests check behaviour. Type hints are not enforced at runtime by default.
Seven examples: annotate function inputs; descriptive names; docstrings; separate I/O from logic; test expected output; test edge cases; record focused Git commits.
Interview Q&A: Are hints runtime enforcement? No, not by default. Unit test? Tests a small unit of behaviour. Regression test? Checks old behaviour after a change. Why docstrings? Explain public functions. PEP 8? Python style guide. Version control? Tracks changes. Code review? Review correctness, clarity, maintainability and risks.

## Final projects
1. Build a menu-driven contact manager.
2. Validate inputs.
3. Save/load JSON.
4. Split into modules.
5. Add unit tests.
6. Document setup and usage.
7. Explain design, limitations and tests in an interview.
