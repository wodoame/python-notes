# In Python, functions are defined using the "def" keyword. 
# Functions allow you to reuse code, making it easier to write and maintain large programs.

# The basic syntax for defining a function is as follows:

def function_name(arguments):
    # code to be executed
    return value

# Where:
# - function_name is the name of the function (should be descriptive and lowercase, with words separated by underscores)
# - arguments are the inputs to the function (can be zero or more)
# - code to be executed is the block of code that performs some operation (can be zero or more lines)
# - return value is the value that is returned to the caller (optional)

# Here's an example of a simple function that takes two arguments and returns their sum:

def add(a, b):
    result = a + b
    return result

# To call a function, simply use its name followed by arguments in parentheses:

sum = add(3, 4)
print(sum) # 7

# Functions can also return multiple values:

def multiply_and_divide(a, b):
    product = a * b
    quotient = a / b
    return product, quotient

result = multiply_and_divide(10, 5)
print(result) # (50, 2.0)

# Note that Python has many built-in functions, such as print(), len(), etc.
# You can also import functions from libraries and modules, and create your own custom libraries.
