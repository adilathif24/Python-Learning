# My practice: conditions, for loops, and while loops

marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Passed")
else:
    print("Keep practising")

# range(1, 6) produces 1, 2, 3, 4, 5.
for i in range(1, 6):
    print(i)

# Accumulator: keep a running total.
total = 0
for i in range(1, 11):
    total += i
print("Sum from 1 to 10:", total)

# Counter: count how many values match a condition.
numbers = [4, 12, 18, 7, 10]
count = 0
for number in numbers:
    if number > 10:
        count += 1
print("Numbers greater than 10:", count)

# A while loop needs progress toward ending.
n = 1
while n <= 5:
    print("while:", n)
    n += 1
