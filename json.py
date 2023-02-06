import json

# To encode a Python object into a JSON formatted string
def python_to_json(python_obj):
    return json.dumps(python_obj)

# To decode a JSON formatted string into a Python object
def json_to_python(json_str):
    return json.loads(json_str)

# Example usage:

# Python object
python_obj = {
    "name": "John Doe",
    "age": 35,
    "city": "New York"
}

# Encode the Python object into a JSON formatted string
json_str = python_to_json(python_obj)
print(json_str)
# Output: {"name": "John Doe", "age": 35, "city": "New York"}

# Decode the JSON formatted string into a Python object
python_obj = json_to_python(json_str)
print(python_obj)
# Output: {'name': 'John Doe', 'age': 35, 'city': 'New York'}
