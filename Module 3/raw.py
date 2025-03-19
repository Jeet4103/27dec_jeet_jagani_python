import pymysql

try:
    db = pymysql.connect(
        host="127.0.0.1", user="root", password="", database="sampledb"
    )
    print("Database connected!")
except Exception as e:
    print(e)


cr = db.cursor()
# Table Create
tbl_create = "create table studinfo(id integer primary key auto_increment, name varchar(20), city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


# Insert Data
"""insert_data = "insert into studinfo(name,city)values('sanket','rajkot'),('ashok','baroda'),('hitesh','ahmedabad'),('nirav','morbi')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

# Update Data
"""update_data = "update studinfo set name='prasiddh', city='rajkot' where id=4"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data = "delete from studinfo where id=4"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    # data = cr.fetchmany(3)
    # data = cr.fetchone()
    # print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)