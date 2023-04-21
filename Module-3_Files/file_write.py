fl=open('test.txt','w')

#fl.write("Good Morning!")

if fl.writable():
    print("Yes...")
else:
    print("Error!")


