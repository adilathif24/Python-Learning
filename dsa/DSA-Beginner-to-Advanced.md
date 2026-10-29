# Data Structures and Algorithms (DSA): Basic to Advanced


> **Professional interview preparation:** For structured syntax, complete code examples, interview-ready explanations, seven solved interview Q&As and five practice tasks with solutions, also use the [Professional Interview Workbook](dsa/Professional-Interview-Workbook.md).

This track is separate from Python Core and OOP. For each topic, learn the definition, explanation, where/when/how to use it, a real-world use case, seven solved examples/questions, and five practice questions with answers.

## How to solve a DSA question
Clarify requirements → make a small example → outline brute force → handle edge cases → implement → dry-run → analyse time/space complexity → solve a variation.

## 1. Complexity
**Definition:** Time complexity describes how operation growth scales with input size; space complexity describes memory usage. Big O commonly expresses an asymptotic upper bound.
**Use/when:** Compare algorithms for large inputs and identify dominant operations. **Real world:** Choose between scanning customer records and looking up an indexed customer ID.
### Seven examples with answers
1. Index a Python list: O(1) typical.
2. Scan n elements: O(n).
3. Two nested n-sized loops: O(n²).
4. Halve search space repeatedly: O(log n).
5. Merge sort: O(n log n) time.
6. Store an extra n-item list: O(n) extra space.
7. Two sequential O(n) loops: O(n) overall, not O(2n) in asymptotic notation.
### Five practice Q&A
1. Binary search complexity? **Answer:** O(log n) on sorted data.
2. Three nested n-loops? **Answer:** O(n³), if each loops n times.
3. What is auxiliary space? **Answer:** Extra memory used by an algorithm.
4. Is O(n) always faster for tiny inputs? **Answer:** Not necessarily; constants and overhead matter.
5. Why analyse complexity? **Answer:** To estimate scalability and compare approaches.

## 2. Arrays and lists
**Definition:** An indexed sequence; Python lists are dynamic arrays of object references. **Explanation:** Indexing is O(1), searching O(n), front insertion usually O(n).
**Where/when/how:** Use for ordered items and index-based operations. **Real world:** Daily temperatures, shopping cart items, scores.
### Seven solved examples
1. Largest element: scan once and update `best` — O(n).
2. Reverse copy: `a[::-1]`.
3. Append: `a.append(x)` — amortised O(1).
4. Linear search: return index on match — O(n).
5. Sum values: accumulator — O(n).
6. Second distinct largest: track largest and second largest in one pass — O(n).
7. Move zeroes: write non-zero values forward then fill zeroes — O(n).
### Five practice Q&A
1. Find largest without `max()`? **Answer:** Initialise from first item and scan; reject empty input.
2. Remove duplicates preserving order? **Answer:** Use a seen set and output list for hashable values.
3. Rotate right by k? **Answer:** For non-empty `a`, set `k %= len(a)` and use `a[-k:] + a[:-k]`, handling k=0.
4. Merge sorted arrays? **Answer:** Two pointers; append the smaller current value.
5. List search complexity? **Answer:** O(n).

## 3. Strings
**Definition:** An immutable sequence of Unicode characters. **Use/when:** Text validation, parsing and pattern matching. Clarify case, spaces and punctuation rules. **Real world:** Search logs or validate usernames.
### Seven solved examples
1. Reverse: `s[::-1]`.
2. Palindrome: normalise then compare to reverse.
3. Length: `len(s)`.
4. Character frequency: dictionary counter.
5. Anagram: compare character counts after agreed normalisation.
6. First unique character: count then scan in original order.
7. Longest common prefix: shorten a candidate until every string starts with it.
### Five practice Q&A
1. Reverse `python`? **Answer:** `nohtyp`.
2. Is `level` a palindrome? **Answer:** Yes.
3. Vowels in `hello`? **Answer:** 2.
4. First unique in `swiss`? **Answer:** `w`.
5. Why immutable? **Answer:** Contents cannot be modified in place; operations create new strings.

## 4. Hash maps and sets
**Definition:** A dict maps keys to values; a set stores unique hashable values. Average-case membership/lookup is commonly O(1). **Use/when:** Frequency counting, membership, de-duplication and complement lookup. **Real world:** Count events or find shared IDs.
### Seven solved examples
1. Frequency: `counts[x] = counts.get(x, 0) + 1`.
2. Membership: `x in seen`.
3. Unique values: `set(values)` when order is irrelevant.
4. Ordered deduplication: seen set plus result list.
5. Two Sum: store previous values and indexes.
6. Intersection: `set(a) & set(b)`.
7. Group anagrams using sorted-word or character-count keys.
### Five practice Q&A
1. Why dict for frequencies? **Answer:** Efficient expected updates by key.
2. Can a list be a dict key? **Answer:** No, lists are unhashable.
3. First repeated number? **Answer:** Scan with a seen set.
4. Two Sum in expected O(n)? **Answer:** Check `target - value` in a map, then store current value/index.
5. Count words? **Answer:** Split according to specified whitespace rules and count with a dict or `collections.Counter`.

## 5. Two pointers
**Definition:** Two indexes scan a sequence, often from opposite ends or at different speeds. **Use/when:** Sorted pair sums, palindrome checks, merging and in-place filtering. **Real world:** Find two sorted prices that match a budget.
### Seven solved examples
1. Reverse an array by swapping ends.
2. Palindrome: compare left/right characters.
3. Sorted pair sum: move left if sum too small, right if too large.
4. Remove duplicates from sorted list with a write pointer.
5. Move zeroes with a write pointer.
6. Merge sorted arrays by advancing the smaller side.
7. Linked-list cycle detection with slow/fast pointers.
### Five practice Q&A
1. Is two pointers always O(n)? **Answer:** No; common scans are O(n), but technique alone guarantees no complexity.
2. Why sorted input helps pair sum? **Answer:** It gives a valid direction for pointer movement.
3. Reverse `[1,2,3]`? **Answer:** `[3,2,1]`.
4. Remove duplicates from sorted values? **Answer:** Write each new value only when it differs from the previous unique value.
5. When avoid opposite-end pointers? **Answer:** When no rule justifies moving either end.

## 6. Sliding window and prefix sums
**Definition:** A sliding window maintains a contiguous segment; prefix sums store cumulative totals. **Use/when:** Contiguous subarray/substring constraints and repeated range-sum queries. **Real world:** Best sales total over seven consecutive days.
### Seven solved examples
1. Fixed k sum: add entering value, subtract leaving value.
2. Maximum k-window sum: update running sum and best.
3. Average k-window: sum divided by k.
4. Longest unique substring: variable window plus last-seen indexes.
5. Build prefix: start `[0]`, append cumulative sums.
6. Range sum l..r: `prefix[r+1] - prefix[l]`.
7. Subarray sum k: prefix sum plus frequency map initialised with `{0: 1}`.
### Five practice Q&A
1. Fixed window scan complexity? **Answer:** O(n).
2. Does a standard shrinking-window sum work with arbitrary negative values? **Answer:** Not generally; input assumptions matter.
3. Prefix build cost? **Answer:** O(n).
4. Range query after prefix preprocessing? **Answer:** O(1).
5. Why start prefix frequency with `{0: 1}`? **Answer:** It counts a matching subarray beginning at index zero.

## 7. Searching and sorting
**Definition:** Searching locates a value; sorting orders values. Binary search halves a monotonic search range. **Use/when:** Binary search requires sorted data or a monotonic predicate. **Real world:** Find a product or first threshold-crossing day.
### Seven solved examples
1. Linear search: O(n).
2. Binary search on sorted list: O(log n).
3. `sorted(a)` returns a new list.
4. `a.sort()` mutates list.
5. Merge sort: O(n log n) time, typically O(n) extra space.
6. First occurrence: after match, continue left.
7. Sort records: `sorted(users, key=lambda u: u['age'])`.
### Five practice Q&A
1. Binary search on unsorted data? **Answer:** Not reliably.
2. Stable sort? **Answer:** Equal-key items retain their relative input order.
3. Comparison sorting lower bound? **Answer:** Ω(n log n) comparisons in the general comparison model.
4. What is off-by-one? **Answer:** Boundary/index error.
5. In-place vs new sorted list? **Answer:** `list.sort()` mutates; `sorted()` returns a new list.

## 8. Recursion and backtracking
**Definition:** Recursion calls a function on a smaller problem. Backtracking explores choices and undoes them before trying alternatives. **Use/when:** Hierarchies, combinations, permutations and constraint search. **Real world:** Scheduling or maze solving.
### Seven solved examples
1. Factorial: base case then `n * factorial(n-1)`.
2. Fibonacci recursion repeats work without memoization.
3. Tree traversal recursively visits children.
4. Subsets: include/exclude each item.
5. Permutations: choose, recurse, undo.
6. N-Queens: place queens and prune invalid choices.
7. Maze path: explore neighbours and backtrack.
### Five practice Q&A
1. Why base case? **Answer:** To stop recursion.
2. Call stack? **Answer:** Active calls and their execution state.
3. Pruning? **Answer:** Stop exploring a branch that cannot produce a valid answer.
4. Is recursion always better? **Answer:** No; iteration may use less stack space.
5. Avoid repeated recursive work? **Answer:** Memoization/DP.

## 9. Linked lists, stacks and queues
**Definition:** Linked lists connect nodes by references; stack is LIFO; queue is FIFO. **Use/when:** Stack for nested matching/undo; queue for arrival order and BFS. **Real world:** Browser undo history or background jobs.
### Seven solved examples
1. Stack push: `stack.append(x)`.
2. Stack pop: `stack.pop()`.
3. Queue enqueue with deque: `q.append(x)`.
4. Queue dequeue: `q.popleft()`.
5. Valid parentheses: push openers, match closers.
6. Reverse linked list by tracking previous/current/next.
7. Detect cycle with Floyd slow/fast pointers.
### Five practice Q&A
1. LIFO? **Answer:** Last in, first out.
2. FIFO? **Answer:** First in, first out.
3. Why deque for queue? **Answer:** Efficient append and popleft.
4. Stack append/pop at end complexity? **Answer:** Amortised O(1) append; O(1) pop at end.
5. Linked-list cycle? **Answer:** Following next references eventually revisits a node.

## 10. Trees and heaps
**Definition:** Trees model hierarchy; a heap efficiently exposes a min/max priority; a BST orders keys. **Use/when:** Trees for hierarchy, heaps for repeated priority extraction. **Real world:** File tree or job scheduler.
### Seven solved examples
1. Preorder: root-left-right.
2. Inorder: left-root-right.
3. Postorder: left-right-root.
4. BFS uses a queue.
5. `heapq.heappush` inserts into a min-heap.
6. `heapq.heappop` removes the smallest.
7. Top-k frequent values can use heap or sorting depending on constraints.
### Five practice Q&A
1. Inorder of valid BST? **Answer:** Sorted keys.
2. Is every BST balanced? **Answer:** No; an unbalanced one can degrade to O(n).
3. Is a heap fully sorted? **Answer:** No.
4. What is a priority queue? **Answer:** Removes items according to priority.
5. Tree height? **Answer:** Longest root-to-leaf path under the stated edge/node convention.

## 11. Graphs
**Definition:** A graph has vertices and edges; it may be directed/undirected and weighted/unweighted. **Use/when:** Routes, social connections, dependencies. **Real world:** Navigation.
### Seven solved examples
1. BFS uses a queue.
2. DFS explores depth-first.
3. BFS finds shortest paths in unweighted graphs.
4. A visited set prevents repeated traversal.
5. Connected components can be counted using DFS/BFS.
6. Dijkstra assumes non-negative edge weights.
7. Topological sorting applies to DAGs.
### Five practice Q&A
1. Why visited set? **Answer:** Avoid repeated work and revisits.
2. Dijkstra with negative weights? **Answer:** Not safe in general.
3. What is a cycle? **Answer:** A path that returns to a previously visited vertex.
4. Adjacency list? **Answer:** Each vertex stores its neighbours.
5. Shortest unweighted path? **Answer:** BFS.

## 12. Greedy and dynamic programming
**Definition:** Greedy chooses a local option at each step; dynamic programming reuses overlapping subproblem results. **Use/when:** Greedy needs a correctness proof; DP needs state, base cases and transitions. **Real world:** Scheduling and resource allocation.
### Seven solved examples
1. Activity selection often chooses earliest finishing compatible activity.
2. Fractional knapsack can greedily select by value/weight.
3. The same greedy rule is not generally optimal for 0/1 knapsack.
4. Fibonacci DP stores previous results.
5. Memoization is top-down caching.
6. Tabulation fills results bottom-up.
7. Coin change DP compares previous amounts and denominations.
### Five practice Q&A
1. Is greedy always optimal? **Answer:** No.
2. DP state? **Answer:** A precise subproblem representation.
3. Transition? **Answer:** A recurrence connecting states.
4. Memoization vs tabulation? **Answer:** Top-down caching vs bottom-up table.
5. What define before coding DP? **Answer:** State meaning, base cases and transition.

## 13. Advanced structures and bit manipulation
**Definition:** Tries store shared prefixes; DSU tracks disjoint sets/connectivity; Fenwick/segment trees support range queries; bit operations manipulate binary representations.
**Use/when:** Learn after arrays, hashing, trees and graph fundamentals. **Real world:** Autocomplete, dynamic connectivity and range-sum dashboards.
### Seven solved examples
1. Trie supports prefix search.
2. DSU `find(x)` locates a set representative.
3. DSU `union(a,b)` merges sets.
4. Fenwick tree supports prefix sums and point updates.
5. Segment tree supports flexible range queries and updates.
6. `n & 1` tests parity for non-negative n.
7. For positive n, `(n & (n - 1)) == 0` tests a power of two.
### Five practice Q&A
1. Trie use? **Answer:** Prefix lookup/autocomplete.
2. DSU use? **Answer:** Track connectivity as sets merge.
3. Path compression? **Answer:** Flattens DSU paths to speed later lookups.
4. Segment tree use? **Answer:** Efficient supported range queries and updates.
5. Bitmask? **Answer:** Integer bits represent flags or choices.

## Pattern recognition checklist
- Hash map: frequency, duplicates, Two Sum.
- Two pointers: sorted pair conditions, palindrome, in-place changes.
- Sliding window: contiguous segment constraints.
- Prefix sums: repeated range sums.
- Binary search: sorted data or monotonic decision.
- Stack: nested structure and last-in-first-out.
- Queue/BFS: level traversal and unweighted shortest path.
- Heap: repeated min/max and top-k.
- DP: overlapping subproblems with reusable results.
- Backtracking: enumerate choices and prune.

## Recruiter-ready DSA checklist
- Explain brute force before optimisation.
- State time and auxiliary-space complexity.
- Test empty, one-element, duplicates, boundary and invalid cases where applicable.
- Explain why the algorithm is correct, not only what the code does.
- Solve unseen variations independently.

**Scope note:** This is a structured roadmap and starter interview guide, not a claim of mastery. Practise additional unseen problems and run all code yourself.