# DSA — Beginner to Advanced Roadmap and Interview Guide

This track is separate from Python fundamentals and OOP. For each topic, study definition, explanation, real-world use, when/where/how to apply it, seven examples/questions with answers, and tasks.

> AI assistance helped organise these notes. Run the examples, test edge cases and solve new variations independently.

## A repeatable DSA problem-solving method
1. Restate the problem and constraints.
2. Dry-run a small example by hand.
3. Identify edge cases: empty input, one item, duplicates, negative values and missing results where relevant.
4. Write a simple correct solution before optimising.
5. Trace variables, test the code and explain time/space complexity.
6. Explain why the chosen pattern works and when it would not work.

## 1. Complexity analysis
**Definition:** Time complexity describes how operation counts grow with input size; space complexity describes memory usage.
**Explanation:** Common growth rates are O(1), O(log n), O(n), O(n log n), O(n²) and O(2^n).
**Real world:** Compare scanning a million records with repeated hash lookups.
**When/how:** Count dominant operations and state assumptions.
**Seven Q&A:** 1) Array index access? O(1). 2) One scan? O(n). 3) Two full nested loops? O(n²). 4) Halving a range? O(log n). 5) Merge-sort time? O(n log n). 6) Extra list of n items? O(n) space. 7) Is O(n) always faster on tiny input? Not necessarily; constants matter.
**Tasks:** Analyse one loop, nested loops and binary search.

## 2. Arrays and Python lists
**Definition:** An array stores indexed values; Python lists are dynamic arrays of object references.
**Explanation:** Index access O(1), search O(n), append amortised O(1), front insertion usually O(n).
**Real world:** Store scores, temperatures or product prices.
**When/how:** Use for ordered items and index-based processing.
**Seven Q&A:** 1) First item? arr[0], if non-empty. 2) Last item? arr[-1], if non-empty. 3) Append? arr.append(x). 4) Find largest? One scan, O(n). 5) Reverse in place? arr.reverse(). 6) Reversed copy? arr[::-1]. 7) Deduplicate while preserving order? Use a seen set and result list.
**Example:**
    def largest(arr):
        if not arr:
            raise ValueError("empty input")
        best = arr[0]
        for value in arr[1:]:
            if value > best:
                best = value
        return best
**Tasks:** Second largest, move zeroes, rotate by k, merge sorted lists.

## 3. Strings
**Definition:** A string is an immutable sequence of Unicode characters.
**Explanation:** Many problems need a scan, frequency count or two pointers.
**Real world:** Validate identifiers, parse logs, normalise input.
**When/how:** Clarify case, spaces, punctuation and Unicode rules.
**Seven Q&A:** 1) Reverse? text[::-1]. 2) Palindrome? Compare normalised text with reverse. 3) Count characters? len() or frequency map. 4) First unique character? Count then scan in original order. 5) Anagram? Compare frequencies after normalisation. 6) Remove literal spaces? replace(" ", ""). 7) Why immutable? Contents cannot change in place.
**Example:**
    def is_palindrome(text):
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]
**Tasks:** Character frequency, first unique character, anagram, longest common prefix.

## 4. Hashing: dictionaries and sets
**Definition:** Hash tables map hashable keys to values or track unique values.
**Explanation:** Membership is expected O(1) average; keys must be hashable.
**Real world:** Look up users, count events, remove duplicates, find pair sums.
**When/how:** Use when repeated membership checks or frequency counting dominate.
**Seven Q&A:** 1) Count frequencies? Dictionary. 2) Repeated membership? Set/dict. 3) Unordered deduplication? Set. 4) Preserve order? Seen set plus result list. 5) Two Sum? Store prior values and indexes. 6) Can list be a dict key? No, unhashable. 7) Why set? Unique values and efficient average membership.
**Example:**
    def two_sum(nums, target):
        seen = {}
        for i, value in enumerate(nums):
            needed = target - value
            if needed in seen:
                return [seen[needed], i]
            seen[value] = i
        return None
**Tasks:** First repeated value, group anagrams, word counts, array intersection.

## 5. Two pointers
**Definition:** Two indexes scan a sequence, often from opposite ends or at different speeds.
**Explanation:** Sorted data can let a pointer move based on comparison.
**Real world:** Find two sorted prices that match a budget.
**When/how:** Look for sorted pair searches, palindromes and in-place rearrangement.
**Seven Q&A:** 1) Reverse list? Swap ends inward. 2) Palindrome? Compare both ends. 3) Sorted pair sum? Move pointer according to sum. 4) Sorted deduplication? Write pointer. 5) Move zeroes? Write nonzero values then fill rest. 6) Merge sorted lists? Advance the pointer with smaller value. 7) Always O(n)? No; it depends on pointer movement and nested work.
**Example:**
    def has_pair_sum(nums, target):
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
**Tasks:** Pair sum, palindrome, sorted deduplication, move zeroes.

## 6. Sliding window
**Definition:** Maintain a contiguous range while moving its boundaries.
**Explanation:** Fixed windows update a running result; variable windows expand/shrink when a condition changes. Some patterns assume non-negative values.
**Real world:** Busiest seven-day period or longest substring satisfying a rule.
**When/how:** Look for contiguous subarray/substring and fixed/longest/shortest range.
**Seven Q&A:** 1) Sum each size-k window? Add entering, subtract leaving. 2) Max sum of k? Track maximum. 3) Average of k? Window sum/k. 4) Longest unique substring? Track last-seen positions. 5) Minimum sum threshold? Shrinking window works for positive/non-negative values; negatives complicate it. 6) Why often O(n)? Each boundary advances at most n times. 7) Every subarray problem? No.
**Example:**
    def max_window_sum(nums, k):
        if k <= 0 or k > len(nums):
            raise ValueError("invalid window size")
        current = sum(nums[:k])
        best = current
        for right in range(k, len(nums)):
            current += nums[right] - nums[right-k]
            best = max(best, current)
        return best
**Tasks:** Maximum window sum, averages, longest unique substring.

## 7. Prefix sums
**Definition:** Store cumulative sums to answer range sums efficiently.
**Explanation:** If prefix[i] sums values before i, range l..r equals prefix[r+1] - prefix[l].
**Real world:** Repeated totals across date ranges.
**When/how:** Useful for many queries on unchanged data.
**Seven Q&A:** 1) Build? Start with zero, append cumulative totals. 2) Sum indexes 1..3? prefix[4]-prefix[1]. 3) Preprocess? O(n). 4) Range query? O(1). 5) Fast arbitrary updates automatically? No. 6) Negative values allowed? Yes. 7) Common bug? Off-by-one.
**Example:**
    def build_prefix(nums):
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        return prefix

    def range_sum(prefix, left, right):
        return prefix[right + 1] - prefix[left]
**Tasks:** Multiple range sums and count subarrays with target sum.

## 8. Sorting and binary search
**Definition:** Sorting arranges values; binary search halves a sorted search range.
**Explanation:** sorted() returns a new list; list.sort() mutates it. Binary search requires sorted input or a monotonic predicate.
**Real world:** Search catalogues or find the first threshold crossing.
**When/how:** Maintain a clear search invariant and check boundary conditions.
**Seven Q&A:** 1) Ascending sort? sorted(values). 2) In-place sort? values.sort(). 3) Descending? sorted(values, reverse=True). 4) Search sorted data? Binary search O(log n). 5) Search unsorted data once? Linear search may be simpler. 6) First occurrence? Continue left after match. 7) Binary search unsorted data? Not reliable.
**Example:**
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
**Tasks:** Lower bound, first/last occurrence, search insert position.

## 9. Recursion and backtracking
**Definition:** Recursion solves smaller versions of a problem; backtracking explores choices and undoes them.
**Explanation:** Recursion needs a base case and progress. Backtracking uses choose, explore, unchoose.
**Real world:** Generate schedules, combinations, permutations or maze paths.
**When/how:** Use for naturally recursive structures or search spaces; consider Python's recursion limit.
**Seven Q&A:** 1) Factorial? n * factorial(n-1), with base case. 2) Base case? Terminates recursion. 3) Call stack? Active calls. 4) Subsets? Include/exclude. 5) Permutations? Choose, recurse, undo. 6) Backtracking? Reverse choices before alternatives. 7) Always best? No, iteration may be clearer.
**Example:**
    def factorial(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        if n <= 1:
            return 1
        return n * factorial(n - 1)
**Tasks:** Subsets, permutations, balanced parentheses.

## 10. Linked lists, stacks and queues
**Definition:** Linked lists connect nodes; stack is LIFO; queue is FIFO.
**Explanation:** Use a Python list as a stack and collections.deque as a queue. Linked lists teach pointer/reference manipulation.
**Real world:** Undo history (stack), job scheduling (queue).
**When/how:** Choose based on operations; don't implement linked lists when list/deque is simpler.
**Seven Q&A:** 1) Push? append(). 2) Pop? pop(). 3) Enqueue? deque.append(). 4) Dequeue? deque.popleft(). 5) LIFO? Last in, first out. 6) FIFO? First in, first out. 7) Detect linked-list cycle? Floyd slow/fast pointers.
**Example:**
    stack = []
    stack.append("page1")
    stack.append("page2")
    print(stack.pop())  # page2
**Tasks:** Valid parentheses, queue with two stacks, reverse list, cycle detection.

## 11. Trees and binary search trees
**Definition:** Trees are hierarchical structures; a binary tree node has at most two children; a BST orders keys by a rule.
**Explanation:** DFS traversals are preorder, inorder, postorder; BFS visits level by level. Unbalanced BSTs can degrade to O(n).
**Real world:** File hierarchy, organisation charts, syntax trees.
**When/how:** Use for hierarchy and ordered search; choose traversal for the required output.
**Seven Q&A:** 1) Preorder? Root-left-right. 2) Inorder? Left-root-right. 3) Postorder? Left-right-root. 4) BFS? Queue. 5) Height? Longest root-to-leaf path under chosen convention. 6) Every BST balanced? No. 7) Inorder of valid BST? Sorted keys.
**Example:**
    def inorder(node):
        if node is None:
            return []
        return inorder(node.left) + [node.value] + inorder(node.right)
**Tasks:** Preorder, BFS, height, BST search, validate BST.

## 12. Heaps and priority queues
**Definition:** A heap efficiently exposes the highest-priority item; heapq provides a min-heap.
**Explanation:** Push/pop O(log n), minimum peek O(1); a heap is not fully sorted.
**Real world:** Job scheduling, top-k, merging sorted streams.
**When/how:** Use when repeatedly extracting the next smallest/largest item.
**Seven Q&A:** 1) Build? heapq.heapify(). 2) Insert? heappush(). 3) Remove smallest? heappop(). 4) Peek? heap[0]. 5) k smallest? heapq.nsmallest(). 6) Fully sorted? No. 7) Priority queue? Removes by priority.
**Example:**
    import heapq
    values = [7, 2, 9, 1]
    heapq.heapify(values)
    print(heapq.heappop(values))  # 1
**Tasks:** kth largest, merge sorted lists, running median.

## 13. Graphs
**Definition:** Graphs contain vertices and edges; edges can be directed/undirected and weighted/unweighted.
**Explanation:** Adjacency lists suit sparse graphs. BFS finds shortest paths in unweighted graphs. Dijkstra assumes non-negative edge weights.
**Real world:** Roads, social networks, task dependencies.
**When/how:** Identify direction, weights, cycles and graph size before choosing representation.
**Seven Q&A:** 1) Sparse representation? Adjacency list. 2) Level traversal? BFS. 3) Deep exploration? DFS. 4) Unweighted shortest path? BFS. 5) Dijkstra with negative edges? Not safe. 6) Cycle? Path returning to a visited vertex under graph rules. 7) Visited set? Avoid repeated/infinite traversal.
**Example:**
    from collections import deque

    def bfs(graph, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return order
**Tasks:** Connected components, reachability, unweighted shortest path, cycle detection.

## 14. Greedy algorithms
**Definition:** Greedy chooses a locally attractive option at each step.
**Explanation:** Correctness needs a property/proof; a plausible local choice is not enough.
**Real world:** Activity selection can choose the compatible activity with earliest finish time.
**When/how:** State the rule and justify why it can be part of an optimal solution.
**Seven Q&A:** 1) Greedy? Locally optimal choice. 2) Always optimal? No. 3) Activity selection? Earliest finish is a standard optimal rule. 4) Fractional knapsack? Value/weight ratio is optimal with fractions. 5) 0/1 knapsack with same rule? Not generally. 6) Why prove? Local choices may block global optimum. 7) How test? Seek counterexamples and prove correctness.
**Tasks:** Interval scheduling, fractional knapsack, coin change; identify counterexamples.

## 15. Dynamic programming
**Definition:** DP solves overlapping subproblems and reuses their results.
**Explanation:** Top-down uses memoization; bottom-up fills a table. Define state, transition, base cases and order.
**Real world:** Budget optimisation, sequence comparison, resource allocation.
**When/how:** Look for repeated subproblems and optimal substructure; define dp[i] before coding.
**Seven Q&A:** 1) Fibonacci DP? Store previous results. 2) Memoization? Cache recursive results. 3) Tabulation? Fill table upward. 4) State? Subproblem representation. 5) Transition? Relation between states. 6) Can DP reduce exponential recursion? Often, when distinct states are fewer. 7) Define first? State, base cases, recurrence.
**Example:**
    def fibonacci(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        if n < 2:
            return n
        previous, current = 0, 1
        for _ in range(2, n + 1):
            previous, current = current, previous + current
        return current
**Tasks:** Climbing stairs, coin change, house robber, longest common subsequence, 0/1 knapsack.

## 16. Tries, DSU and range-query structures
**Definition:** Tries store prefixes; Disjoint Set Union tracks components; Fenwick and segment trees support range queries/updates.
**Explanation:** DSU with path compression and union by size/rank has near-constant amortised operations. Fenwick supports prefix sums and point updates; segment trees support flexible range operations.
**Real world:** Autocomplete, connected accounts, dynamic range sums.
**When/how:** Learn after arrays, hashing and trees; use when required operations justify complexity.
**Seven Q&A:** 1) Trie? Prefix search. 2) DSU? Dynamic connectivity. 3) find(x)? Set representative. 4) union(a,b)? Merge sets. 5) Fenwick? Prefix sums and point updates. 6) Segment tree? Flexible range queries. 7) Start here as beginner? No.
**Tasks:** Implement a trie, DSU and Fenwick tree.

## 17. Bit manipulation and advanced backtracking
**Definition:** Bit manipulation works with binary representations; backtracking explores choices and prunes invalid branches.
**Explanation:** Operators include &, |, ^, ~, << and >>. Write a small binary example before applying a bit trick.
**Real world:** Permission flags, compact state and constraint puzzles.
**When/how:** Define choices/constraints and prune impossible branches; check integer assumptions.
**Seven Q&A:** 1) Parity for non-negative n? n & 1. 2) Clear lowest set bit? n & (n-1), for positive n. 3) Power of two? n > 0 and (n & (n-1)) == 0. 4) Subsets? Include/exclude. 5) Permutations? Choose and recurse. 6) Pruning? Stop exploring impossible branches. 7) Bitmask? Bits representing flags/choices.
**Tasks:** Subsets, N-Queens, combinations, bit operations.

## 18. Recognising interview patterns
**Definition:** A pattern is a reusable approach that fits a family of problems.
**Explanation:** Constraints and input properties guide the approach.
**Real world:** Interviews assess reasoning, implementation, testing and trade-offs.
**When/how:** Explain why the pattern applies and its limitations.
**Seven Q&A:** 1) Pair condition and repeated lookup? Hash map. 2) Sorted pair search? Two pointers. 3) Contiguous range? Sliding window or prefix sum. 4) Sorted input/monotonic predicate? Binary search. 5) Nested matching/LIFO? Stack. 6) Level traversal/unweighted shortest path? BFS. 7) Overlapping subproblems? Dynamic programming.

## Practice by level
**Beginner:** largest/second-largest; reverse string; palindrome; frequencies; Two Sum; linear/binary search; valid parentheses.
**Intermediate:** merge intervals; longest unique substring; rotated-array search; reverse linked list; tree traversals; top-k frequency; connected components.
**Advanced:** backtracking word search; coin change; longest common subsequence; Dijkstra for non-negative edges; minimum spanning tree; trie; segment/Fenwick tree; DSU.

## Required workflow for every topic
1. Learn definition and intuition.
2. Dry-run a small input by hand.
3. Write a basic solution.
4. Complete the seven questions/examples in the phase.
5. Solve three unseen variations without copying.
6. Test boundaries and invalid inputs.
7. Explain time and space complexity.
8. Record mistakes and revisit later.

**Portfolio honesty:** This is a structured roadmap and starter guide, not a claim that every advanced topic is mastered. The repository becomes more credible when you add runnable files and tests for solutions you personally verified.
