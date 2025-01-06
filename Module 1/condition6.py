num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("choice 1: sub")
print("choice 2: mul")
print("choice 3: div")
print("choice 4: add")
choice = int(input("Enter the choice:"))

if num1 > 0 and num2 > 0:
    if choice == 1:
        print(f"sub of numbers are {num1 - num2}")
    elif choice == 2:
        print(f"mul of numbers are {num1 * num2}")
    elif choice == 3:
        print(f"div of numbers are {num1 / num2}") 
    elif choice == 4:
        print(f"add of numbers are {num1 + num2}") 
else:
    print("invalid choice")                    