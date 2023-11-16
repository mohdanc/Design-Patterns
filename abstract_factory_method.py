'''
    The Abstract Factory pattern is another creational design pattern that provides an interface
    for creating families of related or dependent objects without specifying their concrete classes.
    This pattern involves multiple interfaces, each representing a family of related products.
'''

from abc import ABC, abstractmethod

# Abstract Product Interfaces
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Habitat(ABC):
    @abstractmethod
    def description(self):
        pass

# Concrete Product Classes
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Forest(Habitat):
    def description(self):
        return "A forest habitat."

class House(Habitat):
    def description(self):
        return "A house habitat."

# Abstract Factory Interface
class AbstractFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

    @abstractmethod
    def create_habitat(self) -> Habitat:
        pass

# Concrete Factory Classes
class ForestFactory(AbstractFactory):
    def create_animal(self) -> Animal:
        return Dog()

    def create_habitat(self) -> Habitat:
        return Forest()

class HouseFactory(AbstractFactory):
    def create_animal(self) -> Animal:
        return Cat()

    def create_habitat(self) -> Habitat:
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
