sub1 = int(input("Enter the marks of subject 1:"))
sub2 = int(input("Enter the marks of subject 2:"))
sub3 = int(input("Enter the marks of subject 3:"))
sub4 = int(input("Enter the marks of subject 4:"))

total = sub1 + sub2 + sub3 + sub4

percentage = total / 4

if percentage > 70:
    print("You have got A+ grade") 

elif percentage > 60:
    print("You have got A grade") 

elif percentage > 50:
    print("You have got B grade") 

elif percentage > 40:
    print("You have got C grade")

else:
    print("Your failed")
