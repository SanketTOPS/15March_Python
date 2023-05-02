class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter car detail:")
        self.bal=input("Enter bank balance detail:")

class nirav(father):
    def n_printdata(self):
        print("Nirav's Car:",self.car)
        print("Nirav's Bank Balance:",self.bal)

class ashok(father):
    def a_printdata(self):
        print("Ashok's Car:",self.car)
        print("Ashok's Bank Balance:",self.bal)

a=ashok()
a.getdata()
a.a_printdata()


n=nirav()
n.n_printdata()