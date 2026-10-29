# Day 39 — SQL with Python (Application Track)

**Status:** Full study pack. This lesson covers Python applications using SQL databases; keep it separate from the Data Analyst learning syllabus.

## 1. Definition
SQL retrieves and changes relational data. Python's `sqlite3` module runs SQL statements through a database connection and returns rows to the program. SQLite is included with Python and is useful for learning and local apps.

## 2. Why / where / when
Use a database when data must persist across runs and has relationships or structured queries: inventory, tasks, users, orders. Use parameter placeholders instead of concatenating user input into SQL. Larger multi-user deployments may need a server database such as PostgreSQL or MySQL.

## 3. Syntax and rules
```python
import sqlite3
with sqlite3.connect("app.db") as connection:
    connection.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)")
    connection.execute("INSERT INTO tasks(title) VALUES (?)", ("Study Python",))
    rows=connection.execute("SELECT id,title FROM tasks").fetchall()
```
Use `?` placeholders for SQLite parameters. The connection context manager commits or rolls back a transaction as appropriate, but connection lifetime should still be managed deliberately; with SQLite connection objects, the context manager does not close the connection.

## 4. Five worked examples
### Example 1 — In-memory database
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE students(id INTEGER, name TEXT)")
    db.execute("INSERT INTO students VALUES (?,?)",(1,"Adil"))
    print(db.execute("SELECT * FROM students").fetchall())
```
Output: `[(1, 'Adil')]`.

### Example 2 — Insert many rows
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE tasks(id INTEGER,title TEXT)")
    db.executemany("INSERT INTO tasks VALUES (?,?)",[(1,"Learn"),(2,"Practise")])
    print(db.execute("SELECT title FROM tasks ORDER BY id").fetchall())
```
Output: `[('Learn',), ('Practise',)]`.

### Example 3 — Parameterised query
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE users(name TEXT)")
    db.executemany("INSERT INTO users VALUES (?)",[("Adil",),("Maya",)])
    print(db.execute("SELECT name FROM users WHERE name = ?",("Adil",)).fetchone())
```
Output: `('Adil',)`. Parameterisation keeps values separate from SQL syntax.

### Example 4 — Update data
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE stock(sku TEXT, qty INTEGER)")
    db.execute("INSERT INTO stock VALUES (?,?)",("PEN",10))
    db.execute("UPDATE stock SET qty=? WHERE sku=?",(8,"PEN"))
    print(db.execute("SELECT qty FROM stock WHERE sku=?",("PEN",)).fetchone())
```
Output: `(8,)`.

### Example 5 — Return dictionary-like rows
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.row_factory=sqlite3.Row
    db.execute("CREATE TABLE products(id INTEGER,name TEXT)")
    db.execute("INSERT INTO products VALUES (?,?)",(1,"Notebook"))
    row=db.execute("SELECT * FROM products").fetchone()
    print(dict(row))
```
Output: `{'id': 1, 'name': 'Notebook'}`.

## 5. Five tasks with solutions
### Task 1 — Count records
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE t(v INTEGER)")
    db.executemany("INSERT INTO t VALUES (?)",[(1,),(2,),(3,)])
    print(db.execute("SELECT COUNT(*) FROM t").fetchone()[0])
```
Output: `3`.

### Task 2 — Filter rows
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE scores(name TEXT, score INTEGER)")
    db.executemany("INSERT INTO scores VALUES (?,?)",[("A",80),("B",45)])
    print(db.execute("SELECT name FROM scores WHERE score>=50").fetchall())
```
Output: `[('A',)]`.

### Task 3 — Delete one row safely
```python
import sqlite3
with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE items(id INTEGER)")
    db.executemany("INSERT INTO items VALUES (?)",[(1,),(2,)])
    db.execute("DELETE FROM items WHERE id=?",(1,))
    print(db.execute("SELECT id FROM items").fetchall())
```
Output: `[(2,)]`.

### Task 4 — Roll back a transaction
```import sqlite3
db=sqlite3.connect(":memory:")
db.execute("CREATE TABLE x(v INTEGER)")
try:
    with db:
        db.execute("INSERT INTO x VALUES (1)")
        raise ValueError("cancel")
except ValueError: pass
print(db.execute("SELECT * FROM x").fetchall())
db.close()
```
Output: `[]`. The exception causes transaction rollback.

### Task 5 — Parameterise user search
```python
def find_user(connection, name):
    return connection.execute("SELECT name FROM users WHERE name = ?",(name,)).fetchall()
```
Usage: pass a connection with a users table. Parameter placeholders prevent treating the value as SQL code.

## 6. Common mistakes
- SQL string concatenation risks injection.
- Forgetting commit can lose writes outside transactional context.
- Confusing table name with a parameter; table names generally cannot be bound as values.
- Not checking missing query results from fetchone.
- A SQLite connection context manager manages transactions but does not itself close the connection.

## 7. Interview Q&A
1. Why parameterised queries? **Protect against SQL injection and handle values safely.**
2. fetchone vs fetchall? **One row vs all rows.**
3. What is a transaction? **A unit of database work that is committed or rolled back.**
4. What does PRIMARY KEY do? **Uniquely identifies rows.**
5. When choose SQLite? **Local tools, prototypes, embedded apps and learning; high-concurrency deployments may need a server DB.**

## 8. Project — SQLite Task Manager
Save as `sqlite_task_manager.py`.
```python
import sqlite3

def init_db(connection):
    connection.execute("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )""")

def add_task(connection, title):
    title=title.strip()
    if not title: raise ValueError("Task title is required")
    cursor=connection.execute("INSERT INTO tasks(title) VALUES (?)",(title,))
    return cursor.lastrowid

def list_tasks(connection):
    return connection.execute("SELECT id,title,done FROM tasks ORDER BY id").fetchall()

def complete_task(connection, task_id):
    cursor=connection.execute("UPDATE tasks SET done=1 WHERE id=?",(task_id,))
    if cursor.rowcount == 0: raise ValueError("Task not found")

def main():
    with sqlite3.connect("tasks.db") as connection:
        init_db(connection)
        title=input("Task title: ").strip()
        if title:
            add_task(connection,title)
        print(list_tasks(connection))

if __name__ == "__main__": main()
```
Run `python sqlite_task_manager.py`; tasks persist in `tasks.db`.

### Tests — `test_sqlite_task_manager.py`
```python
import sqlite3, unittest
from sqlite_task_manager import init_db, add_task, list_tasks, complete_task

class TaskDBTests(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(":memory:"); init_db(self.db)
    def tearDown(self): self.db.close()
    def test_add(self):
        add_task(self.db,"Study"); self.assertEqual(list_tasks(self.db)[0][1],"Study")
    def test_empty_title(self):
        with self.assertRaises(ValueError): add_task(self.db," ")
    def test_complete(self):
        task_id=add_task(self.db,"Study"); complete_task(self.db,task_id)
        self.assertEqual(list_tasks(self.db)[0][2],1)
    def test_missing_task(self):
        with self.assertRaises(ValueError): complete_task(self.db,99)
    def test_parameterized_text(self):
        add_task(self.db,"Learn SQL'); DROP TABLE tasks;--")
        self.assertEqual(len(list_tasks(self.db)),1)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Included SQL driver? **sqlite3.**
2. Which placeholder? **? in SQLite.**
3. fetchall returns? **A list of rows.**
4. Why use a primary key? **Unique row identity.**
5. Why parameterise? **Safer and correct value binding.**
**Challenge:** Add deletion by task ID and tests for existing and missing IDs. Keep this database programming topic separate from Data Analyst topics.

## Real-world use cases — where, when and how
1. **Task manager:** Where: personal productivity tool. When records must persist between runs. How: store title/status in SQLite and parameterize all values.
2. **Inventory:** Where: stock systems. When each SKU has quantity and change history. How: use a primary key, transactions and update queries.
3. **Contact lookup:** Where: desktop app. When searching many records by field. How: query with WHERE and indexes where appropriate.
4. **Orders:** Where: checkout. When several related tables must update together. How: use transactions and constraints for consistency.
5. **Application audit:** Where: support tools. When recent actions must be reviewed. How: insert records into an append-style table with timestamps.


## 10. Completion
- [ ] I can connect, query, insert, update and delete with sqlite3.
- [ ] Queries use placeholders for values.
- [ ] Project tests pass.
