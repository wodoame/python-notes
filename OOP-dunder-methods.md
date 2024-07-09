In Python, **dunder methods** (short for "double underscore" methods) allow instances of a class to interact with built-in functions and operators. These special methods start and end with two underscores (e.g., `__str__` or `__add__`). Here are some key dunder methods and their purposes:

1. **`__init__`**: The initializer (not to be confused with the constructor). It sets up the initial state of an object when it's created.
2. **`__repr__`**: Customizes an object's string representation. Useful for debugging and when working with the Python REPL.
3. **`__eq__`**: Customizes what it means for objects to be equal to one another. Typically returns a boolean value.
4. **`__ne__`**: Rarely implemented. Used for inequality checks (negates the result of `__eq__`).
5. **`__hash__`**: Determines the hash value of an object. Objects with custom `__eq__` methods need a custom `__hash__` method to be hashable (used as keys in dictionaries or values in sets).
6. **Comparison Operators**: Overloaded with dunder methods (`<`, `>`, `<=`, `>=`). These methods define the relative ordering of objects (e.g., for sorting).

Remember, magic methods are not meant to be invoked directly by you; Python handles their invocation internally based on specific actions. If you want more details or examples, feel free to explore the [complete list of dunder methods](https://www.pythonmorsels.com/every-dunder-method/).

```python
   class Employee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __repr__(self) -> str:
        return f'Employee(\'{self.name}\', {self.salary})'
    
    def __str__(self) -> str:
        return self.name
    
    # add the employees together: overloading the '+' operator
    def __add__(self, other):
        return self.salary + other.salary

    employee = Employee('bernard', 1000)
    employee2 = Employee('miriam', 3000)
    
    print(employee + employee2)
```
