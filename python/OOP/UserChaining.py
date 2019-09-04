#Update your previous assignment so that each instance's methods are chained

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance =0
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User:"+self.name, "Balance:$"+ str(self.account_balance))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self



person1 = User('John','john@gmail.com')
person2 = User('Tim','tim@gmail.com')
person2.make_deposit(50)  #50
person1.make_deposit(100).make_deposit(200).transfer_money(person2,50)
person1.display_user_balance()
person2.display_user_balance()









