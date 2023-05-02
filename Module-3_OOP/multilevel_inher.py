class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")
    
class mitesh(nirav):
    mid=0
    msub=''

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.msub=input("Enter Mitesh's Subject:")


class tops(mitesh):
    def printdata(self):
        print("---------Nirav's Data--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("---------Mitesh's Data--------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Subject:",self.msub)
       
tp=tops()
tp.n_getdata()
tp.m_getdata()
tp.printdata()

