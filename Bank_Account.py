class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance is: ", self.balance)

    def Withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful. New balance is: ", self.balance)
        else:
            print("Insufficient balance.")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print("Bank fees of 5% have been applied. New balance is: ", self.balance)

    def display(self):
        print("Account details:\nAccount number: {}\nAccount owner: {}\nBalance: {}".format(self.accountNumber, self.name, self.balance))

my_account = BankAccount(input('Account number '), input('Enter Name'), 5000)


my_account.display()
my_account.Deposit(1000)
my_account.Withdrawal(2000)
my_account.bankFees()
