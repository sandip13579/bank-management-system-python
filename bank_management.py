class Account:
    def __init__(self,acc_no,pin,balance=0):
        self.acc_no = acc_no
        self.__pin = pin
        self.__balance = balance

    def check_pin(self,pin):
        if self.__pin == pin:
            return True
        else:
            print("Wrong Pin...")
            return False
    
    def balance_details(self):
        return self.__balance

    def deposit(self,amount):
            if amount > 0:
                self.__balance+= amount 
                print("New Balance is:",self.__balance)
            else:
                print("Invalid Amount")
    
    def withdraw(self,amount):
        if amount < 0:
            print("Invalid Amount!!")
        elif amount <= self.__balance:
            self.__balance-=amount
            print("Withdrawal Successfull...")
        else:
            print("Insufficient Balance...")

class Bank:
    def __init__(self):
        self.accounts = []
    
    def create_account(self,acc_no,pin):
            if  self.find_account(acc_no):
                print("Account already exists...")
            else:
                acc = Account(acc_no,pin)
                self.accounts.append(acc)
                print("Account has been created successfully...")
    
    def find_account(self,acc_no):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
        return None

bnk = Bank()

acc1 = Account(12345,9999)
acc2 = Account(6789,1111)

bnk.accounts.append(acc1)
bnk.accounts.append(acc2)

while True:
    print("\nBANKING MENU-:")
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Show Balance")
    print("5.Find Account")
    print("6.Exit")

    choice = int(input("Enter any choice-:"))
    if choice == 1:
        acc_no = int(input("Enter account number-:"))
        pin = int(input("Enter pin number-:"))
        bnk.create_account(acc_no,pin)
    
    elif choice == 2:
        acc_no = int(input("Enter account number-:"))
        acc = bnk.find_account(acc_no)

        if acc:
            PIN = int(input("Enter PIN No-:"))
            if acc.check_pin(PIN):
                amount = int(input("Enter amount-:"))
                acc.deposit(amount)
            else:
                print("Wrong PIN...")
        else:
            print("Account not Found...")
    
    elif choice == 3:
        acc_no = int(input("Enter account number-:"))
        acc = bnk.find_account(acc_no)

        if acc:
            PIN = int(input("Enter PIN No-:"))
            if acc.check_pin(PIN):
                amount = int(input("Enter amount-:"))
                acc.withdraw(amount)
            else:
                print("Wrong PIN...")
        else:
            print("Account not Found...")

    elif choice == 4:
        acc_no = int(input("Enter account number-:"))
        acc = bnk.find_account(acc_no)

        if acc:
            PIN = int(input("Enter PIN-:"))
            if acc.check_pin(PIN):
                print("Balance in your account is-:",acc.balance_details())
            else:
                print("Wrong PIN...")
        else:
            print("Account not found")
        
    elif choice == 5:
        acc_no = int(input("Enter account number-:"))
        acc = bnk.find_account(acc_no)
        
        if acc:
            print("Account has been found...")
        else:
            print("Account not found...")
            ch = input("Do you want to add an account in our bank(y/n):")
            if ch.lower() == "y":
                acc_no = int(input("Enter account number:"))
                pin = int(input("Enter pin number-:"))
                bnk.create_account(acc_no,pin)
            else:
                print("Back to menu")

    elif choice == 6:
        print("Exit.....")
        break