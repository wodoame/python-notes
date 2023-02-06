# The "with" Keyword in Python

# The "with" keyword is used as a context manager in Python and is used to wrap the execution of a block of code.
# A context manager is an object that defines the methods __enter__ and __exit__. The "with" statement creates a context 
# in which the __enter__ method is executed before the code block is executed, and the __exit__ method is executed after
# the code block is executed, even if it raises an exception.

# Here is an example of using the "with" keyword to open and read a file:

with open("sample.txt", "r") as file:
    contents = file.read()
    print(contents)

# In this example, the "with" statement creates a context in which the file is opened and read. The "as" keyword assigns
# the file object to the variable "file". The "file.read()" method is executed within the context, and the contents of
# the file are assigned to the "contents" variable. After the code block is executed, the "__exit__" method is executed
# automatically, which closes the file and releases any resources it was using. This way, the programmer does not have to
# worry about manually closing the file, even if an exception is raised within the code block.
