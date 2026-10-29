# Python Core Concepts — Beginner to Advanced

Separate track: Python language fundamentals. OOP and DSA have their own guides.

Every topic includes definition, explanation, real-world example, when/where/how to use it, seven examples or Q&A items, practice tasks and interview questions with answers. The seven items are a starting set; practise additional variations independently.

## Study method
1. Read the definition and why the concept exists.
2. Type each example and predict the output before running it.
3. Dry-run variable changes on paper.
4. Test normal, empty, boundary and invalid inputs.
5. Complete the tasks without looking at the examples.
6. Explain the concept in your own words as if speaking to an interviewer.

## 1. Variables and data types
**Definition:** A variable name refers to an object. A type determines the values and operations supported by that object.
**Explanation:** Python is dynamically typed. Common types are int, float, str, bool, list, tuple, set, dict and NoneType.
**Real-world example:** An order uses a string for product name, integer for quantity, number for price and boolean for availability.
**Where/when/how:** Choose types based on the data and operations; use meaningful names and validate external input.
### Seven examples
1. age = 23 — integer.
2. price = 49.5 — float.
3. name = 'Adil' — string.
4. active = True — boolean.
5. skills = ['Python', 'SQL'] — list.
6. point = (4, 7) — tuple.
7. profile = {'name': 'Adil'} — dictionary.
### Tasks
- Create variables for a product, quantity, price and stock status.
- Print values and their types.
- Convert the string '125' to int and add 25.
### Interview Q&A
1. **What is dynamic typing?** Names can refer to objects of different types without a type declaration.
2. **Is a variable an object?** A name refers to an object.
3. **What does input() return?** A string.
4. **What is None?** A singleton commonly used to represent no value.
5. **What happens in int('hello')?** ValueError is raised.
6. **Why meaningful names?** They communicate intent and reduce mistakes.
7. **How inspect a type?** Use type(value).

## 2. Operators and expressions
**Definition:** Operators perform arithmetic, comparison, logical, identity or membership operations.
**Explanation:** Arithmetic: + - * / // % **. Comparisons: == != < > <= >=. Logic: and, or, not. Membership: in, not in.
**Real-world example:** Calculate a checkout total and check whether a discount threshold is met.
**Where/when/how:** Choose the operator matching the requirement; use parentheses to make complicated expressions clear.
### Seven examples
1. 5 + 2 gives 7.
2. 5 / 2 gives 2.5.
3. 5 // 2 gives 2.
4. 5 % 2 gives 1.
5. 2 ** 3 gives 8.
6. 10 >= 10 gives True.
7. 'py' in 'python' gives True.
### Tasks
- Check divisibility by both 3 and 5.
- Calculate the remainder of 47 divided by 6.
- Check if a username belongs to an allowed list.
### Interview Q&A
1. **= versus ==?** Assignment versus equality comparison.
2. **/ versus //?** True division versus floor division.
3. **What does % do?** Returns the remainder.
4. **What does ** do?** Exponentiation.
5. **What is precedence?** Rules for evaluation order.
6. **What is short-circuiting?** and/or may stop once the result is known.
7. **Why parentheses?** To make grouping explicit.

## 3. Input and output; type conversion
**Definition:** Input receives data; output presents results; conversion changes a value from one type to another where valid.
**Explanation:** input() returns text. int(), float(), str() and bool() have different conversion rules; invalid numeric text can raise ValueError.
**Real-world example:** A form receives quantity as text, validates it and converts it to an integer before calculating the bill.
**Where/when/how:** Validate input at system boundaries and handle invalid conversions with a clear message.
### Seven examples
1. name = input('Name: ')
2. age = int(input('Age: '))
3. price = float('12.50')
4. str(100) gives '100'.
5. int('42') gives 42.
6. int('4.2') raises ValueError.
7. print('Total:', 10 + 20).
### Tasks
- Read two numbers and print their sum.
- Reject non-numeric input gracefully.
- Calculate total price from quantity and unit price.
### Interview Q&A
1. **Why convert input?** input() returns str.
2. **int('3.8') result?** ValueError; convert through float if that is the intended rule.
3. **What is casting?** Converting a value to another type.
4. **What is ValueError?** A value has the right general type but is invalid for the operation.
5. **Why validate input?** External data may be missing or malformed.
6. **Does bool('False') return False?** No; any non-empty string is truthy.
7. **How avoid crashing on bad input?** Catch expected conversion exceptions and ask again or report an error.

## 4. Conditions
**Definition:** Conditional statements choose which block executes based on a condition.
**Explanation:** if, elif and else are checked in order; the first matching branch executes.
**Real-world example:** A shop applies different discounts based on order value.
**Where/when/how:** List decision cases, order overlapping conditions carefully, and include a fallback when needed.
### Seven examples
1. if age >= 18: print('Adult').
2. if n % 2 == 0: print('Even').
3. if score >= 90: grade = 'A'.
4. if not username: print('Required').
5. if item in cart: print('In cart').
6. if 0 <= score <= 100: print('Valid').
7. if role == 'admin' and active: print('Allowed').
### Tasks
- Classify marks into grades.
- Check a leap year.
- Validate age from 0 through 120.
### Interview Q&A
1. **What is elif?** Another condition checked after earlier branches fail.
2. **Can a list be a condition?** Yes; empty is falsy, non-empty is truthy.
3. **Why does order matter?** Earlier branches can prevent later ones from running.
4. **What is nesting?** A condition inside another condition.
5. **What does and mean?** Both operands must be truthy for the combined result to be truthy.
6. **What does or mean?** The combined result is truthy if an operand is truthy.
7. **How simplify deep conditions?** Use clear guard clauses and helper functions.

## 5. Loops, counters and accumulators
**Definition:** Loops repeat work. A counter tracks occurrences; an accumulator combines values into a result.
**Explanation:** for iterates over an iterable; while repeats while its condition remains true. range stop is exclusive. break exits; continue skips to the next iteration.
**Real-world example:** Process every transaction to calculate total sales.
**Where/when/how:** Use for to iterate collections and while for condition-controlled repetition. Ensure a while loop can terminate.
### Seven examples
1. for i in range(5): print(i) prints 0 through 4.
2. for item in ['a', 'b']: print(item).
3. total = 0; add each value to total.
4. count = 0; increment when a condition matches.
5. n = 3; while n > 0: n -= 1.
6. continue skips the current iteration.
7. break exits the current loop.
### Tasks
- Print a multiplication table.
- Sum even numbers from 1 to 100.
- Count digits in an integer.
- Generate the first n Fibonacci numbers.
### Interview Q&A
1. **for versus while?** Iterable-driven versus condition-driven repetition.
2. **Infinite loop?** A loop that never reaches its exit condition.
3. **What is range(1, 5)?** 1, 2, 3, 4.
4. **Counter versus accumulator?** Count events versus build a result.
5. **break versus continue?** Exit loop versus skip one iteration.
6. **Why total = 0?** Zero is the additive identity.
7. **Off-by-one error?** A boundary error caused by incorrect index or range limits.

## 6. Strings
**Definition:** A string is an immutable sequence of Unicode characters.
**Explanation:** Strings support indexing, slicing, searching, splitting, joining and formatting. Operations create new strings rather than modifying the original.
**Real-world example:** Normalise a username or parse a line from an application log.
**Where/when/how:** Decide whether case, spaces, punctuation and Unicode matter before cleaning or comparing text.
### Seven examples
1. 'python'.upper() gives 'PYTHON'.
2. '  hi  '.strip() gives 'hi'.
3. 'python'[0] gives 'p'.
4. 'python'[1:4] gives 'yth'.
5. 'a,b'.split(',') gives ['a', 'b'].
6. '-'.join(['2026', '10', '29']) gives '2026-10-29'.
7. f'Hello, {name}' inserts name.
### Tasks
- Reverse a string.
- Count vowels while ignoring case.
- Check a palindrome ignoring spaces and punctuation.
- Count words in a sentence.
### Interview Q&A
1. **Are strings mutable?** No.
2. **What is slicing?** Selecting a range; the stop index is excluded.
3. **What does strip do?** Removes leading/trailing whitespace by default.
4. **What does split return?** A list.
5. **How join strings?** separator.join(iterable_of_strings).
6. **How reverse a string?** text[::-1].
7. **Why use f-strings?** Readable value interpolation.

## 7. Lists
**Definition:** A list is an ordered, mutable sequence.
**Explanation:** Lists support indexing, slicing, append, extend, insert, remove, pop, sorting and iteration. Index access is O(1); searching and insertion near the front are O(n).
**Real-world example:** Store ordered tasks, scores or shopping-cart items.
**Where/when/how:** Use a list when order matters and elements may be added, removed or updated.
### Seven examples
1. values = [10, 20, 30].
2. values.append(40) adds one value.
3. values.extend([50, 60]) adds many values.
4. values.pop() removes and returns the last item.
5. values[0] reads the first item.
6. values[1:3] returns a slice.
7. sorted(values) returns a sorted copy; values.sort() changes the list.
### Tasks
- Find largest and second-largest values.
- Remove duplicates while preserving order.
- Move all zeroes to the end.
- Rotate a list by k positions.
### Interview Q&A
1. **Are lists mutable?** Yes.
2. **append versus extend?** Append one object; extend with elements from an iterable.
3. **pop versus remove?** pop uses an index and returns the removed value; remove deletes the first matching value.
4. **What is slicing?** Creating a subsequence using start, stop and optional step.
5. **Why is front insertion O(n)?** Existing elements usually need to shift.
6. **sort versus sorted?** In-place mutation versus a new sorted list.
7. **How copy a list?** list.copy() or list(list_name), both shallow copies.

## 8. Tuples
**Definition:** A tuple is an ordered immutable sequence.
**Explanation:** Tuples suit fixed collections; elements can still refer to mutable objects.
**Real-world example:** Represent a coordinate, RGB value or fixed return record.
**Where/when/how:** Use a tuple when the sequence should not be structurally changed.
### Seven examples
1. point = (3, 4).
2. one = (5,) — comma creates a one-item tuple.
3. x, y = point — unpacking.
4. point[0] reads first item.
5. len(point) returns length.
6. (1, 2) + (3,) concatenates tuples.
7. Use tuple(values) to convert an iterable.
### Tasks
- Return both minimum and maximum from a function.
- Swap two variables with tuple unpacking.
- Explain when a tuple containing a list is not deeply immutable.
### Interview Q&A
1. **Tuple versus list?** Tuple is immutable; list is mutable.
2. **Why the comma in (5,)?** It defines a one-element tuple.
3. **Can tuples be dictionary keys?** Only if all their elements are hashable.
4. **Can a tuple contain a list?** Yes, but the list itself can still change.
5. **What is unpacking?** Assigning iterable elements to multiple names.
6. **Can tuple items be reassigned?** No.
7. **When choose a tuple?** For a fixed ordered record or sequence.

## 9. Sets
**Definition:** A set stores unique hashable elements.
**Explanation:** Sets support membership and operations such as union, intersection and difference. They do not provide index-based access.
**Real-world example:** Track unique visitors, tags or IDs already processed.
**Where/when/how:** Use sets for uniqueness and repeated membership tests; do not rely on positional order.
### Seven examples
1. set([1, 1, 2]) gives {1, 2}.
2. {1, 2} | {2, 3} gives union {1, 2, 3}.
3. {1, 2} & {2, 3} gives {2}.
4. {1, 2} - {2, 3} gives {1}.
5. 2 in {1, 2} is True.
6. values.add(4) inserts a value.
7. values.discard(99) does not fail if 99 is absent.
### Tasks
- Find common values between two lists.
- Remove duplicates from a list.
- Find values present in one list but not another.
### Interview Q&A
1. **Can a set contain duplicates?** No.
2. **Can a set contain a list?** No; list is unhashable.
3. **What is union?** Elements from either set.
4. **What is intersection?** Elements common to both.
5. **discard versus remove?** remove raises KeyError if absent; discard does not.
6. **Are sets indexed?** No.
7. **Average membership complexity?** Expected O(1), subject to hashing assumptions.

## 10. Dictionaries
**Definition:** A dictionary maps hashable keys to values.
**Explanation:** Dictionaries are useful for lookup, counting and grouping. Key lookup is expected O(1) on average.
**Real-world example:** Store customer details by customer ID or count event frequencies.
**Where/when/how:** Use a dictionary when each item has a key that identifies the value.
### Seven examples
1. user = {'name': 'Adil', 'age': 23}.
2. user['name'] reads a value.
3. user.get('city', 'Unknown') supplies a default.
4. user['age'] = 24 updates a value.
5. user.keys() gives keys view.
6. for key, value in user.items(): iterates pairs.
7. counts[ch] = counts.get(ch, 0) + 1 counts characters.
### Tasks
- Count words in a sentence.
- Group students by grade.
- Merge two dictionaries and describe duplicate-key behaviour.
### Interview Q&A
1. **What is a key-value pair?** A key identifies its associated value.
2. **Can a list be a key?** No, lists are unhashable.
3. **What happens with missing-key indexing?** KeyError.
4. **get versus indexing?** get can return a default for a missing key.
5. **How count frequencies?** Use a dictionary or collections.Counter.
6. **What is a dictionary view?** A dynamic view of keys, values or items.
7. **Why use a dictionary?** Efficient average-case lookup by key.

## 11. Functions
**Definition:** A function is a reusable block of code that can receive arguments and return a result.
**Explanation:** Parameters are named in the definition; arguments are passed at call time. return sends a result to the caller; print displays output.
**Real-world example:** Reuse a tax calculation or input validation rule in multiple places.
**Where/when/how:** Make a function when logic has one clear responsibility, needs reuse or needs independent testing.
### Seven examples
1. def greet(): return 'Hello'.
2. def add(a, b): return a + b.
3. def power(n, exponent=2): return n ** exponent.
4. add(a=2, b=3) uses keyword arguments.
5. def total(*values): return sum(values).
6. def details(**kwargs): return kwargs.
7. def is_even(n): return n % 2 == 0.
### Tasks
- Write factorial and prime-checking functions.
- Validate a username.
- Refactor repeated logic into helper functions.
### Interview Q&A
1. **return versus print?** Return passes a value back; print displays it.
2. **What is a default parameter?** A parameter with a fallback value.
3. **What are *args?** Conventionally collects extra positional arguments.
4. **What are **kwargs?** Conventionally collects extra keyword arguments.
5. **What is scope?** The region where a name can be accessed.
6. **Why avoid mutable defaults?** The same object is reused across calls.
7. **What is recursion?** A function calls itself, requiring a terminating base case.

## 12. Comprehensions
**Definition:** A comprehension creates a collection from an iterable, optionally filtering or transforming values.
**Explanation:** List, set and dictionary comprehensions provide concise alternatives to some loops.
**Real-world example:** Transform raw scores into adjusted scores or build an index from records.
**Where/when/how:** Use comprehensions for simple transformations; prefer a normal loop when logic becomes hard to read.
### Seven examples
1. [n * 2 for n in range(5)].
2. [n for n in range(10) if n % 2 == 0].
3. {n * n for n in range(5)}.
4. {n: n*n for n in range(5)}.
5. [word.lower() for word in words].
6. [x for row in matrix for x in row] flattens one level.
7. Use a generator expression in parentheses for lazy iteration.
### Tasks
- Extract all positive numbers.
- Build a word-length dictionary.
- Flatten a nested list.
### Interview Q&A
1. **What is a comprehension?** A concise way to construct a collection.
2. **Can it filter values?** Yes, with an if clause.
3. **List versus generator comprehension?** List builds a list; generator expression yields lazily.
4. **When avoid comprehensions?** When nested logic hurts readability.
5. **What does a set comprehension produce?** A set of unique values.
6. **What does a dictionary comprehension produce?** A mapping of generated keys to values.
7. **Do comprehensions replace every loop?** No.

## 13. Modules, packages and imports
**Definition:** A module is a Python file that can be imported; packages organise modules.
**Explanation:** Imports make existing functionality available. The main guard prevents certain code from running when a file is imported.
**Real-world example:** Split a contact manager into validation, storage and command-line modules.
**Where/when/how:** Separate code by responsibility, avoid circular imports, and use a virtual environment for dependencies.
### Seven examples
1. import math.
2. math.sqrt(25).
3. from pathlib import Path.
4. import collections.
5. Define a helper in helpers.py and import it from main.py.
6. Use if __name__ == '__main__': for script-only entry behaviour.
7. Install project dependencies inside a virtual environment.
### Tasks
- Split a small app into two modules.
- Add a main guard.
- Write setup steps in README.
### Interview Q&A
1. **What is a module?** An importable Python file.
2. **What is a package?** A namespace organising related modules.
3. **Why use imports?** Reuse functionality and organise code.
4. **What is the main guard?** A condition that runs script-entry code only when executed as the main module.
5. **Why avoid wildcard imports?** They can pollute namespaces and obscure where names came from.
6. **What is a virtual environment?** An isolated environment for project dependencies.
7. **What is a circular import?** Modules depend on each other during import in a way that can cause incomplete initialisation.

## 14. Exceptions and debugging
**Definition:** Exceptions represent abnormal execution conditions; debugging identifies and fixes defects.
**Explanation:** Syntax errors prevent parsing, runtime exceptions interrupt execution, and logic errors can silently produce incorrect output.
**Real-world example:** A form should report invalid numeric input instead of crashing.
**Where/when/how:** Catch specific expected exceptions, read tracebacks, reproduce the issue, fix it and add a regression test.
### Seven examples
1. int('abc') raises ValueError.
2. 10 / 0 raises ZeroDivisionError.
3. items[99] may raise IndexError.
4. record['missing'] raises KeyError.
5. try/except ValueError handles expected conversion failure.
6. raise ValueError('age must be non-negative') rejects invalid data.
7. finally can run cleanup whether or not an exception occurred.
### Tasks
- Safely parse an integer.
- Validate non-negative age.
- Test empty input and missing keys.
### Interview Q&A
1. **What is an exception?** An object representing an abnormal execution condition.
2. **Why catch specific exceptions?** Avoid hiding unrelated defects.
3. **What does finally do?** Runs as control leaves the try statement, commonly for cleanup.
4. **What is a traceback?** Call-stack information about an exception.
5. **What is a logic error?** The code runs but gives the wrong result.
6. **What is validation?** Checking data against expected rules.
7. **How debug?** Reproduce, inspect, isolate, fix, retest.

## 15. Files and JSON
**Definition:** File operations persist data beyond the life of a program. JSON is a text format for structured data.
**Explanation:** Use with open(...) to close files reliably. Mode w truncates, a appends and r reads.
**Real-world example:** Save a contact list and reload it next time the application starts.
**Where/when/how:** Use pathlib for paths, explicit encoding, JSON for simple structured records, and handle missing or malformed files.
### Seven examples
1. with open('notes.txt', 'r', encoding='utf-8') as f: text = f.read().
2. Write using mode 'w'.
3. Append using mode 'a'.
4. import json.
5. json.loads(text) parses a JSON string.
6. json.dump(data, file) writes JSON to an open file.
7. Use pathlib.Path to work with file paths.
### Tasks
- Save and reload a list of contacts.
- Handle a missing file gracefully.
- Separate file I/O from business logic.
### Interview Q&A
1. **Why use with open?** It reliably closes the file.
2. **What does w do?** Opens for writing and truncates existing content.
3. **What does a do?** Appends to a file.
4. **What is JSON?** A text format for structured data.
5. **loads versus load?** Parse from string versus file-like object.
6. **Why explicit encoding?** Avoid platform-dependent text decoding issues.
7. **Why catch file errors?** Files may be absent, inaccessible or invalid.

## 16. Iterators and generators
**Definition:** An iterable can provide an iterator; an iterator yields successive values; a generator is a convenient way to create an iterator.
**Explanation:** yield produces a value and suspends generator execution until the next request.
**Real-world example:** Process a large log file one line at a time.
**Where/when/how:** Use lazy iteration when data is large or produced incrementally.
### Seven examples
1. iter([1, 2, 3]) creates an iterator.
2. next(iter([10, 20])) returns 10.
3. A generator function uses yield.
4. (n*n for n in range(5)) is a generator expression.
5. for item in iterator iterates values.
6. Exhausted iterators raise StopIteration internally.
7. A generator is generally consumed; create another to iterate afresh.
### Tasks
- Generate numbers lazily.
- Read a large text file line by line.
- Compare memory use of a list and a generator conceptually.
### Interview Q&A
1. **Iterable versus iterator?** An iterable can supply an iterator; an iterator yields successive items.
2. **What does yield do?** Produces a value and suspends generator execution.
3. **What is lazy evaluation?** Compute values when requested.
4. **Why generators?** They can reduce memory use for streaming.
5. **Can an exhausted generator restart?** No; create a new generator.
6. **What does next do?** Requests the next value.
7. **When not use a generator?** When you need repeated random access to all results.

## 17. Advanced core Python: decorators, context managers, type hints and testing
**Definition:** Decorators wrap callables; context managers manage setup/cleanup; type hints document expected types; tests verify behaviour.
**Explanation:** These tools support maintainability, not automatic correctness. Type hints are not enforced at runtime by default.
**Real-world example:** Time a function, reliably close a file, document an API contract and automatically test a price calculation.
**Where/when/how:** Use decorators for reusable cross-cutting behaviour, context managers for resources, hints for clearer interfaces, and unit tests for regressions.
### Seven examples
1. @property exposes a method through attribute syntax.
2. @classmethod receives cls.
3. @staticmethod receives no automatic instance/class argument.
4. functools.wraps preserves wrapped-function metadata.
5. with open(...) is a context-manager pattern.
6. def add(a: int, b: int) -> int: return a + b.
7. Test a function with expected, boundary and invalid inputs.
### Tasks
- Add type hints to a small module.
- Write unit tests for a calculator.
- Explain a decorator you have used.
### Interview Q&A
1. **What is a decorator?** A callable that wraps or transforms another callable/class.
2. **What is a context manager?** A construct that manages entry and cleanup around a block.
3. **Do type hints enforce types at runtime?** Not by default.
4. **What is a unit test?** A test of a small unit of behaviour.
5. **What is regression testing?** Checking existing behaviour after a change.
6. **Why use functools.wraps?** Preserve useful metadata on a wrapped function.
7. **What is PEP 8?** Python's widely used style guide.

## Capstone tasks
1. Build a menu-driven contact manager.
2. Validate input and show useful errors.
3. Save/load contacts using JSON.
4. Split the code into modules.
5. Add unit tests and type hints.
6. Document setup, usage and limitations in README.
7. Explain design choices and test coverage in an interview.