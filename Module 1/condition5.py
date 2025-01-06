num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > 0 and num2 > 0:
    if num1 > num2:
        print(f"sub of numbers are {num1 - num2}")
    else:
        print(f"mul of numbers are {num2 * num1}")   

else:
    print("number is zero")