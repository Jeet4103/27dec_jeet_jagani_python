Full_name = input("Enter your full name: ")
Age = input("Enter your age: ")
Mobile_number = input("Enter your mobile number: ")
Password = input("Enter your password: ")
confirm_password = input("Enter your confirm password: ")

if Full_name.isalpha() and Age.isdigit() and Mobile_number.isdigit() and len(Mobile_number) == 10 and Password.isalnum() and confirm_password.isalnum() and Password == confirm_password:
    print("Full Name:", Full_name)
    print("Age:", Age)
    print("Mobile Number:", Mobile_number)
    print("Password:", Password)
else:
    print("Please enter valid input")