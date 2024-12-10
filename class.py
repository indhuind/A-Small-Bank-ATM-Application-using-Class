class Bank:
    def __init__(self):
        self.closingBal = 0

    def display(self):
        print("Enter your options: ")
        print("1 for deposit: \n2 for withdraw: ")
        getOption = input()
        if getOption == "1":
            self.deposit()
        elif getOption == "2":
            self.withdraw()
        elif getOption != 1 or getOption != 2:
            print("thanks")
            return
        print("your closing balance:", self.closingBal)
        print("do you want to continue:")
        a = input()
        if a == "Y" or a == "y":
            self.display()
        else:
            print("thanks for visiting our bank")

    def deposit(self):
        depositAmount = int(input("enter your deposit amount:"))
        self.closinBBal = self.closingBal + depositAmount
        return self.closingBal

    def withdraw(self):
        withdrawAmount = int(input("enter your withdraw amount;"))
        if self.closingBal >= withdrawAmount:
            self.closingBal = self.closingBal - withdrawAmount
            print("after withdraw your balance amount is:", self.closingBal)
        else:
            print("no sufficient  balance")
        return self.closingBal


bankObj = Bank()
bankObj.display()
