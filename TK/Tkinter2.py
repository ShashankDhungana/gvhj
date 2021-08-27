from tkinter import *
top = Tk()
top.geometry("400x200")

name = Label(top, text="Name").place(x = 40,y = 60)
address = Label(top, text="Address").place(x = 40,y = 100)
contact = Label(top, text="Contact").place(x = 40,y = 140)

e1 = Entry(top).place(x = 90,y = 60)
e2 = Entry(top).place(x = 90,y = 100)
e3 = Entry(top).place(x = 90,y = 140)

top.mainloop()

