class BankAccount:
    def __init__(self,Account_number,Account_Holder_Name,Balances):
        self.Account_number=Account_number
        self.Account_Holder_Name=Account_Holder_Name
        self.Balances=Balances
    def deposit(self,amount):
        if amount>0:
            self.Balances +=amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposited amount") 
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid withdraw amount")
        elif amount>self.Balances:
            print("Insufficent Balances")
        else:
            print("amount withdraw successfully")    

    def check_balances(self):
        print("current balances:",self.Balances)

account=BankAccount("ACC101", "Anil", 5000)
while True:
    print("\n========Menu=========")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check_balances")
    print("4.Exist")
    choice=int(input("enter a choice:"))
    if choice==1:
        amount=float(input("enter deposit amount:"))
        account.deposit(amount)
    elif choice==2:
        amount=float(input("enter withdraw amount:"))
        account.withdraw(amount)
    elif choice==3:
        account.check_balances()
    elif choice==4:
        print("Thank You Visit Again") 
        break
    else:
        print("invaild choice")               
