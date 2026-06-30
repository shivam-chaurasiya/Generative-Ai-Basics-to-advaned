---- IN THIS CHAPTER WE ARE WORKING ON THE TOPIC WHICH NAMED AS FUNCTION ----

FUNCTIONS: A function in Python is a reusable block of organized code used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusability.

ADVANTAGES OF FUNCTION: 
1. CODE REUSABILITY
2. TRACEABILITY
3. MODULARITY
4. READABILITY
5. MAINTAINABILITY

NOTE: To define a function, use the def keyword, followed by the function name, parentheses (), and a colon :. The code block inside the function must be indented.

DEF keyword : 


SCOPE OF VARIABLES IN PYTHON: 

THE LEGB HIERARCHY: L-local, E- Enclosing, G- Global,   B - Built-in

Local Scope: A variable created inside a function belongs exclusively to that function's local namespace

Enclosing Scope : This applies to nested functions. The inner function can read variables belonging to the outer function

Global Scope: Global variables are declared outside of all functions. Any function can read them, but modifying them requires specific keywords.

----Scope Modification Keywords-----

global Keyword: Allows you to modify a variable at the module/top level from inside a function.

nonlocal Keyword: Used inside nested functions to modify a variable belonging to the immediate outer enclosing function.

-----Handling Arguments in Python----------

In Python, we can handle arguments in two different contexts,1. handling command-line arguments passed to a script, and 2.handling function arguments passed within your code

Handling Function Arguments: When designing functions, Python gives you intense control over how parameters are declared and passed.

Positional vs. Keyword Arguments:

1.Positional: Arguments map directly to parameters based on the order you pass them.

2.Keyword: Arguments are matched explicitly by name, freeing you from ordering constraints.

1.*args: Collects an arbitrary number of extra positional arguments into a tuple.
2.**kwargs: Collects an arbitrary number of extra keyword arguments into a dictionary.

pure and impure functions in python:
1.Pure Fuctions: A function is considered pure if it meets two strict criteria-
-Deterministic: It always returns the same output when given the exact same input.
-No Side Effects: It does not modify variables outside its scope, change mutable inputs, or perform any I/O operations (like printing or writing files).

Impure Functions: A function is impure if it violates either of the rules above. It may produce different results for the same inputs or cause a change in the application state.

Lambda Function: A lambda function in Python is a small, anonymous function that is defined without a name and contains exactly one expression

You use them for short-lived, throwaway logic where a full function definition using def would be overkill

Syntax: lambda arguments: expression

lambda keyword: Signals the creation of an anonymous function.
arguments: Comma-separated inputs (can be zero, one, or multiple).
expression: A single line of code evaluated and automatically returned (no return keyword allowed)
