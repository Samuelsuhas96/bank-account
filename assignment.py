class Bank_Account():
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
    def withdraw(self, amount):
        if(amount>self.balance):
            print(f"insufficient funds, Available balance is: {self.balance}")
        else:
            self.balance-=amount
            print(f"Available balance after withdrawal: {self.balance}")

    def deposit(self, amount):
        self.balance+=amount
        print(f"Available balance after depositing: {self.balance}")
account = Bank_Account("Samuel Suhas Bellapu", 10)
print(f"Account details, name:{account.name}, available balance:{account.balance}")
def switch():
    while(True):
        print("Enter A to Deposit\nEnter B to Withdraw \nEnter C to Exit ")
        option = str(input("You have chosen option : "))
        if option == "A":
            amount=(int(input("enter the amount to be deposited: ")))
            account.deposit(amount)
            continue
        elif option == "B":
            amount=(int(input("enter the amount to be withdrawn: ")))
            account.withdraw(amount)
            continue
        elif option == "C":
            print("Thank You")
            break
        else:
            print("Select one of the given options")
switch()