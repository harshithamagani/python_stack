#If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

#For this assignment, we'll add some functionality to the User class:

#make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
#display_user_balance(self) - have this method print the user's name and account balance to the terminal
#eg. "User: Guido van Rossum, Balance: $150
#BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance =0
    
    def make_deposit(self,amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print("User:"+self.name, "Balance:$"+ str(self.account_balance))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount



person1 = User('John','john@gmail.com')
person2 = User('Tim','tim@gmail.com')
person1.make_deposit(100)
person1.make_deposit(200) #300
person2.make_deposit(50)  #50
person1.transfer_money(person2,50)
person1.display_user_balance()
person2.display_user_balance()



