
from abc import ABC, abstractmethod # abstract base class module
class dinner (ABC):
    def bill(self, amount):
        print("Your total today: ",amount)
    @abstractmethod # defining method without implementation (pass)
    def payment(self,amount):
        pass

class GiftCardPayment(dinner):
    def payment(self, amount): # utilizing the abstract method
        print("Your purchase of {} exceeded the balance of your gift card.".format(amount))

obj = GiftCardPayment()
obj.bill("$200")
obj.payment("$200")
