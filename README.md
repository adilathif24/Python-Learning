# Python Learning — Beginner Notes and Mini Project

> **AI assistance disclosure:** These notes were prepared with AI assistance based on the code and concepts practised during learning. They are learning material, not a claim that every line was written independently without help. Run, review, and modify the examples so you can explain them yourself in interviews.

## Topics covered
- Functions with `def`; function definition vs function call
- Parameters and arguments
- Lists, zero-based indexing, `append()`, `remove()`, and `len()`
- `if` / `else`, `in`, and `not in`
- Active, deleted, and restored lists
- Safe deletion, restoring names, counting, and viewing data
- Common mistakes, worked examples, practice questions, and interview Q&A

## 1. Function: definition, syntax, and purpose

A **function** is a reusable block of code that performs a specific task. Functions help avoid repeated code, improve readability, and make logic easier to test and maintain.

```python
def function_name(parameters):
    # indented function body
    print("Task completed")

function_name(arguments)  # calling the function
```

- `def` starts a function definition.
- The function name identifies the task.
- Parameters are variables that receive input.
- The colon `:` starts the function body; indentation matters.
- Defining a function does not execute its body. Calling it does.

### Parameter vs argument

```python
def greet(name):       # name is a parameter
    print("Hello", name)

greet("Adil")          # "Adil" is an argument
```

A **parameter** appears in the function definition. An **argument** is the actual value supplied in a function call.

### print() vs return

`print()` displays a value; `return` sends a value back to the caller.

```python
def count_items(items):
    return len(items)

total = count_items(["a", "b"])
print(total)  # 2
```

A function without an explicit `return` returns `None` by default.

## 2. Lists and useful operations

A **list** is an ordered, mutable collection of items. It can hold multiple values and can be changed after creation.

```python
names = ["Syed", "Adil", "Ali"]
print(names[0])       # Syed: indexing starts at 0
names.append("Athif") # add an item to the end
names.remove("Adil")  # remove the first matching value
print(len(names))     # number of current items
print("Ali" in names) # True if present
print("Ravi" not in names)
```

- `append(value)`: adds one item to the end.
- `remove(value)`: removes the first matching value; raises `ValueError` if missing.
- `len(list)`: counts the elements currently in the list.
- `value in list`: checks whether a value is present.
- `value not in list`: checks whether a value is absent.
- `if` / `else`: chooses which block of code to run based on a condition.

### Why, where, and how are these useful?
- **Functions:** reusable calculations, validation, report generation, and application operations.
- **Lists:** contacts, tasks, shopping-cart items, student records, and inventory.
- **Conditions:** validating input and choosing an action.
- **Membership checks:** preventing duplicate entries and checking before deletion.
- **len():** counting current tasks, records, or results.
- **Separate active/deleted/restore lists:** demonstrating a simple undo/restore workflow. Real applications normally need persistent storage and audit history.

## 3. Five worked examples

### Example 1 — Greeting function

```python
def greet(name):
    print("Hello", name)

greet("Adil")
greet("Syed")
```

Output:
```text
Hello Adil
Hello Syed
```

**Explanation:** The same function is reused with different arguments. This pattern is useful for personalised greetings and messages.

### Example 2 — Add a name only if it is not already present

```python
names = []

def addname(name):
    if name not in names:
        names.append(name)
        print("New name added =", name)
    else:
        print("Name already exists")

addname("Adil")
addname("Syed")
addname("Adil")
print(names)
```

**Explanation:** `not in` checks for an existing name before `append()`. String comparisons are case-sensitive: `"Adil"` and `"adil"` are different values. This is a basic duplicate-prevention pattern.

### Example 3 — Delete a name safely

```python
names = ["Adil", "Syed", "Ali"]
deleted = []

def removename(name):
    if name in names:
        names.remove(name)
        deleted.append(name)
        print("Deleted successfully =", name)
    else:
        print("No suitable name to delete")

removename("Syed")
removename("Ravi")
print("Active:", names)
print("Deleted:", deleted)
```

**Explanation:** Check membership before calling `remove()` to avoid a missing-value error. A successful deletion moves the name into a separate list. This is similar to removing a task or contact from an active collection.

### Example 4 — Restore a deleted name safely

```python
names = ["Adil", "Ali"]
deleted = ["Syed"]
restore = []

def restoreName(name):
    if name in names:
        print("Name already exists in active names")
    elif name in deleted:
        deleted.remove(name)
        names.append(name)
        restore.append(name)
        print("Restored successfully =", name)
    else:
        print("Name not found in deleted names")

restoreName("Syed")
restoreName("Adil")
restoreName("Ravi")
print("Active:", names)
print("Deleted:", deleted)
print("Restored history:", restore)
```

**Explanation:** First avoid duplicates in the active list. If the name is in the deleted list, move it back and record the successful restoration. Otherwise, report that it was not found.

### Example 5 — View lists and counts

```python
names = ["Adil", "Ali"]
deleted = ["Syed"]
restore = ["Athif"]

def viewname():
    print("Active names:", names)
    print("Number of active names:", len(names))
    print("Deleted names:", deleted)
    print("Number currently deleted:", len(deleted))
    print("Restoration history:", restore)

viewname()
```

**Explanation:** `len()` counts current elements. The active count is not the total number of names ever added. This is useful for a simple report or dashboard.

## 4. Combined mini project — Name Management System

```python
names = []
deleted = []
restore = []

def addname(name):
    if name not in names:
        names.append(name)
        print("New name added =", name)
    else:
        print("Name already exists")

def removename(name):
    if name in names:
        names.remove(name)
        deleted.append(name)
        print("Name deleted successfully =", name)
    else:
        print("Name not found in active names")

def restoreName(name):
    if name in names:
        print("Name already exists in active names")
    elif name in deleted:
        deleted.remove(name)
        names.append(name)
        restore.append(name)
        print("Restored successfully =", name)
    else:
        print("Name not found in deleted names")

def viewname():
    print("\n--- Name Management Report ---")
    print("Active names:", names)
    print("Number of active names:", len(names))
    print("Deleted names:", deleted)
    print("Number currently deleted:", len(deleted))
    print("Restoration history:", restore)

addname("syed adil")
addname("syed")
addname("adil")
addname("ali")
addname("athif")
removename("syed adil")
removename("adil")
restoreName("syed adil")
restoreName("Rahul")
addname("syed")  # duplicate check
viewname()
```

### How the project works
- `names`: names currently active.
- `deleted`: names deleted but not restored.
- `restore`: history of successful restorations.
- `addname()`: adds a name if it is not active already.
- `removename()`: moves an active name to the deleted list.
- `restoreName()`: moves a deleted name back and records the restoration.
- `viewname()`: prints lists and current counts.

### Important index lesson

```python
names = ["Adil", "Syed", "Ali", "Athif"]
names.remove("Adil")
print(names)     # ['Syed', 'Ali', 'Athif']
print(names[1])  # Ali, not Syed
```

List indexes are positions, not permanent identifiers. Removing an earlier item shifts later values left. Passing the intended name directly is clearer than relying on an index that may change.

### Limitations
This is a beginner practice project. The lists exist only in memory and data disappears when the program stops. Real applications need persistence, validation, access controls, and reliable audit logs.

## 5. Five practice questions with answers

### Q1. Write a function to return the square of a number.

```python
def square(number):
    return number * number

print(square(4))  # 16
print(square(7))  # 49
```

**Explanation:** The parameter receives the input and `return` sends the calculated result back to the caller.

### Q2. Check whether a name is present.

```python
names = ["Adil", "Syed", "Ali"]
if "Syed" in names:
    print("Found")
else:
    print("Not found")
```

**Output:** `Found`. The `in` operator returns a Boolean result.

### Q3. Count elements in a list.

```python
names = ["Adil", "Syed", "Ali"]
print(len(names))  # 3
```

**Explanation:** `len()` counts current elements.

### Q4. Show how indexes change after removal.

```python
names = ["Adil", "Syed", "Ali"]
print(names[1])  # Syed
names.remove("Adil")
print(names[1])  # Ali
```

**Explanation:** Removing the first element shifts the remaining elements left.

### Q5. Restore a deleted name without creating a duplicate.

```python
names = ["Adil"]
deleted = ["Syed"]
restore = []

def restoreName(name):
    if name in names:
        print("Name already exists")
    elif name in deleted:
        deleted.remove(name)
        names.append(name)
        restore.append(name)
        print("Restored successfully")
    else:
        print("Name not found in deleted names")

restoreName("Syed")
restoreName("Adil")
restoreName("Ravi")
```

**Explanation:** Check active names first, then deleted names. Only a successful move updates the restoration history.

## 6. Interview questions and answers

1. **What is a function?** A reusable block of code designed for a particular task.
2. **Which keyword defines a function?** `def`.
3. **Definition vs call?** Defining creates the function; calling executes its body.
4. **What is a parameter?** A variable in the function definition that receives input.
5. **What is an argument?** The value passed to a function call.
6. **What is a list?** An ordered, mutable collection of items.
7. **Can lists contain duplicates?** Yes.
8. **What does `append()` do?** Adds one item to the end of a list.
9. **What does `remove()` do?** Removes the first matching value; it raises `ValueError` if the value is absent.
10. **What does `len()` return?** The number of items currently in a collection.
11. **What does `in` do?** Checks whether a value is present.
12. **What does `not in` do?** Checks whether a value is absent.
13. **What is zero-based indexing?** The first element has index `0`.
14. **Why check before removing?** To avoid removing a value that is not present.
15. **Difference between `print()` and `return`?** `print()` displays output; `return` sends a value back to the caller.
16. **Why did an index refer to a different name after deletion?** Later elements shift left.
17. **Why keep active, deleted, and restored lists separately?** To represent current state and restoration history in this learning example.
18. **What happens if there is no explicit return?** The function returns `None`.
19. **What is one project limitation?** Data is not saved after the program exits.
20. **How can this project be improved?** Add a menu, input validation, tests, and persistent storage.

## 7. Five coding interview questions and answers

### 1. Add a name only if it is not already present

```python
names = ["Adil", "Syed"]
name = "Ali"
if name not in names:
    names.append(name)
print(names)  # ['Adil', 'Syed', 'Ali']
```

### 2. Count items

```python
names = ["Adil", "Syed", "Ali", "Athif"]
print(len(names))  # 4
```

### 3. Delete safely

```python
names = ["Adil", "Syed", "Ali"]
name = "Syed"
if name in names:
    names.remove(name)
print(names)  # ['Adil', 'Ali']
```

### 4. Move a deleted name back to active names

```python
names = ["Adil"]
deleted = ["Syed"]
name = "Syed"
if name in deleted and name not in names:
    deleted.remove(name)
    names.append(name)
print(names)   # ['Adil', 'Syed']
print(deleted) # []
```

### 5. Return the number of active names

```python
names = ["Adil", "Syed", "Ali"]

def count_names():
    return len(names)

print(count_names())  # 3
```

## 8. Common mistakes and fixes

| Mistake | Fix |
|---|---|
| Forgetting parentheses in a function call | Call it like `addname("Adil")` |
| Incorrect indentation | Indent function and condition bodies consistently |
| Removing a missing value | Check `if name in names` first |
| Expecting a history list to update automatically | Append only when the action succeeds |
| Assuming indexes stay unchanged after removal | Inspect the list again or pass the target value directly |
| Printing the whole list when one value is needed | Print the current variable |
| Treating `len(names)` as lifetime additions | Describe it as the current active count |
| Restoring an already-active name | Check `name in names` first |

## 9. Practice plan

1. Type each example yourself.
2. Predict the output before running the code.
3. Test duplicate names, missing names, and empty lists.
4. Explain each function's purpose, parameters, condition, list operation, and result.
5. Add a `searchname(name)` function.
6. Build a menu with Add, Delete, Restore, View, and Exit.
7. Later, save records to a file or database.

## AI assistance disclosure

This guide was drafted with AI assistance from the concepts and code explored during practice. The learner should test, review, adapt, and understand the examples before presenting the project as work they can explain. Be transparent in a portfolio or interview that this was a beginner practice project developed while learning with AI assistance.
