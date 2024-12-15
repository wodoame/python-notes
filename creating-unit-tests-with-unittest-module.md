The `unittest` module in Python provides a built-in framework for writing and running tests. Here's a step-by-step guide to using it:

---

### **1. Write Your Tests**
Create a Python script with test cases. Each test case is a method in a class that inherits from `unittest.TestCase`.

#### Example Test File: `test_example.py`
```python
import unittest

# Code to test
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Test cases
class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test if add works correctly
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)


if __name__ == "__main__":
    unittest.main()
```

---

### **2. Run the Tests**

#### **Option 1: Run Tests from the Command Line**
Save the above file as `test_example.py` and run it:
```bash
python test_example.py
```

Output:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
Here:
- `..` means two tests passed.
- `OK` indicates all tests succeeded.

#### **Option 2: Discover and Run All Tests**
You can let `unittest` automatically discover and run all test files in a directory. Test files must match the pattern `test*.py` by default.

From the command line, run:
```bash
python -m unittest discover
```

By default, it searches in the current directory and runs all test files.

You can specify options:
```bash
python -m unittest discover -s tests -p "test_*.py"
```
- `-s`: The start directory (e.g., `tests`).
- `-p`: The pattern for test files (e.g., `test_*.py`).

---

### **3. Run Tests Programmatically**
You can also run tests from a Python script using `unittest`'s `TestLoader` and `TextTestRunner`.

#### Example: Run Tests Programmatically
```python
import unittest

# Load test cases from a module
loader = unittest.TestLoader()
suite = loader.discover('.')

# Run tests
runner = unittest.TextTestRunner()
runner.run(suite)
```

---

### **4. Test Assertions**
`unittest` provides many assertion methods to validate test results:

| **Method**                     | **Description**                                           |
|--------------------------------|-----------------------------------------------------------|
| `assertEqual(a, b)`            | Check `a == b`.                                           |
| `assertNotEqual(a, b)`         | Check `a != b`.                                           |
| `assertTrue(x)`                | Check `x` is `True`.                                      |
| `assertFalse(x)`               | Check `x` is `False`.                                     |
| `assertIs(a, b)`               | Check `a is b`.                                           |
| `assertIsNot(a, b)`            | Check `a is not b`.                                       |
| `assertIn(a, b)`               | Check `a in b`.                                           |
| `assertNotIn(a, b)`            | Check `a not in b`.                                       |
| `assertRaises(exc, func, *args)` | Check if `func(*args)` raises exception `exc`.            |

#### Example of Assertions
```python
class TestAssertions(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2 + 2, 4)

    def test_raises(self):
        with self.assertRaises(ValueError):
            int("invalid")  # This raises a ValueError
```

---

### **5. Structure Your Tests**

For larger projects, organize your tests in a dedicated directory, e.g., `tests/`:
```
project/
│
├── mymodule.py
├── tests/
│   ├── test_mymodule.py
│   └── test_othermodule.py
```

Run all tests from the `tests` directory:
```bash
python -m unittest discover -s tests
```

---

### **6. Verbose Output**
For more detailed output, use the `-v` flag:
```bash
python -m unittest -v
```

Output:
```
test_add (test_example.TestMathOperations) ... ok
test_subtract (test_example.TestMathOperations) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

---

### **7. Mocking (Optional)**
Use `unittest.mock` to test functions that depend on external systems (e.g., databases or APIs).

#### Example: Mocking
```python
from unittest.mock import patch

def get_data():
    # Simulate fetching data from an API
    raise RuntimeError("Network error")

class TestWithMock(unittest.TestCase):
    @patch('__main__.get_data', return_value="mocked data")
    def test_get_data(self, mock_get_data):
        self.assertEqual(get_data(), "mocked data")
```

---

With this guide, you should be able to write, organize, and execute tests effectively using the `unittest` module.
