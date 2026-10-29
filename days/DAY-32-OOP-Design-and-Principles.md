# Day 32 — OOP Design and Principles

**Status:** Full study pack created; mastery requires independent implementation and tests.

## 1. Definition
OOP design includes **encapsulation** (control access to state), **inheritance** (derive a class from another), **polymorphism** (different types support a common interface), **abstraction** (expose essentials, hide implementation), and **composition** (build objects from other objects).

## 2. When to use
Use composition to model “has-a” relationships; inheritance for genuine “is-a” specializations; abstraction when several implementations need the same contract. Don't create inheritance only to reuse a few lines—composition or functions may be simpler.

## 3. Syntax
```python
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError
class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} by card"
```
A method call through a common interface supports polymorphism: each concrete type implements its own behavior.

## 4. Five worked examples
### Example 1 — Encapsulation by methods
```python
class Thermostat:
    def __init__(self, temperature=20): self._temperature=temperature
    def set_temperature(self,value):
        if not 5 <= value <= 35: raise ValueError("temperature out of range")
        self._temperature=value
    def get_temperature(self): return self._temperature
t=Thermostat(); t.set_temperature(22)
print(t.get_temperature())
```
Output: `22`. The method checks a state invariant. A leading underscore signals internal use by convention.

### Example 2 — Inheritance
```python
class Animal:
    def speak(self): return "sound"
class Dog(Animal):
    def speak(self): return "woof"
print(Dog().speak())
```
Output: `woof`. Dog specializes Animal behavior.

### Example 3 — Polymorphism
```python
class EmailNotice:
    def send(self): return "email"
class SMSNotice:
    def send(self): return "sms"
for notice in [EmailNotice(),SMSNotice()]: print(notice.send())
```
Output: email then sms. The same method call works for different types.

### Example 4 — Composition
```python
class Engine:
    def start(self): return "engine on"
class Car:
    def __init__(self,engine): self.engine=engine
    def start(self): return self.engine.start()
print(Car(Engine()).start())
```
Output: `engine on`. A car has an engine object.

### Example 5 — Abstract base class
```python
from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message): pass
class ConsoleNotifier(Notifier):
    def send(self,message): return f"Sent: {message}"
print(ConsoleNotifier().send("Hello"))
```
Output: `Sent: Hello`. The abstract class defines a contract.

## 5. Five tasks with solutions
### Task 1 — Shape abstraction
```from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Square(Shape):
    def __init__(self,side): self.side=side
    def area(self): return self.side**2
print(Square(4).area())
```
Output: `16`.

### Task 2 — Inherit a greeting
```class Person:
    def __init__(self,name): self.name=name
class Student(Person):
    def introduce(self): return f"Student {self.name}"
print(Student("Ali").introduce())
```
Output: `Student Ali`.

### Task 3 — Polymorphic pricing
```class Standard:
    def price(self,base): return base
class Premium:
    def price(self,base): return base*1.2
print([plan().price(100) for plan in (Standard,Premium)])
```
Output: `[100, 120.0]`.

### Task 4 — Composition with address
```class Address:
    def __init__(self,city): self.city=city
class User:
    def __init__(self,name,address): self.name,self.address=name,address
print(User("Maya",Address("Ongole")).address.city)
```
Output: `Ongole`.

### Task 5 — Encapsulated stock
```class Stock:
    def __init__(self,quantity=0): self._quantity=quantity
    def add(self,amount):
        if amount <= 0: raise ValueError("positive amount required")
        self._quantity += amount
    @property
    def quantity(self): return self._quantity
s=Stock(2); s.add(3)
print(s.quantity)
```
Output: `5`.

## 6. Common mistakes
- Inheriting where composition is more suitable.
- Calling super().__init__ incorrectly when base initialization is needed.
- Treating underscore fields as truly private; Python uses conventions and name mangling rather than strict access control.
- Overriding a method with incompatible behavior.
- Creating abstractions with no real benefit.

## 7. Interview Q&A
1. Encapsulation? **Protecting invariants and grouping state with behavior.**
2. Inheritance? **A class derives behavior/data from a base class.**
3. Polymorphism? **Same interface with type-specific behavior.**
4. Composition? **One object contains/uses another.**
5. Abstraction? **Expose essential contract while hiding implementation detail.**

## 8. Project — Notification Service
Save as `notification_service.py`.
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message): pass

class ConsoleNotifier(Notifier):
    def send(self, recipient, message):
        if not recipient.strip() or not message.strip(): raise ValueError("recipient and message required")
        return f"To {recipient}: {message}"

class NotificationService:
    def __init__(self, notifier): self.notifier=notifier
    def notify(self, recipient, message): return self.notifier.send(recipient,message)

def main():
    service=NotificationService(ConsoleNotifier())
    print(service.notify("Adil","Interview tomorrow"))

if __name__ == "__main__": main()
```
Example output: `To Adil: Interview tomorrow`.

### Tests — `test_notification_service.py`
```python
import unittest
from notification_service import ConsoleNotifier, NotificationService
class NotificationTests(unittest.TestCase):
    def test_send(self): self.assertEqual(ConsoleNotifier().send("A","Hi"),"To A: Hi")
    def test_invalid(self):
        with self.assertRaises(ValueError): ConsoleNotifier().send(" ","Hi")
    def test_service(self): self.assertIn("Hi",NotificationService(ConsoleNotifier()).notify("A","Hi"))
    def test_empty_message(self):
        with self.assertRaises(ValueError): ConsoleNotifier().send("A"," ")
    def test_polymorphic_stub(self):
        class Stub:
            def send(self,r,m): return "stub"
        self.assertEqual(NotificationService(Stub()).notify("A","x"),"stub")
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Is-a relationship? **Inheritance.**
2. Has-a relationship? **Composition.**
3. Which pattern allows interchangeable implementations? **Polymorphism.**
4. What does ABC help define? **Abstract contracts.**
5. Is underscore name truly private? **No; it is a convention.**
**Challenge:** Add a second notifier implementation and test that the service works without changing its own code.

## Real-world use cases — where, when and how
1. **Payment methods:** Where: checkout systems. When card/wallet/bank payments share a contract. How: polymorphic pay methods provide different implementations.
2. **Notification service:** Where: business apps. When messages go by email, SMS or console. How: inject a notifier object through composition.
3. **Access control:** Where: user management. When state changes must obey rules. How: encapsulate permissions and expose controlled methods.
4. **File storage adapters:** Where: apps that save local/cloud. When interchangeable backends are needed. How: define a common interface and implement each backend.
5. **Shape calculations:** Where: drawing/geometry. When many shapes answer area differently. How: abstraction defines area(); concrete shapes implement it.


## 10. Completion
- [ ] I can explain the four pillars and composition.
- [ ] Tests pass.
- [ ] I implemented and tested a second notifier.


## Additional reference — separate OOP track

For deeper design patterns and interview preparation, continue with the [OOP beginner-to-advanced guide](../oop/Python-OOP-Beginner-to-Advanced.md), [topic-by-topic practical guide](../oop/Topic-by-Topic-Code-Explanation-Real-World.md), and [OOP interview workbook](../oop/Professional-Interview-Workbook.md). This day is a learning entry point; it does not replace the separate OOP track.
