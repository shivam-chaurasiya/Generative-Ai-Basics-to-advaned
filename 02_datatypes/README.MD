---------   IN THIS CHAPTER WE ARE WORKING ON DATA TYPES IN PYTHON PROGRAMMING ---------

BEFORE STARTING THE DATA TYPES WE NEED TO DISCUSS ABOUT MUTABLE AND IMMUTABLE OBJECT IN PYTHON
  
MUTABLE OBJECTS - # mutable objects can change their internal state or values after creation.and in this mutable object id are not always changed when we add some extra object to the particular list, set etc e.g list, dict, set
IMMUTABLE OBJECTS - #  immutable objects cannot be modified and will instead create a brand-new object in memory when you attempt to change them. that's whyid of the object always changed e.g. int, float, str, tuple


DATA TYPES IN PYTHON 

1. NUMBERS: # INTEGER, BOOLEAN, REAL, COMPLEX NUMBER

* the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be used for grouping
* Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %

*it is possible to use the ** operator to calculate powers

STRINGS:

* Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one

* Indices may also be negative numbers, to start counting from the right
* negative indices start from -1


chapter-4 # Tuples and membership testing

Tuples: # Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples).

chapter-5 # List

List: #list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

* Like strings, lists can be indexed and sliced
* Lists also support operations like concatenation
* lists are a mutable type, i.e. it is possible to change their content
* You can also add new items at the end of the list, by using the list.append() method

Chapter-6 # sets and frozensets in python

Set: #A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

* Curly braces or the set() function can be used to create sets. to create an empty set you have to use set(), not {}

chapter-7 Dictionary

Dictionary: dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.

* Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys
* dictionary as a set of key value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary {}

* Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

