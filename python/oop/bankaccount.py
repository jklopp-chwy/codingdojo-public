class BankAccount:
        def __init__(self, int_rate, balance):
            self.int_rate = int_rate
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            return self

        def withdrawl(self, amount):
            self.balance -= amount
            return self

        def display_account_info(self):
            print(f"Account Balance: ${self.balance}, Interest Rate: %{self.int_rate*100}")
            return self
        
        def yield_interest(self):
            self.balance = (self.balance * self.int_rate) + self.balance
            return self

###Stuff###

account123 = BankAccount(.01,100)
account456 = BankAccount(.025,50)

account123.deposit(50).deposit(25).deposit(25).yield_interest().display_account_info()
account456.deposit(20).deposit(20).withdrawl(5).withdrawl(5).withdrawl(5).withdrawl(5).yield_interest().display_account_info()