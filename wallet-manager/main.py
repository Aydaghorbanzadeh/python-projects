
wallet = {
    "balance": 1000
}


def show_wallet():
    print("Current balance:", wallet["balance"])


def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        wallet["balance"] += amount
        print("Deposited successfully")
    else:
        print("Invalid amount")


def withdraw():
    amount = float(input("Enter amount to withdraw: "))

    if amount > 0 and amount <= wallet["balance"]:
        wallet["balance"] -= amount
        print("Withdrawn successfully")
    else:
        print("Insufficient funds or invalid amount")


def main():
    while True:
        print("\n---- Wallet Manager ----")
        print("1. Show wallet")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_wallet()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Exit")
            break

        else:
            print("Invalid choice")


main()
