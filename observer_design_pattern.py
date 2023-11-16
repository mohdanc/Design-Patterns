'''
    Observer Design Pattern
    The Observer Pattern defines a one-to-many dependency between objects so that
    when one object changes state, all of its dependents are notified and updated
'''
from abc import ABC, abstractmethod

class Observer(ABC):
    """Observer interface."""
    @abstractmethod
    def update(self, message):
        """Update method to be implemented by concrete observers."""

class ConcreteObserver(Observer):
    """Concrete observer implementation."""
    def __init__(self, name):
        """Initialize the concrete observer with a name."""
        self.name = name

    def update(self, message):
        """Print the received message."""
        print(f"{self.name} received message: {message}")

class Subject:
    """Subject being observed."""
    def __init__(self):
        """Initialize the subject with an empty list of observers."""
        self.observers = []

    def add_observer(self, observer):
        """Add an observer to the list."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Remove an observer from the list."""
        self.observers.remove(observer)

    def notify_observers(self, message):
        """Notify all observers with a message."""
        for observer in self.observers:
            observer.update(message)

# Client Code
if __name__ == "__main__":
    # Create subject
    subject = Subject()

    # Create observers
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    # Attach observers to the subject
    subject.add_observer(observer1)
    subject.add_observer(observer2)

    # Notify observers about a change
    subject.notify_observers("Hello, observers!")

    # Remove one observer
    subject.remove_observer(observer1)

    # Notify remaining observers
    subject.notify_observers("Observer 1 is removed.")
