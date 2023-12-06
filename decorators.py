# In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods without changing their actual code.
# Decorators are functions themselves, and they are applied to other functions or methods using the `@decorator` syntax.

# Here's a basic overview of how decorators work in Python:

### 1. Function Basics:
# In Python, functions are first-class citizens, meaning they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.


def simple_function():
    print("This is a simple function.")

# Assigning a function to a variable
my_function = simple_function

# Calling the function through the variable
my_function()  # Output: This is a simple function.


### 2. Decorators:
# A decorator is a function that takes another function as an argument and extends or modifies the behavior of that function. Decorators use the `@decorator` syntax to apply them to a function.


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Note that this is equivalent to doing 
say_hello = my_decorator(say_hello)
# So the decorator function takes the original function as an argument and returns a modified function which has the same name as the original function
# Because of this when you call the function it has some modified behaviour

# Using the decorated function
say_hello()


# In this example, `my_decorator` is a decorator that wraps the `say_hello` function. When `say_hello` is called, it is replaced by the `wrapper` function defined inside the decorator.
# This allows additional functionality to be executed before and after the original function.

### 3. Multiple Decorators:

# You can apply multiple decorators to a single function by stacking them using the `@decorator1` and `@decorator2` syntax.


def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Original function")

# Calling the decorated function
my_function()


# In this example, `my_function` is first wrapped by `decorator2` and then by `decorator1`. 
# The order of stacking decorators matters.

### 4. Decorators with Arguments:
# You can create decorators that accept arguments by introducing an additional layer of functions.


def parametrized_decorator(param):
    def actual_decorator(func):
        def wrapper():
            print(f"Decorator with parameter: {param}")
            func()
        return wrapper
    return actual_decorator

@parametrized_decorator("Custom Parameter")
def my_function():
    print("Original function")

# Calling the decorated function
my_function()


# In this case, `parametrized_decorator` takes a parameter and returns the actual decorator, which, in turn, wraps the original function.
# This is some code I wrote. The original factorial function can be modified to take multiple numbers. If it takes just one number it functions normally but if you pass in mutliple numbers it returns 
# A list of the results. I achieve this using the extended decorator
import math 

def extended(func): 
    def modified(*args):
        return func(args[0]) if len(args) == 1 else [func(n) for n in args]
    return modified


@extended
def factorial(n):
    return math.factorial(n)



print(factorial(5, 6, 7, 8)) # Ouput: [120, 720, 5040, 40320]

# Decorators are a powerful tool in Python, often used for tasks such as logging, access control, memoization, and more.
# They provide a clean and elegant way to extend the behavior of functions or methods.
