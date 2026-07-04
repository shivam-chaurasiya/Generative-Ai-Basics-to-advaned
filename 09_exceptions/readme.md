-------------------In this we are discussing on the topic Errors and Exceptions -----------------------

1. Syntax Error: Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

2. Exceptions: Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions.

--Most exceptions are not handled by programs, however, and result in error messages 

3. Handling Exceptions: It is possible to write programs that handle selected exceptions.

The try statement works as follows.

--First, the try clause (the statement(s) between the try and except keywords) is executed.

--If no exception occurs, the except clause is skipped and execution of the try statement is finished.

--If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

--If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with an error message.

4. Raising Exceptions: The raise statement allows the programmer to force a specified exception to occur.

5. Finally Clause: If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception.

6. Try.. Except with else clause: The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception.

The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.