def getdata(*data):
    for i in range(n):
        print("ID:", data[0][i],"Name:", data[1][i])    

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

getdata(students["id"], students["name"])