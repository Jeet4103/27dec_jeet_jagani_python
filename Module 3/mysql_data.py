import pymysql

try:
    db = pymysql.connect(
        host="127.0.0.1", user="root", password="", database="sampledb"
    )
    print("Database connected!")
except Exception as e:
    print(e)

cr = db.cursor()


tbl_create = "create table studinfo(id integer primary key auto_increment, name varchar(20), city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

def insert():
    n = int(input("How many records you want to enter? "))
    for i in range(n):
        name = input("Enter the name: ")
        city = input("Enter the city: ")
        try:
            query = f"INSERT INTO studinfo (name, city) VALUES ('{name}', '{city}')"
            cr.execute(query)
            db.commit()
            print("Record inserted!")
        except Exception as e:
            print(f"Error: {e}")


def Update():
    id = input("Enter the ID to update: ")
    name = input("Enter the new name: ")
    city = input("Enter the new city: ")
    try:
        cr.execute(f"UPDATE studinfo SET name={name}, city={city} WHERE id={id}")
        db.commit()
        print("Record updated!")
    except Exception as e:
        print(e)

def Delete():
    id_to_delete = input("Enter the ID to delete: ")
    try:
        cr.execute(f"DELETE FROM studinfo WHERE id={id_to_delete}")
        db.commit()
        print("Record deleted!")
    except Exception as e:
        print(e)

def View():
    show_data = "SELECT * FROM studinfo"
    try:
        cr.execute(show_data)
        data = cr.fetchall()
        for record in data:
            print(record)
    except Exception as e:
        print(e)

def main():
    is_running = True
    while is_running:
        print("\nWelcome to the database")
        print("1. Insert data")
        print("2. Update data")
        print("3. Delete data")
        print("4. View data")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            insert()
        elif choice == "2":
            Update()
        elif choice == "3":
            Delete()
        elif choice == "4":
            View()
        elif choice == "5":
            is_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main() 
