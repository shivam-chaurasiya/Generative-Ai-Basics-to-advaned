-----------------Generators --------------------------

Generators: Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). 

Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

For large datasets, generators save memory

The Yield Statement: The yield statement can be used to omit the parentheses that would otherwise be required in the equivalent yield expression statement.

A yield statement is semantically equivalent to a yield expression.

The yield keyword is what makes a function a generator.

When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.

Unlike return, which terminates the function, yield pauses it and can be called multiple times.

Using next() with Generators:
You can manually iterate through a generator using the next() function

Infinite Generator: An infinite generator in Python is a function that produces an endless sequence of values using a while True loop combined with the yield keyword. Because generators use lazy evaluation, they only compute and yield one item at a time on demand.

Built-in Infinite Iterators (itertools):
1. itertools.count(start, step)
2. itertools.cycle(iterable)
3. itertools.repeat(element)

Send Generator: The generator.send(value) method in Python resumes a suspended generator and injects a value back into it, making that value the result of the current yield expression.

Close Generator: In Python, you close a generator by calling its close() method.

Calling this method terminates the generator prematurely by raising a GeneratorExit exception at the point where the generator function was last paused.