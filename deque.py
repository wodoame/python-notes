# In Python, a `deque` (double-ended queue) is a data structure that allows you to efficiently append and pop elements from both ends of the queue.
# It's part of the `collections` module. Here's a tutorial on how to use `deque` in Python:

### 1. Import the `deque` class:

from collections import deque

### 2. Create a deque:
# You can create a deque by calling the `deque()` constructor. You can pass an iterable (e.g., a list) to initialize the deque with initial elements.

my_deque = deque([1, 2, 3, 4, 5])

### 3. Basic Operations:

#### 3.1 Append and Pop:

# Append to the right
my_deque.append(6)

# Append to the left
my_deque.appendleft(0)

# Pop from the right
popped_right = my_deque.pop()

# Pop from the left
popped_left = my_deque.popleft()

print(my_deque)  # Output: deque([0, 1, 2, 3, 4, 5])


#### 3.2 Access Elements:

# Access elements by index
first_element = my_deque[0]
last_element = my_deque[-1]

print(first_element, last_element)  # Output: 0 5


### 4. Rotating Elements:
# You can rotate the deque in either direction:

# Rotate to the right
my_deque.rotate(2)

# Rotate to the left
my_deque.rotate(-2)

print(my_deque)  # Output: deque([4, 5, 0, 1, 2, 3])


### 5. Other Operations:
#### 5.1 Length:

length = len(my_deque)
print(length)  # Output: 6

#### 5.2 Clear:

my_deque.clear()
print(my_deque)  # Output: deque([])


#### 5.3 Extend:

# Extend the deque with another iterable
my_deque.extend([6, 7, 8])
print(my_deque)  # Output: deque([6, 7, 8])


### 6. Performance:

# Deques are optimized for fast append and pop operations from both ends, making them suitable for use as a queue or a stack.

from collections import deque
import time

# Measure performance
start_time = time.time()
my_deque = deque()

for i in range(10**6):
    my_deque.append(i)

end_time = time.time()
print("Time taken to append 1 million elements:", end_time - start_time, "seconds")

# This is a basic overview of using `deque` in Python. Depending on your specific use case, you might discover additional methods and functionalities offered by
# the `deque` class in the [official documentation](https://docs.python.org/3/library/collections.html#collections.deque).
