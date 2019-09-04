class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    
    
    def display_user_balance(self):
        print("User:"+self.name, "email:"+ str(self.email),"balance:$",self.account.balance)
    
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
    
    def make_deposit(self,amount):
        self.account.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

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

person1 = User('John','john@gmail.com')
person2 = User('Tim','tim@gmail.com')
person1.make_deposit(100)
person1.make_deposit(200) #300
person2.make_deposit(50)  #50
person1.transfer_money(person2,50)

person1.display_user_balance()
person2.display_user_balance()








