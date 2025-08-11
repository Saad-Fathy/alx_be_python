class BankAccount:
    def __init__(self,account_balance=0):
        self.balance = account_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        
    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= 0:
            return True
            self.balance -= amount
        
    def display_balance(self):
        print(f"Current Balance:{self.balance}")
        
    