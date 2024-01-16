# The `collections` module in Python provides several specialized and efficient data structures beyond `deque`.
# Here are some of the other notable classes and functionalities available in the `collections` module:

# 1. **Counter:**
   # - The `Counter` class is used to count the occurrences of elements in a collection (usually a list or a string).

   
   from collections import Counter

   my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
   counter = Counter(my_list)

   print(counter)  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})
   

# 2. **NamedTuple:**
#    - `namedtuple` is a factory function for creating tuple subclasses with named fields, improving code readability.

   
   from collections import namedtuple

   Point = namedtuple('Point', ['x', 'y'])
   p = Point(1, 2)

   print(p.x, p.y)  # Output: 1 2
   

# 3. **OrderedDict:**
#    - `OrderedDict` is a dictionary subclass that maintains the order in which items were inserted.

   
   from collections import OrderedDict

   my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

   for key, value in my_dict.items():
       print(key, value)
   

# 4. **defaultdict:**
#    - `defaultdict` is a dictionary subclass that provides a default value for a nonexistent key.

   
   from collections import defaultdict

   # Default value for a nonexistent key is set to int() which is 0
   my_dict = defaultdict(int)

   my_dict['a'] += 1
   my_dict['b'] += 2

   print(my_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
   

# 5. **ChainMap:**
#    - `ChainMap` is used to combine multiple dictionaries into a single mapping.

   
   from collections import ChainMap

   dict1 = {'a': 1, 'b': 2}
   dict2 = {'c': 3, 'd': 4}

   combined_dict = ChainMap(dict1, dict2)

   print(combined_dict['a'], combined_dict['c'])  # Output: 1 3
   

# 6. **deque (double-ended queue):**
#    - As mentioned earlier, `deque` provides a fast and memory-efficient list-like container with fast appends and pops from both ends.

   
   from collections import deque

   my_deque = deque([1, 2, 3, 4, 5])
   

# These are just a few examples of the functionalities provided by the `collections` module.
# Depending on your needs, you might find other classes and functions in the module that can simplify and enhance your code.
# For more details, refer to the [official documentation](https://docs.python.org/3/library/collections.html).
