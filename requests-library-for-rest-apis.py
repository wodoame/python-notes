# The `requests` library is a popular and powerful library in Python for making HTTP requests.
# It provides a simple and elegant way to interact with RESTful APIs or fetch web pages.
# Here's a basic tutorial on how to use the `requests` library:

### Installing Requests
# Before you start using the `requests` library, you need to install it. You can do this using `pip`:

# pip install requests

### Making a Simple GET Request

# Now, let's start with a simple GET request. We'll use the JSONPlaceholder API for demonstration purposes:

import requests

# Specify the URL for the GET request
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make the GET request
response = requests.get(url)

# Check the status code and print the response content
if response.status_code == 200:
    print("Request was successful!")
    print(response.json())  # Assuming the response is in JSON format
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes

### Adding Headers to a Request

# If your API requires headers, you can include them in the request using the `headers` parameter:
import requests

url = "https://api.example.com/data"
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'User-Agent': 'Your User Agent',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Request was successful!")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
  
### Making a POST Request

# If you need to send data to a server, you can use a POST request. Here's an example:
import requests

url = "https://api.example.com/post-endpoint"
headers = {
    'Content-Type': 'application/json',
}
data = {
    'key1': 'value1',
    'key2': 'value2',
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:  # Assuming the server responds with 201 for a successful creation
    print("POST request was successful!")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
  
### Handling Errors

# It's essential to handle errors gracefully.
# You can use `response.raise_for_status()` to raise an exception for bad responses (4xx and 5xx status codes):

import requests

url = "https://api.example.com/data"
response = requests.get(url)

try:
    response.raise_for_status()
    print("Request was successful!")
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")

### Session Objects

# If you need to persist certain parameters across requests, you can use a `Session` object:
import requests

url = "https://api.example.com"
headers = {'User-Agent': 'Your User Agent'}

# Create a session
session = requests.Session()
session.headers.update(headers)

# Make requests using the session
response1 = session.get(url + "/endpoint1")
response2 = session.get(url + "/endpoint2")

print(response1.text)
print(response2.text)

# Don't forget to close the session when done
session.close()


# This tutorial covers the basics of using the `requests` library for making HTTP requests in Python.
# For more advanced features and options, refer to the official documentation: [Requests Documentation](https://docs.python-requests.org/en/master/).

