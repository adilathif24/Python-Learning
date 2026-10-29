# Day 24 — CSV and JSON

**Status:** Full study pack. Test normal, missing and malformed data before marking mastery.

## 1. Definition
**CSV** stores tabular rows as delimited text; Python's `csv` module handles quoting and separators. **JSON** represents structured data using objects, arrays, strings, numbers, booleans and null. Python's `json` module serializes and parses JSON.

## 2. Why, where, when
Use CSV for spreadsheet-style interchange and JSON for nested API payloads/configuration. Use the standard libraries rather than manual string splitting because quoted delimiters and escaping need correct handling. Validate parsed structure: successful parsing does not mean data is semantically valid.

## 3. Syntax and rules
```python
import csv, json
with open("people.csv", newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))
data = json.loads('{"name":"Adil"}')
print(data["name"])
```
For CSV, use `newline=""` with the module. For JSON, `loads` parses a string and `load` reads a file; `dumps` returns a string and `dump` writes a file.

## 4. Five worked examples
### Example 1 — Read CSV rows
```python
import csv, io
source = io.StringIO("name,score\nAli,80\nMaya,95\n")
rows = list(csv.DictReader(source))
print(rows[1]["name"])
```
Output: `Maya`. DictReader maps column names to values.

### Example 2 — Write CSV
```python
import csv, io
out = io.StringIO(newline="")
writer = csv.writer(out); writer.writerow(["name","score"]); writer.writerow(["Ali",80])
print(out.getvalue(), end="")
```
Output: two rows, `name,score` and `Ali,80`.

### Example 3 — Parse JSON
```python
import json
record = json.loads('{"name":"Ali","active":true}')
print(record["active"])
```
Output: `True`. JSON true maps to Python True.

### Example 4 — Serialize nested data
```python
import json
payload = {"tags":["python","sql"], "count":2}
text = json.dumps(payload, sort_keys=True)
print(text)
```
Output: `{"count": 2, "tags": ["python", "sql"]}`. sort_keys makes key order stable for display.

### Example 5 — Handle malformed JSON
```python
import json
try: json.loads("{bad")
except json.JSONDecodeError: print("Invalid JSON")
```
Output: `Invalid JSON`.

## 5. Five tasks with solutions
### Task 1 — Sum scores from CSV-like rows
```python
rows = [{"score":"80"},{"score":"90"}]
print(sum(int(row["score"]) for row in rows))
```
Output: `170`. Convert strings before calculation.

### Task 2 — Access optional JSON field
```import json
obj = json.loads('{"name":"Ali"}')
print(obj.get("city", "Unknown"))
```
Output: `Unknown`.

### Task 3 — Round-trip JSON
```python
import json
original = {"a":[1,2], "ok":True}
print(json.loads(json.dumps(original)) == original)
```
Output: `True`. Serialization then parsing should preserve compatible values.

### Task 4 — CSV quoting
```python
import csv, io
f=io.StringIO('name,city\n"Ali, A.",Ongole\n')
print(next(csv.DictReader(f))["name"])
```
Output: `Ali, A.`. The CSV parser respects quoted commas.

### Task 5 — Validate top-level JSON type
```import json
data=json.loads('[1,2,3]')
if not isinstance(data, list): raise ValueError("List expected")
print(len(data))
```
Output: `3`.

## 6. Common mistakes
- Splitting CSV lines manually fails when quoted cells contain commas/newlines.
- JSON does not support Python tuples, sets or arbitrary objects directly.
- JSON uses true/false/null; Python representation uses True/False/None.
- Parsing successfully does not validate fields or types.
- Untrusted huge/hostile inputs can still consume resources; apply size and schema limits as required.

## 7. Interview Q&A
1. CSV vs JSON? **CSV is tabular; JSON supports nested structures.**
2. DictReader? **Reads each row as a dict keyed by header.**
3. loads vs load? **String vs file object.**
4. What error on malformed JSON? **JSONDecodeError.**
5. Why validate after parsing? **Format correctness does not guarantee business correctness.**

## 8. Project — CSV Score Report with JSON Summary
Save as `score_report.py`.
```python
import csv, json
from pathlib import Path

def build_report(csv_path, json_path):
    rows=[]
    with open(csv_path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try: score=float(row["score"])
            except (KeyError, ValueError) as error: raise ValueError("Every row needs a numeric score") from error
            if not 0 <= score <= 100: raise ValueError("Score must be 0–100")
            rows.append({"name": row.get("name","").strip(), "score": score})
    report={"count":len(rows),"average":sum(r["score"] for r in rows)/len(rows) if rows else 0,"students":rows}
    Path(json_path).write_text(json.dumps(report,indent=2),encoding="utf-8")
    return report

def main():
    try: print(build_report("scores.csv","report.json"))
    except (OSError, ValueError) as error: print(f"Could not build report: {error}")

if __name__ == "__main__": main()
```
Create scores.csv with columns `name,score`; sample rows `Ali,80` and `Maya,90`. Average is 85.

### Tests — `test_score_report.py`
```python
import csv, json, tempfile, unittest
from pathlib import Path
from score_report import build_report

class ReportTests(unittest.TestCase):
    def write_csv(self, path, rows):
        with path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=["name","score"]); w.writeheader(); w.writerows(rows)
    def test_average(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.write_csv(p/"in.csv",[{"name":"A","score":"80"},{"name":"B","score":"100"}])
            result=build_report(p/"in.csv",p/"out.json")
            self.assertEqual(result["average"],90)
    def test_bad_score(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.write_csv(p/"in.csv",[{"name":"A","score":"bad"}])
            with self.assertRaises(ValueError): build_report(p/"in.csv",p/"out.json")
    def test_out_of_range(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.write_csv(p/"in.csv",[{"name":"A","score":"101"}])
            with self.assertRaises(ValueError): build_report(p/"in.csv",p/"out.json")
    def test_empty_csv(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.write_csv(p/"in.csv",[])
            self.assertEqual(build_report(p/"in.csv",p/"out.json")["count"],0)
    def test_json_written(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.write_csv(p/"in.csv",[{"name":"Ali","score":"75"}]); build_report(p/"in.csv",p/"out.json")
            self.assertEqual(json.loads((p/"out.json").read_text())["count"],1)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 9. Quiz and challenge
1. Which module handles CSV? **csv.**
2. Which function parses JSON text? **json.loads.**
3. How handle CSV headers? **DictReader.**
4. Does valid JSON guarantee correct business data? **No.**
5. Which exception signals malformed JSON? **JSONDecodeError.**
**Challenge:** Extend the report with highest/lowest scorer and tests for ties and an empty file.

## Real-world use cases — where, when and how
1. **Student score import:** Where: school reporting apps. When records come from spreadsheets. How: use DictReader and validate every score before calculation.
2. **API responses:** Where: integrations. When external services respond with nested objects. How: parse JSON then validate key names and value types.
3. **App settings:** Where: local utilities. When named preferences persist between runs. How: store configuration as JSON and supply defaults.
4. **Export reports:** Where: business apps. When tabular results are shared. How: use csv.writer/DictWriter to handle delimiters and quoting safely.
5. **Data exchange:** Where: internal tools. When a nested payload must move between services. How: serialize JSON and version/validate the expected schema.


## 10. Completion
- [ ] I can read/write CSV and JSON.
- [ ] Report tests pass on valid, malformed and boundary cases.
- [ ] I solved the challenge.
