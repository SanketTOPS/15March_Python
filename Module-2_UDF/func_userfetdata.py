def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)


# static calling
#getdata(1,'nirav','python')

# Dynamic calling
"""stid=input("Enter ID:")
stnm=input("Enter name:")
stsub=input("Enter subject:")
getdata(stid,stnm,stsub)"""

n=int(input("Enter number of students:"))
for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter name:")
    stsub=input("Enter subject:")
    getdata(stid,stnm,stsub)
