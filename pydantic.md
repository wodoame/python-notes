### Tutorial: Using Pydantic in Python

Pydantic is a Python library that provides data validation and settings management using Python type annotations. It is widely used for parsing and validating data, especially in APIs, configuration management, and data serialization/deserialization.

In this tutorial, we'll cover the basics of Pydantic, including:

1. **Installing Pydantic**
2. **Creating a Pydantic Model**
3. **Validating Data**
4. **Using Default Values**
5. **Nested Models**
6. **Custom Validators**
7. **Serializing and Deserializing Data**
8. **Using Pydantic with APIs**

---

### 1. Installing Pydantic

First, you need to install Pydantic. You can do this using `pip`:

```bash
pip install pydantic
```

---

### 2. Creating a Pydantic Model

Pydantic models are created by subclassing `BaseModel` and defining fields using type annotations.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True  # Default value
```

Here, we've defined a `User` model with four fields: `id`, `name`, `age`, and `is_active`. The `is_active` field has a default value of `True`.

---

### 3. Validating Data

Pydantic automatically validates data when you create an instance of a model. If the data doesn't match the expected types, Pydantic will raise a `ValidationError`.

```python
# Valid data
user = User(id=1, name="John Doe", age=30)
print(user)

# Invalid data (will raise ValidationError)
try:
    user = User(id="one", name="John Doe", age=30)
except Exception as e:
    print(e)
```

---

### 4. Using Default Values

If a field has a default value, you can omit it when creating an instance of the model.

```python
user = User(id=1, name="Jane Doe", age=25)
print(user)  # is_active will be True by default
```

---

### 5. Nested Models

Pydantic supports nested models, allowing you to define complex data structures.

```python
class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    age: int
    address: Address

# Creating an instance with a nested model
address = Address(street="123 Main St", city="Springfield", zipcode="12345")
user = UserWithAddress(id=1, name="John Doe", age=30, address=address)
print(user)
```

---

### 6. Custom Validators

You can define custom validation logic using the `@validator` decorator.

```python
from pydantic import validator

class User(BaseModel):
    id: int
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, value):
        if value < 0:
            raise ValueError('Age must be a positive number')
        return value

# Valid data
user = User(id=1, name="John Doe", age=30)

# Invalid data (will raise ValidationError)
try:
    user = User(id=1, name="John Doe", age=-5)
except Exception as e:
    print(e)
```

---

### 7. Serializing and Deserializing Data

Pydantic models can easily be converted to and from dictionaries and JSON.

```python
# Convert model to dictionary
user_dict = user.dict()
print(user_dict)

# Convert model to JSON
user_json = user.json()
print(user_json)

# Convert dictionary to model
user_from_dict = User(**user_dict)
print(user_from_dict)

# Convert JSON to model
user_from_json = User.parse_raw(user_json)
print(user_from_json)
```

---

### 8. Using Pydantic with APIs

Pydantic is commonly used with web frameworks like FastAPI to validate request and response data.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

# Run the FastAPI app
# uvicorn script_name:app --reload
```

In this example, the `Item` model is used to validate the JSON payload of a POST request.

---

### Conclusion

Pydantic is a powerful tool for data validation and settings management in Python. It integrates well with other libraries and frameworks, making it a popular choice for developers working with APIs, configuration, and data processing.

By following this tutorial, you should now have a good understanding of how to use Pydantic in your Python projects. For more advanced features, check out the [Pydantic documentation](https://pydantic-docs.helpmanual.io/).
