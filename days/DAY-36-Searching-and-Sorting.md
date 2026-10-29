# Day 36 — Searching and Sorting Algorithms

**Status:** Full study pack created. These algorithms belong to the DSA track.

## 1. Definition
Searching finds a target; sorting arranges values. Linear search scans each element. Binary search repeatedly halves a **sorted** sequence. Bubble sort swaps adjacent out-of-order values; Python's built-in sort is typically the correct production choice.

## 2. Why / when
Implement basic algorithms to understand complexity and interview reasoning. Prefer built-in `sorted()` in production unless learning constraints or special requirements demand a custom algorithm. Binary search requires sorted input and random access for the usual O(log n) analysis.

## 3. Syntax
```python
def binary_search(values, target):
    left, right = 0, len(values)-1
    while left <= right:
        mid = (left+right)//2
        if values[mid] == target: return mid
        if values[mid] < target: left = mid+1
        else: right = mid-1
    return -1
```
The search returns an index or -1 when not found.

## 4. Five worked examples
### Example 1 — Linear search
```python
def linear_search(values,target):
    for i,value in enumerate(values):
        if value==target: return i
    return -1
print(linear_search([7,9,12],9))
```
Output: `1`; O(n).

### Example 2 — Binary search
```python
def binary_search(a,x):
    lo,hi=0,len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]==x:return mid
        if a[mid]<x:lo=mid+1
        else:hi=mid-1
    return -1
print(binary_search([2,4,6,8,10],8))
```
Output: `3`; O(log n) on sorted list.

### Example 3 — Built-in sort
```python
print(sorted([5,2,7,1]))
```
Output: `[1, 2, 5, 7]`.

### Example 4 — Bubble sort
```python
def bubble_sort(values):
    result=values.copy()
    for end in range(len(result)-1,0,-1):
        swapped=False
        for i in range(end):
            if result[i]>result[i+1]:
                result[i],result[i+1]=result[i+1],result[i]; swapped=True
        if not swapped: break
    return result
print(bubble_sort([4,1,3]))
```
Output: `[1, 3, 4]`. Worst-case O(n²).

### Example 5 — Stable custom key
```python
students=[("Ali",80),("Maya",90),("Ravi",80)]
print(sorted(students,key=lambda row:row[1]))
```
Output: Ali then Ravi (both 80), then Maya. Python sort is stable.

## 5. Five tasks with solutions
### Task 1 — Return all matching indices
```def find_all(values,target):
    return [i for i,value in enumerate(values) if value==target]
print(find_all([2,1,2,2],2))
```
Output: `[0, 2, 3]`.

### Task 2 — Descending order
```print(sorted([1,4,2],reverse=True))
```
Output: `[4, 2, 1]`.

### Task 3 — Sort without mutation
```a=[3,1,2]; b=sorted(a)
print(a,b)
```
Output: `[3, 1, 2] [1, 2, 3]`.

### Task 4 — Test absent search
```def binary_search(a,x):
    lo,hi=0,len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]==x:return mid
        if a[mid]<x:lo=mid+1
        else:hi=mid-1
    return -1
print(binary_search([1,3,5],2))
```
Output: `-1`.

### Task 5 — Sort pairs by second item
```rows=[("a",3),("b",1),("c",2)]
print(sorted(rows,key=lambda row:row[1]))
```
Output: `[('b', 1), ('c', 2), ('a', 3)]`.

## 6. Common mistakes
- Binary search on unsorted input can return wrong answers.
- Infinite loops occur when left/right pointers fail to change.
- Confusing returned index with value.
- Bubble sort is educational but poor for large data.
- Duplicates may produce any matching index unless a first/last-match rule is implemented.

## 7. Interview Q&A
1. Linear search complexity? **O(n).**
2. Binary search complexity? **O(log n).**
3. Binary search requirement? **Sorted sequence.**
4. Built-in sort complexity? **Typically O(n log n).**
5. What is stable sorting? **Equal-key items preserve relative input order.**

## 8. Project — Searchable Contact Directory
Save as `contact_directory.py`.
```python
def search_contact(contacts, query):
    query=query.strip().casefold()
    return sorted([contact for contact in contacts if query in contact["name"].casefold()],
                  key=lambda contact:contact["name"].casefold())

def main():
    contacts=[{"name":"Adil","phone":"111"},{"name":"Maya","phone":"222"},{"name":"Ali","phone":"333"}]
    query=input("Search name: ")
    print(search_contact(contacts,query))

if __name__ == "__main__": main()
```
Input `al` returns Ali and Adil, sorted by name.

### Tests — `test_contact_directory.py`
```python
import unittest
from contact_directory import search_contact
class DirectoryTests(unittest.TestCase):
    def setUp(self): self.data=[{"name":"Maya","phone":"2"},{"name":"Ali","phone":"3"},{"name":"Adil","phone":"1"}]
    def test_search(self): self.assertEqual([x["name"] for x in search_contact(self.data,"al")],["Adil","Ali"])
    def test_case(self): self.assertEqual(len(search_contact(self.data,"MAYA")),1)
    def test_missing(self): self.assertEqual(search_contact(self.data,"zz"),[])
    def test_empty_query(self): self.assertEqual(len(search_contact(self.data,"")),3)
    def test_source_unchanged(self): search_contact(self.data,"a"); self.assertEqual(self.data[0]["name"],"Maya")
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Which search halves the search space? **Binary search.**
2. Does binary search require sorting? **Yes.**
3. Linear search worst-case? **O(n).**
4. What is stable sorting? **Preserves equal-key relative order.**
5. Which method for production sort? **Usually built-in sorted/list.sort.**
**Challenge:** Modify binary search to find the first occurrence among duplicates and test duplicate/missing values.

## Real-world use cases — where, when and how
1. **Contact search:** Where: address book. When records are in small unsorted lists. How: use linear search; for sorted data use binary search.
2. **Leaderboard:** Where: games or scores. When ranking is needed. How: sort on score and a tie-break key.
3. **Product sorting:** Where: catalogues. When user chooses price/name. How: built-in sorted with a field key.
4. **Route/lookup table:** Where: pre-sorted static data. When repeated lookup justifies sorting once. How: binary search sorted data and benchmark trade-offs.
5. **Batch report:** Where: export. When original order should remain available. How: create a sorted copy rather than mutate source.


## 10. Completion
- [ ] Search code passes hit/miss and boundary tests.
- [ ] I can explain complexities.
- [ ] I completed the duplicate-first challenge.
