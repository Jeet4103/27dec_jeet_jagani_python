def getdata(students):
    for i in range(n):
        print("ID:", students["id"][i],"Name:", students["name"][i])

n = int(input("How many student's data you want to enter:"))

students = {
    "id": [],
    "name": []
}

for i in range(n):
    id = int(input("Enter ID:"))
    name = input("Enter Name:")
    students["id"].append(id)
    students["name"].append(name)

getdata(students)
