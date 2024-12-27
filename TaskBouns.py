class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number


if __name__ == "__main__":
    account = BankAccount("123456789", 1000.0)
    print(f"Account Number: {account.get_account_number()}")
    print(f"Current Balance: ${account.get_balance():.2f}")
    account.deposit(200)
    account.withdraw(150)
    account.withdraw(1200)
    print(f"Final Balance: ${account.get_balance():.2f}")
