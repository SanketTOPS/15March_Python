import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='testdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

# Create Table
create_tbl="create table studinfo(id integer primary key auto_increment,name text,sub text)"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('nirav','java'),('ashok','angular'),('hitesh','php'),('aarya','c++'),('pratik','react')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set name='prasiddh',sub='HTML' where id=6"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where name='sanket'"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
select_data="select * from studinfo"
try:
    cr.execute(select_data)
    #data=cr.fetchall()
    data=cr.fetchmany(3)
    #data=cr.fetchone()
    print(data)
except Exception as e:
    print(e)