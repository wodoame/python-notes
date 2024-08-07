Let's start with a simple example of a class that fetches data from an API without using dependency injection.

### Without Dependency Injection

```python
import requests

class ApiService:
    def fetch_data(self, url):
        response = requests.get(url)
        return response.json()

class DataProcessor:
    def __init__(self):
        self.api_service = ApiService()  # Direct dependency

    def process_data(self, url):
        data = self.api_service.fetch_data(url)
        # Process the data
        return data

# Usage
processor = DataProcessor()
data = processor.process_data('https://api.example.com/data')
print(data)
```

In this example, `DataProcessor` directly depends on `ApiService`, making it difficult to test and maintain.

### With Dependency Injection

Now, let's refactor the code to use dependency injection:

```python
import requests

class ApiService:
    def fetch_data(self, url):
        response = requests.get(url)
        return response.json()

class DataProcessor:
    def __init__(self, api_service):
        self.api_service = api_service  # Dependency is injected

    def process_data(self, url):
        data = self.api_service.fetch_data(url)
        # Process the data
        return data

# Usage
api_service = ApiService()
processor = DataProcessor(api_service)
data = processor.process_data('https://api.example.com/data')
print(data)
```

By injecting the `ApiService` dependency into `DataProcessor`, we make the code more flexible and easier to test. For example, you can now easily mock `ApiService` in your tests.
