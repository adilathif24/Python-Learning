# Day 33 — Decorators and Context Managers

**Status:** Planned  
**Goal:** Understand reusable wrappers and safe resource management.

## 1. Decorators

**Definition:** A decorator is a callable that takes a function (or class) and returns a replacement or wrapped callable.

**Syntax**
```python
@decorator_name
def function_name():
    pass
```

### Example 1 — Basic decorator
```python
def announce(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper

@announce
def greet():
    print("Hello!")

greet()
```
Output:
```text
Starting
Hello!
Finished
```

### Example 2 — Preserve arguments
```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3, 4))
```
Output: `Calling add` then `7`.

### Example 3 — Timing a function
```python
from time import perf_counter

def measure(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"Elapsed: {perf_counter() - start:.6f}s")
        return result
    return wrapper

@measure
def calculate():
    return sum(range(10000))

print(calculate())
```

### Example 4 — Decorator with a setting
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")

say_hi()
```

### Example 5 — Context manager with `with`
```python
from pathlib import Path

path = Path("sample.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Saved safely")
print(path.read_text(encoding="utf-8"))
```

## Where / when to use
- Logging function calls, timing, authentication/permission checks, caching and retries.
- Use context managers for files, locks, database connections and other resources that must be cleaned up.
- Avoid decorators that hide important behaviour or make debugging harder.

## Practice tasks
1. Write a decorator that prints a function name.
2. Write a decorator that logs arguments and return value.
3. Add a decorator that rejects negative numbers for a square-root function.
4. Use `with open(...)` to save and read a user note.
5. Create a context manager with `contextlib.contextmanager` that prints enter/exit messages.

## Interview questions
1. What does `@decorator` do?
2. Why should wrappers usually accept `*args, **kwargs`?
3. What is the purpose of `functools.wraps`?
4. Why is a context manager safer than manually closing a file?
5. Name real-world cases for decorators.

**Completion checklist:** Run the examples, solve all five tasks independently, explain the output, and add tests before marking Completed.
