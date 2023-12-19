# The `del` statement in Python is used to delete objects, elements, or even slices from various data structures.
# Let's go through a tutorial on using the `del` operator in different scenarios:

### Deleting Variables:

# Define a variable
x = 10

# Delete the variable
del x

# Trying to access x after deletion will result in an error
# print(x)  # Uncommenting this line will result in a NameError


### Deleting Elements from Lists:

# Define a list
my_list = [1, 2, 3, 4, 5]

# Delete the element at index 2
del my_list[2]

# The list is now [1, 2, 4, 5]
print(my_list)


### Deleting Slices from Lists:


# Define a list
my_list = [1, 2, 3, 4, 5]

# Delete a slice from index 1 to 3 (exclusive)
del my_list[1:3]

# The list is now [1, 4, 5]
print(my_list)


### Deleting Elements from a Dictionary:


# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Delete the key 'b' and its corresponding value
del my_dict['b']

# The dictionary is now {'a': 1, 'c': 3}
print(my_dict)


### Deleting Items from a Set:


# Define a set
my_set = {1, 2, 3, 4, 5}

# Delete the element 3
my_set.discard(3)

# The set is now {1, 2, 4, 5}
print(my_set)


### Deleting Attributes from Objects:


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create an instance of MyClass
obj = MyClass(10, 20)

# Delete the attribute 'x' from the object
del obj.x

# Trying to access obj.x after deletion will result in an AttributeError
# print(obj.x)  # Uncommenting this line will result in an AttributeError


### Deleting Items from a Tuple (Note: Tuples are immutable, so you can't directly delete elements from them):


# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a list, delete an element, and convert it back to a tuple
my_list = list(my_tuple)
del my_list[2]
my_tuple = tuple(my_list)

# The tuple is now (1, 2, 4, 5)
print(my_tuple)


Remember that while `del` removes references to objects, it does not necessarily free up memory immediately. Python's garbage collector will reclaim memory as needed. Also, be cautious when using `del` as it can lead to unexpected behavior if not used carefully.
