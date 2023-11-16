'''
    The Abstract Factory pattern is another creational design pattern that provides an interface
    for creating families of related or dependent objects without specifying their concrete classes.
    This pattern involves multiple interfaces, each representing a family of related products.
'''
from abc import ABC, abstractmethod

# Abstract Product Interfaces
class Animal(ABC):
    """Abstract product interface for different types of animals."""
    @abstractmethod
    def speak(self):
        '''Speak method'''

class Habitat(ABC):
    """Abstract product interface for different types of habitats."""
    @abstractmethod
    def description(self):
        '''Description method'''

# Concrete Product Classes
class Dog(Animal):
    """Concrete product representing a Dog."""
    def speak(self):
        """Return the sound a dog makes."""
        return "Woof!"

class Cat(Animal):
    """Concrete product representing a Cat."""
    def speak(self):
        """Return the sound a cat makes."""
        return "Meow!"

class Forest(Habitat):
    """Concrete product representing a Forest habitat."""
    def description(self):
        """Return a description of the forest habitat."""
        return "A forest habitat."

class House(Habitat):
    """Concrete product representing a House habitat."""
    def description(self):
        """Return a description of the house habitat."""
        return "A house habitat."

# Abstract Factory Interface
class AbstractFactory(ABC):
    """Abstract factory interface for creating families of products."""
    @abstractmethod
    def create_animal(self) -> Animal:
        '''Create animal'''

    @abstractmethod
    def create_habitat(self) -> Habitat:
        '''Create habitat'''

# Concrete Factory Classes
class ForestFactory(AbstractFactory):
    """Concrete factory creating a family of products for a forest habitat."""
    def create_animal(self) -> Animal:
        """Create and return a Dog."""
        return Dog()

    def create_habitat(self) -> Habitat:
        """Create and return a Forest habitat."""
        return Forest()

class HouseFactory(AbstractFactory):
    """Concrete factory creating a family of products for a house habitat."""
    def create_animal(self) -> Animal:
        """Create and return a Cat."""
        return Cat()

    def create_habitat(self) -> Habitat:
        """Create and return a House habitat."""
        return House()

# Client Code
if __name__ == "__main__":
    # Create a forest habitat with a dog
    forest_factory = ForestFactory()
    forest_animal = forest_factory.create_animal()
    forest_habitat = forest_factory.create_habitat()

    print("Forest Habitat Description:", forest_habitat.description())
    print("Animal in the Forest:", forest_animal.speak())

    # Create a house habitat with a cat
    house_factory = HouseFactory()
    house_animal = house_factory.create_animal()
    house_habitat = house_factory.create_habitat()

    print("\nHouse Habitat Description:", house_habitat.description())
    print("Animal in the House:", house_animal.speak())
