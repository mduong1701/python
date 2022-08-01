class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $", self.balance)
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def print_instances(cls):
        for account in cls.accounts:
            print("Balance: $", account.balance, ". Interest rate: ", account.int_rate * 100, "%.")



account_1 = BankAccount(0.07, 1000)
account_2 = BankAccount(0.05, 2000)

account_1.deposit(100).deposit(200).deposit(300).withdraw(1200).yield_interest().display_account_info()
account_2.deposit(500).deposit(800).withdraw(1000).withdraw(1200).yield_interest().display_account_info()

BankAccount.print_instances()