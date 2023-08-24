class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs. {amount} successful.")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs. {amount} successful.")
        else:
            print("Insufficient balance. Withdrawal failed.")

    def check_balance(self):
        print(f"Account balance: Rs. {self.balance}")

account = BankAccount("1234567890", 5000, "2022-01-01", "John Doe")

account.check_balance()  

account.deposit(2000) 
account.check_balance() 

account.withdraw(3000)  
account.check_balance() 
account.withdraw(5000)  
account.check_balance() 
