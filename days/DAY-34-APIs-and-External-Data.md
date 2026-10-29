# Day 34 — APIs and External Data

**Status:** Full study pack. Complete offline examples first; network calls may depend on internet/service availability.

## 1. Definition
An **API** defines how software components communicate. A web API commonly exchanges JSON over HTTP. A client sends a request, receives a status and payload, parses it, validates expected fields, and handles failures.

## 2. Why / where / when
Use APIs when another service owns data or offers a capability: job listings, maps, weather, payments, analytics, or internal business services. Set timeouts, check status, validate responses, respect rate limits, and keep secret tokens in environment variables. Never assume a successful HTTP response contains valid application data.

## 3. Syntax and rules
```python
from urllib.request import Request, urlopen
import json
request = Request("https://jsonplaceholder.typicode.com/todos/1",
                  headers={"User-Agent":"PythonLearning/1.0"})
with urlopen(request, timeout=10) as response:
    data = json.load(response)
```
GET typically retrieves resources; POST usually sends data to create/process a resource. A timeout bounds waiting. HTTPError represents HTTP status errors; URLError represents network/URL errors. The sample API is public demo data; the network example needs internet.

## 4. Five worked examples
### Example 1 — Parse JSON offline
```python
import json
data=json.loads('{"name":"Adil","skills":["Python","SQL"]}')
print(data["name"], data["skills"][0])
```
Output: `Adil Python`.

### Example 2 — Build query parameters
```python
from urllib.parse import urlencode
print(urlencode({"q":"python basics","page":2}))
```
Output: `q=python+basics&page=2`. urlencode escapes query values.

### Example 3 — Validate a payload
```python
def display_user(data):
    user_id=data.get("id"); name=data.get("name")
    if not isinstance(user_id,int) or not isinstance(name,str) or not name.strip():
        raise ValueError("Expected integer id and non-empty name")
    return f"{user_id}: {name}"
print(display_user({"id":7,"name":"Mina"}))
```
Output: `7: Mina`.

### Example 4 — Handle network errors
```python
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json
request=Request("https://jsonplaceholder.typicode.com/todos/1",headers={"User-Agent":"PythonLearning/1.0"})
try:
    with urlopen(request,timeout=5) as response: data=json.load(response)
    print(data.get("title","Missing title"))
except HTTPError as error: print("HTTP status:",error.code)
except URLError as error: print("Network failure:",error.reason)
except json.JSONDecodeError: print("Invalid JSON")
```
Output depends on service/network; each expected failure is handled separately.

### Example 5 — Read an environment variable
```python
import os
token=os.getenv("DEMO_API_TOKEN")
print("Configured" if token else "Token not configured")
```
Output is based on the environment. Never print secret values into logs.

## 5. Five practice tasks with solutions
### Task 1 — Read a JSON title
```python
import json
payload='{"title":"Learn APIs","done":false}'
record=json.loads(payload)
print(record["title"])
```
Output: `Learn APIs`.

### Task 2 — Require an object
```import json
data=json.loads('{"id":3}')
if not isinstance(data,dict): raise ValueError("Object expected")
print(data["id"])
```
Output: `3`.

### Task 3 — Handle missing field
```def get_title(data):
    title=data.get("title")
    if not isinstance(title,str) or not title.strip(): raise ValueError("title required")
    return title
print(get_title({"title":"Job listing"}))
```
Output: `Job listing`.

### Task 4 — Build a query
```from urllib.parse import urlencode
print(urlencode({"city":"Hyderabad","page":1}))
```
Output: `city=Hyderabad&page=1`.

### Task 5 — Handle status without network
```def ensure_success(status):
    if not 200 <= status < 300: raise ValueError(f"Request failed: {status}")
    return True
print(ensure_success(200))
```
Output: `True`.

## 6. Common mistakes
- No timeout can hang an application.
- Network status does not guarantee valid JSON.
- Parsed JSON doesn't guarantee expected keys or types.
- Hard-coded API secrets can leak in public repositories.
- A retry policy should be bounded and should respect rate limits.
- Not every HTTP error should be retried; inspect status and operation semantics.

## 7. Interview Q&A
1. What is an API? **A contract for software components to communicate.**
2. GET vs POST? **GET retrieves; POST submits/processes data, depending on the API contract.**
3. Why use timeout? **Avoid indefinite waits.**
4. Why validate payload? **External service data may be missing or have unexpected types.**
5. Where store keys? **Environment variables or a secure secret manager.**

## 8. Project — Public Todo Fetcher
Save as `todo_client.py`.
```python
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def validate_todo(data):
    if not isinstance(data,dict): raise ValueError("Todo must be an object")
    if not isinstance(data.get("id"),int): raise ValueError("id must be an integer")
    if not isinstance(data.get("title"),str) or not data["title"].strip(): raise ValueError("title required")
    return {"id":data["id"],"title":data["title"],"completed":bool(data.get("completed",False))}

def fetch_todo(todo_id, timeout=5):
    if not isinstance(todo_id,int) or isinstance(todo_id,bool) or todo_id <= 0:
        raise ValueError("todo_id must be positive")
    request=Request(f"https://jsonplaceholder.typicode.com/todos/{todo_id}",headers={"User-Agent":"PythonLearning/1.0"})
    with urlopen(request,timeout=timeout) as response:
        if not 200 <= response.status < 300: raise ValueError(f"HTTP status {response.status}")
        data=json.load(response)
    return validate_todo(data)

def main():
    try: print(fetch_todo(int(input("Todo ID: ").strip())))
    except (ValueError, HTTPError, URLError, TimeoutError, json.JSONDecodeError) as error:
        print(f"Could not fetch todo: {error}")

if __name__ == "__main__": main()
```
Run `python todo_client.py`; example output is a todo record if the demo endpoint is reachable.

### Tests — `test_todo_client.py`
```python
import unittest
from todo_client import validate_todo

class TodoTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate_todo({"id":1,"title":"x"})["id"],1)
    def test_missing_title(self):
        with self.assertRaises(ValueError): validate_todo({"id":1})
    def test_wrong_id(self):
        with self.assertRaises(ValueError): validate_todo({"id":"1","title":"x"})
    def test_wrong_shape(self):
        with self.assertRaises(ValueError): validate_todo([])
    def test_completed_default(self): self.assertFalse(validate_todo({"id":1,"title":"x"})["completed"])

if __name__ == "__main__": unittest.main()
```
The tests exercise offline validation, not internet availability. Run `python -m unittest -v`.

## 9. Quiz and challenge
1. What is JSON? **A structured text data format.**
2. Why timeout? **Bound waiting.**
3. What does urlencode do? **Encodes query parameters.**
4. Why validate fields? **Payload shape may differ from assumptions.**
5. Why protect API tokens? **They can grant access or incur costs.**
**Challenge:** Add a small retry for temporary URL errors, cap attempts at 3, and test the retry function using a mocked fetch function rather than requiring internet.

## 10. Completion
- [ ] Offline JSON examples work.
- [ ] Validation tests pass.
- [ ] I can describe timeout/status/validation/security.
