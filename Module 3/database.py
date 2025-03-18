import sqlite3

try:
    db = sqlite3.connect("stud.db")
    print("Database created!")
except Exception as e:
    print(e)

create_td = "create table studinfo(id integer primary key autoincrement, name text, city text)"

try:
    db.execute(create_td)
    print("Table created!")
except Exception as e:
    print(e)

n = int(input("How many records you want to enter? "))
for i in range(n):
    name = input("Enter the name: ")
    city = input("Enter the city: ")
    try:
        db.execute(f"insert into studinfo(name,city)values('{name}','{city}')")
        db.commit()
        print("Record inserte!")
    except Exception as e:
        print(e)

