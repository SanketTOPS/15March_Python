class student:
    stid=12
    stnm='Nirav'

    def getdata(self):
        print("This is getdata.")

#Object of class
st=student()
print(st.stid)
print(st.stnm)
st.getdata()