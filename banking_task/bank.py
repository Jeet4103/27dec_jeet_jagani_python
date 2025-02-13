import Withdrawl as wl
import deposite as dp    
import Balance as bl
import Account_detail as ad

def menu():
    is_running = True
    while is_running:
        print("\nBank Management System")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Open Account")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
               bl.show_balance()
        elif choice == '2':
            dp.Deposit()
        elif choice == '3':
            wl.withdraw()
        elif choice == '4':
            ad.account_opening()
        elif choice == '5':
            is_running = False
            print("Thank you for using the Bank Management System.")
        else:
            print("That's an invalid choice")

print("Welcome to Bank")
menu()