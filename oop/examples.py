"""Runnable examples for Python OOP.
Run: python oop/examples.py
"""

# 1-2. Class, object, __init__, self and instance state
class Student:
    school = "Learning Academy"  # class attribute

    def __init__(self, name, marks):
        if not 0 <= marks <= 100:
            raise ValueError("marks must be between 0 and 100")
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 40

    def __str__(self):
        return f"{self.name}: {self.marks}"

student1 = Student("Adil", 85)
student2 = Student("Sara", 35)
print("1-2. Students:", student1, student2, student1.passed(), student2.passed())

# 3. Instance, class and static methods
class Employee:
    company = "Example Ltd"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @classmethod
    def from_text(cls, text):
        name, employee_id = text.split(",")
        return cls(name.strip(), employee_id.strip())

    @staticmethod
    def valid_id(employee_id):
        return employee_id.startswith("EMP-")

employee = Employee.from_text("Mina, EMP-104")
print("3. Employee:", employee.name, Employee.valid_id(employee.employee_id))

# 4. Encapsulation and properties
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("starting balance cannot be negative")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("invalid withdrawal amount")
        self._balance -= amount

account = BankAccount("Adil", 100)
account.deposit(50)
account.withdraw(20)
print("4. Balance:", account.balance)

# 5. Inheritance and method overriding
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

print("5. Inheritance/override:", Animal().speak(), Dog().speak())

# 6. Polymorphism and duck typing
class Cat:
    def speak(self):
        return "Meow"

def make_sound(animal):
    return animal.speak()

print("6. Polymorphism:", make_sound(Dog()), make_sound(Cat()))

# 7. Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by card"

print("7. Abstraction:", CardPayment().pay(250))

# 8. Composition: a car HAS an engine
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

print("8. Composition:", Car(Engine()).start())

# 9. Dataclasses and special methods
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def discounted_price(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.price * (1 - percent / 100)

product = Product("Keyboard", 2000)
print("9. Dataclass:", product, "after 10% discount:", product.discounted_price(10))
