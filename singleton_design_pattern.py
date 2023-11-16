'''
    The Singleton pattern is a creational design pattern that ensures a class
    has only one instance and provides a global point of access to that instance.
'''
class Singleton:
    """Singleton class that ensures only one instance is created."""

    _instance = None

    def __new__(cls):
        """Override the __new__ method to control instance creation."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the singleton instance."""
        # Additional initialization can be done here if needed

    def some_method(self):
        """Example method of the singleton class."""
        return "This is a method of the Singleton class."

# Client Code
if __name__ == "__main__":
    # Creating instances of the Singleton class
    singleton_instance1 = Singleton()
    singleton_instance2 = Singleton()

    # Both instances refer to the same object
    print(f"Is instance 1 the same as instance 2? {singleton_instance1 is singleton_instance2}")

    # Using a method of the Singleton class
    result = singleton_instance1.some_method()
    print(result)
