# Python OOP — Separate Beginner-to-Advanced Track

This guide is intentionally separate from Python core concepts and DSA. OOP means Object-Oriented Programming.

Each topic has definition, explanation, real-world example, where/when/how to use it, seven examples or interview Q&A items, tasks and answers.

## 1. Classes, objects, attributes and methods
**Definition:** A class defines the structure/behaviour of objects; an object is an instance. Attributes store state and methods define behaviour.
**Explanation:** Each instance can hold its own attributes. Use classes when state and related operations belong together.
**Real-world example:** A BankAccount stores a balance and supports deposit/withdraw operations.
**Where/when/how:** Identify the entity, its data and actions; create a class when this grouping improves clarity.
### Seven examples
1. class Dog: pass
2. pet = Dog() creates an object.
3. pet.name = 'Milo' adds an attribute dynamically; usually define expected attributes in __init__.
4. class Dog with __init__(self, name) sets self.name.
5. Add a speak method returning 'Woof'.
6. Create two Dog instances with different names.
7. Call pet.speak() to invoke the bound instance method.
### Tasks
- Create Student with name and marks.
- Create Product with name and price.
- Create BankAccount with deposit and withdraw methods.
### Interview Q&A
1. **Class?** A definition used to create objects.
2. **Object?** An instance of a class.
3. **Attribute?** Data associated with an object or class.
4. **Method?** A function defined on a class.
5. **What is self?** Conventional name for the current instance argument.
6. **Can a class make multiple objects?** Yes.
7. **When avoid a class?** When a simple function/data structure is clearer.

## 2. __init__, self and instance state
**Definition:** __init__ initialises an already-created instance; __new__ is responsible for creating the object.
**Explanation:** self.name = name stores state on that instance.
**Real-world example:** Initialise a product with name, price and quantity.
**Where/when/how:** Put required initial state and simple validation in __init__.
### Seven examples
1. def __init__(self): self.count = 0
2. def __init__(self, name): self.name = name
3. Student('Adil', 85) passes initialiser arguments.
4. Compare attributes on two separate instances.
5. Use immutable defaults where suitable.
6. Validate a non-negative price before assignment.
7. Use self to call another instance method.
### Tasks
- Initialise Employee with name and ID.
- Reject invalid price.
- Show that two instances have separate state.
### Interview Q&A
1. **What is __init__?** The instance initialiser.
2. **Is __init__ the object creator?** Strictly, __new__ creates; __init__ initialises.
3. **Is self a keyword?** No, but it is the standard convention.
4. **Why define attributes in __init__?** It makes the expected object state clear.
5. **Can __init__ return a value?** It must return None.
6. **Why avoid a mutable default list?** Calls may share the same list object.
7. **How create independent lists?** Use None as a default and create a fresh list inside.

## 3. Instance, class and static methods
**Definition:** Instance methods receive self; class methods receive cls; static methods receive neither automatically.
**Explanation:** Choose method type based on which state or context the operation needs.
**Real-world example:** A class method can construct an Employee from a CSV row; a static method can validate an employee code.
**Where/when/how:** Instance behaviour uses object state; class methods handle class-level operations/alternative constructors; static methods are related utilities.
### Seven examples
1. Instance method reads self.name.
2. Instance method updates self.balance.
3. Class attribute stores a shared configuration value.
4. @classmethod def from_text(cls, text): return cls(text).
5. Using cls supports subclass-aware construction.
6. @staticmethod checks a code format.
7. Compare calling instance, class and static methods.
### Tasks
- Implement Employee.from_text().
- Add a static validator.
- Explain your chosen method type.
### Interview Q&A
1. **Instance method?** Receives instance by convention.
2. **Class method?** Receives class as cls.
3. **Static method?** Receives no automatic self/cls.
4. **Alternative constructor?** A class method can provide one.
5. **Does staticmethod get self?** No.
6. **Why use cls rather than hard-code class name?** It supports subclasses.
7. **Should every helper be static?** No; module-level functions may be clearer.

## 4. Encapsulation and properties
**Definition:** Encapsulation groups state and behaviour behind a controlled interface.
**Explanation:** A leading underscore signals internal use by convention. Double leading underscores trigger name mangling, not absolute privacy. @property can add validation or computed behaviour.
**Real-world example:** A product price should not be assigned a negative value.
**Where/when/how:** Use a property when getting/setting an attribute requires validation or computation; avoid unnecessary boilerplate.
### Seven examples
1. self._balance signals non-public state.
2. A public property reads balance.
3. @property computes a full name.
4. A setter validates age.
5. Raise ValueError for negative price.
6. __code demonstrates name mangling, not security.
7. Expose deposit() instead of arbitrary balance changes.
### Tasks
- Create a price property that rejects negative values.
- Validate age.
- Explain underscore conventions.
### Interview Q&A
1. **Encapsulation?** Grouping state/behaviour and controlling the public interface.
2. **Is _name private?** No; it is a convention.
3. **What is name mangling?** Rewriting double-leading-underscore names to reduce accidental clashes.
4. **What is @property?** Method access through attribute syntax.
5. **Why a setter?** To validate or control assignment.
6. **Encapsulation versus encryption?** They are different concepts.
7. **Should every attribute be a property?** No; add one when it provides value.

## 5. Inheritance, overriding and MRO
**Definition:** Inheritance defines a class based on another class. Overriding replaces inherited method behaviour. MRO is Python's method lookup order.
**Explanation:** Use super() to access the next implementation in the method resolution order.
**Real-world example:** EmailNotification and SMSNotification share a notification interface but send differently.
**Where/when/how:** Use inheritance for a genuine substitutable is-a relationship. Prefer composition for has-a relationships.
### Seven examples
1. Define Animal as a base class.
2. Define Dog(Animal).
3. Override speak() in Dog.
4. Call super().__init__(name).
5. Use an inherited attribute.
6. Add a subclass-only method.
7. Create multiple subclasses with different implementations.
### Tasks
- Create Employee and Manager.
- Override a notification method.
- Compare Car has-an Engine with Dog is-an Animal.
### Interview Q&A
1. **Inheritance?** Deriving a class from another class.
2. **Overriding?** Providing a specialised inherited method implementation.
3. **What does super() do?** Accesses the next implementation in MRO.
4. **Base class?** The class inherited from.
5. **Multiple inheritance?** Inheriting from more than one base class.
6. **MRO?** Order Python uses to resolve attributes/methods.
7. **When composition?** When the relationship is has-a or inheritance couples designs too tightly.

## 6. Polymorphism and duck typing
**Definition:** Polymorphism lets different objects be used through a common interface. Duck typing focuses on supported behaviour.
**Explanation:** Unrelated classes may both implement send(); a caller can use either if it only needs send().
**Real-world example:** A report can be exported to a file or sent to a service through a common method.
**Where/when/how:** Program to the behaviour required; use explicit interfaces when they improve clarity.
### Seven examples
1. len('abc') and len([1, 2]) use the same built-in on different types.
2. Two classes implement speak().
3. A function calls speaker.speak().
4. Different payment providers implement pay(amount).
5. Iterate mixed objects and call a common method.
6. Use isinstance() when type checking is genuinely required.
7. Use ABCs or protocols for explicit contracts where useful.
### Tasks
- Build two notification classes with send().
- Write a function that accepts either object.
- Explain duck typing in your own words.
### Interview Q&A
1. **Polymorphism?** Different implementations through a shared interface.
2. **Duck typing?** Focus on behaviour rather than declared type.
3. **Does Python overload methods by signature like Java?** Not in the same traditional way; defaults, variadic args or dispatch tools are common alternatives.
4. **Overriding?** Subclass implementation replaces inherited behaviour.
5. **Why a shared interface?** Reduces coupling to concrete classes.
6. **Operator overloading?** Special methods customise operations such as +.
7. **Can unrelated classes be polymorphic?** Yes, when they support the required behaviour.

## 7. Abstraction and abstract base classes
**Definition:** Abstraction exposes essential operations while hiding implementation details. An abstract base class can define required methods.
**Explanation:** Python's abc module provides ABC and @abstractmethod.
**Real-world example:** Different payment providers share pay() while implementing different payment processing.
**Where/when/how:** Use an ABC when a family of classes should satisfy a shared contract.
### Seven examples
1. Import ABC and abstractmethod from abc.
2. Define class Shape(ABC).
3. Mark area() as abstract.
4. Implement area() in Rectangle.
5. Instantiate a concrete subclass.
6. An incomplete abstract class cannot be instantiated.
7. Define a PaymentMethod contract for multiple providers.
### Tasks
- Create abstract Shape and concrete Circle/Rectangle.
- Explain why the base class need not know each formula.
- Add a new shape without modifying the caller.
### Interview Q&A
1. **Abstraction?** Expose essential operations, hide implementation details.
2. **Abstract class?** Defines a shared interface and possibly shared implementation.
3. **Can it have concrete methods?** Yes.
4. **What does abstractmethod do?** Requires implementation before concrete instantiation.
5. **Abstraction versus encapsulation?** Interface focus versus controlled grouping of state/behaviour.
6. **Does Python enforce all interfaces at compile time?** No.
7. **When is an ABC unnecessary?** When a simple function or duck-typed contract suffices.

## 8. Composition, special methods and dataclasses
**Definition:** Composition assembles objects from other objects. Special methods integrate with Python syntax. Dataclasses reduce boilerplate for data-focused classes.
**Explanation:** Car has an Engine. __str__ customises readable display; dataclasses can generate common methods.
**Real-world example:** A task record is a dataclass; a car delegates engine operations to an Engine object.
**Where/when/how:** Prefer composition for has-a relationships. Use dataclasses when generated equality/initialisation/representation match the data model.
### Seven examples
1. Car stores an Engine.
2. Library stores Book objects.
3. __str__ gives readable output.
4. __repr__ gives developer-oriented representation.
5. @dataclass defines a data-focused Product.
6. Implement __eq__ only for intentional equality rules.
7. Use default_factory for mutable dataclass fields.
### Tasks
- Model Car composed of Engine.
- Create a Student dataclass.
- Add readable string output.
### Interview Q&A
1. **Composition?** Building an object using other objects.
2. **Inheritance versus composition?** Is-a versus has-a/uses-a as a rule of thumb.
3. **Dunder methods?** Special methods integrated with Python behaviour.
4. **__str__ versus __repr__?** User-friendly display versus developer-oriented representation.
5. **Dataclass?** A decorator that generates common methods for data-focused classes.
6. **Do dataclasses validate types automatically?** No.
7. **Why default_factory?** It creates a separate mutable default for each instance.

## Seven OOP coding questions with answers
### Q1. Student class
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks
        def passed(self):
            return self.marks >= 40
    print(Student('Adil', 78).passed())  # True
**Answer/approach:** Put state in __init__ and behaviour in a method.

### Q2. Bank account
    class BankAccount:
        def __init__(self, balance=0):
            if balance < 0:
                raise ValueError('Balance cannot be negative')
            self._balance = balance
        def deposit(self, amount):
            if amount <= 0:
                raise ValueError('Deposit must be positive')
            self._balance += amount
        def withdraw(self, amount):
            if amount <= 0 or amount > self._balance:
                raise ValueError('Invalid withdrawal')
            self._balance -= amount
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print(account._balance)  # 120
**Answer/approach:** Keep state on the object and enforce rules in its methods. In a production design, expose a read-only balance property.

### Q3. Inheritance
    class Animal:
        def speak(self):
            return 'Some sound'
    class Dog(Animal):
        def speak(self):
            return 'Woof'
    print(Dog().speak())  # Woof
**Answer:** Dog overrides inherited behaviour.

### Q4. Polymorphism
    class Email:
        def send(self): return 'Email sent'
    class SMS:
        def send(self): return 'SMS sent'
    def notify(channel): return channel.send()
    print(notify(Email()))
    print(notify(SMS()))
**Answer:** The caller depends on send(), not a specific class.

### Q5. Abstraction
    from abc import ABC, abstractmethod
    class Shape(ABC):
        @abstractmethod
        def area(self): pass
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self): return self.width * self.height
    print(Rectangle(4, 3).area())  # 12
**Answer:** The abstract base class defines a contract; Rectangle supplies the formula.

### Q6. Composition
    class Engine:
        def start(self): return 'Engine started'
    class Car:
        def __init__(self, engine): self.engine = engine
        def start(self): return self.engine.start()
    print(Car(Engine()).start())
**Answer:** Car uses an Engine object rather than inheriting from Engine.

### Q7. Dataclass
    from dataclasses import dataclass
    @dataclass
    class Product:
        name: str
        price: float
    print(Product('Notebook', 50.0))
**Answer:** Dataclass generates common methods suitable for simple data records.

## OOP mastery checklist
- [ ] Explain class, object, self and __init__.
- [ ] Distinguish instance/class/static methods.
- [ ] Explain encapsulation and properties.
- [ ] Demonstrate inheritance, overriding, super and MRO.
- [ ] Explain polymorphism and duck typing.
- [ ] Implement an ABC.
- [ ] Compare composition with inheritance.
- [ ] Solve all seven coding questions without copying.