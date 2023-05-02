class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter car detail:")
        self.bal=input("Enter bank balance detail:")

class son(father):
    def printdata(self):
        print("Car:",self.car)
        print("Bank Balance:",self.bal)


sn=son()
sn.getdata()
sn.printdata()

