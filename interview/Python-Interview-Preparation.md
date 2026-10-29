# Python Interview Preparation — Concepts, Questions and Coding Practice

This is a separate interview-preparation section for beginner Python learners. It covers important concepts, direct interview answers, coding questions, problem-solving approaches, dry runs, and project discussion.

> AI assistance disclosure: AI assisted with organising this guide and suggesting practice material. Run and understand the code yourself; do not claim examples were tested unless you actually ran them.

## How to answer an interview question

For theory: define the concept, explain how it works, give an example, and mention a practical use.

For coding:
1. Clarify input, output and constraints.
2. Work through a small example by hand.
3. Choose and explain an approach.
4. Write readable code.
5. Dry-run variable changes.
6. Test normal, boundary and invalid cases.
7. Explain time and space complexity where relevant.

---

# Part A — Important concepts and interview answers

## 1. What is Python?
Python is a high-level, general-purpose programming language known for readable syntax. It is used for automation, web development, testing, data processing and AI/ML applications.

Example:
    message = "Hello, Python"
    print(message)

## 2. What is a variable?
A variable is a name that refers to a value/object. Python does not require you to declare a variable's type first.

    age = 23
    age = "twenty-three"
    print(age)

This is allowed, but keeping a variable's meaning consistent generally improves readability.

## 3. What are common built-in data types?
- int: integers, e.g. 10
- float: decimal floating-point values, e.g. 3.14
- str: text, e.g. "Python"
- bool: True or False
- list: ordered, mutable collection
- tuple: ordered, immutable sequence
- set: collection of unique hashable values
- dict: key-value mapping
- NoneType: the type of None

Use type(value) to inspect a value's type.

## 4. Mutable versus immutable objects
A mutable object can be changed after creation; an immutable object cannot be changed in place.

    numbers = [1, 2]
    numbers.append(3)
    text = "cat"
    text = text + "s"
    print(numbers, text)

Lists and dictionaries are mutable; strings and integers are immutable. This matters when objects are passed to functions or copied.

## 5. List versus tuple
Both are ordered sequences. Lists are mutable and usually written with square brackets. Tuples are immutable sequences and usually written with parentheses.

    fruits = ["apple", "mango"]
    point = (10, 20)
    fruits.append("orange")
    print(fruits)
    print(point[0])

Use a list when the collection needs to change; use a tuple for a fixed sequence.

## 6. What is a dictionary?
A dictionary stores key-value pairs. Keys must be hashable.

    person = {"name": "Adil", "age": 23}
    print(person["name"])
    print(person.get("city", "Not provided"))

Indexing a missing key raises KeyError; get() can supply a default. Dictionaries are useful for lookups and counting frequencies.

## 7. What is a set?
A set stores unique hashable values and is useful for membership checks and removing duplicates when order is not the main requirement.

    print(set([2, 2, 3, 4, 4]))

Do not rely on a set's display order.

## 8. Difference between = and ==?
The single equals sign assigns a value; the double equals sign compares values.

    score = 90
    print(score == 90)  # True

## 9. Difference between /, // and %?
/ performs true division; // performs floor division; % returns the remainder.

    print(7 / 2)   # 3.5
    print(7 // 2)  # 3
    print(7 % 2)   # 1

Floor division rounds down, so -7 // 2 is -4.

## 10. What does input() return?
input() returns a string. Convert it before numeric calculations.

    number = int(input("Enter an integer: "))
    print(number + 1)

Invalid numeric text raises ValueError, so real programs should validate input.

## 11. if, elif and else
These branches select which block runs. Conditions are checked in order, so ordering matters when conditions overlap.

    marks = 82
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Needs improvement")

## 12. for versus while
A for loop iterates over an iterable. A while loop repeats while its condition is true.

    for value in [10, 20, 30]:
        print(value)

    count = 1
    while count <= 3:
        print(count)
        count += 1

A while loop needs a path toward a false condition to avoid running forever.

## 13. What does range(1, 5) mean?
It represents 1, 2, 3, 4; the stop value is excluded.

    print(list(range(1, 5)))  # [1, 2, 3, 4]

## 14. break versus continue
break exits the nearest loop. continue skips the rest of the current iteration and starts the next one.

    for number in range(1, 6):
        if number == 2:
            continue
        if number == 5:
            break
        print(number)

Output: 1, 3, 4.

## 15. What is a function? What are parameters and arguments?
A function is reusable code. Parameters are names in its definition; arguments are values supplied in a call.

    def add(a, b):
        return a + b

    print(add(3, 4))  # 7

## 16. return versus print()
print() displays output. return sends a result to the caller and ends that function call. A function without an explicit return value returns None.

    def add(a, b):
        return a + b

    result = add(2, 5)
    print(result)  # 7

## 17. What are local and global variables?
A local variable is defined inside a function. A global name is defined at module level. Passing values as arguments and returning results often makes functions easier to test than changing global state.

    rate = 2
    def calculate(value):
        return value * rate
    print(calculate(5))  # 10

## 18. What is indexing and slicing?
Sequences use zero-based indexing. A slice selects a range with start included and stop excluded.

    letters = ["a", "b", "c", "d"]
    print(letters[0])     # a
    print(letters[1:3])   # ['b', 'c']
    print(letters[::-1])  # ['d', 'c', 'b', 'a']

An invalid index raises IndexError; slices can return a shorter sequence.

## 19. What is exception handling?
Exceptions signal errors during execution. try/except can handle expected failures.

    try:
        age = int("not a number")
    except ValueError:
        print("Please provide a valid integer")

Catch specific exceptions where possible instead of hiding all errors.

## 20. Syntax, runtime and logic errors
- Syntax error: code cannot be parsed, e.g. a missing colon.
- Runtime error: execution raises an exception, e.g. division by zero.
- Logic error: code runs but returns the wrong answer.

Debug by reading the traceback, inspecting the failing line and values, reproducing a small case, fixing the cause and retesting.

## 21. What is a module?
A module is a Python file containing reusable definitions. For example:

    import math
    print(math.sqrt(25))  # 5.0

Modules help separate code into logical units.

## 22. What is object-oriented programming?
OOP organises code around objects with attributes and methods. A class defines how objects are created.

    class Dog:
        def __init__(self, name):
            self.name = name
        def speak(self):
            return f"{self.name} says woof"

    pet = Dog("Milo")
    print(pet.speak())

self refers to the instance for an instance method.

## 23. What is a list comprehension?
A compact way to build a list from an iterable, optionally filtering items.

    squares = [n * n for n in range(1, 6)]
    print(squares)  # [1, 4, 9, 16, 25]

Use it when it improves clarity; a loop is preferable for complicated logic.

## 24. What is time complexity?
Time complexity describes how an algorithm's work grows with input size. Typical examples: list index access O(1), scanning a list O(n), nested full loops O(n²), and binary search on sorted data O(log n).

Complexity depends on the operation and assumptions, not just the number of code lines.

## 25. Alias versus shallow copy
An alias is another name for the same object. A shallow copy creates a new outer collection but shares nested objects.

    original = [[1, 2], [3, 4]]
    alias = original
    copied = original.copy()
    alias[0].append(99)
    print(original)
    print(copied)

Both display the changed inner list because the nested list is shared. For nested mutable structures, learn when copy.deepcopy() is appropriate.

---

# Part B — Coding questions with approach, code and dry run

## 1. Even or odd

**Approach:** An even integer has remainder zero when divided by 2.

    def even_or_odd(n):
        if n % 2 == 0:
            return "Even"
        return "Odd"

    print(even_or_odd(8))  # Even
    print(even_or_odd(7))  # Odd

**Dry run for 7:** 7 % 2 is 1, so the condition is false and the function returns "Odd".
**Complexity:** O(1) time and O(1) extra space.

## 2. Largest of three numbers

**Approach:** Compare each value with the other two. Using >= handles ties.

    def largest_of_three(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        return c

    print(largest_of_three(12, 8, 15))  # 15
    print(largest_of_three(5, 5, 2))    # 5

**Dry run:** For 12, 8, 15, the first and second conditions fail; return 15.
**Complexity:** O(1) time and O(1) extra space.

## 3. Sum from 1 through n

**Approach:** Start at zero and accumulate each number through n.

    def sum_to_n(n):
        if n < 1:
            return 0
        total = 0
        for number in range(1, n + 1):
            total += number
        return total

    print(sum_to_n(5))  # 15

**Dry run:** total changes 0 → 1 → 3 → 6 → 10 → 15.
**Complexity:** O(n) time and O(1) extra space.

## 4. Factorial

**Approach:** Multiply the integers from 1 through n. Starting at 1 handles 0! = 1.

    def factorial(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        result = 1
        for value in range(1, n + 1):
            result *= value
        return result

    print(factorial(5))  # 120
    print(factorial(0))  # 1

**Dry run for 4:** result changes 1 → 1 → 2 → 6 → 24.
**Complexity:** O(n) time, O(1) extra space.

## 5. Prime-number check

**Approach:** Values below 2 are not prime. Check possible divisors only while divisor squared is at most n.

    def is_prime(n):
        if n < 2:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    for value in [1, 2, 9, 17, 25]:
        print(value, is_prime(value))

Expected: 1 False; 2 True; 9 False; 17 True; 25 False.

**Dry run for 9:** 2 does not divide 9; 3 divides 9 evenly, so return False.
**Complexity:** O(√n) time, O(1) extra space.

## 6. Fibonacci sequence

**Approach:** Keep two consecutive values. Append the first, then update the pair.

    def fibonacci(count):
        if count < 0:
            raise ValueError("count must be non-negative")
        a, b = 0, 1
        sequence = []
        for _ in range(count):
            sequence.append(a)
            a, b = b, a + b
        return sequence

    print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]

**Dry run:** Begin with (0, 1); append 0 and update to (1, 1), then append 1 and update to (1, 2).
**Complexity:** O(count) time, O(count) output space.

## 7. Count digits

**Approach:** Use abs() to handle negatives. Handle zero separately, then remove one digit per integer division by 10.

    def count_digits(n):
        n = abs(n)
        if n == 0:
            return 1
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    print(count_digits(12345))  # 5
    print(count_digits(0))      # 1
    print(count_digits(-72))    # 2

**Dry run for 456:** input changes 456 → 45 → 4 → 0; count becomes 3.
**Complexity:** O(d) time for d digits, O(1) extra space.

## 8. Reverse an integer

**Approach:** Extract the final digit with %, append it to the result after multiplying the result by 10, and remove the digit with //.

    def reverse_number(n):
        sign = -1 if n < 0 else 1
        n = abs(n)
        result = 0
        while n > 0:
            digit = n % 10
            result = result * 10 + digit
            n //= 10
        return sign * result

    print(reverse_number(1234))  # 4321
    print(reverse_number(-120))  # -21

**Dry run for 123:** result changes 0 → 3 → 32 → 321. Leading zeros are not preserved in integers.
**Complexity:** O(d) time, O(1) extra space.

## 9. Count vowels and consonants

**Approach:** Iterate over characters. Check the current character, not the whole string. Ignore spaces and punctuation using isalpha().

    def count_letters(text):
        vowels = "aeiou"
        vowel_count = 0
        consonant_count = 0
        for ch in text.lower():
            if ch.isalpha():
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        return vowel_count, consonant_count

    print(count_letters("Python by me!"))  # (2, 8)

**How to solve:** Identify one character, classify it, then update the right counter.
**Complexity:** O(n) time, O(1) extra space for fixed-size counters.

## 10. Palindrome string

**Approach:** Define the rules first. Here, ignore spaces, punctuation and case; then compare the cleaned text to its reverse.

    def is_palindrome(text):
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]

    print(is_palindrome("Never odd or even"))  # True
    print(is_palindrome("Python"))             # False

**Complexity:** O(n) time and O(n) extra space.

## 11. Largest list value without max()

**Approach:** Reject an empty list. Start with the first value, not zero, so lists of negative numbers work correctly.

    def largest_value(values):
        if not values:
            raise ValueError("values must not be empty")
        largest = values[0]
        for value in values[1:]:
            if value > largest:
                largest = value
        return largest

    print(largest_value([-5, -2, -9]))  # -2

**Complexity:** O(n) time. The slice creates an O(n) temporary list; iterating by index avoids that extra copy.

## 12. Remove duplicates while preserving order

**Approach:** Add a value only if it has not already been added. This simple approach is easy to understand, but list membership makes it O(n²) in the worst case.

    def unique_in_order(values):
        result = []
        for value in values:
            if value not in result:
                result.append(value)
        return result

    print(unique_in_order([3, 1, 3, 2, 1]))  # [3, 1, 2]

For hashable values, a set of seen values can improve expected lookup time while the result list preserves order.

## 13. Character frequency using a dictionary

**Approach:** Count each character in a dictionary. get(ch, 0) returns zero when the character has not appeared yet.

    def character_frequency(text):
        frequency = {}
        for ch in text:
            frequency[ch] = frequency.get(ch, 0) + 1
        return frequency

    print(character_frequency("aba"))  # {'a': 2, 'b': 1}

**Dry run:** first 'a' gives count 1, 'b' gives count 1, second 'a' increments a to 2.
**Complexity:** Expected O(n) time and O(k) space for k distinct characters.

## 14. FizzBuzz

**Problem:** For numbers 1 through n, use Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for both, otherwise the number as text.

**Approach:** Check the combined case first, or multiples of 15 will be caught by the condition for 3.

    def fizz_buzz(n):
        result = []
        for value in range(1, n + 1):
            if value % 3 == 0 and value % 5 == 0:
                result.append("FizzBuzz")
            elif value % 3 == 0:
                result.append("Fizz")
            elif value % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(value))
        return result

    print(fizz_buzz(5))  # ['1', '2', 'Fizz', '4', 'Buzz']

**Complexity:** O(n) time and O(n) output space.

## 15. Two Sum

**Problem:** Return indexes of two distinct elements that add to the target. This version returns None if no pair exists.

**Approach:** For each number, calculate the needed partner. Look for it in a dictionary of previously seen values before storing the current number.

    def two_sum(numbers, target):
        seen = {}
        for index, number in enumerate(numbers):
            needed = target - number
            if needed in seen:
                return [seen[needed], index]
            seen[number] = index
        return None

    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 3], 6))          # [0, 1]

**Dry run:** At index 0, value 2 needs 7, so store {2: 0}. At index 1, value 7 needs 2; the dictionary has 2 at index 0, so return [0, 1].
**Complexity:** Expected O(n) time and O(n) extra space.

---

# Part C — Project interview questions

## 1. Explain your Name Management project.
Suggested answer: "I created a beginner Python console project to practise functions, conditions and lists. It can add active names, prevent duplicate active names, delete names, restore deleted names and display counts. The current version stores data in memory, so it is lost when the program exits. Improvements I plan to make include a menu, automated tests, case-insensitive matching and file persistence."

Use this only if it accurately describes the version you have actually built and understand.

## 2. Why did you use functions?
Functions separate operations into small units, reduce repeated code, improve readability and make individual operations easier to test.

## 3. What are the project's limitations?
It uses in-memory lists, so it does not persist data. Matching is case-sensitive and the current design lacks automated tests and robust validation for every input. Explaining limitations shows that you can review your work critically.

## 4. How would you test it?
Test successful add, delete and restore operations, plus blank names, duplicates, deleting a missing name, restoring a name that is not deleted, restoring an already active name and viewing empty lists. After separating logic from user input, test each operation independently.

## 5. Tell me about a bug you fixed.
Use a real example from your own work. Explain expected behaviour, actual behaviour, reproduction steps, root cause, fix and the test that prevents recurrence. Do not invent a bug story.

## 6. How do you approach an unfamiliar coding problem?
Restate the requirements, write a small example, identify edge cases, choose a straightforward approach, implement it, dry-run it, test boundaries and then consider efficiency.

## 7. Why should a recruiter review this repository?
Suggested answer: "This repository documents my Python learning through explanations, examples, practice problems and a small project. I am working to demonstrate that I can explain my decisions, test edge cases, identify limitations and improve my work. I disclose AI assistance and take responsibility for understanding and verifying the content."

Adapt the answer to work you have actually completed.

---

# Part D — Common mistakes

1. Returning a function name instead of the computed result.
2. Using print() where the caller needs a returned value.
3. Checking the entire string instead of the current character.
4. Forgetting that input() returns a string.
5. Forgetting that range() excludes its stop value.
6. Forgetting to update a while-loop condition.
7. Treating 1 as prime.
8. Forgetting that zero has one digit.
9. Initialising a largest-value search to zero when all values might be negative.
10. Removing a list item without checking whether it exists.
11. Assuming list indexes stay unchanged after deletion.
12. Testing only ordinary inputs instead of zero, negatives, empty lists, duplicates and invalid values.
13. Claiming code has been tested without actually running it.
14. Memorising an answer without being able to explain the logic.

# Part E — Self-assessment checklist

- [ ] Explain variables and built-in data types.
- [ ] Explain conditions, loops, counters and accumulators.
- [ ] Write a function and explain parameters, arguments and return.
- [ ] Solve even/odd, largest-of-three and sum problems.
- [ ] Solve factorial, prime, Fibonacci and digit-count problems.
- [ ] Process strings and explain palindrome logic.
- [ ] Work with lists and dictionaries.
- [ ] Dry-run code line by line.
- [ ] Test zero, negative, empty, duplicate and missing inputs where relevant.
- [ ] Explain time and space complexity for these algorithms.
- [ ] Explain the Name Management project's actual features and limitations.

## Suggested practice plan

- Session 1: Concepts 1–10; explain each answer aloud.
- Session 2: Conditions, loops, functions and collections.
- Session 3: Coding questions 1–7; dry-run each loop.
- Session 4: Coding questions 8–15; explain data structures and complexity.
- Session 5: Project questions; demonstrate the actual project honestly.
- Session 6: Repeat missed questions without reading the answers first.
