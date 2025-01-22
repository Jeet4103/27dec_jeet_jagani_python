num_tables = int(input("How many tables do you want to print? "))

for i in range(num_tables):
    table = int(input("Enter the number for the table: "))
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
