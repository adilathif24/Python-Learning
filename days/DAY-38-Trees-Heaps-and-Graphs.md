# Day 38 — Trees, Heaps and Graphs

**Status:** Full study pack created in the DSA track.

## 1. Definition
A **tree** is a hierarchical graph with a root and child relationships. A **binary tree** node has at most two children. A **heap** is a priority-oriented structure. A **graph** contains vertices and edges, directed or undirected. BFS explores level by level; DFS explores deeply before backtracking.

## 2. Why / when
Trees model file systems and hierarchies; heaps support priority queues; graphs model routes, social connections and dependencies. Use adjacency lists for sparse graphs; choose a matrix when dense connections or constant-time edge lookup is required. Use BFS for shortest paths in unweighted graphs.

## 3. Syntax and rules
```python
from collections import deque
graph={"A":["B","C"],"B":["A"],"C":["A"]}
queue=deque(["A"]); visited={"A"}
```
Mark vertices visited when enqueuing to avoid duplicate queue entries. In graphs that may be cyclic, traversal needs a visited set.

## 4. Five worked examples
### Example 1 — Binary-tree node
```class Node:
    def __init__(self,value,left=None,right=None): self.value,self.left,self.right=value,left,right
root=Node(2,Node(1),Node(3))
print(root.left.value,root.right.value)
```
Output: `1 3`.

### Example 2 — Inorder traversal
```def inorder(node):
    return [] if node is None else inorder(node.left)+[node.value]+inorder(node.right)
print(inorder(Node(2,Node(1),Node(3))))
```
Output: `[1, 2, 3]`. Inorder of a BST visits keys in sorted order.

### Example 3 — Heap
```import heapq
heap=[5,1,4]; heapq.heapify(heap)
print(heapq.heappop(heap))
```
Output: `1`. A min-heap pops the smallest value.

### Example 4 — BFS
```from collections import deque
def bfs(graph,start):
    queue=deque([start]); seen={start}; order=[]
    while queue:
        node=queue.popleft(); order.append(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in seen: seen.add(neighbor); queue.append(neighbor)
    return order
print(bfs({"A":["B","C"],"B":["D"],"C":[],"D":[]},"A"))
```
Output: `['A', 'B', 'C', 'D']`.

### Example 5 — DFS
```def dfs(graph,start):
    seen=set(); order=[]
    def visit(node):
        if node in seen: return
        seen.add(node); order.append(node)
        for neighbor in graph.get(node,[]): visit(neighbor)
    visit(start); return order
print(dfs({"A":["B","C"],"B":["D"],"C":[],"D":[]},"A"))
```
Output: `['A', 'B', 'D', 'C']`. Order depends on neighbor ordering.

## 5. Five tasks with solutions
### Task 1 — Minimum using heap
```import heapq
values=[9,2,7]
heapq.heapify(values)
print(heapq.heappop(values))
```
Output: `2`.

### Task 2 — Connected reachability
```from collections import deque
def reachable(graph,start,target):
    queue=deque([start]); seen={start}
    while queue:
        node=queue.popleft()
        if node==target:return True
        for nxt in graph.get(node,[]):
            if nxt not in seen:seen.add(nxt);queue.append(nxt)
    return False
print(reachable({"A":["B"],"B":["C"],"C":[]},"A","C"))
```
Output: `True`.

### Task 3 — Count tree nodes
```def count_nodes(node):
    return 0 if node is None else 1+count_nodes(node.left)+count_nodes(node.right)
print(count_nodes(Node(2,Node(1),Node(3))))
```
Output: `3`.

### Task 4 — Find shortest unweighted distance
```from collections import deque
def distance(graph,start,target):
    q=deque([(start,0)]); seen={start}
    while q:
        node,d=q.popleft()
        if node==target:return d
        for nxt in graph.get(node,[]):
            if nxt not in seen:seen.add(nxt);q.append((nxt,d+1))
    return -1
print(distance({"A":["B","C"],"B":["D"],"C":[],"D":[]},"A","D"))
```
Output: `2`. BFS yields shortest edge count for unweighted graphs.

### Task 5 — Top two smallest
```import heapq
print(heapq.nsmallest(2,[8,2,5,1]))
```
Output: `[1, 2]`.

## 6. Common mistakes
- Traversing a cyclic graph without visited tracking.
- Assuming a heap is fully sorted; only the root is guaranteed minimal in a min-heap.
- BFS shortest-path guarantee applies to unweighted/equal-edge-cost graphs.
- Recursive DFS may hit recursion depth on huge graphs.
- Define behavior for missing start/target nodes.

## 7. Interview Q&A
1. BFS vs DFS? **Queue/level order vs stack/recursion depth-first.**
2. BFS shortest path when? **In unweighted graphs.**
3. What is a min-heap? **Parent values are no greater than child values; root is minimum.**
4. What is a tree root? **Top node with no parent.**
5. Why visited set? **Avoid repeat traversal and cycles.**

## 8. Project — Shortest Route Finder
Save as `route_finder.py`.
```python
from collections import deque

def shortest_path(graph,start,target):
    if start==target:return [start]
    queue=deque([(start,[start])]); seen={start}
    while queue:
        node,path=queue.popleft()
        for neighbor in graph.get(node,[]):
            if neighbor in seen:continue
            next_path=path+[neighbor]
            if neighbor==target:return next_path
            seen.add(neighbor); queue.append((neighbor,next_path))
    return []

def main():
    graph={"Home":["Shop","Park"],"Shop":["Home","Office"],"Park":["Home"],"Office":["Shop"]}
    print(shortest_path(graph,"Home","Office"))

if __name__ == "__main__": main()
```
Output: `['Home', 'Shop', 'Office']`.

### Tests — `test_route_finder.py`
```python
import unittest
from route_finder import shortest_path
class RouteTests(unittest.TestCase):
    def test_route(self): self.assertEqual(shortest_path({"A":["B"],"B":["C"],"C":[]},"A","C"),["A","B","C"])
    def test_same_node(self): self.assertEqual(shortest_path({},"A","A"),["A"])
    def test_unreachable(self): self.assertEqual(shortest_path({"A":[],"B":[]},"A","B"),[])
    def test_cycle(self): self.assertEqual(shortest_path({"A":["B"],"B":["A"]},"A","B"),["A","B"])
    def test_direct_preferred(self): self.assertEqual(shortest_path({"A":["B","C"],"B":["C"],"C":[]},"A","C"),["A","C"])
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Which traversal uses a queue? **BFS.**
2. Which structure retrieves minimum efficiently? **Min-heap.**
3. Why visited set? **Avoid cycles/revisits.**
4. BFS shortest path applies to which graphs? **Unweighted graphs.**
5. What is an edge? **Connection between vertices.**
**Challenge:** Return both shortest path and distance, and test multiple equal-length paths.

## Real-world use cases — where, when and how
1. **File hierarchy:** Where: file browsers. When folders contain children. How: model directories as a tree and traverse recursively or iteratively.
2. **Priority scheduling:** Where: job queues. When smallest deadline/cost should be processed first. How: use heapq as a min-heap.
3. **Shortest routes:** Where: maps/network paths. When all edges have equal cost. How: run BFS and store parent/distance.
4. **Dependency graph:** Where: package/build systems. When tasks depend on other tasks. How: model vertices/edges and detect unreachable/cyclic relationships.
5. **Social network:** Where: connection recommendations. When neighboring accounts matter. How: graph traversal finds reachable nodes or shared connections.


## 10. Completion
- [ ] I can explain tree, heap, graph, BFS and DFS.
- [ ] Route finder tests pass.
- [ ] I solved the path/distance challenge.
