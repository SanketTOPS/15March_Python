a=int(input("Enter A:"))
b=int(input("Enter B:"))


if a!=0 and b!=0: #root
    if a<b: #child
        a+=b
        print("Sum:",a)
    else:
        a*=b
        print("Mul:",a)
else:
    print("Error!Plz enter valid number.")
    
