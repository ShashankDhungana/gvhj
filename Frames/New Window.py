from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("New Window")
root.iconbitmap("C:/Users/Omen/Desktop/A/deep.ico")
def open():
    global my_img
    top = Toplevel()
    top.title("Another Window")
    top.iconbitmap("C:/Users/Omen/Desktop/A/deep.ico")
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/Omen/Desktop/A/slack.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=quit).pack()

btn = Button(root, text="Open", command=open).pack()
root.mainloop()

