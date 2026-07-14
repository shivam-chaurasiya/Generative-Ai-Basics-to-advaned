--------------------- IN THIS CHAPTER WE ARE WORKING ON THE PYDANTIC IN PYTHON -------------------------------

Pydantic: Pydantic is the most widely used data validation library for Python.

Why use Pydantic?: 
1. Powered by type hints: with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools.
2. Speed:  Pydantic’s core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python.
3.JSON Schema: Pydantic models can emit JSON Schema, allowing for easy integration with other tools.
4.Strict and Lax mode: Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate

# Concepts:

1. Models: One of the primary ways of defining schema in Pydantic is via models. Models are simply classes which inherit from BaseModel and define fields as annotated attributes.

2. 