class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        self.transactions = []

    def deposit(self,amount):
        self.deposits.append(amount)
        self.balance += amount
        return f"Hello {self.name}, you have deposited {amount}. Your new balance is {self.balance}"


    def withdraw(self,amount):
        if amount <= self.balance:
            self.withdrawals.append(amount)
            self.balance -= amount
            return f"Hello {self.name}, you have withdrawn {amount}. Your new balance is {self.balance}"
        else:
           return "Insufficient funds"
  
        
    def get_balance(self):
        return f"Hello {self.name}, your balance is {self.balance}"

    def transfer(self,amount,receipient_account):
        if amount <= self.balance:
            self.balance -= amount
            receipient_account.balance += amount
            return f"Hello {self.name}, you have transferred {amount} to {account2.name}. Your new balance is {self.balance}"
        else:
            return "Insufficient funds cannot transfer"

    def request_loan(self,amount):
        if amount > 0:
            self.loan_balance += amount
            return f"Hello {self.name} you have received a loan of {amount} and your current loan balance is {self.loan_balance}"
        else:
            return "Loan request denied"

    def repay_loan(self,amount):
        if amount > 0:
            self.loan_balance -= amount
            return f"Hello {self.name},you have repaid {amount} of your loan. Your loan_balance is {self.loan_balance}"
        
    def account_details(self):
        return f"Hello {self.name} your account balance is {self.balance}"


    def change_owners_name(self,new_name):
        self.name = new_name
        return f"Owners name updated to {self.name}"

    def account_statement(self):
        print("Account Statement:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: ${self.get_balance()}")
        
    def calculate_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        return f"Interest of {interest} added new balance is {self.balance}"

    def freeze_account(self):
        self.is_frozen = True
        return f"Hello {self.name} your account is frozen"

    def unfreeze_account(self):
        self.is_frozen = False
        return f"Hello {self.name} your account is unfrozen"

    def minimum_balances(self, amount):
        if amount >= 0:
            self.minimum_balance = amount
            return f"Minimum balance set to ${amount}"

    def close_account(self):
        balance = 0
        self.transactions.clear()
        return f"Account closed. All transactions have been cleared"
       


account1 = Account("Ameer")
account2 = Account("Elizabeth")
print (account1.deposit(2000))
print (account1.withdraw(200))
print (account1.get_balance())
print (account1.transfer(200,account2))
print (account1.request_loan(500))
print (account1.repay_loan(100))
print (account1.account_details())
print (account1.change_owners_name("Victoria"))
print (account1.account_statement())
print (account1.calculate_interest())
print (account1.freeze_account())
print (account1.unfreeze_account())
print (account1.minimum_balances(400))
print (account1.close_account())

   