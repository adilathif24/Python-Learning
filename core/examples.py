"""Runnable examples for Python Core Concepts.
Run: python core/examples.py
These are educational examples; change inputs to practise.
"""

# 1. Variables, types, input conversion
name = "Adil"
age = 23
price = 49.5
active = True
print("1. Variables:", name, age, price, active, type(age).__name__)
print("Conversion:", int("12") + 3)

# 2. Operators and conditions
number = 8
print("2. Arithmetic:", 7 + 3, 7 // 2, 7 % 2, 2 ** 4)
print("Condition:", "even" if number % 2 == 0 else "odd")

# 3. Loops
total = 0
for n in range(1, 6):
    total += n
print("3. Sum 1..5:", total)
countdown = 3
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1

# 4. Strings
word = "python"
print("4. First:", word[0], "slice:", word[1:4], "reverse:", word[::-1])
print("Palindrome:", (lambda s: s == s[::-1])("level"))
print("Vowels:", sum(ch in "aeiou" for ch in "education"))

# 5. Lists
numbers = [3, 1, 2]
numbers.append(4)
print("5. List:", numbers, "squares:", [n * n for n in numbers])
print("Largest:", max(numbers))

# 6. Tuples
point = (2, 5)
x, y = point
print("6. Tuple unpacking:", x, y)

# 7. Sets
first = {1, 2, 3}
second = {3, 4, 5}
print("7. Union:", first | second, "intersection:", first & second)

# 8. Dictionaries and frequency counting
user = {"name": "Adil", "age": 23}
print("8. Safe lookup:", user.get("city", "Unknown"))
frequencies = {}
for char in "banana":
    frequencies[char] = frequencies.get(char, 0) + 1
print("Frequencies:", frequencies)

# 9. Functions
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result

def add(a, b):
    return a + b

print("9. Function:", add(4, 5), "factorial:", factorial(5))

# 10. Comprehensions and modules
import math
print("10. Even squares:", [n * n for n in range(10) if n % 2 == 0])
print("Square root:", math.sqrt(25))

# 11. Exceptions
def parse_age(value):
    try:
        age_value = int(value)
        if age_value < 0:
            raise ValueError("age cannot be negative")
        return age_value
    except ValueError as error:
        return f"Invalid age: {error}"

print("11. Valid input:", parse_age("23"))
print("Invalid input:", parse_age("abc"))

# 12. Iterators, generators, type hints
def squares(limit: int):
    for value in range(limit):
        yield value * value

print("12. Generator:", list(squares(5)))

# File I/O example: uncomment to create a local file safely.
# with open("example_notes.txt", "w", encoding="utf-8") as file:
#     file.write("Practise Python every day.\\n")
# with open("example_notes.txt", encoding="utf-8") as file:
#     print(file.read())
