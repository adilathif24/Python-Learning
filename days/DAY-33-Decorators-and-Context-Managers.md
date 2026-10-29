# Day 33 — Decorators and Context Managers

**Status:** Full study pack. Run every example and test before marking mastery.

## 1. Definition
A **decorator** is a callable that takes a function or class and returns a wrapped/replacement callable. A **context manager** manages setup and cleanup around a block of code, commonly using `with`.

## 2. Why / where / when
Decorators help add logging, timing, authorization checks or caching without repeating logic. Context managers protect resources such as files, locks and database connections. Use `functools.wraps` to preserve wrapped-function metadata. Avoid decorators that conceal major side effects or make call order unclear.

## 3. Syntax and rules
```python
from functools import wraps
def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting")
        return func(*args, **kwargs)
    return wrapper

@announce
def greet(name):
    return f"Hello {name}"
```
Decorator syntax is equivalent to rebinding the function through the decorator. Wrappers often forward `*args, **kwargs` and return the original result.

## 4. Five worked examples
### Example 1 — Basic decorator
```python
def announce(func):
    def wrapper():
        print("Before"); func(); print("After")
    return wrapper
@announce
def say_hi(): print("Hi")
say_hi()
```
Output: Before, Hi, After. The decorator wraps the original function.

### Example 2 — Preserve arguments and result
```python
from functools import wraps
def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@logged
def add(a,b): return a+b
print(add(3,4))
```
Output: `Calling add` then `7`. The wrapper forwards arguments and returns the result.

### Example 3 — Timing
```python
from functools import wraps
from time import perf_counter
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=perf_counter()
        result=func(*args, **kwargs)
        print(f"Elapsed: {perf_counter()-start:.6f}s")
        return result
    return wrapper
@timed
def total(): return sum(range(100))
print(total())
```
Output includes elapsed time and 4950. Timing varies by machine.

### Example 4 — Decorator with an argument
```python
from functools import wraps
def repeat(times):
    if times < 0: raise ValueError("times must be non-negative")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result=None
            for _ in range(times): result=func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(2)
def double(n): return n*2
print(double(4))
```
Output: `8`. The function executes twice and returns the final result.

### Example 5 — File context manager
```python
from pathlib import Path
p=Path("context-demo.txt")
with p.open("w",encoding="utf-8") as file: file.write("saved")
print(p.read_text(encoding="utf-8"))
p.unlink()
```
Output: `saved`. Exiting with closes the file automatically.

## 5. Five practice tasks with solutions
### Task 1 — Log a function name
```python
from functools import wraps
def log_name(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper
@log_name
def greet(name): return f"Hi {name}"
print(greet("Ali"))
```
Output: `greet` then `Hi Ali`.

### Task 2 — Reject negative input
```python
from functools import wraps
def non_negative(func):
    @wraps(func)
    def wrapper(value):
        if value < 0: raise ValueError("negative value")
        return func(value)
    return wrapper
@non_negative
def square_root_input(value): return value ** 0.5
print(square_root_input(9))
```
Output: `3.0`. Negative values raise ValueError.

### Task 3 — Use contextlib
```python
from contextlib import contextmanager
@contextmanager
def tagged():
    print("enter")
    try: yield
    finally: print("exit")
with tagged(): print("inside")
```
Output: enter, inside, exit.

### Task 4 — Preserve function metadata
```from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs): return func(*args,**kwargs)
    return wrapper
@decorator
def greet(): """Greeting demo."""; return "hi"
print(greet.__name__)
```
Output: `greet`. wraps preserves name and docstring.

### Task 5 — Ensure cleanup after error
```from contextlib import contextmanager
@contextmanager
def managed():
    print("open")
    try: yield
    finally: print("close")
try:
    with managed(): raise RuntimeError("problem")
except RuntimeError: print("caught")
```
Output: open, close, caught. Finally runs during exception propagation.

## 6. Common mistakes
- Wrapper doesn't return the wrapped function's result.
- Wrapper signature breaks positional/keyword calls.
- Forgetting wraps hides metadata.
- Decorator order matters when stacking several decorators.
- Context-manager cleanup should be in finally/exit handling.
- Do not catch and suppress exceptions unless that behavior is intended.

## 7. Interview questions
1. What does @decorator do? **Passes the function through the decorator and binds the returned callable.**
2. Why wraps? **Preserves metadata such as name/docstring.**
3. What is a context manager? **Controls setup and cleanup around a with block.**
4. Why use yield in contextmanager? **Separates the setup point from cleanup after the with body.**
5. Common decorator uses? **Logging, timing, caching and access checks.**

## 8. Project — Timing Decorator
Save as `timed_report.py`.
```python
from functools import wraps
from time import perf_counter

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        started=perf_counter()
        result=func(*args, **kwargs)
        elapsed=perf_counter()-started
        return result, elapsed
    return wrapper

@measure
def sum_range(limit):
    if limit < 0: raise ValueError("limit must be non-negative")
    return sum(range(limit))

def main():
    result, elapsed=sum_range(100_000)
    print(f"Result: {result}; elapsed: {elapsed:.6f}s")

if __name__ == "__main__": main()
```
Run `python timed_report.py`. Timing is informational, not a benchmark guarantee.

### Tests — `test_timed_report.py`
```python
import unittest
from timed_report import sum_range

class TimedTests(unittest.TestCase):
    def test_result(self): self.assertEqual(sum_range(10)[0],45)
    def test_zero(self): self.assertEqual(sum_range(0)[0],0)
    def test_elapsed_nonnegative(self): self.assertGreaterEqual(sum_range(5)[1],0)
    def test_negative_raises(self):
        with self.assertRaises(ValueError): sum_range(-1)
    def test_metadata(self): self.assertEqual(sum_range.__name__,"sum_range")

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Why return func result? **So callers retain normal behavior.**
2. What does wraps preserve? **Metadata.**
3. Which keyword starts a context manager block? **with.**
4. Where put cleanup? **finally or context-manager exit logic.**
5. What does decorator factory return? **Usually a decorator callable.**
**Challenge:** Add a retry decorator for a function that raises a specified exception, with a maximum attempt limit and tests for success-on-retry and exhausted retries.

## Real-world use cases — where, when and how
1. **Call logging:** Where: internal libraries. When function calls need traceability. How: a decorator records function names and safe metadata.
2. **Timing:** Where: profiling. When comparing code paths. How: wrap a function with a timer and keep its return result intact.
3. **Authorization check:** Where: service methods. When roles must be checked before execution. How: a decorator checks the actor and refuses unauthorized calls.
4. **File/database resources:** Where: persistence code. When handles must be released. How: use with/context managers for deterministic cleanup.
5. **Temporary configuration:** Where: tests. When state must be reset even after failure. How: a context manager sets up state and restores it in finally.


## 10. Completion
- [ ] I can explain wrapper and decorator factory.
- [ ] Context manager cleanup tests pass.
- [ ] I solved the retry challenge.
