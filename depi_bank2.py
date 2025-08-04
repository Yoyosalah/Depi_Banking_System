import random  


class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def account_info(self):
        print(f"Name:{self.name}, Balance:{self.balance}")

class Bank:
    def __init__(self,name):
        self.name = name
        print(f"Welcome To {self.name}")

    def check_balance(self,account:Account):
        account.account_info()

    def deposit(self,account:Account):
        amount = float(input("Enter amount to deposit: "))
        while amount <= 0:
            amount = float(input("Enter a valid amount: "))
        account.balance += amount
        account.account_info()
    
    def withdraw(self,account:Account):
        amount = float(input("Enter amount to withdraw: "))
        while amount > account.balance or amount <= 0:
            amount = float(input("Enter a valid amount: "))
        account.balance -= amount
        account.account_info()
    
    def create_account(self):
        print("Creating Account:")
        name = input("Enter Name: ")
        balance = float(input("Enter Balance: "))
        account = Account(name,balance)
        self.check_balance(account)
        return account
    
def menu(account:Account, bank:Bank):
    while True:
        while True:
            choice = input("choices:\n1)Check Balance\n2)Deposit\n3)Withdraw\n4)Exit\n")
            flag = validateInput(choice, ["1", "2", "3", "4"])
            if not flag:
                print("Invalid input")
            else:
                break
        
        if choice == "1":
            bank.check_balance(account)
        elif choice == "2":
            bank.deposit(account)
        elif choice == "3":
            bank.withdraw(account)
        elif choice == "4":
            print(f"Thank You For Trusting {bank.name} Bank")
            return
        
def validateInput(x, valid_list): 
    if x not in valid_list:
        return False
    else:
        return True


if __name__ == "__main__":

    banks = ["CIB", "HSBC", "Al Ahly"]
    rand = random.randint(0, len(banks)-1)
    bank = Bank(banks[rand])

    account = bank.create_account()

    menu(account,bank)


       

