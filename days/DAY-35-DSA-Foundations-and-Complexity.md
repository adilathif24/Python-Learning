# Day 35 — DSA Foundations and Complexity

**Status:** Full study pack created. This starts the separate Python DSA track, not Data Analyst learning.

## 1. Definition
A **data structure** organises data; an **algorithm** describes steps to solve a problem. **Time complexity** estimates how work grows with input size; **space complexity** estimates extra memory. Big-O describes an upper growth rate, not an exact runtime.

## 2. Why / where / when
DSA is used in interviews and to choose efficient solutions. Identify input size n, count repeated operations, and compare growth rates. Avoid optimizing by intuition alone; measure real systems after selecting an appropriate algorithm.

## 3. Syntax and complexity intuition
```python
def has_value(values, target):
    for value in values:       # up to n checks
        if value == target:
            return True
    return False
```
Worst-case time is O(n), extra space O(1). A nested loop over the same n items is usually O(n²).

## 4. Five worked examples
### Example 1 — Constant time
```def first(values):
    return values[0] if values else None
print(first([9,8,7]))
```
Output: `9`. Index access is O(1) for lists.

### Example 2 — Linear scan
```python
def contains(values, target):
    for value in values:
        if value == target: return True
    return False
print(contains([3,4,5],4))
```
Output: `True`. It may inspect every item: O(n).

### Example 3 — Nested loop
```python
pairs = [(a,b) for a in range(3) for b in range(3)]
print(len(pairs))
```
Output: `9`. Two loops of size n produce roughly n² pairs.

### Example 4 — Binary search prerequisite
```python
values = [2,4,6,8,10]
print(6 in values)
```
Output: `True`. Membership here is linear; binary search can be O(log n) on sorted random-access sequences.

### Example 5 — Count with dictionary
```python
counts={}
for value in [1,2,1,3,1,2]:
    counts[value]=counts.get(value,0)+1
print(counts[1])
```
Output: `3`. Dictionary counting is O(n) average for n inputs.

## 5. Five tasks with solutions
### Task 1 — Sum list
```def total(values):
    result=0
    for value in values: result += value
    return result
print(total([1,2,3,4]))
```
Output: `10`, O(n) time, O(1) extra space.

### Task 2 — Find maximum
```def maximum(values):
    if not values: raise ValueError("non-empty list required")
    result=values[0]
    for value in values[1:]:
        if value>result: result=value
    return result
print(maximum([3,9,2]))
```
Output: `9`, O(n).

### Task 3 — Remove duplicates with set
```def unique(values): return list(dict.fromkeys(values))
print(unique([1,2,1,3]))
```
Output: `[1, 2, 3]`. Average O(n), preserves order.

### Task 4 — Count pairs
```values=[1,2,3]
count=0
for i in range(len(values)):
    for j in range(i+1,len(values)): count+=1
print(count)
```
Output: `3`, pair enumeration is O(n²).

### Task 5 — Compare list vs set membership
```values=list(range(1000)); value_set=set(values)
print(999 in values, 999 in value_set)
```
Output: `True True`. Both correct, expected membership cost differs.

## 6. Common mistakes
- Big-O does not tell exact wall-clock time.
- Average-case and worst-case may differ.
- Nested loops are not always O(n²); inspect how many times each runs.
- Space complexity concerns extra memory as input grows.
- Benchmarking needs representative inputs and repeated measurements.

## 7. Interview Q&A
1. What does O(1) mean? **Work stays bounded as n grows.**
2. What is O(n)? **Work grows approximately linearly.**
3. What is O(log n)? **Each step reduces the problem by a constant factor, as in binary search.**
4. What is a trade-off? **Time may be reduced by using more memory, or vice versa.**
5. Why analyze complexity? **Compare how solutions scale.**

## 8. Project — Algorithm Profiler
Save as `algorithm_profiler.py`.
```python
from time import perf_counter

def linear_contains(values, target):
    for value in values:
        if value == target: return True
    return False

def profile(size):
    values=list(range(size))
    start=perf_counter()
    found=linear_contains(values, size-1)
    elapsed=perf_counter()-start
    return found, elapsed

if __name__ == "__main__":
    found, seconds=profile(100_000)
    print(f"found={found}, seconds={seconds:.6f}")
```
Timing varies by computer and is only illustrative.

### Tests — `test_algorithm_profiler.py`
```python
import unittest
from algorithm_profiler import linear_contains, profile
class ProfilerTests(unittest.TestCase):
    def test_found(self): self.assertTrue(linear_contains([1,2],2))
    def test_missing(self): self.assertFalse(linear_contains([1,2],3))
    def test_empty(self): self.assertFalse(linear_contains([],1))
    def test_profile(self): self.assertTrue(profile(10)[0])
    def test_zero_size(self): self.assertFalse(profile(0)[0])
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Linear scan worst-case? **O(n).**
2. Nested n×n loops? **Usually O(n²).**
3. Binary search prerequisite? **Sorted searchable sequence.**
4. What is space complexity? **Extra memory growth.**
5. Dictionary lookup average complexity? **O(1), average case.**
**Challenge:** Compare linear search and binary search for a sorted list, prove result correctness with tests and explain complexity.

## Real-world use cases — where, when and how
1. **Search optimization:** Where: product/user lookup. When input size grows. How: compare linear scan with hash lookup or binary search where preconditions allow.
2. **Memory planning:** Where: data import. When collections grow large. How: estimate additional storage and process generators if data need not remain in memory.
3. **Interview analysis:** Where: coding rounds. When explaining alternatives. How: state time/space complexity and define the input size.
4. **Duplicate detection:** Where: data quality checks. When repeated IDs are invalid. How: use a set and analyze expected O(n) membership.
5. **Algorithm selection:** Where: utility design. When performance requirements matter. How: choose structures and algorithms by access pattern and measure representative workloads.


## 10. Completion
- [ ] I can explain time/space complexity and Big-O.
- [ ] Project tests pass.
- [ ] I completed the binary-search challenge.
