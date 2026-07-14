-----------In this chapter we are working on Asyncio in Python -----------------------------------

Asyncio: asyncio is a library to write concurrent code using the async/await syntax.

-asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

-asyncio is often a perfect fit for IO-bound and high-level structured network code.

Async def: declare a coroutine(special funtion that can be paused)

await: pauses the execution untill the result is ready

Event loop: The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

Coroutine: In Python, a coroutine is a specialized function that can pause its execution and resume it later.

Awaitables: We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.

There are three main types of awaitable objects: coroutines, Tasks, and Futures.

Tasks: Tasks are used to schedule coroutines concurrently.

# When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:

ThreadPoolExecutor: ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.

# Deadlocks can occur when the callable associated with a Future waits on the results of another Future.

Daemon thread: A boolean value indicating whether this thread is a daemon thread (True) or not (False). This must be set before start() is called, otherwise RuntimeError is raised.

# Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.

