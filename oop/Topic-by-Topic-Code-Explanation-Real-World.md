# Python OOP — Complete Code, Explanation and Real-World Use

OOP (Object-Oriented Programming) groups related data and behaviour into classes and objects. For each section, type the code and run it. Examples are independent unless stated otherwise.

## 1. Class, object, attributes and methods

**Definition:** A class is a blueprint; an object is an instance. Attributes hold data; methods define behaviour.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

pet = Dog("Milo")
print(pet.name)     # Milo
print(pet.speak())  # Milo says Woof!
```

**Line-by-line explanation:**
1. `class Dog:` defines a new class.
2. `__init__` runs when a new instance is initialised.
3. `self.name = name` stores the supplied name on this particular object.
4. `speak` is an instance method and can read the object's name.
5. `Dog("Milo")` constructs an object; `pet.speak()` calls its method.

**Seven examples, with actual code**

### Example 1 — Define a class
```python
class Dog:
    pass

print(Dog)
```
**Explanation:** `pass` is a placeholder; the class exists but has no custom behaviour yet.

### Example 2 — Create an object
```python
class Dog:
    pass

pet = Dog()
print(type(pet).__name__)  # Dog
```
**Explanation:** Calling the class creates an instance of that class.

### Example 3 — Add an attribute dynamically
```python
class Dog:
    pass

pet = Dog()
pet.name = "Milo"
print(pet.name)
```
**Explanation:** Python allows an attribute to be attached to this instance. In regular application code, prefer defining expected attributes in `__init__` so every object has a predictable structure.

### Example 4 — Initialise an attribute with __init__
```python
class Dog:
    def __init__(self, name):
        self.name = name

pet = Dog("Milo")
print(pet.name)
```
**Explanation:** Each new Dog receives a name at construction time.

### Example 5 — Add a speak method
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof"

pet = Dog("Milo")
print(pet.speak())  # Woof
```
**Explanation:** Methods are functions defined in a class. Calling `pet.speak()` passes the instance as `self` automatically.

### Example 6 — Create two independent instances
```python
class Dog:
    def __init__(self, name):
        self.name = name

first = Dog("Milo")
second = Dog("Bruno")
first.name = "Max"
print(first.name)   # Max
print(second.name)  # Bruno
```
**Explanation:** Each instance has its own `name`; updating one does not change the other.

### Example 7 — Call a bound instance method
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof"

pet = Dog("Milo")
sound_function = pet.speak
print(sound_function())  # Milo says Woof
```
**Explanation:** Accessing an instance method through an object creates a bound method that remembers the instance.

**Real-world use:** A `Dog` example teaches the same pattern used by `User`, `Order`, `Employee` or `BankAccount` objects. Use a class when data and the operations on that data naturally belong together.

## 2. __init__, self and instance state

```python
class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("price cannot be negative")
        self.name = name
        self.price = price

keyboard = Product("Keyboard", 2000)
print(keyboard.name, keyboard.price)
```

**Explanation:** `self` refers to the current instance. `__init__` initialises the instance after creation. `__new__` is the lower-level method responsible for creating the instance. The validation prevents an invalid product from being created normally.

**Real-world use:** Initialise an order with a customer ID, a product with a price, or an employee with an employee ID.

## 3. Instance, class and static methods

```python
class Employee:
    company = "Example Ltd"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

    @classmethod
    def change_company(cls, company):
        cls.company = company

    @staticmethod
    def is_valid_id(value):
        return value.startswith("EMP-")

employee = Employee("Adil")
print(employee.introduce())
Employee.change_company("New Company")
print(Employee.company)
print(Employee.is_valid_id("EMP-101"))
```

**Explanation:** Instance methods use `self`; class methods receive `cls` and can work with class-level state; static methods receive no automatic instance/class argument and are suitable for related utility logic.

**Real-world use:** Alternative constructors, shared configuration, and employee-code validation.

## 4. Encapsulation and properties

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

account = BankAccount("Adil", 100)
account.deposit(50)
print(account.balance)  # 150
```

**Explanation:** Encapsulation keeps state and the rules for changing it together. A leading underscore signals an internal-use attribute by convention; it does not make the attribute truly private. The property lets callers read the balance without directly assigning it.

**Real-world use:** Bank balances, inventory quantities, product prices and validated user settings.

## 5. Inheritance and overriding

```python
class User:
    def __init__(self, name):
        self.name = name

    def describe_role(self):
        return "General user"

class Admin(User):
    def describe_role(self):
        return "Administrator"

admin = Admin("Adil")
print(admin.name)            # inherited attribute
print(admin.describe_role()) # overridden behaviour
```

**Explanation:** `Admin` inherits from `User`. It reuses the parent's initialisation and overrides `describe_role` with specialised behaviour. Use inheritance for a genuine “is-a” relationship, not merely to reuse unrelated code.

**Real-world use:** Different account roles, specialised employee types or different notification providers sharing an interface.

## 6. Polymorphism and duck typing

```python
class EmailNotifier:
    def send(self, message):
        return f"Email: {message}"

class SMSNotifier:
    def send(self, message):
        return f"SMS: {message}"

def notify(service, message):
    return service.send(message)

print(notify(EmailNotifier(), "Interview tomorrow"))
print(notify(SMSNotifier(), "Interview tomorrow"))
```

**Explanation:** The same `notify` function works with different objects because each provides a compatible `send` method. Duck typing focuses on supported behaviour rather than exact class identity.

**Real-world use:** Swap email, SMS or push notification services without rewriting the calling workflow.

## 7. Abstraction

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} by card"

payment = CardPayment()
print(payment.pay(500))
```

**Explanation:** An abstract base class defines a required interface. A concrete subclass implements the abstract method. You cannot normally instantiate `PaymentMethod` while its abstract method remains unimplemented.

**Real-world use:** Payment systems, storage providers, notification interfaces and interchangeable data sources.

## 8. Composition

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

car = Car(Engine())
print(car.start())
```

**Explanation:** A car *has an* engine. Composition combines objects instead of forcing a parent-child inheritance relationship. The engine can be replaced with another compatible object.

**Real-world use:** A checkout has a payment service; a report generator has a data source; a car has an engine.

## 9. Special methods and dataclasses

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __str__(self):
        return f"{self.name}: ₹{self.price:.2f}"

item = Product("Mouse", 799)
print(item)
```

**Explanation:** `@dataclass` generates useful methods such as `__init__` and `__repr__`. `__str__` defines a readable string representation for users.

**Real-world use:** Data records such as products, coordinates, configuration values and API payloads.

## Mini-project: simple library catalogue

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if not self.is_available:
            return f"{self.title} is already borrowed"
        self.is_available = False
        return f"You borrowed {self.title}"

    def return_book(self):
        self.is_available = True
        return f"{self.title} returned"

book = Book("Clean Code", "Robert C. Martin")
print(book.borrow())
print(book.borrow())
print(book.return_book())
```

**Real-world use:** This small project models book inventory and state changes. Improve it with a `Library` class, multiple books, search, validation and unit tests.
