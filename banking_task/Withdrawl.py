balance = 0.0

def withdraw():
    global balance
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
    elif amount <= 0:
        print("Amount must be greater than 0")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully")


