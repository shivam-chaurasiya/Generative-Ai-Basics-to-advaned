--------Comprehensions-----------

Comprehensions: Comprehensions in Python are concise, single-line syntactic structures used to create new data collections from existing iterables. They provide a cleaner, more readable, and often faster alternative to traditional for loops.

Python supports four types of comprehensions: List, Dictionary, Set, and Generator expressions

Where are comprehensions are used in real life:
1. filter item
2. transform items
3. create a new collection
4. flatten nested structure.

what purpose they do serve:
1. Cleaner code
2. Faster execution


1. List Comprehensions: Creates a new list by applying an expression to each item in an iterable.
Syntax: [expression for item in iterable if condition]

2. Set Comprehension: Builds a new set, meaning it automatically eliminates duplicate values.

Syntax: {expression for item in iterable if condition}

3. Dictionary Comprehension: Constructs a new dictionary by dynamically generating key-value pairs.

Syntax: {key_expression : value_expression for item in iterable if condition}

4. Generator Comprehension: Looks similar to a list comprehension but uses parentheses. It produces items lazily (on demand) rather than loading the entire collection into memory at once, making it highly memory-efficient for massive datasets.

Syntax: (expression for item in iterable if condition)
