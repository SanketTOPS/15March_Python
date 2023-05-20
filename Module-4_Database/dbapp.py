import sqlite3

try:
    dbcon=sqlite3.connect("demodb.db")
    print("Database connected!")
except Exception as e:
    print(e)


# Create Table
create_tbl="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('nirav','java'),('ashok','angular'),('hitesh','php'),('aarya','c++'),('pratik','react')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


# Update Data
"""update_data="update studinfo set name='prasiddh',sub='HTML' where id=12"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where name='sanket'"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

cr=dbcon.cursor()

# Show Data
select_data="select * from studinfo"
try:
    cr.execute(select_data)
    data=cr.fetchall()
    #data=cr.fetchmany(6)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)
    