'''
The Strategy Pattern defines a family of algorithms, encapsulates each one, and
makes them interchangeable. Strategy lets the algorithm vary independently from
clients that use it.















































+++++'''
from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    '''
    The Strategy Interface declares operations common to all supported versions
    '''
    @abstractmethod
    def pay(self, amount):
        '''
        The Context uses this method to call the algorithm defined by Concrete
        '''

# Concrete Payment Strategies
class CreditCardPayment(PaymentStrategy):
    '''
    Concrete Strategies implement the algorithm while following the base
    '''
    def pay(self, amount):
        '''
        Here goes the actual implementation of the algorithm
        '''
        print(f"Paying {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    '''
    Concrete Strategies implement the algorithm while following the base
    '''
    def pay(self, amount):
        '''
        Here goes the actual implementation of the algorithm
        '''
        print(f"Paying {amount} using PayPal")

class BankTransferPayment(PaymentStrategy):
    '''
    Concrete Strategies implement the algorithm while following the base
    '''
    def pay(self, amount):
        print(f"Paying {amount} using Bank Transfer")

# Context Class
class ShoppingCart:
    '''
    The Context defines the interface of interest to clients
    '''
    def __init__(self, payment_strategy):
        '''
            constructor method
        '''
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item):
        '''
        Usually, the Context accepts a strategy through the constructor, but also
        provides a setter to change it at runtime
        '''
        self.items.append(item)

    def checkout(self):
        '''
        The Context delegates some work to the Strategy object instead of
        '''
        total_amount = sum(item['price'] for item in self.items)
        self.payment_strategy.pay(total_amount)
        print("Items purchased:")
        for item in self.items:
            print(f"- {item['name']} (${item['price']})")

# Client Code
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
bank_transfer_payment = BankTransferPayment()

customer1_cart = ShoppingCart(credit_card_payment)
customer1_cart.add_item({'name': 'Laptop', 'price': 1200})
customer1_cart.add_item({'name': 'Mouse', 'price': 20})
customer1_cart.checkout()

customer2_cart = ShoppingCart(paypal_payment)
customer2_cart.add_item({'name': 'Smartphone', 'price': 800})
customer2_cart.checkout()

customer3_cart = ShoppingCart(bank_transfer_payment)
customer3_cart.add_item({'name': 'Headphones', 'price': 50})
customer3_cart.add_item({'name': 'Backpack', 'price': 40})
customer3_cart.checkout()
