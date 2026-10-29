# Python Learning Portfolio

A structured, hands-on record of my Python learning: concepts, runnable examples, problem-solving practice, debugging notes, and small projects.

I am building this repository to strengthen programming fundamentals and prepare for technical interviews. It documents what I have practised and what I plan to learn next; planned topics are not presented as completed skills.

## Current focus

- Variables, built-in data types, input and output
- Arithmetic, comparison and logical operators
- if / elif / else conditions
- for and while loops, range(), counters and accumulators
- Number problems: sum, multiplication tables, factorial, prime check, Fibonacci, digit count and swapping
- String iteration and vowel/consonant counting
- Functions, parameters, arguments, calls and return values
- Lists, indexing, membership, append(), remove() and len()
- Name Management mini-project using functions, conditions and lists

## Repository map

| File | Purpose |
| --- | --- |
| [Detailed learning notes](notes/Python-Basics-to-Functions-and-Lists.md) | Definitions, syntax, examples, dry runs, common mistakes, practice problems with solutions and interview Q&A |
| [Learning roadmap](ROADMAP.md) | Beginner-to-advanced sequence with honest progress checkpoints |
| [Mind map](MINDMAP.md) | Quick view of how topics connect |

## How I practise

For each topic, I aim to:
1. Explain the concept in my own words.
2. Type and run examples rather than only copy them.
3. Predict the output and dry-run variable changes.
4. Test normal inputs, boundary values and invalid inputs.
5. Solve questions without looking at solutions first.
6. Refactor the code for readability and explain its limitations.
7. Mark a topic complete only when I can use it independently.

## Current project

### Name Management — beginner console project

Practises adding names, preventing active duplicates, deleting names, restoring deleted names, and displaying current counts. At this stage, data is stored in Python lists and is lost when the program exits. It is a learning project, not a production contact-management system.

Next improvements: menu-driven input, case-insensitive matching, automated tests, file persistence, and clearer separation between program logic and user interface.

## Roadmap

The full roadmap continues through collections, functions, debugging and testing, files, exceptions, modules, object-oriented programming, intermediate Python, data structures and algorithms, databases, projects, and interview preparation. See [ROADMAP.md](ROADMAP.md) for the full sequence.

## Quality and accuracy

Examples should include expected output where useful and should be tested before being treated as verified. If an example has not been run in an environment, it should not be described as tested. The repository is a work in progress and will grow topic by topic.

## AI assistance disclosure

AI tools have assisted with organising notes, explaining concepts, suggesting practice problems, and reviewing code. I am responsible for reviewing, running, understanding, and improving the material before relying on it. This disclosure is intentional; AI assistance is not represented as unaided work.

## Contact and profile

- GitHub: [adilathif24](https://github.com/adilathif24)
- Repository: [Python-Learning](https://github.com/adilathif24/Python-Learning)

## Separate learning and interview tracks

- [Python Core Concepts — Beginner to Advanced](interview/Python-Core-Concepts.md) — definitions, explanations, real-world uses, tasks and interview Q&A for each core topic.
- [Python OOP — Beginner to Advanced](interview/Python-OOP-Interview-Guide.md) — classes, objects, encapsulation, inheritance, polymorphism, abstraction, composition and seven OOP coding interview examples.
- [DSA — Beginner to Advanced](interview/DSA-Roadmap-and-Interview-Guide.md) — complexity, arrays, strings, hashing, two pointers, sliding window, prefix sums, binary search, recursion, linked lists, stacks, queues, trees, heaps, graphs, greedy, DP and advanced structures.

**Study rule:** Keep Python fundamentals, OOP and DSA as separate tracks. For each topic, study the definition and explanation, understand the real-world use, complete examples and tasks, then answer interview questions without copying. These guides are learning material, not a claim that every topic is mastered or every code sample independently tested.

## Separate Learning Tracks — Beginner to Advanced

Study each track independently. The Python Core guide focuses on language fundamentals; OOP has its own concepts and interview questions; DSA focuses on data structures, algorithms, coding patterns and complexity.

- [Python Core Concepts — Beginner to Advanced](notes/Python-Core-Concepts-Beginner-to-Advanced.md) — variables, types, operators, input/output, conditions, loops, strings, lists, tuples, sets, dictionaries, functions, comprehensions, imports, exceptions, files, generators, decorators, type hints and testing. Each topic has definitions, explanations, real-world use, seven examples/Q&A and tasks.
- [Python OOP — Beginner to Advanced](oop/Python-OOP-Beginner-to-Advanced.md) — classes, objects, self, constructors, instance/class/static methods, encapsulation, properties, inheritance, overriding, MRO, polymorphism, duck typing, abstraction, composition, special methods, dataclasses and seven coding interview questions with answers.
- [DSA with Python — Beginner to Advanced](dsa/DSA-Python-Beginner-to-Advanced.md) — complexity, arrays/lists, strings, hashing, two pointers, sliding window, prefix sums, sorting, binary search, recursion, backtracking, linked lists, stacks, queues, trees, heaps, graphs, greedy, dynamic programming, tries, DSU, range-query structures and bit manipulation.
- [Python Interview Preparation](interview/Python-Interview-Preparation.md) — general Python interview concepts and coding practice.

### How to study
1. Learn Python core fundamentals first.
2. Study OOP as a separate track and build small class-based examples.
3. Study DSA topic by topic: understand the pattern, dry-run, implement, analyse complexity, then solve unseen variations.
4. For every topic, complete the examples, interview Q&A and tasks before moving on.
5. Run code locally and verify it; these guides are learning materials, not a substitute for independent practice.

## Separate learning tracks — recruiter-friendly

Study Python fundamentals, OOP and DSA independently so each skill is easy to navigate and review.

- [Python Core Concepts: Beginner to Advanced](core/Python-Core-Concepts-Beginner-to-Advanced.md) — variables, operators, conditions, loops, strings, lists, tuples, sets, dictionaries, functions, files, exceptions and advanced core concepts. Each topic includes a definition, use cases, seven solved examples and five practice answers.
- [Python OOP: Beginner to Advanced](oop/Python-OOP-Beginner-to-Advanced.md) — classes, objects, constructors, methods, encapsulation, inheritance, polymorphism, abstraction, composition and seven OOP coding interview examples.
- [DSA: Beginner to Advanced](dsa/DSA-Beginner-to-Advanced.md) — complexity, arrays, strings, hashing, two pointers, sliding windows, prefix sums, searching, recursion, linked lists, stacks, queues, trees, heaps, graphs, greedy, dynamic programming and advanced structures.
- [Python Interview Preparation](interview/Python-Interview-Preparation.md) — general Python interview questions, coding questions and project discussion.

### Recommended learning order
1. Python Core Concepts — complete examples and practice tasks.
2. OOP — implement each class and explain design choices.
3. DSA — learn one pattern at a time; dry-run and analyse complexity.
4. Projects — add tests, clear README instructions and examples of your own work.

### Contribution and accuracy note
These are learning notes and starter interview practice, not a claim that every topic is mastered. Run code, test edge cases, correct mistakes and solve new variations independently before listing a skill as interview-ready.


## Runnable code examples

Each learning track now has a Python file you can run locally. These files demonstrate the main concepts and common coding patterns; use them alongside the detailed Markdown guide.

- [Python Core runnable examples](core/examples.py) — variables, operators, loops, strings, collections, functions, exceptions, generators and more.
- [OOP runnable examples](oop/examples.py) — classes, constructors, methods, encapsulation, inheritance, polymorphism, abstraction, composition and dataclasses.
- [DSA runnable examples](dsa/examples.py) — searching, arrays, strings, hashing, two pointers, sliding window, prefix sums, recursion, stacks, queues/BFS, heaps, DP, greedy and bit manipulation.

### Run the examples

From the repository's root folder, use:

```bash
python core/examples.py
python oop/examples.py
python dsa/examples.py
```

If your system uses the Python 3 launcher, use `py` instead of `python`. Read each function, predict the output, run it, then change the inputs and test edge cases. The examples are starter implementations; verify them in your own environment before treating them as tested interview solutions.


## Full code + explanation + real-world guides

The detailed topic guides above provide complete code snippets, plain-English explanations, and practical use cases instead of only short example descriptions.

- [Python Core: topic-by-topic code, explanation and real-world use](core/Topic-by-Topic-Code-Explanation-Real-World.md)
- [Python OOP: complete examples with explanations and real-world use](oop/Topic-by-Topic-Code-Explanation-Real-World.md)
- [DSA: implementations, explanations, complexity and real-world use](dsa/Topic-by-Topic-Code-Explanation-Real-World.md)

For OOP, the Dog examples now show the full code for defining a class, creating an object, adding an attribute, using `__init__`, writing `speak()`, creating independent objects, and calling a bound method. The other tracks likewise contain code and explanations for their main topics. These are learning guides; run the code and test edge cases yourself before treating a solution as verified.
