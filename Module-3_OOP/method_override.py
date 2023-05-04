class studninfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class otherstudent(studninfo):
   def getdata(self, id, name):
       return super().getdata(id, name)
    

st=studninfo()
ot=otherstudent()

st.getdata(101,'Sanket')
ot.getdata(102,'Nirav')
