"""Runnable starter implementations for common DSA patterns.
Run: python dsa/examples.py
"""

from collections import Counter, deque
import heapq

# 1. Complexity, linear search
def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

print("1. Linear search:", linear_search([4, 8, 2], 8))  # O(n)

# 2. Arrays/lists: maximum and reverse
def reverse_in_place(values):
    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return values

print("2. Reverse:", reverse_in_place([1, 2, 3, 4]))

# 3. Strings: palindrome normalised to letters/digits
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print("3. Palindrome:", is_palindrome("A man, a plan, a canal: Panama"))

# 4. Hashing: Two Sum and frequency counts
def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], index]
        seen[value] = index
    return []

print("4. Two Sum:", two_sum([2, 7, 11, 15], 9))
print("Frequencies:", dict(Counter("banana")))

# 5. Two pointers: sorted pair sum
def has_pair_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False

print("5. Pair sum:", has_pair_sum_sorted([1, 2, 4, 6, 9], 10))

# 6. Sliding window: maximum sum of k consecutive elements
def max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    current = sum(nums[:k])
    best = current
    for right in range(k, len(nums)):
        current += nums[right] - nums[right - k]
        best = max(best, current)
    return best

print("6. Sliding window:", max_window_sum([2, 1, 5, 1, 3, 2], 3))

# 7. Prefix sums and range sum [left, right]
def prefix_sums(nums):
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)
    return prefix

nums = [2, 4, 6, 8]
prefix = prefix_sums(nums)
print("7. Range sum indexes 1..2:", prefix[3] - prefix[1])

# 8. Binary search: input must be sorted
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

print("8. Binary search:", binary_search([1, 3, 5, 7, 9], 7))

# 9. Recursion
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("9. Factorial:", factorial(5))

# 10. Stack: balanced parentheses
def valid_parentheses(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

print("10. Stack:", valid_parentheses("{[()]}"))

# 11. Queue/BFS: shortest distance in an unweighted graph
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
print("11. BFS distances:", bfs_distances(graph, "A"))

# 12. Heap: k largest values
def k_largest(nums, k):
    if k < 0 or k > len(nums):
        raise ValueError("k out of range")
    return heapq.nlargest(k, nums)

print("12. Heap top 3:", k_largest([4, 1, 9, 2, 7], 3))

# 13. Dynamic programming: Fibonacci with tabulation
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("13. Fibonacci:", fibonacci(10))

# 14. Greedy: minimum number of standard coins for canonical denominations
def greedy_coin_count(amount, coins=(25, 10, 5, 1)):
    if amount < 0:
        raise ValueError("amount must be non-negative")
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count

print("14. Greedy coin count for 41:", greedy_coin_count(41))

# 15. Bit manipulation
n = 16
print("15. Is power of two:", n > 0 and (n & (n - 1)) == 0)
