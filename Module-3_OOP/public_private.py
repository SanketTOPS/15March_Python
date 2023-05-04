class studinfo:
    __stid=1
    __stnm='Nirav'

    def __getdata(self):
        print("This is getdata!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def prindata(self):
        self.__getdata()

st=studinfo()
st.prindata()