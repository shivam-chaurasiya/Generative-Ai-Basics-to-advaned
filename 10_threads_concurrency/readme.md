-------- In this chapter we are working Threading, concurrency and parallelism ---------------------

Threading: Threading in Python allows your program to run multiple operations concurrently within a single process by sharing the same memory space. It is highly efficient for I/O-bound tasks (e.g., web scraping, API calls, and file operations) where the program spends most of its time waiting for external resources.

Concurrency: concurrency is about dealing with many things at once by interleaving tasks

--In Python, concurrency can be achieved using the threading module, which provides a way to create and manage threads. A thread is a separate execution flow within a program and can be used to run tasks concurrently with the main program.

--Asyncio and Threading are the type of concurrency.

Parallelism: parallelism is about doing many things at once by executing tasks simultaneously across multiple CPU cores.

--multiprocessing is a type of parallelism

multiprocessing is a module in Python that provides tools to write concurrent, parallel programs. The module allows you to write parallel programs that take advantage of multiple CPU cores in your system. This makes it possible to write fast, efficient programs that can perform multiple tasks at the same time.

--The main component of the multiprocessing module is the Process class. The Process class is used to create new processes in your Python program. Each process created with the Process class runs as a separate entity and has its own memory space, making it possible to run multiple processes in parallel.

GIL(Global Interpreter Lock): it is a mutex (mutual exclusion lock) in the default CPython implementation that allows only one thread to execute Python bytecode at a time

Why Python Uses the GIL: Guido van Rossum added the GIL early in Python's history for three main reasons:

1.Memory Management
2.Simplicity
3.Single-Thread Speed

How to Bypass the GIL: Use Multiprocessing, Use C-Extensions & Libraries, Alternative Interpreters.