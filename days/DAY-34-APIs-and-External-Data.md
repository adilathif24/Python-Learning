# Day 34 — APIs and External Data

**Status:** Planned  
**Goal:** Learn how Python requests data from a web API and validates the response.

## Definition
An API (Application Programming Interface) defines how programs exchange data. A web API commonly responds with JSON over HTTP.

## Core concepts
- GET: retrieve data; POST: submit/create data.
- Status codes communicate success or failure.
- JSON represents structured data as objects, arrays, strings, numbers, booleans and null.
- Validate external data; do not assume every request succeeds.

## Example 1 — Parse JSON without the network
```python
import json

payload = '{"name": "Adil", "skills": ["Python", "SQL"]}'
data = json.loads(payload)
print(data["name"])
print(data["skills"][0])
```
Output:
```text
Adil
Python
```

## Example 2 — Build a query string
```python
from urllib.parse import urlencode

params = {"q": "python basics", "page": 2}
print(urlencode(params))
```

## Example 3 — Make an HTTP request with the standard library
```python
from urllib.request import Request, urlopen
import json

url = "https://jsonplaceholder.typicode.com/todos/1"
request = Request(url, headers={"User-Agent": "PythonLearning/1.0"})
with urlopen(request, timeout=10) as response:
    print("Status:", response.status)
    todo = json.load(response)
    print(todo["title"])
```
This example requires internet access. A network or service error is possible.

## Example 4 — Handle expected request failures
```python
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

request = Request(
    "https://jsonplaceholder.typicode.com/todos/1",
    headers={"User-Agent": "PythonLearning/1.0"}
)
try:
    with urlopen(request, timeout=10) as response:
        data = json.load(response)
        print(data.get("title", "Title missing"))
except HTTPError as error:
    print("HTTP error:", error.code)
except URLError as error:
    print("Network error:", error.reason)
except json.JSONDecodeError:
    print("The server returned invalid JSON")
```

## Example 5 — Validate fields before use
```python
def display_user(data):
    user_id = data.get("id")
    name = data.get("name")
    if not isinstance(user_id, int) or not isinstance(name, str) or not name.strip():
        raise ValueError("Expected an integer id and a non-empty name")
    return f"{user_id}: {name}"

print(display_user({"id": 7, "name": "Mina"}))
```

## Where / when / how
- Where: dashboards, job listings, weather apps, payment integrations and automation.
- When: another service owns the data or provides a capability.
- How: send a request, set a timeout, check status, parse the response, validate fields, handle failures and protect secrets.
- Never hard-code API keys in a public repository; use environment variables.

## Practice tasks
1. Parse a JSON string and print two fields.
2. Create query parameters with `urlencode`.
3. Fetch a public JSON endpoint with a timeout.
4. Handle HTTP and network errors separately.
5. Validate a response before converting it into a Python object.

## Interview questions
1. What is an API?
2. What is the difference between GET and POST?
3. Why should requests have a timeout?
4. What is JSON and how does Python parse it?
5. How should an API key be stored safely?

**Completion checklist:** Run offline examples first, then network examples; test missing fields and failures before marking Completed.
