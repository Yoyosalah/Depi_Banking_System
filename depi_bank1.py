import random
   
def validateInput(x, valid_list):
    if x not in valid_list:
        return False
    else:
        return True

def createAccount():
    print("Creating Account:")
    name = input("Enter Name: ")
    balance = float(input("Enter Balance: "))
    checkBalance(name,balance)
    return name, balance
    
def menu(name, balance):
    while True:
        while True:
            choice = input("choices:\n1)Check Balance\n2)Deposit\n3)Withdraw\n4)Exit\n")
            flag = validateInput(choice, ["1", "2", "3", "4"])
            if not flag:
                print("Invalid input")
            else:
                break
        space()
        
        if choice == "1":
            checkBalance(name, balance)
        elif choice == "2":
            balance = deposit(name, balance)
        elif choice == "3":
            balance = withdraw(name, balance)
        elif choice == "4":
            return
        space()

def checkBalance(name, balance):
    print(f"Name: {name}\nBalance: {balance}")
    return

def deposit(name, balance):
    amount = float(input("Enter amount to deposit: "))
    while amount <= 0:
        amount = float(input("Enter a valid amount: "))
    balance += amount
    checkBalance(name, balance)
    return balance

def withdraw(name, balance):
    amount = float(input("Enter amount to withdraw: "))
    while amount > balance:
        amount = float(input("Enter a valid amount: "))
    balance -= amount
    checkBalance(name, balance)
    return balance

def space():
    print("=====================")



# Start of code (main)
Bank = ["CIB", "HSBC", "Al Ahly"]
rand = random.randint(0, len(Bank)-1)
print(f"Welcome To {Bank[rand]}\n")
while True:
    choice = input("1)Create Account\n2)Exit\n")
    flag = validateInput(choice, ["1", "2"])
    if not flag:
        print("Invalid input")
    else:
        break
space()
if choice == "1":
    name, balance = createAccount()
    space()
    menu(name, balance)
    print("Thank you for using our bank")
elif choice == "2":
    print("Thank you for using our bank")
