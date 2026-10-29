# Day 37 — Stacks, Queues, Linked Lists and Recursion

**Status:** Full study pack created in the DSA track.

## 1. Definition
A **stack** is last-in-first-out (LIFO); a **queue** is first-in-first-out (FIFO). A **linked list** stores nodes connected by references. **Recursion** solves a problem by calling a function on a smaller input, with a base case that stops.

## 2. Why / when
Use stacks for undo/history and expression parsing, queues for scheduling, linked lists when node insertion/removal trade-offs matter, and recursion for tree-like or divide-and-conquer problems. Python lists are efficient stacks; use `collections.deque` for queues. Recursion has depth limits and is not always the best choice for large linear input.

## 3. Syntax and rules
```python
stack=[]; stack.append("x"); top=stack.pop()
from collections import deque
queue=deque(["a"]); first=queue.popleft()
```
A recursive function needs a base case and progress toward it.

## 4. Five worked examples
### Example 1 — Stack
```python
stack=[]
stack.extend([1,2,3])
print(stack.pop(), stack)
```
Output: `3 [1, 2]`. The last item is removed first.

### Example 2 — Queue
```python
from collections import deque
queue=deque(["A","B"])
queue.append("C")
print(queue.popleft())
```
Output: `A`. The first item leaves first.

### Example 3 — Recursive factorial
```def factorial(n):
    if n<0: raise ValueError("n must be non-negative")
    return 1 if n<2 else n*factorial(n-1)
print(factorial(5))
```
Output: `120`. The base cases are 0 and 1.

### Example 4 — Recursive sum
```def recursive_sum(values):
    if not values: return 0
    return values[0]+recursive_sum(values[1:])
print(recursive_sum([1,2,3]))
```
Output: `6`. Each call reduces list length; slicing adds memory/time overhead.

### Example 5 — Linked-list node
```class Node:
    def __init__(self,value,next_node=None): self.value,self.next=value,next_node
head=Node(1,Node(2,Node(3)))
print(head.next.value)
```
Output: `2`. Each node points to the following node.

## 5. Five tasks with solutions
### Task 1 — Reverse with stack
```def reverse_text(text):
    stack=list(text); result=""
    while stack: result += stack.pop()
    return result
print(reverse_text("python"))
```
Output: `nohtyp`. For large strings, a list plus join or slicing is more efficient.

### Task 2 — Balanced brackets
```def balanced(text):
    stack=[]; pairs={")":"(","]":"[","}":"{"}
    for char in text:
        if char in "([{": stack.append(char)
        elif char in pairs:
            if not stack or stack.pop()!=pairs[char]: return False
    return not stack
print(balanced("([])"))
```
Output: `True`.

### Task 3 — Queue processing
```from collections import deque
def serve(items):
    queue=deque(items); order=[]
    while queue: order.append(queue.popleft())
    return order
print(serve(["A","B","C"]))
```
Output: `['A', 'B', 'C']`.

### Task 4 — Iterative factorial alternative
```def factorial(n):
    if n<0: raise ValueError
    result=1
    for k in range(2,n+1): result*=k
    return result
print(factorial(5))
```
Output: `120`. Iteration avoids recursion depth for this simple sequence.

### Task 5 — Linked-list traversal
```class Node:
    def __init__(self,value,next_node=None): self.value,self.next=value,next_node
def to_list(head):
    values=[]
    while head: values.append(head.value); head=head.next
    return values
print(to_list(Node(1,Node(2))))
```
Output: `[1, 2]`.

## 6. Common mistakes
- Stack/queue order confusion.
- Removing index 0 repeatedly from a list is inefficient for a queue.
- Recursion without a base case does not terminate.
- Deep recursion may raise RecursionError.
- Incorrect node pointers can lose part of a linked list.

## 7. Interview Q&A
1. LIFO means? **Last in, first out.**
2. FIFO means? **First in, first out.**
3. Why deque over list for queue? **Efficient pops from the left.**
4. What is recursion base case? **Condition that returns without recursive call.**
5. Why use a linked list? **Node-based structure supports local link updates, though indexing is linear.**

## 8. Project — Browser History Stack
Save as `browser_history.py`.
```python
class BrowserHistory:
    def __init__(self): self.back_stack=[]; self.current=None
    def visit(self,url):
        if not url.strip(): raise ValueError("URL required")
        if self.current is not None: self.back_stack.append(self.current)
        self.current=url
    def back(self):
        if not self.back_stack: return self.current
        self.current=self.back_stack.pop()
        return self.current

def main():
    history=BrowserHistory()
    history.visit("example.com"); history.visit("python.org")
    print(history.back())

if __name__ == "__main__": main()
```
Output: `example.com`.

### Tests — `test_browser_history.py`
```python
import unittest
from browser_history import BrowserHistory
class HistoryTests(unittest.TestCase):
    def test_back(self):
        h=BrowserHistory(); h.visit("a"); h.visit("b"); self.assertEqual(h.back(),"a")
    def test_empty_back(self):
        h=BrowserHistory(); self.assertIsNone(h.back())
    def test_current(self):
        h=BrowserHistory(); h.visit("a"); self.assertEqual(h.current,"a")
    def test_empty_url(self):
        with self.assertRaises(ValueError): BrowserHistory().visit(" ")
    def test_several_back(self):
        h=BrowserHistory(); [h.visit(x) for x in ["a","b","c"]]
        self.assertEqual(h.back(),"b"); self.assertEqual(h.back(),"a")
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Stack order? **LIFO.**
2. Queue order? **FIFO.**
3. What stops recursion? **Base case.**
4. Why deque? **Efficient operations at both ends.**
5. Linked-list node contains? **Value and reference to next node (in a singly linked list).**
**Challenge:** Implement a queue class with enqueue/dequeue/peek and test empty behavior.

## Real-world use cases — where, when and how
1. **Undo history:** Where: editors/browser. When latest action reverses first. How: use a stack and pop the last action.
2. **Job scheduling:** Where: worker systems. When requests should be served in arrival order. How: use deque as FIFO queue.
3. **Expression parsing:** Where: calculators. When brackets/operators must be matched. How: push opening symbols, pop on valid closing symbols.
4. **Linked data:** Where: educational structures or frequent node insertion. When node links are updated locally. How: store each value with a reference to its next node.
5. **Hierarchical recursion:** Where: tree traversal. When data naturally contains subtrees. How: use a base case and recurse on child nodes; use iterative methods for very deep input.


## 10. Completion
- [ ] I can explain stack, queue, linked list and recursion.
- [ ] Tests pass.
- [ ] I solved the queue class challenge.
