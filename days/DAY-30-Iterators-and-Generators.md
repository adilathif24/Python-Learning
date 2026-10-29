# Day 30 — Iterators and Generators

**Status:** Full study pack. Complete the exercises and tests before marking mastery.

## 1. Definition
An **iterable** can provide an iterator. An **iterator** produces items one at a time via `next()` and eventually raises StopIteration. A **generator** is a convenient iterator created by a generator function using `yield`.

## 2. Why / where / when
Iterators and generators support lazy processing, large files, streams and pipelines without materializing all results in memory. Use lists when you need repeatable indexing or all results at once; use a generator for one-pass consumption. Remember that generators are exhausted after iteration.

## 3. Syntax and rules
```python
def count_up_to(limit):
    current=1
    while current <= limit:
        yield current
        current += 1
for number in count_up_to(3):
    print(number)
```
Calling a generator function returns a generator; its body begins when iterated. `yield` pauses and preserves local state.

## 4. Five worked examples
### Example 1 — Iterator manually
```python
iterator = iter([10,20])
print(next(iterator), next(iterator))
```
Output: `10 20`. The iterator advances per next call.

### Example 2 — Handle exhaustion
```python
it = iter([1])
print(next(it))
print(next(it, "done"))
```
Output: `1` then `done`. The default avoids StopIteration on exhaustion.

### Example 3 — Generator function
```python
def squares(n):
    for value in range(n): yield value*value
print(list(squares(4)))
```
Output: `[0, 1, 4, 9]`. Yield emits one value at a time.

### Example 4 — Generator expression
```python
total = sum(n*n for n in range(1, 4))
print(total)
```
Output: `14`. Generator expression avoids building a temporary list.

### Example 5 — One-pass consumption
```python
items = (x for x in [1,2,3])
print(list(items))
print(list(items))
```
Output: `[1, 2, 3]` then `[]`. The generator is exhausted.

## 5. Five tasks with solutions
### Task 1 — Yield even values
```def evens(values):
    for value in values:
        if value % 2 == 0: yield value
print(list(evens(range(1,7))))
```
Output: `[2, 4, 6]`.

### Task 2 — Generate running totals
```def running_total(values):
    total=0
    for value in values:
        total += value
        yield total
print(list(running_total([2,3,4])))
```
Output: `[2, 5, 9]`.

### Task 3 — Read non-empty lines from text
```def nonempty_lines(lines):
    for line in lines:
        if line.strip(): yield line.strip()
print(list(nonempty_lines(["a\n","  ","b\n"])))
```
Output: `['a', 'b']`.

### Task 4 — Build a safe next wrapper
```def next_or_none(iterator):
    return next(iterator, None)
print(next_or_none(iter([])))
```
Output: `None`.

### Task 5 — Compose generator pipeline
```values = range(1, 11)
result = sum(n for n in values if n % 2 == 0)
print(result)
```
Output: `30`. The generator lazily filters values as sum consumes it.

## 6. Common mistakes
- Calling next on an iterable directly; call iter first.
- Reusing an exhausted generator.
- Returning a list instead of yield when lazy behavior is the point.
- Assuming a generator can be indexed.
- Keeping file handles or resources open longer than needed.

## 7. Interview Q&A
1. Iterable vs iterator? **Iterable supplies an iterator; iterator yields successive values.**
2. What does yield do? **Emits a value and suspends generator state.**
3. Why generators save memory? **They produce values on demand instead of storing all values.**
4. What signals exhaustion? **StopIteration.**
5. Can you iterate a generator twice? **Not after exhaustion; create a new generator.**

## 8. Project — Lazy Log Filter
Save as `log_filter.py`.
```python
def matching_lines(lines, keyword):
    needle = keyword.casefold()
    for line in lines:
        if needle in line.casefold():
            yield line.rstrip("\\n")

def main():
    sample = ["INFO started\n", "ERROR disk full\n", "WARN slow\n", "ERROR timeout\n"]
    for line in matching_lines(sample, "error"): print(line)

if __name__ == "__main__": main()
```
Output: lines for ERROR disk full and ERROR timeout.

### Tests — `test_log_filter.py`
```python
import unittest
from log_filter import matching_lines

class LogFilterTests(unittest.TestCase):
    def test_case_insensitive(self): self.assertEqual(list(matching_lines(["Error!"],"error")),["Error!"])
    def test_no_matches(self): self.assertEqual(list(matching_lines(["ok"],"error")),[])
    def test_multiple(self): self.assertEqual(list(matching_lines(["err","ERROR"],"err")),["err","ERROR"])
    def test_lazy_iterator(self): self.assertTrue(hasattr(matching_lines(["x"],"x"),"__next__"))
    def test_empty_keyword_matches_all(self): self.assertEqual(list(matching_lines(["a","b"],"")),["a","b"])

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What does iter return? **An iterator.**
2. What does yield produce? **A value and a pause point.**
3. What happens after generator exhaustion? **Iteration ends.**
4. Why use a generator for a big file? **Processes one item at a time.**
5. What exception marks exhaustion? **StopIteration.**
**Challenge:** Read a large log file line-by-line and count ERROR records without storing all lines, then test with an in-memory iterator.

## Real-world use cases — where, when and how
1. **Large logs:** Where: server support tools. When files exceed memory comfort. How: stream lines and yield only matching records.
2. **Data pipelines:** Where: ETL-like application code. When each record is transformed in sequence. How: chain generators for filtering/normalization.
3. **Paginated API:** Where: integrations. When records arrive page by page. How: yield each page's records instead of accumulating everything.
4. **Infinite sequences:** Where: simulations or scheduling. When values are generated on demand. How: use a generator with explicit stopping conditions at the consumer.
5. **Memory-aware aggregation:** Where: reports. When only the total is needed. How: pass a generator expression to sum rather than allocating a separate list.


## 10. Completion
- [ ] I understand iterable, iterator, next and yield.
- [ ] Project tests pass.
- [ ] I completed the lazy file-processing challenge.
