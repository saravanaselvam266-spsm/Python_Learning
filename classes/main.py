'''Sum 1 - Create a class BankAccount with attributes name and balance.
Add methods deposit(amount) and withdraw(amount) that update the balance and showbalance().
Prevent withdrawal if the balance is less than the amount and print a warning message.
Create two BankAccount objects and try deposit and withdraw money from the account
Bonus: simulate a transfer(amount, to_account) method to transfer between two bank accounts'''

class BankAccount :
    # Constructor
    def __init__ (self,name,balance):
        self.name = name
        self.balance = balance

    # Methods 
    def deposit(self,amount):
        self.balance += amount
        print("Deposit successfully",self.balance)
        

    def withdraw(self,amount):
        if self.balance < amount :
            print(f"Your balance is {self.balance} so you can't withdraw {amount}")
        else :
            self.balance-= amount
            print(self.balance)
        
    def transfer(self,amount,to_person):
        if self.balance < amount :
            print(f"You can't transfer this amount {amount} because your balance is {self.balance}")
        else :
            self.balance -= amount
            to_person.balance += amount
            print("Your transfer is successfully")
    def show_balance(self):
        return print(f"Your balance :{self.balance}")


user1=BankAccount("Paul",10000)
user2=BankAccount("rohi",1000)


user1.deposit(2000)
user1.withdraw(4000)
user2.deposit(5000)
user2.withdraw(4000)
user1.transfer(200,user2)

user1.show_balance()
user2.show_balance()
user1.transfer(4000,user2)
user1.show_balance()
user2.show_balance()

# -----------------------------------------------------------------

'''Sum - 2  Create a class LibraryBook with attributes title, author, and available_copies.
Add the following methods:
borrow_book() → Decreases available copies by 1 if available.
If no copies are left, print “Book not available!”
return_book() → Increases available copies by 1.
show_status() → Displays the title, author, and available copies.
Create two LibraryBook objects and simulate borrowing and returning books.
Example Output:

Book borrowed: Harry Potter
Available copies: 2
Book borrowed: Harry Potter
Available copies: 1
Book not available!'''