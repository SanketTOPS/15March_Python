import tkinter
from tkinter import ttk

screen=tkinter.Tk()

screen.title("FirstApp")
screen.config(background="gold")
screen.geometry("500x600")

#tkinter.Label(text="Firstname:").pack()
#tkinter.Label(text="Lastname:").pack()

#tkinter.Label(text="Firstname:").place(x=0,y=0)
#tkinter.Label(text="Lastname:").place(x=0,y=40)

tkinter.Label(text="Firstname:",bg='gold',font='Bahnschrift 15 bold').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='gold',font='Bahnschrift 15 bold').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text="Male",bg='gold',font='Bahnschrift 15 bold').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1, text="Female",bg='gold',font='Bahnschrift 15 bold').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text="Python",bg='gold',font='Bahnschrift 15 bold').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text="JAVA",bg='gold',font='Bahnschrift 15 bold').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text="PHP",bg='gold',font='Bahnschrift 15 bold').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text="Android",bg='gold',font='Bahnschrift 15 bold').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar']

ttk.Combobox(values=city).grid(row=7,column=0)

tkinter.Button(text="Submit",font='Bahnschrift 15 bold').place(x=220,y=280)


tkinter.mainloop()
