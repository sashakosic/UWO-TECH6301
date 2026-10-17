import os
import random
from datetime import datetime


class BankAccount(object):
    VALID_TYPES = ("chequing", "savings")
    _used_numbers = set()  # account numbers already given out in this session

    def __init__(self, name, accountType, balance=0):
        name = str(name).strip()
        accountType = str(accountType).strip().lower()

        if name == "":
            raise ValueError("The holder name can't be empty.")
        if accountType not in BankAccount.VALID_TYPES:
            raise ValueError("The account type must be 'chequing' or 'savings'.")
        if isinstance(balance, bool) or not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("The opening balance must be a number that is zero or more.")

        self.name = name
        self.accountType = accountType
        self.balance = round(float(balance), 2)

        # Generate a unique 6-digit account number whose statement file doesn't already exist
        while True:
            self.accountNumber = random.randint(100000, 999999)
            self.filename=str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
            if self.accountNumber not in BankAccount._used_numbers and not os.path.exists(self.filename):
                break
        BankAccount._used_numbers.add(self.accountNumber)

        # Create the statement file with a header, then record the opening balance
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(f"Account Number: {self.accountNumber}\n")
                file.write(f"Holder Name: {self.name}\n")
                file.write(f"Account Type: {self.accountType}\n")
                file.write("-" * 50 + "\n")
        except OSError as error:
            print(f"Error: could not create the statement file ({error}).")

        self._recordTransaction("OPEN", self.balance)

    @staticmethod
    def _isValidAmount(amount):
        return not isinstance(amount, bool) and isinstance(amount, (int, float)) and amount > 0

    def _recordTransaction(self, transactionType, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{timestamp} | {transactionType:<8} | {amount:>10.2f} | Balance: {self.balance:.2f}\n"
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(line)
        except OSError as error:
            print(f"Error: could not record the transaction ({error}).")

    def deposit(self, amount):
        if not self._isValidAmount(amount):
            print("Deposit failed: the amount must be a positive number.")
            return False
        self.balance = round(self.balance + amount, 2)
        self._recordTransaction("DEPOSIT", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if not self._isValidAmount(amount):
            print("Withdrawal failed: the amount must be a positive number.")
            return False
        if amount > self.balance:
            print(f"Withdrawal failed: insufficient funds. Your balance is ${self.balance:.2f}.")
            return False
        self.balance = round(self.balance - amount, 2)
        self._recordTransaction("WITHDRAW", amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def getBalance(self):
        return self.balance

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAccountType(self):
        return self.accountType

    def getTransactionHistory(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return "No statement file was found for this account."
        except OSError as error:
            return f"Error: could not read the statement file ({error})."


if __name__ == "__main__":
    print("--- Creating accounts ---")
    account1 = BankAccount("Alice", "chequing")
    account2 = BankAccount("Bob", "savings", 500)

    for account in (account1, account2):
        print(f"Account number: {account.getAccountNumber()}")
        print(f"Holder name: {account.getName()}")
        print(f"Account type: {account.getAccountType()}")
        print(f"Balance: ${account.getBalance():.2f}")
        print()

    print("--- Alice's transactions ---")
    account1.deposit(1000)
    account1.withdraw(250.50)
    account1.withdraw(5000)   # more than the balance: rejected
    account1.deposit(-20)     # invalid amount: rejected
    print(f"Alice's balance: ${account1.getBalance():.2f}")

    print("\n--- Bob's transactions ---")
    account2.withdraw(200)
    account2.deposit(75.25)
    print(f"Bob's balance: ${account2.getBalance():.2f}")

    print("\n--- Alice's statement ---")
    print(account1.getTransactionHistory())

    print("--- Bob's statement ---")
    print(account2.getTransactionHistory())

    print("--- Invalid account type ---")
    try:
        BankAccount("Carol", "business")
    except ValueError as error:
        print(f"Could not create account: {error}")