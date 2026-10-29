# Data Structures and Algorithms (DSA) — Beginner to Advanced

This is a separate track from Python Core Concepts and OOP. Examples use Python. Each phase gives definition, explanation, real-world use, when/where/how, seven example questions with answers, and tasks.

## Standard problem-solving method
1. Restate the problem and confirm input/output.
2. Clarify constraints and edge cases.
3. Dry-run a small example by hand.
4. Write a simple correct approach first.
5. Improve only after understanding the baseline.
6. Test empty, single-item, duplicate, boundary and invalid inputs where relevant.
7. Explain time and space complexity.

## 1. Complexity analysis
**Definition:** Time complexity describes how work grows with input size; space complexity describes memory usage. Big O describes asymptotic growth/upper bounds.
**Real-world example:** Repeatedly scanning a huge customer list may be slower than indexing customers by ID.
**When/where/how:** Count dominant operations and state assumptions before comparing approaches.
### Seven Q&A
1. **Array index lookup?** O(1) for Python lists.
2. **Scan n items once?** O(n).
3. **Two nested loops over n?** Usually O(n²).
4. **Halve search space repeatedly?** O(log n).
5. **Typical comparison sort?** O(n log n).
6. **Store a second n-item list?** O(n) extra space.
7. **Is O(n) always faster for tiny input?** Not necessarily; constants and input size matter.
**Tasks:** Analyse a linear scan, nested loop and binary search.

## 2. Arrays and Python lists
**Definition:** An array stores indexed elements; Python list is a dynamic array of object references.
**Explanation:** Index access O(1); search O(n); append amortised O(1); front insertion typically O(n).
**Real-world example:** Store temperatures, scores or cart items.
**When/where/how:** Use for ordered, indexable data. Choose another structure if frequent front operations dominate.
### Seven Q&A/examples
1. **Read first?** arr[0], if non-empty.
2. **Read last?** arr[-1], if non-empty.
3. **Append?** arr.append(value).
4. **Find maximum?** One pass, O(n).
5. **Reverse in place?** arr.reverse().
6. **Reversed copy?** arr[::-1].
7. **Remove duplicates preserving order?** Track seen values and append first occurrences.
### Worked example: largest value
    def largest(arr):
        if not arr:
            raise ValueError('empty input')
        best = arr[0]
        for value in arr[1:]:
            if value > best:
                best = value
        return best
**Approach:** Keep the best candidate; replace it whenever a larger value appears. Time O(n), extra space O(1).
**Tasks:** Second largest, move zeroes, rotate list, merge sorted lists.

## 3. Strings
**Definition:** A string is an immutable sequence of Unicode characters.
**Explanation:** String questions often use scans, frequency maps or two pointers. Clarify case, spaces, punctuation and Unicode requirements.
**Real-world example:** Validate text identifiers, parse logs or compare normalised names.
**When/where/how:** Normalise only according to the stated requirement; avoid silently removing meaningful characters.
### Seven Q&A/examples
1. **Reverse?** s[::-1].
2. **Palindrome?** Compare normalised text with its reverse.
3. **Count characters?** len(s) or a frequency map.
4. **First non-repeating character?** Count, then scan original order.
5. **Anagram?** Compare character counts after agreed normalisation.
6. **Remove literal spaces?** s.replace(' ', '').
7. **Why immutable?** Contents cannot be changed in place.
### Worked example: palindrome
    def is_palindrome(text):
        cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]
**Approach:** Normalise the input then compare with its reverse. Time O(n), extra space O(n).
**Tasks:** Character frequency, first unique character, anagram check, longest common prefix.

## 4. Hashing: dictionaries and sets
**Definition:** Hash tables map hashable keys to values or track unique keys.
**Explanation:** Dictionary/set membership is expected O(1) average; keys must be hashable.
**Real-world example:** Look up users by ID, count events or find a pair sum.
**When/where/how:** Use hashing for repeated membership tests, counts, grouping and complements.
### Seven Q&A/examples
1. **Count values?** Dictionary or Counter.
2. **Membership?** value in seen.
3. **Remove duplicates unordered?** set(values).
4. **Preserve unique order?** Seen set plus result list.
5. **Two Sum?** Store prior values and indexes.
6. **Can list be a key?** No, it is unhashable.
7. **Why use set?** Unique values and efficient expected membership.
### Worked example: Two Sum
    def two_sum(nums, target):
        seen = {}
        for i, value in enumerate(nums):
            needed = target - value
            if needed in seen:
                return [seen[needed], i]
            seen[value] = i
        return None
**Approach:** For each value, check if its complement was already seen. Expected O(n) time and O(n) space.
**Tasks:** First repeated value, group anagrams, word frequency, array intersection.

## 5. Two pointers
**Definition:** Two indexes/references scan a sequence, often from opposite ends or at different speeds.
**Real-world example:** Find two prices that sum to a budget in a sorted price list.
**When/where/how:** Look for sorted arrays, pair conditions, palindrome checks or in-place rearrangement. Justify each pointer movement.
### Seven Q&A
1. **Reverse array?** Swap endpoints until they meet.
2. **Palindrome?** Compare characters at both ends.
3. **Pair sum in sorted list?** Move left if sum too small, right if too large.
4. **Remove sorted duplicates?** Read pointer plus write pointer.
5. **Move zeroes?** Write nonzero values then fill remaining positions.
6. **Merge sorted lists?** Advance the pointer holding the smaller value.
7. **Always O(n)?** Common scans are O(n), but the technique alone does not guarantee it.
### Worked example: pair sum
    def has_pair_sum(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target: return True
            if total < target: left += 1
            else: right -= 1
        return False
**Assumption:** nums is sorted. Time O(n), extra space O(1).
**Tasks:** Pair sum, palindrome, remove duplicates, move zeroes.

## 6. Sliding window
**Definition:** A sliding window maintains a contiguous sequence segment while its boundaries move.
**Real-world example:** Find the busiest seven-day period or longest substring meeting a rule.
**When/where/how:** Look for contiguous subarray/substring and fixed-size or longest/shortest valid window. Check assumptions such as non-negative values.
### Seven Q&A
1. **Fixed-size sum?** Add incoming value and subtract outgoing value.
2. **Maximum sum of k consecutive values?** Track running sum and maximum.
3. **Average of k values?** Window sum divided by k.
4. **Longest unique substring?** Window plus last-seen indexes/set.
5. **Minimum sum-at-least-target window?** Shrinking window works for positive/non-negative values; negatives complicate it.
6. **Why often O(n)?** Each boundary moves forward at most n times.
7. **Works for every subarray problem?** No; the property and input constraints matter.
### Worked example: max sum of size k
    def max_window_sum(nums, k):
        if k <= 0 or k > len(nums):
            raise ValueError('invalid window size')
        current = sum(nums[:k])
        best = current
        for right in range(k, len(nums)):
            current += nums[right] - nums[right-k]
            best = max(best, current)
        return best
**Tasks:** Max sum, average of k, longest unique substring.

## 7. Prefix sums
**Definition:** Prefix sums store cumulative sums so range sums can be answered quickly.
**Real-world example:** Answer many date-range sales queries after preprocessing daily totals.
**When/where/how:** Useful when many range-sum queries use the same unchanged array.
### Seven Q&A
1. **Build?** Start with zero and append cumulative totals.
2. **Sum l through r?** prefix[r+1] - prefix[l].
3. **Preprocessing?** O(n).
4. **Range query?** O(1) after preprocessing.
5. **Fast arbitrary updates?** Not automatically; updates may require rebuilding or another structure.
6. **Can include negative values?** Yes.
7. **Common bug?** Off-by-one indexes.
### Worked example
    def build_prefix(nums):
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        return prefix
    def range_sum(prefix, left, right):
        return prefix[right + 1] - prefix[left]
**Tasks:** Multiple range sums; count subarrays with a target sum using prefix sums and frequencies.

## 8. Sorting and binary search
**Definition:** Sorting arranges values; binary search halves a sorted search interval repeatedly.
**Real-world example:** Search a sorted catalogue or find the first point a metric crosses a threshold.
**When/where/how:** Binary search needs sorted data or a monotonic predicate. Maintain a clear search invariant.
### Seven Q&A
1. **Sorted copy?** sorted(values).
2. **Sort in place?** values.sort().
3. **Descending?** sorted(values, reverse=True).
4. **Search sorted list?** Binary search O(log n).
5. **One search in unsorted data?** Linear search may be simpler.
6. **First occurrence?** Continue left after a match.
7. **Can binary search reliably search unsorted values?** No.
### Worked example
    def binary_search(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return -1
**Tasks:** Lower bound, first/last occurrence, search insert position.

## 9. Recursion and backtracking
**Definition:** Recursion solves a smaller version of a problem; backtracking explores choices and undoes them to try alternatives.
**Real-world example:** Generate combinations, solve puzzles or search paths through a maze.
**When/where/how:** Define a base case and progress toward it. For backtracking, choose, explore and unchoose; prune impossible branches.
### Seven Q&A
1. **Recursive factorial?** n times factorial(n-1), with base case.
2. **Why base case?** It stops recursion.
3. **Call stack?** Stores active calls and their local state.
4. **Generate subsets?** Include/exclude each item.
5. **Generate permutations?** Choose unused item, recurse, undo choice.
6. **Backtracking?** Explore and reverse a choice before trying another.
7. **Is recursion always better?** No; iterative solutions can be simpler and avoid recursion limits.
### Worked example
    def factorial(n):
        if n < 0: raise ValueError('n must be non-negative')
        if n <= 1: return 1
        return n * factorial(n - 1)
**Tasks:** Subsets, permutations, balanced parentheses.

## 10. Linked lists, stacks and queues
**Definition:** Linked lists connect nodes by references; stacks are LIFO; queues are FIFO.
**Real-world example:** Stack for undo history; queue for jobs waiting to be processed.
**When/where/how:** Python lists are convenient stacks using append/pop at the end. Use collections.deque for efficient queue operations. Learn linked lists to understand node references and pointer changes.
### Seven Q&A
1. **Stack push?** append().
2. **Stack pop?** pop().
3. **Queue enqueue?** deque.append().
4. **Queue dequeue?** deque.popleft().
5. **LIFO?** Last in, first out.
6. **FIFO?** First in, first out.
7. **Linked-list cycle detection?** Floyd's slow/fast pointer algorithm.
### Tasks
- Validate parentheses with a stack.
- Implement a queue using two stacks.
- Reverse a linked list.
- Detect a linked-list cycle.

## 11. Trees and binary search trees
**Definition:** A tree is a hierarchy of nodes; a binary tree node has at most two children. A BST orders keys by a comparison rule.
**Real-world example:** File hierarchies, organisation charts, syntax trees and indexes.
**When/where/how:** Use trees for hierarchical data. Choose traversal based on whether root-first, sorted order, children-first or level-order processing is needed.
### Seven Q&A
1. **Preorder?** Root, left, right.
2. **Inorder?** Left, root, right.
3. **Postorder?** Left, right, root.
4. **BFS?** Use a queue.
5. **Height?** Longest root-to-leaf path, according to the chosen convention.
6. **Is every BST balanced?** No.
7. **Inorder of valid BST?** Keys in sorted order.
### Worked example
    def inorder(node):
        if node is None: return []
        return inorder(node.left) + [node.value] + inorder(node.right)
**Tasks:** Preorder, BFS, tree height, BST search and BST validation.

## 12. Heaps and priority queues
**Definition:** A heap efficiently exposes a minimum or maximum-priority item. Python heapq implements a min-heap.
**Real-world example:** Schedule urgent jobs, find top-k items, merge sorted streams.
**When/where/how:** Use a heap when repeatedly extracting the next minimum/maximum matters more than maintaining a fully sorted list.
### Seven Q&A
1. **Build heap?** heapq.heapify(values).
2. **Insert?** heapq.heappush(heap, value).
3. **Remove minimum?** heapq.heappop(heap).
4. **Inspect minimum?** heap[0], if non-empty.
5. **Get k smallest?** heapq.nsmallest(k, values).
6. **Is a heap fully sorted?** No.
7. **Priority queue?** Removes items by priority.
### Worked example
    import heapq
    values = [7, 2, 9, 1]
    heapq.heapify(values)
    print(heapq.heappop(values))  # 1
**Tasks:** Kth largest, merge sorted lists, running median.

## 13. Graphs: BFS, DFS and shortest paths
**Definition:** A graph contains vertices connected by edges; it can be directed/undirected and weighted/unweighted.
**Real-world example:** Road maps, social networks, task dependencies.
**When/where/how:** Identify direction, weights and cycles before choosing representation and algorithm. BFS finds shortest paths in unweighted graphs; Dijkstra assumes non-negative edge weights.
### Seven Q&A
1. **Sparse representation?** Adjacency list.
2. **Traverse level by level?** BFS.
3. **Explore deeply?** DFS.
4. **Shortest unweighted path?** BFS.
5. **Dijkstra with negative edges?** Not safe in general.
6. **Cycle?** A path that returns to a previously visited vertex under graph rules.
7. **Why visited set?** Prevent revisiting and infinite cycling.
### Worked example
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
**Tasks:** Connected components, reachability, shortest unweighted path, cycle detection.

## 14. Greedy algorithms
**Definition:** Greedy algorithms choose a locally attractive option at each step.
**Real-world example:** Schedule the maximum number of compatible activities by selecting earliest finishing activities.
**When/where/how:** State the greedy rule and prove why it preserves an optimal solution; a plausible local choice is not enough.
### Seven Q&A
1. **Greedy?** Choose a locally optimal step.
2. **Always optimal?** No.
3. **Activity selection?** Earliest finishing compatible activity is a standard optimal strategy.
4. **Fractional knapsack?** Value/weight greedy is optimal when fractions are allowed.
5. **0/1 knapsack with same rule?** Not generally optimal.
6. **Why prove the rule?** Local choices may block global optimality.
7. **How test a greedy idea?** Search for counterexamples and prove correctness.
**Tasks:** Interval scheduling, fractional knapsack, minimum coins for a specified coin system.

## 15. Dynamic programming
**Definition:** DP solves overlapping subproblems and reuses their results.
**Explanation:** Top-down uses memoization; bottom-up uses tabulation. Define state, transition, base cases and computation order.
**Real-world example:** Budget optimisation, sequence comparison and resource allocation.
**When/where/how:** Look for repeated subproblems and optimal substructure. Define exactly what each DP state means before writing transitions.
### Seven Q&A
1. **Fibonacci DP?** Save prior results.
2. **Memoization?** Cache recursive results.
3. **Tabulation?** Fill a table from base cases upward.
4. **State?** Representation of a subproblem.
5. **Transition?** Formula relating states.
6. **Can DP reduce exponential recursion?** Often, if the number of distinct states is much smaller.
7. **What define first?** State, base cases and recurrence.
### Worked example
    def fibonacci(n):
        if n < 0: raise ValueError('n must be non-negative')
        if n < 2: return n
        previous, current = 0, 1
        for _ in range(2, n + 1):
            previous, current = current, previous + current
        return current
**Tasks:** Climbing stairs, coin change, house robber, longest common subsequence, 0/1 knapsack.

## 16. Tries, DSU, Fenwick trees and segment trees
**Definition:** Trie stores shared prefixes; Disjoint Set Union maintains connected components; Fenwick and segment trees support range queries and updates.
**Real-world example:** Autocomplete, grouping connected accounts and dynamic range-sum queries.
**When/where/how:** Learn these after arrays, hashing, trees and complexity. Use them when their operation trade-offs justify added complexity.
### Seven Q&A
1. **Trie use?** Prefix lookup/autocomplete.
2. **DSU use?** Track components as edges are added.
3. **find(x)?** Return the representative of x's set.
4. **union(a,b)?** Merge sets.
5. **Fenwick tree?** Efficient prefix sums and point updates.
6. **Segment tree?** Flexible range queries and updates.
7. **Start here as a beginner?** No; master fundamentals first.
**Tasks:** Implement a trie, DSU and Fenwick tree.

## 17. Bit manipulation and advanced backtracking
**Definition:** Bit manipulation works with binary representations; backtracking searches choices and undoes them.
**Real-world example:** Permission flags, compact state masks, puzzles and constrained combinations.
**When/where/how:** For bit operations, write binary examples first. For search, identify constraints and prune impossible branches.
### Seven Q&A
1. **Even/odd for non-negative n?** n & 1 checks the lowest bit.
2. **Clear lowest set bit?** n & (n - 1) for positive integers.
3. **Power of two?** n > 0 and (n & (n - 1)) == 0.
4. **Generate subsets?** Include/exclude each item.
5. **Generate permutations?** Choose an unused candidate and recurse.
6. **Pruning?** Stop exploring branches that cannot lead to a solution.
7. **Bitmask?** Bits represent flags or choices.
**Tasks:** Subsets, N-Queens, combinations and bit operations.

## Pattern recognition interview questions
1. **Two Sum?** Pair condition; hashing gives expected O(n).
2. **Sliding window?** Contiguous segment with a maintained property.
3. **Binary search?** Sorted input or monotonic predicate.
4. **Stack?** LIFO or nested structure matching.
5. **BFS?** Level order and shortest path in unweighted graphs.
6. **DP?** Overlapping subproblems with reusable results.
7. **What after solving?** Test edge cases, explain complexity and solve a variation.

## Practice by level
### Beginner
- Largest and second-largest values.
- Reverse string and palindrome.
- Character frequencies.
- Pair sum.
- Linear and binary search.
- Valid parentheses.
### Intermediate
- Merge intervals.
- Longest substring without repeated characters.
- Search rotated sorted array.
- Reverse linked list and detect cycle.
- Tree traversals and level-order traversal.
- Top-k frequent values.
- Connected components.
### Advanced
- Backtracking word search.
- Coin change and longest common subsequence.
- Dijkstra with non-negative weights.
- Minimum spanning tree.
- Segment tree/Fenwick tree.
- Trie prefix search.
- DSU connectivity.

## Required topic workflow
For every topic: definition and intuition; dry-run; implement; answer seven topic questions/examples; solve three unseen variations; test edge cases; state time/space complexity; write down mistakes and revisit them.

**Important:** This is a roadmap and starter interview guide, not a guarantee that all advanced DSA is mastered by reading it. Solve additional problems independently.