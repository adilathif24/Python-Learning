# Python OOP — Beginner to Advanced Interview Guide

This is a separate learning track. Each topic contains definitions, explanations, real-world use, examples, tasks and interview Q&A.

AI assistance was used to organise this guide. Run the examples yourself.

# 1. Classes, objects, attributes and methods
**Definition:** A class describes a type of object; an object is an instance. Attributes store state and methods define behaviour.
**Real-world example:** A BankAccount has a balance and deposit/withdraw operations.
**Where/when/how:** Use a class when related state and behaviour belong together; use a simple function for a one-off calculation.

Seven examples:
1. class Dog: pass
2. pet = Dog()
3. pet.name = "Milo" (usually define attributes in __init__ instead).
4. Define __init__(self, name) and set self.name.
5. Define speak(self) returning "Woof".
6. Create two dogs with different names.
7. Call pet.speak().

Tasks: Student class; Product class; BankAccount class.
Interview Q&A:
1. Class? Definition for creating objects.
2. Object? Instance of a class.
3. Attribute? Data associated with an object or class.
4. Method? Function defined on a class.
5. self? Conventional name for the current instance.
6. Can a class create many objects? Yes.
7. When avoid OOP? When a function or simple data structure is clearer.

# 2. Initialisation and instance state
**Definition:** __init__ initialises a newly created instance; __new__ is responsible for creating it.
**Real-world example:** Initialise a product with name, price and stock.
**Where/when/how:** Set required initial state and basic validation in __init__.

Seven examples:
1. Initialise count to zero.
2. Initialise a name.
3. Pass arguments when creating Student("Adil", 85).
4. Create two objects and compare their attributes.
5. Use safe immutable defaults.
6. Reject a negative price.
7. Call another instance method through self.

Tasks: Employee initialisation; validate balance; show independent instance state.
Interview Q&A:
1. What is __init__? Instance initializer.
2. Is it the strict object constructor? __new__ creates; __init__ initialises.
3. self? Current instance.
4. Is self a keyword? No, a convention.
5. Why initialise attributes? Clear, consistent state.
6. Mutable default list? Avoid; create a fresh list per instance.
7. Can __init__ return an arbitrary value? No, it must return None.

# 3. Instance, class and static methods
**Definition:** Instance methods receive self; class methods receive cls; static methods receive neither automatically.
**Real-world example:** A class method creates an object from a string; a static method validates a code.
**Where/when/how:** Choose the method type according to the state it needs.

Seven examples:
1. Instance method reads self.name.
2. Instance method updates self.balance.
3. Class attribute stores shared class-level data.
4. @classmethod alternative constructor returns cls(name).
5. Using cls supports subclass construction.
6. @staticmethod validates a code.
7. Call and compare each method type.

Tasks: from_string constructor; product-code validation; explain choices.
Interview Q&A:
1. Instance method? Receives instance by convention.
2. Class method? Receives class as cls.
3. Static method? No automatic instance/class argument.
4. Alternative constructor? Yes, class method is useful.
5. Does staticmethod receive self? No.
6. Why use cls for inheritance? It respects subclass construction.
7. Should every helper be static? No, a module function may be clearer.

# 4. Encapsulation and properties
**Definition:** Encapsulation groups state and behaviour behind a useful interface. Python uses conventions and properties rather than strict private access.
**Real-world example:** Prevent invalid product prices or bank-account operations.
**Where/when/how:** Use properties when reads/writes need validation or computed behaviour.

Seven examples:
1. _balance signals internal use by convention.
2. Read internal state via a public property.
3. @property calculates a full name.
4. A setter validates age.
5. Raise ValueError for negative price.
6. __code demonstrates name mangling, not secrecy.
7. deposit() controls balance changes.

Tasks: validated price property; age property; explain underscore convention.
Interview Q&A:
1. Encapsulation? Grouping state/behaviour and controlling access.
2. Is _name private? No, it is a convention.
3. Name mangling? Reduces accidental subclass name clashes.
4. @property? Exposes method behaviour as an attribute.
5. Why setter? Validate/control assignments.
6. Is encapsulation encryption? No.
7. Should every attribute use a property? No, only where useful.

# 5. Inheritance and overriding
**Definition:** Inheritance defines a class based on another; overriding replaces inherited method behaviour in a subclass.
**Real-world example:** EmailNotification and SMSNotification share an interface but send differently.
**Where/when/how:** Use for genuine is-a relationships; prefer composition when an object merely uses another object.

Seven examples:
1. Define Animal.
2. Define Dog(Animal).
3. Override speak().
4. Call super().__init__(name).
5. Use inherited attributes.
6. Add a subclass-specific method.
7. Add another subclass with different behaviour.

Tasks: Employee/Manager; notification subclasses; compare Car has-a Engine to is-a.
Interview Q&A:
1. Inheritance? Build a class based on another.
2. Overriding? Subclass replaces inherited method behaviour.
3. super()? Access next implementation in method resolution order.
4. Base class? Class being inherited from.
5. Multiple inheritance? Inherit from more than one base.
6. MRO? Method Resolution Order.
7. When composition? For has-a/use-a relationships or to reduce tight coupling.

# 6. Polymorphism and duck typing
**Definition:** Different objects can be used through a shared interface. Duck typing focuses on supported behaviour rather than declared type.
**Real-world example:** Different notification providers implement send().
**Where/when/how:** Write callers against the required behaviour, not a concrete class, when appropriate.

Seven examples:
1. len("abc") and len([1,2]).
2. Two classes implement speak().
3. A function calls speaker.speak().
4. Payment providers implement pay(amount).
5. Loop over mixed objects and call a common method.
6. Use isinstance when a type check is genuinely required.
7. Use an ABC or Protocol for an explicit contract when helpful.

Tasks: display() objects; notification types; explain duck typing.
Interview Q&A:
1. Polymorphism? Different implementations through a common interface.
2. Duck typing? Behaviour matters more than declared type.
3. Does Python overload methods by signature like Java? Not traditionally; use defaults, variadic args or dispatch tools.
4. Overriding? Subclass implementation of inherited method.
5. Why common interface? Reduces coupling.
6. Operator overloading? Special methods customise operators.
7. Can unrelated classes be polymorphic? Yes, if they support the required behaviour.

# 7. Abstraction and abstract base classes
**Definition:** Abstraction exposes essential operations while hiding implementation details. ABCs can specify required methods.
**Real-world example:** Different payment methods expose pay() but implement it differently.
**Where/when/how:** Use an abstract base class when related classes need a shared interface.

Seven examples:
1. Import ABC and abstractmethod.
2. Define Shape(ABC).
3. Mark area() abstract.
4. Implement area() in Rectangle.
5. Instantiate Rectangle.
6. An incomplete abstract class cannot be instantiated.
7. Create PaymentMethod subclasses.

Tasks: Shape ABC; Circle/Rectangle; explain the contract.
Interview Q&A:
1. Abstraction? Essential interface without exposing all details.
2. Abstract class? Defines a shared interface and possibly common behaviour.
3. Can it contain concrete methods? Yes.
4. @abstractmethod? Requires implementation before concrete instantiation.
5. Abstraction versus encapsulation? Interface focus versus grouping/control of state.
6. Does Python enforce all interfaces at compile time? No.
7. When ABC unnecessary? When duck typing is enough.

# 8. Composition, special methods and dataclasses
**Definition:** Composition builds an object using other objects. Special methods integrate with Python syntax. Dataclasses reduce boilerplate for data-focused classes.
**Real-world example:** A Car has an Engine; a Student record can be a dataclass.
**Where/when/how:** Use composition for has-a relationships and dataclasses for records; dataclasses do not automatically validate types.

Seven examples:
1. Car stores an Engine.
2. Library stores Book objects.
3. __str__ gives readable output.
4. __repr__ gives developer-oriented representation.
5. @dataclass defines a data class.
6. __eq__ customises equality when needed.
7. default_factory creates a fresh mutable field per instance.

Tasks: Car/Engine; Student dataclass; readable representation.
Interview Q&A:
1. Composition? Build an object from other objects.
2. Inheritance vs composition? Is-a vs has-a, as a rule of thumb.
3. Dunder methods? Special methods with double underscores.
4. __str__ vs __repr__? User-friendly vs developer-oriented representation.
5. Dataclass? Generates common methods for data classes.
6. Do dataclasses validate types at runtime? No.
7. Why default_factory? Avoid sharing one mutable default between instances.

# Seven OOP coding interview questions with answers

## Q1. Student class
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks
        def passed(self):
            return self.marks >= 40
    print(Student("Adil", 78).passed())  # True
Approach: Store state in __init__; place behaviour in methods.

## Q2. BankAccount
    class BankAccount:
        def __init__(self, balance=0):
            if balance < 0:
                raise ValueError("Balance cannot be negative")
            self._balance = balance
        @property
        def balance(self):
            return self._balance
        def deposit(self, amount):
            if amount <= 0:
                raise ValueError("Deposit must be positive")
            self._balance += amount
        def withdraw(self, amount):
            if amount <= 0 or amount > self._balance:
                raise ValueError("Invalid withdrawal")
            self._balance -= amount
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print(account.balance)  # 120
Approach: Encapsulate state and enforce rules in methods.

## Q3. Inheritance
    class Animal:
        def speak(self):
            return "Some sound"
    class Dog(Animal):
        def speak(self):
            return "Woof"
    print(Dog().speak())
Approach: Put shared behaviour in the base; override specialised behaviour.

## Q4. Polymorphism
    class Email:
        def send(self):
            return "Email sent"
    class SMS:
        def send(self):
            return "SMS sent"
    def notify(channel):
        return channel.send()
    print(notify(Email()))
    print(notify(SMS()))
Approach: Caller relies on shared behaviour, not concrete class.

## Q5. Abstraction
    from abc import ABC, abstractmethod
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height
    print(Rectangle(4, 3).area())  # 12
Approach: Abstract class defines contract; concrete class implements formula.

## Q6. Composition
    class Engine:
        def start(self):
            return "Engine started"
    class Car:
        def __init__(self, engine):
            self.engine = engine
        def start(self):
            return self.engine.start()
    print(Car(Engine()).start())
Approach: Car uses an Engine rather than inheriting from it.

## Q7. Dataclass
    from dataclasses import dataclass
    @dataclass
    class Product:
        name: str
        price: float
    print(Product("Notebook", 50.0))
Approach: Use when a class mainly stores data.

## OOP checklist
- [ ] Explain classes, objects, attributes, methods, self and __init__.
- [ ] Distinguish instance, class and static methods.
- [ ] Explain encapsulation and properties.
- [ ] Demonstrate inheritance, overriding and super().
- [ ] Explain polymorphism and duck typing.
- [ ] Build an abstract base class.
- [ ] Explain composition and dataclasses.
- [ ] Solve all seven coding questions without copying.
