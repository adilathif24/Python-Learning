# Python Fundamentals: Notes, Examples and Practice

These notes cover the concepts practised so far. The goal is understanding and independent problem solving, not memorising answers.

> **AI assistance disclosure:** AI assisted with organising explanations and generating practice material. Code should be run, reviewed, understood and adapted by the learner. The repository does not present AI-assisted material as unaided work.

## How to use these notes

For every example: predict the output, run the code, explain each line, change the input, and test an edge case. Attempt the practice section before reading its solutions.

## 1. Output, variables, types and input

A variable is a name bound to a value. Python is dynamically typed: the type belongs to the value, and a variable can later refer to a value of another type.

    name = "Adil"
    age = 23
    height = 1.80
    is_learning = True

    print(name)
    print(age)
    print(type(height))
    print(is_learning)

Expected output:

    Adil
    23
    <class 'float'>
    True

Common built-in types:
- int: integer, for example 7 or -2
- float: floating-point number, for example 3.5
- str: text, for example "Python"
- bool: True or False
- NoneType: the single value None, used to represent absence of a value

input() returns a string. Convert input when numeric operations are needed.

    name = input("Name: ")
    age = int(input("Age: "))
    print(f"Hello, {name}. Next year you will be {age + 1}.")

This example assumes the user types a valid integer. If the input is "twenty", int(...) raises ValueError; later exception-handling lessons will cover this.

### Example 1 — Bill total

    price = 125.50
    quantity = 2
    total = price * quantity
    print(f"Total: {total:.2f}")

Output: Total: 251.00

### Example 2 — Convert minutes to hours and minutes

    minutes = 135
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(hours, "hours and", remaining_minutes, "minutes")

Output: 2 hours and 15 minutes

### Example 3 — Swap values using a temporary variable

    a = 10
    b = 20
    temp = a
    a = b
    b = temp
    print(a, b)

Output: 20 10

### Example 4 — Swap values with Python assignment

    a = "left"
    b = "right"
    a, b = b, a
    print(a, b)

Output: right left

### Example 5 — Type conversion

    text_number = "42"
    number = int(text_number)
    print(number + 8)

Output: 50

Why it matters: programs use variables for prices, scores, user input, counts, and intermediate calculations. Validate external input before trusting it.

## 2. Operators

| Operator | Purpose | Example result |
|---|---|---|
| + | addition | 3 + 2 gives 5 |
| - | subtraction | 3 - 2 gives 1 |
| * | multiplication | 3 * 2 gives 6 |
| / | true division | 5 / 2 gives 2.5 |
| // | floor division | 5 // 2 gives 2 |
| % | remainder | 5 % 2 gives 1 |
| ** | exponentiation | 2 ** 3 gives 8 |
| == | equality comparison | 3 == 3 gives True |
| != | inequality comparison | 3 != 4 gives True |
| >, <, >=, <= | comparisons | 5 > 2 gives True |
| and, or, not | Boolean logic | combine or invert conditions |

Important distinction: = assigns a value; == compares two values. For negative numbers, // rounds down toward negative infinity, so -5 // 2 is -3.

### Example 6 — Even or odd

    number = 17
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

Output: Odd

### Example 7 — Simple discount rule

    bill = 1200
    if bill >= 1000:
        discount = bill * 0.10
    else:
        discount = 0
    print("Discount:", discount)
    print("Pay:", bill - discount)

Output: Discount: 120.0; Pay: 1080.0

## 3. Conditions

A condition selects a path based on whether an expression is truthy or false.

Syntax:

    if condition:
        statement
    elif another_condition:
        statement
    else:
        statement

Branches are checked in order. Once a branch matches, its body runs and the remaining branches are skipped.

### Example 8 — Grade bands

    marks = 72
    if not 0 <= marks <= 100:
        print("Invalid marks")
    elif marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")

Output: Pass

### Example 9 — Find the largest of three values

    a, b, c = 12, 8, 15
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print(largest)

Output: 15

### Example 10 — Check login input (illustrative only)

    saved_username = "learner"
    entered_username = "learner"
    if entered_username == saved_username:
        print("Username matches")
    else:
        print("Username does not match")

This demonstrates equality only. A real authentication system must not rely on a hard-coded username or omit secure password verification.

## 4. Loops, counters and accumulators

A for loop processes each item in an iterable. range(start, stop, step) generates integers and excludes stop. A while loop repeats while its condition remains true; update the relevant state to avoid an infinite loop.

### Example 11 — Print a range

    for number in range(1, 6):
        print(number)

Output: 1, 2, 3, 4, 5 on separate lines.

### Example 12 — Countdown

    for number in range(5, 0, -1):
        print(number)
    print("Go!")

Output: 5, 4, 3, 2, 1, Go!

### Example 13 — Sum from 1 through n

    n = 5
    total = 0
    for number in range(1, n + 1):
        total += number
    print(total)

Output: 15

Dry run: total begins at 0; then becomes 1, 3, 6, 10, and 15.

### Example 14 — Counter versus accumulator

    numbers = [4, 12, 18, 7, 10]
    count = 0
    total = 0
    for number in numbers:
        count += 1
        total += number
    print("Count:", count)
    print("Total:", total)

Output: Count: 5; Total: 51

A counter tracks occurrences; an accumulator collects a running result.

### Example 15 — Multiplication table

    n = 7
    for multiplier in range(1, 11):
        print(f"{n} x {multiplier} = {n * multiplier}")

### Example 16 — while loop

    number = 1
    while number <= 5:
        print(number)
        number += 1

Output: 1 through 5. If number += 1 is removed, the condition never changes and the loop continues indefinitely.

## 5. Number problems

### Example 17 — Factorial

For a non-negative integer n, n! is the product of integers from 1 through n. By definition, 0! = 1.

    def factorial(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        result = 1
        for value in range(1, n + 1):
            result *= value
        return result

    print(factorial(5))
    print(factorial(0))

Output: 120, then 1.

Dry run for 5: result is 1 → 1 → 2 → 6 → 24 → 120. The function returns the computed result, not the function name. Raising ValueError makes invalid input explicit.

### Example 18 — Prime check

A prime number is an integer greater than 1 with exactly two positive divisors: 1 and itself.

    def is_prime(n):
        if n < 2:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    print(is_prime(2))   # True
    print(is_prime(7))   # True
    print(is_prime(12))  # False
    print(is_prime(1))   # False

It is sufficient to test divisors up to the square root: if n = a * b and both factors were greater than the square root, their product would exceed n.

### Example 19 — Fibonacci sequence

    def fibonacci(count):
        if count < 0:
            raise ValueError("count must be non-negative")
        a, b = 0, 1
        result = []
        for _ in range(count):
            result.append(a)
            a, b = b, a + b
        return result

    print(fibonacci(8))

Output: [0, 1, 1, 2, 3, 5, 8, 13]

### Example 20 — Count digits, including zero and negatives

    def count_digits(number):
        number = abs(number)
        if number == 0:
            return 1
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    print(count_digits(12345))  # 5
    print(count_digits(0))      # 1
    print(count_digits(-908))   # 3

The number is made non-negative with abs(). Each // 10 removes the final decimal digit. Zero needs a special case.

### Example 21 — Sum of digits

    def digit_sum(number):
        number = abs(number)
        total = 0
        while number > 0:
            total += number % 10
            number //= 10
        return total

    print(digit_sum(1234))  # 10
    print(digit_sum(0))     # 0

### Example 22 — Reverse an integer

    def reverse_number(number):
        sign = -1 if number < 0 else 1
        number = abs(number)
        reversed_value = 0
        while number > 0:
            digit = number % 10
            reversed_value = reversed_value * 10 + digit
            number //= 10
        return sign * reversed_value

    print(reverse_number(1234))   # 4321
    print(reverse_number(-120))   # -21

Leading zeros are not preserved in an integer. Reversing 120 produces integer 21, not text "021".

## 6. Strings

Strings are sequences of text characters and are immutable: methods such as lower() return a new string rather than modifying the original string in place.

### Example 23 — Count vowels and consonants

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

The loop checks the current character ch, not the entire input string. isalpha() skips spaces and punctuation. This simple English-vowel rule does not classify every letter in every language.

### Example 24 — Count words

    sentence = "Python is fun to learn"
    words = sentence.split()
    print(len(words))

Output: 5

split() without an argument handles runs of whitespace and avoids empty items between repeated spaces.

### Example 25 — Palindrome text

    def is_palindrome(text):
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]

    print(is_palindrome("Never odd or even"))  # True
    print(is_palindrome("Python"))             # False

This version ignores spaces, punctuation and letter case. Slicing with step -1 reverses the string.

## 7. Functions

A function is a named, reusable block of code. Parameters appear in the definition; arguments are supplied in a call. return passes a result back to the caller and ends that function call. print() displays output and does not substitute for return.

### Example 26 — Return versus print

    def add(a, b):
        return a + b

    answer = add(4, 6)
    print(answer)

Output: 10

If a function only prints a value and does not return one, assigning its call to a variable stores None.

### Example 27 — Default argument

    def greet(name="Learner"):
        return f"Hello, {name}!"

    print(greet())
    print(greet("Adil"))

Output: Hello, Learner! then Hello, Adil!

### Example 28 — Validate a function input

    def percentage(marks, total):
        if total <= 0:
            raise ValueError("total must be positive")
        if not 0 <= marks <= total:
            raise ValueError("marks must be between zero and total")
        return marks / total * 100

    print(percentage(45, 50))  # 90.0

Functions help isolate tasks, avoid repetition, and make code easier to test.

## 8. Lists

A list is an ordered, mutable collection. Indexes start at zero. Lists can contain duplicate values. remove(value) removes the first matching value and raises ValueError if it is absent; check membership when absence is possible.

### Example 29 — Common list operations

    names = ["Adil", "Syed", "Ali"]
    print(names[0])       # Adil
    names.append("Athif")
    print(len(names))     # 4
    print("Ali" in names) # True
    print("Ravi" not in names)  # True
    names.remove("Syed")
    print(names)          # ['Adil', 'Ali', 'Athif']

### Example 30 — Safely remove an item

    tasks = ["study", "code"]
    target = "sleep"
    if target in tasks:
        tasks.remove(target)
    else:
        print("Task not found")

Output: Task not found

### Example 31 — Filter a list

    numbers = [4, 12, 18, 7, 10]
    large_numbers = []
    for number in numbers:
        if number > 10:
            large_numbers.append(number)
    print(large_numbers)

Output: [12, 18]

Deleting an item shifts later items left. Use a value or a carefully managed index; do not assume indexes remain unchanged after mutation.

## 9. Name Management mini-project

### Goal

Maintain three lists:
- names: currently active names
- deleted: names deleted and not yet restored
- restore: history of successful restorations

This is an in-memory practice project. Its data disappears when the program exits. Names are case-sensitive: "Adil" and "adil" are different strings.

    names = []
    deleted = []
    restore = []

    def add_name(name):
        name = name.strip()
        if not name:
            print("Name cannot be empty")
        elif name in names:
            print("Name already exists")
        else:
            names.append(name)
            print("Added:", name)

    def remove_name(name):
        if name in names:
            names.remove(name)
            deleted.append(name)
            print("Deleted:", name)
        else:
            print("Active name not found")

    def restore_name(name):
        if name in names:
            print("Name is already active")
        elif name in deleted:
            deleted.remove(name)
            names.append(name)
            restore.append(name)
            print("Restored:", name)
        else:
            print("Deleted name not found")

    def view_names():
        print("Active:", names)
        print("Active count:", len(names))
        print("Deleted, not restored:", deleted)
        print("Currently deleted count:", len(deleted))
        print("Restoration history:", restore)

    add_name("Adil")
    add_name("Syed")
    add_name("Adil")
    remove_name("Syed")
    restore_name("Syed")
    view_names()

### Project review

Strengths: small functions, membership checks, readable state, and practice with lists and conditions.

Limitations: data is not persistent; duplicate handling is case-sensitive; operations are not tested automatically; lists are global; restoration history records names but not timestamps or unique record IDs.

Next improvements:
1. Add a while-loop menu with Add, Delete, Restore, View and Exit.
2. Validate empty input and normalise case consistently.
3. Add automated tests for duplicate add, missing delete, restore and empty lists.
4. Save/load data from JSON only after learning file handling.
5. Keep program logic separate from menu/input code.

## 10. Practice questions — try before viewing solutions

### Beginner

1. Print your name and a favourite programming language.
2. Read two integers and print their sum, difference, product and quotient. Decide how to handle division by zero.
3. Check whether an integer is positive, negative or zero.
4. Print even numbers from 2 through 20.
5. Calculate the sum of numbers from 1 through n.
6. Print the multiplication table of a number.
7. Count the numbers in a list that are greater than 10.
8. Add a name to a list only if it is not already present.
9. Write a function that returns the square of a number.
10. Remove a task safely only if it exists.

### Intermediate

11. Calculate factorial and reject negative input.
12. Check whether a number is prime; test 0, 1, 2, 9 and 17.
13. Return the first n Fibonacci numbers.
14. Count the digits of positive, negative and zero inputs.
15. Return the sum of a number's digits.
16. Reverse an integer and consider negative numbers.
17. Count vowels, consonants and non-letter characters separately.
18. Check whether text is a palindrome while ignoring spaces and case.
19. Find the largest value in a list without using max().
20. Count how often each character appears in a string.

### Applied and project-focused

21. Extend Name Management with a menu and Exit option.
22. Prevent empty or whitespace-only names.
23. Add case-insensitive duplicate checking while preserving display spelling.
24. Write tests for add, delete and restore operations.
25. Explain why the current project loses data after the program exits and propose a file-based solution.

## 11. Practice solutions

### Solution 1 — Name and language

    print("Name: Adil")
    print("Learning: Python")

### Solution 2 — Arithmetic with zero-division guard

    a, b = 12, 4
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Cannot divide by zero")

### Solution 3 — Positive, negative or zero

    number = -3
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

### Solution 4 — Even numbers from 2 through 20

    for number in range(2, 21, 2):
        print(number)

### Solution 5 — Sum 1 through n

    def sum_to_n(n):
        if n < 1:
            return 0
        total = 0
        for number in range(1, n + 1):
            total += number
        return total

    print(sum_to_n(5))  # 15

This solution defines the result as 0 when n is below 1. Another valid design is to reject negative input; document whichever rule you choose.

### Solution 6 — Multiplication table

    def print_table(n):
        for multiplier in range(1, 11):
            print(f"{n} x {multiplier} = {n * multiplier}")

    print_table(3)

### Solution 7 — Count values greater than 10

    values = [4, 12, 18, 7, 10]
    count = 0
    for value in values:
        if value > 10:
            count += 1
    print(count)  # 2

### Solution 8 — Add unique name

    names = ["Adil", "Ali"]
    new_name = "Syed"
    if new_name not in names:
        names.append(new_name)
    print(names)

Output: ['Adil', 'Ali', 'Syed']

### Solution 9 — Square function

    def square(number):
        return number * number

    print(square(6))  # 36

### Solution 10 — Safe task removal

    tasks = ["study", "code"]
    target = "code"
    if target in tasks:
        tasks.remove(target)
    print(tasks)  # ['study']

### Solution 11 — Factorial with validation

    def factorial(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        result = 1
        for value in range(1, n + 1):
            result *= value
        return result

    print(factorial(5))  # 120

### Solution 12 — Prime check

    def is_prime(n):
        if n < 2:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    for value in [0, 1, 2, 9, 17]:
        print(value, is_prime(value))

Expected: 0 False; 1 False; 2 True; 9 False; 17 True.

### Solution 13 — Fibonacci

    def fibonacci(count):
        if count < 0:
            raise ValueError("count must be non-negative")
        a, b = 0, 1
        sequence = []
        for _ in range(count):
            sequence.append(a)
            a, b = b, a + b
        return sequence

    print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]

### Solution 14 — Digit count

    def count_digits(n):
        n = abs(n)
        if n == 0:
            return 1
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    print(count_digits(0), count_digits(-456))  # 1 3

### Solution 15 — Digit sum

    def digit_sum(n):
        n = abs(n)
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total

    print(digit_sum(1234))  # 10

### Solution 16 — Reverse integer

    def reverse_number(n):
        sign = -1 if n < 0 else 1
        n = abs(n)
        result = 0
        while n:
            result = result * 10 + n % 10
            n //= 10
        return sign * result

    print(reverse_number(120))   # 21
    print(reverse_number(-345))  # -543

### Solution 17 — Count letters and other characters

    def character_counts(text):
        vowels = "aeiou"
        vowels_count = 0
        consonants_count = 0
        other_count = 0
        for ch in text.lower():
            if not ch.isalpha():
                other_count += 1
            elif ch in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        return vowels_count, consonants_count, other_count

    print(character_counts("Hi, Adil!"))

Output: (3, 3, 3) for this English-letter example.

### Solution 18 — Palindrome

    def is_palindrome(text):
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]

    print(is_palindrome("Never odd or even"))  # True

### Solution 19 — Largest list value without max()

    def largest_value(values):
        if not values:
            raise ValueError("list must not be empty")
        largest = values[0]
        for value in values[1:]:
            if value > largest:
                largest = value
        return largest

    print(largest_value([-5, -2, -9]))  # -2

### Solution 20 — Character frequency

    def character_frequency(text):
        frequency = {}
        for ch in text:
            frequency[ch] = frequency.get(ch, 0) + 1
        return frequency

    print(character_frequency("aba"))  # {'a': 2, 'b': 1}

This introduces dictionaries; study the dictionary topic carefully before relying on this pattern.

### Solutions 21–25 — Project tasks

These are design tasks, so there can be more than one correct implementation. A good solution should:
- keep showing the menu until Exit is selected;
- reject blank names after strip();
- choose and document one consistent case-normalisation rule;
- test both success and failure paths;
- persist data only after learning file reading/writing, and handle missing or invalid files.

## 12. Interview questions and answers

1. **What is Python?** A high-level, general-purpose programming language.
2. **What is a variable?** A name bound to a value.
3. **What is dynamic typing?** A name can refer to values of different types at different times; Python determines the type at runtime.
4. **What does input() return?** A string.
5. **Difference between int and float?** int represents integers; float represents floating-point numbers.
6. **Difference between = and ==?** Assignment versus equality comparison.
7. **Difference between / and //?** True division versus floor division.
8. **What does % do?** Returns the remainder.
9. **What is a Boolean?** A value that is either True or False.
10. **What does if/elif/else do?** Selects which branch to execute based on conditions.
11. **What is a loop?** A control structure that repeats code.
12. **Difference between for and while?** for iterates over an iterable; while repeats as long as its condition is true.
13. **What is range(1, 5)?** Values 1, 2, 3 and 4; the stop value is excluded.
14. **What is an infinite loop?** A loop that does not reach its stopping condition.
15. **What is a counter?** A variable used to count occurrences or iterations.
16. **What is an accumulator?** A variable that builds a result, such as a running sum.
17. **What is factorial?** The product from 1 through n for non-negative integer n, with 0! equal to 1.
18. **Is 1 prime?** No. A prime number must be greater than 1 and have exactly two positive divisors.
19. **Why can prime checks stop at the square root?** Any composite number has a factor less than or equal to its square root.
20. **What is Fibonacci?** A sequence in which each term after the first two is the sum of the previous two.
21. **What is a function?** A named reusable block of code.
22. **What is a parameter?** A name in a function definition.
23. **What is an argument?** A value or expression passed to a function call.
24. **Difference between print and return?** print displays output; return passes a value back to the caller.
25. **What happens when a function has no return statement?** It returns None.
26. **What is a list?** An ordered, mutable collection.
27. **Can a list contain duplicates?** Yes.
28. **What does append() do?** Adds one item to the end of a list.
29. **What does remove() do?** Removes the first matching value; if absent, it raises ValueError.
30. **What does len() return?** The number of items currently in a collection.
31. **What is zero-based indexing?** The first item is at index 0.
32. **Why do list indexes shift after deletion?** Remaining items move to fill the gap.
33. **What is a logic error?** The program runs but produces an incorrect result.
34. **Why test edge cases?** They reveal failures at boundaries such as zero, empty input, duplicates or missing values.
35. **What is a limitation of the Name Management project?** It keeps data only in memory and does not persist records after exit.
36. **How would you improve the project?** Add input validation, a menu, tests, persistence, and a clearer separation of logic and interface.

## 13. Code review checklist

Before adding a solution to the repository, check:
- Does it run without syntax errors?
- Are variables and functions named clearly?
- Does it handle the required input range?
- What happens for zero, negatives, empty collections, duplicates or missing values?
- Is the output correct and explained?
- Can repeated logic become a function?
- Have I understood and tested the solution myself?
- Does the note accurately describe whether the code was run or merely reasoned through?

## 14. Next study sequence

1. Practise the 25 questions without reading the solutions first.
2. Build a menu-driven Name Management program.
3. Learn list slicing and the remaining common list operations.
4. Learn tuples, sets and dictionaries.
5. Learn debugging, exceptions and automated testing.
6. Learn file handling and make project data persistent.
7. Continue through the roadmap in ROADMAP.md.

