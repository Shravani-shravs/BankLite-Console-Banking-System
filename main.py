from utils import storage, auth
from utils.bank import Bank

USER_FILE = "users.json"

def main():
    bank = Bank()
    users = storage.load_users(USER_FILE)

    print("==== Welcome to BankLite ====")
    name = input("Enter your name: ").strip()

    user_id = auth.login(users, name)
    if user_id:
        print(f"Welcome back, {name}! (ID: {user_id})")
    else:
        user_id = auth.register(users, name)
        print(f"Account created for {name}. Your ID is {user_id}")

    while True:
        print("\n--- Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. View Transactions")
        print("6. Save & Exit")
        choice = input("Choose option: ")

        if choice == "1":
            initial = float(input("Enter initial balance: "))
            acc = bank.create_account(name, initial)
            print(f"Account created! ID: {acc.id}")

        elif choice in ("2", "3", "4", "5"):
            acc_id = int(input("Enter your Account ID: "))
            acc = bank.find_account_by_id(acc_id)
            if not acc:
                print("Account not found.")
                continue

            if choice == "2":
                amt = float(input("Enter deposit amount: "))
                print(acc.deposit(amt))
            elif choice == "3":
                amt = float(input("Enter withdrawal amount: "))
                print(acc.withdraw(amt))
            elif choice == "4":
                print(f"Balance: ₹{acc.balance:.2f}")
            elif choice == "5":
                print("Transaction History:")
                for tx in acc.transactions:
                    print(" -", tx)

        elif choice == "6":
            storage.save_users(USER_FILE, users)
            print("Users saved.")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
