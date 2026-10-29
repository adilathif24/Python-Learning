# Day 06 — Strings in Python

**Status:** Full study pack published. Finish examples, tasks, tests and challenge before marking mastery.

## 1. Definition

A **string** (`str`) is an immutable sequence of Unicode characters. It supports indexing, slicing, iteration, comparison, and methods for searching or transforming text. Since strings are immutable, string methods return new strings rather than changing the original.

## 2. Why, where and when

Strings are used for names, messages, identifiers, filenames, logs and text entered by users. Index when you need a character at a known position; slice when you need a portion; use methods like `strip()`, `split()`, and `join()` to normalise or process text. For complex formats like email addresses, URLs or CSV data, use purpose-built parsers or libraries instead of a long chain of fragile string checks.

## 3. Syntax and rules

```python
text = "python"
print(text[0])       # p
print(text[-1])      # n
print(text[1:4])     # yth
print(text.upper())  # PYTHON
parts = "a,b,c".split(",")
print("-".join(parts))
```

- Indexes start at 0; negative indexes count from the end.
- A slice `text[start:stop:step]` excludes the stop index.
- Strings are immutable: `text[0] = "P"` raises `TypeError`.
- `strip()` removes whitespace at both ends; it does not remove every internal space.
- `split()` returns a list; `join()` joins an iterable of strings.
- Case operations can change characters; use `casefold()` for robust case-insensitive comparisons in many human-text use cases.

### Dry run

For `word = "python"`, `word[1:4]` starts at index 1 (`y`) and stops before index 4 (`o`), so the result is `yth`.

## 4. Five worked examples

### Example 1 — Index and slice

```python
word = "python"
print(word[0])
print(word[-1])
print(word[1:4])
print(word[::-1])
```
**Output**
```text
p
n
yth
nohtyp
```
**Explanation:** Negative index selects from the end; a negative step reverses the sequence.

### Example 2 — Normalize user text

```python
raw = "   Adil Ali  "
clean = raw.strip()
print(clean)
print(clean.casefold())
```
**Output**
```text
Adil Ali
adil ali
```
**Explanation:** `strip()` removes edge whitespace; `casefold()` enables case-insensitive comparison.

### Example 3 — Count vowels

```python
text = "Python Programming"
vowels = set("aeiou")
count = sum(1 for char in text.casefold() if char in vowels)
print(count)
```
**Output:** `4`  
**Explanation:** Iterate through characters and count those that belong to the vowel set; spaces and consonants are ignored.

### Example 4 — Split and join

```python
csv_line = "red, green, blue"
colors = [part.strip() for part in csv_line.split(",")]
print(colors)
print(" | ".join(colors))
```
**Output**
```text
['red', 'green', 'blue']
red | green | blue
```
**Explanation:** Split separates text into items; stripping each item removes surrounding spaces.

### Example 5 — Case-insensitive palindrome

```python
text = "Never odd or even"
normalized = "".join(char.casefold() for char in text if char.isalnum())
print(normalized == normalized[::-1])
```
**Output:** `True`  
**Explanation:** Remove non-alphanumeric characters and normalise case before comparing the string with its reverse.

## 5. Five practice tasks with complete solutions

### Task 1 — Count characters excluding spaces

```python
text = "learn python well"
count = sum(1 for char in text if not char.isspace())
print(count)
```
**Output:** `14`  
**Explanation:** `isspace()` recognises whitespace beyond ordinary spaces, including tabs.

### Task 2 — Replace a word

```python
message = "I learn Java"
updated = message.replace("Java", "Python")
print(updated)
```
**Output:** `I learn Python`  
**Explanation:** `replace()` returns a new string; it does not mutate the original.

### Task 3 — First and last name

```python
full_name = "  Syed Adil Ali  "
parts = full_name.split()
print(parts[0])
print(parts[-1])
```
**Output**
```text
Syed
Ali
```
**Explanation:** `split()` with no separator handles runs of whitespace and ignores outer whitespace.

### Task 4 — Character frequency

```python
text = "banana"
target = "a"
print(text.count(target))
```
**Output:** `3`  
**Explanation:** `count()` counts non-overlapping occurrences of the substring.

### Task 5 — Validate a simple username

```python
def valid_username(value):
    return value.isascii() and value.isalnum() and 3 <= len(value) <= 16

print(valid_username("adil123"))
print(valid_username("ad"))
print(valid_username("adil ali"))
```
**Output**
```text
True
False
False
```
**Explanation:** This deliberately narrow rule allows only ASCII letters/digits and lengths 3–16; production policies may differ.

## 6. Common mistakes and edge cases

- Strings are immutable; build a new string or use a list when making many incremental changes.
- `text[100]` raises `IndexError`; slicing out of bounds is allowed and clips to the available range.
- `split(",")` and `split()` behave differently.
- `len(text)` counts Unicode code points, which may not match user-perceived grapheme clusters.
- `lower()`/ `casefold()` help normalise case, but do not replace language-aware text processing for every locale.
- A string that looks like a number is still text until converted.
- Test empty strings, repeated characters, spaces, punctuation and uppercase/lowercase input.

## 7. Interview questions and answers

**Q1. Are Python strings mutable?** No; operations create new strings.

**Q2. Difference between indexing and slicing?** Indexing returns one element and can raise `IndexError`; slicing returns a sequence portion and tolerates out-of-range bounds.

**Q3. What does `strip()` do?** Removes leading/trailing whitespace by default.

**Q4. Difference between `split()` and `join()`?** `split()` divides a string into a list; `join()` combines strings from an iterable using a separator.

**Q5. Why use `casefold()`?** It is designed for caseless text matching and can be more thorough than `lower()`.

**Q6. Why use a list to assemble many string pieces?** It avoids repeatedly rebuilding a string in a loop; join the pieces at the end.

## 8. Real-world mini-project — Text Analyzer

Save as `text_analyzer.py`. It reports words, characters, vowels and case-insensitive palindrome status.

```python
def analyze_text(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = text.split()
    normalized = "".join(char.casefold() for char in text if char.isalnum())
    vowel_set = set("aeiou")
    return {
        "characters": len(text),
        "characters_without_whitespace": sum(not char.isspace() for char in text),
        "words": len(words),
        "vowels": sum(char.casefold() in vowel_set for char in text),
        "palindrome_ignoring_spaces_punctuation_case": bool(normalized) and normalized == normalized[::-1],
    }


def main():
    text = input("Enter text: ")
    result = analyze_text(text)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```

### Sample run
```text
Enter text: Never odd or even
characters: 17
characters_without_whitespace: 15
words: 4
vowels: 6
palindrome_ignoring_spaces_punctuation_case: True
```

### Tests

Save as `test_text_analyzer.py`; run `python -m unittest -v`.

```python
import unittest
from text_analyzer import analyze_text


class TestTextAnalyzer(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(analyze_text("hello world")["words"], 2)

    def test_empty_string(self):
        result = analyze_text("")
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["characters"], 0)

    def test_palindrome(self):
        self.assertTrue(analyze_text("Never odd or even")["palindrome_ignoring_spaces_punctuation_case"])

    def test_whitespace_only(self):
        self.assertEqual(analyze_text("  \t ")["words"], 0)

    def test_non_string_rejected(self):
        with self.assertRaises(TypeError):
            analyze_text(123)


if __name__ == "__main__":
    unittest.main()
```

## 9. Revision quiz

1. Are strings mutable?
2. What is `"python"[1:4]`?
3. What does `split()` return?
4. What does `strip()` remove by default?
5. Why is `"".join(parts)` used?

### Answer key
1. No.
2. `yth`.
3. A list of strings.
4. Leading and trailing whitespace.
5. To combine string pieces efficiently with the empty string as separator.

### Independent challenge
Add a frequency summary that reports each alphabetic character's count, case-insensitively. Test empty input, repeated letters, punctuation and Unicode text; explain how your code treats accented letters.

## 10. Progress checklist

- [ ] I can explain indexing, slicing, immutability, splitting and joining.
- [ ] I ran all five examples and tasks.
- [ ] The text-analyzer tests pass.
- [ ] I solved the independent challenge.

## Real-world use cases — where, when and how
1. **Form cleanup:** Where: user registration. When: accidental whitespace is present. How: strip values before validation.
2. **Search:** Where: contact finder. When: case should not matter. How: normalise with casefold and compare.
3. **Text analytics:** Where: feedback summaries. When: word/character counts are needed. How: split text and count tokens/chars.
4. **Parsing tags:** Where: simple command-line lists. When: comma-separated input is expected. How: split, strip each value, then validate.
5. **Safe display:** Where: reports. When: only partial identifiers should show. How: mask all but the required final characters.

