The Strategy Pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable. This pattern enables the algorithm to be selected at runtime, providing flexibility and promoting code reusability¹².

### Example in Python

Let's create an example to illustrate the Strategy Pattern. We'll design a system for calculating different types of discounts.

#### Step 1: Define the Strategy Interface

First, we'll define an interface for the strategy.

```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass
```

#### Step 2: Implement Concrete Strategies

Next, we'll implement concrete strategies for different types of discounts.

```python
class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        return price - self.amount
```

#### Step 3: Define the Context

The context class will use a discount strategy to calculate the final price.

```python
class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def total_price(self):
        total = sum(price for item, price in self.items)
        return self.discount_strategy.apply_discount(total)
```

#### Step 4: Use the Strategy

Finally, we'll use the strategy to calculate the total price with different discount strategies.

```python
def main():
    cart = ShoppingCart(NoDiscount())
    cart.add_item("Item 1", 100)
    cart.add_item("Item 2", 200)
    print(f"Total price without discount: {cart.total_price()}")  # Output: 300

    cart = ShoppingCart(PercentageDiscount(10))
    cart.add_item("Item 1", 100)
    cart.add_item("Item 2", 200)
    print(f"Total price with 10% discount: {cart.total_price()}")  # Output: 270

    cart = ShoppingCart(FixedAmountDiscount(50))
    cart.add_item("Item 1", 100)
    cart.add_item("Item 2", 200)
    print(f"Total price with $50 discount: {cart.total_price()}")  # Output: 250

if __name__ == "__main__":
    main()
```

### Explanation

1. **Strategy Interface**: `DiscountStrategy` defines the interface for discount strategies.
2. **Concrete Strategies**: `NoDiscount`, `PercentageDiscount`, and `FixedAmountDiscount` implement the `DiscountStrategy` interface.
3. **Context**: `ShoppingCart` uses a discount strategy to calculate the total price.
4. **Usage**: The `main` function demonstrates how to use different discount strategies.

This pattern helps in decoupling the algorithm from the context, making the code more flexible and easier to maintain.
