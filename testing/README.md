# Python Testing Track

## Learning order
1. [Day 20 — Debugging Fundamentals](../days/DAY-20-Debugging-Fundamentals.md)
2. [Day 22 — Testing and Assertions](../days/DAY-22-Testing.md)
3. Run tests linked from [Day 21 — Exceptions](../days/DAY-21-Exceptions.md), [Day 23 — Files](../days/DAY-23-Files.md), and [Day 39 — SQL with Python](../days/DAY-39-SQL-with-Python.md).

## Required test categories
- Happy path and ordinary inputs
- Exact boundaries and values just outside them
- Invalid types and malformed input
- Empty or missing data
- Regression cases for bugs that have been fixed

## Commands
Run the tests from the directory containing the test files:
```bash
python -m unittest -v
```
Use temporary directories or in-memory SQLite databases to keep tests isolated. Do not claim code has been tested unless you actually ran it.
