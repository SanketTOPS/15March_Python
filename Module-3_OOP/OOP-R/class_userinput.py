class studinfo:
    stid=0
    stnm=''

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")
    
    def printdata(self):
        #print("ID:",self.stid)
        #print("Name:",self.stnm)
        print(f"ID:{self.stid}\nName:{self.stnm}")

st=studinfo()
st.getdata()
st.printdata()