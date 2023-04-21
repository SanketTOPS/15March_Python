
fl=open('newfile.txt','a')

id=input("Enter ID:")
name=input("Enter Name:")

"""fl.write(id)
fl.write(name)"""

fl.write(f"ID:{id}\nName:{name}\n")