# Q2. Bank Account
# Create a BankAccount class with Account Holder Name, Account Number, Balance.
# Methods: deposit(), withdraw(), display_balance().
# Conditions: Deposit must be positive and withdrawal cannot exceed balance.
class BankAccount:
    def __init__(self, account_holder_name, account_number, balance, pin):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self):
        amount = float(input("Enter amount to deposit: Rs"))

        if amount > 0:
            self.balance += amount
            print(f"\n{amount}Rs deposited successfully.")
            print(f"Current Balance: {self.balance}Rs")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: {amount}Rs"))

        if amount <= 0:
            print("Invalid amount.")

        elif amount <= self.balance:
            self.balance -= amount
            print(f"\n{amount}Rs withdrawn successfully.")
            print(f"Remaining Balance: {self.balance}Rs")

        else:
            print("Insufficient Balance!")

    def display_balance(self):
        print(f"\nCurrent Balance: {self.balance}Rs")

    def change_pin(self):
        old_pin = input("Enter current PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect current PIN.")


#Create Account

account = BankAccount(
    account_holder_name="Mohd Saqib",
    account_number="123456789",
    balance=10000,
    pin="1234"
)

# ATM

while True:

    print("\n========== WELCOME TO ATM ==========")
    print("Select Language")
    print("1. English")
    print("2. Urdu")
    print("3. Hindi")

    language = input("Enter Choice: ")

    if language not in ["1", "2", "3"]:
        print("Invalid Language Selection!")
        continue

    card = input("\nInsert Card (type 'valid'): ")

    if card.lower() != "valid":
        print("Invalid Card!")
        continue

    entered_pin = input("Enter PIN: ")

    if entered_pin != account.pin:
        print("Incorrect PIN!")
        continue

    # ATM MENU

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Change PIN")
        print("5. Help")
        print("6. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            account.deposit()

        elif option == "2":
            account.withdraw()

        elif option == "3":
            account.display_balance()

        elif option == "4":
            account.change_pin()

        elif option == "5":
            print("\nCustomer Care Number: 1234-567-890")

        elif option == "6":
            print("\nThank you for using our ATM.")
            exit()

        else:
            print("Invalid Choice!")

        # Back or Home

        while True:

            print("\nWhat would you like to do next?")
            print("1. Back to ATM Menu")
            print("2. Home Screen")
            print("3. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                break

            elif choice == "2":
                print("\nReturning to Home Screen...")
                break_home = True
                break

            elif choice == "3":
                print("\nThank you for using our ATM.")
                exit()

            else:
                print("Invalid Choice!")

        if choice == "2":
            break