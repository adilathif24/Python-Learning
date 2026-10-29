# Python Learning — Day-Wise Master Plan

> **Learning rule:** Follow the days in order. A day marked **Practised** means it appeared in our learning sessions; it does not mean mastery. A day marked **Next / Planned** must be taught and practised before it is checked off.

## Mandatory lesson format — apply to every topic

Do not teach a topic as a short summary. Teach it thoroughly, from the definition to independent practice. Every topic/lesson must include:

1. **Definition:** simple-English definition and the correct technical meaning.
2. **Detailed explanation:** explain the concept step by step, with a mental model and a dry run where useful.
3. **Why, where, and when:** why the concept exists, where it is used in real work, when to choose it, and when not to use it.
4. **Syntax and rules:** general syntax, parameters, indentation, return behaviour, and important rules.
5. **Five complete worked examples (minimum):** each must contain the problem/question, complete runnable code, expected output, explanation of important lines, and a short dry run. Progress from easy to medium and include variations. Never provide fragments when a complete program is needed.
6. **Five practice tasks (minimum):** each must include the question, requirements, sample input/output, and a **full working solution code** followed by an explanation. Do not leave hints in place of solutions.
7. **Common mistakes and edge cases:** show incorrect patterns, explain why they fail, and provide corrected code when appropriate.
8. **Interview preparation:** likely interview questions with clear, ready-to-say answers and follow-up questions.
9. **One real-world mini-project:** explain the purpose, users, use cases, and design; provide the **complete runnable project code**, instructions to run it, sample output, test cases, limitations, and possible improvements.
10. **Revision:** quiz with answers plus one independent challenge to attempt without copying.
11. **GitHub organisation:** save the lesson in the correct folder, link it from README/index files where appropriate, and update progress only after the user has practised it.

All code examples, task answers, and project code must be complete enough to run. Include expected outputs. Explain code in simple English. Split a large topic into multiple lessons rather than rushing or omitting requirements. Do not mark a topic mastered merely because notes were written.

## Progress key

- **Practised** — studied in our recent sessions; revise and solve fresh variations.
- **Next** — the next lesson sequence to cover.
- **Planned** — later topics; do not mark complete early.

## Part A — What we have studied so far

### Day 01 — Python output, variables, and basic data types — Practised
- `print()`, variables, assignment, `int`, `float`, `str`, `bool`
- Basic `input()` usage and understanding that input arrives as text
- Still to strengthen: `type()`, `None`, comments, naming, f-strings, conversions and invalid input

### Day 02 — Operators — Practised / revise
- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Still to cover properly: logical, assignment, membership, identity and precedence

### Day 03 — Conditions — Practised / revise
- `if`, `elif`, `else`, comparisons, simple decision-making
- Still to cover: combined/nested conditions, boundaries, input validation and branch ordering

### Day 04 — Loops and counting — Practised
- `for`, `while`, `range()`, counters and accumulators
- Sum of a range, multiplication tables and countdown-style practice
- Still to cover: `break`, `continue`, nested loops, patterns, menu loops and loop safety

### Day 05 — Number problems — Practised / revise
- Sum, multiplication table, factorial, prime check, Fibonacci, digit counting
- Swapping values with a third variable and without a third variable
- Still to cover: digit sum, number reversal, numeric palindrome, Armstrong, GCD/LCM, negative and boundary cases
- Fix previous mistakes by tracing conditions carefully (for example, a loop condition such as `while n < 0` will not run for a positive number).

### Day 06 — Strings — Initial practice
- Iterating over a string and counting vowels/consonants
- Previously encountered issue to remember: test the character (for example, `if ch in vowels`), not the entire string variable
- Still to cover: indexing, slicing, immutability, `lower()`, `upper()`, `strip()`, `split()`, `join()`, `replace()`, frequency and palindrome handling

### Day 07 — Lists and basic collection operations — Practised
- Lists, zero-based indexing, `append()`, `remove()`, `len()`, `in`, `not in`
- Name Management mini-project: add, delete, restore and view names
- Still to cover: list slicing, `extend()`, `insert()`, `pop()`, `clear()`, `count()`, `index()`, sorting, copying and aliasing

### Day 08 — Functions and return values — Practised
- `def`, calling functions, parameters versus arguments, `return` versus `print()`
- Using functions to organise the Name Management project

### Day 09 — Function argument patterns — Practised / continue
- Single argument
- Multiple positional arguments
- Named/keyword arguments
- Arbitrary positional arguments with `*args` (collected into a tuple)
- Arbitrary keyword arguments with `**kwargs` (collected into a dictionary)
- Email validator exercise: trim surrounding spaces, check `@`, reject repeated `@`, collect accepted values and return the list
- Important: this is a beginner-level email-like check, not complete standards-compliant email validation.
- Still to cover: default arguments, parameter ordering, local/global scope, docstrings, argument validation and clean return contracts

## Part B — Remaining Python Core sequence

### Day 10 — Finish function fundamentals — Next
- Default arguments, positional vs keyword calling, scope and local variables
- Docstrings, small functions, validation, returning values consistently
- **Project:** reusable unit converter or order-total calculator

### Day 11 — Complete lists — Planned
- Mutating vs returning, slices, copy vs alias, nested lists, list methods
- **Project:** shopping cart with add/remove/update/total

### Day 12 — Tuples and unpacking — Planned
- Tuple creation, immutability, unpacking, returning multiple values
- **Project:** coordinate and student-record helper

### Day 13 — Sets — Planned
- Unique values, membership, union/intersection/difference
- **Project:** event registration and attendance comparison

### Day 14 — Dictionaries — Planned
- Key-value pairs, `get()`, `keys()`, `values()`, `items()`, update and nested dictionaries
- **Project:** student marks / inventory lookup

### Day 15 — Choosing collections — Planned
- List vs tuple vs set vs dictionary; lookup and duplication trade-offs
- **Project:** combined contact book using the right structure

### Day 16 — String mastery — Planned
- Indexing, slicing, methods, counting, splitting, joining, formatting and palindrome checks
- **Project:** text analyser with word/character counts

### Day 17 — Loop mastery — Planned
- `break`, `continue`, nested loops, patterns, sentinel and menu-driven loops
- **Project:** menu-driven ATM simulator (educational; no real transactions)

### Day 18 — Number problem patterns — Planned
- Digit sum/reverse, palindrome, Armstrong, GCD/LCM, efficient loops and edge cases
- **Project:** number-analysis toolkit

### Day 19 — Input validation and clean console programs — Planned
- Type conversion, invalid input, boundaries, retry loops, useful messages
- **Project:** robust bill and discount calculator

### Day 20 — Debugging fundamentals — Planned
- Syntax, runtime and logic errors; reading tracebacks; tracing variables
- **Project:** debug a deliberately broken student-grade program

### Day 21 — Exceptions — Planned
- `try`, `except`, `else`, `finally`; `ValueError`, `TypeError`, `KeyError`, `IndexError`
- Avoid overly broad exception handling
- **Project:** safe calculator with clear error messages

### Day 22 — Testing — Planned
- Test cases, assertions, boundary and invalid-input tests, simple unit tests
- **Project:** tests for the email validator and Name Management program

### Day 23 — Files — Planned
- Reading/writing text, `with open()`, modes, paths, encoding and missing files
- **Project:** save and reload a contact list

### Day 24 — CSV and JSON — Planned
- Read/write structured data, parse JSON, handle malformed/missing data
- **Project:** file-backed task manager

### Day 25 — Modules and packages — Planned
- `import`, `from ... import`, modules, packages, `__name__ == "__main__"`
- **Project:** split a calculator/contact manager into modules

### Day 26 — Virtual environments and dependencies — Planned
- `venv`, `pip`, dependency files, README setup instructions
- **Project:** create a reproducible environment for a small Python app

### Day 27 — Comprehensions and built-ins — Planned
- List/set/dictionary comprehensions, `enumerate()`, `zip()`, `sorted()`, `sum()`, `min()`, `max()`
- **Project:** marks and sales summary report

### Day 28 — Sorting and lambdas — Planned
- `sorted(key=...)`, custom sort keys, lambda basics and readable alternatives
- **Project:** sort students/products by selected fields

### Day 29 — Functions deeper — Planned
- `*args`, `**kwargs`, unpacking calls, scope, type hints and return contracts
- **Project:** configurable report generator

### Day 30 — Iterators and generators — Planned
- Iterable vs iterator, `iter()`, `next()`, `yield`, lazy processing
- **Project:** process a large log file line by line

### Day 31 — OOP foundations — Planned
- Classes, objects, attributes, `__init__`, `self`, instance/class attributes
- **Project:** Student or Product class

### Day 32 — OOP design — Planned
- Methods, encapsulation, inheritance, polymorphism, abstraction, composition
- When to choose a class versus a function
- **Project:** library or employee management model

### Day 33 — Context managers and decorators — Planned
- Learn after functions, exceptions and OOP basics; use cases and trade-offs
- **Project:** timing/logging decorator and safe resource handling

### Day 34 — APIs and external data — Planned
- HTTP/JSON concepts, requests, status codes, timeouts and error handling (after dependencies)
- **Project:** API-powered information lookup, with graceful failure handling

## Part C — Problem solving, integration, and career projects

### Day 35 — DSA foundations and complexity — Planned
- Big O, time vs space, arrays/lists, strings and hash maps
- **Project:** compare simple search/count approaches and explain complexity

### Day 36 — Searching and sorting — Planned
- Linear/binary search, sorting algorithms, sorted-input assumptions and complexity
- **Project:** searchable sorted contact/product list

### Day 37 — Stacks, queues, linked lists, recursion — Planned
- Core operations, use cases, recursion base cases and call stack
- **Project:** undo history or task queue simulation

### Day 38 — Trees, heaps and graphs — Planned
- Traversal concepts, priority queues, graph representation and BFS/DFS
- **Project:** simple route/network traversal exercise

### Day 39 — SQL with Python — Planned
- Keep SQL theory as a distinct learning track; then connect Python to a database
- CRUD, parameterised queries, transactions and database error handling
- **Project:** database-backed contact or task manager

### Day 40 — Capstone and interview preparation — Planned
- Choose one project, organise code, validate inputs, write tests and document setup
- Practise explaining design, limitations, test cases and complexity
- **Project options:** file-backed task manager, inventory/contact manager, or an API-backed application

## Repository file order

Follow this order even if the GitHub file list is alphabetic:

1. `README.md` — entry point and links.
2. `DAY-WISE-PYTHON-LEARNING-PLAN.md` — this schedule and progress tracker.
3. `ROADMAP.md` — topic checklist across the full curriculum.
4. `MINDMAP.md` — visual/text map of how topics connect.
5. `core/` — Python fundamentals, functions, collections, files, exceptions and intermediate Python.
6. `oop/` — OOP only after function and collection foundations.
7. `dsa/` — DSA only after basic Python and complexity introduction.
8. `interview/` — revision workbooks; use alongside each phase, not as a substitute for practice.

Existing detailed guides should be reused and linked from the matching day. Do not duplicate a guide just to make a new day file; create a new lesson file when a topic is missing or needs the full five-example/five-task format.

## Daily completion checklist

Before checking a day off, confirm:

- [ ] I can define the topic in simple English.
- [ ] I can explain why, where and when it is useful.
- [ ] I can write all five examples without copy-pasting.
- [ ] I have attempted all five tasks and checked the full solutions.
- [ ] I can explain the real-world project's complete code.
- [ ] I tested normal, boundary and invalid inputs.
- [ ] I can answer interview questions and solve one new variation independently.

## Important note about progress

The “Practised” labels are based on our learning-session history, not a claim that all exercises or every line in existing guides have been executed. Keep SQL/data-analysis learning separate from this Python curriculum. SQL integration appears near the end only as a Python application topic.
