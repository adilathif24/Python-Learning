# Day 39 — SQL with Python (Application Track)

**Status:** Planned  
**Scope:** This is only about connecting Python applications to SQL databases. Keep it separate from the Data Analyst learning syllabus.

## Definition
SQL is used to query and modify relational data. Python database drivers let an application send SQL statements and retrieve results.

## Example 1 — SQLite in-memory database
```python
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE students (id INTEGER, name TEXT)")
    connection.execute("INSERT INTO students VALUES (?, ?)", (1, "Adil"))
    rows = connection.execute("SELECT id, name FROM students").fetchall()
    print(rows)
```
Output: `[(1, 'Adil')]`

## Example 2 — Insert multiple rows safely
```python
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE tasks (id INTEGER, title TEXT)")
    tasks = [(1, "Learn Python"), (2, "Practise SQL")]
    connection.executemany("INSERT INTO tasks VALUES (?, ?)", tasks)
    print(connection.execute("SELECT title FROM tasks ORDER BY id").fetchall())
```

## Example 3 — Parameterised query
```python
import sqlite3

name_to_find = "Adil"
with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    connection.executemany("INSERT INTO users VALUES (?, ?)", [(1, "Adil"), (2, "Mina")])
    row = connection.execute(
        "SELECT id, name FROM users WHERE name = ?", (name_to_find,)
    ).fetchone()
    print(row)
```
Use placeholders and parameters; do not build SQL by concatenating untrusted input.

## Example 4 — Update and delete
```python
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE inventory (sku TEXT, quantity INTEGER)")
    connection.execute("INSERT INTO inventory VALUES (?, ?)", ("PEN", 10))
    connection.execute("UPDATE inventory SET quantity = ? WHERE sku = ?", (8, "PEN"))
    print(connection.execute("SELECT * FROM inventory").fetchall())
    connection.execute("DELETE FROM inventory WHERE sku = ?", ("PEN",))
    print(connection.execute("SELECT * FROM inventory").fetchall())
```

## Example 5 — Convert rows into dictionaries
```python
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.row_factory = sqlite3.Row
    connection.execute("CREATE TABLE products (id INTEGER, name TEXT)")
    connection.execute("INSERT INTO products VALUES (?, ?)", (1, "Notebook"))
    row = connection.execute("SELECT * FROM products").fetchone()
    print(dict(row))
```

## Where / when / how
- Where: user accounts, inventory, task management, booking and business applications.
- When: data must persist between runs and can be represented in related tables.
- How: connect using a driver, parameterise SQL, commit writes when appropriate, handle exceptions, close resources and protect credentials.
- SQLite is included with Python and is useful for learning and small local applications. Larger deployments may use PostgreSQL or MySQL drivers.

## Practice tasks
1. Create a table and insert three rows.
2. Query records using a parameterised filter.
3. Update one row and verify the result.
4. Delete one row and verify the result.
5. Build a small task manager that stores tasks in SQLite.

## Interview questions
1. Why use parameterised SQL?
2. What is the difference between `fetchone()` and `fetchall()`?
3. Why use a context manager for a connection?
4. What is a transaction?
5. When would SQLite be unsuitable for a multi-user application?

**Completion checklist:** Run all five examples, test invalid inputs, and complete the task-manager mini-project before marking Completed.
