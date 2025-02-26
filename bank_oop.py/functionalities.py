class Details:
        account_number = None
        name = None
        account_type = None
        balance = 0

class CreateAccount(Details):
    def create_account(self):
        self.account_number = input("Enter your account number: ")
        self.name = input("Enter your name: ")
        self.account_type = input("Enter your account type (Savings/Current): ")
        while True:
            self.balance = int(input("Enter your initial balance (Minimum amount should be 2000): "))
            if self.balance >= 2000:
                break
            print("Initial balance must be at least 2000")

class Deposit(CreateAccount):
    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print(f"Deposit successful! Your new balance is {self.balance}")

class Withdraw(Deposit):
    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Your new balance is {self.balance}")

class Display(Withdraw):
    def display(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")


ban = Display()

while True:
    print("\nMenu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        cus.create_account()
    elif choice == '2':
        if cus.account_number:
            cus.deposit()
        else:
            print("No account found! Please create an account first.")
    elif choice == '3':
        if cus.account_number:
            cus.withdraw()
        else:
            print("No account found! Please create an account first.")
    elif choice == '4':
        if cus.account_number:
            cus.display()
        else:
            print("No account found! Please create an account first.")
    elif choice == '5':
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice! Please try again.")
