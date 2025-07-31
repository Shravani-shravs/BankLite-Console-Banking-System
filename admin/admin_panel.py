def show_all_accounts(bank):
    for acc in bank.accounts:
        print(f"ID: {acc.id}, Name: {acc.name}, Balance: ₹{acc.balance}")
