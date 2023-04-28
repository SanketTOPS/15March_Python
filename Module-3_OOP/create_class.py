class studinfo:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("This is getdata.")

# Object of class
st=studinfo() #object
#print(st.stid)
#print(st.stnm)    
print("ID:",st.stid)
print("Name:",st.stnm)
st.getdata()