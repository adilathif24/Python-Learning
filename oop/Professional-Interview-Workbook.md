# Python OOP — Professional Interview Workbook

Answer each OOP interview question using: **definition → mechanism → code → real-world application → design trade-off**.

## 1. Class, object, attributes, methods and self
**Definition:** A class defines a type's structure and behaviour; an object is an instance. Attributes represent state and methods represent behaviour. `self` conventionally refers to the instance.
**Syntax:** `class Name: def __init__(self, value): self.value = value`.
### Seven complete examples
```python
# 1. Define a class
class Dog:
    pass
print(Dog.__name__)  # Dog

# 2. Create an object
pet = Dog()
print(type(pet).__name__)  # Dog

# 3. Add an attribute dynamically
pet.name = "Milo"
print(pet.name)  # Milo; usually declare expected attributes in __init__

# 4. Initialise state
class Dog:
    def __init__(self, name):
        self.name = name
pet = Dog("Milo")
print(pet.name)  # Milo

# 5. Add an instance method
class Dog:
    def __init__(self, name): self.name = name
    def speak(self): return f"{self.name} says Woof!"
pet = Dog("Milo")
print(pet.speak())  # Milo says Woof!

# 6. Independent instances
first, second = Dog("Milo"), Dog("Luna")
print(first.name, second.name)  # Milo Luna

# 7. Bound instance method
pet = Dog("Milo")
sound = pet.speak()
print(sound)  # Milo says Woof!
# pet.speak() is effectively Dog.speak(pet)
```
**Explanation:** `__init__` initialises instance state; `self.name` stores state on the current object. Each instance has independent state. Python binds the instance when an instance method is accessed through an object.
**Real-world use:** A `BankAccount` groups owner/balance data with deposit/withdraw behaviour. A Dog example teaches syntax; business classes should model domain responsibilities.
### Seven interview questions and answers
1. **Class?** A definition describing the structure and behaviour of instances.
2. **Object?** A runtime instance with identity, state and behaviour.
3. **What is self?** The conventional first parameter of an instance method, referring to the target instance.
4. **What does __init__ do?** Initialises a new instance; allocation itself is handled by __new__.
5. **Instance method?** A method receiving the instance and able to read or update instance state.
6. **Class vs instance attribute?** Class attributes are shared through the class unless shadowed; instance attributes belong to one object.
7. **Why avoid dynamic attributes for expected state?** They make object structure inconsistent; constructor declarations improve predictability.
### Five practice questions with answers/code
1. Car model:
```python
class Car:
    def __init__(self, model): self.model = model
print(Car("Civic").model)  # Civic
```
2. Greeting method:
```python
class Greeter:
    def greet(self, name): return f"Welcome, {name}"
print(Greeter().greet("Adil"))
```
3. Independent state:
```python
a, b = Dog("Asha"), Dog("Ravi")
a.name = "Maya"
print(a.name, b.name)  # Maya Ravi
```
4. Default argument:
```python
class Ticket:
    def __init__(self, priority="normal"): self.priority = priority
print(Ticket().priority)
```
5. Counter:
```python
class Counter:
    def __init__(self): self.value = 0
    def increment(self): self.value += 1
c = Counter(); c.increment(); print(c.value)  # 1
```

## 2. Encapsulation, properties and invariants
**Definition:** Encapsulation groups state with behaviour and provides a controlled interface for valid changes. Python uses naming conventions and properties rather than strict private-instance enforcement.
### Seven examples
```python
# 1. Internal-by-convention attribute
class Account:
    def __init__(self, balance): self._balance = balance

# 2. Read-only property
class ReadOnlyAccount:
    def __init__(self, balance): self._balance = balance
    @property
    def balance(self): return self._balance
print(ReadOnlyAccount(100).balance)

# 3. Validated property
class Person:
    def __init__(self, age): self.age = age
    @property
    def age(self): return self._age
    @age.setter
    def age(self, value):
        if value < 0: raise ValueError("Age cannot be negative")
        self._age = value

# 4. Deposit
class Wallet:
    def __init__(self): self.balance = 0
    def deposit(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive")
        self.balance += amount

# 5. Withdrawal
class Account:
    def __init__(self, balance=0): self._balance = balance
    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("Invalid withdrawal")
        self._balance -= amount

# 6. Name mangling is not security
class Example:
    def __init__(self): self.__token = "internal"
obj = Example()
print(obj._Example__token)  # internal

# 7. Complete account with invariant
class BankAccount:
    def __init__(self, owner, opening_balance=0):
        if opening_balance < 0: raise ValueError("Negative balance")
        self.owner, self._balance = owner, opening_balance
    @property
    def balance(self): return self._balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("Deposit must be positive")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance: raise ValueError("Invalid withdrawal")
        self._balance -= amount
account = BankAccount("Maya", 500)
account.deposit(100); account.withdraw(75)
print(account.balance)  # 525
```
**Real-world use:** Account balances, stock quantities, order statuses and configuration that must preserve valid states.
### Seven interview Q&A
1. **Encapsulation?** Keep data and related operations together behind a controlled interface.
2. **Does Python have private variables?** Underscores are conventions; double underscores trigger name mangling, not security.
3. **Property?** Attribute-style access that can invoke getter/setter logic.
4. **Why validate state?** To preserve invariants and prevent invalid objects.
5. **Why not expose every field?** A controlled interface can enforce rules and allow internal implementation changes.
6. **Invariant?** A condition that must remain true, e.g. balance cannot be negative.
7. **Is encapsulation authorization?** No. Access control and security must be enforced at trusted application boundaries.
### Five practice questions
1. Use Person's property to reject negative ages.
2. Reject negative stock:
```python
class Stock:
    def __init__(self, quantity=0):
        if quantity < 0: raise ValueError("Negative stock")
        self.quantity = quantity
```
3. Add a validated deposit: use Wallet.deposit above.
4. Format account summary:
```python
class Summary:
    def __init__(self, owner, balance): self.owner, self.balance = owner, balance
    def display(self): return f"{self.owner}: balance={self.balance}"
print(Summary("Ravi", 200).display())
```
5. Explain direct mutation risk: it may bypass validation and violate object invariants.

## 3. Inheritance, overriding, polymorphism and composition
**Definition:** Inheritance specialises a base type; overriding replaces inherited behaviour; polymorphism lets different implementations support the same operation; composition assembles behaviour from collaborating objects.
### Seven examples
```python
# 1. Inheritance
class Animal:
    def eat(self): return "Eating"
class Dog(Animal): pass
print(Dog().eat())

# 2. Override
class Animal:
    def speak(self): return "Sound"
class Dog(Animal):
    def speak(self): return "Woof"
print(Dog().speak())

# 3. super()
class User:
    def __init__(self, name): self.name = name
class Admin(User):
    def __init__(self, name, permissions):
        super().__init__(name); self.permissions = permissions
print(Admin("Maya", ["read"]).name)

# 4. Polymorphism
class EmailNotifier:
    def send(self, message): return f"Email: {message}"
class SMSNotifier:
    def send(self, message): return f"SMS: {message}"
def notify(channel, message): return channel.send(message)
print(notify(EmailNotifier(), "Ready"))
print(notify(SMSNotifier(), "Ready"))

# 5. Duck typing
class CsvExporter:
    def export(self, data): return "CSV exported"
class JsonExporter:
    def export(self, data): return "JSON exported"
def run_exporter(exporter, data): return exporter.export(data)
print(run_exporter(JsonExporter(), []))

# 6. Abstract contract
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): pass
class CardPayment(PaymentMethod):
    def pay(self, amount): return f"Paid {amount} by card"
print(CardPayment().pay(100))

# 7. Composition
class Engine:
    def start(self): return "Engine started"
class Car:
    def __init__(self, engine): self.engine = engine
    def start(self): return self.engine.start()
print(Car(Engine()).start())
```
**Real-world use:** Multiple payment, notification or export providers implement a common operation without coupling callers to a specific provider.
### Seven interview Q&A
1. **Inheritance?** Derive a specialised class from a base class.
2. **Overriding?** A subclass supplies its own implementation of inherited behaviour.
3. **super()?** Delegates according to method resolution order, commonly to parent behaviour.
4. **Polymorphism?** Different objects respond to the same operation with their own implementations.
5. **Duck typing?** Focus on supported behaviour rather than declared class identity.
6. **Abstract base class?** Defines an explicit contract and prevents instantiation while abstract methods remain unimplemented.
7. **Inheritance vs composition?** “Is-a” versus “has-a/uses-a”; composition often reduces coupling.
### Five practice questions
1. Manager extends Employee:
```python
class Employee:
    def __init__(self, name): self.name = name
class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name); self.team_size = team_size
print(Manager("Asha", 4).team_size)
```
2. Override area:
```python
class Square:
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
print(Square(4).area())  # 16
```
3. Add a new notifier implementing `send(message)`; caller remains unchanged.
4. Add an exporter implementing `export(data)`; reuse run_exporter.
5. Explain bad inheritance: inheriting only to reuse one helper is usually weaker than composition or a module-level function.

## 4. Class/static methods, dataclasses and special methods
**Definition:** Instance methods receive an instance; class methods receive the class; static methods receive neither automatically. Dataclasses generate common data-model methods.
### Seven examples
```python
# 1. Instance method
class Counter:
    def __init__(self, value=0): self.value = value
    def increment(self): self.value += 1

# 2. Classmethod factory
class User:
    def __init__(self, name): self.name = name
    @classmethod
    def from_email(cls, email): return cls(email.split("@")[0])
print(User.from_email("maya@example.com").name)  # maya

# 3. Static utility
class Temperature:
    @staticmethod
    def to_fahrenheit(c): return c * 9/5 + 32
print(Temperature.to_fahrenheit(0))  # 32.0

# 4. Class attribute
class Employee:
    organisation = "Example Ltd"
print(Employee.organisation)

# 5. Dataclass
from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
print(Product("Pen", 10))

# 6. __repr__
class Ticket:
    def __init__(self, number): self.number = number
    def __repr__(self): return f"Ticket(number={self.number})"
print(Ticket(7))

# 7. Dataclass equality
@dataclass
class Point:
    x: int
    y: int
print(Point(1, 2) == Point(1, 2))  # True
```
**Real-world use:** Dataclasses model configuration, coordinates, API payloads and structured records.
### Seven interview Q&A
1. **Instance vs class method?** Instance method gets object; class method gets class and supports alternate constructors.
2. **Static method?** Namespaced utility with no implicit instance/class argument.
3. **Dataclass?** Generates methods such as init, repr and equality based on declared fields.
4. **Dunder method?** Special method integrating a type with Python syntax/built-ins.
5. **Class attribute use?** Shared data; avoid mutable class attributes for per-instance state.
6. **MRO?** The order Python searches base classes for attributes/methods.
7. **Should every class use these features?** No; use the simplest design that fits the domain.
### Five practice tasks
1. Build a `from_email` factory like User above.
2. Static positive check:
```python
class NumberRules:
    @staticmethod
    def is_positive(value): return value > 0
print(NumberRules.is_positive(5))
```
3. Book dataclass:
```python
@dataclass
class Book:
    title: str
    pages: int
print(Book("Python", 200))
```
4. Add `__repr__` to an Order object.
5. Explain mutable class-state risk: instances may unexpectedly share the same mutable object.

## Project: Library lending system
**Interview question:** Design a small library model that prevents a book being borrowed twice.
**Professional answer:** A Book owns its borrowing invariant; Library manages the collection. A production implementation would add persistence, transaction/locking, authentication and audit logs.
```python
class Book:
    def __init__(self, isbn, title):
        self.isbn, self.title = isbn, title
        self._borrower = None
    @property
    def is_available(self): return self._borrower is None
    def borrow(self, member_id):
        if not member_id: raise ValueError("Member ID required")
        if not self.is_available: raise ValueError("Already borrowed")
        self._borrower = member_id
    def return_book(self, member_id):
        if self._borrower != member_id: raise ValueError("Wrong borrower")
        self._borrower = None
class Library:
    def __init__(self): self._books = {}
    def add_book(self, book):
        if book.isbn in self._books: raise ValueError("Duplicate ISBN")
        self._books[book.isbn] = book
    def find_book(self, isbn): return self._books.get(isbn)
library = Library()
book = Book("978-0001", "Python Fundamentals")
library.add_book(book); book.borrow("MEM-101")
print(book.is_available)  # False
book.return_book("MEM-101")
print(book.is_available)  # True
```
**Project follow-ups:** Why split Book/Library? Separate domain state from collection management. What tests? Duplicate ISBN, double borrow, wrong-member return, successful borrow/return. What concurrency issue exists? Two requests could race; production persistence needs transactions/locking.
