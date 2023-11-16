'''
    The Decorator design pattern is a structural pattern that allows behavior
    to be added to an individual object, either statically or dynamically, 
    without affecting the behavior of other objects from the same class. 
    It is commonly used to extend or enhance the behavior of classes in a flexible and reusable way.
'''

from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    """The Component interface that declares the method 'cost'."""
    @abstractmethod
    def cost(self):
        '''
            The Component interface declares operations that can be altered by
        '''

# Concrete Component
class SimpleCoffee(Coffee):
    """A Concrete Component that implements the 'Coffee' interface."""
    def cost(self):
        """Return the cost of a simple coffee."""
        return 5

# Decorator Base Class
class CoffeeDecorator(Coffee):
    """The base class for Decorators, extending the 'Coffee' interface."""
    def __init__(self, coffee):
        """Initialize the decorator with a reference to the decorated coffee."""
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    """A Concrete Decorator adding the cost of milk."""
    def cost(self):
        """Return the cost of the decorated coffee with added milk."""
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    """A Concrete Decorator adding the cost of sugar."""
    def cost(self):
        """Return the cost of the decorated coffee with added sugar."""
        return self._coffee.cost() + 1

# Client Code
if __name__ == "__main__":
    # Create a simple coffee
    my_coffee = SimpleCoffee()
    print("Cost of Simple Coffee:", my_coffee.cost())

    # Decorate the coffee with milk
    milk_coffee = MilkDecorator(my_coffee)
    print("Cost of Milk Coffee:", milk_coffee.cost())

    # Decorate the coffee with sugar
    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print("Cost of Sugar Milk Coffee:", sugar_milk_coffee.cost())
