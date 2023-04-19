x=34

print("X:",x)

def getvalue():
    global x
    x=65
    print("New X:",x)

getvalue()