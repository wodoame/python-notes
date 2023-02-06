# Methods that can be used on File Objects in Python

# File objects in Python are used to manipulate files on a file system. When a file is opened using the built-in "open"
# function, a file object is returned that can be used to read from or write to the file. The file object has several
# methods that can be used to perform various operations on the file.

# Here are some commonly used methods on file objects in Python:

# 1. read() - reads the entire contents of the file and returns it as a string
# 2. readline() - reads the next line from the file and returns it as a string
# 3. readlines() - reads all the lines from the file and returns them as a list of strings
# 4. write(string) - writes the string to the file
# 5. writelines(list) - writes the elements of the list to the file, with each element being a separate line
# 6. seek(offset, [from]) - moves the file pointer to a new position, where "offset" is the number of bytes to move the
#     pointer, and "from" is an optional argument that specifies the reference point for the offset (default is 0, which
#     means the beginning of the file)
# 7. tell() - returns the current position of the file pointer
# 8. close() - closes the file and releases any resources it was using

# Here is an example that demonstrates the use of some of these methods:

with open("sample.txt", "r") as file:
    print("First line:", file.readline())
    file.seek(0)
    contents = file.readlines()
    print("All lines:", contents)

# In this example, the file is opened in read mode using the "with" statement. The "readline()" method is used to read
# the first line of the file, and the "seek(0)" method is used to move the file pointer back to the beginning of the file.
# The "readlines()" method is then used to read all the lines of the file and store them in a list. The contents of the
# list are then printed to the console.


# Examples for Methods on File Objects in Python

# 1. read()
with open("sample.txt", "r") as file:
    contents = file.read()
    print("Contents of the file:")
    print(contents)

# 2. readline()
with open("sample.txt", "r") as file:
    print("First line of the file:", file.readline())

# 3. readlines()
with open("sample.txt", "r") as file:
    contents = file.readlines()
    print("Lines of the file:")
    print(contents)

# 4. write(string)
with open("output.txt", "w") as file:
    file.write("This is a sample file.")

# 5. writelines(list)
with open("output.txt", "w") as file:
    lines = ["Line 1", "Line 2", "Line 3"]
    file.writelines(lines)

# 6. seek(offset, [from])
with open("sample.txt", "r") as file:
    print("Current position of the file pointer:", file.tell())
    file.seek(10)
    print("New position of the file pointer:", file.tell())

# 7. tell()
with open("sample.txt", "r") as file:
    print("Current position of the file pointer:", file.tell())
    file.readline()
    print("New position of the file pointer:", file.tell())

# 8. close()
file = open("sample.txt", "r")
print("File is open:", file.closed)
file.close()
print("File is open:", file.closed)
