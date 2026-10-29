# Python Learning & Technical Interview Preparation

A structured repository for developing Python programming fundamentals, object-oriented design, and data structures and algorithms (DSA), with code examples, practical scenarios, interview explanations, and problem-solving practice.

This repository documents an ongoing learning process. The guides are organised to support interview preparation, but topics should only be considered mastered after the code has been run, tested, and explained independently.

## Learning tracks

Keep these tracks separate and study them in sequence. Each guide includes professional terminology, clear reasoning, code, practical applications, and interview follow-ups.

| Track | What it covers | Main guide |
|---|---|---|
| **Python Core** | Data types, control flow, collections, functions, files, exceptions, generators, type hints and maintainable code | [Core topic guide](core/Topic-by-Topic-Code-Explanation-Real-World.md) · [Professional interview workbook](core/Professional-Interview-Workbook.md) |
| **Object-Oriented Programming** | Classes, object state, constructors, methods, encapsulation, inheritance, polymorphism, abstraction, composition and design trade-offs | [OOP topic guide](oop/Topic-by-Topic-Code-Explanation-Real-World.md) · [Professional interview workbook](oop/Professional-Interview-Workbook.md) |
| **Data Structures & Algorithms** | Complexity, arrays, strings, hashing, two pointers, sliding window, binary search, recursion, stacks, queues, trees, heaps, graphs, greedy and DP | [DSA topic guide](dsa/Topic-by-Topic-Code-Explanation-Real-World.md) · [Professional interview workbook](dsa/Professional-Interview-Workbook.md) |

## Runnable code

Run the examples from the repository root with Python 3:

```bash
python core/examples.py
python oop/examples.py
python dsa/examples.py
```

On Windows, `py` can be used instead of `python` if that is how Python is configured on your system.

- [Core examples](core/examples.py)
- [OOP examples](oop/examples.py)
- [DSA examples](dsa/examples.py)

## How each topic is prepared

The goal is to prepare to **explain and implement a concept in a technical interview**, not merely memorise a definition.

1. **Definition and purpose** — what the concept is and why it exists.
2. **Professional explanation** — how to describe it accurately in an interview.
3. **Code implementation** — readable, runnable Python with meaningful names.
4. **Line-by-line reasoning** — explain the important decisions and control flow.
5. **Output and dry run** — trace how the program behaves.
6. **Real-world application** — identify where the technique or design is useful.
7. **Complexity and trade-offs** — where relevant, explain time, space, assumptions and limitations.
8. **Edge cases and testing** — validate normal, boundary, invalid and no-result cases.
9. **Interview follow-ups** — prepare for “why this approach?”, “what could fail?” and “how would you improve it?”
10. **Independent practice** — solve variations without copying the reference solution.

## Recommended study workflow

1. Complete Python Core fundamentals and practise writing functions.
2. Study OOP separately; build small domain models and explain the design decisions.
3. Study DSA one pattern at a time. Start with a baseline solution, optimise it, then analyse complexity.
4. Run each example locally and test edge cases.
5. Practise explaining solutions aloud in your own words.
6. Build a small project, write tests, document how to run it, and explain its limitations.
7. Mark a topic as interview-ready only when you can solve a new variation independently.

## What professional preparation should demonstrate

- Clear function and class responsibilities.
- Explicit assumptions and validation of input.
- Meaningful names and understandable control flow.
- Correctness arguments and complexity analysis for DSA.
- Appropriate error handling and edge-case tests.
- Awareness of trade-offs rather than claiming one solution fits every situation.
- Honest descriptions of what has been implemented and verified.

## Project and learning notes

- [Python Functions — Arbitrary Positional Arguments (\`*args\`)](core/Functions-Arbitrary-Positional-Arguments-args.md)
- [Python Core — Beginner to Advanced](core/Python-Core-Concepts-Beginner-to-Advanced.md)
- [Python OOP — Beginner to Advanced](oop/Python-OOP-Beginner-to-Advanced.md)
- [DSA — Beginner to Advanced](dsa/DSA-Beginner-to-Advanced.md)
- [Python Interview Preparation](interview/Python-Interview-Preparation.md)
- [Learning roadmap](ROADMAP.md)
- [Mind map](MINDMAP.md)

## Quality and accuracy

The code and notes are learning material, not a guarantee that every example has been executed or that every topic is mastered. Run examples in a Python 3 environment, add tests, verify expected output, and correct any issues found. For money-related calculations, production systems commonly need explicit currency and rounding rules; for algorithms, always state input assumptions.

## AI assistance disclosure

AI tools have assisted with organising material, generating draft examples, and improving explanations. The material should be reviewed, executed, tested, and understood before it is relied on in an interview or represented as independently completed work.

## Profile

- GitHub: [adilathif24](https://github.com/adilathif24)
- Repository: [Python-Learning](https://github.com/adilathif24/Python-Learning)
