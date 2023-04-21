fl=open('temp.txt','r+')

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[2])
#print(fl.readlines()[0:5])

fl.write("\nHello Students")

"""for i in fl:
    print(i)"""

"""if fl.readable():
    print("Yes...")
else:
    print("Error!")
"""