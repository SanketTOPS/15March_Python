class student:
    stid=12
    stnm='Nirav'

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object of class
"""st=student()
st.getdata()
st.stid=56
st.stnm='Ashok'
st.getdata()"""

#Instance of class
student().getdata()
student().stid=11
student().stnm='Mitesh'
student().getdata()