from tkinter import *
root = Tk()
root.title('Radio Button')


#Creating modes for radio buttons
MODES = [
    ("Red", "R"),
    ("Green", "G"),
    ("Blue", "B"),
    ("Black", "BL")
]

color = StringVar()
color.set("R")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=color, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text="Click", command=lambda:clicked(color.get())).pack()
root.mainloop()
