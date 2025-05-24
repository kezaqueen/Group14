class Account():
    def __init__(self, owner,initial_balance=0, min_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.min_balance = min_balance
        self.transactions = []
        self.loan_balance = 0
        self.frozen = False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited:{amount}")
            return f"Confirmed. Deposit successful. Your new balance is {self.balance}"
        return "Deposit amount must be positive"
    

    def withdraw(self, amount):
        if self.frozen:
            return "Your account is frozen. Cannot withdraw."
        if amount > 0 and self.balance - amount >= self.min_balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            return f"Confirmed. Withdaral successful.Your new balance is {self.balance}"
        return "Insufficient balance to withdraw"
    
    def transfer_funds(self, amount, recipient_account):
        if self.frozen: return "Your accunt is frozen. Cannot transfer funds"
        if amount > 0 and self.balance - amount >= self.min_balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(f"Confirmed. Transfered {amount} to {recipient_account.owner}")
            recipient_account.transactions.append(f"Confirmed. You have received {amount} from {self.owner}")
            return f"Transfer successful. Your new balance is {self.balance}"
        return "Insufficient amount"
    

    def get_balance(self):
        return f"Your current balance is {self.balance}"
    

    def request_loan(self, amount):
        if amount > 0:
            self.loan_balance += amount
            self.transactions.append(f"Loan requested: {amount}")
            return f"Confirmed. Your loan request of {amount} approved"
        return "Low loan amount"
    

    def repay_loan(self, amount):
        if amount > 0 and amount <= self.loan_balance:
            self.loan_balance -= amount
            self.transactions.append(f"Loan repaid: {amount}")
            return f"Confirmed. Loan repayment successful. Your remaining loan is {self.balance}"
        return "Invalid amount"
    

    def view_account_details(self):
        return f"Account owner: {self.owner} : {self.loan_balance}"
    

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner has successfully been changed to {new_owner}"
    

    def account_statement(self):
        return self.transactions.join()
    

    def interest_calculation(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest: {interest}")
        return f"New balance: {self.balance}"
    
    def freeze_account(self):
        self.frozen = True
        return "Your account has been frozen"
    

    def unfreeze_account(self):
        self.frozen = False
        return "Your account has been unfrozen"
    

    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.min_balance = amount
            return f"Minimum balance successfully set to {amount}"
        return "Negative minimum balance"
    

    def close_account(self):
        self.balance = 0
        self.loan_balance = 0
        self.transactions = []
        return "Your account has been successfully closed"
    