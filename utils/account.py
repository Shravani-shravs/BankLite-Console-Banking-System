import datetime

class Account:
    def __init__(self, acc_id, name, balance=0.0):
        self.id = acc_id
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive."
        self.balance += amount
        self.transactions.append(f"{datetime.datetime.now()} - Deposited ₹{amount:.2f}")
        return "Deposit successful."

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transactions.append(f"{datetime.datetime.now()} - Withdrew ₹{amount:.2f}")
        return "Withdrawal successful."

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }

    @classmethod
    def from_dict(cls, data):
        acc = cls(data['id'], data['name'], data['balance'])
        acc.transactions = data.get('transactions', [])
        return acc
