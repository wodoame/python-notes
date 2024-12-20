In Python, the terms **module**, **package**, and **library** are related but distinct concepts. Here's a breakdown of their meanings and differences:

---

### 1. **Module**
A module is a single Python file containing Python code. It can include functions, classes, and variables, and it may also include runnable code.

- **How to Recognize**: A single `.py` file, e.g., `math.py`.
- **Purpose**: To group related functionality in one place for reuse.
- **Examples**:
  - Standard library modules: `math`, `os`, `sys`.
  - Custom modules: A file named `my_module.py` you create yourself.
- **Usage**:
  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
  ```

---

### 2. **Package**
A package is a collection of Python modules organized in a directory hierarchy. A package typically contains an `__init__.py` file (though this is optional in Python 3.3+). 

- **How to Recognize**: A directory containing a collection of `.py` files and often an `__init__.py` file.
- **Purpose**: To organize and distribute a set of related modules together.
- **Examples**:
  - Standard library packages: `collections`, `email`.
  - Third-party packages: `requests`, `numpy`.
- **Usage**:
  ```python
  from package_name import module_name
  ```

**Structure Example**:
```
mypackage/
    __init__.py       # Marks the directory as a package
    module1.py
    module2.py
```

Usage:
```python
from mypackage import module1
module1.some_function()
```

---

### 3. **Library**
A library is a broader term that refers to a collection of modules or packages bundled together to provide reusable functionality. Libraries often include a wide range of features and may depend on multiple modules or packages.

- **How to Recognize**: A collection of modules/packages distributed via PyPI or other repositories.
- **Purpose**: To provide a reusable toolset for specific tasks or domains.
- **Examples**:
  - Standard library: A built-in set of modules and packages (e.g., `math`, `os`, `datetime`).
  - Third-party libraries: `requests` (HTTP library), `pandas` (data analysis library).

**Usage**:
```python
import requests
response = requests.get("https://example.com")
print(response.text)
```

---

### Key Differences

| Feature        | Module                        | Package                        | Library                          |
|----------------|-------------------------------|--------------------------------|----------------------------------|
| **Definition** | A single Python file.         | A directory of related modules.| A collection of modules/packages.|
| **File**       | `.py` file.                   | Folder with modules/files.     | Can be a package or set of packages.|
| **Purpose**    | Organizes reusable code.      | Groups related modules.        | Provides functionality/toolset. |
| **Scope**      | Narrow, focused functionality.| Broader organization.          | Comprehensive, task-oriented.   |

---

### Real-World Examples

| Type      | Example             | Description                                        |
|-----------|---------------------|----------------------------------------------------|
| Module    | `math`              | A single file providing mathematical functions.    |
| Package   | `numpy`             | A package with many modules for numerical computing.|
| Library   | `scikit-learn`      | A library with multiple modules for machine learning.|

---

### Summary
- A **module** is the basic building block—a single Python file.
- A **package** is a way to organize related modules into a directory structure.
- A **library** is a collection of modules/packages providing reusable functionality.
