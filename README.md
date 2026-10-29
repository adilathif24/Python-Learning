# My Python Learning Journey 🐍

Hi! I am learning Python step by step and using this repository to keep my notes, practice programs, mistakes, and mini-projects in one place. I write and run examples as I learn, then add explanations so I can revise them later and prepare for interviews.

> **AI assistance:** I use AI as a study helper to explain concepts, review errors, and organise notes. The examples are learning material that I should run, understand, test, and adapt myself. I disclose this assistance rather than presenting AI help as something it was not.

## What I have practised so far
- Python statements, print(), variables, basic types, operators
- Conditions: if, elif, else
- Loops: for, while, range()
- Counters and accumulators
- Functions: def, parameters, arguments, function calls, return
- Lists, indexing, append(), remove(), len(), in, not in
- Coding exercises: sum, multiplication table, factorial, prime check, Fibonacci, digit count, vowel/consonant count, swapping
- Name Management mini-project: add, remove, restore, view
- Practice and interview questions

## 1. Python basics

### Output and variables
A variable is a name that refers to a value. Common types: int (whole number), float (decimal), str (text), and bool (True/False).
~~~python
name = "Adil"
age = 23
print("Hello", name)
print(age)
~~~
print() displays output. Use variables to store data for later calculations and decisions.

### Operators
~~~python
a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3: floor division
print(a % b)   # 1: remainder
print(a ** b)  # 1000: power
~~~
Use ==, !=, >, <, >=, <= to compare values. = assigns a value; == compares two values.

## 2. Conditions

Conditions let a program make decisions.
~~~python
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Passed")
else:
    print("Keep practising")
~~~
**Why/where:** input validation, grading, login checks, and deciding whether an item can be removed or restored. Put a colon after each condition and indent the body consistently.

## 3. Loops, counters and accumulators

A for loop iterates over a sequence. A while loop repeats while a condition is true.
~~~python
for i in range(1, 6):
    print(i)  # 1 through 5; stop value is excluded

a = 1
while a <= 5:
    print(a)
    a += 1
~~~
Always update a while-loop variable so the condition eventually becomes false.

An **accumulator** collects a running result; a **counter** tracks how many times something happens.
~~~python
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
~~~
Multiplication table:
~~~python
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
~~~

## 4. Functions: definition, syntax, parameters and arguments

A **function** is a reusable block of code that performs a task. def defines it; calling it executes it.
~~~python
def greet(name):       # name is a parameter
    print("Hello", name)

greet("Adil")          # "Adil" is an argument
~~~
A **parameter** is named in the definition; an **argument** is the actual value passed to the call.

return sends a value back to the caller; print() only displays it.
~~~python
def add(a, b):
    return a + b

answer = add(4, 6)
print(answer)  # 10
~~~
**Why use functions?** Reuse logic, organise code, improve readability, and test small pieces independently. Real-world uses include calculations, data validation, reporting, and application logic.

Common mistakes: forgetting to call a function, incorrect indentation, forgetting the colon, or returning the function name instead of the calculated result. A function without an explicit return returns None.

## 5. Lists and membership

A **list** is an ordered, mutable collection. Indexing starts at zero.
~~~python
names = ["Syed", "Adil", "Ali"]
print(names[0])       # Syed
names.append("Athif") # add at the end
print(len(names))     # current item count
print("Ali" in names) # True
print("Ravi" not in names) # True
names.remove("Adil")  # remove first matching value
print(names)
~~~
- append(value): add one item at the end.
- remove(value): remove the first matching value; raises ValueError if absent.
- len(items): number of items currently in the list.
- value in items: membership test.
- items[0]: first item.
Lists can contain duplicates. Removing an item shifts later items left, so their indexes change. Check membership before removing when a missing item is possible.

## 6. Eight worked coding examples

### Example 1 — Sum 1 to 10
~~~python
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
~~~
The accumulator adds each number to the running total.

### Example 2 — Factorial
Factorial is the product of positive integers up to n; by definition, 0! = 1.
~~~python
def factorial(n):
    if n < 0:
        return "Not defined for negative integers"
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(5))  # 120
print(factorial(0))  # 1
~~~
Multiply the result by n, then decrease n. Return the computed value.

### Example 3 — Prime check
A prime integer is greater than 1 and has no positive divisors except 1 and itself.
~~~python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(12))  # False
~~~
Testing divisors up to the square root is sufficient.

### Example 4 — Fibonacci sequence
~~~python
a, b = 0, 1
for _ in range(8):
    print(a, end=" ")
    a, b = b, a + b
# 0 1 1 2 3 5 8 13
~~~
Each new term is the sum of the previous two.

### Example 5 — Count digits
~~~python
n = abs(12345)
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print(count)  # 5
~~~
Floor-dividing by 10 removes the last digit. Zero needs a special case.

### Example 6 — Count vowels and consonants
~~~python
text = "python by me"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for ch in text.lower():
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
~~~
Check the current character ch, not the whole string. isalpha() skips spaces and punctuation.

### Example 7 — Swap using a third variable
~~~python
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)  # 20 10
~~~

### Example 8 — Swap without a third variable
~~~python
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10
~~~
Python multiple assignment swaps the values directly.

## 7. Name Management mini-project

Lists used:
- names: currently active names.
- deleted: deleted names that have not been restored.
- restore: history of successful restorations.

~~~python
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
        print("No suitable name to delete")

def restoreName(name):
    if name in names:
        print("Name already exists in active names")
    elif name in deleted:
        deleted.remove(name)
        names.append(name)
        restore.append(name)
        print("Restored successfully =", name)
    else:
        print("Name not found in deleted list")

def viewname():
    print("Active names:", names)
    print("Total active names:", len(names))
    print("Deleted names:", deleted)
    print("Total currently deleted:", len(deleted))
    print("Restoration history:", restore)

addname("syed adil")
addname("syed")
addname("adil")
addname("ali")
addname("athif")
removename("syed adil")
removename("adil")
viewname()
restoreName("syed adil")
restoreName("adil")
viewname()
~~~

**How it works:** addname() prevents an active duplicate; removename() checks before removing and records the deletion; restoreName() avoids duplicate active names and restores only a deleted name; viewname() shows current lists and counts.

**Index lesson:** if names = ["Adil", "Syed", "Ali"] and you remove "Adil", the list becomes ["Syed", "Ali"]. Now names[1] is "Ali", not "Syed". Pass the intended name directly when possible.

**Limitations:** Lists live only in memory, so data disappears when the program exits. String comparisons are case-sensitive ("Adil" and "adil" differ). A real application may need persistent storage, input validation, permissions, and audit logs.

## 8. Five practice questions with solutions

### Q1. Multiply two numbers using a function
~~~python
def multiply(a, b):
    return a * b
print(multiply(4, 5))  # 20
~~~

### Q2. Add a value only if it is not already present
~~~python
numbers = [2, 4, 6]
value = 4
if value not in numbers:
    numbers.append(value)
print(numbers)  # [2, 4, 6]
~~~

### Q3. Count items in a list
~~~python
names = ["A", "B", "C"]
print(len(names))  # 3
~~~

### Q4. Safely remove a task
~~~python
tasks = ["study", "code"]
task = "code"
if task in tasks:
    tasks.remove(task)
print(tasks)  # ['study']
~~~

### Q5. Count numbers greater than 10
~~~python
numbers = [4, 12, 18, 7, 10]
count = 0
for number in numbers:
    if number > 10:
        count += 1
print(count)  # 2
~~~

## 9. Interview questions and answers

1. **What is Python?** A high-level, general-purpose programming language.
2. **What is a variable?** A name that refers to a value.
3. **What is a function?** Reusable code that performs a task.
4. **What does def do?** Defines a function.
5. **Parameter vs argument?** A parameter is in the definition; an argument is passed to the call.
6. **print() vs return?** print() displays; return sends a value to the caller.
7. **What is a loop?** A structure that repeats code.
8. **for vs while?** for iterates over an iterable; while repeats while a condition is true.
9. **What is an accumulator?** A variable that collects a running result.
10. **What is a list?** An ordered, mutable collection.
11. **Can a list contain duplicates?** Yes.
12. **What does append() do?** Adds an item to the end.
13. **What does remove() do?** Removes the first matching value.
14. **What does len() return?** Current item count.
15. **What does in do?** Checks membership and returns a Boolean.
16. **What is zero-based indexing?** The first item has index 0.
17. **Why do indexes change after deletion?** Later items shift left.
18. **Why check before removing?** To avoid ValueError for a missing value.
19. **What is a prime number?** An integer greater than 1 divisible only by 1 and itself.
20. **What is factorial?** Product of integers from 1 through n; 0! = 1.
21. **What is Fibonacci?** A sequence where each term is the sum of the previous two.
22. **What does // do?** Floor division.
23. **What does % do?** Returns a remainder.
24. **Why use ch in vowels in a loop?** ch is the current character; testing the whole string checks the wrong value.
25. **How could the mini-project improve?** Add a menu, tests, validation, and persistent storage.

## 10. Common mistakes

- Forgetting a colon or using incorrect indentation.
- Using = instead of == for comparison.
- Forgetting to update a while loop variable.
- Using a wrong loop condition, such as while n < 0 when processing a positive number.
- Returning the function name instead of the calculated answer.
- Checking the whole string instead of the current character in vowel counting.
- Removing a missing item without checking membership.
- Assuming indexes remain unchanged after deletion.
- Confusing the current list length with the total number ever added.

## 11. My next practice steps

1. Type and run each example myself instead of only copying it.
2. Predict output before running it.
3. Test edge cases: zero, negative numbers, empty lists, missing names, and duplicates.
4. Explain each variable and line in my own words.
5. Try the five practice questions without viewing the solutions first.
6. Extend the mini-project with a menu: Add, Delete, Restore, View, Exit.
7. Next, I plan to learn file handling and databases so records can be saved between runs.

## AI assistance disclosure

These notes were organised and drafted with AI assistance from the learner's practice code and questions. AI helped explain concepts, identify common mistakes, and prepare examples and interview questions. The learner should test and understand the code and disclose AI assistance honestly when sharing the repository.
