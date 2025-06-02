import datetime
class Transaction:
    def __init__(self, date, narration, transaction_type, amount):
        self.date = date
        self.narration = narration
        self.transaction_type = transaction_type
        self.amount = amount 
        
class Account:
    def __init__(self, name, account_no):
        self.name = name
        self._account_no = account_no
        self.transactions = []  
        self._balance = 0
        self._is_frozen = False
        self._minimum_balance = 0
        self._loan_balance = 0
    
    
    def deposit(self, amount, narration='deposit'):
        if self._is_frozen:
            return "Account is frozen can't deposit"
        if amount <= 0:
            print("Please input a positive amount.")
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date, narration, 'deposit', amount)
            self.transactions.append(new_transaction)
            self._balance += amount
            print(f"Deposited {amount} to {self.name}'s account. New balance: {self._balance}")
            print (f"Transaction Date: {new_transaction.date}")


    def withdraw(self, amount, narration='withdraw'):
        if self._is_frozen:
            return "Account is frozen cannot withdraw"
        if amount <= 0:
            print("Please input a positive amount.")
        if amount > self._balance:
            return "Insufficient funds"
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date, narration, 'withdraw', amount)
            self.transactions.append(new_transaction)
            self._balance -= amount
            print(f"{self.name} Withdrew {amount} New balance: {self._balance}")
            print (f"Transaction Date: {new_transaction.date}")   

    def transfer(self,amount,receipient_account):
        if self._is_frozen or receipient_account._is_frozen:
            return "Either of the accounts is frozen"
        if amount <= 0:
            return "transfer amount must be positive"
        if amount > self._balance:
            return "Insufficient funds."
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction (current_date,'transfer to ' + receipient_account.name,'transfer',amount)
            self.transactions.append(new_transaction)
            self._balance -= amount
            receipient_account.deposit(amount,'transfer from' + self.name)
            return f"Transferred {amount} to {receipient_account.name}  on {new_transaction.date}. Your new balance is {self._balance}"
    
    def request_loan(self,amount):
        if self._is_frozen:
            return "Account is frozen cannot request loan"
        if amount < 0:
            return "Amount must be positive"
        else:    
            self._loan_balance += amount
            self._balance += amount
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date, 'loan requested', 'loan', amount)
            self.transactions.append(new_transaction)
            return f"Loan of {amount} approved  on {new_transaction.date}. Your new balance is {self._balance}"

    def repay_loan(self, amount):
        if self._is_frozen:
            return "Account is frozen. Cannot request loan"
        if amount < 0:
            return "Amount must be positive"
        if amount < self._loan_balance:
            self._loan_balance -= amount

        current_date = datetime.datetime.now()
        if amount > self._loan_balance:
            excess_amount = amount - self._loan_balance 
            new_transaction = Transaction(current_date, 'loan repayment', 'repayment', self._loan_balance)
            self.transactions.append(new_transaction)
            self._balance += excess_amount
            self._loan_balance = 0
            return f"Loan repayment of {amount} has been settled. Excess amount of {excess_amount} has been deposited. Your new balance is {self._balance}"
        else:
            new_transaction = Transaction(current_date, 'loan repayment', 'repayment', amount)
            self.transactions.append(new_transaction)
            self._loan_balance -= amount
            return f"Loan repayment of {amount} has been settled  on {new_transaction.date}. Your new loan balance is {self._loan_balance}. Your new balance is {self._balance}"

    def change_account_owner(self,new_owner):
        if self._is_frozen:
            return "Account is frozen. Cannot change owners name"
        else:    
            self.name = new_owner
            return f"Owners name updated to {self.name}"
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,'change of owner','change', 0)
            self.transactions.append(new_transaction)
            return f"Account owner changed to {new_owner} on {new_transaction.date}"
    
    def calculate_interest(self):
        if self._is_frozen:
            return "Account is frozen cannot apply interest"
        else:
            interest = self._balance * 0.5
            self._balance += interest
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,'interest calculation','interest',0.5)
            self.transactions.append(new_transaction)
            return f"Interest of {interest} added {new_transaction.date}. New balance is {self._balance} on "

    def get_balance(self):
        current_date = datetime.datetime.now()
        new_transaction = Transaction(current_date,'balance calculation','balance',0)
        self.transactions.append(new_transaction)
        return f"Hello {self.name},your balance is {self._balance} seen on {new_transaction.date}"


    def freeze_account(self):    
        self._is_frozen = False
        current_date = datetime.datetime.now()
        new_transaction = Transaction(current_date,'freeze account','freeze',0)   
        self.transactions.append(new_transaction)
        return f"Hello {self.name} your account has been frozen"

    def unfreeze_account(self):
        self.unfreeze_account = True
        current_date = datetime.datetime.now()
        new_transaction = Transaction(current_date,'unfreeze account','unfreeze',0)   
        self.transactions.append(new_transaction)
        return f"Hello {self.name} your account has been unfrozen"


    def close_account(self):
        if self._loan_balance > 0:
            return "Cannot close account with outstanding loan."
        else:
            self._balance = 0
            self._is_frozen = True
            self._min_balance = 0
            self._loan_balance = 0
            return "Account has been closed."

    def account_statement(self):
        if not self.transactions:
            return "No transactions found."
            statement = f"Account Statement for {self.name}"
        for transaction in self.transactions:
            statement += f"Date: {transaction.date}, Narration: {transaction.narration}, Type: {transaction.transaction_type}, Amount: {transaction.amount}"
            return statement

   

          
    





            
