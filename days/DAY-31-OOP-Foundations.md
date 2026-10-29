# Day 31 — OOP Foundations: Classes, Objects and Methods

**Status:** Full study pack created; practice and tests required before mastery.

## 1. Definition
Object-oriented programming (OOP) groups data and the behavior that operates on it into objects. A **class** defines a type; an **object** is an instance. `__init__` initializes an instance; `self` refers to that instance.

## 2. Why / where / when
Use OOP when a program models entities with state and behavior—products, users, bank accounts, tasks. Avoid classes for simple one-off calculations where a function is clearer. Keep each class focused on one concept.

## 3. Syntax and dry run
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says woof"

dog = Dog("Milo")
print(dog.speak())
```
Creating Dog("Milo") calls `__init__`, setting this object's name. Calling `dog.speak()` passes dog as `self`.

## 4. Five worked examples
### Example 1 — First class
```python
class Student:
    def __init__(self, name):
        self.name = name
student = Student("Adil")
print(student.name)
```
Output: `Adil`. Each instance has its own name.

### Example 2 — Instance method
```python
class Counter:
    def __init__(self): self.value = 0
    def increment(self): self.value += 1
counter = Counter(); counter.increment()
print(counter.value)
```
Output: `1`. Method changes the object's state.

### Example 3 — Multiple objects
```python
class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price
a=Product("Pen",10); b=Product("Book",50)
print(a.name, b.price)
```
Output: `Pen 50`. Each object stores different values.

### Example 4 — String representation
```python
class Point:
    def __init__(self,x,y): self.x,self.y=x,y
    def __repr__(self): return f"Point({self.x}, {self.y})"
print(Point(2,3))
```
Output: `Point(2, 3)`. repr offers a useful representation.

### Example 5 — Method with validation
```python
class BankAccount:
    def __init__(self, balance=0):
        if balance < 0: raise ValueError("negative balance")
        self.balance=balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("amount must be positive")
        self.balance += amount
account=BankAccount(10); account.deposit(5)
print(account.balance)
```
Output: `15`. State is updated only after validation.

## 5. Five practice tasks with solutions
### Task 1 — Rectangle area
```python
class Rectangle:
    def __init__(self,w,h):
        if w < 0 or h < 0: raise ValueError("non-negative dimensions required")
        self.w,self.h=w,h
    def area(self): return self.w*self.h
print(Rectangle(3,4).area())
```
Output: `12`. Data and behavior are grouped.

### Task 2 — Employee annual salary
```python
class Employee:
    def __init__(self,name,monthly_salary): self.name,self.monthly_salary=name,monthly_salary
    def annual_salary(self): return self.monthly_salary*12
print(Employee("Maya",5000).annual_salary())
```
Output: `60000`.

### Task 3 — Track instances independently
```class Lamp:
    def __init__(self): self.is_on=False
    def toggle(self): self.is_on=not self.is_on
a,b=Lamp(),Lamp(); a.toggle()
print(a.is_on,b.is_on)
```
Output: `True False`.

### Task 4 — Add a task completion method
```class Task:
    def __init__(self,title): self.title=title; self.done=False
    def complete(self): self.done=True
t=Task("Study"); t.complete()
print(t.done)
```
Output: `True`.

### Task 5 — Validate product price
```class Product:
    def __init__(self,name,price):
        if price < 0: raise ValueError("negative price")
        self.name,self.price=name,price
print(Product("Book",40).price)
```
Output: `40`.

## 6. Common mistakes
- Forgetting `self` in instance methods.
- Confusing class attributes (shared) with instance attributes (per object).
- Putting unrelated responsibilities in one class.
- Assuming `__init__` returns the object; Python creates it before calling __init__.
- Not validating state changes.

## 7. Interview questions
1. Class vs object? **Class defines the type; object is an instance.**
2. What is self? **Reference to the instance receiving the method call.**
3. What is __init__? **Initializer invoked for a new instance.**
4. Instance vs class attribute? **Per object vs shared on class (unless shadowed).**
5. When prefer a function? **When no meaningful stateful object model is needed.**

## 8. Project — Bank Account
Save as `bank_account.py`.
```python
class BankAccount:
    def __init__(self, owner, opening_balance=0):
        if not owner.strip(): raise ValueError("owner required")
        if opening_balance < 0: raise ValueError("balance cannot be negative")
        self.owner=owner.strip(); self.balance=float(opening_balance)
    def deposit(self, amount):
        if amount <= 0: raise ValueError("deposit must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0: raise ValueError("withdrawal must be positive")
        if amount > self.balance: raise ValueError("insufficient funds")
        self.balance -= amount
    def statement(self): return f"{self.owner}: ₹{self.balance:.2f}"

def main():
    account=BankAccount(input("Owner: "),0)
    try:
        account.deposit(float(input("Deposit: ")))
        print(account.statement())
    except ValueError as error: print(f"Error: {error}")

if __name__ == "__main__": main()
```
Example owner Adil, deposit 100 → `Adil: ₹100.00`.

### Tests — `test_bank_account.py`
```python
import unittest
from bank_account import BankAccount
class AccountTests(unittest.TestCase):
    def test_deposit(self):
        a=BankAccount("A",10); a.deposit(5); self.assertEqual(a.balance,15)
    def test_withdraw(self):
        a=BankAccount("A",10); a.withdraw(4); self.assertEqual(a.balance,6)
    def test_insufficient(self):
        with self.assertRaises(ValueError): BankAccount("A",2).withdraw(3)
    def test_empty_owner(self):
        with self.assertRaises(ValueError): BankAccount(" ",0)
    def test_invalid_deposit(self):
        with self.assertRaises(ValueError): BankAccount("A").deposit(0)
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What is an instance? **Object created from a class.**
2. Why self? **To access the object instance.**
3. Who calls __init__? **Python calls it during instance creation.**
4. Why validation? **Keep state within allowed rules.**
5. Can each instance have a different attribute value? **Yes.**
**Challenge:** Add a transfer method that moves money between two accounts and test same-account, zero, negative and insufficient-funds cases.

## 10. Completion
- [ ] I can define classes, create objects, and explain self.
- [ ] Project tests pass.
- [ ] I completed the transfer challenge.
