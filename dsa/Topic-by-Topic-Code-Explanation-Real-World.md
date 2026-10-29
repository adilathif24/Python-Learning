# DSA — Code, Explanation, Complexity and Real-World Use


> **Professional interview preparation:** For structured syntax, complete code examples, interview-ready explanations, seven solved interview Q&As and five practice tasks with solutions, also use the [Professional Interview Workbook](dsa/Professional-Interview-Workbook.md).

This guide develops DSA from pattern foundations to interview-ready solutions. For each problem, practise the approach, assumptions, correctness, complexity, dry run and edge cases. DSA remains a separate learning track from Python Core and OOP.

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


---

# Interview-Ready DSA: Explain the Approach Before the Code

The examples above introduce common patterns. In a technical interview, a complete solution should include requirement clarification, a baseline approach, optimisation reasoning, complexity analysis, and edge-case tests.

## Worked interview problem: Two Sum

**Problem:** Return the indices of two distinct elements whose values sum to the target. Return an empty list if no solution exists.

### Baseline approach
Check every pair. This is O(n²) time and O(1) auxiliary space. It is easy to explain, but slow for large inputs.

### Optimised approach

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    index_by_value: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in index_by_value:
            return [index_by_value[complement], index]
        index_by_value[value] = index

    return []


def run_examples() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 20) == []
    assert two_sum([], 0) == []
    print("All Two Sum examples passed.")


if __name__ == "__main__":
    run_examples()
```

**Expected output:** `All Two Sum examples passed.`

### How to explain the optimisation
“I use a dictionary to store values I have already visited and their indices. For each current value, I calculate the complement required to reach the target. If that complement is already present, I return the two indices; otherwise, I store the current value. This reduces expected time from O(n²) to O(n), at the cost of O(n) additional space.”

### Important edge case
The lookup happens before inserting the current value. That prevents a single element from being used twice. Duplicate values are handled because the dictionary can contain the first occurrence before the second is processed.

## Interview answer framework for every DSA problem

1. **Clarify:** Are inputs sorted? Can values repeat? What should happen if there is no answer? Are indices or values required?
2. **Baseline:** State the simplest correct solution and its complexity.
3. **Pattern:** Explain why hashing, two pointers, a sliding window, BFS, a heap or DP fits the constraints.
4. **Invariant:** Describe what remains true during each iteration.
5. **Code:** Use descriptive names, clear branches and explicit edge-case behaviour.
6. **Dry run:** Walk through one normal example and one edge case.
7. **Complexity:** Analyse time and auxiliary space; mention assumptions.
8. **Tests:** Include empty input, one element, duplicates, boundaries and no-solution cases where applicable.
9. **Trade-offs:** Explain what extra memory or assumptions the optimisation requires.

## Professional DSA follow-up questions

- **Why is binary search O(log n)?** Each iteration reduces the remaining search interval by approximately half; it requires sorted data or another monotonic property.
- **When does sliding window apply?** Usually to a contiguous range when the window can be updated incrementally. Variable-size windows often rely on a condition that can be maintained as pointers move.
- **BFS vs DFS?** BFS explores by distance layers and finds shortest paths in unweighted graphs; DFS explores deeply and is useful for reachability, components and backtracking.
- **Greedy vs dynamic programming?** Greedy commits to a locally chosen option and needs a proof that this choice is safe. DP evaluates reusable states and transitions when subproblems overlap.
- **What does O(n) space mean?** Additional memory grows proportionally to input size; clarify whether the analysis includes output storage.

## Quality bar for interview solutions

A passing example is not enough. Make the assumptions explicit, use clear function contracts, test edge cases, and be ready to justify the complexity and trade-offs. Do not claim that every algorithm is optimal for every input; state the conditions under which the approach is correct.