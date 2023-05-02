class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

st=studinfo()
#st.getdata(101,'Sanket')

stid=input("Enter ID:")
stnm=input("Enter Name:")
st.getdata(stid,stnm)