# DSA — Code, Explanation, Complexity and Real-World Use

Data Structures and Algorithms (DSA) is a separate track from Python core and OOP. Examples below are compact implementations intended for learning. Complexity is stated for the usual case and may depend on assumptions.

## 1. Big-O and linear search

**Definition:** Time complexity describes how runtime grows with input size; space complexity describes extra memory use.

```python
def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

print(linear_search([4, 8, 2], 8))  # 1
```

**Explanation:** Inspect values from left to right and return the first matching index. Worst-case time O(n); auxiliary space O(1).

**Real-world use:** Find a record in a small unsorted list.

## 2. Arrays/lists and in-place operations

```python
def reverse_in_place(values):
    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return values

print(reverse_in_place([1, 2, 3, 4]))  # [4, 3, 2, 1]
```

**Explanation:** Swap the two ends, then move both pointers inward. Time O(n), extra space O(1).

**Real-world use:** Rearranging an array without allocating a second array.

## 3. Strings and palindrome check

```python
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
```

**Explanation:** Normalise to lowercase alphanumeric characters, then compare with the reversed string. Time O(n), extra space O(n) for the cleaned string.

**Real-world use:** Text checks where punctuation and letter case should not affect the result.

## 4. Hash maps, sets and Two Sum

```python
def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], index]
        seen[value] = index
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

**Explanation:** For each number, check whether its complement has appeared. Store each value and its index. Expected time O(n), extra space O(n).

**Real-world use:** Match transactions, identify pairs that satisfy a total, or count repeated log events.

## 5. Two pointers

```python
def has_pair_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return True
        if current < target:
            left += 1
        else:
            right -= 1
    return False

print(has_pair_sum_sorted([1, 2, 4, 6, 9], 10))  # True
```

**Explanation:** This requires sorted input. If the sum is too small, move the left pointer up; if too large, move the right pointer down. Time O(n), extra space O(1).

**Real-world use:** Find two sorted prices that fit a budget.

## 6. Sliding window

```python
def max_window_sum(nums, k):
    if k < 1 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    current = sum(nums[:k])
    best = current
    for right in range(k, len(nums)):
        current += nums[right] - nums[right - k]
        best = max(best, current)
    return best

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))  # 9
```

**Explanation:** Compute the first window, then add the entering value and subtract the leaving value. Time O(n), extra space O(1).

**Real-world use:** Highest sales total over k consecutive days or average traffic in a fixed time window.

## 7. Prefix sums

```python
def build_prefix(nums):
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)
    return prefix

nums = [2, 4, 6, 8]
prefix = build_prefix(nums)
left, right = 1, 2  # inclusive indexes in nums
print(prefix[right + 1] - prefix[left])  # 10
```

**Explanation:** Each prefix entry stores the sum before that position. A range sum is the prefix at the end minus the prefix before the start. Build O(n); each range query O(1); extra space O(n).

**Real-world use:** Repeated range-sum queries over daily sales or sensor readings.

## 8. Binary search

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 7))  # 3
```

**Explanation:** The list must be sorted. Each comparison discards about half the remaining search interval. Time O(log n), extra space O(1).

**Real-world use:** Search sorted records or find a threshold in a monotonic condition.

## 9. Recursion

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:              # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

**Explanation:** Each call reduces the problem size. The base case stops recursion. Time O(n), call-stack space O(n).

**Real-world use:** Tree traversal and naturally recursive structures. For large depth, consider iteration to avoid recursion limits.

## 10. Stack

```python
def valid_parentheses(text):
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
    return not stack

print(valid_parentheses("{[()]}"))  # True
print(valid_parentheses("([)]"))    # False
```

**Explanation:** A stack is Last In, First Out (LIFO). The latest opening bracket must be the first one matched. Time O(n), extra space O(n).

**Real-world use:** Syntax checking, undo operations, nested expressions and browser history.

## 11. Queue and breadth-first search (BFS)

```python
from collections import deque

def bfs_distances(graph, start):
    distances = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, []):
            if neighbour not in distances:
                distances[neighbour] = distances[node] + 1
                queue.append(neighbour)
    return distances

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
print(bfs_distances(graph, "A"))
```

**Explanation:** A queue is First In, First Out (FIFO). BFS visits nodes in layers; for an unweighted graph, its distances give shortest path lengths. Time O(V + E) using an adjacency list.

**Real-world use:** Minimum number of connections in a network or shortest route by number of stops.

## 12. Trees and heaps

```python
import heapq

values = [4, 1, 9, 2, 7]
heap = []
for value in values:
    heapq.heappush(heap, value)
print(heapq.heappop(heap))  # 1
print(heapq.nlargest(3, values))  # [9, 7, 4]
```

**Explanation:** Python's `heapq` implements a min-heap; the smallest value is at the root. Push/pop are O(log n); reading the minimum is O(1). A heap is not a fully sorted list.

**Real-world use:** Job scheduling, priority queues and top-k queries. Trees also model folders, organisation charts and nested data.

## 13. Graphs: depth-first search

```python
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                stack.append(neighbour)
    return visited

graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
print(sorted(dfs(graph, "A")))
```

**Explanation:** DFS uses a stack to explore deeper nodes first. The visited set prevents repeated processing. Time O(V + E) with an adjacency list.

**Real-world use:** Dependency exploration, connected components, reachability and maze traversal.

## 14. Greedy algorithms

```python
def greedy_coin_count(amount, coins=(25, 10, 5, 1)):
    if amount < 0:
        raise ValueError("amount must be non-negative")
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count

print(greedy_coin_count(41))  # 4 coins: 25 + 10 + 5 + 1
```

**Explanation:** At each step choose as many as possible of the largest denomination. This works for the listed canonical coin system, but greedy is not optimal for every possible denomination system or every problem. Time O(number of denominations).

**Real-world use:** Some scheduling and selection problems, when a correctness argument proves the local choice is safe.

## 15. Dynamic programming (DP)

```python
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous

print(fibonacci(10))  # 55
```

**Explanation:** Each iteration reuses the two previous results instead of recomputing recursive branches. Time O(n), extra space O(1). For more complex DP, define the state, base cases and transition before coding.

**Real-world use:** Optimisation, sequence problems, planning and resource-allocation problems with overlapping subproblems.

## 16. Bit manipulation

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False
```

**Explanation:** A positive power of two has exactly one set bit. Subtracting one flips that bit and all lower bits; the bitwise AND becomes zero.

**Real-world use:** Flags, permissions, low-level data processing and interview problems involving binary representations.

## Pattern recognition: which tool should I try?

- Need counts, duplicates or complement lookup → dictionary/set.
- Sorted sequence and pair condition → two pointers.
- Contiguous segment → sliding window or prefix sums; check input constraints.
- Sorted list or monotonic condition → binary search.
- Nested or last-in-first-out work → stack.
- Level order or unweighted shortest path → queue/BFS.
- Explore all reachable states → DFS/BFS with visited tracking.
- Repeated optimal subproblems → consider dynamic programming.
- Repeated smallest/largest extraction → heap.
- Enumerate combinations and undo choices → backtracking.

## Practice rule

For each problem: explain the brute-force approach, identify the pattern, write code, dry-run a sample, state time/space complexity, and test empty input, duplicates and boundaries where relevant. A technique is not correct unless its assumptions match the problem.
