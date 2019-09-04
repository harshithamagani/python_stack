#Create a BankAccount class with the attributes interest rate and balance
#Add a deposit method to the BankAccount class
#Add a withdraw method to the BankAccount class
#Add a display_account_info method to the BankAccount class
#Add a yield_interest method to the BankAccount class
#Create 2 accounts
#To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
#To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    
    def display_user_balance(self):
        print("User:"+self.name, "email:"+ str(self.email))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

class BankAccount:
    def __init__(self,balance=0,interest=0.02):
        self.balance=balance
        self.interest=interest
    
    def make_deposit(self,amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def yield_interest(self):
        self.balance += (self.balance * self.interest)
        return self
    
    def display_user_balance(self):
        print("Balance:$"+ str(self.balance))


johnAccount = BankAccount()
timAccount =  BankAccount()

johnAccount.make_deposit(100).make_deposit(50).make_deposit(50).make_withdrawal(20).yield_interest()
timAccount.make_deposit(100).make_deposit(100).make_withdrawal(50).yield_interest()

johnAccount.display_user_balance()
timAccount.display_user_balance()







