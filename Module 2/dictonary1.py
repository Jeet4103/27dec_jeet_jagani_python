dic = {}

n = int(input("Enter the number of keys you want: "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    values = input(f"Enter values for key {i+1}: ").split(',')
    dic[key] = values

print(dic)