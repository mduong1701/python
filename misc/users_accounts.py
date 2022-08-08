class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def new_account(self, rate, balance):
        self.accounts.append(BankAccount(rate, balance))

    def make_deposit(self, account_index, amount):
        self.accounts[account_index].deposit(amount)

    def make_withdrawal(self, account_index, amount):
        self.accounts[account_index].withdraw(amount)

    def display_user_balance(self, account_index):
        self.accounts[account_index].display_account_info()

    def transfer_money(self, amount, other_user):
        self.accounts[0].balance -= amount
        other_user.accounts[0].balance += amount

class BankAccount:

    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

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

man = User("Man", "man@man.com")
man.new_account(0.1, 9000)
mike = User("Mike", "mike@mike.com")
mike.new_account(0.07, 20000)
man.display_user_balance(0)
mike.display_user_balance(0)
man.transfer_money(500, mike)
man.display_user_balance(0)
mike.display_user_balance(0)