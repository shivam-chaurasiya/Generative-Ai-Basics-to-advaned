-------- IN THIS CHAPTER I AM WORKING ON OBJECT ORIENTED PROGRAMMING IN PYTHON -----------------

OOPS: Object Oriented Programming empowers developers to build modular, maintainable and scalable applications. OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior.

Class: A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.  

1.Classes are created by keyword class.
2.Attributes are the variables that belong to a class.
3.Attributes are always public and can be accessed using the dot (.) operator. Example- Myclass.Myattribute

Object: An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data

Attribute Shadowing: attribute shadowing occurs when an instance attribute is created with the exact same name as an existing class attribute.

Because Python searches the instance namespace (__dict__) before checking the class namespace, the new instance attribute hides (shadows) the class attribute during subsequent lookups on that specific instance.

self argument: self represents the specific instance of a class. It binds the attributes and methods of a class to a newly created object so that each object can maintain its own data independently.

self is a reference to all the parameter, all the properties that you are defined.

init method: __init__ is a special method used as an initializer (or constructor) that automatically runs whenever you create a new instance of a class.

Its primary purpose is to assign values to object properties (attributes) and perform any startup configuration the object needs

Inheritence: Inheritance is a core concept in Python's Object-Oriented Programming (OOP) that allows a new class (the child or derived class) to adopt all attributes and behaviors from an existing class (the parent or base class). 

Accessing base class: There are three ways to access the base class in python
1. Code dupliation 
2. Explicit call
3. super() method.

Method Resolution Order: Method Resolution Order (MRO) is the deterministic sequence Python follows to look up attributes and methods in an inheritance hierarchy. It ensures a predictable, linear path for method execution when dealing with complex class architectures, particularly when utilizing multiple inheritance.


static method: In Python, a static method is a function defined inside a class that does not require an instance or the class itself to be executed. It is created using the @staticmethod decorator and behaves exactly like a plain, isolated function, but lives inside the class's namespace for logical organization

classmethod: In Python, a classmethod is a method that is bound to the class itself rather than its individual object instances. It is defined using the @classmethod decorator and automatically receives the class as its first argument, which is conventionally named cls

-@classmethod is used to create a method that works with the class instead of an object instance. A class method receives the class itself as the first argument using cls. It is commonly used to access class variables, create factory methods and perform operations related to the class.