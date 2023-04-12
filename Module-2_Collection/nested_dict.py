stdata={}

keys=['id','name','sub']


n=int(input("Enter number of students:"))

vl=[]

for i in range(n):
    for j in range(n):
        value=input(f"Enter values of {keys[i]}:")
    vl.append(value)
    stdata[keys[i]]=vl
        
print(stdata)