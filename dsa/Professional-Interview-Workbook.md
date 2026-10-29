# DSA — Professional Coding Interview Workbook (Python)

For every solution, communicate: **clarify constraints → baseline approach → chosen pattern → correctness reasoning → dry run → time/space complexity → edge cases**.

## 1. Complexity analysis
**Definition:** Time complexity describes how resource use grows with input size; space complexity describes memory growth. Big O represents an asymptotic upper bound.
### Seven code/analysis examples
```python
# 1. O(1) list index
values = [10, 20, 30]; print(values[1])  # 20
# 2. O(n) scan
def contains(values, target):
    for value in values:
        if value == target: return True
    return False
print(contains([2, 4, 8], 4))
# 3. O(n^2) pairs
def print_pairs(values):
    for left in values:
        for right in values: print(left, right)
# 4. O(log n) repeated halving
def count_halvings(n):
    steps = 0
    while n > 1: n //= 2; steps += 1
    return steps
print(count_halvings(16))  # 4
# 5. Typical comparison sort O(n log n)
print(sorted([5, 1, 4, 2]))
# 6. O(n) auxiliary output space
def doubled(values): return [x * 2 for x in values]
# 7. Sequential O(n) loops remain O(n)
def count_twice(values):
    total = 0
    for _ in values: total += 1
    for _ in values: total += 1
    return total
```
### Seven interview answers
1. **Big O?** An asymptotic upper bound used to reason about algorithm growth.
2. **O(n) vs O(log n)?** Linear scan versus repeated constant-factor reduction.
3. **Auxiliary space?** Extra memory beyond the input, using a stated convention.
4. **Is O(1) always faster?** Not for every small input; constants and overhead matter.
5. **Best/average/worst case?** Resource usage under favourable, typical/modelled and least favourable inputs.
6. **Why analyse space?** Memory limits can make an otherwise fast algorithm impractical.
7. **How state complexity?** Define n, state time and auxiliary space, and identify dominant work.
### Five practice answers
1. One loop: O(n). 2. Two n-loops nested: O(n²). 3. Divide by 3 until 1: O(log n). 4. Sort then scan: O(n log n). 5. Build a list of n outputs: O(n) extra space.

## 2. Arrays, strings and two pointers
**Definition:** Python lists are dynamic arrays with O(1) indexed access; two pointers maintain indices to eliminate redundant work, often on sorted sequences.
### Seven complete examples
```python
# 1. Linear search
def linear_search(values, target):
    for i, value in enumerate(values):
        if value == target: return i
    return -1
print(linear_search([4, 8, 2], 8))  # 1

# 2. Reverse in place
def reverse_in_place(values):
    left, right = 0, len(values)-1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1; right -= 1
    return values
print(reverse_in_place([1,2,3,4]))  # [4,3,2,1]

# 3. Palindrome normalisation
def is_palindrome(text):
    s = "".join(c.lower() for c in text if c.isalnum())
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]: return False
        left += 1; right -= 1
    return True
print(is_palindrome("Never odd or even"))  # True

# 4. Pair sum in sorted list
def has_pair_sum_sorted(values, target):
    left, right = 0, len(values)-1
    while left < right:
        total = values[left] + values[right]
        if total == target: return True
        if total < target: left += 1
        else: right -= 1
    return False
print(has_pair_sum_sorted([1,2,4,7,11], 9))  # True

# 5. Remove duplicates in sorted list in place
def deduplicate_sorted(values):
    if not values: return 0
    write = 1
    for read in range(1, len(values)):
        if values[read] != values[write-1]:
            values[write] = values[read]; write += 1
    return write
a = [1,1,2,2,3]; size = deduplicate_sorted(a)
print(a[:size])  # [1,2,3]

# 6. Merge sorted lists
def merge_sorted(a, b):
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out
print(merge_sorted([1,4], [2,3]))  # [1,2,3,4]

# 7. Maximum with empty-input validation
def find_maximum(values):
    if not values: raise ValueError("Input cannot be empty")
    best = values[0]
    for value in values[1:]:
        if value > best: best = value
    return best
print(find_maximum([7,2,19,4]))  # 19
```
**Real-world use:** Search IDs, compare text, merge sorted exports and deduplicate sorted records.
### Seven interview Q&A
1. **Why is indexing O(1)?** Dynamic-array offset access locates an element directly.
2. **Why is unsorted search O(n)?** Worst case checks every element.
3. **When use two pointers?** When sequence structure lets pointer movement safely eliminate candidates.
4. **Why sorted input for pair sum?** Sum direction determines which pointer can move.
5. **In-place?** Modifies input using limited extra storage; state assumptions.
6. **Why check empty input?** Avoid invalid index access and define contract.
7. **Merge complexity?** O(n+m) time; output implementation uses O(n+m) space.
### Five practice tasks with solutions
1. Linear search: use `linear_search` above.
2. Reverse in place: use `reverse_in_place` above.
3. Palindrome: use `is_palindrome` above.
4. Merge sorted lists: use `merge_sorted` above.
5. Maximum with empty check: use `find_maximum` above.

## 3. Hashing and frequency maps
**Definition:** Hash tables map hashable keys to values. Python dictionaries/sets offer average-case O(1) membership and lookup under typical conditions.
### Seven complete examples
```python
# 1. Membership
print(20 in {10,20,30})  # True
# 2. Counter
from collections import Counter, defaultdict
print(Counter("banana"))
# 3. Manual frequency
def frequencies(values):
    counts = {}
    for value in values: counts[value] = counts.get(value, 0) + 1
    return counts
print(frequencies([1,2,1,3,2,1]))  # {1:3, 2:2, 3:1}
# 4. Two Sum
def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in seen: return [seen[need], i]
        seen[value] = i
    return []
print(two_sum([2,7,11,15], 9))  # [0,1]
# 5. First unique character index
def first_unique(text):
    counts = Counter(text)
    for i, char in enumerate(text):
        if counts[char] == 1: return i
    return -1
print(first_unique("swiss"))  # 1
# 6. Group by department
groups = defaultdict(list)
for name, dept in [("Asha","IT"),("Ravi","HR"),("Maya","IT")]:
    groups[dept].append(name)
print(dict(groups))
# 7. Detect duplicates
def has_duplicate(values): return len(values) != len(set(values))
print(has_duplicate([1,2,1]))  # True
```
**Real-world use:** Deduplicate imports, count events, group employees and match transactions.
### Seven interview Q&A
1. **Hashing?** Maps keys to hash values used to locate entries.
2. **Why average O(1)?** Hash tables usually inspect a small candidate set; collisions/resizing affect details.
3. **Hashable key?** Stable hash and consistent equality; lists are unhashable.
4. **Two Sum approach?** Store seen values/indices and look up each complement.
5. **Collision?** Different keys map to the same hash/bucket; implementation resolves it.
6. **Why set?** Unique values and efficient membership.
7. **Two Sum space?** O(n) worst-case dictionary storage.
### Five practice tasks
1. Frequency count: use `frequencies`. 2. Two Sum: use `two_sum`. 3. Duplicates: use `has_duplicate`. 4. First unique char: use `first_unique`. 5. Group employees with `defaultdict(list)`.

## 4. Sliding window, prefix sums and binary search
**Definition:** Sliding windows update a contiguous range incrementally; prefix sums store cumulative totals; binary search halves a sorted candidate range.
### Seven complete examples
```python
# 1. Maximum sum of fixed window
def max_window_sum(nums, k):
    if k <= 0 or k > len(nums): raise ValueError("Invalid window size")
    window = sum(nums[:k]); best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right-k]
        best = max(best, window)
    return best
print(max_window_sum([2,1,5,1,3,2], 3))  # 9

# 2. Longest substring without repeats
def longest_unique_length(text):
    last = {}; left = best = 0
    for right, char in enumerate(text):
        if char in last and last[char] >= left: left = last[char] + 1
        last[char] = right
        best = max(best, right-left+1)
    return best
print(longest_unique_length("abcabcbb"))  # 3

# 3. Prefix sums
def prefix_sums(values):
    out = [0]
    for value in values: out.append(out[-1] + value)
    return out
print(prefix_sums([2,4,6]))  # [0,2,6,12]

# 4. Inclusive range sum
prefix = prefix_sums([2,4,6,8])
print(prefix[3+1] - prefix[1])  # 18

# 5. Binary search
def binary_search(values, target):
    left, right = 0, len(values)-1
    while left <= right:
        mid = left + (right-left)//2
        if values[mid] == target: return mid
        if values[mid] < target: left = mid+1
        else: right = mid-1
    return -1
print(binary_search([1,3,5,7,9], 7))  # 3

# 6. Lower bound: first index with value >= target
def lower_bound(values, target):
    left, right = 0, len(values)
    while left < right:
        mid = (left+right)//2
        if values[mid] < target: left = mid+1
        else: right = mid
    return left
print(lower_bound([1,3,3,5], 3))  # 1

# 7. Matrix total; for many rectangle queries use a 2D prefix table
matrix = [[1,2],[3,4]]
print(sum(sum(row) for row in matrix))  # 10
```
**Real-world use:** Rolling traffic/sales metrics, date-range totals and lookup in sorted catalogues.
### Seven interview Q&A
1. **When use sliding window?** Contiguous subarray/substring problems with incrementally updateable state.
2. **Fixed vs variable window?** Known length versus expanding/shrinking range.
3. **Why often O(n)?** Each pointer typically moves forward at most n times.
4. **Prefix sum?** Cumulative totals answer range sums by subtraction.
5. **Why sorted input for binary search?** Ordering permits safe elimination of half the candidates.
6. **Binary-search invariant?** The target, if present, remains in the candidate interval.
7. **Duplicates?** Specify any match, first match or insertion position before coding.
### Five practice tasks
1. Fixed maximum window: use `max_window_sum`.
2. Longest unique substring: use `longest_unique_length`.
3. Prefix sums: use `prefix_sums`.
4. Sorted search: use `binary_search`.
5. First index >= target: use `lower_bound`.

## 5. Stack, queue, recursion, trees and graphs
**Definition:** Stack is LIFO, queue is FIFO; recursion solves smaller subproblems; BFS visits by layers and DFS explores deeply before backtracking.
### Seven complete examples
```python
# 1. Stack
stack = []; stack.append("page-1"); stack.append("page-2")
print(stack.pop())  # page-2

# 2. Balanced brackets
def balanced(text):
    stack = []; pairs = {")":"(", "]":"[", "}":"{"}
    for char in text:
        if char in "([{": stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]: return False
    return not stack
print(balanced("{[()]}"))  # True

# 3. Queue
from collections import deque
queue = deque(["job-1","job-2"])
print(queue.popleft())  # job-1

# 4. Recursion
def factorial(n):
    if n < 0: raise ValueError("n must be non-negative")
    if n <= 1: return 1
    return n * factorial(n-1)
print(factorial(5))  # 120

# 5. BFS
def bfs(graph, start):
    visited, queue, order = {start}, deque([start]), []
    while queue:
        node = queue.popleft(); order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                visited.add(nxt); queue.append(nxt)
    return order
graph = {"A":["B","C"],"B":["D"],"C":[],"D":[]}
print(bfs(graph,"A"))  # ['A','B','C','D']

# 6. DFS
def dfs(graph, start):
    visited, order = set(), []
    def visit(node):
        if node in visited: return
        visited.add(node); order.append(node)
        for nxt in graph.get(node, []): visit(nxt)
    visit(start); return order
print(dfs({"A":["B"],"B":["A"]},"A"))  # ['A','B']

# 7. Tree preorder
class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right
def preorder(node):
    if node is None: return []
    return [node.value] + preorder(node.left) + preorder(node.right)
print(preorder(Node(1, Node(2), Node(3))))  # [1,2,3]
```
**Real-world use:** Undo history, job queues, shortest paths in unweighted networks, dependency traversal and hierarchical data.
### Seven interview Q&A
1. **Stack vs queue?** LIFO vs FIFO.
2. **Why deque?** Efficient front removal; list.pop(0) shifts remaining elements.
3. **Recursion base case?** Stops further recursive calls.
4. **Recursion risk in Python?** Deep calls can hit recursion limit; iterative solutions may be safer.
5. **BFS vs DFS?** BFS explores layers and finds shortest edge-count path in unweighted graphs; DFS explores deeply.
6. **Why visited set?** Prevents repeated work and infinite traversal through cycles.
7. **BFS/DFS complexity?** O(V+E) with adjacency lists.
### Five practice tasks
1. Reverse text using a stack:
```python
def reverse_text(text):
    stack, result = list(text), []
    while stack: result.append(stack.pop())
    return "".join(result)
print(reverse_text("python"))  # nohtyp
```
2. Balanced brackets: use `balanced`. 3. FIFO queue: use `deque`. 4. Factorial: use `factorial`. 5. Graph traversal: use BFS/DFS.

## Project: support-ticket priority queue
**Question:** How would you repeatedly retrieve the highest-priority ticket while new tickets arrive?
**Professional answer:** Use a heap rather than re-sorting the whole collection each time. Python's heapq is a min-heap, so negate priority for max-priority behaviour. Add a sequence number to break ties deterministically.
```python
import heapq
from itertools import count
class TicketQueue:
    def __init__(self):
        self._heap = []; self._sequence = count()
    def add(self, ticket_id, priority):
        heapq.heappush(self._heap, (-priority, next(self._sequence), ticket_id))
    def next_ticket(self):
        if not self._heap: raise IndexError("No tickets available")
        priority, _, ticket_id = heapq.heappop(self._heap)
        return {"ticket_id":ticket_id, "priority":-priority}
q = TicketQueue()
q.add("INC-101", 2); q.add("INC-102", 5); q.add("INC-103", 5)
print(q.next_ticket())  # highest priority INC-102
```
**Complexity:** insert O(log n), pop O(log n), peek O(1). **Follow-ups:** How handle ties? Sequence counter. How update priority? Lazy invalidation or indexed priority queue. What production work remains? Persistence, concurrency controls, audit logs, retries and monitoring.
