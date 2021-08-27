from tkinter import *

root = Tk()
root.title("Slider")
root.iconbitmap('C:/Users/Omen/Desktop/A/deep.ico')

#Vertical Slider

vertical = Scale(root, from_=0, to=450)
vertical.pack()

#Horizontal Slider

horizontal = Scale(root, from_=0, to=450, orient = HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=horizotal.get()).pack()
    root.geometry(str(horizontal.get() + "x" + str(vertical.get()))

my_btn = Button(root, text="Click to re-align", command=slide).pack()
root.mainloop()

