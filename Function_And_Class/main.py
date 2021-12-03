class Account:
    accountNumber = 0
    accountHolderName = " "
    balance = 0.0

    def __init__(self, no, name, bal):
        self.accountNumber = no
        self.accountHolderName = name
        self.balance = bal

    def getName(self):
        return self.accountHolderName

    def setName(self, name):
        self.accountHolderName = name

    def getAccNo(self):
        return self.accountNumber

    def setAccNo(self, no):
        self.accountNumber = no

    def getBal(self):
        return self.balance

    def setBal(self, bal):
        self.balance = bal

    def details(self):
        print("Account Number:", self.accountNumber, "Name:", self.accountHolderName, "Balance:", self.balance)

    def deposit(self, amount):
        print("\nAfter Deposit: ")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount or self.balance == 0:
            print("\nInsufficient balance")
        else:
            print("\nAfter Withdraw: ")
            self.balance = self.balance - amount


a1 = Account(1, "A", 1100)
a2 = Account(2, "B", 1200)
a3 = Account(3, "C", 1300)
a4 = Account(4, "D", 1400)
a5 = Account(5, "E", 1500)

Account = [a1, a2, a3, a4, a5]

for x in Account:
    x.details()

a2.deposit(500)
a2.details()

a5.withdraw(1000)
a5.details()

