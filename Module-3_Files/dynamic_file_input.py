filenm=input("Enter your file name:")
flmode=input("Enter your file mode:")

fl=open(filenm,flmode)

def getdata():
    id=input("Enter ID:")
    name=input("Enter Name:")
    sub=input("Enter Subject:")
    fl.write(f"ID:{id}\nName:{name}\nSubject:{sub}\n")

n=int(input("Enter number of students:"))

for i in range(n):
    getdata()




