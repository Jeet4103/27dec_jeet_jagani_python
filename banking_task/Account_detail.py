account_details = {}
def account_opening():
    global account_details
    account_number = input("Enter account number: ")
    holder_name = input("Enter account holder name: ")
    account_type = input("Enter account type (e.g., Savings, Current): ")

    if not account_number.isdigit():
        print("Invalid account number. It should contain only digits.")
        return
    if not holder_name.replace(" ", "").isalpha():
        print("Invalid holder name. It should contain only letters.")
        return

    account_details = {
        "Account Number": account_number,
        "Holder Name": holder_name,
        "Account Type": account_type
    }
    print("Account opened successfully")
    print(f"Account Details: {account_details}")
