class Person:
    # The constructor sets the initial value of the instance variable "name"
    def __init__(self, name):
        self._name = name
        
    # Getter method to get the value of "name"
    @property
    def name(self):
        return self._name
    
    # Setter method to set the value of "name"
    @name.setter
    def name(self, value):
        self._name = value

person = Person("John")
print(person.name) # Output: John
person.name = "Jane"
print(person.name) # Output: Jane

# The Person class has an instance variable "_name" which is initialized in the constructor.
# The getter and setter methods allow us to get and set the value of "_name" respectively.
# The "property" decorator is used to create a getter method, and the setter is defined by using the same name 
# and adding a ".setter" decorator. These methods are then accessed as properties on the instance of the class, 
# just like any other property.
