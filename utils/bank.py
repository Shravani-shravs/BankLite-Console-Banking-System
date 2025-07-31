from utils.account import Account

class Bank:
    def __init__(self):
        self.accounts = []
        self.last_id = 1000

    def create_account(self, name, initial_balance=0.0):
        self.last_id += 1
        acc = Account(self.last_id, name, initial_balance)
        self.accounts.append(acc)
        return acc

    def find_account_by_id(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                return acc
        return None

    def to_dict_list(self):
        return [acc.to_dict() for acc in self.accounts]

    def load_from_list(self, data_list):
        self.accounts = [Account.from_dict(d) for d in data_list]
        if self.accounts:
            self.last_id = max(acc.id for acc in self.accounts)
