from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function run")
        func()
        print("after the func run")
    return wrapper
    
@my_decorator
def greet():
    print("Hello from decorator class from Shivam")

greet()
print(greet.__name__)