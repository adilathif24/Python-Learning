# Day 16 — String Mastery

**Status:** Full study pack published. Complete exercises, tests and challenge before marking mastery.

## 1. Definition and purpose
Strings are immutable Unicode sequences. String mastery means choosing the right string methods, iteration strategy, normalisation, parsing and formatting. It is useful for text cleanup, logs, search, filenames and user inputs. For complicated formats, use dedicated parsers rather than brittle manual splitting.

## 2. Syntax and rules
```python
text = "  Python, SQL, Python "
clean = text.strip()
parts = [part.strip() for part in clean.split(",")]
print(parts)
print(" | ".join(parts))
```
Indexes begin at 0; slices exclude stop. Methods return new strings. `split()` separates; `join()` combines. `casefold()` helps caseless matching. `isalpha()`, `isdigit()`, `isalnum()`, and `isspace()` test character categories.

Dry run: `" A, B ".strip().split(",")` yields `[" A", " B"]`; strip each part to remove internal token whitespace.

## 3. Five worked examples
### Example 1 — Clean a list of tags
```python
raw = " Python,SQL, python , Git "
tags = [tag.strip().casefold() for tag in raw.split(",") if tag.strip()]
print(tags)
```
Output: `['python', 'sql', 'python', 'git']`. Each token is stripped and normalised.

### Example 2 — Count words
```python
sentence = "Learn Python step by step"
print(len(sentence.split()))
```
Output: `5`. Splitting without a separator handles runs of whitespace.

### Example 3 — Frequency of characters
```python
from collections import Counter
print(Counter("banana")["a"])
```
Output: `3`. Counter tallies hashable characters.

### Example 4 — Mask all but last four digits
```python
card = "1234567812345678"
print("*" * (len(card)-4) + card[-4:])
```
Output: `************5678`. Never print full sensitive payment information in real applications.

### Example 5 — Validate ASCII identifier
```python
def valid_identifier(value):
    return value.isascii() and value.replace("_", "a").isalnum() and bool(value) and not value[0].isdigit()
print(valid_identifier("user_01"))
print(valid_identifier("01user"))
```
Output: `True` then `False`. This is a deliberately narrow rule, not Python's full identifier grammar.

## 4. Five tasks with solutions
### Task 1 — Title case names
```python
name = "  syed adil ali "
print(" ".join(part.capitalize() for part in name.split()))
```
Output: `Syed Adil Ali`. Split normalises spaces; capitalize adjusts each word's first letter.

### Task 2 — Remove punctuation
```python
import string
text = "Hi, Python!"
clean = "".join(char for char in text if char not in string.punctuation)
print(clean)
```
Output: `Hi Python`. Punctuation is filtered character by character.

### Task 3 — Check prefix and suffix
```python
filename = "report.csv"
print(filename.endswith(".csv"), filename.startswith("report"))
```
Output: `True True`. Dedicated methods express the intent.

### Task 4 — Get initials
```python
name = "Syed Adil Ali"
initials = "".join(part[0].upper() for part in name.split())
print(initials)
```
Output: `SAA`. Each word contributes its first character.

### Task 5 — Normalise repeated whitespace
```python
messy = "Python   is\tvery   useful"
print(" ".join(messy.split()))
```
Output: `Python is very useful`. Split/join collapses whitespace runs.

## 5. Common mistakes and edge cases
- Strings are immutable.
- `split(",")` differs from `split()`.
- Slicing beyond bounds is safe, indexing beyond bounds is not.
- Unicode text may contain combined characters; length may differ from visible character count.
- Never use an oversimplified email/URL regex as a full standards-compliant validator.
- Escape special characters when building regex patterns.

## 6. Interview questions
1. Why are strings immutable? **Operations return new string objects rather than changing existing ones.**
2. `split` vs `join`? **split creates a list; join combines strings.**
3. What is casefold? **Text normalisation for caseless comparisons.**
4. What does startswith do? **Checks a prefix.**
5. Why use Counter? **Convenient frequency counting.**

## 7. Project — Text Analyser
Save `text_analyser.py`.
```python
from collections import Counter
import string

def analyse(text):
    if not isinstance(text, str): raise TypeError("text must be str")
    words = [word.strip(string.punctuation).casefold() for word in text.split()]
    words = [word for word in words if word]
    normalized = "".join(ch.casefold() for ch in text if ch.isalnum())
    return {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(set(words)),
        "top_words": Counter(words).most_common(3),
        "normalized_palindrome": bool(normalized) and normalized == normalized[::-1],
    }

def main():
    report = analyse(input("Enter text: "))
    for key, value in report.items(): print(f"{key}: {value}")

if __name__ == "__main__": main()
```
Run with `python text_analyser.py`; input `Never odd or even` reports 4 words and a true normalized palindrome.

### Tests — `test_text_analyser.py`
```python
import unittest
from text_analyser import analyse

class AnalyseTests(unittest.TestCase):
    def test_word_count(self): self.assertEqual(analyse("Hi there!")["words"],2)
    def test_empty(self): self.assertEqual(analyse("")["words"],0)
    def test_repeat(self): self.assertEqual(analyse("red red blue")["top_words"][0],("red",2))
    def test_palindrome(self): self.assertTrue(analyse("Never odd or even")["normalized_palindrome"])
    def test_wrong_type(self):
        with self.assertRaises(TypeError): analyse(8)

if __name__ == "__main__": unittest.main()
```
Run `python -m unittest -v`.

## 8. Quiz and challenge
1. Are strings mutable? **No.**
2. What counts whitespace-separated words? **`len(text.split())`.**
3. What combines strings? **join.**
4. What checks a suffix? **endswith.**
5. What library class counts characters? **Counter.**
**Challenge:** Add a report of the top five non-empty words, ignoring punctuation and case. Test empty input and repeated words.

## 9. Progress checklist
- [ ] I ran all examples and tasks.
- [ ] Project tests pass.
- [ ] I solved the challenge independently.
