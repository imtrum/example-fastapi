
class InsufficientFunds(Exception):
    pass
def add(nums1: int,nums2: int):
    return nums1 + nums2


def subtract(nums1:int , nums2: int):
    return nums1 - nums2

class BankAccount():
    def __init__(self,starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
            self.balance  += amount

    def withdraw(self, amount):
            if amount > self.balance:
                 raise InsufficientFunds("Insufficient funds in account")
            self.balance  -= amount 

    def collect_interest(self, amount):
                self.balance  *= 1.1
    


