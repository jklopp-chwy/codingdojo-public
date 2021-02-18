class User:
        def __init__(self, username, email_address):
            self.name = username
            self.email = email_address
            self.account = BankAccount(int_rate=0.02, balance=0)

        def make_deposit(self, amount):
            self.account.balance += amount
            return self

        def make_withdrawl(self, amount):
            self.account.balance -= amount
            return self

        def make_yield_interest(self):
            self.account.balance = (self.account.balance * self.account.int_rate) + self.account.balance
            return self

        def display_user_balance(self):
            print(f"User: {self.name}, Balance: ${self.account.balance}")
            return self

        def transfer_money(self, amount, account_from, account_to):
            account_from.account.balance -= amount
            account_to.account.balance += amount
            return
            
class BankAccount:
        def __init__(self, int_rate, balance):
            self.int_rate = int_rate
            self.balance = balance


###Stuff###

jeff = User("jeff", "jeff@python.com").make_deposit(10).display_user_balance().make_yield_interest().display_user_balance()

