'''
    The Factory Method pattern is a creational design pattern that provides an interface
    for creating objects in a superclass but allows subclasses to alter the type of objects
    that will be created. It is a way to delegate the responsibility of instantiating objects
    to its subclasses.
'''
from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    """The Product interface that declares the method 'speak'."""
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    """A Concrete Product representing a Dog."""
    def speak(self):
        """Return the sound a dog makes."""
        return "Woof!"

class Cat(Animal):
    """A Concrete Product representing a Cat."""
    def speak(self):
        """Return the sound a cat makes."""
        return "Meow!"

# Creator Interface
class AnimalCreator(ABC):
    """The Creator interface that declares the method 'create_animal'."""
    @abstractmethod
    def create_animal(self):
        '''
            create animal
        '''

    def speak(self):
        """Use the created animal to get its sound."""
        animal = self.create_animal()
        return animal.speak()

# Concrete Creators
class DogCreator(AnimalCreator):
    """A Concrete Creator for creating Dog objects."""
    def create_animal(self):
        """Create and return a Dog."""
        return Dog()

class CatCreator(AnimalCreator):
    """A Concrete Creator for creating Cat objects."""
    def create_animal(self):
        """Create and return a Cat."""
        return Cat()

# Client Code
if __name__ == "__main__":
    # Create a dog using DogCreator
    dog_creator = DogCreator()
    dog = dog_creator.create_animal()
    print("Dog says:", dog.speak())

    # Create a cat using CatCreator
    cat_creator = CatCreator()
    cat = cat_creator.create_animal()
    print("Cat says:", cat.speak())
