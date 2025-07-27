heading = "SIMPLE BANKING SYSTEM"
print(heading.center(125, " "))

# Base Class 
class BankAccount:
    def __init__(self, accnum, name, bal):
        self.accountnumber = accnum
        self.holdername = name
        self.balance = bal

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited. New balance: Rs.{self.balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Rs.{amount} withdrawn. New balance: Rs.{self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")

    def check_balance(self):
        print(f"Account Holder: {self.holdername}")
        print(f"Current Balance: Rs.{self.balance}")

    def bonus(self):
        bonus = 150
        self.balance += bonus
        print(f"Bonus of Rs.{bonus} added. New Balance: Rs.{self.balance}")


class SavingAccount(BankAccount):
    def __init__(self, accnum, name, bal, interest_rate):
        super().__init__(accnum, name, bal)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of Rs.{interest:.2f} applied. New balance: Rs.{self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, accnum, name, bal, overdraft_limit):
        super().__init__(accnum, name, bal)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Rs.{amount} withdrawn. New balance: Rs.{self.balance}")
            else:
                print("Withdrawal exceeds overdraft limit!")
        else:
            print("Invalid withdrawal amount")


# -------- Runtime Input --------
def create_account():
    print("\n--- Create New Account ---")
    print("1. Saving Account")
    print("2. Current Account")
    choice = input("Choose account type (1 or 2): ")

    accnum = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    bal = float(input("Enter Initial Balance: "))

    if choice == "1":
        rate = float(input("Enter Interest Rate (%): "))
        return SavingAccount(accnum, name, bal, rate)
    elif choice == "2":
        limit = float(input("Enter Overdraft Limit: "))
        return CurrentAccount(accnum, name, bal, limit)
    else:
        print("Invalid choice. Try again.")
        return create_account()

# -------- Main Loop --------
account = create_account()

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Apply Interest (Saving Account)")
    print("5. Add Bonus")
    print("6. Exit")

    option = input("Select option: ")

    if option == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif option == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif option == "3":
        account.check_balance()

    elif option == "4":
        if isinstance(account, SavingAccount):
            account.apply_interest()
        else:
            print("This option is only for Saving Accounts.")

    elif option == "5":
        account.bonus()

    elif option == "6":
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid option. Please try again.")
