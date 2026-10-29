# Day 23 — Files, Paths and Encoding

**Status:** Full study pack. Complete the examples and file-backed project tests before marking mastery.

## 1. Definition
A file stores data beyond a program run. Python uses `open()` to access a file; `with` ensures the file is closed even when an error occurs. A path identifies a file or directory.

## 2. Why, where, when
Use files for logs, saved settings, reports and small persistent records. Use `pathlib.Path` for path operations and specify encoding such as UTF-8 for text. Avoid overwriting important files unintentionally; use append or atomic-write patterns where appropriate.

## 3. Syntax and rules
```python
from pathlib import Path
path = Path("notes.txt")
path.write_text("Hello\n", encoding="utf-8")
text = path.read_text(encoding="utf-8")
print(text)
```
Common modes: `r` read; `w` write/truncate; `a` append; `x` create only if absent; `b` binary. Prefer `with open(path, encoding="utf-8") as file:`.

## 4. Five worked examples
### Example 1 — Write and read
```python
from pathlib import Path
p = Path("example.txt")
p.write_text("Python", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
p.unlink()
```
Output: `Python`. The final line cleans up the demo file.

### Example 2 — Append
```python
from pathlib import Path
p = Path("log.txt")
p.write_text("start\n", encoding="utf-8")
with p.open("a", encoding="utf-8") as file: file.write("done\n")
print(p.read_text(encoding="utf-8"), end="")
p.unlink()
```
Output: start then done on separate lines.

### Example 3 — Safe missing-file handling
```python
from pathlib import Path
p = Path("missing-demo.txt")
try: p.read_text(encoding="utf-8")
except FileNotFoundError: print("File not found")
```
Output: `File not found`.

### Example 4 — Count lines
```python
content = "a\nb\nc\n"
print(len(content.splitlines()))
```
Output: `3`. splitlines handles line separators.

### Example 5 — Use a context manager
```from pathlib import Path
p = Path("with-demo.txt")
with p.open("w", encoding="utf-8") as file:
    file.write("closed automatically")
print(p.read_text(encoding="utf-8"))
p.unlink()
```
Output: `closed automatically`. The file is closed at block exit.

## 5. Five tasks with solutions
### Task 1 — Save several lines
```python
from pathlib import Path
p=Path("task-lines.txt")
p.write_text("\n".join(["one","two","three"]),encoding="utf-8")
print(p.read_text(encoding="utf-8").splitlines())
p.unlink()
```
Output: `['one', 'two', 'three']`.

### Task 2 — Append a log line
```from pathlib import Path
p=Path("task-log.txt")
with p.open("a",encoding="utf-8") as f: f.write("event\n")
print(p.read_text(encoding="utf-8").strip())
p.unlink()
```
Output: `event`.

### Task 3 — Detect a path
```from pathlib import Path
p=Path(".")
print(p.exists(), p.is_dir())
```
Output starts with `True True` for the current working directory.

### Task 4 — Count words in file text
```python
text="Python is useful"
print(len(text.split()))
```
Output: `3`. The same approach can be applied to the text read from a file.

### Task 5 — Handle Unicode
```python
from pathlib import Path
p=Path("unicode.txt")
p.write_text("नमस्ते Python",encoding="utf-8")
print(p.read_text(encoding="utf-8"))
p.unlink()
```
Output: `नमस्ते Python`.

## 6. Common mistakes
- `w` overwrites an existing file.
- Relative paths resolve from the current working directory.
- Not specifying encoding can make files behave differently across systems.
- Forgetting `with` can leave file handles open.
- Catch FileNotFoundError specifically when that is the intended recoverable case.

## 7. Interview Q&A
1. Why use with open? **It closes the resource reliably.**
2. Difference between w and a? **w truncates/creates; a appends/creates.**
3. What is UTF-8? **A widely used Unicode text encoding.**
4. How handle missing file? **Catch FileNotFoundError or check path.exists when appropriate.**
5. What is a relative path? **Path interpreted from current working directory.**

## 8. Project — Persistent Contact List
Save as `contacts_file.py`.
```python
import json
from pathlib import Path

def save_contacts(path, contacts):
    Path(path).write_text(json.dumps(contacts, ensure_ascii=False, indent=2), encoding="utf-8")

def load_contacts(path):
    p = Path(path)
    if not p.exists(): return []
    try: data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error: raise ValueError("Contacts file is invalid JSON") from error
    if not isinstance(data, list): raise ValueError("Contacts file must contain a list")
    return data

def main():
    path = Path("contacts.json")
    contacts = load_contacts(path)
    name = input("Contact name: ").strip()
    if name:
        contacts.append({"name": name})
        save_contacts(path, contacts)
    print(contacts)

if __name__ == "__main__": main()
```
Run `python contacts_file.py`; enter a name to persist it in contacts.json.

### Tests — `test_contacts_file.py`
```python
import json, tempfile, unittest
from pathlib import Path
from contacts_file import save_contacts, load_contacts

class ContactsTests(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"contacts.json"; save_contacts(p,[{"name":"Adil"}])
            self.assertEqual(load_contacts(p),[{"name":"Adil"}])
    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as d: self.assertEqual(load_contacts(Path(d)/"x.json"),[])
    def test_bad_json(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.json"; p.write_text("{",encoding="utf-8")
            with self.assertRaises(ValueError): load_contacts(p)
    def test_wrong_shape(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.json"; p.write_text(json.dumps({}),encoding="utf-8")
            with self.assertRaises(ValueError): load_contacts(p)
    def test_unicode(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.json"; save_contacts(p,[{"name":"नमस्ते"}])
            self.assertEqual(load_contacts(p)[0]["name"],"नमस्ते")

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Which mode overwrites? **w.**
2. Which mode appends? **a.**
3. How ensure text encoding? **Specify encoding="utf-8".**
4. What handles missing files? **FileNotFoundError.**
5. Why use pathlib? **Clear, cross-platform path operations.**
**Challenge:** Add delete-by-name contact functionality and write tests for present, absent and empty names.

## 10. Completion
- [ ] I can read, write, append, and use paths safely.
- [ ] Contact persistence tests pass.
- [ ] Challenge completed.
