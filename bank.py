class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"You have successfully funded the account. The amount on the account is {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Insufficient funds")
        elif money <= self.balance:
            print(f"You have successfully withdrawn {money}. Account balance: {self.balance}")

    def all_balance(self):
        print(f"Current balance: {self.balance}")

man = Account("123456", 1000)
man.withdraw(450)
man.withdraw(1200)
man.deposit(2000)

