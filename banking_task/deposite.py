def Deposit():
    global balance
    amount = float(input("Enter amount to be deposited: "))
    if amount <= 0:
        print("Amount must be greater than 0")
    else:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully")