from tkinter import*
root = Tk()
root.title('Dropdown Menu')
root.iconbitmap('C:/Users/Omen/Desktop/A/deep.ico')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

#Making a list
options= [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()