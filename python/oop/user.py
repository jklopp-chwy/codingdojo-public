class User:
        def __init__(self, username, email_address):
            self.name = username
            self.email = email_address
            self.account_balance = 0

        def make_deposit(self, amount):
            self.account_balance += amount
            return self

        def make_withdrawl(self, amount):
            self.account_balance -= amount
            return self

        def display_user_balance(self):
            print(f"User: {self.name}, Balance: ${self.account_balance}")
            return self

        def transfer_money(self, amount, account_from, account_to):
            account_from.account_balance -= amount
            account_to.account_balance += amount
            return

jeff = User("jeff Python", "jeff@python.com")
jeff.make_deposit(100).make_deposit(10).make_deposit(15).make_withdrawl(50).display_user_balance()
# jeff.make_deposit(10)
# jeff.make_deposit(15)
# jeff.make_withdrawl(50)
# jeff.display_user_balance()

sally = User("sally python", "sally@python.com")
sally.make_deposit(10).make_deposit(15).make_withdrawl(5).make_withdrawl(1).display_user_balance()
# sally.make_deposit(15)
# sally.make_withdrawl(5)
# sally.make_withdrawl(1)
# sally.display_user_balance()

kevin = User("Kevin Bacon", "kevin@bacon.com")
kevin.make_deposit(10).make_withdrawl(5).make_withdrawl(5).make_withdrawl(5).display_user_balance()
# kevin.make_withdrawl(5)
# kevin.make_withdrawl(5)
# kevin.make_withdrawl(5)
# kevin.display_user_balance()

jeff.transfer_money(10, jeff, kevin)
jeff.display_user_balance()
kevin.display_user_balance()