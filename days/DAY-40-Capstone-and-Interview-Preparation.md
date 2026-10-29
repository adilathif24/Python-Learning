# Day 40 — Capstone Project and Interview Preparation

**Status:** Full capstone guide. Mark complete only after implementation, tests, documentation and a mock interview.

## 1. Definition
A **capstone** combines several skills in a complete application. Interview preparation means explaining the problem, design, trade-offs, failures, and tests—not only memorizing definitions.

## 2. Why / where / when
Build a capstone to prove you can connect language fundamentals, OOP, exceptions, files/JSON, tests, and SQLite. Keep its scope small enough to finish. Avoid adding frameworks or AI features before core requirements and tests work.

## 3. Capstone requirements — Personal Task Manager
Features:
- create, list, complete, and delete tasks;
- persist tasks in SQLite;
- validate input and report errors clearly;
- keep database operations in a small module;
- add automated tests;
- provide README setup/use instructions.
Suggested structure:
```text
task_manager/
  app.py
  task_store.py
  tests/
    test_task_store.py
  README.md
```

## 4. Five worked mini-examples
### Example 1 — Function boundary
```python
def validate_title(title):
    if not isinstance(title,str) or not title.strip(): raise ValueError("title required")
    return title.strip()
print(validate_title(" Study "))
```
Output: `Study`.

### Example 2 — Object state
```python
class Task:
    def __init__(self,title): self.title,self.done=title,False
    def complete(self): self.done=True
task=Task("Practise"); task.complete()
print(task.done)
```
Output: `True`.

### Example 3 — Persistence
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE tasks(title TEXT)")
    db.execute("INSERT INTO tasks VALUES (?)",("Study Python",))
    print(db.execute("SELECT title FROM tasks").fetchone()[0])
```
Output: `Study Python`.

### Example 4 — Automated check
```python
assert validate_title("A") == "A"
print("check passed")
```
Output: `check passed`.

### Example 5 — Boundary outcome
```python
try: validate_title(" ")
except ValueError as error: print(error)
```
Output: `title required`.

## 5. Five practice tasks with solution sketches
### Task 1 — Add a task
```python
def add_task(tasks,title):
    title=validate_title(title); tasks.append({"title":title,"done":False})
    return len(tasks)
tasks=[]; print(add_task(tasks,"Study"))
```
Output: `1`.

### Task 2 — Complete by index
```python
def complete_task(tasks,index):
    if not 0 <= index < len(tasks): raise IndexError("task not found")
    tasks[index]["done"]=True
tasks=[{"title":"Study","done":False}]; complete_task(tasks,0)
print(tasks[0]["done"])
```
Output: `True`.

### Task 3 — Filter pending tasks
```tasks=[{"title":"A","done":False},{"title":"B","done":True}]
print([t["title"] for t in tasks if not t["done"]])
```
Output: `['A']`.

### Task 4 — Safely parse an ID
```def parse_id(raw):
    try: value=int(raw)
    except ValueError as error: raise ValueError("ID must be integer") from error
    if value<1: raise ValueError("ID must be positive")
    return value
print(parse_id("3"))
```
Output: `3`.

### Task 5 — Describe test evidence
```tests = {"normal": True, "boundary": True, "invalid": True}
print(all(tests.values()))
```
Output: `True`. In the real project, these booleans must represent tests actually run, not assumptions.

## 6. Common mistakes
- Calling a project complete without tests.
- Storing code, database, validation and UI responsibilities in one giant function.
- Concatenating untrusted values into SQL.
- Not documenting how to run or test the project.
- Claiming production readiness for a learning prototype.

## 7. Interview questions
1. Explain the problem your capstone solves. **Describe the user, pain point, and expected outcome.**
2. Why SQLite? **Simple local persistence and no separate database server for this scope.**
3. How did you validate data? **At input boundaries and in core functions.**
4. How did you test? **Normal, boundary, invalid-input and regression cases.**
5. What would you improve next? **Name a concrete limitation and measurable next step.**

## 8. Starter project — Task domain and in-memory store
Save as `task_manager_core.py`. This is the tested domain layer; add the SQLite storage module as the capstone extension.
```python
def validate_title(title):
    if not isinstance(title,str) or not title.strip(): raise ValueError("Task title required")
    return title.strip()

def add_task(tasks,title):
    task={"title":validate_title(title),"done":False}
    tasks.append(task)
    return task

def complete_task(tasks,index):
    if not isinstance(index,int) or isinstance(index,bool) or not 0 <= index < len(tasks):
        raise IndexError("Task does not exist")
    tasks[index]["done"]=True

def pending_tasks(tasks):
    return [task for task in tasks if not task["done"]]

def main():
    tasks=[]
    while True:
        choice=input("1 Add 2 List pending 3 Complete first 4 Quit: ").strip()
        if choice=="1":
            try: add_task(tasks,input("Title: "))
            except ValueError as error: print(error)
        elif choice=="2": print(pending_tasks(tasks))
        elif choice=="3":
            try: complete_task(tasks,0)
            except IndexError as error: print(error)
        elif choice=="4": break
        else: print("Select 1–4")

if __name__ == "__main__": main()
```

### Tests — `test_task_manager_core.py`
```python
import unittest
from task_manager_core import add_task, complete_task, pending_tasks
class TaskTests(unittest.TestCase):
    def test_add(self):
        tasks=[]; add_task(tasks,"A"); self.assertEqual(len(tasks),1)
    def test_empty_title(self):
        with self.assertRaises(ValueError): add_task([]," ")
    def test_complete(self):
        tasks=[]; add_task(tasks,"A"); complete_task(tasks,0); self.assertEqual(pending_tasks(tasks),[])
    def test_bad_index(self):
        with self.assertRaises(IndexError): complete_task([],0)
    def test_pending_filter(self):
        tasks=[{"title":"A","done":False},{"title":"B","done":True}]
        self.assertEqual([t["title"] for t in pending_tasks(tasks)],["A"])
if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and independent challenge
1. What makes a capstone credible? **Working code, tests, documentation and a clear explanation.**
2. What test categories? **Normal, boundaries, invalid input and regression.**
3. Why separate storage? **Clear responsibility and easier testing.**
4. Why parameterise SQL? **Security and correct value binding.**
5. What does a good improvement plan include? **A real limitation, next action and success criterion.**

**Independent challenge:** Implement SQLite persistence for the task manager, add create/list/complete/delete operations, write at least eight tests, and record a two-minute project walkthrough covering design and trade-offs.

## 10. Completion checklist
- [ ] Complete app runs from clean setup.
- [ ] Automated tests pass.
- [ ] README has setup, usage, examples and test instructions.
- [ ] I can explain every module and key decision.
- [ ] I completed a mock interview without reading the notes.
